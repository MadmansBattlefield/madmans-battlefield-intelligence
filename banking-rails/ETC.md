---
ticker: ETC
name: Ethereum Classic
chain: ethereum-classic
contract: "native (Ethereum Classic proof-of-work chain, chain id 61)"
overall_score: 4.1
overall_verdict: FAIL
section_scores:
  revenue: 1
  foundation_team: 3
  insider_holdings: 7
  selling_behavior: 6
  tokenomics_supply: 8
  liquidity_market: 5
  product_development: 3
  adoption_customers: 2
  security_audits: 3
  regulatory: 7
  catalysts: 3
gates_failed: [revenue]
red_lines:
  hack_exploit: "no exploit in the review window; history of 51%-attack reorganizations (Jan 2019, three in Aug 2020); hashrate still rentable"
  mint_path_live: "no: fixed emission schedule (ECIP-1017, 20% cut every 5M blocks), ~210.7M cap"
  team_wallet_to_exchange_during_pump: "not applicable: no live team or treasury allocation; the 2015 Ethereum genesis presale balances are legacy, not traced here"
  one_hop_sale_status: none_found
  treasury_selling: "not applicable today; the proposed Olympia upgrade (targeted 2027) would route base fees to a treasury contract"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "Holders capture nothing; fees go to miners."
pump_day_price_source: "Gate ETC_USDT UTC daily closes, re-run 16 Nov 2026 with scripts/pump_day_test.py (19 of 360 days); the body's earlier count used CoinGecko daily closes"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions: []
price_usd: 5.94
price_source: "CoinGecko, 16 Nov 2026 7:53 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### ETC · Overall grade **4.1 / 10 · ❌ FAIL**

**Summary:** Ethereum Classic is the original Ethereum chain that kept running after the 2016 DAO fork. It is proof-of-work with a capped emission schedule (~210.7M) and no team or treasury allocation, so insider selling is not the issue. The problem is that **almost nobody uses it**: about **7,100 transactions a day**, **$93k of DeFi TVL**, and **$7.0k of fees in a whole year** (all to miners). The revenue gate fails. Its hashrate (~173 TH/s) is small enough that it has been 51%-attacked four times, three of them in Aug 2020 (widely reported).

**🚨 Top warning:** usage has collapsed to a rounding error for a $945M coin. Blockscout counts **7,137 transactions today** and network utilization of **0.23%** ([Blockscout stats](https://etc.blockscout.com/api/v2/stats)), and DefiLlama shows **$256.85 of fees in the last 30 days**. The price is −60% in a year and −96% from its 2021 high. CoinGecko's top-volume venue is a small exchange (CoinUp.io), so reported volume may overstate real liquidity. Every link is in the 🔗 Evidence trail below.

**Sections passed: 4 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 1/10 | ❌ FAIL (hard gate) |
| 🏛️ Foundation & team | 3/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 7/10 | ✅ PASS |
| 📉 Selling behavior | 6/10 | ✅ PASS |
| 📊 Tokenomics & supply | 8/10 | ✅ PASS |
| 💧 Liquidity & market | 5/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 3/10 | ❌ FAIL |
| 🤝 Adoption & customers | 2/10 | ❌ FAIL |
| 🛡️ Security & audits | 3/10 | ❌ FAIL |
| ⚖️ Regulatory | 7/10 | ✅ PASS |
| 📅 Catalysts & calendar | 3/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 ETC · Ethereum Classic · 4.1 / 10 · ❌ FAIL

> **One line:** Clean, capped PoW supply with no insiders, but no fees, almost no users and a rentable hashrate.

| 📊 Market (CoinGecko, 16 Nov 2026 7:53 AM MST) | 🔗 On-chain ([Blockscout](https://etc.blockscout.com/), 16 Nov 2026 7:55 AM MST) |
|---|---|
| **Price** $5.94 | **Block height** 25,745,717 · avg block 12.3 s |
| **24h / 7d / 30d** 🔴 −0.3% / −12.7% / −24.4% · 1y −60.4% | **Supply** 159.04M of a ~210.7M cap (75.5%) |
| **Market cap** $944.6M · **FDV** $944.6M | **Transactions today** 7,137 · utilization 0.23% |
| **24h volume** $17.5M (CoinGecko aggregate) | **Hashrate** ~172.7 TH/s (pool-reported network figure) |
| **ATH** $167.09 (6 May 2021) · now −96.4% | **Fees** $6,979 in 12 months · $256.85 in 30 days (DefiLlama) |
| **Pump days, last 365 days** 19 (Binance ETCUSDT closes; largest +36.7% on 21 Aug 2026) | **DeFi TVL** $92.8k (DefiLlama) |

---

## 💰 Revenue — Does it make money? · 1/10 · ❌ FAIL (hard gate)

| Metric | Value | Source |
|---|---:|---|
| Fees, last 12 months | **$6,979** (30 days: $256.85), all paid to miners | [Tier A] [DefiLlama `ethereum-classic` fees](https://api.llama.fi/summary/fees/ethereum-classic?dataType=dailyFees) |
| Protocol revenue / to holders | **$0** (no burn, no treasury today) | No fee switch |

**What it means:** Holders capture nothing, and even miners' fee income is negligible. **1 → hard-gate FAIL.**

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** Holders capture nothing; fees go to miners.

## 🏛️ Foundation & team — Who is in charge? · 3/10 · ❌ FAIL

- No foundation controls the chain. Upgrades go through public ECIPs ([ECIP repository](https://github.com/ethereumclassic/ECIPs)). Development depends on a few volunteer and grant-funded client teams. There is no protocol treasury to pay them, which is exactly what the proposed Olympia upgrade tries to fix.

## 🪙 Foundation / team holdings — How many coins do they hold? · 7/10 · ✅ PASS

- No team, foundation or treasury allocation exists on ETC today. ETC shares Ethereum's 2015 genesis ledger, so presale and early-contributor balances from 2015 also exist on ETC; they are legacy holders, not a live insider allocation, and were not traced here.

## 📉 Selling behavior — Do insiders sell into pumps? · 6/10 · ✅ PASS

- With no team or treasury wallets, the insider pump-day test does not apply. The 19 pump days (largest +36.7% on 21 Aug 2026, +30.8% on 23 Aug, +25.5% on 22 Sep) line up with market-wide moves.
- Ongoing sell pressure is miner issuance: 1.6384 ETC a block (6th era, since block 25,000,000), about 11.5k ETC a day (≈ $68k) at ~12.3-second blocks.

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from Gate ETC_USDT UTC daily closes, re-run 16 Nov 2026 with scripts/pump_day_test.py (19 of 360 days); the body's earlier count used CoinGecko daily closes.

## 📊 Tokenomics & supply · 8/10 · ✅ PASS

- Fixed schedule under ECIP-1017: the block reward falls 20% every 5M blocks, toward a cap of ~210.7M. 159.04M (75.5%) is issued.

## 💧 Liquidity & market · 5/10 · ❌ FAIL

- $17.5M of aggregate 24h volume on a $945M cap (1.9%). CoinGecko's ticker list is led by CoinUp.io, Poloniex and Azbit rather than the largest exchanges, so real depth is likely thinner than the headline figure.

## 🧑‍💻 Product & development · 3/10 · ❌ FAIL

- The last mainnet upgrade was Spiral (Feb 2024). The next, [Olympia](https://ethereumclassic.com/news/olympia-upgrade-overview) (ECIP-1111/1112), would add EIP-1559 pricing and send base fees to a treasury contract; it is still on testnet with mainnet targeted for 2027 and no activation block set ([ECIP-1111](https://github.com/ethereumclassic/ECIPs/blob/master/_specs/ecip-1111.md)).

## 🤝 Adoption & customers · 2/10 · ❌ FAIL

- ~7,100 transactions a day, 0.23% of block capacity used, and $93k of DeFi TVL.

## 🛡️ Security & audits · 3/10 · ❌ FAIL

- ETC suffered deep 51% reorganizations in Jan 2019 and three times in Aug 2020 (widely reported; not re-sourced this session). The network hashrate today is ~172.7 TH/s on Etchash, hardware that can be rented, so the same attack remains economically possible. No exploit in the review window.

## ⚖️ Regulatory · 7/10 · ✅ PASS

- A decentralized PoW asset with no issuer; it trades on US-regulated venues and through a Grayscale trust. No enforcement against the asset found.

## 📅 Catalysts & calendar · 3/10 · ❌ FAIL

| Date | Event |
|---|---|
| 2027 (target, block TBD) | Olympia upgrade: EIP-1559 with base fees to a treasury |
| ~mid-2028 (block 30,000,000, estimated from 12.3-second blocks) | Next 20% block-reward cut (ECIP-1017) |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟡 None in window; history of 51% attacks |
| Team wallet → exchange during a pump | 🟢 Not applicable (no team wallets) |
| Live mint path | 🟢 None beyond the fixed schedule |
| Treasury selling | 🟢 Not applicable today |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| No team or treasury wallets | — | — | high | n/a | None |

## 📚 Sources

- [Tier A] Methodology update 16 Nov 2026: no new Arkham lookups; the attribution table uses evidence already cited in this report.
- [Tier A] [Blockscout ETC stats API](https://etc.blockscout.com/api/v2/stats) (height, transactions today, utilization, block time), 16 Nov 2026 7:55 AM MST
- [Tier B] 2miners ETC pool API, network hashrate field (172.7 TH/s), 16 Nov 2026 ~7:57 AM MST
- [Tier A] [ECIP-1111](https://github.com/ethereumclassic/ECIPs/blob/master/_specs/ecip-1111.md); [Olympia overview](https://ethereumclassic.com/news/olympia-upgrade-overview)
- [Tier A] DefiLlama `ethereum-classic` fees and chain TVL; CoinGecko `ethereum-classic` (16 Nov 2026 7:53 AM MST); Binance ETCUSDT daily closes for pump days
- [Tier B] Arkham, network list read 16 Nov 2026 ~7:35 AM MST (signed-in account): **Ethereum Classic is not supported.** Arkham's network selector lists only Ethereum, Polygon, BNB Chain, Optimism, Avalanche, Arbitrum, Base, Bitcoin, Tron, Flare, Solana, Dogecoin, Zcash, HyperEVM, Hypercore, Robinhood Chain. No Arkham labels were available for this report. ETC also has no team, foundation or treasury wallets to look up

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| 7,137 tx today, 0.23% utilization, height 25.75M | [Blockscout stats](https://etc.blockscout.com/api/v2/stats) | A | 16 Nov 2026 |
| Fees $6,979 / 12 months | [DefiLlama fees](https://api.llama.fi/summary/fees/ethereum-classic?dataType=dailyFees) | A | 16 Nov 2026 |
| TVL $92.8k | [DefiLlama chains](https://api.llama.fi/v2/chains) | A | 16 Nov 2026 |
| Olympia not yet active, 2027 target | [ECIP-1111](https://github.com/ethereumclassic/ECIPs/blob/master/_specs/ecip-1111.md) · [overview](https://ethereumclassic.com/news/olympia-upgrade-overview) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Legacy 2015 genesis balances moving on pump days** | Track the largest genesis-era ETC addresses on Blockscout around the Aug–Sep 2026 pump days | Free |
| 2 | **Real exchange volume** | Compare Binance/Coinbase/Kraken ETC volume with CoinGecko's aggregate | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.

- Research only. Not investment advice.
