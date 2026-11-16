---
ticker: SOL
name: Solana
chain: solana
contract: "native (wrapped SOL mint So11111111111111111111111111111111111111112)"
overall_score: 6.6
overall_verdict: PASS
section_scores:
  revenue: 6
  foundation_team: 6
  insider_holdings: 5
  selling_behavior: 5
  tokenomics_supply: 6
  liquidity_market: 10
  product_development: 8
  adoption_customers: 8
  security_audits: 7
  regulatory: 7
  catalysts: 6
gates_failed: []
red_lines:
  one_hop_sale_status: none_found
  hack_exploit: none
  network_halt: none_in_series
  foundation_wallets_unpublished: tripped
methodology_effective: 2026-11-16
revenue_reaches_holders: "yes"
revenue_mechanism: "Half of every base fee is burned on-chain and priority fees and tips go to validators and their stakers automatically, so revenue reaches holders, though it does not cover inflation."
pump_day_price_source: "CoinGecko SOL daily closes (as published; named last resort)"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions: []
price_usd: 72.24
price_source: "CoinGecko, 14 Nov 2026 12:12 PM MST"
chain_read_slot: 469444012
last_updated: 2026-11-15
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### SOL · Overall grade **6.6 / 10 · ✅ PASS**

**Summary:** The highest fee earner per dollar of market cap of the big layer-1s (~$230M a year), with active client teams and no outage in this series, but the Solana Foundation stopped publishing token reports years ago, so its holdings and sales can't be checked.

**🚨 Top warning:** The Solana Foundation has not published its wallets or a token report since about Aug 2020, and Arkham has **no "Solana Foundation" entity** (only a generic "Solana" one), so Foundation holdings and any sales **cannot be checked** on-chain. No wallet-level evidence link exists for this; the gap itself is the finding.

**Sections passed: 9 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 6/10 | ✅ PASS |
| 🏛️ Foundation & team | 6/10 | ✅ PASS |
| 🪙 Foundation / team holdings | 5/10 | ❌ FAIL |
| 📉 Selling behavior | 5/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 6/10 | ✅ PASS |
| 💧 Liquidity & market | 10/10 | ✅ PASS |
| 🧑‍💻 Product & development | 8/10 | ✅ PASS |
| 🤝 Adoption & customers | 8/10 | ✅ PASS |
| 🛡️ Security & audits | 7/10 | ✅ PASS |
| ⚖️ Regulatory | 7/10 | ✅ PASS |
| 📅 Catalysts & calendar | 6/10 | ✅ PASS |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 SOL · Solana · 6.6 / 10 · ✅ PASS

> **One line:** The highest fee earner per dollar of market cap of the big layer-1s (~$230M a year), with active client teams and no outage in this series, but the Solana Foundation stopped publishing token reports years ago, so its holdings and sales can't be checked.

ℹ️ **Adapted for a layer-1.** "Revenue" = fees users pay, the part burned, and what reaches stakers. "Foundation" = Solana Foundation (Zug, Switzerland) plus the client teams. "Holdings / Selling" = accounts the network itself marks as non-circulating, and Foundation stake.

| 📊 Market (CoinGecko, 14 Nov 2026 12:12 PM MST) | 🔗 On-chain (Solana RPC, slot 469,444,012, epoch 1086) |
|---|---|
| **Price** $72.24 | **Total supply** 637,554,682 SOL |
| **24h / 7d / 30d** 🔴 −9.9% / −19.4% / −31.7% | **Circulating** 591,573,720 · **non-circulating** 45,980,962 (7.21%) |
| **Market cap** $42.76B · **FDV** $46.09B | **Inflation** 3.557%/yr, all to validators/stakers (foundation share 0) |
| **24h volume** $3.70B | **Active stake** 429.65M SOL (67.4% of supply) |
| **ATH** $293.31 (19 Jan 2025) · now −75% | **Validators** 663 active + 36 delinquent · Nakamoto coefficient **18** |

---

## 💰 Revenue — Does it make money? · 6/10 · ✅ PASS

| Metric | Value | Source |
|---|---:|---|
| 24h fees | $448,750 | [Tier A] DefiLlama `solana`, 14 Nov 2026 |
| 30-day fees | $16,245,905 | [Tier A] DefiLlama |
| 12-month fees | $230,471,207 | [Tier A] DefiLlama |
| All-time fees | $1,639,307,995 | [Tier A] DefiLlama |
| 30-day revenue (burned share of base fees) | $1,563,273 | [Tier A] DefiLlama |
| 12-month burn | $25,159,979 | [Tier A] DefiLlama |
| Who captures the rest | Priority fees and tips → validators and their stakers | [Tier A] protocol |

**What it means:** Solana users paid ~$230M in fees over 12 months, ~0.54% of market cap — the best ratio of the layer-1s in this set. Most goes to stakers, a little is burned. It does not cover the 3.56% inflation, so holders who don't stake are diluted.

- **Reaches holders (binary test, 16 Nov 2026 rules): Yes.** Half of every base fee is burned on-chain and priority fees and tips go to validators and their stakers automatically, so revenue reaches holders, though it does not cover inflation.

## 🏛️ Foundation & team — Who is in charge? · 6/10 · ✅ PASS

| Item | Finding | Source |
|---|---|---|
| Solana Foundation | Swiss non-profit (Solana Stiftung, Zug). Runs delegation program and grants | [Tier A] solana.org |
| Board change | Swiss commercial-registry entry (SHAB) dated 4 Mar 2026 reportedly records Lily Liu leaving the board / presidency | [Unverified] registry entry not opened this pass |
| Client teams | Agave (Anza) — `anza-xyz/agave` pushed 14 Nov 2026, v4.5.0-beta.0 on 6 Nov · Firedancer (Jump) — v26.11.0 on 11 Nov 2026 | [Tier A] GitHub |
| Running version | solana-core 4.4.0 on the RPC node read | [Tier A] RPC `getVersion` |
| Change process | SIMDs + stake-weighted validator votes; no admin key over SOL | [Tier A] |

**What it means:** Two independent client teams ship weekly. The foundation is a real entity, but its leadership change was not confirmed from a primary page.

## 🪙 Foundation / team holdings — How many coins do they hold? · 5/10 · ❌ FAIL

| Bucket | SOL | % of supply | Source |
|---|---:|---:|---|
| Network-marked non-circulating accounts (foundation / locked) | 45,980,962 | 7.21% | [Tier A] RPC `getSupply` |
| Solana Foundation stake accounts (599 accounts, 30 Oct 2026) | ~27.38M | ~4.3% | [Unverified] one Tier B rich-list write-up |
| Arkham "Solana" entity (generic, not labelled "Solana Foundation") | 27.466M SOL | ~4.3% | [Tier B] Arkham, read 15 Nov 2026 ~11:00 AM MST (signed-in account). Close to the 27.38M figure, but Arkham does not say these are Foundation wallets, so it does **not** count as a second source for the Foundation stake [Unverified] |
| Original allocation (team 12.79%, foundation 10.46%, seed/private sales) | — | — | [Unverified] not re-read from a primary doc this pass |
| Last Foundation transparency report | August 2020 | — | [Unverified] solana.com transparency page per search, not opened |

**What it means:** The chain says ~46M SOL (7%) is not circulating, but the Foundation has not published which wallets it controls or how much it holds for years.

## 📉 Selling behavior — Do insiders sell into pumps? · 5/10 · ❌ FAIL

**Pump test:** CoinGecko daily closes, 15 Nov 2025 – 14 Nov 2026: **25 of 361 days** were pump days (most recent cluster 19–23 Sep 2026; last +16.7% on 23 Sep).

| Check | Finding | Source |
|---|---|---|
| Solana Foundation → exchange on a pump day | **Not found** — but Foundation wallets are not published, so this cannot be proven | Not found |
| Large unstake-and-send flows | One unlabeled wallet unstaked 1.93M SOL and sent it to Coinbase Institutional in four rounds in Oct 2026 (12, 16, 27, 31 Oct — none are pump days); same pattern 1.86M SOL in June | [Unverified] one Tier B outlet; owner unknown |
| Alameda / FTX estate | Repeated unstakes routed to creditor-distribution addresses (Mar, Apr, Oct 2026) | [Tier B] CoinDesk + CoinAlertNews |

**What it means:** No Foundation selling into pumps was found, but without published wallets "not found" is not a pass under this method. Large non-Foundation holders (FTX estate, unlabeled whales) are the visible sellers.

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from CoinGecko SOL daily closes (as published; named last resort).

## 📊 Tokenomics & supply · 6/10 · ✅ PASS

| Item | Value | Source |
|---|---|---|
| Supply | 637.55M, no hard cap | [Tier A] RPC |
| Inflation | 3.557% now; schedule falls 15% a year toward a 1.5% floor | [Tier A] RPC `getInflationRate` · Solana docs |
| Burn | 50% of base fees (priority fees go to validators) | [Tier A] docs · DefiLlama |
| Admin / mint key over SOL | None | [Tier A] |

## 💧 Liquidity & market · 10/10 · ✅ PASS

- $3.70B 24h volume; every major exchange; US spot SOL ETFs exist (e.g. Bitwise BSOL) [Tier B].

## 🧑‍💻 Product & development · 8/10 · ✅ PASS

- Throughput sample: ~2,217 transactions/second over the last 10 performance samples ([Tier A] RPC).
- 566.7B lifetime transactions ([Tier A] RPC `getEpochInfo`).
- Two production clients (Agave, Firedancer) both released in November 2026.

## 🤝 Adoption & customers · 8/10 · ✅ PASS

- $230M of fees in 12 months is paid usage. Payment / stablecoin integrations (e.g. Samsung Wallet USDC on Solana, 5 Nov 2026) — [Unverified] one outlet.

## 🛡️ Security & audits · 7/10 · ✅ PASS

- No protocol hack. Past full-network halts (most recently Feb 2024) are a known weakness; no halt in this report series.
- Stake is spread across 663 validators; 18 of them together hold over one-third of stake.

## ⚖️ Regulatory · 7/10 · ✅ PASS

- Spot SOL ETFs trading in the US [Tier B]. No current enforcement against SOL found.

## 📅 Catalysts & calendar · 6/10 · ✅ PASS

| Date | Event | Effect |
|---|---|---|
| Every epoch (~2 days) | Inflation to stakers | Supply ↑ ~3.56%/yr |
| Nov 2026 | Agave 4.5 beta → mainnet | Product |
| 15–17 Nov 2026 | Breakpoint conference (reported) | [Unverified] date |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None |
| Network halt | 🟢 None in this series |
| Foundation wallets unpublished | 🟡 Tripped — holdings and sales can't be audited (no Foundation address list exists to link; Arkham has no Foundation entity) |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| Arkham "Solana" entity (27.47M SOL) | Generic entity, not labelled Solana Foundation | Arkham | low | no | None: Foundation stake stays [Unverified] |

## 📚 Sources

- [Tier A] Methodology update 16 Nov 2026: no new Arkham lookups; the attribution table uses evidence already cited in this report.
- [Tier A] Solana mainnet RPC: `getSupply`, `getInflationRate`, `getEpochInfo`, `getVersion`, `getVoteAccounts`, `getRecentPerformanceSamples`; 14 Nov 2026 ~12:25 PM MST
- [Tier A] DefiLlama fees `solana`, 14 Nov 2026
- [Tier A] CoinGecko `solana` price and 365-day daily closes, 14 Nov 2026 12:12 PM MST
- [Tier A] GitHub [`anza-xyz/agave`](https://github.com/anza-xyz/agave) ([releases](https://github.com/anza-xyz/agave/releases)), [`firedancer-io/firedancer`](https://github.com/firedancer-io/firedancer) ([releases](https://github.com/firedancer-io/firedancer/releases))
- [Tier A] [DefiLlama Solana fees](https://defillama.com/chain/solana) · [CoinGecko `solana`](https://www.coingecko.com/en/coins/solana)
- [Tier B] [CoinDesk (Alameda unstakes, 13 Apr 2026)](https://www.coindesk.com/markets/2026/04/13/alameda-moves-usd16-million-in-solana-s-sol-token-for-possible-creditor-distribution) · CoinAlertNews · Basecamp Markets
- [Tier B] Arkham, read 15 Nov 2026 ~11:00 AM MST (signed-in account): only a generic "Solana" entity (27.466M SOL); no "Solana Foundation" entity or address list. First page only; all-time exchange totals Enterprise-locked
- [Unverified] Foundation stake ~27.38M; board change; original allocation; transparency-report date; Breakpoint dates; Samsung Wallet item

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer) or the label source (Arkham) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Non-circulating SOL 45,980,962 (7.21%) per the network's own supply call | Solana RPC `getSupply` (JSON-RPC call; no static page) | A | 14 Nov 2026 |
| No "Solana Foundation" entity on Arkham; only a generic "Solana" entity (27.466M SOL) | Arkham entity search, signed-in (no Foundation address to link) | B | 15 Nov 2026 ~11:00 AM MST |
| Alameda / FTX estate unstakes routed to creditor-distribution addresses | [CoinDesk, 13 Apr 2026](https://www.coindesk.com/markets/2026/04/13/alameda-moves-usd16-million-in-solana-s-sol-token-for-possible-creditor-distribution) | B | 14 Nov 2026 |
| Unlabeled whale unstaked 1.93M SOL to Coinbase Institutional (Oct 2026) | One Tier B outlet; wallet address not captured, so no explorer link [Unverified] | B (one source) | 14 Nov 2026 |
| Two client teams ship weekly (Agave, Firedancer) | [Agave releases](https://github.com/anza-xyz/agave/releases) · [Firedancer releases](https://github.com/firedancer-io/firedancer/releases) | A | 14 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Which wallets the Solana Foundation controls** | Ask the Foundation for a current transparency report with addresses; get the stake-authority list behind the 599 stake accounts and check it against Arkham's "Solana" entity | Free |
| 2 | **Foundation stake ~27.38M** | Read the 599 stake accounts with `getProgramAccounts` filtered by the Foundation's stake authority | Free (RPC) |
| 3 | **Original allocation** | Re-read the token distribution from a primary Solana / Foundation doc | Free |
| 4 | **Foundation board / leadership change** | Swiss commercial register (Zug) entry for the Solana Foundation | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
