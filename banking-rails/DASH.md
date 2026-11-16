---
ticker: DASH
name: Dash
chain: dash
contract: "native (Dash, X11 proof-of-work + masternodes)"
overall_score: 4.7
overall_verdict: FAIL
section_scores:
  revenue: 1
  foundation_team: 6
  insider_holdings: 6
  selling_behavior: 6
  tokenomics_supply: 6
  liquidity_market: 6
  product_development: 7
  adoption_customers: 3
  security_audits: 6
  regulatory: 4
  catalysts: 6
gates_failed: [revenue]
red_lines:
  one_hop_sale_status: none_found
  hack_exploit: none
  v24_hard_fork_activation: watch_delayed
  treasury_payout_on_pump_day: tripped_1_of_12_months_calendar_driven
  eu_privacy_coin_rule_2027: open
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "Users pay almost nothing; miners, masternodes and developers are paid by inflation."
pump_day_price_source: "Gate DASH_USDT UTC daily closes, re-run 16 Nov 2026 with scripts/pump_day_test.py (50 of 360 days); the body's earlier count used CoinGecko daily closes"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions: []
price_usd: 38.22
price_source: "CoinGecko, 15 Nov 2026 6:45 AM MST"
chain_read_height: 2572718
last_updated: 2026-11-15
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### DASH · Overall grade **4.7 / 10 · ❌ FAIL**

**Summary:** A 12-year-old payments coin with a real on-chain treasury and no team token stash, but users pay only ~$9.7k a year in fees, so everything (miners, masternodes and the ~$3M-a-year developer budget) runs on new-coin issuance while on-chain usage is small (~12k transactions a day).

> ⚠️ **Top warning:** The DCG treasury payee [`7mUyau75…`](https://chainz.cryptoid.info/dash/address.dws?7mUyau75ATy1c6LoZeG3D57jKBkR4iHJkE.htm) passes every coin through and sent **4,832 + 200 DASH on the 1 Sep 2026 pump day** ([tx 3e9b42ad… (200)](https://chainz.cryptoid.info/dash/tx.dws?3e9b42ad28783094896d3c58fa3789d5c41aff643a4cd93eda976dedbad7d6a2.htm), [tx c12921d6…](https://chainz.cryptoid.info/dash/tx.dws?c12921d6dcefdd13784a03bafe4785fe81b79d0a7271ce8f701943cc80a0d7c7.htm)) — the regular 1st-of-month payroll, but the downstream wallets ([`7c7of2xz…`](https://chainz.cryptoid.info/dash/address.dws?7c7of2xznwtYy3p2EMxLEaoDC996Q1CSfm.htm), [`7pk3RNRA…`](https://chainz.cryptoid.info/dash/address.dws?7pk3RNRAwCiteq5Bs8RdS4jCqYwMmVT9qd.htm), [`XvEU6pEW…`](https://chainz.cryptoid.info/dash/address.dws?XvEU6pEWA2oC4FVdcxVdXcxHaMjyLZvPdt.htm)) are unlabelled and Arkham does not cover Dash.

**Sections passed: 8 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 1/10 | ❌ FAIL |
| 🏛️ Foundation & team | 6/10 | ✅ PASS |
| 🪙 Foundation / team holdings | 6/10 | ✅ PASS |
| 📉 Selling behavior | 6/10 | ✅ PASS |
| 📊 Tokenomics & supply | 6/10 | ✅ PASS |
| 💧 Liquidity & market | 6/10 | ✅ PASS |
| 🧑‍💻 Product & development | 7/10 | ✅ PASS |
| 🤝 Adoption & customers | 3/10 | ❌ FAIL |
| 🛡️ Security & audits | 6/10 | ✅ PASS |
| ⚖️ Regulatory | 4/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 6/10 | ✅ PASS |

*Pass = 6 or more out of 10. Full details for every section follow below. Overall fails the **Revenue gate** (1 ≤ 3).*

---


# 🪪 DASH · Dash · 4.7 / 10 · ❌ FAIL

> **One line:** A 12-year-old payments coin with a real on-chain treasury and no team token stash, but users pay only ~$9.7k a year in fees, so everything (miners, masternodes and the ~$3M-a-year developer budget) runs on new-coin issuance while on-chain usage is small (~12k transactions a day).

ℹ️ **Adapted for a layer-1 with a DAO treasury.** "Revenue" = transaction fees. Block subsidy is issuance, not revenue. "Foundation" = Dash Core Group, Inc. (DCG) plus the masternode-voted treasury. "Holdings / Selling" = the treasury's biggest payee (DCG's on-chain payout address), plus early-mined supply.

| 📊 Market (CoinGecko, 15 Nov 2026 6:45 AM MST) | 🔗 On-chain (Insight + Blockchair, block 2,572,718, 6:52 AM MST) |
|---|---|
| **Price** $38.22 | **Supply** 12,895,422 DASH (Chainz explorer) · CoinGecko total 12,895,389 |
| **24h / 7d / 30d / 1y** 🔴 −2.4% / −18.0% / −23.3% / −51.3% | **Max supply** 18,920,000 (68.2% issued) |
| **Market cap** $492.9M · **FDV** same · rank #102 | **Blocks / txs last 24h** 543 / 12,298 |
| **24h volume** $58.2M | **Median / average fee** $0.00018 / $0.0013 |
| **ATH** $1,493.59 (19 Dec 2017) · now −97.4% | **Masternodes** 2,067 enabled (weighted 3,120) |
| **1 year ago** $93.04 (16 Nov 2025 close) | **Node software majority** v23.1.8 (protocol 70240); v24 hard fork pending |

---

## 💰 Revenue — Does it make money? · 1/10 · ❌ FAIL

| Metric | Value | Source |
|---|---:|---|
| 24h fees | $15 | [Tier A] DefiLlama `dash` fees, 15 Nov 2026 |
| 30-day fees | $509 | [Tier A] DefiLlama |
| 12-month fees | **$9,700** | [Tier A] DefiLlama |
| Fees by month | Nov 25 $2.3k · Dec $819 · Jan $1.1k · Feb $1.7k · Mar $865 · Apr $624 · May $568 · Jun $395 · Jul $339 · Aug $463 · Sep $781 · Oct $559 · Nov 1–14 $229 | [Tier A] DefiLlama |
| Protocol "revenue" | **$0**: fees go to miners; no burn | [Tier A] DefiLlama revenue series |
| Transactions, last 24h | 12,298 · average fee $0.0013 | [Tier A] Blockchair chain stats |
| What actually funds the network | New coins: ~892.6 DASH a day to miners + masternodes (≈ **$34.1k a day**), plus the monthly treasury superblock (up to 6,828 DASH) | [Tier A] Blockchair `inflation_24h` · DashCentral budget |
| Treasury budget, next superblock | 6,828 DASH available · **5,651 DASH allotted** to passing proposals (≈ $216k) | [Tier B] DashCentral API · protocol rule in [Tier A] Dash docs |

**What it means:** Users pay almost nothing (~$27 a day at most). Miners, masternodes and the developers are all paid by inflation, about $12–14M a year at today's price. The token has no cash-flow claim.

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** Users pay almost nothing; miners, masternodes and developers are paid by inflation.

## 🏛️ Foundation & team — Who is in charge? · 6/10 · ✅ PASS

| Item | Finding | Source |
|---|---|---|
| Governance | Masternodes vote on-chain on budget proposals; a proposal passes when (yes − no) ≥ 10% of eligible votes; regular masternode = 1 vote, evonode = 4 | [Tier A] [Dash docs, Understanding Governance](https://docs.dash.org/en/stable/docs/user/governance/understanding.html) |
| Main developer | **Dash Core Group, Inc.** (named in the docs as a treasury-funded organisation; publisher of docs.dash.org) | [Tier A] Dash docs |
| DCG funding | Proposal "DCG-Operations-Aug-Nov-26" ("Dash Core Group Operations September – December 2026"): **4,832 DASH a month × 4**, 753 yes / 63 no, payout address [`7mUyau75ATy1c6LoZeG3D57jKBkR4iHJkE`](https://chainz.cryptoid.info/dash/address.dws?7mUyau75ATy1c6LoZeG3D57jKBkR4iHJkE.htm) | [Tier A] Insight `gobject/get` (on-chain governance object) · [Tier B] DashCentral |
| DCG share of the budget | 4,832 of 5,651 allotted (**86%**) or of 6,828 maximum (71%) | Calculated |
| Code | `dashpay/dash`: v24.0.0 (5 Nov), v24.0.1 (13 Nov), v24.0.2 (14 Nov 2026); **1,722 commits in 13 weeks**. `dashpay/platform`: v5.0.3 (3 Nov), v5.1.0-dev.1 (13 Nov) | [Tier A] GitHub API |
| DCG officers, registration | Not re-read this pass | [Unverified] — see Open items |

**What it means:** Control is unusually transparent: who gets paid and how much is decided by on-chain votes anyone can read. The concentration is that one company takes most of the budget and writes most of the code.

## 🪙 Foundation / team holdings — How many coins do they hold? · 6/10 · ✅ PASS

| Holder | DASH | % of supply | Source |
|---|---:|---:|---|
| Team / foundation premine or ICO | **0**: no premine, no sale, no vesting | [Tier A] Dash docs (budget is "done without changing the emission") |
| DCG payout address [`7mUyau75…`](https://chainz.cryptoid.info/dash/address.dws?7mUyau75ATy1c6LoZeG3D57jKBkR4iHJkE.htm) | **0.00000577** (lifetime received 228,469.05 and sent 228,469.05) | [Tier A] Insight `addr` |
| Treasury | No treasury balance exists. Unallocated budget "is simply never created" | [Tier A] Dash docs |
| Masternode collateral (all operators) | ≈3.12M DASH locked (~24%): 1,716 regular × 1,000 + 351 evonodes × 4,000, derived from 2,067 nodes / 3,120 weighted | [Tier B] DashCentral counts · calculated · collateral sizes [Unverified] this pass |
| **Early mining (launch week)** | Blocks dated 19–20 Jan 2014: **9,808 blocks, 4,027,022 DASH (31% of today's supply)** | [Tier A] Blockchair chain aggregate (`sum(generation)`) |
| Who holds the launch-week coins today | Not known | [Unverified] |

**What it means:** No foundation or team stash, and DCG passes coins straight through. The open question is the 2014 launch: a large share of today's supply was mined in the first two days by a small number of miners, and nobody can see who holds it now.

## 📉 Selling behavior — Do insiders sell into pumps? · 6/10 · ✅ PASS

**Pump test:** CoinGecko daily closes, 16 Nov 2025 – 15 Nov 2026: **50 of 360 testable days (13.9%)** were pump days. Biggest cluster 14–19 Jan 2026 (**peak +130.7%** on 17 Jan); others in Dec, Apr, May, Aug and **5–9 Sep (+62.6%)**; last 29 Sep 2026.

**DCG payout address [`7mUyau75ATy1c6LoZeG3D57jKBkR4iHJkE`](https://chainz.cryptoid.info/dash/address.dws?7mUyau75ATy1c6LoZeG3D57jKBkR4iHJkE.htm), 12-month full trace** ([Tier A] Insight API, 40 txs):

| Flow | DASH | Pattern |
|---|---:|---|
| Received (12 superblock payments, 21st–23rd of each month) | 63,377 | 5,703 → 5,341 → 5,396 → 5,196 → 5,032 → 4,832 a month |
| Sent out (21 txs) | 63,377 | Almost all on the **1st–2nd of each month** (payroll pattern) |
| **Sent on pump days** | **5,207** (8.2%) | 29 Dec 2025: 175 · **1 Sep 2026: 4,832 + 200** (5-day move +14.1%) |

Selected outflows (each tx pays 1–4 addresses plus a change-style `7…` multisig address):

| Date (UTC) | DASH | Tx | Destinations |
|---|---:|---|---|
| 22 Nov 2025 | 5,196 | [`9384ba58…`](https://chainz.cryptoid.info/dash/tx.dws?9384ba58659fa6754758a01a78535a8249b59528b37583f6074ae80fe3d8ea68.htm) | [`XvEU6pEW…`](https://chainz.cryptoid.info/dash/address.dws?XvEU6pEWA2oC4FVdcxVdXcxHaMjyLZvPdt.htm) 2,000 + [`7pAv6sYX…`](https://chainz.cryptoid.info/dash/address.dws?7pAv6sYXvDPn9gG5ktQPhmJpkYPvnVPZrw.htm) 3,196 |
| 2 Feb 2026 | 5,341 | [`58df107c…`](https://chainz.cryptoid.info/dash/tx.dws?58df107cbce3c2a7298cde7eee44e400f650a47ed8c9a28f9d3dff791a25a060.htm) | [`XoHhGzZn…`](https://chainz.cryptoid.info/dash/address.dws?XoHhGzZnW14d2EjhXeEkhbpp8oTjJrgrZX.htm) 271 + [`7YHgvcG4…`](https://chainz.cryptoid.info/dash/address.dws?7YHgvcG4UBtZMmBggKxcUvxDTWdzPTCBeT.htm) 5,070 |
| **1 Sep 2026** (pump day) | 4,832 | [`c12921d6…`](https://chainz.cryptoid.info/dash/tx.dws?c12921d6dcefdd13784a03bafe4785fe81b79d0a7271ce8f701943cc80a0d7c7.htm) | [`Xg8pTryH…`](https://chainz.cryptoid.info/dash/address.dws?Xg8pTryH4eNhCvCwB87xZRXEnFPCMsGbDq.htm) 2.2 + [`7c7of2xz…`](https://chainz.cryptoid.info/dash/address.dws?7c7of2xznwtYy3p2EMxLEaoDC996Q1CSfm.htm) 4,829.8 |
| 1 Oct 2026 | 4,832 | [`442325c1…`](https://chainz.cryptoid.info/dash/tx.dws?442325c1cbfe13c8dfe228371c43c5f998825a72b9af1596bb1fbe5da42c4332.htm) | [`XvEU6pEW…`](https://chainz.cryptoid.info/dash/address.dws?XvEU6pEWA2oC4FVdcxVdXcxHaMjyLZvPdt.htm) 500 + [`7pk3RNRA…`](https://chainz.cryptoid.info/dash/address.dws?7pk3RNRAwCiteq5Bs8RdS4jCqYwMmVT9qd.htm) 4,332 |
| 2 Nov 2026 | 4,832 | [`dc6a7a22…`](https://chainz.cryptoid.info/dash/tx.dws?dc6a7a2240209b7f284ba3d021c2585b19ae87aad97d00b8563d001a2667a949.htm) | [`XchbTk8r…`](https://chainz.cryptoid.info/dash/address.dws?XchbTk8rXM4WsNtbfDkmBp94VhimNDW4sG.htm) 163 + [`7f1kNTrK…`](https://chainz.cryptoid.info/dash/address.dws?7f1kNTrKnzcDfp9sXvschTvjpLxjKKFgun.htm) 4,669 |

- The single pump-day payout is the regular 1st-of-month transfer. It follows the calendar, not the price.
- Whether DCG's downstream wallets (`7…` multisigs, `X…` addresses) sell on exchanges is **not labelled** → [Unverified].
- The superblock itself pays all funded proposals on a fixed ~30.29-day block schedule ([Tier A] docs).

**What it means:** The main insider payee receives coins on a fixed schedule and moves them on a fixed schedule. No pump-timed selling was found. It passes at 6, not higher, because the downstream wallets and any exchange sales are unlabelled.

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from Gate DASH_USDT UTC daily closes, re-run 16 Nov 2026 with scripts/pump_day_test.py (50 of 360 days); the body's earlier count used CoinGecko daily closes.

## 📊 Tokenomics & supply · 6/10 · ✅ PASS

| Item | Value | Source |
|---|---|---|
| Supply / max | 12,895,422 / 18,920,000 | [Tier B] Chainz explorer · CoinGecko |
| Block reward split | **80%** miners + masternodes · **20%** governance budget | [Tier A] Dash docs |
| Emission decline | Budget and subsidy fall ~**7.14% a year** | [Tier A] Dash docs |
| Issuance now | ~892.6 DASH a day coinbase (~325.8k a year) + ~5,651 a month treasury (~68.1k a year) ≈ **394k DASH a year ≈ 3.05%** | [Tier A] Blockchair · [Tier B] DashCentral · calculated |
| Unallocated budget | Never minted (reduces actual inflation) | [Tier A] docs |
| Mint / freeze / admin key | None (proof-of-work coin) | [Tier A] |
| Launch distribution | ~31% of today's supply was mined on 19–20 Jan 2014 | [Tier A] Blockchair aggregate |

## 💧 Liquidity & market · 6/10 · ✅ PASS

| Venue | Pair | 24h volume | Cost to move price +2% / −2% |
|---|---|---:|---:|
| Binance | DASH/USDT | $6.20M | $106k / $198k |
| WhiteBIT | DASH/USDT | $6.19M | $49k / $69k |
| Bitrue | DASH/USDT | $3.25M | $84k / $126k |
| KuCoin | DASH/USDT | $2.61M | $22k / $62k |

- 71 tickers, including Binance, Binance US, Coinbase, Kraken and OKX ([Tier A] CoinGecko tickers, 15 Nov 2026).
- Thin books for a ~$490M asset: under $200k of bids within 2% on the largest venue.

## 🧑‍💻 Product & development · 7/10 · ✅ PASS

- **Dash Core v24** (hard fork) shipped 5 Nov 2026: "decentralized masternode shares and multi-party payouts, extended masternode addresses, version 2 asset locks and unlocks for Dash Platform, compact quorum proofs, descriptor wallets by default" ([Tier A] GitHub release notes).
- Two patch releases within 9 days: **v24.0.1** fixed `LLMQ_400_85` quorums failing to form, which "delayed the v24 network upgrade on mainnet". **v24.0.2** fixed a memory leak that hit "every node… masternodes the most" ([Tier A] release notes).
- Dash Platform (Evolution) is active: v5.0.3 on 3 Nov 2026 ([Tier A] GitHub).

## 🤝 Adoption & customers · 3/10 · ❌ FAIL

| Metric | Value | Source |
|---|---:|---|
| On-chain transactions | 12,298 in 24h | [Tier A] Blockchair |
| Fees paid by users | ~$9.7k in 12 months | [Tier A] DefiLlama |
| Merchant / payment partners | Old draft cited Flexa capacity and a Dash–Zebec card; **not re-confirmed** with either party this pass | [Unverified] |
| Platform usage (DashPay usernames, Platform credits) | Not measured | Not found |

**What it means:** The network works, but few people use it to pay for things on-chain.

## 🛡️ Security & audits · 6/10 · ✅ PASS

| Item | Finding | Source |
|---|---|---|
| Protocol hack | None found | [Tier A] (absence in release notes and docs) |
| Upgrade friction | v24 activation slipped (quorum DKG failures) and v24.0.0 leaked memory; both patched by 14 Nov | [Tier A] release notes |
| Consensus | Proof-of-work (X11) + masternode quorums; 2,067 masternodes | [Tier A] / [Tier B] DashCentral |
| Mining concentration, ChainLocks coverage | Not measured this pass | Not found — see Open items |
| Bug disclosure | "vulnerability-disclosure-compensation" proposal (100 DASH a month) is in the funded budget | [Tier B] DashCentral |

## ⚖️ Regulatory · 4/10 · ❌ FAIL

- **US:** Dash is **not** among the named examples of digital commodities in SEC Release 33-11412 (17 Mar 2026). The list is examples only, so this is not a finding that Dash is a security, but it gives no clarity either ([Tier A] sec.gov).
- **EU (MiCA):** white paper for "Dash" (DTI FFG `PPDH6B273`) notified to BaFin on 12 Dec 2025 by **Crypto Risk Metrics GmbH**, a third party ([Tier A] ESMA interim register). This is a notification, not an approval.
- **EU (AML Regulation 2024/1624, Art. 79), from 10 Jul 2027:** CASPs may not keep accounts that allow anonymisation or "increased obfuscation of transactions, including through anonymity-enhancing coins" ([Tier B] EUR-Lex summary + law-text sites). **Whether Dash's optional CoinJoin makes it an "anonymity-enhancing coin" is not settled** → [Unverified]. If it does, EU exchanges could delist it.
- Privacy-coin delistings elsewhere: not re-checked this pass.

## 📅 Catalysts & calendar · 6/10 · ✅ PASS

| Date | Event | Effect |
|---|---|---|
| ~17 Nov 2026 (block 2,573,818) | Superblock voting opens; masternodes should be on v24.0.1+ | Governance |
| **~20 Nov 2026, morning MST (estimated)** (block 2,575,480) | Monthly superblock: 5,651 DASH allotted (incl. 4,832 to DCG) | Supply ↑ (scheduled) |
| **Earliest ~28 Nov 2026** (block 2,580,480) | **v24 hard-fork activation**, now gated on an `LLMQ_400_85` quorum signing | Product; outdated nodes split off |
| 3 Dec 2026 | DCG's current 4-month proposal ends; a renewal vote is needed | Funding / governance |
| 10 Jul 2027 | EU AMLR anonymity-enhancing-coin rule applies to CASPs | Listing risk |

## 🚩 Red lines status

| Red line | Status | Evidence |
|---|---|---|
| Hack / exploit | 🟢 None found | — |
| v24 hard-fork activation | 🟡 Watch (delayed; patches out) | v24.0.1 / v24.0.2 notes |
| Treasury payee outflow on a pump day | 🟡 1 of 12 months (1 Sep 2026), calendar-driven | [tx c12921d6…](https://chainz.cryptoid.info/dash/tx.dws?c12921d6dcefdd13784a03bafe4785fe81b79d0a7271ce8f701943cc80a0d7c7.htm) ([raw](https://insight.dash.org/insight-api/tx/c12921d6dcefdd13784a03bafe4785fe81b79d0a7271ce8f701943cc80a0d7c7)) from [DCG payout address](https://chainz.cryptoid.info/dash/address.dws?7mUyau75ATy1c6LoZeG3D57jKBkR4iHJkE.htm) |
| EU privacy-coin rule | 🟡 Open | AMLR Art. 79 |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| Main treasury payee | Dash Core Group (budget payee) | Superblock schedule | high | yes (protocol) | None: calendar-driven payouts, no pump-timed selling found |

## 📚 Sources

- [Tier A] Methodology update 16 Nov 2026: no new Arkham lookups; the attribution table uses evidence already cited in this report.
- [Tier A] Insight API ([`insight.dash.org`](https://insight.dash.org/insight-api/addr/7mUyau75ATy1c6LoZeG3D57jKBkR4iHJkE)): raw JSON for every tx cited ([example](https://insight.dash.org/insight-api/tx/c12921d6dcefdd13784a03bafe4785fe81b79d0a7271ce8f701943cc80a0d7c7)); human-readable views on [Chainz (cryptoID)](https://chainz.cryptoid.info/dash/address.dws?7mUyau75ATy1c6LoZeG3D57jKBkR4iHJkE.htm), linked inline and in the Evidence trail; `status`, `gobject/get/91808ffd…` (DCG proposal), `addr/7mUyau75…`, `txs?address=7mUyau75…` (40 txs); 15 Nov 2026 ~6:55 AM MST
- [Tier A] Blockchair `dash/stats` and block aggregate for 19–21 Jan 2014; 15 Nov 2026
- [Tier A] [Dash docs: Understanding Governance](https://docs.dash.org/en/stable/docs/user/governance/understanding.html)
- [Tier A] GitHub API `dashpay/dash` (v24.0.0–v24.0.2 release notes, participation), `dashpay/platform`
- [Tier A] DefiLlama fees/revenue `dash`; CoinGecko `dash` coin data, 365-day closes, tickers; 15 Nov 2026 6:45 AM MST
- [Tier A] SEC Release 33-11412 · ESMA interim MiCA register `OTHER.csv`
- [Tier B] DashCentral API (`/api/v1/budget`, `/api/v1/public`): budget, proposals, masternode counts · Chainz (cryptoid) supply
- [Tier B] EUR-Lex summary of AMLR and Art. 79 text sites
- [Tier B] [Arkham](https://intel.arkm.com/explorer/address/7pk3RNRAwCiteq5Bs8RdS4jCqYwMmVT9qd), read 15 Nov 2026 ~11:05 AM MST (signed-in account): **Dash is not supported** ([`7pk3RNRA…`](https://chainz.cryptoid.info/dash/address.dws?7pk3RNRAwCiteq5Bs8RdS4jCqYwMmVT9qd.htm) returns "Something went wrong"; [`7f1kNTrK…`](https://chainz.cryptoid.info/dash/address.dws?7f1kNTrKnzcDfp9sXvschTvjpLxjKKFgun.htm) and [`XvEU6pEW…`](https://chainz.cryptoid.info/dash/address.dws?XvEU6pEWA2oC4FVdcxVdXcxHaMjyLZvPdt.htm) not opened for the same reason). Open item #1 stays open
- [Unverified] DCG officers and registration; downstream DCG wallets; launch-week coin holders; merchant partners; masternode collateral sizes; AMLR classification of Dash

## 🔗 Evidence trail

*Strongest findings first. Each link opens the primary record (block explorer) or the label source (Arkham) for the claim, so any number can be checked by hand.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| 🟡 Pump-day payout 1 Sep 2026: 4,829.8 → `7c7of2xz…`, 2.2 → `Xg8pTryH…` | [tx c12921d6…](https://chainz.cryptoid.info/dash/tx.dws?c12921d6dcefdd13784a03bafe4785fe81b79d0a7271ce8f701943cc80a0d7c7.htm) · [raw](https://insight.dash.org/insight-api/tx/c12921d6dcefdd13784a03bafe4785fe81b79d0a7271ce8f701943cc80a0d7c7) · [`7c7of2xz…`](https://chainz.cryptoid.info/dash/address.dws?7c7of2xznwtYy3p2EMxLEaoDC996Q1CSfm.htm) | A | 15 Nov 2026 ~6:55 AM MST |
| 🟡 Pump-day payout 1 Sep 2026 (second tx, same block time): 200 DASH → `XdSQkyna…` 96.5 + `7f8SVFmG…` 103.5 | [tx 3e9b42ad…](https://chainz.cryptoid.info/dash/tx.dws?3e9b42ad28783094896d3c58fa3789d5c41aff643a4cd93eda976dedbad7d6a2.htm) · [raw](https://insight.dash.org/insight-api/tx/3e9b42ad28783094896d3c58fa3789d5c41aff643a4cd93eda976dedbad7d6a2) | A | 15 Nov 2026 ~6:55 AM MST |
| DCG payout address: 228,469 DASH in and out lifetime; 63,377 in 12 months | [Chainz](https://chainz.cryptoid.info/dash/address.dws?7mUyau75ATy1c6LoZeG3D57jKBkR4iHJkE.htm) · [Insight raw](https://insight.dash.org/insight-api/addr/7mUyau75ATy1c6LoZeG3D57jKBkR4iHJkE) · [12-month tx list](https://insight.dash.org/insight-api/txs?address=7mUyau75ATy1c6LoZeG3D57jKBkR4iHJkE) | A | 15 Nov 2026 ~6:55 AM MST |
| 1 Oct 2026: 500 → `XvEU6pEW…`, 4,332 → `7pk3RNRA…` | [tx 442325c1…](https://chainz.cryptoid.info/dash/tx.dws?442325c1cbfe13c8dfe228371c43c5f998825a72b9af1596bb1fbe5da42c4332.htm) · [raw](https://insight.dash.org/insight-api/tx/442325c1cbfe13c8dfe228371c43c5f998825a72b9af1596bb1fbe5da42c4332) · [`XvEU6pEW…`](https://chainz.cryptoid.info/dash/address.dws?XvEU6pEWA2oC4FVdcxVdXcxHaMjyLZvPdt.htm) · [`7pk3RNRA…`](https://chainz.cryptoid.info/dash/address.dws?7pk3RNRAwCiteq5Bs8RdS4jCqYwMmVT9qd.htm) | A | 15 Nov 2026 ~6:55 AM MST |
| 2 Nov 2026: 163 → `XchbTk8r…`, 4,669 → `7f1kNTrK…` | [tx dc6a7a22…](https://chainz.cryptoid.info/dash/tx.dws?dc6a7a2240209b7f284ba3d021c2585b19ae87aad97d00b8563d001a2667a949.htm) · [raw](https://insight.dash.org/insight-api/tx/dc6a7a2240209b7f284ba3d021c2585b19ae87aad97d00b8563d001a2667a949) · [`7f1kNTrK…`](https://chainz.cryptoid.info/dash/address.dws?7f1kNTrKnzcDfp9sXvschTvjpLxjKKFgun.htm) | A | 15 Nov 2026 ~6:55 AM MST |
| 22 Nov 2025: 2,000 → `XvEU6pEW…`, 3,196 → `7pAv6sYX…` | [tx 9384ba58…](https://chainz.cryptoid.info/dash/tx.dws?9384ba58659fa6754758a01a78535a8249b59528b37583f6074ae80fe3d8ea68.htm) · [raw](https://insight.dash.org/insight-api/tx/9384ba58659fa6754758a01a78535a8249b59528b37583f6074ae80fe3d8ea68) · [`7pAv6sYX…`](https://chainz.cryptoid.info/dash/address.dws?7pAv6sYXvDPn9gG5ktQPhmJpkYPvnVPZrw.htm) | A | 15 Nov 2026 ~6:55 AM MST |
| 2 Feb 2026: 271 → `XoHhGzZn…`, 5,070 → `7YHgvcG4…` | [tx 58df107c…](https://chainz.cryptoid.info/dash/tx.dws?58df107cbce3c2a7298cde7eee44e400f650a47ed8c9a28f9d3dff791a25a060.htm) · [raw](https://insight.dash.org/insight-api/tx/58df107cbce3c2a7298cde7eee44e400f650a47ed8c9a28f9d3dff791a25a060) · [`7YHgvcG4…`](https://chainz.cryptoid.info/dash/address.dws?7YHgvcG4UBtZMmBggKxcUvxDTWdzPTCBeT.htm) | A | 15 Nov 2026 ~6:55 AM MST |
| Arkham does not cover Dash (downstream owners open) | [Arkham `7pk3RNRA…`](https://intel.arkm.com/explorer/address/7pk3RNRAwCiteq5Bs8RdS4jCqYwMmVT9qd) | B | 15 Nov 2026 ~11:05 AM MST |
| No premine; budget does not change emission | [Dash docs: governance](https://docs.dash.org/en/stable/docs/user/governance/understanding.html) | A | 15 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exact path to close it | Cost / access |
|---|---|---|---|
| 1 | Do DCG's downstream wallets ([`7pk3RNRA…`](https://chainz.cryptoid.info/dash/address.dws?7pk3RNRAwCiteq5Bs8RdS4jCqYwMmVT9qd.htm), [`7f1kNTrK…`](https://chainz.cryptoid.info/dash/address.dws?7f1kNTrKnzcDfp9sXvschTvjpLxjKKFgun.htm), [`7c7of2xz…`](https://chainz.cryptoid.info/dash/address.dws?7c7of2xznwtYy3p2EMxLEaoDC996Q1CSfm.htm), [`XvEU6pEW…`](https://chainz.cryptoid.info/dash/address.dws?XvEU6pEWA2oC4FVdcxVdXcxHaMjyLZvPdt.htm) etc.) sell on exchanges, and when? | **Arkham checked 15 Nov 2026: Dash not supported; stays open.** Insight `GET /insight-api/txs?address={addr}` for each, 2–3 hops; match against exchange deposit clusters | Insight free; exchange labels need Arkham or Chainalysis (paid) or a disclosure request to DCG |
| 2 | DCG's monthly sales / treasury policy | Ask DCG for its finance or transparency report; check dash.org/forum DCG budget threads and the proposal pages on DashCentral | Free; request to DCG |
| 3 | DCG legal registration and officers | OpenCorporates search for "Dash Core Group, Inc." to find the registering state, then that state's official business-entity search for officers and status; IRS 990 not applicable (for-profit) | Free |
| 4 | Who holds the ~4.03M DASH mined on 19–20 Jan 2014 | Blockchair `dash/outputs?q=block_id(0..9808),is_spent(false)` to measure how much is still unspent, then cluster by address | Blockchair free tier is rate-limited; a key (paid) for bulk |
| 5 | Exact masternode and evonode counts and collateral | Dash Core RPC `masternode count` / `protx list valid 1` (run a node), or Insight-compatible masternode list endpoint; collateral sizes from docs.dash.org masternode setup pages | Free (own node) |
| 6 | Whether Dash counts as an "anonymity-enhancing coin" under AMLR Art. 79 | EUR-Lex text of Regulation (EU) 2024/1624; AMLA / EBA guidance or RTS when published; ask a major EU CASP (e.g. Bitvavo, Kraken EU) for its listing position | Free |
| 7 | Mining-pool concentration and 51% / ChainLock coverage | Blockchair `dash/blocks?a=guessed_miner,count()` for the last 30 days; Dash docs on ChainLocks | Free |
| 8 | Merchant and payment partners (Flexa, Dash–Zebec card) | Flexa's own asset list (flexa.network) and Zebec's official announcements; need a partner-side primary record | Free |
| 9 | Platform usage (DashPay usernames, credits burned) | `dashpay/platform` explorer (platform-explorer.com) or Platform DAPI queries | Free |
| 10 | Why Blockchair's 4.03M launch-week figure differs from the often-quoted ~1.9M "instamine" | Re-run the aggregate by block height ranges (first 24h vs 48h) and compare with the Dash wiki and historic forum disclosure | Free |

**Unverified items: 10**

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
