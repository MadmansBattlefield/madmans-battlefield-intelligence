#!/usr/bin/env python3
"""Rebuild banking-rails/ALL-PROJECTS.md from data/projects.json.

Usage (from the repository root):

    python3 scripts/build_all_projects.py

The page is generated from data/projects.json. If banking-rails/RANKING.md
is present, its ranks, scores, verdicts and hard gates are overlaid on the
matching tickers (RANKING.md is the source of truth for finished v3
reports) and data/projects.json is written back so the two stay in sync.

A public status scan (data/status-scan.json, or --scan PATH) updates
statuses, market figures, red flags and identity notes for coins that are
not already published v3 reports. The 28 ranked reports stay done.

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
SCAN_PATH = ROOT / "data" / "status-scan.json"
DEAD_PATH = ROOT / "data" / "dead.json"

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

SCAN_STATUS_MAP = {
    "done": "done",
    "close": "close",
    "wallet": "wallet",
    "wallet-work": "wallet",
    "gaps": "gaps",
    "big-gaps": "gaps",
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

# After the 15 in progress: healthiest remaining names from the status scan.
NEXT_UP_AFTER = [
    "SYRUP",
    "CFG",
    "HUMA",
    "SOLV",
    "ARB",
    "ICP",
    "API3",
    "INJ",
    "SUI",
    "ZEC",
    "HYPER",
    "KAIO",
    "CPOOL",
    "W",
    "CRO",
    "ZK",
    "XPL",
    "S",
    "KAIA",
    "BCH",
]

# Preferred order for the identity-notes landmines.
IDENTITY_ORDER = [
    "PI",
    "RISE",
    "NXS",
    "MTR",
    "USDN",
    "SNP",
    "YETI",
    "OMNI",
    "MORPH",
    "KEY",
    "CTX",
    "VERA",
    "ZENITH",
    "TX",
    "AEON",
    "BXX",
    "COLLAT",
    "MXC",
    "THUSD",
    "NANOPAY",
    "FIGR",
    "VVPR",
    "HANDLE",
    "NIGHT",
    "METAL",
    "CROWN",
    "REG",
]

# Public-safe display names when the pipeline only stored the ticker.
NAME_OVERRIDES = {
    "ADA": "Cardano",
    "DOT": "Polkadot",
}

# Tickers that already have a short public stub in other-tokens.md.
DRAFT_IN_OTHER_TOKENS = {"SHX", "LL", "SWFTC", "ZK", "RISE"}

UNVERIFIED_DEAD_FLAG = "delisted and inactive (no official notice re-read) [Unverified]"

FLAG_LABELS = {
    "market cap under $1M": "dying: mcap <$1M",
    "24h volume under $10k": "dying: 24h vol <$10k",
    "not listed on CoinGecko": "not listed on CoinGecko",
    "CoinGecko market cap unreported (returned 0)": "mcap unreported",
    "delisted and inactive (no official notice re-read) [Unverified]": "[Unverified] delisted / inactive",
    "official shutdown": "official shutdown",
    "historical collapse / wound down": "historical collapse",
    "identity [Unverified] as a coin": "identity [Unverified] as a coin",
    "identity [Unverified] (symbol NANO)": "identity [Unverified] (symbol NANO)",
    "MTR stable appears inactive; MTRG (governance) still has a CoinPaprika ticker": "MTR inactive; MTRG still listed",
}

PUBLIC_SCAN_ROW_KEYS = [
    "ticker",
    "name",
    "status",
    "reason",
    "red_flags",
    "identity_note",
    "mcap_usd",
    "vol24_usd",
    "fees30d",
    "revenue30d",
    "tvl",
    "coingecko_id",
    "paprika_id",
    "defillama_slug",
    "mcap_source",
    "vol_source",
    "tvl_source",
    "website",
    "cg_name",
    "cg_confidence",
    "llama_listed",
    "already_v3",
    "checked_at",
]

MARKET_KEYS = [
    "mcap_usd",
    "vol24_usd",
    "fees30d",
    "revenue30d",
    "tvl",
    "red_flags",
    "identity_note",
    "coingecko_id",
    "paprika_id",
    "defillama_slug",
    "mcap_source",
    "vol_source",
    "tvl_source",
    "website",
    "scan_reason",
    "unverified_dead",
    "checked_at",
]

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
] + MARKET_KEYS


def market_url(ticker: str, coingecko_id: str | None = None) -> str:
    if coingecko_id:
        return f"https://www.coingecko.com/en/coins/{coingecko_id}"
    return f"https://www.coingecko.com/en/search?query={ticker}"


def paprika_url(paprika_id: str | None) -> str | None:
    if not paprika_id:
        return None
    return f"https://coinpaprika.com/coin/{paprika_id}/"


def llama_url(project: dict) -> str | None:
    source = (project.get("tvl_source") or "").strip()
    if source.lower().startswith("defillama chain/"):
        chain = source.split("/", 1)[1].strip()
        if chain:
            return "https://defillama.com/chain/" + chain.replace(" ", "%20")
    slug = project.get("defillama_slug")
    if slug:
        return f"https://defillama.com/protocol/{slug}"
    return None


def clean_website(url: str | None) -> str | None:
    if not url or not isinstance(url, str):
        return None
    url = url.strip()
    if url.startswith(("https://", "http://")):
        return url
    return None


def published_report_rel(ticker: str, published: set[str] | None) -> str | None:
    """Link a report only if it is a published v3 note (in RANKING.md).

    In-progress drafts such as SKY.md are ignored on purpose.
    """
    if published is not None and ticker not in published:
        return None
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


def report_name(ticker: str, published: set[str] | None = None) -> str | None:
    if published is not None and ticker not in published:
        return None
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

    header = re.compile(
        r"^##\s+(?:[🥇🥈🥉]\s+)?#(\d+)\s+·\s+([A-Z0-9]+)\s+·\s+(.+?)\s*$",
        re.M,
    )
    parts = header.split(text)
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


def fmt_usd(value) -> str:
    if value is None:
        return "—"
    try:
        number = float(value)
    except (TypeError, ValueError):
        return "—"
    if number == 0:
        return "$0"
    sign = "-" if number < 0 else ""
    amount = abs(number)

    def trim(n: float) -> str:
        return f"{n:.2f}".rstrip("0").rstrip(".")

    if amount >= 1e9:
        return f"{sign}${trim(amount / 1e9)}B"
    if amount >= 1e6:
        return f"{sign}${trim(amount / 1e6)}M"
    if amount >= 1e3:
        return f"{sign}${trim(amount / 1e3)}k"
    if amount >= 10:
        return f"{sign}${trim(amount)}"
    return f"{sign}${amount:.2f}"


def format_red_flags(flags) -> str:
    if not flags:
        return "—"
    labels = []
    for flag in flags:
        label = FLAG_LABELS.get(flag, flag)
        if label not in labels:
            labels.append(label)
    return "; ".join(labels)


def is_unverified_dead(row: dict) -> bool:
    flags = row.get("red_flags") or []
    return any(flag == UNVERIFIED_DEAD_FLAG for flag in flags)


def md_cell(text: str | None) -> str:
    if not text:
        return "—"
    return str(text).replace("|", "\\|").replace("\n", " ")


def links_cell(project: dict, *, from_banking_rails: bool = True) -> str:
    bits: list[str] = []
    site = clean_website(project.get("website"))
    if site:
        bits.append(f"[Site]({site})")
    draft = project.get("draft")
    if draft:
        rel = Path(draft).name if from_banking_rails else draft
        bits.append(f"[Draft]({rel})")
    gecko_id = project.get("coingecko_id")
    paprika_id = project.get("paprika_id")
    mcap_source = (project.get("mcap_source") or project.get("vol_source") or "")
    if gecko_id:
        bits.append(f"[CoinGecko]({market_url(project['ticker'], gecko_id)})")
    elif mcap_source == "coinpaprika" and paprika_id:
        bits.append(f"[CoinPaprika]({paprika_url(paprika_id)})")
    else:
        url = project.get("market_url") or market_url(project["ticker"])
        label = "CoinPaprika" if "coinpaprika.com" in url else "CoinGecko"
        bits.append(f"[{label}]({url})")
    if paprika_id and gecko_id and mcap_source == "coinpaprika":
        bits.append(f"[CoinPaprika]({paprika_url(paprika_id)})")
    llama = llama_url(project)
    if llama:
        bits.append(f"[DefiLlama]({llama})")
    return " · ".join(bits) if bits else "—"


def activity_value(project: dict) -> float | None:
    fees = project.get("fees30d")
    rev = project.get("revenue30d")
    if fees is None and rev is None:
        return None
    return max(float(fees or 0), float(rev or 0))


def sort_undone(
    projects: list[dict],
    lead_tickers: list[str] | None = None,
    *,
    by_activity: bool = False,
) -> list[dict]:
    lead = {t: i for i, t in enumerate(lead_tickers or [])}

    def key(p: dict):
        ticker = p["ticker"]
        if ticker in lead:
            return (0, lead[ticker], ticker)
        if by_activity:
            activity = activity_value(p)
            vol = p.get("vol24_usd")
            if activity is not None:
                return (1, -activity, -(float(vol) if vol is not None else -1), ticker)
            if vol is not None:
                return (2, -float(vol), ticker)
            return (3, 0, ticker)
        score = p.get("old_score")
        if score is None:
            return (2, 0, ticker)
        return (1, -float(score), ticker)

    return sorted(projects, key=key)


def overlay_ranking(
    projects: list[dict], ranking: dict[str, dict], published: set[str]
) -> list[dict]:
    by_ticker = {p["ticker"]: p for p in projects}
    for ticker, rec in ranking.items():
        p = by_ticker.get(ticker)
        report = published_report_rel(ticker, published)
        name = rec.get("name") or (p.get("name") if p else None) or report_name(ticker, published) or ticker
        gates = rec.get("gates") or []
        verdict = rec.get("verdict")
        score = rec.get("score")
        fields = {
            "ticker": ticker,
            "name": name,
            "status": "done",
            "rank": rec.get("rank"),
            "score": score,
            "verdict": verdict,
            "gates": gates,
            "sink": sink_from_gates(verdict, gates),
            "gaps": "HHHHHHHHHHH",
            "dead_reason": None,
            "report": report or (p.get("report") if p else None),
            "draft": None,
        }
        if p:
            fields["old_score"] = p.get("old_score")
            if not p.get("market_url"):
                fields["market_url"] = market_url(ticker, p.get("coingecko_id"))
            p.update(fields)
        else:
            fields["old_score"] = None
            fields["market_url"] = market_url(ticker)
            projects.append(normalize_project(fields))
            by_ticker[ticker] = projects[-1]
    return projects


def empty_market() -> dict:
    return {
        "mcap_usd": None,
        "vol24_usd": None,
        "fees30d": None,
        "revenue30d": None,
        "tvl": None,
        "red_flags": [],
        "identity_note": None,
        "coingecko_id": None,
        "paprika_id": None,
        "defillama_slug": None,
        "mcap_source": None,
        "vol_source": None,
        "tvl_source": None,
        "website": None,
        "scan_reason": None,
        "unverified_dead": False,
        "checked_at": None,
    }


def normalize_project(raw: dict) -> dict:
    ticker = raw["ticker"]
    status = SCAN_STATUS_MAP.get(raw.get("status") or "gaps", raw.get("status"))
    if status not in STATUS_ORDER:
        raise SystemExit(f"Unknown status for {ticker}: {status}")
    name = raw.get("name") or NAME_OVERRIDES.get(ticker) or ticker
    gates = list(raw.get("gates") or [])
    verdict = raw.get("verdict") or None
    flags = list(raw.get("red_flags") or [])
    project = {
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
        "report": raw.get("report"),
        "draft": raw.get("draft") or (draft_rel(ticker) if status != "done" else None),
        "market_url": raw.get("market_url") or market_url(ticker, raw.get("coingecko_id")),
    }
    market = empty_market()
    for key in MARKET_KEYS:
        if key in raw and raw[key] is not None:
            market[key] = raw[key]
        elif key == "red_flags":
            market[key] = flags
        elif key == "unverified_dead":
            market[key] = bool(raw.get("unverified_dead"))
    market["website"] = clean_website(market.get("website"))
    project.update(market)
    return project


def apply_scan_row(project: dict, row: dict, published: set[str]) -> None:
    project["mcap_usd"] = row.get("mcap_usd")
    project["vol24_usd"] = row.get("vol24_usd")
    project["fees30d"] = row.get("fees30d")
    project["revenue30d"] = row.get("revenue30d")
    project["tvl"] = row.get("tvl")
    project["red_flags"] = list(row.get("red_flags") or [])
    project["identity_note"] = row.get("identity_note") or None
    project["coingecko_id"] = row.get("coingecko_id") or None
    project["paprika_id"] = row.get("paprika_id") or None
    project["defillama_slug"] = row.get("defillama_slug") or None
    project["mcap_source"] = row.get("mcap_source") or None
    project["vol_source"] = row.get("vol_source") or None
    project["tvl_source"] = row.get("tvl_source") or None
    project["website"] = clean_website(row.get("website"))
    project["scan_reason"] = row.get("reason") or None
    project["checked_at"] = row.get("checked_at") or None
    project["market_url"] = market_url(project["ticker"], project.get("coingecko_id"))
    if project["ticker"] in published:
        project["status"] = "done"
        project["unverified_dead"] = False
        return
    status = SCAN_STATUS_MAP.get(row.get("status") or "", "gaps")
    project["status"] = status
    project["unverified_dead"] = bool(status == "dead" and is_unverified_dead(row))
    if status == "dead":
        project["dead_reason"] = clean_dead_reason(row.get("reason"))
        project["draft"] = draft_rel(project["ticker"])
    else:
        project["dead_reason"] = None
        project["draft"] = draft_rel(project["ticker"])
        project["report"] = None


def overlay_scan(projects: list[dict], scan: dict, published: set[str]) -> list[dict]:
    by_ticker = {p["ticker"]: p for p in projects}
    for row in scan.get("rows") or []:
        ticker = row.get("ticker")
        if not ticker:
            continue
        if ticker in by_ticker:
            apply_scan_row(by_ticker[ticker], row, published)
        else:
            project = normalize_project(
                {
                    "ticker": ticker,
                    "name": row.get("name") or ticker,
                    "status": "gaps",
                }
            )
            apply_scan_row(project, row, published)
            projects.append(project)
            by_ticker[ticker] = project
    return projects


def sanitize_scan(raw: dict) -> dict:
    rows = []
    for row in raw.get("rows") or []:
        clean = {key: row.get(key) for key in PUBLIC_SCAN_ROW_KEYS}
        clean["website"] = clean_website(clean.get("website"))
        clean["red_flags"] = list(clean.get("red_flags") or [])
        clean["status"] = row.get("status")
        rows.append(clean)
    excluded = raw.get("excluded") or {}
    return {
        "checked_at": raw.get("checked_at") or "16 Nov 2026 5:24 AM MST",
        "timezone": TIMEZONE,
        "scan_universe": raw.get("scan_universe") or len(rows),
        "status_counts": raw.get("status_counts") or {},
        "in_progress": list(excluded.get("researched_separately") or IN_PROGRESS),
        "sources": [
            {"name": "CoinGecko", "url": "https://www.coingecko.com/"},
            {"name": "DefiLlama", "url": "https://defillama.com/"},
            {"name": "CoinPaprika", "url": "https://coinpaprika.com/"},
        ],
        "rows": rows,
    }


def load_scan(path: Path) -> dict:
    raw = json.loads(path.read_text(encoding="utf-8"))
    if "rows" not in raw:
        raise SystemExit(f"Scan file is missing rows: {path}")
    return sanitize_scan(raw)


def write_public_scan(path: Path, scan: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(scan, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def bootstrap_from_pipeline(path: Path, ranking: dict[str, dict], published: set[str]) -> list[dict]:
    data = json.loads(path.read_text(encoding="utf-8"))
    fields = data["fields"]
    idx = {name: i for i, name in enumerate(fields)}
    dead_map = data.get("dead") or {}
    projects: list[dict] = []
    for row in data["rows"]:
        ticker = row[idx["ticker"]]
        raw_name = row[idx["name"]]
        tier = str(row[idx["tier(1 close/2 wallets/3 gaps/D done)"]])
        is_dead = bool(row[idx["dead"]]) or ticker in dead_map
        if ticker in published:
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
        if ticker in published and ranking[ticker].get("name"):
            name = ranking[ticker]["name"]
        elif status == "done":
            name = report_name(ticker, published) or name
        project = normalize_project(
            {
                "ticker": ticker,
                "name": name,
                "status": status,
                "rank": ranking[ticker]["rank"] if ticker in published else None,
                "score": ranking[ticker]["score"] if ticker in published else None,
                "verdict": ranking[ticker]["verdict"] if ticker in published else None,
                "gates": ranking[ticker]["gates"] if ticker in published else [],
                "gaps": row[idx["section_gaps(11 chars H/P/M)"]] or "",
                "old_score": row[idx["old_score"]],
                "dead_reason": clean_dead_reason(dead_map.get(ticker)) if status == "dead" else None,
                "report": published_report_rel(ticker, published) if status == "done" else None,
                "draft": draft_rel(ticker) if status != "done" else None,
                "market_url": market_url(ticker),
            }
        )
        projects.append(project)
    return overlay_ranking(projects, ranking, published)


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
    unverified = sum(1 for p in projects if p.get("unverified_dead"))
    payload = {
        "title": "All projects",
        "last_updated": meta.get("last_updated") or "2026-11-16",
        "timezone": TIMEZONE,
        "disclaimer": DISCLAIMER,
        "total": len(projects),
        "scored_reports": counts["done"],
        "passing": passing,
        "counts": counts,
        "dead_unverified": unverified,
        "scan_checked_at": meta.get("scan_checked_at"),
        "section_keys": [name for name, _ in SECTIONS],
        "rebuild_order_in_progress": list(
            meta.get("rebuild_order_in_progress") or IN_PROGRESS
        ),
        "next_up_after": list(meta.get("next_up_after") or NEXT_UP_AFTER),
        "projects": [{k: p.get(k) for k in PROJECT_KEYS} for p in sort_for_json(projects)],
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def sort_for_json(projects: list[dict]) -> list[dict]:
    next_up = {t: i for i, t in enumerate(IN_PROGRESS + NEXT_UP_AFTER)}

    def key(p: dict):
        status_i = STATUS_ORDER.index(p["status"])
        if p["status"] == "done":
            return (status_i, 0, p.get("rank") or 999, p["ticker"])
        if p["status"] == "dead":
            return (status_i, 0, 0, p["ticker"])
        if p["ticker"] in next_up:
            return (status_i, 0, next_up[p["ticker"]], p["ticker"])
        if p["status"] in {"wallet", "close"}:
            activity = activity_value(p)
            vol = p.get("vol24_usd")
            if activity is not None:
                return (status_i, 1, -activity, p["ticker"])
            if vol is not None:
                return (status_i, 2, -float(vol), p["ticker"])
            return (status_i, 3, 0, p["ticker"])
        score = p.get("old_score")
        if score is None:
            return (status_i, 2, 0, p["ticker"])
        return (status_i, 1, -float(score), p["ticker"])

    return sorted(projects, key=key)


def identity_rows(projects: list[dict]) -> list[dict]:
    lead = {t: i for i, t in enumerate(IDENTITY_ORDER)}
    rows = [p for p in projects if p.get("identity_note")]
    return sorted(
        rows,
        key=lambda p: (0, lead[p["ticker"]]) if p["ticker"] in lead else (1, p["ticker"]),
    )


def market_header() -> tuple[str, str]:
    header = "| Ticker | Name | Mcap | 24h vol | 30d fees | 30d rev | Red flag | Links | What's missing |"
    sep = "|---|---|---:|---:|---:|---:|---|---|---|"
    return header, sep


def market_row(project: dict, ticker_cell: str) -> str:
    return (
        f"| {ticker_cell} | {md_cell(project['name'])} | "
        f"{fmt_usd(project.get('mcap_usd'))} | {fmt_usd(project.get('vol24_usd'))} | "
        f"{fmt_usd(project.get('fees30d'))} | {fmt_usd(project.get('revenue30d'))} | "
        f"{md_cell(format_red_flags(project.get('red_flags')))} | {links_cell(project)} | "
        f"{md_cell(whats_missing(project.get('gaps')))} |"
    )


def format_checked_at(meta: dict) -> str:
    return meta.get("scan_checked_at") or "16 Nov 2026 5:24 AM MST"


def render_page(meta: dict, projects: list[dict]) -> str:
    in_progress = list(meta.get("rebuild_order_in_progress") or IN_PROGRESS)
    next_after = list(meta.get("next_up_after") or NEXT_UP_AFTER)
    by_status = {s: [p for p in projects if p["status"] == s] for s in STATUS_ORDER}
    done = sorted(by_status["done"], key=lambda p: (p.get("rank") or 999, p["ticker"]))
    close = sort_undone(by_status["close"], in_progress, by_activity=True)
    wallet = sort_undone(by_status["wallet"], next_after, by_activity=True)
    gaps = sort_undone(by_status["gaps"], by_activity=True)
    dead = sorted(by_status["dead"], key=lambda p: p["ticker"])
    passing = sum(1 for p in done if p.get("verdict") == "PASS")
    failing = len(done) - passing
    total = len(projects)
    last_updated = LAST_UPDATED
    if meta.get("last_updated"):
        raw = str(meta["last_updated"])
        m = re.match(r"(\d{4})-(\d{2})-(\d{2})$", raw)
        if m:
            from datetime import date

            last_updated = date(int(m.group(1)), int(m.group(2)), int(m.group(3))).strftime("%-d %b %Y")
        else:
            last_updated = raw
    checked_at = format_checked_at(meta)
    unverified = [p for p in dead if p.get("unverified_dead")]
    remaining_close = [p for p in close if p["ticker"] not in set(in_progress)]
    in_progress_rows = [p for t in in_progress for p in projects if p["ticker"] == t]
    next_after_rows = [p for t in next_after for p in projects if p["ticker"] == t]
    notes = identity_rows(projects)

    lines: list[str] = []
    lines.append("---")
    lines.append("title: All projects")
    lines.append(f"total: {total}")
    lines.append(f"scored_reports: {len(done)}")
    lines.append(f"passing: {passing}")
    lines.append(f"last_updated: {meta.get('last_updated') or '2026-11-16'}")
    lines.append(f"timezone: {TIMEZONE}")
    lines.append(f"scan_checked_at: {checked_at}")
    lines.append(f"disclaimer: {DISCLAIMER}")
    lines.append("---")
    lines.append("")
    lines.append("# 📋 All projects")
    lines.append("")
    lines.append(f"**{DISCLAIMER}**")
    lines.append(
        f"Updated {last_updated} ({TIMEZONE}). "
        f"Scoring rules are in the [cover sheet](COVER.md). "
        f"Market and status figures in the unfinished groups were read {checked_at} from "
        f"[CoinGecko](https://www.coingecko.com/), [DefiLlama](https://defillama.com/) and "
        f"[CoinPaprika](https://coinpaprika.com/)."
    )
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
        f"**{len(gaps)}** 🔴 big gaps · **{len(dead)}** ⚫ dead or wound down "
        f"({len(unverified)} of them [Unverified])"
    )
    lines.append("")
    lines.append("- [✅ Done (v3 reports)](#done)")
    lines.append("- [🟢 Close](#close)")
    lines.append("- [🟡 Need wallet work](#wallet)")
    lines.append("- [🔴 Big gaps](#gaps)")
    lines.append("- [⚫ Dead or wound down](#dead)")
    lines.append("- [🔄 Next up](#next)")
    lines.append("- [⚠️ Identity notes](#identity)")
    lines.append("- [📚 Sources](#sources)")
    lines.append("")
    lines.append(
        "Finished reports are ranked on the [ranking page](RANKING.md). "
        "Scoring rules are also in the [methodology](../METHODOLOGY.md). "
        "Names formally moved out of the live pipeline are listed in [DEAD.md](../DEAD.md), "
        "with the date and the reason; a failing scored report is never dropped from the ranking in silence. "
        "A few shorter, unscored stubs live in [other-tokens.md](other-tokens.md)."
    )
    lines.append("")
    lines.append(
        "What's missing uses the 11 v3 sections: Rev, Team, Hold, Sell, Token, Liq, Prod, Adopt, Sec, Reg, Catal. "
        "**H** = have, **P** = partial, **M** = missing. "
        "A **$0** fees or revenue figure means DefiLlama reported zero, not a missing value. "
        "**—** means the API did not return that field. "
        "Red flags such as `dying: mcap <$1M` or `dying: 24h vol <$10k` are quick-kill warnings from the scan, not a final verdict."
    )
    lines.append("")
    lines.append("---")
    lines.append("")

    lines.append('<a id="done"></a>')
    lines.append("## ✅ Done (v3 reports)")
    lines.append("")
    lines.append(
        f"**{len(done)} reports. {passing} pass, {failing} fail.** "
        "A score of 6.0 or more is a PASS. If Revenue or Selling scores 3 or less, it's an automatic FAIL."
    )
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

    header, sep = market_header()
    lines.append('<a id="close"></a>')
    lines.append("## 🟢 Close")
    lines.append("")
    lines.append(
        f"**{len(close)} coins.** Most of the data is already in hand. "
        f"The first {len(in_progress)} are next in the [Next up](#next) list."
    )
    lines.append("")
    lines.append(header.replace("| What's missing |", "| What's missing | Queue |"))
    lines.append(sep + "---|")
    for p in close:
        queue = "In progress" if p["ticker"] in set(in_progress) else "—"
        ticker_cell = f"**{p['ticker']}**" if p["ticker"] in set(in_progress) else p["ticker"]
        # market_row ends with " |" already; append queue by rebuilding
        row = market_row(p, ticker_cell)
        lines.append(row[:-2] + f" | {queue} |")
    lines.append("")
    lines.append("---")
    lines.append("")

    lines.append('<a id="wallet"></a>')
    lines.append("## 🟡 Need wallet work")
    lines.append("")
    lines.append(
        f"**{len(wallet)} coins.** These still need the team-wallet and pump-day tracing. "
        "The [Next up](#next) names are listed first, then the rest by 30-day DefiLlama fees or revenue, then 24h volume."
    )
    lines.append("")
    lines.append(header)
    lines.append(sep)
    for p in wallet:
        lines.append(market_row(p, p["ticker"]))
    lines.append("")
    lines.append("---")
    lines.append("")

    lines.append('<a id="gaps"></a>')
    lines.append("## 🔴 Big gaps")
    lines.append("")
    lines.append(
        f"**{len(gaps)} coins.** Very little reliable current market data, or the ticker's identity is still unsettled."
    )
    lines.append("")
    lines.append(header)
    lines.append(sep)
    for p in gaps:
        lines.append(market_row(p, p["ticker"]))
    lines.append("")
    lines.append("---")
    lines.append("")

    lines.append('<a id="dead"></a>')
    lines.append("## ⚫ Dead or wound down")
    lines.append("")
    lines.append(
        f"**{len(dead)} coins**, **{len(unverified)} of them [Unverified]**. "
        "The unverified names were delisted or inactive in this pass, but no official shutdown notice was re-read. "
        "The others have an official wind-down or a historical collapse. A leftover ticker does not undo a shutdown."
    )
    lines.append("")
    lines.append("| Ticker | Name | Tag | Reason | Mcap | 24h vol | Red flag | Links |")
    lines.append("|---|---|---|---|---:|---:|---|---|")
    for p in dead:
        tag = "[Unverified]" if p.get("unverified_dead") else "—"
        reason = clean_dead_reason(p.get("dead_reason"))
        lines.append(
            f"| {p['ticker']} | {md_cell(p['name'])} | {tag} | {md_cell(reason)} | "
            f"{fmt_usd(p.get('mcap_usd'))} | {fmt_usd(p.get('vol24_usd'))} | "
            f"{md_cell(format_red_flags(p.get('red_flags')))} | {links_cell(p)} |"
        )
    lines.append("")
    lines.append("---")
    lines.append("")

    lines.append('<a id="next"></a>')
    lines.append("## 🔄 Next up")
    lines.append("")
    lines.append("**In progress now**, in this order — full v3 reports:")
    lines.append("")
    for i, p in enumerate(in_progress_rows, start=1):
        lines.append(f"{i}. **{p['ticker']}** · {p['name']}")
    missing_ip = [t for t in in_progress if t not in {p["ticker"] for p in in_progress_rows}]
    start = len(in_progress_rows) + 1
    for offset, t in enumerate(missing_ip):
        lines.append(f"{start + offset}. **{t}**")
    lines.append("")
    lines.append(
        "**Then these**, the healthiest remaining names from the status scan "
        "(ranked by the larger of 30-day DefiLlama revenue or fees, then 24h volume):"
    )
    lines.append("")
    start = len(in_progress) + 1
    for i, p in enumerate(next_after_rows, start=start):
        bits = [f"**{p['ticker']}** · {p['name']}"]
        if p.get("fees30d") is not None or p.get("revenue30d") is not None:
            bits.append(f"30d rev {fmt_usd(p.get('revenue30d'))}, fees {fmt_usd(p.get('fees30d'))}")
        if p.get("vol24_usd") is not None:
            bits.append(f"24h vol {fmt_usd(p.get('vol24_usd'))}")
        if p.get("mcap_usd") is not None:
            bits.append(f"mcap {fmt_usd(p.get('mcap_usd'))}")
        lines.append(f"{i}. " + " · ".join(bits))
    missing_next = [t for t in next_after if t not in {p["ticker"] for p in next_after_rows}]
    n = start + len(next_after_rows)
    for t in missing_next:
        lines.append(f"{n}. **{t}**")
        n += 1
    if remaining_close:
        names = ", ".join(f"**{p['ticker']}**" for p in remaining_close)
        lines.append("")
        lines.append(f"**Then the rest of Close:** {names}.")
    lines.append("")
    lines.append("---")
    lines.append("")

    lines.append('<a id="identity"></a>')
    lines.append("## ⚠️ Identity notes")
    lines.append("")
    lines.append(
        "These tickers were easy to mix up, or the public listing does not clearly match the name in the pipeline. "
        "Landmines first: **PI is Plian**, not Pi Network. **NXS is Nexus**, not the CoinGecko token named NEXUS (symbol NEX). "
        "Market figures were used only when the match was good enough to keep."
    )
    lines.append("")
    lines.append("| Ticker | Name | Note |")
    lines.append("|---|---|---|")
    for p in notes:
        lines.append(f"| {p['ticker']} | {md_cell(p['name'])} | {md_cell(p.get('identity_note'))} |")
    lines.append("")
    lines.append("---")
    lines.append("")

    lines.append('<a id="sources"></a>')
    lines.append("## 📚 Sources")
    lines.append("")
    lines.append(f"Status scan read **{checked_at}**. Numbers are only the values those APIs actually returned.")
    lines.append("")
    lines.append("- [CoinGecko](https://www.coingecko.com/) — market cap and 24h volume (`/coins/list`, `/coins/markets`)")
    lines.append("- [DefiLlama](https://defillama.com/) — 30-day fees, 30-day revenue, and TVL (protocols, fees, revenue, and v2 chains)")
    lines.append("- [CoinPaprika](https://coinpaprika.com/) — fallback market figures when a coin is not on CoinGecko; those rows are linked to CoinPaprika")
    lines.append(
        "- Official project posts and contemporaneous coverage for shutdown claims, as summarized in the [scan data](../data/status-scan.json)"
    )
    lines.append("")
    lines.append(
        "A leftover CoinGecko or CoinPaprika listing does not undo an official wind-down. "
        "Machine-readable project data is in [data/projects.json](../data/projects.json)."
    )
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


def resolve_scan_path(cli_path: Path | None) -> Path | None:
    if cli_path:
        return cli_path
    if SCAN_PATH.is_file():
        return SCAN_PATH
    return None


def overlay_dead_list(projects: list[dict], published: set[str]) -> list[dict]:
    """Apply dated moves from data/dead.json. Never silently drop a published report."""
    if not DEAD_PATH.is_file():
        return projects
    data = json.loads(DEAD_PATH.read_text(encoding="utf-8"))
    by_ticker = {p["ticker"]: p for p in projects}
    for row in data.get("entries") or []:
        ticker = row.get("ticker")
        if not ticker or ticker in published:
            continue
        project = by_ticker.get(ticker)
        if not project:
            continue
        project["status"] = "dead"
        if row.get("reason"):
            project["dead_reason"] = clean_dead_reason(row.get("reason"))
        project["unverified_dead"] = bool(row.get("unverified"))
        project["report"] = None
    return projects


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--bootstrap",
        type=Path,
        help="Optional pipeline coins.json to rebuild data/projects.json from scratch",
    )
    parser.add_argument(
        "--scan",
        type=Path,
        help="Status scan JSON (default: data/status-scan.json if present)",
    )
    parser.add_argument(
        "--no-ranking-overlay",
        action="store_true",
        help="Do not overlay ranks and scores from banking-rails/RANKING.md",
    )
    args = parser.parse_args(argv)

    ranking = {} if args.no_ranking_overlay else parse_ranking(RANKING_PATH)
    published = set(ranking)
    meta = {
        "last_updated": "2026-11-16",
        "rebuild_order_in_progress": IN_PROGRESS,
        "next_up_after": NEXT_UP_AFTER,
    }

    if args.bootstrap:
        if not args.bootstrap.is_file():
            raise SystemExit(f"Bootstrap file not found: {args.bootstrap}")
        projects = bootstrap_from_pipeline(args.bootstrap, ranking, published)
    else:
        if not JSON_PATH.is_file():
            raise SystemExit(
                f"{JSON_PATH} is missing. Create it first, or pass --bootstrap PATH."
            )
        loaded_meta, projects = load_bundle(JSON_PATH)
        meta.update({k: v for k, v in loaded_meta.items() if v is not None})
        meta.setdefault("rebuild_order_in_progress", IN_PROGRESS)
        meta.setdefault("next_up_after", NEXT_UP_AFTER)

    scan_path = resolve_scan_path(args.scan)
    if scan_path:
        if not scan_path.is_file():
            raise SystemExit(f"Scan file not found: {scan_path}")
        scan = load_scan(scan_path)
        write_public_scan(SCAN_PATH, scan)
        meta["scan_checked_at"] = scan.get("checked_at")
        projects = overlay_scan(projects, scan, published)

    if ranking:
        projects = overlay_ranking(projects, ranking, published)

    projects = overlay_dead_list(projects, published)

    # Never treat an in-progress draft as a published report.
    for p in projects:
        if p["ticker"] not in published:
            if p.get("report"):
                p["report"] = None
            if p["status"] == "done":
                # A done flag without a ranking entry should not survive a scan/rebuild.
                pass

    write_json(JSON_PATH, meta, projects)
    PAGE_PATH.write_text(render_page(meta, projects), encoding="utf-8")

    missing = check_relative_links(PAGE_PATH)
    counts = {s: sum(1 for p in projects if p["status"] == s) for s in STATUS_ORDER}
    passing = sum(1 for p in projects if p["status"] == "done" and p.get("verdict") == "PASS")
    unverified = sum(1 for p in projects if p.get("unverified_dead"))
    print(f"Wrote {JSON_PATH.relative_to(ROOT)}")
    print(f"Wrote {PAGE_PATH.relative_to(ROOT)}")
    if scan_path:
        print(f"Wrote {SCAN_PATH.relative_to(ROOT)}")
    print(
        f"Counts: total={len(projects)} done={counts['done']} (passing={passing}) "
        f"close={counts['close']} wallet={counts['wallet']} gaps={counts['gaps']} "
        f"dead={counts['dead']} (unverified={unverified})"
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
