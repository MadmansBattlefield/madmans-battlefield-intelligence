---
ticker: BCH
name: Bitcoin Cash
chain: bitcoin-cash
contract: "native (Bitcoin Cash proof-of-work chain)"
overall_score: 5.2
overall_verdict: FAIL
section_scores:
  revenue: 1
  foundation_team: 4
  insider_holdings: 9
  selling_behavior: 7
  tokenomics_supply: 8
  liquidity_market: 7
  product_development: 5
  adoption_customers: 3
  security_audits: 5
  regulatory: 8
  catalysts: 4
gates_failed: [revenue]
red_lines:
  hack_exploit: "none in the review window; structural 51%-attack risk (hashrate ~0.3% of Bitcoin's)"
  mint_path_live: "no: fixed 21M cap; block subsidy halves every 210,000 blocks"
  team_wallet_to_exchange_during_pump: "not applicable: no team, foundation, premine or treasury wallets exist"
  one_hop_sale_status: none_found
  treasury_selling: "not applicable: no treasury"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "No burn, buyback or fee share; fees go to miners."
pump_day_price_source: "Gate BCH_USDT UTC daily closes, re-run 16 Nov 2026 with scripts/pump_day_test.py (30 of 360 days); the body's earlier count used CoinGecko daily closes"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions: []
price_usd: 205.79
price_source: "CoinGecko, 16 Nov 2026 6:58 AM MST"
last_updated: 2026-11-17
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### BCH · Overall grade **5.2 / 10 · ❌ FAIL**

**Summary:** Bitcoin Cash is a 2017 proof-of-work fork of Bitcoin. It has a fixed 21M cap, no premine, no team allocation and no foundation, so there are **no insider wallets to sell into pumps**, and it scores well on holdings, tokenomics and selling. But the protocol itself earns nothing: **fees ($44.4k in 12 months) all go to miners**, and DefiLlama counts $0 of protocol revenue, so the revenue gate fails. Usage is thin (about 14k transactions a day). Its hashrate is ~0.3% of Bitcoin's, which leaves it exposed to a 51% attack.

**🚨 Top warning:** BCH is secured by only **~3.5 EH/s**, against ~1,133 EH/s on Bitcoin ([Blockchair stats](https://blockchair.com/bitcoin-cash)). Hash power using the same SHA-256 hardware could be pointed at BCH to reorganize it. The price is −58% in a year and −95% from its 2017 high. There is no treasury or development fund: developers rely on voluntary crowdfunding. Every link is in the 🔗 Evidence trail below.

**Sections passed: 5 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 1/10 | ❌ FAIL (hard gate) |
| 🏛️ Foundation & team | 4/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 9/10 | ✅ PASS |
| 📉 Selling behavior | 7/10 | ✅ PASS |
| 📊 Tokenomics & supply | 8/10 | ✅ PASS |
| 💧 Liquidity & market | 7/10 | ✅ PASS |
| 🧑‍💻 Product & development | 5/10 | ❌ FAIL |
| 🤝 Adoption & customers | 3/10 | ❌ FAIL |
| 🛡️ Security & audits | 5/10 | ❌ FAIL |
| ⚖️ Regulatory | 8/10 | ✅ PASS |
| 📅 Catalysts & calendar | 4/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 BCH · Bitcoin Cash · 5.2 / 10 · ❌ FAIL

> **One line:** Clean supply and no insiders, but no protocol revenue, little usage and a small, rentable hashrate.

| 📊 Market (CoinGecko, 16 Nov 2026 6:58 AM MST) | 🔗 On-chain ([Blockchair](https://blockchair.com/bitcoin-cash), 16 Nov 2026) |
|---|---|
| **Price** $205.79 | **Block height** 977,635 |
| **24h / 7d / 30d** 🔴 −2.2% / −14.9% / −24.6% · 1y −57.9% | **Supply** 20.118M of a 21M cap (95.8%) |
| **Market cap** $4.14B · **FDV** $4.14B | **Hashrate (24h)** ~3.55 EH/s (~0.3% of Bitcoin) |
| **24h volume** $62.7M (CoinGecko aggregate) | **Transactions (24h)** 14,095 · avg fee $0.005 |
| **ATH** $3,785.82 (19 Dec 2017) · now −94.6% | **Nodes** 612 |
| **Pump days, last 365 days** 30 (Binance BCHUSDT closes) | **TVL** $4.5M (DefiLlama) |

---

## 💰 Revenue — Does it make money? · 1/10 · ❌ FAIL (hard gate)

| Metric | Value | Source |
|---|---:|---|
| Fees, last 12 months | **$44,393** (30 days: $2,339), all paid to miners | [Tier A] [DefiLlama, `bitcoin-cash` fees](https://api.llama.fi/summary/fees/bitcoin-cash?dataType=dailyFees) |
| Protocol revenue / to holders | **$0** (no burn, no treasury) | [Tier A] [DefiLlama revenue](https://api.llama.fi/summary/fees/bitcoin-cash?dataType=dailyRevenue) |

**What it means:** Like every PoW coin without a burn, holders capture nothing, and even the miners' fee income is tiny. **1 → hard-gate FAIL.**

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** No burn, buyback or fee share; fees go to miners.

## 🏛️ Foundation & team — Who is in charge? · 4/10 · ❌ FAIL

- There is no foundation or company. Several volunteer node teams (e.g. Bitcoin Cash Node) coordinate a yearly May upgrade through public CHIP proposals. Funding is voluntary crowdfunding. The 2020 plan to divert miner rewards to developers was abandoned (and split off the eCash chain). Accountable leadership and funding are weak.

## 🪙 Foundation / team holdings — How many coins do they hold? · 9/10 · ✅ PASS

- **None.** BCH split from Bitcoin at block 478,558 (Aug 2017), so every coin was mined or carried over. There is no premine and no team allocation. Large legacy holders (dormant early-Bitcoin coins, exchange estates) are an overhang, but they are not insiders.

## 📉 Selling behavior — Do insiders sell into pumps? · 7/10 · ✅ PASS

- With no team, foundation or treasury wallets, the insider pump-day test does not apply. The 30 pump days in the last year (largest +47.5% on 22 Sep 2026, +41.4% on 21 Aug 2026) coincide with market-wide moves seen in other coins on the same dates.
- Ongoing sell pressure comes from miners (~3.125 BCH a block, ~450 BCH a day ≈ $93k a day). This is normal PoW selling, not insider dumping.

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from Gate BCH_USDT UTC daily closes, re-run 16 Nov 2026 with scripts/pump_day_test.py (30 of 360 days); the body's earlier count used CoinGecko daily closes.

## 📊 Tokenomics & supply · 8/10 · ✅ PASS

- Fixed **21M cap**. 95.8% is already issued. The subsidy is 3.125 BCH a block since the April 2024 halving; the next halving is at block 1,050,000 (~April 2028, estimated from 10-minute blocks).

## 💧 Liquidity & market · 7/10 · ✅ PASS

- $4.1B cap, listed on every major exchange. CoinGecko's aggregate 24h volume of $62.7M (1.5% of cap) is modest, and its top venue list is led by smaller exchanges.

## 🧑‍💻 Product & development · 5/10 · ❌ FAIL

- Steady yearly upgrades: [May 2025](https://upgradespecs.bitcoincashnode.org/2025-05-15-upgrade/) added VM limits and BigInt arithmetic; [May 2026](https://upgradespecs.bitcoincashnode.org/2026-05-15-upgrade/) added Pay-to-Script, bounded loops, functions and bitwise ops. CashTokens exist, but few apps use them.

## 🤝 Adoption & customers · 3/10 · ❌ FAIL

- About 14k transactions a day and $4.5M of TVL. Payments use is a niche.

## 🛡️ Security & audits · 5/10 · ❌ FAIL

- No consensus failure in the window. But the hashrate is ~0.3% of Bitcoin's on the same SHA-256 hardware, so a deep reorganization is economically feasible for a large miner or pool.

## ⚖️ Regulatory · 8/10 · ✅ PASS

- **US:** SEC Release 33-11412 (issued 17 Mar 2026, effective 23 Mar 2026, joined by the CFTC) names **Bitcoin Cash (BCH)** as an example of a **digital commodity**, which is not a security ([Tier A] [govinfo](https://www.govinfo.gov/content/pkg/FR-2026-03-23/html/2026-05635.htm)). It is a decentralized PoW asset available on US-regulated venues. No enforcement against the asset found.
- **Correction, 17 Nov 2026:** Regulatory **7 → 8** after Release 33-11412 was applied. Overall **5.1 → 5.2**. Still FAIL on the revenue gate.

## 📅 Catalysts & calendar · 4/10 · ❌ FAIL

| Date | Event |
|---|---|
| 15 May 2027 | Next yearly network upgrade (CHIPs TBD) |
| ~Apr 2028 | Halving (block 1,050,000) |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟡 None, but structural 51%-attack risk |
| Team wallet → exchange during a pump | 🟢 Not applicable (no team wallets) |
| Live mint path | 🟢 None beyond the fixed schedule |
| Treasury selling | 🟢 Not applicable |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| No team, foundation or treasury wallets | — | — | high | n/a | None: insider test does not apply |

## 📚 Sources

- [Tier A] Methodology update 16 Nov 2026: no new Arkham lookups; the attribution table uses evidence already cited in this report.
- [Tier A] [Blockchair Bitcoin Cash stats](https://blockchair.com/bitcoin-cash) (height, circulation, hashrate, transactions, nodes), 16 Nov 2026 ~7:30 AM MST; [Blockchair Bitcoin](https://blockchair.com/bitcoin) hashrate for comparison
- [Tier A] [Bitcoin Cash upgrade specifications](https://upgradespecs.bitcoincashnode.org/) (2025 and 2026 upgrades)
- [Tier B] Arkham, read 16 Nov 2026 ~7:35 AM MST (signed-in account): **Bitcoin Cash is not supported.** The network selector lists only Ethereum, Polygon, BNB Chain, Optimism, Avalanche, Arbitrum, Base, Bitcoin, Tron, Flare, Solana, Dogecoin, Zcash, HyperEVM, Hypercore, Robinhood Chain. BCH also has no foundation, team or treasury wallets to look up (no premine, no dev fund). No Arkham labels were available for this report
- [Tier A] DefiLlama `bitcoin-cash` fees, revenue and TVL; CoinGecko `bitcoin-cash` (16 Nov 2026 6:58 AM MST); Binance BCHUSDT daily closes (2024 onward)

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Supply 20.118M of 21M; height 977,635 | [Blockchair](https://blockchair.com/bitcoin-cash) | A | 16 Nov 2026 |
| Hashrate ~3.55 EH/s vs Bitcoin ~1,133 EH/s | [BCH](https://blockchair.com/bitcoin-cash) · [BTC](https://blockchair.com/bitcoin) | A | 16 Nov 2026 |
| Fees $44.4k, revenue $0 | [fees](https://api.llama.fi/summary/fees/bitcoin-cash?dataType=dailyFees) · [revenue](https://api.llama.fi/summary/fees/bitcoin-cash?dataType=dailyRevenue) | A | 16 Nov 2026 |
| 2025 / 2026 upgrades | [2025](https://upgradespecs.bitcoincashnode.org/2025-05-15-upgrade/) · [2026](https://upgradespecs.bitcoincashnode.org/2026-05-15-upgrade/) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Large legacy holders (exchange estates, dormant early coins) moving on pump days** | Track known estate and custodian clusters with a BCH explorer (Arkham does not cover Bitcoin Cash). There are no insider addresses to look up | Free |
| 2 | **Real exchange volume** | Compare Binance/Coinbase/Kraken reported volume with CoinGecko's aggregate | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.

- Research only. Not investment advice.
