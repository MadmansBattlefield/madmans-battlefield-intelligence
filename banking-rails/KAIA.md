---
ticker: KAIA
name: Kaia
chain: kaia
contract: "native (Kaia mainnet, chain id 8217); canonical WKAIA 0x19Aac5f612f524B754CA7e7c41cbFa2E981A4432"
overall_score: 3.9
overall_verdict: FAIL
section_scores:
  revenue: 1
  foundation_team: 6
  insider_holdings: 5
  selling_behavior: 4
  tokenomics_supply: 3
  liquidity_market: 3
  product_development: 6
  adoption_customers: 4
  security_audits: 6
  regulatory: 6
  catalysts: 4
gates_failed: [revenue]
red_lines:
  hack_exploit: "none found on Kaia mainnet"
  mint_path_live: "yes: 9.6 KAIA minted per block (~300M a year, ~5.2% inflation), with no cap; half goes to Foundation-run KEF/KIF"
  team_wallet_to_exchange_during_pump: "not tested: Kaiascan's API needs a key this pass did not have, so fund-wallet outflows could not be traced"
  treasury_selling: "KIF budget explicitly covers 'token swap' and 'providing market liquidity'; ~295M KAIA disbursed from the KIF executor and ~129M from KEF since Aug 2024; destinations only on Kaia Square"
price_usd: 0.02917
price_source: "CoinGecko, 16 Nov 2026 6:58 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### KAIA · Overall grade **3.9 / 10 · ❌ FAIL**

**Summary:** Kaia is the merged Klaytn (Kakao) and Finschia (LINE) chain. The Foundation is visible and publishes every fund transfer, but the chain earns almost nothing: **$43.8k of revenue in 12 months** against about **300M KAIA (~$8.8M) of new issuance a year**. Half of that issuance goes to two Foundation-run funds, and one of them is budgeted for "providing market liquidity". TVL is $5.3M and daily volume $3.6M. The price is −93% from its high. The revenue gate fails. Selling could not be tested on-chain this pass.

**🚨 Top warning:** Every block mints new KAIA, and **25% goes to the KIF**. The Foundation spends the KIF on operations, "token swap" and "providing market liquidity" ([token economy docs](https://docs.kaia.io/learn/token-economics/token-economy/)). The KIF executor [`0x587e…fcde`](https://kaiascan.io/address/0x587e624a5e8d8b6064643eab18734245a9defcde) has received **319.3M KAIA in 10 announced transfers** ([Aug 2024](https://govforum.kaia.io/t/896) to [Nov 2026](https://govforum.kaia.io/t/1540)). It holds **23.8M** now, so **~295M KAIA (~$8.6M at today's price) has gone out**, and that cannot be traced here. Every link is in the 🔗 Evidence trail below.

**Sections passed: 4 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 1/10 | ❌ FAIL (hard gate) |
| 🏛️ Foundation & team | 6/10 | ✅ PASS |
| 🪙 Foundation / team holdings | 5/10 | ❌ FAIL |
| 📉 Selling behavior | 4/10 | ❌ FAIL (not proven) |
| 📊 Tokenomics & supply | 3/10 | ❌ FAIL |
| 💧 Liquidity & market | 3/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 6/10 | ✅ PASS |
| 🤝 Adoption & customers | 4/10 | ❌ FAIL |
| 🛡️ Security & audits | 6/10 | ✅ PASS |
| ⚖️ Regulatory | 6/10 | ✅ PASS |
| 📅 Catalysts & calendar | 4/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 KAIA · Kaia · 3.9 / 10 · ❌ FAIL

> **One line:** A transparent Foundation running an inflationary chain that barely earns anything.

| 📊 Market (CoinGecko, 16 Nov 2026 6:58 AM MST) | 🔗 On-chain (Kaia RPC, 16 Nov 2026) |
|---|---|
| **Price** $0.0292 | **Token** native KAIA; [WKAIA](https://kaiascan.io/address/0x19Aac5f612f524B754CA7e7c41cbFa2E981A4432) |
| **24h / 7d / 30d** 🔴 −1.1% / −7.6% / −33.6% · 1y −66.7% | **Supply** 6.469B, no cap; +9.6 KAIA a block |
| **Market cap** $188.5M · **FDV** $188.5M | **KEF mint** [`0x2D49…0926`](https://kaiascan.io/address/0x2D493DC06B73CF8Dede958FABBC9d62C31fA0926) 149.0M · **executor** [`0xdd41…ead8`](https://kaiascan.io/address/0xdd413c62b3882c4ea8398cb23714743d88fcead8) 25.9M |
| **24h volume** $3.6M (Bithumb, Binance, Upbit, BloFin, Bybit) | **KIF mint** [`0x4403…67D5`](https://kaiascan.io/address/0x440372e3cE41a85b7B5A6091c232470d186367D5) 48.1M · **executor** [`0x587e…fcde`](https://kaiascan.io/address/0x587e624a5e8d8b6064643eab18734245a9defcde) 23.8M |
| **ATH** $0.407 (2 Dec 2024) · now −92.8% | **KPF (GP-21)** [`0xAb6f…A6e0`](https://kaiascan.io/address/0xAb6ff701E1EF80253fdCa472D41160411077A6e0) 7.0M |
| **Pump days, last 365 days** 33 (Binance KAIAUSDT closes) | **TVL** $5.3M (DefiLlama) |

*Fund addresses come from the [Kaia contract-address docs](https://docs.kaia.io/references/contract-addresses/) and Foundation forum posts. Balances are from the public Kaia RPC.*

---

## 💰 Revenue — Does it make money? · 1/10 · ❌ FAIL (hard gate)

| Metric | Value | Source |
|---|---:|---|
| Chain fees, last 12 months | **$49,450** (30 days: $2,759) | [Tier A] [DefiLlama, `kaia`](https://api.llama.fi/summary/fees/kaia?dataType=dailyFees) |
| Revenue (burned fees), last 12 months | **$43,760** | [Tier A] [DefiLlama revenue](https://api.llama.fi/summary/fees/kaia?dataType=dailyRevenue) |

**What it means:** Revenue is about 0.5% of the value of new issuance. **1 → hard-gate FAIL.**

## 🏛️ Foundation & team — Who is in charge? · 6/10 · ✅ PASS

- The Kaia DLT Foundation runs the chain with a Governance Council of corporate validators (Kakao and LINE affiliates among them). Votes happen on Kaia Square, and every fund move is pre-announced on the [governance forum](https://govforum.kaia.io/t/1540).
- The Foundation has published a phased tokenomics reform ([GP-21](https://govforum.kaia.io/t/1451)): end proposal rewards, burn unearned rewards, review the issuance rate, and later fee-based buyback-and-burn.

## 🪙 Foundation / team holdings — How many coins do they hold? · 5/10 · ❌ FAIL

| Fund | Mint wallet | Executor | Sent to executor (announced) | Disbursed (approx.) |
|---|---:|---:|---:|---:|
| KEF (ecosystem) | 149.0M | 25.9M | 155M | ~129M |
| KIF (infrastructure / operations) | 48.1M | 23.8M | 319.3M | ~295M |
| KPF | 7.0M | — | — | — |

- Known fund balances total ~254M KAIA (3.9% of supply). The older KFF/KCF/KVC rebalance wallets are empty. The funds refill continuously from issuance.

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL (not proven)

- **Not tested on-chain.** Kaiascan's API requires an access key, and Etherscan's free tier does not cover Kaia, so KEF/KIF executor outflows could not be matched against exchange wallets or the 33 pump days. The biggest was **+61.3% on 9 Oct 2026, the Upbit KRW listing**.
- KIF's stated uses include "token swap" and "providing market liquidity" ([docs](https://docs.kaia.io/learn/token-economics/token-economy/)), so exchange-bound flows are an expected, disclosed use. Their timing is unknown.

## 📊 Tokenomics & supply · 3/10 · ❌ FAIL

- 9.6 KAIA a block, about 300M a year (~5.2%). The split is 50% validators/community, 25% KEF and 25% KIF. Since GP-21 (2026), unearned contribution rewards are burned. A review of the issuance rate is planned but not yet proposed.

## 💧 Liquidity & market · 3/10 · ❌ FAIL

- $3.6M of 24h volume on a $188M cap (1.9%), spread across Korean venues and Binance.

## 🧑‍💻 Product & development · 6/10 · ✅ PASS

- Mainnet live since Aug 2024 (Klaytn + Finschia merger), EVM-compatible. Gasless swaps, a native bridge, an MEV auction (GP-15) and LINE Mini Dapps. Permissionless validators are planned for 2026.

## 🤝 Adoption & customers · 4/10 · ❌ FAIL

- **TVL $5.3M** (DefiLlama). The Foundation itself reports about $170M of stablecoins on Kaia with under 3% used in DeFi ([GP-21 CR parameters](https://govforum.kaia.io/t/1460)).

## 🛡️ Security & audits · 6/10 · ✅ PASS

- No mainnet exploit found. Validators are still permissioned (the Governance Council).

## ⚖️ Regulatory · 6/10 · ✅ PASS

- Listed on the Korean majors (Upbit KRW since 9 Oct 2026, Bithumb). No enforcement found.

## 📅 Catalysts & calendar · 4/10 · ❌ FAIL

| Date | Event |
|---|---|
| 2026 (planned) | Permissionless validators; supply-phase tokenomics review |
| Ongoing | KEF/KIF budget transfers (forum announcements) |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | ⚪ Not tested (no explorer API access) |
| Live mint path | 🔴 ~5.2% a year, uncapped |
| Treasury selling | 🟡 KIF is budgeted for market liquidity; ~295M disbursed, not traced |

## 📚 Sources

- [Tier A] Kaia public RPC (`public-en.node.kaia.io`): fund balances, 16 Nov 2026 ~7:27 AM MST
- [Tier A] [Kaia docs: token economy](https://docs.kaia.io/learn/token-economics/token-economy/); [Kaia docs: contract addresses](https://docs.kaia.io/references/contract-addresses/)
- [Tier A] Kaia governance forum: KEF/KIF budget transfer announcements [896](https://govforum.kaia.io/t/896), [1028](https://govforum.kaia.io/t/1028), [1091](https://govforum.kaia.io/t/1091), [1190](https://govforum.kaia.io/t/1190), [1215](https://govforum.kaia.io/t/1215), [1439](https://govforum.kaia.io/t/1439), [1459](https://govforum.kaia.io/t/1459), [1489](https://govforum.kaia.io/t/1489), [1502](https://govforum.kaia.io/t/1502), [1540](https://govforum.kaia.io/t/1540); [GP-21](https://govforum.kaia.io/t/1451)
- [Tier B] Arkham, read 16 Nov 2026 ~7:35 AM MST (signed-in account): **Kaia is not supported.** The network selector lists only Ethereum, Polygon, BNB Chain, Optimism, Avalanche, Arbitrum, Base, Bitcoin, Tron, Flare, Solana, Dogecoin, Zcash, HyperEVM, Hypercore, Robinhood Chain. No Arkham labels were available for this report
- [Tier A] DefiLlama `kaia` fees, revenue and TVL; CoinGecko `kaia` (16 Nov 2026 6:58 AM MST); Binance KAIAUSDT daily closes
- [Unverified] where the ~424M KAIA disbursed from the KEF/KIF executors went. Arkham does not support Kaia (checked 16 Nov 2026)

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Issuance 9.6 KAIA a block; KIF uses include market liquidity | [docs](https://docs.kaia.io/learn/token-economics/token-economy/) | A | 16 Nov 2026 |
| KIF executor received 319.3M in 10 transfers | [first](https://govforum.kaia.io/t/896) · [latest](https://govforum.kaia.io/t/1540) · [executor](https://kaiascan.io/address/0x587e624a5e8d8b6064643eab18734245a9defcde) | A | 16 Nov 2026 |
| KEF executor received 155M | [first](https://govforum.kaia.io/t/896) · [executor](https://kaiascan.io/address/0xdd413c62b3882c4ea8398cb23714743d88fcead8) | A | 16 Nov 2026 |
| Revenue $43.8k / 12 months | [DefiLlama](https://api.llama.fi/summary/fees/kaia?dataType=dailyRevenue) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **KEF/KIF executor outflows vs. pump days** | Get a free Kaiascan API key and match the executors' outflows against Kaiascan exchange labels (Arkham does not cover Kaia) | Free key |
| 2 | **How much KIF went to "market liquidity"** | Read the Kaia Square disbursement records | Free |
| 3 | **Supply-phase reform (issuance cut?)** | Watch the governance forum | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.

- Research only. Not investment advice.
