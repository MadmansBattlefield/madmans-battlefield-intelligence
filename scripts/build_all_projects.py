#!/usr/bin/env python3
"""Rebuild banking-rails/ALL-PROJECTS.md from data/projects.json.

Usage (from the repository root):

    python3 scripts/build_all_projects.py

The page is generated from data/projects.json. If banking-rails/RANKING.md
is present, its ranks, scores, verdicts and hard gates are overlaid on the
matching tickers (RANKING.md is the source of truth for finished v3
reports) and data/projects.json is written back so the two stay in sync.

Optional bootstrap from a pipeline coins.json (fields/rows/dead schema):

    python3 scripts/build_all_projects.py --bootstrap /path/to/coins.json
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
JSON_PATH = ROOT / "data" / "projects.json"
PAGE_PATH = ROOT / "banking-rails" / "ALL-PROJECTS.md"
RANKING_PATH = ROOT / "banking-rails" / "RANKING.md"
REPORTS_DIR = ROOT / "banking-rails"

SECTIONS = [
    ("Rev", 0),
    ("Team", 1),
    ("Hold", 2),
    ("Sell", 3),
    ("Token", 4),
    ("Liq", 5),
    ("Prod", 6),
    ("Adopt", 7),
    ("Sec", 8),
    ("Reg", 9),
    ("Catal", 10),
]

STATUS_ORDER = ["done", "close", "wallet", "gaps", "dead"]
STATUS_LABEL = {
    "done": "done",
    "close": "close",
    "wallet": "wallet",
    "gaps": "gaps",
    "dead": "dead",
}

# First 15 of the Close group, in the recommended rebuild order.
IN_PROGRESS = [
    "SKY",
    "ENA",
    "PACT",
    "JST",
    "QUAI",
    "CARDS",
    "ZIG",
    "ADA",
    "ROSE",
    "SPA",
    "DOT",
    "POLYX",
    "INV",
    "TRAC",
    "EXA",
]

# Public-safe display names when the pipeline only stored the ticker.
NAME_OVERRIDES = {
    "ADA": "Cardano",
    "DOT": "Polkadot",
}

# Tickers that already have a short public stub in other-tokens.md.
DRAFT_IN_OTHER_TOKENS = {"SHX", "LL", "SWFTC", "ZK", "RISE"}

LAST_UPDATED = "16 Nov 2026"
TIMEZONE = "MST"
DISCLAIMER = (
    "Research only. Not financial advice. Not a recommendation to buy or sell."
)

PROJECT_KEYS = [
    "ticker",
    "name",
    "status",
    "rank",
    "score",
    "verdict",
    "gates",
    "sink",
    "gaps",
    "old_score",
    "dead_reason",
    "report",
    "draft",
    "market_url",
]


def market_url(ticker: str) -> str:
    return f"https://www.coingecko.com/en/search?query={ticker}"


def report_rel(ticker: str) -> str | None:
    path = REPORTS_DIR / f"{ticker}.md"
    if path.is_file():
        return f"banking-rails/{ticker}.md"
    return None


def draft_rel(ticker: str) -> str | None:
    if ticker in DRAFT_IN_OTHER_TOKENS:
        return "banking-rails/other-tokens.md"
    return None


def sink_from_gates(verdict: str | None, gates: list[str]) -> str | None:
    if not verdict:
        return None
    if verdict == "PASS":
        return None
    if not gates:
        return "Low overall"
    if gates == ["Revenue"]:
        return "Revenue gate"
    if gates == ["Selling"]:
        return "Selling gate"
    if set(gates) == {"Revenue", "Selling"}:
        return "Revenue and Selling gates"
    if len(gates) == 1:
        return f"{gates[0]} gate"
    return " and ".join(gates) + " gates"


def parse_gates(text: str) -> list[str]:
    text = (text or "").strip()
    if not text or text.lower() == "none":
        return []
    parts = [p.strip() for p in re.split(r",| and ", text) if p.strip()]
    out: list[str] = []
    for p in parts:
        key = p
        if p.lower() in {"selling", "selling behavior", "selling_behavior"}:
            key = "Selling"
        elif p.lower() == "revenue":
            key = "Revenue"
        if key not in out:
            out.append(key)
    return out


def report_name(ticker: str) -> str | None:
    path = REPORTS_DIR / f"{ticker}.md"
    if not path.is_file():
        return None
    text = path.read_text(encoding="utf-8")
    m = re.search(r"^name:\s*(.+)$", text, re.M)
    if not m:
        return None
    name = m.group(1).strip().strip('"').strip("'")
    return name or None


def parse_ranking(path: Path) -> dict[str, dict]:
    """Read ranks, scores, verdicts, names and hard gates from RANKING.md."""
    if not path.is_file():
        return {}
    text = path.read_text(encoding="utf-8")
    found: dict[str, dict] = {}

    # At-a-glance lines: 1. 🟢 **BTC** · 7.3 · ✅ PASS
    glance = re.compile(
        r"^(\d+)\.\s+[🟢🔴]\s+\*\*([A-Z0-9]+)\*\*\s+·\s+([0-9.]+)\s+·\s+[✅❌]\s+(PASS|FAIL)\s*$",
        re.M,
    )
    for m in glance.finditer(text):
        ticker = m.group(2)
        found[ticker] = {
            "rank": int(m.group(1)),
            "score": float(m.group(3)),
            "verdict": m.group(4),
            "name": None,
            "gates": [],
        }

    # Detail headers: ## #20 · QNT · Quant  (optional medal prefix)
    header = re.compile(
        r"^##\s+(?:[🥇🥈🥉]\s+)?#(\d+)\s+·\s+([A-Z0-9]+)\s+·\s+(.+?)\s*$",
        re.M,
    )
    # Split on the detail headers so each block can be searched for gates.
    parts = header.split(text)
    # parts: preamble, rank, ticker, name, body, rank, ticker, name, body, ...
    i = 1
    while i + 3 < len(parts):
        rank = int(parts[i])
        ticker = parts[i + 1]
        name = parts[i + 2].strip()
        body = parts[i + 3]
        rec = found.setdefault(
            ticker, {"rank": rank, "score": None, "verdict": None, "name": name, "gates": []}
        )
        rec["rank"] = rank
        rec["name"] = name
        score_m = re.search(
            r"^###\s+([0-9.]+)\s+/\s+10\s+·\s+[✅❌]\s+(PASS|FAIL)\s*$",
            body,
            re.M,
        )
        if score_m:
            rec["score"] = float(score_m.group(1))
            rec["verdict"] = score_m.group(2)
        gates_m = re.search(r"\*\*Hard gates failed:\*\*\s*(.+)$", body, re.M)
        if gates_m:
            rec["gates"] = parse_gates(gates_m.group(1))
        i += 4
    return found


def whats_missing(gaps: str | None) -> str:
    if not gaps or len(gaps) < 11:
        return "—"
    missing = [name for name, i in SECTIONS if gaps[i] == "M"]
    partial = [name for name, i in SECTIONS if gaps[i] == "P"]
    parts: list[str] = []
    if missing:
        parts.append("Missing: " + ", ".join(missing))
    if partial:
        parts.append("Partial: " + ", ".join(partial))
    if not parts:
        return "Light touch-up only"
    return " · ".join(parts)


def fmt_score(score) -> str:
    if score is None:
        return "—"
    if isinstance(score, float) and score.is_integer():
        return f"{score:.1f}"
    if isinstance(score, int):
        return f"{score:.1f}"
    return f"{score:.1f}" if isinstance(score, float) else str(score)


def fmt_sink(project: dict) -> str:
    if project.get("verdict") == "PASS":
        return "—"
    return project.get("sink") or "—"


def md_cell(text: str | None) -> str:
    if not text:
        return "—"
    return str(text).replace("|", "\\|").replace("\n", " ")


def links_cell(project: dict, *, from_banking_rails: bool = True) -> str:
    bits: list[str] = []
    draft = project.get("draft")
    if draft:
        rel = Path(draft).name if from_banking_rails else draft
        bits.append(f"[Draft]({rel})")
    url = project.get("market_url")
    if url:
        bits.append(f"[CoinGecko]({url})")
    return " · ".join(bits) if bits else "—"


def sort_undone(projects: list[dict], in_progress: list[str] | None = None) -> list[dict]:
    lead = {t: i for i, t in enumerate(in_progress or [])}

    def key(p: dict):
        ticker = p["ticker"]
        if ticker in lead:
            return (0, lead[ticker], ticker)
        score = p.get("old_score")
        # None scores sort last; higher old scores first.
        if score is None:
            return (2, 0, ticker)
        return (1, -float(score), ticker)

    return sorted(projects, key=key)


def overlay_ranking(projects: list[dict], ranking: dict[str, dict]) -> list[dict]:
    by_ticker = {p["ticker"]: p for p in projects}
    for ticker, rec in ranking.items():
        p = by_ticker.get(ticker)
        report = report_rel(ticker)
        name = rec.get("name") or (p.get("name") if p else None) or report_name(ticker) or ticker
        gates = rec.get("gates") or []
        verdict = rec.get("verdict")
        score = rec.get("score")
        updated = {
            "ticker": ticker,
            "name": name,
            "status": "done",
            "rank": rec.get("rank"),
            "score": score,
            "verdict": verdict,
            "gates": gates,
            "sink": sink_from_gates(verdict, gates),
            "gaps": "HHHHHHHHHHH",
            "old_score": p.get("old_score") if p else None,
            "dead_reason": None,
            "report": report or (p.get("report") if p else None),
            "draft": None,
            "market_url": (p.get("market_url") if p else None) or market_url(ticker),
        }
        if p:
            p.update(updated)
        else:
            projects.append(updated)
            by_ticker[ticker] = updated
    return projects


def normalize_project(raw: dict) -> dict:
    ticker = raw["ticker"]
    status = raw.get("status") or "gaps"
    if status not in STATUS_ORDER:
        raise SystemExit(f"Unknown status for {ticker}: {status}")
    name = raw.get("name") or NAME_OVERRIDES.get(ticker) or ticker
    gates = list(raw.get("gates") or [])
    verdict = raw.get("verdict") or None
    return {
        "ticker": ticker,
        "name": name,
        "status": status,
        "rank": raw.get("rank"),
        "score": raw.get("score"),
        "verdict": verdict,
        "gates": gates,
        "sink": raw.get("sink") or sink_from_gates(verdict, gates),
        "gaps": raw.get("gaps") or "",
        "old_score": raw.get("old_score"),
        "dead_reason": clean_dead_reason(raw["dead_reason"]) if raw.get("dead_reason") else None,
        "report": raw.get("report") or (report_rel(ticker) if status == "done" else None),
        "draft": raw.get("draft") or draft_rel(ticker),
        "market_url": raw.get("market_url") or market_url(ticker),
    }


def bootstrap_from_pipeline(path: Path, ranking: dict[str, dict]) -> list[dict]:
    data = json.loads(path.read_text(encoding="utf-8"))
    fields = data["fields"]
    idx = {name: i for i, name in enumerate(fields)}
    dead_map = data.get("dead") or {}
    ranked = set(ranking)
    projects: list[dict] = []
    for row in data["rows"]:
        ticker = row[idx["ticker"]]
        raw_name = row[idx["name"]]
        tier = str(row[idx["tier(1 close/2 wallets/3 gaps/D done)"]])
        is_dead = bool(row[idx["dead"]]) or ticker in dead_map
        if ticker in ranked:
            status = "done"
        elif is_dead:
            status = "dead"
        elif tier == "D":
            status = "done"
        elif tier == "1":
            status = "close"
        elif tier == "2":
            status = "wallet"
        else:
            status = "gaps"
        name = NAME_OVERRIDES.get(ticker) or raw_name
        if ticker in ranked and ranking[ticker].get("name"):
            name = ranking[ticker]["name"]
        elif status == "done":
            name = report_name(ticker) or name
        old_score = row[idx["old_score"]]
        project = normalize_project(
            {
                "ticker": ticker,
                "name": name,
                "status": status,
                "rank": ranking[ticker]["rank"] if ticker in ranked else None,
                "score": ranking[ticker]["score"] if ticker in ranked else None,
                "verdict": ranking[ticker]["verdict"] if ticker in ranked else None,
                "gates": ranking[ticker]["gates"] if ticker in ranked else [],
                "gaps": row[idx["section_gaps(11 chars H/P/M)"]] or "",
                "old_score": old_score,
                "dead_reason": clean_dead_reason(dead_map.get(ticker)) if status == "dead" else None,
                "report": report_rel(ticker) if status == "done" else None,
                "draft": draft_rel(ticker) if status != "done" else None,
                "market_url": market_url(ticker),
            }
        )
        projects.append(project)
    return overlay_ranking(projects, ranking)


def load_bundle(path: Path) -> tuple[dict, list[dict]]:
    bundle = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(bundle, list):
        return {}, [normalize_project(p) for p in bundle]
    projects = [normalize_project(p) for p in bundle.get("projects", [])]
    meta = {k: v for k, v in bundle.items() if k != "projects"}
    return meta, projects


def write_json(path: Path, meta: dict, projects: list[dict]) -> None:
    done = [p for p in projects if p["status"] == "done"]
    passing = sum(1 for p in done if p.get("verdict") == "PASS")
    counts = {s: sum(1 for p in projects if p["status"] == s) for s in STATUS_ORDER}
    payload = {
        "title": "All projects",
        "last_updated": meta.get("last_updated") or "2026-11-16",
        "timezone": TIMEZONE,
        "disclaimer": DISCLAIMER,
        "total": len(projects),
        "scored_reports": counts["done"],
        "passing": passing,
        "counts": counts,
        "section_keys": [name for name, _ in SECTIONS],
        "rebuild_order_in_progress": list(
            meta.get("rebuild_order_in_progress") or IN_PROGRESS
        ),
        "projects": [{k: p.get(k) for k in PROJECT_KEYS} for p in sort_for_json(projects)],
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def sort_for_json(projects: list[dict]) -> list[dict]:
    def key(p: dict):
        status_i = STATUS_ORDER.index(p["status"])
        if p["status"] == "done":
            return (status_i, p.get("rank") or 999, p["ticker"])
        if p["status"] == "dead":
            return (status_i, 0, p["ticker"])
        in_progress = IN_PROGRESS if p["status"] == "close" else []
        lead = {t: i for i, t in enumerate(in_progress)}
        if p["ticker"] in lead:
            return (status_i, 0, lead[p["ticker"]], p["ticker"])
        score = p.get("old_score")
        if score is None:
            return (status_i, 2, 0, p["ticker"])
        return (status_i, 1, -float(score), p["ticker"])

    return sorted(projects, key=key)


def render_page(meta: dict, projects: list[dict]) -> str:
    in_progress = list(meta.get("rebuild_order_in_progress") or IN_PROGRESS)
    by_status = {s: [p for p in projects if p["status"] == s] for s in STATUS_ORDER}
    done = sorted(by_status["done"], key=lambda p: (p.get("rank") or 999, p["ticker"]))
    close = sort_undone(by_status["close"], in_progress)
    wallet = sort_undone(by_status["wallet"])
    gaps = sort_undone(by_status["gaps"])
    dead = sorted(by_status["dead"], key=lambda p: p["ticker"])
    passing = sum(1 for p in done if p.get("verdict") == "PASS")
    failing = len(done) - passing
    total = len(projects)
    last_updated = LAST_UPDATED
    if meta.get("last_updated"):
        # Allow ISO dates in JSON; display as "16 Nov 2026"
        raw = str(meta["last_updated"])
        m = re.match(r"(\d{4})-(\d{2})-(\d{2})$", raw)
        if m:
            from datetime import date

            last_updated = date(int(m.group(1)), int(m.group(2)), int(m.group(3))).strftime("%-d %b %Y")
        else:
            last_updated = raw

    remaining_close = [p for p in close if p["ticker"] not in set(in_progress)]
    in_progress_rows = [p for t in in_progress for p in close if p["ticker"] == t]

    lines: list[str] = []
    lines.append("---")
    lines.append("title: All projects")
    lines.append(f"total: {total}")
    lines.append(f"scored_reports: {len(done)}")
    lines.append(f"passing: {passing}")
    lines.append(f"last_updated: {meta.get('last_updated') or '2026-11-16'}")
    lines.append(f"timezone: {TIMEZONE}")
    lines.append(f"disclaimer: {DISCLAIMER}")
    lines.append("---")
    lines.append("")
    lines.append("# 📋 All projects")
    lines.append("")
    lines.append(f"**{DISCLAIMER}**")
    lines.append(f"Updated {last_updated} ({TIMEZONE}). Scoring rules are in the [cover sheet](COVER.md).")
    lines.append("")
    lines.append(
        f"**{total} coins** in the research pipeline. "
        f"**{len(done)}** have a full v3 report. "
        f"**{passing} pass** and **{failing} fail.** "
        f"The other **{total - len(done)}** are still in progress, grouped by how close each is to a full report."
    )
    lines.append("")
    lines.append(
        f"**{len(done)}** ✅ done · **{len(close)}** 🟢 close · **{len(wallet)}** 🟡 need wallet work · "
        f"**{len(gaps)}** 🔴 big gaps · **{len(dead)}** ⚫ dead or wound down"
    )
    lines.append("")
    lines.append("- [✅ Done (v3 reports)](#done)")
    lines.append("- [🟢 Close](#close)")
    lines.append("- [🟡 Need wallet work](#wallet)")
    lines.append("- [🔴 Big gaps](#gaps)")
    lines.append("- [⚫ Dead or wound down](#dead)")
    lines.append("- [🔄 Rebuild order](#rebuild)")
    lines.append("")
    lines.append("Finished reports are ranked on the [ranking page](RANKING.md). A few shorter, unscored stubs live in [other-tokens.md](other-tokens.md).")
    lines.append("")
    lines.append("What's missing uses the 11 v3 sections: Rev, Team, Hold, Sell, Token, Liq, Prod, Adopt, Sec, Reg, Catal. **H** = have, **P** = partial, **M** = missing.")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Done
    lines.append('<a id="done"></a>')
    lines.append("## ✅ Done (v3 reports)")
    lines.append("")
    lines.append(f"**{len(done)} reports. {passing} pass, {failing} fail.** A score of 6.0 or more is a PASS. If Revenue or Selling scores 3 or less, it's an automatic FAIL.")
    lines.append("")
    lines.append("| # | Coin | Name | Score | Status | What sinks it |")
    lines.append("|:---:|---|---|---:|:---:|---|")
    for p in done:
        ticker = p["ticker"]
        href = Path(p["report"]).name if p.get("report") else f"{ticker}.md"
        mark = "✅ PASS" if p.get("verdict") == "PASS" else "❌ FAIL"
        lines.append(
            f"| {p.get('rank') or '—'} | [{ticker}]({href}) | {md_cell(p['name'])} | {fmt_score(p.get('score'))} | {mark} | {md_cell(fmt_sink(p))} |"
        )
    lines.append("")
    lines.append("---")
    lines.append("")

    # Close
    lines.append('<a id="close"></a>')
    lines.append("## 🟢 Close")
    lines.append("")
    lines.append(f"**{len(close)} coins.** Most of the data is already in hand. The first {len(in_progress)} are next in the [rebuild order](#rebuild).")
    lines.append("")
    lines.append("| Ticker | Name | Links | What's missing | Queue |")
    lines.append("|---|---|---|---|---|")
    for p in close:
        queue = "In progress" if p["ticker"] in set(in_progress) else "—"
        ticker_cell = f"**{p['ticker']}**" if p["ticker"] in set(in_progress) else p["ticker"]
        lines.append(
            f"| {ticker_cell} | {md_cell(p['name'])} | {links_cell(p)} | {md_cell(whats_missing(p.get('gaps')))} | {queue} |"
        )
    lines.append("")
    lines.append("---")
    lines.append("")

    # Wallet
    lines.append('<a id="wallet"></a>')
    lines.append("## 🟡 Need wallet work")
    lines.append("")
    lines.append(f"**{len(wallet)} coins.** These still need the team-wallet and pump-day tracing. Listed by earlier research score, highest first.")
    lines.append("")
    lines.append("| Ticker | Name | Links | What's missing |")
    lines.append("|---|---|---|---|")
    for p in wallet:
        lines.append(
            f"| {p['ticker']} | {md_cell(p['name'])} | {links_cell(p)} | {md_cell(whats_missing(p.get('gaps')))} |"
        )
    lines.append("")
    lines.append("---")
    lines.append("")

    # Gaps
    lines.append('<a id="gaps"></a>')
    lines.append("## 🔴 Big gaps")
    lines.append("")
    lines.append(f"**{len(gaps)} coins.** Very little data so far. Listed by earlier research score, highest first.")
    lines.append("")
    lines.append("| Ticker | Name | Links | What's missing |")
    lines.append("|---|---|---|---|")
    for p in gaps:
        lines.append(
            f"| {p['ticker']} | {md_cell(p['name'])} | {links_cell(p)} | {md_cell(whats_missing(p.get('gaps')))} |"
        )
    lines.append("")
    lines.append("---")
    lines.append("")

    # Dead
    lines.append('<a id="dead"></a>')
    lines.append("## ⚫ Dead or wound down")
    lines.append("")
    lines.append(f"**{len(dead)} coins.** These look shut, wound down, or never launched. I'd drop them from a rebuild unless something comes back to life.")
    lines.append("")
    lines.append("| Ticker | Name | Links | Reason |")
    lines.append("|---|---|---|---|")
    for p in dead:
        reason = clean_dead_reason(p.get("dead_reason"))
        lines.append(
            f"| {p['ticker']} | {md_cell(p['name'])} | {links_cell(p)} | {md_cell(reason)} |"
        )
    lines.append("")
    lines.append("---")
    lines.append("")

    # Rebuild order
    lines.append('<a id="rebuild"></a>')
    lines.append("## 🔄 Rebuild order")
    lines.append("")
    lines.append(f"**Next up, in this order** — full v3 reports, now in progress:")
    lines.append("")
    for i, p in enumerate(in_progress_rows, start=1):
        lines.append(f"{i}. **{p['ticker']}** · {p['name']}")
    missing_ip = [t for t in in_progress if t not in {p['ticker'] for p in in_progress_rows}]
    for t in missing_ip:
        lines.append(f"- **{t}**")
    lines.append("")
    if remaining_close:
        names = ", ".join(f"**{p['ticker']}**" for p in remaining_close)
        lines.append(f"**Then the rest of Close:** {names}.")
        lines.append("")
    lines.append("**Then Need wallet work**, by earlier research score, highest first — the same order as the table above, starting with " + ", ".join(f"**{p['ticker']}**" for p in wallet[:5]) + ".")
    lines.append("")
    lines.append("**Then Big gaps**, same sort, after the closer groups are rebuilt.")
    lines.append("")
    lines.append(f"Last updated {last_updated} ({TIMEZONE}).")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## ⚠️ Disclaimer")
    lines.append("")
    lines.append(
        "This is **research only**. It is **not financial advice** and not a recommendation to buy, sell, or hold any token. "
        "A higher score means more of the evidence we checked points to a real, fairly disclosed business. It does not mean the token is a good investment."
    )
    lines.append("")
    return "\n".join(lines)


def clean_dead_reason(reason: str | None) -> str:
    if not reason:
        return "Wound down (reason not on file)"
    text = reason.strip()
    # "delivery:" is an internal canvas label, not useful on the public page.
    text = re.sub(r"(?i)\bdelivery:\s*", "", text, count=1).strip()
    return text


def check_relative_links(page: Path) -> list[str]:
    text = page.read_text(encoding="utf-8")
    # Strip YAML front matter so we don't treat "title: All projects" as a link.
    missing: list[str] = []
    for m in re.finditer(r"\[([^\]]+)\]\(([^)]+)\)", text):
        href = m.group(2).strip()
        if href.startswith(("http://", "https://", "mailto:", "#")):
            continue
        href = href.split("#", 1)[0]
        if not href:
            continue
        target = (page.parent / href).resolve()
        if not target.exists():
            missing.append(f"{m.group(1)} -> {href}")
    return missing


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--bootstrap",
        type=Path,
        help="Optional pipeline coins.json to rebuild data/projects.json from scratch",
    )
    parser.add_argument(
        "--no-ranking-overlay",
        action="store_true",
        help="Do not overlay ranks and scores from banking-rails/RANKING.md",
    )
    args = parser.parse_args(argv)

    ranking = {} if args.no_ranking_overlay else parse_ranking(RANKING_PATH)
    meta = {
        "last_updated": "2026-11-16",
        "rebuild_order_in_progress": IN_PROGRESS,
    }

    if args.bootstrap:
        if not args.bootstrap.is_file():
            raise SystemExit(f"Bootstrap file not found: {args.bootstrap}")
        projects = bootstrap_from_pipeline(args.bootstrap, ranking)
    else:
        if not JSON_PATH.is_file():
            raise SystemExit(
                f"{JSON_PATH} is missing. Create it first, or pass --bootstrap PATH."
            )
        loaded_meta, projects = load_bundle(JSON_PATH)
        meta.update({k: v for k, v in loaded_meta.items() if v is not None})
        if ranking:
            projects = overlay_ranking(projects, ranking)

    write_json(JSON_PATH, meta, projects)
    PAGE_PATH.write_text(render_page(meta, projects), encoding="utf-8")

    missing = check_relative_links(PAGE_PATH)
    counts = {s: sum(1 for p in projects if p["status"] == s) for s in STATUS_ORDER}
    passing = sum(1 for p in projects if p["status"] == "done" and p.get("verdict") == "PASS")
    print(f"Wrote {JSON_PATH.relative_to(ROOT)}")
    print(f"Wrote {PAGE_PATH.relative_to(ROOT)}")
    print(
        f"Counts: total={len(projects)} done={counts['done']} (passing={passing}) "
        f"close={counts['close']} wallet={counts['wallet']} gaps={counts['gaps']} dead={counts['dead']}"
    )
    if missing:
        print("Broken relative links:", file=sys.stderr)
        for item in missing:
            print(f"  {item}", file=sys.stderr)
        return 1
    print("All relative links resolve.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
