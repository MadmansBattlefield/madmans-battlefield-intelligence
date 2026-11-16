#!/usr/bin/env python3
"""Extract published v3 Markdown reports into data/reports/<TICKER>.json.

Only git-tracked files under banking-rails/ that have v3 front matter are
read. Untracked drafts are ignored. Paths written into the JSON are repo-
relative (banking-rails/TICKER.md), never machine-local paths.

Usage (from the repository root):

    python3 scripts/extract_reports.py
    python3 scripts/extract_reports.py --ticker SKY
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
REPORTS_DIR = ROOT / "banking-rails"
OUT_DIR = ROOT / "data" / "reports"
SCHEMA_VERSION = "report.v1"
MST = timezone(timedelta(hours=-7))

SKIP_NAMES = {
    "COVER.md",
    "RANKING.md",
    "ALL-PROJECTS.md",
    "README.md",
    "other-tokens.md",
}

SECTION_KEYS = [
    "revenue",
    "foundation_team",
    "insider_holdings",
    "selling_behavior",
    "tokenomics_supply",
    "liquidity_market",
    "product_development",
    "adoption_customers",
    "security_audits",
    "regulatory",
    "catalysts",
]

FRONT_MATTER_CORE = {
    "ticker",
    "name",
    "chain",
    "contract",
    "overall_score",
    "overall_verdict",
    "section_scores",
    "gates_failed",
    "red_lines",
    "price_usd",
    "price_source",
    "last_updated",
    "layout_version",
}

SECTION_TITLES = {
    "revenue": "💰 Revenue",
    "foundation_team": "🏛️ Foundation",
    "insider_holdings": "🪙 Foundation / team holdings",
    "selling_behavior": "📉 Selling behavior",
    "tokenomics_supply": "📊 Tokenomics",
    "liquidity_market": "💧 Liquidity",
    "product_development": "🧑‍💻 Product",
    "adoption_customers": "🤝 Adoption",
    "security_audits": "🛡️ Security",
    "regulatory": "⚖️ Regulatory",
    "catalysts": "📅 Catalysts",
}

EXPLORER_HOST_CHAIN = {
    "etherscan.io": "ethereum",
    "cn.etherscan.com": "ethereum",
    "bscscan.com": "bsc",
    "polygonscan.com": "polygon",
    "arbiscan.io": "arbitrum",
    "basescan.org": "base",
    "optimistic.etherscan.io": "optimism",
    "snowtrace.io": "avalanche",
    "ftmscan.com": "fantom",
    "gnosisscan.io": "gnosis",
    "lineascan.build": "linea",
    "scrollscan.com": "scroll",
    "mantlescan.xyz": "mantle",
    "sonicscan.org": "sonic",
    "hyperevmscan.io": "hyperevm",
    "solscan.io": "solana",
    "solana.fm": "solana",
    "explorer.solana.com": "solana",
    "tronscan.org": "tron",
    "tronscan.io": "tron",
    "stellar.expert": "stellar",
    "horizon.stellar.org": "stellar",
    "blockchair.com": None,
    "mempool.space": "bitcoin",
    "blockstream.info": "bitcoin",
    "btc.com": "bitcoin",
    "hashscan.io": "hedera",
    "explorer.sui.io": "sui",
    "suiscan.xyz": "sui",
    "aptoscan.com": "aptos",
    "explorer.aptoslabs.com": "aptos",
    "xrpscan.com": "xrp",
    "livenet.xrpl.org": "xrp",
    "cardanoscan.io": "cardano",
    "cexplorer.io": "cardano",
    "mintscan.io": None,
    "www.mintscan.io": None,
    "www.oklink.com": None,
    "oklink.com": None,
    "polkadot.subscan.io": "polkadot",
    "kusama.subscan.io": "kusama",
    "polymesh.subscan.io": "polymesh",
    "atomscan.com": "cosmos",
    "tzkt.io": "tezos",
    "tezblock.io": "tezos",
    "nearblocks.io": "near",
    "tonviewer.com": "ton",
    "tonscan.org": "ton",
    "explorer.injective.network": "injective",
    "www.mintscan.io": None,
    "algoexplorer.io": "algorand",
    "explorer.perawallet.app": "algorand",
    "purrsec.com": None,
    "hypurrscan.io": "hyperliquid",
    "intel.arkm.com": None,
    "arkm.com": None,
}

EXCHANGE_LABEL_RE = re.compile(
    r"\b(binance|coinbase|kraken|kucoin|ku-?coin|okx|okex|bybit|bitfinex|"
    r"bitget|gate(?:\.io)?|mexc|upbit|bithumb|htx|huobi|poloniex|gemini|"
    r"revolut|anchorage| falconx|wintermute|gsr|jump(?: trading)?|"
    r"wintermute|coinbase prime|binance deposit|kraken deposit)\b",
    re.I,
)

# Entity-ish Arkham / explorer labels we treat as more than a raw address.
ENTITY_HINT_RE = re.compile(
    r"\b(foundation|treasury|team|dao|multisig|safe|lab|protocol|labs|"
    r"association|foundation|deployer|issuer|reserve|ecosystem|grant)\b",
    re.I,
)

UNLABELLED_RE = re.compile(
    r"\b(unlabell?ed|no owner label|no entity label|not labell?ed|"
    r"prediction(?: label)?|pink(?:-|\s)?label|predicted label)\b",
    re.I,
)

PUMP_SALE_YES_RE = re.compile(
    r"(sold|sale|sent|deposit(?:ed|s)?|swept|moved|reached)\b.{0,80}\bpump(?:[ -]?day)?s?\b"
    r"|\bpump(?:[ -]?day)?s?\b.{0,80}\b(sold|sale|sent|deposit(?:ed|s)?|swept|moved|reached)",
    re.I | re.S,
)

NO_DISCLOSURE_RE = re.compile(
    r"(no disclosure found|without disclosure|undisclosed|not disclosed|none disclosed)",
    re.I,
)

FORMAL_DISCLOSURE_RE = re.compile(
    r"\b(official (?:blog|announcement|report|post)|transparency report|"
    r"disclosed (?:in|via|by|on)|governance (?:vote|spell|proposal)|"
    r"formally announced|press release)\b",
    re.I,
)

BURIED_DISCLOSURE_RE = re.compile(
    r"\b(partly (?:disclosed|explained)|partially disclosed|buried|"
    r"mentioned in (?:a |the )?(?:report|footnote|update)|quietly disclosed)\b",
    re.I,
)

NOT_PROVEN_RE = re.compile(r"\bnot proven\b", re.I)
NONE_FOUND_RE = re.compile(
    r"\b(none found|no (?:large )?pump-day sale found|no cex deposit found|"
    r"no exchange outflow|none on the \d+ pump days|not on a pump day)\b",
    re.I,
)

HOLDERS_YES_RE = re.compile(
    r"\b(reaches holders|reach(?:es)? (?:the )?token|holders? (?:do )?get|"
    r"paid to (?:the )?stakers|paid to \w+ (?:holders|stakers)|"
    r"holders revenue|fee share (?:to|for) holders|buy-and-burn|"
    r"smart burn engine|soap (?:flow|burn)|eip-?1559 burn|"
    r"fees? (?:are|is) (?:paid|burned)|burns? part of (?:it|fees)|"
    r"real, measurable fee burn)\b",
    re.I,
)

HOLDERS_NO_RE = re.compile(
    r"\b(none of it reaches holders|token gets no share|token (?:has )?no claim on revenue|"
    r"no live buyback|nothing accruing to holders|nothing (?:obliges|forces) .*? buy|"
    r"token earns nothing|token sees nothing|what it earns goes to (?:block producers|miners|the company)|"
    r"belongs to a company.*not to \w+ holders|no mechanism that returns value to holders|"
    r"no holder revenue|fees go to (?:miners|vault users|the company)|"
    r"the token gets almost none)\b",
    re.I,
)

PROMISE_ONLY_RE = re.compile(
    r"\b(will (?:buy back|burn|share fees)|plans to (?:buy back|burn)|"
    r"proposed (?:buyback|burn|fee share)|once (?:the )?(?:switch|fee switch) is on|"
    r"not (?:yet )?(?:live|executed|active))\b",
    re.I,
)

MECHANISM_PATTERNS = {
    "burn": re.compile(r"\b(buy-and-burn|buy and burn|fee burn|burn(?:s|ed|ing)?)\b", re.I),
    "buyback": re.compile(r"\b(buy-?backs?|repurchase[sd]?|bought (?:back|tokens))\b", re.I),
    "staking_yield_from_fees": re.compile(
        r"\b(stak(?:e|ing) (?:yield|reward|fees?|share)|paid to stakers|fees? (?:go|goes|paid) to stakers)\b",
        re.I,
    ),
    "fee_share": re.compile(r"\b(fee share|holders? revenue|revenue (?:share|split) to holders)\b", re.I),
}

URL_RE = re.compile(r"https?://[^\s)\]>\"']+")
MD_LINK_RE = re.compile(r"\[([^\]]*)\]\((https?://[^)\s]+)\)")
DATE_RE = re.compile(
    r"\b(\d{1,2} (?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) 202[4-7])\b"
)
READ_DATE_RE = re.compile(
    r"(?:read|checked)\s+(\d{1,2} (?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) 202[4-7](?:\s*[~,]?\s*\d{1,2}:\d{2}\s*(?:AM|PM)\s*MST)?)",
    re.I,
)
ARKHAM_READ_RE = re.compile(
    r"Arkham,\s*read\s+([^\])\n]+)",
    re.I,
)
PUMP_SOURCE_RE = re.compile(
    r"pump days from ([^;\n]+)",
    re.I,
)

# Address-like explorer paths.
ADDR_URL_RE = re.compile(
    r"https?://[^\s)\]>\"']+?(?:/(?:address|account|accounts|token/holder|tokenholder|"
    r"contract|accounts/id)/(?:#)?|#/(?:address|contract)/)"
    r"[^\s)\]>\"']+",
    re.I,
)

# Generic catch of explorer address URLs; refined in classify_url.
EXPLORER_URL_RE = re.compile(
    r"https?://(?:www\.)?(?:"
    r"etherscan\.io|bscscan\.com|polygonscan\.com|arbiscan\.io|basescan\.org|"
    r"optimistic\.etherscan\.io|snowtrace\.io|ftmscan\.com|gnosisscan\.io|"
    r"lineascan\.build|scrollscan\.com|mantlescan\.xyz|sonicscan\.org|"
    r"solscan\.io|solana\.fm|explorer\.solana\.com|"
    r"tronscan\.org|tronscan\.io|"
    r"stellar\.expert|"
    r"mempool\.space|blockstream\.info|"
    r"hashscan\.io|explorer\.sui\.io|suiscan\.xyz|aptoscan\.com|"
    r"xrpscan\.com|cardanoscan\.io|cexplorer\.io|"
    r"polkadot\.subscan\.io|kusama\.subscan\.io|polymesh\.subscan\.io|"
    r"nearblocks\.io|tonviewer\.com|"
    r"explorer\.perawallet\.app|algoexplorer\.io|"
    r"intel\.arkm\.com|arkm\.com|"
    r"hypurrscan\.io|hyperevmscan\.io|"
    r"blockchair\.com|oklink\.com|www\.oklink\.com|mintscan\.io|www\.mintscan\.io"
    r")[^\s)\]>\"']+",
    re.I,
)

ETH_ADDR_RE = re.compile(r"0x[a-fA-F0-9]{40}")
# Solana / generic base58 public keys in solscan paths
SOL_IN_URL_RE = re.compile(r"/(?:account|address|token)/([1-9A-HJ-NP-Za-km-z]{32,44})")
TRON_IN_URL_RE = re.compile(r"(?:/address/|#/address/)(T[1-9A-HJ-NP-Za-km-z]{33})")
STELLAR_IN_URL_RE = re.compile(r"/(?:account|address)/([G][A-Z0-9]{55})")

# Words that look like a private person's name; used only to strip labels.
PERSONAL_NAME_RE = re.compile(
    r"^(?:[A-Z][a-z]+ [A-Z][a-z]+(?: [A-Z][a-z]+)?)$"
)


def now_mst_label() -> str:
    return datetime.now(MST).strftime("%Y-%m-%d %H:%M MST")


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def git_tracked_reports() -> list[Path]:
    out = subprocess.check_output(
        ["git", "ls-files", "banking-rails/"],
        cwd=ROOT,
        text=True,
    )
    paths = []
    for rel in out.splitlines():
        name = Path(rel).name
        if not rel.endswith(".md") or name in SKIP_NAMES:
            continue
        path = ROOT / rel
        if path.is_file():
            paths.append(path)
    return sorted(paths)


def parse_front_matter(text: str) -> tuple[dict, str]:
    m = re.match(r"^---\n(.*?)\n---\n(.*)\Z", text, re.S)
    if not m:
        raise ValueError("missing YAML front matter")
    fm = yaml.safe_load(m.group(1)) or {}
    if not isinstance(fm, dict):
        raise ValueError("front matter is not a mapping")
    return fm, m.group(2)


def extract_section(text: str, title_part: str) -> str:
    pat = re.compile(
        r"^## [^\n]*" + re.escape(title_part) + r"[^\n]*\n(.*?)(?=^## |\Z)",
        re.S | re.M,
    )
    m = pat.search(text)
    return m.group(0) if m else ""


def extract_named_section(text: str, heading_part: str) -> str:
    pat = re.compile(
        r"^## [^\n]*" + re.escape(heading_part) + r"[^\n]*\n(.*?)(?=^## |\Z)",
        re.S | re.M,
    )
    m = pat.search(text)
    return m.group(0) if m else ""


def clean_url(url: str) -> str:
    return url.rstrip(").,;\"'<>")


def classify_url(url: str) -> tuple[str, str | None, str | None]:
    """Return (kind, chain, address_or_none). kind is tx/address/token/doc/other."""
    u = clean_url(url)
    low = u.lower()
    host = ""
    mhost = re.match(r"https?://([^/]+)", low)
    if mhost:
        host = mhost.group(1).removeprefix("www.")
    chain = EXPLORER_HOST_CHAIN.get(host)

    if "/tx/" in low or "/transaction/" in low or "/#/transaction/" in low or "/txhash/" in low:
        return "tx", chain, None
    if "/token/" in low and "/address/" not in low and "/account/" not in low:
        addr = _address_from_url(u, chain)
        return "token", chain, addr
    if any(
        p in low
        for p in (
            "/address/",
            "/account/",
            "/#/address/",
            "/accounts/",
            "explorer/address/",
        )
    ):
        addr = _address_from_url(u, chain)
        return "address", chain, addr
    if host.endswith("etherscan.io") or host.endswith("scan.com") or host.endswith("scan.io"):
        if "/tx/" in low:
            return "tx", chain, None
    # Official docs, github, filings, etc.
    if any(
        h in low
        for h in (
            "github.com",
            "docs.",
            "blog.",
            "medium.com",
            "sec.gov",
            "coingecko.com",
            "defillama.com",
            "prnewswire.com",
        )
    ):
        return "doc", chain, None
    return "other", chain, None


def _address_from_url(url: str, chain: str | None) -> str | None:
    u = clean_url(url)
    m = ETH_ADDR_RE.search(u)
    if m:
        return m.group(0).lower()
    m = TRON_IN_URL_RE.search(u)
    if m:
        return m.group(1)
    m = STELLAR_IN_URL_RE.search(u)
    if m:
        return m.group(1)
    m = SOL_IN_URL_RE.search(u)
    if m and (chain == "solana" or "solscan" in u or "solana" in u):
        return m.group(1)
    # Generic path tail for other explorers (Hedera 0.0.x, XRP r..., etc.)
    m = re.search(r"/(?:address|account|accounts)(?:/id)?/([^/?#]+)", u, re.I)
    if m:
        val = m.group(1)
        if val.startswith("0x") and len(val) != 42:
            return None  # likely a tx hash mis-captured
        if re.fullmatch(r"0x[a-fA-F0-9]{64}", val):
            return None
        return val
    m = re.search(r"#/(?:address|contract)/([^/?#]+)", u, re.I)
    if m:
        return m.group(1)
    return None


def parse_evidence_table(text: str) -> list[dict]:
    block = extract_named_section(text, "🔗 Evidence trail")
    if not block:
        return []
    rows = []
    for raw_line in block.splitlines():
        line = raw_line.strip()
        if not line.startswith("|"):
            continue
        cols = [c.strip() for c in line.strip("|").split("|")]
        if len(cols) < 2:
            continue
        if cols[0].lower() in {"claim", ""} or set(cols[0]) <= {"-", ":"}:
            continue
        claim = cols[0]
        links = cols[1] if len(cols) > 1 else ""
        tier = cols[2] if len(cols) > 2 else None
        date_read = cols[3] if len(cols) > 3 else None
        if date_read:
            date_read = date_read.strip() or None
        if tier:
            tier = re.sub(r"\s+", " ", tier).strip() or None
        urls = [clean_url(m[1]) for m in MD_LINK_RE.finditer(links)]
        if not urls:
            urls = [clean_url(u) for u in URL_RE.findall(links)]
        for url in urls:
            kind, _chain, _addr = classify_url(url)
            rows.append(
                {
                    "claim": claim,
                    "url": url,
                    "kind": kind,
                    "tier": tier,
                    "date_read": date_read,
                }
            )
    return rows


def parse_sources(text: str) -> list[dict]:
    block = extract_named_section(text, "📚 Sources")
    if not block:
        return []
    items = []
    for line in block.splitlines():
        s = line.strip()
        if not s.startswith("- "):
            continue
        body = s[2:].strip()
        tier = None
        tm = re.match(r"\[Tier\s+([A-Ca-c]|Unverified)\]\s*", body, re.I)
        if tm:
            tier = tm.group(1)
            if tier.lower() != "unverified":
                tier = tier.upper()
            else:
                tier = "Unverified"
        urls = [clean_url(m[1]) for m in MD_LINK_RE.finditer(body)]
        dm = DATE_RE.search(body)
        items.append(
            {
                "tier": tier,
                "text": body,
                "urls": urls,
                "date_read": dm.group(1) if dm else None,
            }
        )
    return items


def source_read_dates(text: str, fm: dict) -> tuple[list[str], str | None, str | None]:
    dates = set()
    for m in DATE_RE.finditer(text):
        # Keep calendar dates that appear next to "read" or in price_source / evidence.
        dates.add(m.group(1))
    read_hits = [m.group(1).strip() for m in READ_DATE_RE.finditer(text)]
    price_read = fm.get("price_source")
    arkham = None
    am = ARKHAM_READ_RE.search(text)
    if am:
        arkham = am.group(1).strip().rstrip(").;]")
        # Keep it short
        arkham = re.sub(r"\s+", " ", arkham)[:160]
    # Prefer explicitly "read" dates when present, plus last_updated and price_source.
    ordered = []
    seen = set()
    for item in read_hits + ([str(fm.get("last_updated"))] if fm.get("last_updated") else []):
        if item and item not in seen:
            seen.add(item)
            ordered.append(item)
    # Fallback: unique dates that showed up (capped, stable).
    if not ordered:
        ordered = sorted(dates)
    return ordered, str(price_read) if price_read else None, arkham


def extract_addresses(text: str, default_chain: str | None) -> list[dict]:
    found: dict[tuple[str, str], dict] = {}
    for m in EXPLORER_URL_RE.finditer(text):
        url = clean_url(m.group(0))
        kind, chain, addr = classify_url(url)
        if kind not in {"address", "token"} or not addr:
            continue
        # Skip obvious transaction hashes used as path segments
        if re.fullmatch(r"0x[a-fA-F0-9]{64}", addr):
            continue
        key = (chain or default_chain or "", addr)
        if key not in found:
            found[key] = {
                "chain": chain or default_chain,
                "address": addr,
                "url": url,
                "kind": kind,
            }
    return sorted(found.values(), key=lambda r: (r.get("chain") or "", r["address"], r["url"]))


def sanitize_label(label: str | None) -> str | None:
    if not label:
        return None
    label = re.sub(r"\s+", " ", label).strip().strip("\"'`")
    if not label:
        return None
    # Drop ENS / handles that look like a private person.
    if re.search(r"\.eth\b", label, re.I):
        # Keep only clearly project-style labels (contain Foundation, Treasury, Protocol, etc.)
        if not ENTITY_HINT_RE.search(label):
            return "project or individual-labelled wallet"
    if PERSONAL_NAME_RE.match(label):
        return "a named individual"
    if len(label) > 80:
        label = label[:77] + "..."
    return label


def _nearby(text: str, start: int, end: int, window: int = 280) -> str:
    return text[max(0, start - window) : min(len(text), end + window)]


def extract_attributions(text: str, selling: str, holdings: str, red_lines: dict) -> list[dict]:
    """Pull Arkham / explorer label attributions and assign confidence."""
    attributions: dict[str, dict] = {}
    sell_hold_blob = (selling or "") + "\n" + (holdings or "") + "\n" + json.dumps(red_lines or {}, default=str)

    def upsert(addr, url, label, source, confidence, corroboration, sources, kind, appears):
        key = (addr or url or label or "") + "|" + source
        if not key.strip("|"):
            return
        prev = attributions.get(key)
        rec = {
            "address": addr,
            "url": url,
            "label": sanitize_label(label),
            "source": source,
            "confidence": confidence,
            "independent_corroboration": bool(corroboration),
            "corroborating_sources": sources,
            "label_kind": kind,
            "appears_in_selling_or_holdings": bool(appears),
        }
        if prev:
            # Upgrade confidence / corroboration if a later mention is stronger.
            rank = {"low": 0, "medium": 1, "high": 2}
            if rank[confidence] > rank[prev["confidence"]]:
                prev["confidence"] = confidence
                prev["label_kind"] = kind
            if rec["independent_corroboration"]:
                prev["independent_corroboration"] = True
            for s in sources:
                if s not in prev["corroborating_sources"]:
                    prev["corroborating_sources"].append(s)
            prev["appears_in_selling_or_holdings"] = prev["appears_in_selling_or_holdings"] or appears
            if rec["label"] and not prev["label"]:
                prev["label"] = rec["label"]
        else:
            attributions[key] = rec

    # Arkham address links, with surrounding label text.
    for m in re.finditer(
        r"https?://(?:intel\.)?arkm\.com/explorer/address/([0-9a-zA-Z]+)",
        text,
        re.I,
    ):
        addr = m.group(1)
        url = clean_url(m.group(0))
        if addr.startswith("0x") and len(addr) == 42:
            addr = addr.lower()
        nearby = _nearby(text, m.start(), m.end(), 350)
        appears = addr.lower() in sell_hold_blob.lower() or url.lower() in sell_hold_blob.lower() or bool(
            re.search(re.escape(addr[:10]), sell_hold_blob, re.I)
        )
        label = None
        lm = re.search(
            r'(?:Arkham(?:-)?\s*(?:labels?|labelled|labeled)\s+(?:(?:the|this|it|as)\s+)*)["“]?([^\"”\n,]{3,80})["”]?',
            nearby,
            re.I,
        )
        if lm:
            label = lm.group(1)
        quoted = re.findall(r'["“]([^"”]{3,80})["”]', nearby)
        if quoted and not label:
            label = quoted[0]

        if UNLABELLED_RE.search(nearby):
            upsert(addr, url, label or "unlabelled", "arkham", "low", False, [], "unlabelled", appears)
            continue

        sources = ["arkham"]
        corroboration = False
        kind = "unknown"
        confidence = "medium"

        if EXCHANGE_LABEL_RE.search(nearby) or (label and EXCHANGE_LABEL_RE.search(label)):
            kind = "exchange"
            confidence = "medium"
        elif label and ENTITY_HINT_RE.search(label):
            kind = "verified_entity"
            confidence = "medium"
        elif "prediction" in nearby.lower() or "pink" in nearby.lower():
            kind = "prediction"
            confidence = "low"

        # Independent corroboration: Etherscan/Solscan/official mention of same address in nearby or globally with a label.
        if re.search(r"\b(etherscan|bscscan|polygonscan|solscan|tronscan|explorer)[- ]labelled\b", nearby, re.I):
            corroboration = True
            sources.append("explorer")
            confidence = "high"
        if re.search(r"\b(official|docs?|spell|vote|governance|on-chain proof|named in the)\b", nearby, re.I):
            if "Arkham" in nearby:
                # official + arkham in the same window often means two sources
                if re.search(r"\b(spell|vote|docs?|official)\b", nearby, re.I):
                    corroboration = True
                    if "official" not in sources:
                        sources.append("official")
                    if confidence != "low":
                        confidence = "high"
                        if kind == "unknown":
                            kind = "official"

        # A second URL to a non-Arkham explorer in the same sentence / table cell.
        other_links = [clean_url(u) for u in URL_RE.findall(nearby)]
        if any(
            ("etherscan" in u or "solscan" in u or "tronscan" in u or "scan.com" in u)
            and "arkm" not in u
            for u in other_links
        ):
            # Presence of an explorer link is on-chain proof of the *address*, not of the *label*,
            # unless the explorer also labels it. Keep corroboration only if already set or explorer-labelled.
            if "explorer" not in sources:
                sources.append("explorer-link")

        upsert(addr, url, label, "arkham", confidence, corroboration, sources, kind, appears)

    # Mentions of unlabelled / prediction without a parsed URL, in selling/holdings.
    for block, appears in ((selling, True), (holdings, True), (text, False)):
        if not block:
            continue
        if UNLABELLED_RE.search(block):
            # Only add a generic record if we don't already have a low-confidence one from this block's addresses.
            if appears:
                upsert(
                    None,
                    None,
                    "unlabelled or unattributed wallet mentioned in Selling or Holdings",
                    "report",
                    "low",
                    False,
                    [],
                    "unlabelled",
                    True,
                )

    return list(attributions.values())


def classify_pump(fm: dict, selling: str, text: str) -> dict:
    red = fm.get("red_lines") or {}
    red_blob = " ".join(str(v) for v in red.values())
    sell_score = int(fm["section_scores"]["selling_behavior"])
    blob = selling + "\n" + red_blob

    flags = []
    for key, val in red.items():
        if re.search(r"pump", str(key), re.I) or re.search(r"pump", str(val), re.I):
            flags.append(f"{key}: {val}")

    # Price source used for the pump test, if the Sources section states it.
    pump_source = None
    sm = PUMP_SOURCE_RE.search(text)
    if sm:
        pump_source = sm.group(1).strip().rstrip(".")
        # Cut at sentence or parenthesis remainder if huge
        pump_source = re.split(r"\s+\(|;|\.\s", pump_source)[0].strip()[:200]

    not_proven = bool(sell_score == 4 or NOT_PROVEN_RE.search(blob))
    # "not proven" in a red line that still describes a different finding should stay not_proven if that's the conclusion.
    proven: str
    if not_proven and not re.search(r"\byes\b.{0,40}pump", blob, re.I):
        proven = "no"
    elif NONE_FOUND_RE.search(blob) and not PUMP_SALE_YES_RE.search(blob):
        proven = "no"
    elif PUMP_SALE_YES_RE.search(blob) and not NOT_PROVEN_RE.search(blob):
        # Guard: "none on the pump days" should not count as yes.
        if re.search(r"\bnone (?:found )?on (?:the )?(?:\d+ )?pump days\b", blob, re.I) and not re.search(
            r"\byes\b.{0,30}pump", blob, re.I
        ):
            proven = "no"
        else:
            proven = "yes"
    elif sell_score <= 3 and re.search(r"pump", blob, re.I) and not NONE_FOUND_RE.search(blob):
        proven = "yes"
    elif re.search(r"pump", blob, re.I):
        proven = "unclear"
    else:
        proven = "no"

    # Disclosure quality applies when a pump-day sale was found (or claimed).
    if proven == "no" and not_proven:
        disclosure = "not_applicable"
    elif proven == "no":
        disclosure = "not_applicable"
    elif NO_DISCLOSURE_RE.search(blob) and not FORMAL_DISCLOSURE_RE.search(blob):
        disclosure = "silence"
    elif BURIED_DISCLOSURE_RE.search(blob):
        disclosure = "buried_disclosure"
    elif FORMAL_DISCLOSURE_RE.search(blob) or re.search(r"\bdisclosed\b", blob, re.I):
        if re.search(r"\bpartly disclosed\b|\bpartially disclosed\b", blob, re.I):
            disclosure = "buried_disclosure"
        else:
            disclosure = "formal_announcement"
    elif proven == "yes":
        disclosure = "unclear"
    else:
        disclosure = "unclear"

    return {
        "definition": "utc_daily_close_at_least_10pct_above_close_5_days_earlier",
        "price_source": pump_source,
        "timezone": "UTC",
        "lookback_days": 5,
        "threshold_pct": 10,
        "methodology_effective_from": "2026-11-16",
        "rescored_under_effective_rules": False,
        "proven_pump_day_sale": proven,
        "selling_not_proven": bool(sell_score == 4 or (not_proven and proven != "yes")),
        "disclosure_quality": disclosure,
        "pump_day_undisclosed_penalty_applied": False,
        "flags_noted_in_report": flags[:12],
    }


def classify_revenue(fm: dict, revenue_section: str) -> dict:
    blob = revenue_section or ""
    means_m = re.search(
        r"\*\*What it means:\*\*\s*(.*?)(?:\n\n|\n## |\Z)", blob, re.S
    )
    means = means_m.group(1).strip() if means_m else ""
    notes_src = means or blob
    notes = re.sub(r"\s+", " ", notes_src).strip()
    if len(notes) > 400:
        notes = notes[:397] + "..."

    # Decide from the conclusion first, then the rest of the section.
    decision_text = (means + "\n" + blob) if means else blob

    mechanisms = []
    live_mech = re.compile(
        r"\b(?:automatic|on-chain|real-time|in real time|paid to stakers|"
        r"holders revenue|smart burn|buy-and-burn|fee burn|"
        r"buybacks? took|burned [0-9]|$[0-9].{0,40}burn)\b",
        re.I,
    )
    for name, pat in MECHANISM_PATTERNS.items():
        # A bare word in a DefiLlama table header is not enough.
        if pat.search(means) or (pat.search(blob) and live_mech.search(blob)):
            mechanisms.append(name)

    score = int(fm["section_scores"]["revenue"])

    strong_no = re.compile(
        r"\b(none of it reaches holders|none of it is paid to holders|none of (?:it|this) reaches(?: the)?(?: token| holders)?"
        r"|token gets no share|token (?:has )?no claim on revenue"
        r"|no live buyback|nothing accruing to holders"
        r"|no mechanism that returns value to holders"
        r"|the token sees nothing|no checkable revenue reaches the token"
        r"|no holder revenue|none of it reaches \w+"
        r"|does not reach(?: the)?(?: token| holders)?"
        r"|token (?:earns|got|gets) (?:nothing|almost none)"
        r"|all of (?:its|the) (?:yield|revenue|fees) goes? to (?:LPs|lenders|the company|a treasury|block producers|miners)"
        r"|stakers are paid in newly minted"
        r"|fees pay \S+ stakers and the reserve fund, not"
        r"|nothing obliges the company to keep buying"
        r"|the token has no claim on revenue"
        r"|no business revenue flows to the token"
        r"|what it earns goes to (?:block producers|miners|the company))\b",
        re.I,
    )
    strong_yes = re.compile(
        r"\b(reaches holders(?: as reduced supply|:? about|:? )"
        r"|some cash now reaches holders"
        r"|holders do get (?:value|paid|it)"
        r"|paid to stakers in real time"
        r"|the token earns real fees, and they are paid to stakers"
        r"|sends about half of net revenue to .{0,20}holders"
        r"|burns part of it for every holder"
        r"|real, measurable fee burn"
        r"|the burn is real and reaches every holder"
        r"|most goes to stakers, a little is burned"
        r"|paid to (?:SKY |.? )?holders"
        r"|on-chain burns? match"
        r"|100% of SOAP flow buys and burns)\b",
        re.I,
    )
    discretionary = re.compile(
        r"\b(optional|nothing (?:obliges|forces)|discretionary|"
        r"not a dividend|held in the treasury rather than burned|"
        r"no live buyback|token has no claim|"
        r"goes to a treasury the token holders vote on|"
        r"lands in a treasury that governance spends)\b",
        re.I,
    )

    no_hit = strong_no.search(decision_text)
    yes_hit = strong_yes.search(decision_text)
    disc_hit = discretionary.search(decision_text)
    promise = PROMISE_ONLY_RE.search(decision_text) and not re.search(
        r"\b(already|executed|live|paid to stakers|buybacks? took)\b", decision_text, re.I
    )

    automatic = None
    executed = None
    reaches: str

    if no_hit and not yes_hit:
        reaches = "no"
        automatic = False
        executed = False
    elif no_hit and yes_hit:
        # Conclusion both praises a small mechanism and says holders get almost nothing.
        # Treat as no when the section says the token gets almost none / no share.
        reaches = "no"
        automatic = False
        executed = True if mechanisms else False
    elif yes_hit and not promise:
        reaches = "yes"
        automatic = not bool(disc_hit)
        executed = True
    elif mechanisms and disc_hit:
        reaches = "unclear"
        automatic = False
        executed = True
    elif mechanisms and re.search(
        r"\b(buybacks? took|paid to stakers|holders revenue|burned [0-9]|fee burn)\b",
        decision_text,
        re.I,
    ):
        reaches = "unclear"
        automatic = None
        executed = True
    else:
        reaches = "unclear"
        automatic = None
        executed = None

    # Inconsistency flags (do not change the published score):
    # - Score is at or above the hard-gate floor, but the test is a clear no.
    # - Score is a section pass, but the test is not yes.
    # - Test is a clear yes with a live mechanism, yet the hard gate still tripped.
    #   (Only then: a tiny residual burn plus a 1–2 score is usually consistent.)
    inconsistent = False
    if reaches == "no" and score >= 4:
        inconsistent = True
    if score >= 6 and reaches != "yes":
        inconsistent = True
    if reaches == "yes" and score <= 3 and mechanisms and not re.search(
        r"(rounds to zero|no revenue|effectively no business|about 0\.\d%|tiny|"
        r"does not cover|small for a|trips the Revenue gate|which trips the Revenue gate|"
        r"on a \$[0-9]|[0-9]% of (?:market cap|issuance)|\$[0-9.]+[Kk]\s+a year)",
        decision_text,
        re.I,
    ):
        inconsistent = True

    return {
        "reaches_holders": reaches,
        "mechanisms": mechanisms,
        "automatic_onchain": automatic,
        "executed": executed,
        "inconsistent_with_score": inconsistent,
        "notes": notes or None,
    }



def key_numbers(fm: dict, body: str) -> dict:
    out: dict = {}
    if fm.get("price_usd") is not None:
        out["price_usd"] = fm["price_usd"]
    m = re.search(r"\*\*Market cap\*\*\s*\$([0-9.,]+\s*[KMBT]?)", body)
    if m:
        out["market_cap_text"] = "$" + m.group(1).strip()
    m = re.search(r"\*\*FDV\*\*\s*\$([0-9.,]+\s*[KMBT]?)", body)
    if m:
        out["fdv_text"] = "$" + m.group(1).strip()
    m = re.search(r"\*\*24h volume\*\*\s*\$([0-9.,]+\s*[KMBT]?)", body, re.I)
    if m:
        out["volume_24h_text"] = "$" + m.group(1).strip()
    m = re.search(r"\*\*`?totalSupply\(\)`?\*\*\s*([0-9][0-9,.]*)", body)
    if m:
        out["total_supply_text"] = m.group(1)
    return out


def review_flags(pump: dict, revenue: dict, attributions: list[dict], fm: dict, selling: str = "", holdings: str = "") -> dict:
    notes = []
    low_flag = False
    single_arkham = False
    sell = int(fm["section_scores"]["selling_behavior"])
    hold = int(fm["section_scores"]["insider_holdings"])
    red = fm.get("red_lines") or {}
    blob = (selling or "") + "\n" + (holdings or "") + "\n" + json.dumps(red, default=str)

    low_atts = [
        a
        for a in attributions
        if a.get("appears_in_selling_or_holdings")
        and a["confidence"] == "low"
        and not a["independent_corroboration"]
        and a.get("label_kind") in {"unlabelled", "prediction"}
    ]
    # Only flag a published score when Selling or Holdings already moved
    # (a fail, or a pass that treats an unlabelled wallet as the team) on the
    # back of a low-confidence label with no second source. A Selling score of
    # 4 (not proven) because the wallet was unlabelled is the rule working.
    if low_atts and sell <= 3:
        # Did the report still treat an unlabelled wallet as the insider seller?
        if re.search(
            r"(unlabell?ed|prediction|no owner label).{0,120}(team|foundation|treasury|insider|seller)"
            r"|(team|foundation|treasury|insider).{0,120}(unlabell?ed|prediction|no owner label)",
            blob,
            re.I | re.S,
        ):
            low_flag = True
            notes.append(
                "Selling failed, and the report links the flow to the team or treasury through "
                "an unlabelled or prediction attribution with no independent corroboration."
            )
        else:
            notes.append(
                "Selling failed, and unlabelled wallets appear in the trail. The team or treasury "
                "link may rest on funding hops rather than a low-confidence name tag; listed for review, not auto-flagged as a silent score move."
            )
    elif low_atts and sell == 4:
        notes.append(
            "Low-confidence or unlabelled attribution appears in Selling or Holdings; "
            "Selling is 4 (not proven), which matches the rule that such a label cannot move the score alone."
        )

    # Single-source Arkham entity/exchange labels that appear to identify the
    # seller or a large insider holder, with no second source parsed.
    entity_atts = [
        a
        for a in attributions
        if a.get("appears_in_selling_or_holdings")
        and a.get("source") == "arkham"
        and not a["independent_corroboration"]
        and a["confidence"] in {"medium", "high"}
        and a.get("label_kind") == "verified_entity"
    ]
    score_moved = bool(
        re.search(
            r"(selling|holdings).{0,40}(\d\s*[→\-]\s*\d)|"
            r"(downgraded|upgraded|score change)\s+after Arkham|"
            r"Arkham pass.{0,200}(selling|holdings|score).{0,80}(→|->|changed|downgrad|upgrad)",
            blob,
            re.I | re.S,
        )
    )
    if entity_atts and (sell <= 3 or score_moved):
        single_arkham = True
        notes.append(
            "An Arkham team, foundation or entity label in Selling or Holdings has no second "
            "independent source parsed from the report, and that section failed or records a score change."
        )
    elif entity_atts:
        notes.append(
            "Arkham entity labels appear in Selling or Holdings without a second source parsed. "
            "They are recorded on the JSON but not auto-flagged, because the published score may not have depended on them alone."
        )

    seen = set()
    uniq = []
    for n in notes:
        if n not in seen:
            seen.add(n)
            uniq.append(n)

    return {
        "selling_holdings_low_confidence_flag": low_flag,
        "selling_holdings_single_source_arkham_flag": single_arkham,
        "revenue_accrual_inconsistent": bool(revenue.get("inconsistent_with_score")),
        "flag_notes": uniq,
        "dual_review": {
            "status": "not_run",
            "threshold_points": 2,
            "selling_behavior": {
                "scorer_a": None,
                "scorer_b": None,
                "delta": None,
                "reconciliation_note": None,
            },
            "insider_holdings": {
                "scorer_a": None,
                "scorer_b": None,
                "delta": None,
                "reconciliation_note": None,
            },
        },
    }



def extract_one(path: Path, extracted_at: str | None = None) -> dict:
    text = path.read_text(encoding="utf-8")
    fm, body = parse_front_matter(text)
    def _as_str(val):
        if val is None:
            return None
        if isinstance(val, bool):
            return str(val).lower()
        return str(val)

    ticker = str(fm["ticker"]).upper()
    scores = fm["section_scores"]
    for key in SECTION_KEYS:
        if key not in scores:
            raise ValueError(f"{ticker}: missing section score {key}")
        scores[key] = int(scores[key])
    overall = float(fm["overall_score"])
    verdict = str(fm["overall_verdict"]).upper()
    if verdict not in {"PASS", "FAIL"}:
        raise ValueError(f"{ticker}: bad verdict {verdict}")
    gates = list(fm.get("gates_failed") or [])
    # Normalize gate keys
    norm_gates = []
    for g in gates:
        g = str(g)
        if g in {"revenue", "selling_behavior"}:
            norm_gates.append(g)
        elif g in {"selling", "sell"}:
            norm_gates.append("selling_behavior")
        else:
            norm_gates.append(g)
    gates = norm_gates

    passed = sum(1 for k in SECTION_KEYS if scores[k] >= 6)
    hard = {
        "revenue": {
            "score": scores["revenue"],
            "threshold": 3,
            "tripped": scores["revenue"] <= 3,
        },
        "selling_behavior": {
            "score": scores["selling_behavior"],
            "threshold": 3,
            "tripped": scores["selling_behavior"] <= 3,
        },
    }
    # Confirm gates list matches scores; do not silently rewrite published YAML, but record as published.
    extras = {k: v for k, v in fm.items() if k not in FRONT_MATTER_CORE}

    selling = extract_section(text, SECTION_TITLES["selling_behavior"])
    holdings = extract_section(text, SECTION_TITLES["insider_holdings"])
    revenue_sec = extract_section(text, SECTION_TITLES["revenue"])

    evidence = parse_evidence_table(text)
    # Also collect explorer URLs that appear outside the evidence table so the
    # public address list is complete, tagged as kind only (no new claims).
    sources = parse_sources(text)
    addresses = extract_addresses(text, fm.get("chain"))
    dates, price_source, arkham_read = source_read_dates(text, fm)
    pump = classify_pump(fm, selling, text)
    revenue = classify_revenue(fm, revenue_sec)
    attributions = extract_attributions(text, selling, holdings, fm.get("red_lines") or {})
    review = review_flags(pump, revenue, attributions, fm, selling=selling, holdings=holdings)
    extracted_at = extracted_at or now_mst_label()

    rec = {
        "schema_version": SCHEMA_VERSION,
        "ticker": ticker,
        "name": fm.get("name") or ticker,
        "chain": fm.get("chain"),
        "contract": _as_str(fm.get("contract")),
        "overall_score": overall,
        "overall_verdict": verdict,
        "section_scores": {k: scores[k] for k in SECTION_KEYS},
        "sections_passed": passed,
        "gates_failed": gates,
        "hard_gates": hard,
        "red_lines": fm.get("red_lines") or {},
        "price_usd": fm.get("price_usd"),
        "price_source": fm.get("price_source"),
        "front_matter_extras": extras or {},
        "key_numbers": key_numbers(fm, body),
        "last_updated": str(fm.get("last_updated")),
        "layout_version": int(fm.get("layout_version") or 3),
        "source_markdown": {
            "path": f"banking-rails/{ticker}.md",
            "sha256": sha256_text(text),
            "bytes": len(text.encode("utf-8")),
            "extracted_at": extracted_at,
            "timezone_label": "MST",
        },
        "retrieval": {
            "price_source_read": price_source,
            "source_read_dates": dates,
            "arkham_read": arkham_read,
        },
        "evidence_links": evidence,
        "addresses_examined": addresses,
        "pump_day_test": pump,
        "revenue_accrual": revenue,
        "attributions": attributions,
        "review": review,
        "sources": sources,
    }
    # other_contracts if present in extras? keep only in extras to avoid schema mismatch
    if "other_contracts" in extras:
        rec["other_contracts"] = extras["other_contracts"]
    return rec


def write_report_json(rec: dict, out_dir: Path = OUT_DIR) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"{rec['ticker']}.json"
    path.write_text(json.dumps(rec, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return path


def extract_all(tickers: set[str] | None = None) -> list[dict]:
    extracted_at = now_mst_label()
    recs = []
    for path in git_tracked_reports():
        ticker_guess = path.stem
        if tickers and ticker_guess not in tickers:
            continue
        try:
            rec = extract_one(path, extracted_at=extracted_at)
        except Exception as exc:  # noqa: BLE001 — surface every parse failure
            raise SystemExit(f"Failed to extract {path.name}: {exc}") from exc
        write_report_json(rec)
        recs.append(rec)
    recs.sort(key=lambda r: r["ticker"])
    return recs


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ticker", action="append", help="Extract only this ticker (repeatable)")
    args = parser.parse_args(argv)
    tickers = {t.upper() for t in args.ticker} if args.ticker else None
    recs = extract_all(tickers)
    print(f"Wrote {len(recs)} files under data/reports/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
