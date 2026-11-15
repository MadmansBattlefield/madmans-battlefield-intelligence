---
ticker: ONDO
name: Ondo
chain: ethereum
contract: "0xfAbA6f8e4a5E8Ab82F62fe7C39859FA577269BE3"
overall_score: 4.9
overall_verdict: FAIL
section_scores:
  revenue: 3
  foundation_team: 4
  insider_holdings: 3
  selling_behavior: 5
  tokenomics_supply: 2
  liquidity_market: 9
  product_development: 7
  adoption_customers: 7
  security_audits: 6
  regulatory: 7
  catalysts: 3
gates_failed: [revenue]
red_lines:
  hack_exploit: none
  mint_role_used: not_used_still_possible
  control_dispute_at_company: active_litigation
price_usd: 0.3115
price_source: "CoinGecko, 14 Nov 2026 9:08 AM MST"
last_updated: 2026-11-14
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### ONDO · Overall grade **4.9 / 10 · ❌ FAIL**

**Summary:** Ondo the company runs billions in real tokenized products. ONDO the token earns none of it, has a live mint role, and half the supply sits in one 4-of-7 Safe with no on-chain lock.

**Sections passed: 5 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 3/10 | ❌ FAIL |
| 🏛️ Foundation & team | 4/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 3/10 | ❌ FAIL |
| 📉 Selling behavior | 5/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 2/10 | ❌ FAIL |
| 💧 Liquidity & market | 9/10 | ✅ PASS |
| 🧑‍💻 Product & development | 7/10 | ✅ PASS |
| 🤝 Adoption & customers | 7/10 | ✅ PASS |
| 🛡️ Security & audits | 6/10 | ✅ PASS |
| ⚖️ Regulatory | 7/10 | ✅ PASS |
| 📅 Catalysts & calendar | 3/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 ONDO · Ondo · 4.9 / 10 · ❌ FAIL

> **One line:** Ondo the company runs billions in real tokenized products. ONDO the token earns none of it, has a live mint role, and half the supply sits in one 4-of-7 Safe with no on-chain lock.

| 📊 Market (CoinGecko, 14 Nov 2026 9:08 AM MST) | 🔗 On-chain (Ethereum, 10 Oct 2026) |
|---|---|
| **Price** $0.3115 | **Token** `0xfAbA…9BE3` "Ondo", Solidity 0.8.3, not a proxy |
| **24h / 7d / 30d** 🔴 −9.2% / −13.9% / −29.5% | **Supply** 10,000,000,000 (no mint used yet) |
| **Market cap** $1.52B · **FDV** $3.12B | **Admin Safe (4 of 7)** `0x677F…A1A1` ~5.13B (51.8%) |
| **24h volume** $95.8M | **Roles on Safe** `DEFAULT_ADMIN`, `MINTER`, `TRANSFER` since 28 Apr 2022 |
| **ATH** $2.14 (15 Dec 2024) · now −85% | **Circulating (CoinGecko)** 4.87B |

---

## 💰 Revenue — Does it make money? · 3/10 · ❌ FAIL

| Metric | Value | Source |
|---|---:|---|
| 30-day fees (product side) | $7,933,472 | [Tier A] DefiLlama `ondo-yield-assets`, `ondo-global-markets`, `ondo-perps` |
| 30-day revenue to protocol/token | **$0** | [Tier A] DefiLlama |
| All-time fees | $97,351,480 | [Tier A] DefiLlama |
| USDY TVL | $2.40B (152.85% collateralised) | [Tier A] ondo.finance, 3 Nov 2026 |
| OUSG | $317.7M (BUIDL, SWEEP, BENJI, FYOXX) | [Tier A] ondo.finance |
| Ondo Global Markets (stocks) | $1.35B, 470+ assets | [Tier A] ondo.finance |
| Token's claim | "The governance token for the Ondo DAO and Flux Finance." **No contractual claim** on Ondo Finance Inc. revenue or equity | [Tier A] docs.ondo.foundation |
| Company revenue | No audited financials | [Unverified] |

**What it means:** The business clearly makes money. The token is a governance coupon with no cash flow. Real Rails: "TOKEN EARNS NOTHING."

## 🏛️ Foundation & team — Who is in charge? · 4/10 · ❌ FAIL

| Item | Finding | Source |
|---|---|---|
| Token steward | Ondo Foundation — filings not checked | [Unverified] |
| Operating company | Ondo Finance Inc. (Delaware) | [Tier A] court docket |
| Founder | Nathan Allman, Founder & CEO — verified as executive officer on SEC Form D (Ondo I LP, CIK 0001957431, filed 19 Jan 2024) | [Tier A] EDGAR |
| Founder status | Death reported 25 May 2026 | [Tier B] CoinDesk 23 Sep 2026 · [Unverified] by a primary record |
| Litigation | *Kathleen C. Allman v. Ondo Finance Inc.*, Del. Ch. C.A. No. 2026-0978, filed 24 Jul 2026, ACTIVE (Chancellor McCormick) | [Tier A] Delaware CourtConnect |
| Token admin | 4-of-7 Safe `0x677FD4Ed8aE623f2f625DEB2D64F2070E46cA1A1` — signers not publicly named | [Tier A] chain |
| Regulated subsidiaries | Ondo Capital Management (SEC RIA); Ondo USDY LLC (FinCEN MSB); acquired Oasis Pro (BD, ATS, TA) | [Tier A] SEC/FinCEN · [Tier A] Ondo |

**What it means:** Who controls the company is in court, and who signs for half the token supply is not public.

## 🪙 Foundation / team holdings — How many coins do they hold? · 3/10 · ❌ FAIL

| Wallet | ONDO | % of 10B | Locked? |
|---|---:|---:|---|
| Admin Safe `0x677F…A1A1` (Nansen: "Ondo Finance: Multisig 2") | ~5,130,000,000 | ~51.8% | 🔓 **Plain balance** — LinearTimelock does not apply |
| Safe `0xEA5785E1…` (received Apr–Sep 2026) | 725,000,000 received, then distributed | 7.25% | 🔓 |
| Safe `0x52408397…` (received 2025 – Jan 2026) | 1,548,000,000 received, then distributed | 15.48% | 🔓 |
| Safe `0xD2e6E930E25456fFcD4Df0124563cC334F3284f4` | Nansen "Smart Account by Safe" | — | traced |

**What it means:** Over half the supply can be moved by four signatures today, despite the "January 2027 unlock" story.

## 📉 Selling behavior — Do insiders sell into pumps? · 5/10 · ❌ FAIL

| Test | Result | Source |
|---|---|---|
| Admin Safe outflows | 825M traced (725M → `0xEA5785E1…`, 100M → `0x52408397…`). **Neither forwarded to an exchange within one hop** | [Tier A] chain |
| Nansen 7-day exchange net flow | −$4.43M (net out of exchanges) | [Tier B] Nansen |
| Nansen 7-day smart-trader net flow | −$128,705 | [Tier B] Nansen |
| Top exchange-holder balance | 731.4M (+7.27M in 7 days) | [Tier B] Nansen |
| Formal pump-window test on Safe outflows | **Not run** | Gap |

- Real Rails treasury badge: **CAUTION**.

**What it means:** No proof of pump-selling, but big discretionary releases to unnamed Safes with no address-level disclosure.

## 📊 Tokenomics & supply · 2/10 · ❌ FAIL

| Item | Value | Source |
|---|---|---|
| Max supply (docs / MiCA) | 10B, "no scheduled or planned inflation" | [Tier A] docs |
| Mint function | **Live.** Any `MINTER_ROLE` holder can mint, capped only by uint96 | [Tier A] verified source |
| FIP-08 | Anniversary unlocks each January 2025–2029 | [Tier A] [FIP-08](https://forum.fluxfinance.com/t/fip-08-release-of-the-ondo-token-lock-up/563) |
| Jan 2027 tranche | Real Rails: 1.94B (19.4%) on 18 Jan 2027 · trackers: ~1.71B | [Unverified] — governance promise, not an on-chain vest |
| Observed releases | ~100–150M ONDO a month leaking into supply recently | Research model from chain flows |
| Burns | None claimed | [Tier A] |

**What it means:** The code allows unlimited minting and the "unlock schedule" is a promise, not a lock.

## 💧 Liquidity & market · 9/10 · ✅ PASS

- $95.8M 24h volume on a $1.52B cap; listed on all major venues.

## 🧑‍💻 Product & development · 7/10 · ✅ PASS

- Live: USDY, OUSG, Ondo Global Markets (tokenized stocks), Flux.
- **Abandoned:** Ondo Chain L1 — never reached mainnet, discontinued 27 Jul 2026, replaced by off-chain "Ondo Network."
- GitHub `ondoprotocol`: 16 repos, 4 pushed in 90 days, last push 27 Oct 2026.

## 🤝 Adoption & customers · 7/10 · ✅ PASS

| Claim | Status |
|---|---|
| Mastercard MTN's first RWA provider; OUSG backed mainly by BlackRock BUIDL + Franklin + WisdomTree | Confirmed |
| Acquired Oasis Pro (BD, ATS, TA) | Confirmed |
| SEC investigation closed without charges | Confirmed |
| DTCC Industry Working Group participant | Confirmed |
| "Partnered with BlackRock" | Partly |
| "BlackRock, Fidelity, JPMorgan, Goldman are inside Ondo" | False |

## 🛡️ Security & audits · 6/10 · ✅ PASS

- No ONDO hack on file. Token has no pause or blacklist and is not upgradeable. USDY/OUSG admin and KYC controls not fully reviewed [Unverified].

## ⚖️ Regulatory · 7/10 · ✅ PASS

- SEC-registered adviser, FinCEN MSB, broker-dealer/ATS via Oasis Pro; OUSG under Reg D 506(c)/3(c)(7); USDY under Reg S. SEC investigation closed without charges.

**What it means:** The company is one of the more regulated names in crypto. None of that attaches to the ONDO token.

## 📅 Catalysts & calendar · 3/10 · ❌ FAIL

| Date | Event |
|---|---|
| 18 Jan 2027 | FIP-08 anniversary unlock (1.71–1.94B, figures disputed) |
| Open | Del. Ch. 2026-0978 outcome |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None |
| Mint role used | 🟢 Not used (supply exactly 10B on 10 Oct) — 🔴 still possible |
| Control dispute at the company | 🟡 Active litigation |

## 📚 Sources

- [Tier A] Ethereum verified source, RPC and Blockscout holder/log reads, 10 Oct 2026
- [Tier A] [docs.ondo.foundation/ondo-token](https://docs.ondo.foundation/ondo-token) · [FIP-08](https://forum.fluxfinance.com/t/fip-08-release-of-the-ondo-token-lock-up/563)
- [Tier A] [Delaware CourtConnect 2026-0978](https://courtconnect.courts.delaware.gov/cc/cconnect/ck_public_qry_doct.cp_dktrpt_docket_report?case_id=2026-0978)
- [Tier A] [SEC EDGAR CIK 1949480](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=1949480)
- [Tier A] DefiLlama fees/revenue, 13 Nov 2026 · ondo.finance product figures, 3 Nov 2026
- [Tier A] CoinGecko `ondo-finance`, 14 Nov 2026 9:08 AM MST
- [Tier B] CoinDesk 23 Sep 2026 · Nansen pack 9 Nov 2026
- [Unverified] Founder death date; Jan 2027 tranche size; company revenue; Foundation filings

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
