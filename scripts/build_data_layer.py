#!/usr/bin/env python3
"""Build the machine-readable report layer and the methodology sidecars.

From the repository root:

    python3 scripts/build_data_layer.py
    python3 scripts/build_data_layer.py --skip-history

This reads only git-tracked published reports under banking-rails/. It does
not open untracked drafts and it does not change section scores. Run
scripts/build_all_projects.py to refresh the All Projects catalog; that
script can optionally call this one.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))

from extract_reports import (  # noqa: E402
    SECTION_KEYS,
    extract_all,
    git_tracked_reports,
    now_mst_label,
    parse_front_matter,
)
from validate_reports import validate_all  # noqa: E402

MST = timezone(timedelta(hours=-7))
OUT_REPORTS = ROOT / "data" / "reports"
HISTORY_JSON = ROOT / "data" / "history.json"
HISTORY_MD = ROOT / "HISTORY.md"
RATES_JSON = ROOT / "data" / "base-rates.json"
RATES_MD = ROOT / "BASE-RATES.md"
ADDR_JSON = ROOT / "data" / "public-addresses.json"
FLAGS_JSON = ROOT / "data" / "review-flags.json"
FLAGS_MD = ROOT / "REVIEW-FLAGS.md"
DEAD_JSON = ROOT / "data" / "dead.json"
DEAD_MD = ROOT / "DEAD.md"
INDEX_JSON = ROOT / "data" / "index.json"
PROJECTS_JSON = ROOT / "data" / "projects.json"

# Calibration controls already scored at the bottom of the published ranking.
# These are labels only; no new research and no score changes.
CALIBRATION_CONTROLS = [
    {
        "ticker": "ROUTER",
        "name": "Solrouter",
        "score": 2.2,
        "rank": 113,
        "why": "Bottom of the published ranking. Failed Revenue and Selling. Almost no paying product usage; insider selling into pumps is documented in the published report.",
    },
    {
        "ticker": "H",
        "name": "Humanity Protocol",
        "score": 2.4,
        "rank": 112,
        "why": "Failed Revenue. Published report documents a June 2026 key-theft exploit, a reissued token with an uncapped admin mint, and highly concentrated holdings.",
    },
    {
        "ticker": "COTI",
        "name": "COTI",
        "score": 2.4,
        "rank": 111,
        "why": "Failed Revenue and Selling. Published report documents consolidation wallets selling into the first pump after they were funded.",
    },
    {
        "ticker": "SPA",
        "name": "Sperax",
        "score": 2.5,
        "rank": 109,
        "why": "Failed Revenue and Selling (0 of 11 sections passed). Published report documents a team Safe sending tokens to exchange deposits on a pump day.",
    },
    {
        "ticker": "EDEL",
        "name": "Edel Finance",
        "score": 2.5,
        "rank": 108,
        "why": "Failed Revenue and Selling (0 of 11 sections passed). Published report documents two security incidents in 2026 and a large insider take at launch.",
    },
]


def to_mst_label(iso: str) -> str:
    """Convert a git ISO timestamp to an MST-labelled clock time."""
    dt = datetime.fromisoformat(iso)
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    local = dt.astimezone(MST)
    return local.strftime("%Y-%m-%d %H:%M MST")


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def collect_history() -> dict:
    """Walk git history of each published report and record scores per commit."""
    generated_at = now_mst_label()
    reports: list[dict] = []
    for path in git_tracked_reports():
        rel = f"banking-rails/{path.name}"
        log = subprocess.check_output(
            ["git", "log", "--follow", "--format=%H\t%cI\t%s", "--", rel],
            cwd=ROOT,
            text=True,
        )
        versions = []
        for line in log.splitlines():
            if not line.strip():
                continue
            parts = line.split("\t", 2)
            if len(parts) < 3:
                continue
            commit, ciso, subject = parts
            # With --follow the path is usually unchanged in this repo.
            try:
                raw = subprocess.check_output(
                    ["git", "show", f"{commit}:{rel}"],
                    cwd=ROOT,
                    text=True,
                    stderr=subprocess.DEVNULL,
                )
            except subprocess.CalledProcessError:
                continue
            try:
                fm, _ = parse_front_matter(raw)
            except Exception:
                continue
            if "section_scores" not in fm or "overall_score" not in fm:
                continue
            scores = {k: int(fm["section_scores"][k]) for k in SECTION_KEYS if k in fm["section_scores"]}
            versions.append(
                {
                    "commit": commit,
                    "committed_at_mst": to_mst_label(ciso),
                    "subject": subject,
                    "overall_score": float(fm["overall_score"]),
                    "overall_verdict": str(fm.get("overall_verdict", "")).upper(),
                    "section_scores": scores,
                    "gates_failed": list(fm.get("gates_failed") or []),
                    "last_updated": str(fm.get("last_updated") or ""),
                }
            )
        # git log is newest first; store oldest first.
        versions.reverse()
        # Collapse adjacent identical score snapshots, keep first and last of a run plus any score change.
        collapsed = []
        prev_sig = None
        for ver in versions:
            sig = (
                ver["overall_score"],
                ver["overall_verdict"],
                tuple(ver["section_scores"].get(k) for k in SECTION_KEYS),
                tuple(ver["gates_failed"]),
            )
            if sig == prev_sig:
                # Keep the newest commit of an unchanged run by replacing the tail.
                if collapsed:
                    collapsed[-1] = ver
                continue
            collapsed.append(ver)
            prev_sig = sig
        reports.append(
            {
                "ticker": path.stem,
                "path": rel,
                "versions": collapsed,
            }
        )
    reports.sort(key=lambda r: r["ticker"])
    return {
        "title": "Score history for published v3 reports",
        "timezone_label": "MST",
        "generated_at": generated_at,
        "note": "Backfilled from git history of banking-rails/<TICKER>.md. Adjacent commits with identical scores are collapsed to the latest commit of that run. Scores are not recalculated.",
        "reports": reports,
    }


def render_history_md(history: dict) -> str:
    lines = [
        "---",
        "title: Score history",
        f"generated_at: {history['generated_at']}",
        "timezone: MST",
        "disclaimer: Research only. Not financial advice. Not a recommendation to buy or sell.",
        "---",
        "",
        "# 📉 Score history",
        "",
        "**Research only. Not financial advice.** Times are in **MST**.",
        "",
        "This table records each published v3 report's scores across git versions. It is backfilled from the repository history. Adjacent commits that did not change scores are collapsed. The scoring rules themselves are in [METHODOLOGY.md](METHODOLOGY.md) and the [cover sheet](banking-rails/COVER.md).",
        "",
        "Machine-readable copy: [data/history.json](data/history.json).",
        "",
        "| Ticker | Versions | First overall | Current overall | Revenue (first → current) | Selling (first → current) | Holdings (first → current) |",
        "|---|---:|---:|---:|---|---|---|",
    ]
    for rec in history["reports"]:
        vers = rec["versions"]
        if not vers:
            lines.append(f"| {rec['ticker']} | 0 | — | — | — | — | — |")
            continue
        first, last = vers[0], vers[-1]

        def pair(key: str) -> str:
            a = first["section_scores"].get(key)
            b = last["section_scores"].get(key)
            if a is None or b is None:
                return "—"
            if a == b:
                return str(b)
            return f"{a} → {b}"

        lines.append(
            f"| [{rec['ticker']}](banking-rails/{rec['ticker']}.md) | {len(vers)} | "
            f"{first['overall_score']} | {last['overall_score']} | "
            f"{pair('revenue')} | {pair('selling_behavior')} | {pair('insider_holdings')} |"
        )
    lines += [
        "",
        "## Version detail",
        "",
        "Each row is a commit in which that report's scores (or gates) changed, plus the first commit that introduced the report.",
        "",
    ]
    for rec in history["reports"]:
        if not rec["versions"]:
            continue
        if len(rec["versions"]) == 1:
            ver = rec["versions"][0]
            lines.append(
                f"- **{rec['ticker']}** — {ver['overall_score']} {ver['overall_verdict']} "
                f"in `{ver['commit'][:7]}` ({ver['committed_at_mst']})."
            )
            continue
        lines.append(f"### {rec['ticker']}")
        lines.append("")
        lines.append("| Commit | When (MST) | Overall | Verdict | Rev | Sell | Hold | Gates |")
        lines.append("|---|---|---:|---|---:|---:|---:|---|")
        for ver in rec["versions"]:
            ss = ver["section_scores"]
            gates = ", ".join(ver["gates_failed"]) or "—"
            lines.append(
                f"| `{ver['commit'][:7]}` | {ver['committed_at_mst']} | {ver['overall_score']} | "
                f"{ver['overall_verdict']} | {ss.get('revenue', '—')} | {ss.get('selling_behavior', '—')} | "
                f"{ss.get('insider_holdings', '—')} | {gates} |"
            )
        lines.append("")
    lines += [
        "---",
        "",
        "## Disclaimer",
        "",
        "This is **research only**. It is **not financial advice** and not a recommendation to buy, sell, or hold any token.",
        "",
    ]
    return "\n".join(lines)


def compute_base_rates(recs: list[dict]) -> dict:
    n = len(recs)
    fail_rev = [r for r in recs if r["hard_gates"]["revenue"]["tripped"]]
    fail_sell = [r for r in recs if r["hard_gates"]["selling_behavior"]["tripped"]]
    fail_both = [r for r in recs if r in fail_rev and r in fail_sell]
    passing = [r for r in recs if r["overall_verdict"] == "PASS"]
    proven = [r for r in recs if r["pump_day_test"]["proven_pump_day_sale"] == "yes"]
    not_proven = [r for r in recs if r["pump_day_test"]["selling_not_proven"]]
    proven_unclear = [r for r in recs if r["pump_day_test"]["proven_pump_day_sale"] == "unclear"]
    silence = [r for r in recs if r["pump_day_test"]["disclosure_quality"] == "silence"]
    reaches_yes = [r for r in recs if r["revenue_accrual"]["reaches_holders"] == "yes"]
    reaches_no = [r for r in recs if r["revenue_accrual"]["reaches_holders"] == "no"]
    reaches_unclear = [r for r in recs if r["revenue_accrual"]["reaches_holders"] == "unclear"]
    sell4 = [r for r in recs if r["section_scores"]["selling_behavior"] == 4]

    def tickers(rows):
        return [r["ticker"] for r in rows]

    def rate(rows):
        return {"count": len(rows), "share": None if not n else round(len(rows) / n, 4), "tickers": tickers(rows)}

    return {
        "title": "Base rates across published v3 reports",
        "timezone_label": "MST",
        "generated_at": now_mst_label(),
        "universe": n,
        "note": "Computed from the published reports only. Pump-day and holder-accrual flags are parsed from the Markdown; they are not a new investigation. The undisclosed-sale penalty that takes effect on 16 Nov 2026 is not applied retroactively.",
        "pass_rate": rate(passing),
        "fail_revenue_gate": rate(fail_rev),
        "fail_selling_gate": rate(fail_sell),
        "fail_both_gates": rate(fail_both),
        "proven_pump_day_sale": rate(proven),
        "pump_day_sale_unclear": rate(proven_unclear),
        "selling_not_proven": rate(not_proven),
        "selling_score_equals_4": rate(sell4),
        "undisclosed_pump_day_sale_silence": rate(silence),
        "revenue_reaches_holders_yes": rate(reaches_yes),
        "revenue_reaches_holders_no": rate(reaches_no),
        "revenue_reaches_holders_unclear": rate(reaches_unclear),
    }


def pct(count: int, n: int) -> str:
    if not n:
        return "—"
    return f"{count / n * 100:.1f}%"


def render_base_rates_md(rates: dict) -> str:
    n = rates["universe"]

    def row(label, key):
        rec = rates[key]
        return f"| {label} | {rec['count']} | {pct(rec['count'], n)} |"

    lines = [
        "---",
        "title: Base rates",
        f"generated_at: {rates['generated_at']}",
        f"universe: {n}",
        "timezone: MST",
        "disclaimer: Research only. Not financial advice. Not a recommendation to buy or sell.",
        "---",
        "",
        "# 📊 Base rates",
        "",
        f"**Research only. Not financial advice.** Times are in **MST**. Universe: **{n} published v3 reports**.",
        "",
        rates["note"],
        "",
        "Machine-readable copy: [data/base-rates.json](data/base-rates.json). Score history is in [HISTORY.md](HISTORY.md). The underlying method is in [METHODOLOGY.md](METHODOLOGY.md).",
        "",
        "## Headline rates",
        "",
        "| Measure | Count | Share of 113 |",
        "|---|---:|---:|",
        row("Overall PASS (6.0 or more, and no hard gate tripped)", "pass_rate"),
        row("Revenue hard gate tripped (Revenue 3 or below)", "fail_revenue_gate"),
        row("Selling hard gate tripped (Selling 3 or below)", "fail_selling_gate"),
        row("Both hard gates tripped", "fail_both_gates"),
        row("Proven pump-day sale (parsed from the report)", "proven_pump_day_sale"),
        row("Pump-day sale unclear from the text", "pump_day_sale_unclear"),
        row("Selling marked not proven (score 4, or the report says so)", "selling_not_proven"),
        row("Selling score exactly 4", "selling_score_equals_4"),
        row("Proven or claimed pump-day sale with disclosure quality = silence", "undisclosed_pump_day_sale_silence"),
        row("Holder-accrual test = yes", "revenue_reaches_holders_yes"),
        row("Holder-accrual test = no", "revenue_reaches_holders_no"),
        row("Holder-accrual test = unclear", "revenue_reaches_holders_unclear"),
        "",
        "A **proven pump-day sale** here means the published report itself describes a team, foundation, or treasury-linked wallet selling (or funding a wallet that sold) on a day that met the pump-day test. It is not a fresh price check.",
        "",
        "## Ticker lists",
        "",
    ]
    labels = [
        ("Overall PASS", "pass_rate"),
        ("Revenue hard gate tripped", "fail_revenue_gate"),
        ("Selling hard gate tripped", "fail_selling_gate"),
        ("Both hard gates tripped", "fail_both_gates"),
        ("Proven pump-day sale", "proven_pump_day_sale"),
        ("Selling not proven", "selling_not_proven"),
        ("Holder-accrual test = yes", "revenue_reaches_holders_yes"),
        ("Holder-accrual test = no", "revenue_reaches_holders_no"),
    ]
    for title, key in labels:
        rec = rates[key]
        tickers = rec["tickers"]
        lines.append(f"### {title} ({rec['count']})")
        lines.append("")
        if not tickers:
            lines.append("None.")
        else:
            linked = ", ".join(f"[{t}](banking-rails/{t}.md)" for t in tickers)
            lines.append(linked + ".")
        lines.append("")
    lines += [
        "---",
        "",
        "## Disclaimer",
        "",
        "This is **research only**. It is **not financial advice** and not a recommendation to buy, sell, or hold any token.",
        "",
    ]
    return "\n".join(lines)


def collect_addresses(recs: list[dict]) -> dict:
    entries = []
    seen = set()
    for rec in recs:
        for item in rec.get("addresses_examined") or []:
            key = (item.get("chain") or "", item["address"])
            if key in seen:
                continue
            seen.add(key)
            entries.append(
                {
                    "ticker": rec["ticker"],
                    "chain": item.get("chain"),
                    "address": item["address"],
                    "url": item["url"],
                    "kind": item.get("kind") or "address",
                }
            )
    entries.sort(key=lambda r: (r["ticker"], r.get("chain") or "", r["address"]))
    return {
        "title": "Public addresses examined in published v3 reports",
        "timezone_label": "MST",
        "generated_at": now_mst_label(),
        "note": "Every address here was extracted from a public evidence link or explorer URL already published in banking-rails/<TICKER>.md. No private worksheets were used. Labels that would name a private individual are not included.",
        "count": len(entries),
        "addresses": entries,
    }


def collect_flags(recs: list[dict]) -> dict:
    low = []
    single = []
    revenue = []
    for rec in recs:
        rev = rec.get("review") or {}
        if rev.get("selling_holdings_low_confidence_flag"):
            low.append(
                {
                    "ticker": rec["ticker"],
                    "selling_behavior": rec["section_scores"]["selling_behavior"],
                    "insider_holdings": rec["section_scores"]["insider_holdings"],
                    "notes": list(rev.get("flag_notes") or []),
                }
            )
        if rev.get("selling_holdings_single_source_arkham_flag"):
            single.append(
                {
                    "ticker": rec["ticker"],
                    "selling_behavior": rec["section_scores"]["selling_behavior"],
                    "insider_holdings": rec["section_scores"]["insider_holdings"],
                    "notes": list(rev.get("flag_notes") or []),
                }
            )
        if rev.get("revenue_accrual_inconsistent"):
            acc = rec["revenue_accrual"]
            revenue.append(
                {
                    "ticker": rec["ticker"],
                    "revenue_score": rec["section_scores"]["revenue"],
                    "reaches_holders": acc.get("reaches_holders"),
                    "mechanisms": acc.get("mechanisms") or [],
                    "notes": acc.get("notes"),
                }
            )
    return {
        "title": "Review flags from the Arkham-confidence and holder-accrual upgrades",
        "timezone_label": "MST",
        "generated_at": now_mst_label(),
        "note": "Scores were not changed. These are review lists parsed from the published Markdown. A flag means a human (or a later dual review) should look at that section, not that the published score is automatically wrong.",
        "low_confidence_selling_or_holdings": low,
        "single_source_arkham_selling_or_holdings": single,
        "revenue_accrual_inconsistent": revenue,
    }


def render_flags_md(flags: dict) -> str:
    lines = [
        "---",
        "title: Review flags",
        f"generated_at: {flags['generated_at']}",
        "timezone: MST",
        "disclaimer: Research only. Not financial advice. Scores on this page were not changed.",
        "---",
        "",
        "# 🚩 Review flags",
        "",
        "**Research only. Not financial advice.** Times are in **MST**.",
        "",
        flags["note"],
        "",
        "The rules these flags apply are in [METHODOLOGY.md](METHODOLOGY.md). Machine-readable copy: [data/review-flags.json](data/review-flags.json).",
        "",
        "## 1. Selling or Holdings may have used a low-confidence label alone",
        "",
        "Rule: only a verified entity label with on-chain proof, or a second independent source, can move a Selling or Holdings score. Prediction labels and unlabelled attributions cannot move those scores by themselves.",
        "",
    ]
    low = flags["low_confidence_selling_or_holdings"]
    if not low:
        lines.append("No published report was flagged on this stricter test. Cases where Selling is already 4 (not proven) because a wallet was unlabelled are listed in the JSON notes of those reports, and are not treated as a silent score move.")
        lines.append("")
    else:
        lines.append(f"**{len(low)} report(s) flagged.**")
        lines.append("")
        lines.append("| Ticker | Selling | Holdings | Why |")
        lines.append("|---|---:|---:|---|")
        for rec in low:
            why = "<br>".join(rec["notes"]) or "Low-confidence attribution in Selling or Holdings."
            lines.append(
                f"| [{rec['ticker']}](banking-rails/{rec['ticker']}.md) | {rec['selling_behavior']} | {rec['insider_holdings']} | {why} |"
            )
        lines.append("")
    lines += [
        "## 2. Selling or Holdings cites an Arkham label with no second source parsed",
        "",
        "These are not automatically wrong. Exchange and entity labels from Arkham are Tier B. The new rule asks for on-chain proof of the label, or a second independent source, before that label can move Selling or Holdings. They are listed so a later review can confirm or downgrade them. Scores were left as published.",
        "",
    ]
    single = flags["single_source_arkham_selling_or_holdings"]
    if not single:
        lines.append("None parsed.")
        lines.append("")
    else:
        lines.append(f"**{len(single)} report(s) flagged.**")
        lines.append("")
        lines.append("| Ticker | Selling | Holdings |")
        lines.append("|---|---:|---:|")
        for rec in single:
            lines.append(
                f"| [{rec['ticker']}](banking-rails/{rec['ticker']}.md) | {rec['selling_behavior']} | {rec['insider_holdings']} |"
            )
        lines.append("")
    lines += [
        "## 3. Revenue score looks inconsistent with the holder-accrual test",
        "",
        "The test is binary: an on-chain, automatic burn, buyback, staking yield from fees, or fee share that has already executed. Promises do not count. A report is listed when Revenue is 4 or higher and the test is **no**, when Revenue is a pass (6 or more) and the test is not **yes**, or when the test is **yes** and Revenue still trips the hard gate. Scores were left as published.",
        "",
    ]
    rev = flags["revenue_accrual_inconsistent"]
    if not rev:
        lines.append("None parsed.")
        lines.append("")
    else:
        lines.append(f"**{len(rev)} report(s) flagged.**")
        lines.append("")
        lines.append("| Ticker | Revenue | Reaches holders | Mechanisms | Notes (from the report) |")
        lines.append("|---|---:|---|---|---|")
        for rec in rev:
            mech = ", ".join(rec["mechanisms"]) or "—"
            notes = (rec["notes"] or "—").replace("|", "/")
            if len(notes) > 220:
                notes = notes[:217] + "..."
            lines.append(
                f"| [{rec['ticker']}](banking-rails/{rec['ticker']}.md) | {rec['revenue_score']} | {rec['reaches_holders']} | {mech} | {notes} |"
            )
        lines.append("")
    lines += [
        "---",
        "",
        "## Disclaimer",
        "",
        "This is **research only**. It is **not financial advice** and not a recommendation to buy, sell, or hold any token. A flag is a request for review, not a new score.",
        "",
    ]
    return "\n".join(lines)


def build_dead_list() -> dict:
    projects = load_json(PROJECTS_JSON)
    entries = []
    for p in projects.get("projects") or []:
        if p.get("status") != "dead" and p.get("ticker") != "ELK":
            continue
        ticker = p["ticker"]
        if ticker == "ELK":
            entries.append(
                {
                    "ticker": "ELK",
                    "name": p.get("name") or "Elk Finance",
                    "moved_on": "2026-11-16",
                    "category": "dying_market_skip",
                    "unverified": False,
                    "had_v3_score": False,
                    "reason": "Skipped as dying: market cap under $1M and 24h volume under $10k on 16 Nov 2026 (CoinGecko figures from the public status scan). Recorded here so a thin-market skip is not dropped silently from the pipeline.",
                }
            )
            continue
        entries.append(
            {
                "ticker": ticker,
                "name": p.get("name") or ticker,
                "moved_on": "2026-11-16",
                "listed_as_of": "2026-11-16",
                "category": "wound_down_or_collapsed",
                "unverified": bool(p.get("unverified_dead")),
                "had_v3_score": False,
                "reason": p.get("dead_reason") or p.get("scan_reason") or "Listed as dead or wound down in the public catalog.",
            }
        )
    entries.sort(key=lambda r: r["ticker"])
    return {
        "title": "Moved to dead",
        "timezone_label": "MST",
        "generated_at": now_mst_label(),
        "policy": "A published v3 report that fails is never removed from the ranking in silence. It stays on RANKING.md until a dated entry is added here with a reason. Unscored pipeline names can move here for official shutdowns, unfixed exploits, wind-downs, or a documented dying-market skip. Other scan warnings such as thin volume stay warnings until they are formally moved.",
        "dying_market_skip_rule": "Market cap under $1M and 24h volume under $10k, as of a dated public market read, and only when an explicit entry is added on this list.",
        "entries": entries,
        "calibration_controls": CALIBRATION_CONTROLS,
    }


def render_dead_md(dead: dict) -> str:
    lines = [
        "---",
        "title: Moved to dead",
        f"generated_at: {dead['generated_at']}",
        "timezone: MST",
        "disclaimer: Research only. Not financial advice. Not a recommendation to buy or sell.",
        "---",
        "",
        "# ⚫ Moved to dead",
        "",
        "**Research only. Not financial advice.** Times are in **MST**.",
        "",
        "## Policy",
        "",
        dead["policy"],
        "",
        f"**Dying-market skip rule:** {dead['dying_market_skip_rule']} This is not applied automatically to every thin name on the All Projects scan.",
        "",
        "Machine-readable copy: [data/dead.json](data/dead.json). The All Projects catalog still lists every pipeline name, including these, in [banking-rails/ALL-PROJECTS.md](banking-rails/ALL-PROJECTS.md).",
        "",
        "## List",
        "",
        "| Ticker | Name | Moved on | Category | Unverified | Reason |",
        "|---|---|---|---|---|---|",
    ]
    for rec in dead["entries"]:
        unver = "yes" if rec.get("unverified") else "no"
        reason = (rec.get("reason") or "").replace("\n", " ").replace("|", "/")
        if len(reason) > 280:
            reason = reason[:277] + "..."
        lines.append(
            f"| {rec['ticker']} | {rec['name']} | {rec['moved_on']} | {rec['category']} | {unver} | {reason} |"
        )
    lines += [
        "",
        "## Calibration controls",
        "",
        "These already-scored reports sit at the bottom of the published ranking and are labelled as **negative controls**. They are not new research and their scores are not changed. They exist so later methodology changes can be checked against tokens the desk has already graded as clear fails.",
        "",
        "| Ticker | Rank | Score | Why this is a control |",
        "|---|---:|---:|---|",
    ]
    for rec in dead["calibration_controls"]:
        lines.append(
            f"| [{rec['ticker']}](banking-rails/{rec['ticker']}.md) | {rec['rank']} | {rec['score']} | {rec['why']} |"
        )
    lines += [
        "",
        "A known-dead name from the list above can be added as an additional control only if it is later given a full v3 report. No such new report is being written in this pass.",
        "",
        "---",
        "",
        "## Disclaimer",
        "",
        "This is **research only**. It is **not financial advice** and not a recommendation to buy, sell, or hold any token.",
        "",
    ]
    return "\n".join(lines)


def update_index(recs: list[dict]) -> None:
    index = load_json(INDEX_JSON) if INDEX_JSON.is_file() else {}
    paths = dict(index.get("paths") or {})
    paths.update(
        {
            "methodology": "METHODOLOGY.md",
            "history": "HISTORY.md",
            "base_rates": "BASE-RATES.md",
            "dead": "DEAD.md",
            "reproduce": "REPRODUCE.md",
            "reconciliation_template": "RECONCILIATION.md",
            "review_flags": "REVIEW-FLAGS.md",
            "report_schema": "data/schema/report.v1.json",
            "report_json_dir": "data/reports/",
            "history_json": "data/history.json",
            "base_rates_json": "data/base-rates.json",
            "public_addresses": "data/public-addresses.json",
            "dead_json": "data/dead.json",
            "review_flags_json": "data/review-flags.json",
        }
    )
    index["paths"] = paths
    index["timezone"] = "MST"
    index["generated_at"] = now_mst_label()
    # Keep existing daily_reports; refresh token_notes with json paths for scored reports.
    by_id = {r["ticker"]: r for r in recs}
    notes = []
    existing = index.get("token_notes") or []
    seen = set()
    for note in existing:
        ticker = note.get("id")
        if ticker in by_id:
            note = dict(note)
            note["path"] = f"banking-rails/{ticker}.md"
            note["json"] = f"data/reports/{ticker}.json"
            note["layout"] = "v3"
            notes.append(note)
            seen.add(ticker)
        else:
            notes.append(note)
            if ticker:
                seen.add(ticker)
    for rec in recs:
        if rec["ticker"] not in seen:
            notes.append(
                {
                    "id": rec["ticker"],
                    "path": f"banking-rails/{rec['ticker']}.md",
                    "json": f"data/reports/{rec['ticker']}.json",
                    "layout": "v3",
                }
            )
    notes.sort(key=lambda n: n.get("id") or "")
    index["token_notes"] = notes
    index["scored_reports"] = len(recs)
    write_json(INDEX_JSON, index)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skip-history", action="store_true", help="Do not walk git history")
    parser.add_argument("--skip-extract", action="store_true", help="Reuse existing data/reports JSON")
    args = parser.parse_args(argv)

    if args.skip_extract:
        recs = [json.loads(p.read_text(encoding="utf-8")) for p in sorted(OUT_REPORTS.glob("*.json"))]
        print(f"Loaded {len(recs)} existing files from data/reports/")
    else:
        recs = extract_all()
        print(f"Wrote {len(recs)} files under data/reports/")

    errors = validate_all()
    if errors:
        print(f"{len(errors)} validation error(s):", file=sys.stderr)
        for e in errors[:40]:
            print(f"  {e}", file=sys.stderr)
        if len(errors) > 40:
            print(f"  ... {len(errors) - 40} more", file=sys.stderr)
        return 1
    print(f"Validated {len(recs)} report JSON files.")

    if not args.skip_history:
        history = collect_history()
        write_json(HISTORY_JSON, history)
        HISTORY_MD.write_text(render_history_md(history), encoding="utf-8")
        print(f"Wrote {HISTORY_JSON.relative_to(ROOT)} and {HISTORY_MD.name}")
    else:
        print("Skipped git history.")

    rates = compute_base_rates(recs)
    write_json(RATES_JSON, rates)
    RATES_MD.write_text(render_base_rates_md(rates), encoding="utf-8")
    print(f"Wrote {RATES_JSON.relative_to(ROOT)} and {RATES_MD.name}")

    addresses = collect_addresses(recs)
    write_json(ADDR_JSON, addresses)
    print(f"Wrote {ADDR_JSON.relative_to(ROOT)} ({addresses['count']} unique addresses)")

    flags = collect_flags(recs)
    write_json(FLAGS_JSON, flags)
    FLAGS_MD.write_text(render_flags_md(flags), encoding="utf-8")
    print(
        f"Wrote {FLAGS_JSON.relative_to(ROOT)} and {FLAGS_MD.name} "
        f"(low={len(flags['low_confidence_selling_or_holdings'])}, "
        f"arkham={len(flags['single_source_arkham_selling_or_holdings'])}, "
        f"revenue={len(flags['revenue_accrual_inconsistent'])})"
    )

    dead = build_dead_list()
    write_json(DEAD_JSON, dead)
    DEAD_MD.write_text(render_dead_md(dead), encoding="utf-8")
    print(f"Wrote {DEAD_JSON.relative_to(ROOT)} and {DEAD_MD.name} ({len(dead['entries'])} entries)")

    update_index(recs)
    print(f"Updated {INDEX_JSON.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
