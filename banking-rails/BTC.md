---
ticker: BTC
name: Bitcoin
chain: bitcoin
contract: "native (no token contract)"
overall_score: 7.3
overall_verdict: PASS
section_scores:
  revenue: 4
  foundation_team: 7
  insider_holdings: 8
  selling_behavior: 8
  tokenomics_supply: 9
  liquidity_market: 10
  product_development: 8
  adoption_customers: 9
  security_audits: 8
  regulatory: 8
  catalysts: 6
gates_failed: []
red_lines:
  hack_exploit: none
  hashrate_drop_two_retargets: watch
  fee_share_of_miner_revenue_under_2pct: tripped
price_usd: 65569
price_source: "CoinGecko, 14 Nov 2026 12:12 PM MST"
chain_read_height: 975830
last_updated: 2026-11-14
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### BTC · Overall grade **7.3 / 10 · ✅ PASS**

**Summary:** No foundation, no premine, no insider unlocks and the deepest market in crypto, but users pay only ~$78M a year in fees, about 1% of what miners earn, so the network still runs on new-coin subsidy.

**Sections passed: 10 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 4/10 | ❌ FAIL |
| 🏛️ Foundation & team | 7/10 | ✅ PASS |
| 🪙 Foundation / team holdings | 8/10 | ✅ PASS |
| 📉 Selling behavior | 8/10 | ✅ PASS |
| 📊 Tokenomics & supply | 9/10 | ✅ PASS |
| 💧 Liquidity & market | 10/10 | ✅ PASS |
| 🧑‍💻 Product & development | 8/10 | ✅ PASS |
| 🤝 Adoption & customers | 9/10 | ✅ PASS |
| 🛡️ Security & audits | 8/10 | ✅ PASS |
| ⚖️ Regulatory | 8/10 | ✅ PASS |
| 📅 Catalysts & calendar | 6/10 | ✅ PASS |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 BTC · Bitcoin · 7.3 / 10 · ✅ PASS

> **One line:** No foundation, no premine, no insider unlocks and the deepest market in crypto, but users pay only ~$78M a year in fees, about 1% of what miners earn, so the network still runs on new-coin subsidy.

ℹ️ **Adapted for a layer-1 with no issuer.** "Revenue" = fees users pay to the network and who captures them. "Foundation" = who maintains and funds the software. "Holdings / Selling" = the largest identifiable entity holders, since no team allocation exists.

| 📊 Market (CoinGecko, 14 Nov 2026 12:12 PM MST) | 🔗 On-chain (mempool.space, block 975,830) |
|---|---|
| **Price** $65,569 | **Asset** native BTC, no contract |
| **24h / 7d / 30d** 🔴 −4.9% / −13.6% / −20.4% | **Supply** 20,111,937 of 21,000,000 cap (95.8%) |
| **Market cap** $1.319T · **FDV** same | **Hashrate** ~905 EH/s (1-month view) |
| **24h volume** $36.29B | **Difficulty** 134.82T · next retarget est. **−6.6%** (prior −9.1%) |
| **ATH** $126,080 (6 Oct 2025) · now −48% | **Fees right now** 1–2 sat/vB |

---

## 💰 Revenue — Does it make money? · 4/10 · ❌ FAIL

| Metric | Value | Source |
|---|---:|---|
| 24h fees paid by users | $254,571 | [Tier A] DefiLlama `bitcoin` fees, 14 Nov 2026 |
| 30-day fees | $6,302,817 | [Tier A] DefiLlama |
| 12-month fees | $78,495,445 | [Tier A] DefiLlama |
| All-time fees | $4,460,913,569 | [Tier A] DefiLlama |
| "Revenue" (burn / treasury) | **$0** — no burn, no treasury; 100% of fees go to miners | [Tier A] DefiLlama · protocol design |
| Last 144 blocks (≈1 day): miner reward | 454.37 BTC total = 450.00 subsidy + **4.37 BTC fees (0.96%)** | [Tier A] mempool.space reward-stats |
| Block subsidy | 3.125 BTC since the April 2024 halving | [Tier A] protocol |

**What it means:** People pay real money to use Bitcoin, but it is small next to a $1.3T asset (~0.006% a year), and none of it reaches holders. Miners rely on new coins for ~99% of their income; that subsidy halves again in 2028. BTC's value case is scarcity, not cash flow, so it scores low on this section by design.

## 🏛️ Foundation & team — Who is in charge? · 7/10 · ✅ PASS

| Item | Finding | Source |
|---|---|---|
| Foundation | **None.** No company or foundation controls the protocol or holds a treasury. Creator "Satoshi Nakamoto" is pseudonymous and inactive since 2011 | [Tier A] protocol history · white paper |
| Reference client | Bitcoin Core, GitHub `bitcoin/bitcoin` — last push 13 Nov 2026; ~1,122 commits in the last 13 weeks; 90,677 stars | [Tier A] GitHub API |
| Releases | v32.1, v31.2, v30.4 all published 28 Oct 2026 (maintained branches patched together) | [Tier A] GitHub releases |
| Change process | BIPs + rough consensus; node operators choose software. No on-chain vote, no admin key | [Tier A] BIP process |
| Developer funding | Grants from independent non-profits and companies (e.g. Brink, OpenSats, Chaincode, Spiral) | [Unverified] not checked per funder this pass |
| Mining concentration (last ~1 month, 4,378 blocks) | Foundry USA 25.5% · AntPool 20.1% · F2Pool 16.6% · ViaBTC 9.2% · SpiderPool 5.9% · MARA 5.1% → **top 2 = 45.6%, top 3 = 62.2%** | [Tier A] mempool.space pools |

**What it means:** No one is "in charge", which removes foundation risk. The concentration that matters is mining pools: three pools found ~62% of recent blocks.

## 🪙 Foundation / team holdings — How many coins do they hold? · 8/10 · ✅ PASS

| Holder | BTC | % of supply | Notes | Source |
|---|---:|---:|---|---|
| Team / foundation allocation | **0** | 0% | No premine, no ICO, no vesting | [Tier A] protocol |
| Strategy Inc. (largest public company holder) | 850,364 (as of 8 Nov 2026) | 4.23% | Bought 1,036 BTC 2–8 Nov 2026 | [Tier A] Strategy 8-K (SEC), as reported by 2 outlets |
| Early "Satoshi-era" coins | est. ~1.1M | ~5.5% | Never moved; attribution is statistical | [Unverified] |
| Spot ETF custodians | Not read this pass | — | Would need issuer holdings pages | Not found |

**What it means:** There is no insider stack. The big holders are public companies and funds whose holdings are disclosed in filings.

## 📉 Selling behavior — Do insiders sell into pumps? · 8/10 · ✅ PASS

**Pump test:** CoinGecko daily closes, 15 Nov 2025 – 14 Nov 2026: **9 of 361 days** were pump days (5 Mar 2026; 20–25 Aug 2026; 22–23 Sep 2026). Last pump day 23 Sep 2026 (+12.8%).

| Check | Finding | Source |
|---|---|---|
| Team / foundation selling | Not applicable — no team or foundation wallet exists | [Tier A] |
| Largest corporate holder | Strategy was a **net buyer** in the week of 2–8 Nov 2026 (+1,036 BTC) | [Tier A] 8-K |
| Satoshi-era coins | No movement found in this pass | [Unverified] not traced address-by-address |
| Government holders | Not traced this pass | Not found |

**What it means:** There are no insiders who can dump into a pump. Selling pressure comes from the open market (funds, miners, leverage), not a team.

## 📊 Tokenomics & supply · 9/10 · ✅ PASS

| Item | Value | Source |
|---|---|---|
| Max supply | 21,000,000, enforced by every node | [Tier A] protocol |
| Issued | 20,111,937 (95.8%) | [Tier A] CoinGecko / chain |
| New supply | 3.125 BTC per block ≈ 450 BTC/day ≈ 164k/year (~0.8%) | [Tier A] protocol |
| Next halving | ~2028 (block 1,050,000) → 1.5625 BTC | [Tier A] protocol |
| Mint / freeze / blacklist / upgrade key | None | [Tier A] |

## 💧 Liquidity & market · 10/10 · ✅ PASS

- $36.29B 24h volume (CoinGecko, 14 Nov 2026). Listed on every major exchange; US spot ETFs since Jan 2024.
- Leverage risk: ~$1.6B of liquidations reported on 13 Nov 2026 (CoinDesk + The Block, Tier B ×2).

## 🧑‍💻 Product & development · 8/10 · ✅ PASS

- Bitcoin Core: three patched release lines on 28 Oct 2026; active daily commits ([Tier A] GitHub).
- The Block reported three Bitcoin Core bug fixes on 11 Nov 2026, including one serious mining bug already patched — [Unverified] as a news item (one outlet).
- Layer-2s (Lightning etc.) exist but were not measured this pass.

## 🤝 Adoption & customers · 9/10 · ✅ PASS

- 517,547 transactions in the last 144 blocks (~1 day) ([Tier A] mempool.space).
- Public-company and ETF ownership is disclosed in SEC filings (e.g. Strategy 850,364 BTC).
- Fee pressure is very low (1–2 sat/vB), so block space demand is soft right now.

## 🛡️ Security & audits · 8/10 · ✅ PASS

| Item | Finding | Source |
|---|---|---|
| Protocol hack | None. No admin keys to steal | [Tier A] |
| Hashrate trend | Difficulty fell 9.1% at the last retarget and is on track for another **−6.6%** | [Tier A] mempool.space |
| Pool concentration | Top 3 pools = 62.2% of recent blocks | [Tier A] |
| Wrapped BTC | WBTC and others are separate tokens with custodian / contract risk | [Tier A] |

**What it means:** The base layer is the most battle-tested in crypto. Two falling retargets in a row show miners switching off as price and fees fall — worth watching, not a failure.

## ⚖️ Regulatory · 8/10 · ✅ PASS

- US spot bitcoin ETFs approved by the SEC (Jan 2024) [Tier A]; treated as a commodity by the CFTC [Tier A].
- No issuer to sue. Remaining risk is tax, custody and mining rules by country.

## 📅 Catalysts & calendar · 6/10 · ✅ PASS

| Date | Event | Effect |
|---|---|---|
| ~early Dec 2026 | Next difficulty retarget (height 977,760), est. −6.6% | Miner economics |
| 8–9 Dec 2026 | FOMC meeting | Macro |
| ~2028 | Halving to 1.5625 BTC | Supply ↓, miner fee dependence ↑ |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None |
| Hashrate falling two retargets in a row | 🟡 Watch (−9.1% done, −6.6% projected) |
| Fees under 2% of miner revenue | 🔴 Tripped (0.96%, last 144 blocks) |

## 📚 Sources

- [Tier A] mempool.space API (tip height, hashrate, difficulty, reward-stats, pools), 14 Nov 2026 ~12:15 PM MST
- [Tier A] DefiLlama fees `bitcoin`, 14 Nov 2026
- [Tier A] CoinGecko `bitcoin` price and 365-day daily closes, 14 Nov 2026 12:12 PM MST
- [Tier A] GitHub `bitcoin/bitcoin` (pushes, releases, participation)
- [Tier A] Strategy Inc. 8-K (week to 8 Nov 2026) as reported by Bitcoin Magazine and Decrypt
- [Tier B] CoinDesk, The Block (liquidations, Core bug fixes)
- [Unverified] Satoshi-era coin estimate; developer funder list; Core bug-fix news item

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
