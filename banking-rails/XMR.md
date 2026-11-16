---
ticker: XMR
name: Monero
chain: monero
contract: "native (Monero proof-of-work chain, RandomX)"
overall_score: 5.2
overall_verdict: FAIL
section_scores:
  revenue: 2
  foundation_team: 5
  insider_holdings: 9
  selling_behavior: 7
  tokenomics_supply: 7
  liquidity_market: 6
  product_development: 6
  adoption_customers: 6
  security_audits: 5
  regulatory: 2
  catalysts: 5
gates_failed: [revenue]
red_lines:
  hack_exploit: "18-block reorganization on 14 Sep 2025 during the Qubic mining campaign; only 1-block reorgs since Aug 2026"
  mint_path_live: "no: fixed tail emission of 0.6 XMR a block (about 0.8% a year), set in the protocol"
  team_wallet_to_exchange_during_pump: "not applicable: no premine, no team or treasury allocation (fair launch, 2014)"
  one_hop_sale_status: none_found
  regulatory_delisting: "yes: delisted from Binance (2024); EU AMLR bars EU crypto-asset service providers from handling anonymity-enhancing coins from 10 Jul 2027"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "Fees go to miners; nothing accrues to holders."
pump_day_price_source: "MEXC XMRUSDT UTC daily closes, re-run 16 Nov 2026 with scripts/pump_day_test.py (30 of 360 days); the body's earlier count used not applicable (no insider wallets)"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions: []
price_usd: 498.04
price_source: "CoinGecko, 16 Nov 2026 8:15 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### XMR · Overall grade **5.2 / 10 · ❌ FAIL**

**Summary:** Monero is the leading privacy coin: proof-of-work, no premine, no team allocation, and real day-to-day use (about **39k transactions a day**, **$1.38M of fees** in 12 months). It scores well on holdings, selling and supply. But the fees all go to miners and holders capture nothing, so the revenue gate fails. Its main risk is **regulatory**: it has been delisted from Binance and other large venues, and EU rules will bar EU-licensed exchanges from handling it from **10 Jul 2027**.

**🚨 Top warning:** regulated exchanges are being closed to it. EU Regulation 2024/1624 (AMLR) bars crypto-asset service providers from keeping accounts that allow anonymity, including through anonymity-enhancing coins, from 10 Jul 2027 ([EUR-Lex](https://eur-lex.europa.eu/eli/reg/2024/1624/oj)). Binance's XMRUSDT market still reports a frozen last price of $118.70 from its 2024 delisting, against $498 today, and CoinGecko's top venues are KuCoin and HTX. Separately, on 14 Sep 2025 an **18-block reorganization** reversed about 117 confirmed transactions during the Qubic mining campaign (Tier B). Every link is in the 🔗 Evidence trail below.

**Sections passed: 6 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 2/10 | ❌ FAIL (hard gate) |
| 🏛️ Foundation & team | 5/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 9/10 | ✅ PASS |
| 📉 Selling behavior | 7/10 | ✅ PASS |
| 📊 Tokenomics & supply | 7/10 | ✅ PASS |
| 💧 Liquidity & market | 6/10 | ✅ PASS |
| 🧑‍💻 Product & development | 6/10 | ✅ PASS |
| 🤝 Adoption & customers | 6/10 | ✅ PASS |
| 🛡️ Security & audits | 5/10 | ❌ FAIL |
| ⚖️ Regulatory | 2/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 5/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 XMR · Monero · 5.2 / 10 · ❌ FAIL

> **One line:** A clean, genuinely used privacy coin with no holder revenue and a shrinking set of regulated exchanges.

| 📊 Market (CoinGecko, 16 Nov 2026 8:15 AM MST) | 🔗 On-chain ([xmrchain.net](https://xmrchain.net/api/networkinfo), 16 Nov 2026 8:19 AM MST) |
|---|---|
| **Price** $498.04 | **Height** 3,807,739 · hard-fork version 16 |
| **24h / 7d / 30d** +0.2% / 🔴 −17.1% / −9.2% · 1y +20.4% | **Supply** 18,831,786 XMR (emission API) |
| **Market cap** $9.38B · **FDV** $9.38B | **Hashrate** ~7.07 GH/s (RandomX) |
| **24h volume** $121.6M (KuCoin $59.0M, HTX $19.8M, Poloniex, Kraken) | **Transactions** ~38.7k a day (5,823 in the last 100 blocks, ~3.6 h) |
| **ATH** $797.73 (14 Jan 2026) · now −37.6% | **Fees** $1.38M in 12 months · $121k in 30 days (DefiLlama) |
| **Pump days, last 365 days** 30 (CoinGecko daily closes; largest +59.2% on 15 Jan 2026) | **Tail emission** 0.6 XMR a block |

---

## 💰 Revenue — Does it make money? · 2/10 · ❌ FAIL (hard gate)

| Metric | Value | Source |
|---|---:|---|
| Fees, last 12 months | **$1,375,524** (30 days: $121,224), all paid to miners | [Tier A] [DefiLlama `monero` fees](https://api.llama.fi/summary/fees/monero?dataType=dailyFees) |
| Revenue to holders | **$0** (no burn, no treasury) | — |

**What it means:** Real paid usage, but none of it accrues to holders. **2 → hard-gate FAIL.**

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** Fees go to miners; nothing accrues to holders.

## 🏛️ Foundation & team — Who is in charge? · 5/10 · ❌ FAIL

- No company or foundation controls Monero. A volunteer core team maintains the reference software, and development is funded by community crowdfunding (the CCS). Upgrades are decided in open developer meetings, so there are no dated commitments.

## 🪙 Foundation / team holdings — How many coins do they hold? · 9/10 · ✅ PASS

- **None.** Monero launched in 2014 with no premine and no team or treasury allocation; every coin was mined.

## 📉 Selling behavior — Do insiders sell into pumps? · 7/10 · ✅ PASS

- No team wallets exist, and transaction privacy makes holder flows untraceable by design. The 30 pump days (largest run 13–16 Jan 2026, +44% to +59%, leading to the 14 Jan ATH) were market-wide privacy-coin moves. Sell pressure comes from miners: 0.6 XMR a block ≈ 432 XMR a day (≈ $215k).

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from MEXC XMRUSDT UTC daily closes, re-run 16 Nov 2026 with scripts/pump_day_test.py (30 of 360 days); the body's earlier count used not applicable (no insider wallets).

## 📊 Tokenomics & supply · 7/10 · ✅ PASS

- The main emission curve ended in 2022; since then a fixed **0.6 XMR a block** tail emission adds about 0.8% a year, falling slowly as a percentage. Supply is 18.83M ([emission API](https://xmrchain.net/api/emission)).

## 💧 Liquidity & market · 6/10 · ✅ PASS

- $121.6M of 24h volume (1.3% of cap), but concentrated on offshore venues (KuCoin, HTX, Poloniex) after major-exchange delistings. Kraken still lists a USD pair.

## 🧑‍💻 Product & development · 6/10 · ✅ PASS

- The next major upgrade, FCMP++ (full-chain membership proofs) with the Carrot address scheme, is in beta stress-testing: a test-network fork at block 3,102,800 on 5 Oct 2026 and build v0.19.0.0-beta.3.1 on 26 Oct 2026 (Tier B). It has no mainnet date.

## 🤝 Adoption & customers · 6/10 · ✅ PASS

- About 38.7k transactions a day and $1.38M of yearly fees: among the most used payment chains outside Bitcoin, Ethereum and stablecoin rails.

## 🛡️ Security & audits · 5/10 · ❌ FAIL

- On 14 Sep 2025 an 18-block reorganization (heights 3,499,659–3,499,676) reversed about 117 transactions, past the 10-block lock most services used as final, during the Qubic mining campaign. Qubic began moving its miners to Dogecoin on 1 Apr 2026 (Tier B). Since Aug 2026 a monitoring node has seen only 1-block reorgs ([monerometrics](https://monerometrics.net/reorgs), Tier B). The network hashrate (~7.07 GH/s) can still be outbid by a paid CPU-mining scheme.

## ⚖️ Regulatory · 2/10 · ❌ FAIL

- [EU AMLR (Reg. 2024/1624)](https://eur-lex.europa.eu/eli/reg/2024/1624/oj) bars EU crypto-asset service providers from accounts that allow anonymisation, including through anonymity-enhancing coins, from 10 Jul 2027.
- Binance delisted XMR in 2024; its API still shows a frozen last price of [$118.70](https://data-api.binance.vision/api/v3/ticker/price?symbol=XMRUSDT).

## 📅 Catalysts & calendar · 5/10 · ❌ FAIL

| Date | Event |
|---|---|
| 10 Jul 2027 | EU AMLR anonymity-coin ban for CASPs takes effect |
| Not dated | FCMP++/Carrot hard fork (still in stressnet; testnet not started) |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟡 18-block reorg Sep 2025; 1-block reorgs since |
| Team wallet → exchange during a pump | 🟢 Not applicable (no premine or team) |
| Live mint path | 🟢 Fixed tail emission only |
| Regulatory delisting | 🔴 Binance delisted; EU ban from Jul 2027 |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| No team, foundation or treasury wallets | — | — | high | n/a | None: insider test does not apply |

## 📚 Sources

- [Tier A] Methodology update 16 Nov 2026: no new Arkham lookups; the attribution table uses evidence already cited in this report.
- [Tier A] xmrchain.net explorer API (`networkinfo`, `emission`, `transactions`), 16 Nov 2026 8:19 AM MST
- [Tier A] DefiLlama `monero` fees; CoinGecko `monero` (16 Nov 2026 8:15 AM MST) and 365-day closes; Binance public API ticker
- [Tier A] [EU Regulation 2024/1624](https://eur-lex.europa.eu/eli/reg/2024/1624/oj)
- [Tier B] [XMR Daily, Qubic timeline](https://xmrdaily.com/qubic-monero-selfish-mining-attack-timeline-aftermath/); [XMR Daily, FCMP++ status](https://xmrdaily.com/monero-fcmp-plus-plus-hard-fork-status-november-2026/); [Monero Observer, stressnet v3.0](https://monero.observer/fcmp++-carrot-beta-stressnet-v3.0-released/); [monerometrics reorgs](https://monerometrics.net/reorgs)
- Arkham does not cover Monero (16 Nov 2026), and there are no team or treasury wallets to look up; Monero transactions are private

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Height, hashrate | [networkinfo](https://xmrchain.net/api/networkinfo) | A | 16 Nov 2026 |
| Supply 18.83M | [emission](https://xmrchain.net/api/emission) | A | 16 Nov 2026 |
| Fees $1.38M / 12 months | [DefiLlama](https://api.llama.fi/summary/fees/monero?dataType=dailyFees) | A | 16 Nov 2026 |
| EU anonymity-coin ban from Jul 2027 | [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2024/1624/oj) | A | 16 Nov 2026 |
| 18-block reorg, Sep 2025 | [XMR Daily](https://xmrdaily.com/qubic-monero-selfish-mining-attack-timeline-aftermath/) · [monerometrics](https://monerometrics.net/reorgs) | B ×2 | 16 Nov 2026 |
| FCMP++ has no mainnet date | [XMR Daily](https://xmrdaily.com/monero-fcmp-plus-plus-hard-fork-status-november-2026/) · [Monero Observer](https://monero.observer/fcmp++-carrot-beta-stressnet-v3.0-released/) | B ×2 | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Which venues will still list XMR after Jul 2027** | Track delisting notices from Kraken and EU-licensed exchanges | Free |
| 2 | **Pool hashrate concentration** | Check pool share on miningpoolstats against P2Pool's share | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.

- Research only. Not investment advice.
