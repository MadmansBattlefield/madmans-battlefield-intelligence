---
ticker: YELLOW
name: Yellow Network
chain: ethereum
contract: "0x236eb848c95b231299b4aa9f56c73d6893462720"
overall_score: 3.2
overall_verdict: FAIL
section_scores:
  revenue: 2
  foundation_team: 4
  insider_holdings: 2
  selling_behavior: 4
  tokenomics_supply: 3
  liquidity_market: 2
  product_development: 4
  adoption_customers: 3
  security_audits: 5
  regulatory: 5
  catalysts: 4
gates_failed: [revenue]
red_lines:
  hack_exploit: "none found"
  mint_path_live: "not proven: 10B minted once at genesis; no further mints seen"
  team_wallet_to_exchange_during_pump: "not proven: no project-tree transfer to a labelled exchange found within 3 hops; trading is 99% on the project's own venue"
  entity_concentration: "about 98% of supply sits in 6 project Treasury contracts and 4 wallets they funded"
price_usd: 0.08626
price_source: "CoinGecko, 16 Nov 2026 ~8:52 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### YELLOW · Overall grade **3.2 / 10 · ❌ FAIL**

**Summary:** Yellow Network sells itself as a clearing layer for state channels between brokers and exchanges. The token launched on 8 Mar 2026. All 10B YELLOW were minted to one Safe, which sent them to six contracts named "Treasury" on day one. Those Treasuries still hold **8.94B (89.4%)**, and wallets they funded hold another ~0.9B. Almost all trading (99%) happens on "Yellow PRO", the project's own exchange. That leaves a $92M market cap built on a tiny float. No protocol revenue is published, so the revenue gate fails.

**🚨 Top warning:** the float is very thin and the price is set on the project's own venue. On 3 Nov 2026, eight days after the all-time high, the largest Treasury [0xaec5…e72e](https://etherscan.io/address/0xaec5157545635a7523efb5abe3a37f52db7de72e) moved **500M YELLOW** (~$65M at that day's close) to a new plain wallet ([tx](https://etherscan.io/tx/0x0b5fec75a7913c21c70f7ecc1a8c10a8ef0ed5a5c9e781ed475497142c6aa199)). That is about half of today's stated circulating supply. Nothing has left that wallet yet. Every link is in the 🔗 Evidence trail below.

**Sections passed: 0 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 2/10 | ❌ FAIL (hard gate) |
| 🏛️ Foundation & team | 4/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 2/10 | ❌ FAIL |
| 📉 Selling behavior | 4/10 | ❌ FAIL (not proven) |
| 📊 Tokenomics & supply | 3/10 | ❌ FAIL |
| 💧 Liquidity & market | 2/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 4/10 | ❌ FAIL |
| 🤝 Adoption & customers | 3/10 | ❌ FAIL |
| 🛡️ Security & audits | 5/10 | ❌ FAIL |
| ⚖️ Regulatory | 5/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 4/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 YELLOW · Yellow Network · 3.2 / 10 · ❌ FAIL

> **One line:** A $92M market cap on under 2% free float, priced on the project's own exchange.

| 📊 Market (CoinGecko, 16 Nov 2026 ~8:52 AM MST) | 🔗 On-chain ([Etherscan](https://etherscan.io/token/0x236eb848c95b231299b4aa9f56c73d6893462720), 16 Nov 2026 ~9:05 AM MST) |
|---|---|
| **Price** $0.08626 | **Supply** 10,000,000,000 (one mint, 5 Mar 2026) |
| **24h / 7d / 30d** ⚪ +0.1% / 🔴 −25.8% / 🟢 +107.5% | **Treasury contracts** 8.94B (89.4%) |
| **Market cap** $91.7M · **FDV** $863M | **Wallets funded by Treasuries** ~0.90B (9.0%) |
| **24h volume** $2.49M, about 99% on Yellow PRO (the project's venue) | **Stated circulating** 1.063B (10.6%) |
| **ATH** $0.2087 (25 Oct 2026 UTC) · now −58.7% | **Custody contract** 34.1M |
| **Pump days** 41 since 13 Apr 2026 (largest +458.4% on 26 Oct 2026) | |

---

## 💰 Revenue — Does it make money? · 2/10 · ❌ FAIL (hard gate)

- No fee or revenue data on DefiLlama or in project reporting. Not found. **2 → hard-gate FAIL.**

## 🏛️ Foundation & team — Who is in charge? · 4/10 · ❌ FAIL

- Published allocation: Community Treasury 30%, Growth 25%, Foundation 20%, Sales 12.5%, Founders 10% (6-month cliff, then 60 months), Reserve 2.5% (project tokenomics page, Tier B). Which Treasury contract holds which bucket is not published [Unverified].

## 🪙 Foundation / team holdings — How many coins do they hold? · 2/10 · ❌ FAIL

| Holder | YELLOW now | Funded |
|---|---:|---|
| Treasury [0xe277…cfa9](https://etherscan.io/address/0xe277830b3444ea2cfee2b95f780c971222decfa9) | 2.50B | 8 Mar 2026 from genesis Safe |
| Treasury [0xaec5…e72e](https://etherscan.io/address/0xaec5157545635a7523efb5abe3a37f52db7de72e) | 2.49B | 3.0B, genesis |
| Treasury [0xfd8e…cd47](https://etherscan.io/address/0xfd8e336757ae9cdc0766264064b51492814fcd47) | 1.83B | 2.0B, genesis |
| Treasury [0xd572…f88b](https://etherscan.io/address/0xd572f3a0967856a09054578439ace81b2f2ff88b) | 1.12B | 1.25B, genesis |
| Treasury [0x914a…bac8](https://etherscan.io/address/0x914abadc0e36e03f29e4f1516951125c774dbac8) | 1.00B | 1.0B, genesis |
| Wallet [0xede2…cf1b](https://etherscan.io/address/0xede263567477d6656595d4a6b2ff4dde0a9cdf1b) | 500M | from 0xaec5, 3 Nov 2026 |
| Wallet [0x6865…98cb](https://etherscan.io/address/0x6865bf9eb5b026688089cf9a9e5a5969503f98cb) | 150M | from 0xfd8e |
| Wallet [0xd392…dd0f](https://etherscan.io/address/0xd392039acf5824cac1b53db50ed34aec7946dd0f) | 124.4M | 125M from Treasury 0xa8f5, 30 Sep 2026 |
| Wallet [0xfa16…9fa8](https://etherscan.io/address/0xfa1662545fdd6e4d1ed05e2300353d2a37959fa8) | 123.5M | from 0xd572 and Safe 0xfb4b |

- Contract names come from Etherscan verified source ("Treasury"). Genesis split: [tx 0x0e87…](https://etherscan.io/tx/0x0e872dc2d03010a92ea0b4cabcbc2c4c81f8efc655b2f1ed6eda44272adbb1fe) (status 1).

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL (not proven)

- I traced 3 hops from the genesis Safe (60 wallets) and found no transfer to an exchange address labelled on Etherscan.
- **Arkham ([Tier B] Arkham, read 16 Nov 2026 (signed-in account)):** the six Treasury contracts ([0xaec5](https://intel.arkm.com/explorer/address/0xaec5157545635a7523efb5abe3a37f52db7de72e), [0xe277](https://intel.arkm.com/explorer/address/0xe277830b3444ea2cfee2b95f780c971222decfa9), [0xfd8e](https://intel.arkm.com/explorer/address/0xfd8e336757ae9cdc0766264064b51492814fcd47), [0xd572](https://intel.arkm.com/explorer/address/0xd572f3a0967856a09054578439ace81b2f2ff88b), [0x914a](https://intel.arkm.com/explorer/address/0x914abadc0e36e03f29e4f1516951125c774dbac8), [0xa8f5](https://intel.arkm.com/explorer/address/0xa8f52ffe4dee9565505f8e390163a335d6a2f708)) are labelled only "Treasury", with no allocation name, and none sends to an exchange. [0xede2](https://intel.arkm.com/explorer/address/0xede263567477d6656595d4a6b2ff4dde0a9cdf1b) still holds the full 500M, with no outflows. [0xd392](https://intel.arkm.com/explorer/address/0xd392039acf5824cac1b53db50ed34aec7946dd0f) (124.4M, from Treasury 0xa8f5) has made only small transfers to Safes. [0x3a96](https://intel.arkm.com/explorer/address/0x3a9624f9bb2dc43e90c0699ddc4a9b6bec147cde) is a verified **ThresholdCustody** contract with no entity label; its many small in/out flows look like deposit custody.
- About 40.3M YELLOW reached the "ThresholdCustody" contract [0x3a96…7cde](https://etherscan.io/address/0x3a9624f9bb2dc43e90c0699ddc4a9b6bec147cde) and a linked wallet. 38.7M of that went in Mar 2026, before any pump data. Only ~123k went on pump days.
- The custody contract's owner is not identified. Because Yellow PRO isn't labelled, sales on the project's own venue can't be seen on-chain. **Not proven → 4.**

## 📊 Tokenomics & supply · 3/10 · ❌ FAIL

- 10.6% stated circulating, with 89% held in Treasury contracts. Releases are at the project's discretion (500M moved on 3 Nov 2026), and the founders' cliff ended in Sep 2026.

## 💧 Liquidity & market · 2/10 · ❌ FAIL

- 99% of volume is on the project's own exchange. The price swung from $0.029 (21 Oct) to $0.162 (26 Oct) to $0.086 now.

## 🧑‍💻 Product & development · 4/10 · ❌ FAIL

- A state-channel clearing network and an SDK were announced. No independent usage data was found [Unverified].

## 🤝 Adoption & customers · 3/10 · ❌ FAIL

- No independent broker or exchange adoption figures found.

## 🛡️ Security & audits · 5/10 · ❌ FAIL

- No exploit found. Treasury and custody contracts are verified on Etherscan. No audit reports were reviewed.

## ⚖️ Regulatory · 5/10 · ❌ FAIL

- No enforcement found. The project runs its own trading venue.

## 📅 Catalysts & calendar · 4/10 · ❌ FAIL

- Founder vesting runs monthly from Sep 2026, and Treasury releases are discretionary.

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | ⚪ Not proven (own venue unlabelled) |
| Live mint path | ⚪ Not proven |
| Entity concentration | 🔴 ~98% in project contracts and the wallets they funded |

## 📚 Sources

- [Tier A] Etherscan token, contract source, balances and transactions; receipts checked 16 Nov 2026
- [Tier A] CoinGecko `yellow` (market data, venue split, daily prices since 13 Apr 2026)
- [Tier B] [Yellow Network site](https://www.yellow.org/), tokenomics page
- [Tier B] Arkham, read 16 Nov 2026 (signed-in account): Treasury contract labels, ThresholdCustody contract, Gnosis Safes 0x56b3 and 0xfb4b (no market-maker label); no exchange counterparties on the treasury side

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| 10B minted to one Safe | [tx 0x2cdd…](https://etherscan.io/tx/0x2cddab0d92286d588a1cb546af71c2f387d449e41d12e4e2af08dd29237b97dd) | A | 16 Nov 2026 |
| Genesis split to Treasuries | [tx 0x0e87…](https://etherscan.io/tx/0x0e872dc2d03010a92ea0b4cabcbc2c4c81f8efc655b2f1ed6eda44272adbb1fe) | A | 16 Nov 2026 |
| 500M Treasury → new wallet, 3 Nov 2026 | [tx 0x0b5f…](https://etherscan.io/tx/0x0b5fec75a7913c21c70f7ecc1a8c10a8ef0ed5a5c9e781ed475497142c6aa199) | A | 16 Nov 2026 |
| 125M Treasury → wallet, 30 Sep 2026 | [tx 0x20bd…](https://etherscan.io/tx/0x20bd83fa70bab3bea9fe0843bdb3a777ac7240aa9cd5f1a6edf1224529cdc1f3) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Owner of ThresholdCustody and of the funded wallets** | Arkham (16 Nov 2026) labels neither. Ask Yellow which bucket each Treasury contract holds and who runs ThresholdCustody [Unverified] | Free |
| 2 | **Which Treasury holds which allocation** | Ask the project for an address map | Free |
| 3 | **Yellow PRO order-book depth and its market makers** | Read the venue's public order book | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.

- Research only. Not investment advice.
