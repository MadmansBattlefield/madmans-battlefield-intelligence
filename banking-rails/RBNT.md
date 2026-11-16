---
ticker: RBNT
name: Redbelly Network
chain: redbelly
contract: "native RBNT on Redbelly (chain 151); bridged ERC-20 on Ethereum"
overall_score: 3.5
overall_verdict: FAIL
section_scores:
  revenue: 2
  foundation_team: 5
  insider_holdings: 2
  selling_behavior: 4
  tokenomics_supply: 3
  liquidity_market: 3
  product_development: 5
  adoption_customers: 3
  security_audits: 6
  regulatory: 6
  catalysts: 3
gates_failed: [revenue]
red_lines:
  hack_exploit: "none found"
  mint_path_live: "no new mint; 3.02B of 10B circulating, ~48M a month unlocking to ecosystem"
  team_wallet_to_exchange_during_pump: "uncertain: the genesis distribution wallet sent 29,999,900 RBNT to an intermediate wallet on 15 May 2026 (+40.7% day), which deposited 25,499,000 RBNT (~$121k) to a Gate deposit address an hour later"
  entity_concentration: "two Safes hold 2.29B and 2.0B RBNT (~43% of supply)"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "No fee, burn or buyback reaches RBNT holders."
pump_day_price_source: "MEXC RBNT-USDT UTC daily closes"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions:
  - address: "0x970ce12dd52c1c721118ec1d344fcb6eb1e12fdc"
    label: "Unlabelled (Across first funder; contract deployer; Gate withdrawals)"
    confidence: low
    independent_corroboration: false
    basis: "Arkham (Ethereum profile only)"
price_usd: 0.00214199
price_source: "CoinGecko, 16 Nov 2026 ~11:30 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### RBNT · Overall grade **3.5 / 10 · ❌ FAIL**

**Summary:** Redbelly is an Australian layer 1 built for compliant asset tokenisation. It came out of a joint venture with CSIRO and the University of Sydney. Only 3.0B of its 10B RBNT circulates, and two multisig Safes hold about 4.3B. No fee capture for holders is published. On a +40.7% day in May 2026, the wallet that distributed the genesis supply sent 30M RBNT to an intermediate wallet, which put 25.5M on Gate within the hour. RBNT is down 99.6% from its December 2024 peak. The revenue gate fails.

**🚨 Top warning:** **treasury-funded Gate deposit on a pump day.** The genesis distribution wallet `0x415c…3c9f` received the 9.99B RBNT genesis supply and funded the DAO's `rbnt.eth`. On **15 May 2026** at 04:42 UTC it sent **29,999,900 RBNT** to `0x970c…2fdc`. At 05:41 UTC that wallet sent **25,499,000 RBNT (~$121k)** to `0xb140…89b4`, a deposit address that forwards to a wallet Etherscan labels as Gate. Both transfers succeeded. Gate closed that day **+40.7%** on five days earlier. **Alternative:** `0x970c…` may be a market maker or OTC buyer funded by the treasury rather than the company itself, so the attribution is [Unverified]. Every link is in the 🔗 Evidence trail below.

**Sections passed: 2 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 2/10 | ❌ FAIL (hard gate) |
| 🏛️ Foundation & team | 5/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 2/10 | ❌ FAIL |
| 📉 Selling behavior | 4/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 3/10 | ❌ FAIL |
| 💧 Liquidity & market | 3/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 5/10 | ❌ FAIL |
| 🤝 Adoption & customers | 3/10 | ❌ FAIL |
| 🛡️ Security & audits | 6/10 | ✅ PASS |
| ⚖️ Regulatory | 6/10 | ✅ PASS |
| 📅 Catalysts & calendar | 3/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 RBNT · Redbelly Network · 3.5 / 10 · ❌ FAIL

> **One line:** A compliance-focused L1 with 70% of supply still held back and a treasury-funded pump-day exchange deposit.

| 📊 Market (CoinGecko, 16 Nov 2026 ~11:30 AM MST) | 🔗 Chain (Routescan, Redbelly) |
|---|---|
| **Price** $0.00214 | **Supply** 3.02B circulating of 10B |
| **24h / 7d / 30d** 🔴 −0.5% / 🟢 +7.7% / 🟢 +18.9% | **Top Safes** `0xc5c1…879d` 2.29B, `0x7473…c16d` 2.0B |
| **Market cap** $6.47M · **FDV** $21.4M | **Wrapped RBNT** 1.73B |
| **24h volume** ~$0.12M (MEXC USDT $58k, MEXC USDC $56k, Gate $4k, Uniswap v4) | **Unlocks** ~48M a month to ecosystem ([terminalnox](https://terminalnox.com/unlocks/RBNT)) |
| **ATH** $0.4836 (25 Dec 2024) · now −99.6% | |
| **Pump days** 34 in the last year (MEXC RBNT-USDT; largest +52.6% on 4 Nov 2026) | |

---

## 💰 Revenue — Does it make money? · 2/10 · ❌ FAIL (hard gate)

- No published fee, burn or buyback that reaches RBNT holders. **2 → hard-gate FAIL.**

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** No fee, burn or buyback reaches RBNT holders.

## 🏛️ Foundation & team — Who is in charge? · 5/10 · ❌ FAIL

- Created in 2021 by Block8, CSIRO and the University of Sydney ([about](https://redbelly.network/about-us)). A community DAO with an RBNT-weighted Snapshot has run since Sep 2025.

## 🪙 Foundation / team holdings — How many coins do they hold? · 2/10 · ❌ FAIL

- The genesis distribution wallet sent the 10B supply to Safes in Nov 2024. Two Safes still hold ~4.3B. Large Safe-to-Safe moves on 9 Dec 2025 and 10 Sep 2026 (500M) aren't explained publicly.

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL

- I traced the genesis distribution wallet and the top ten holders two hops out on Redbelly, for transfers of 5M RBNT or more. In the window, two Gate deposits: **25.5M on 15 May 2026 (+40.7% pump day)**, funded an hour earlier by the genesis distribution wallet ([tx](https://redbelly.routescan.io/tx/0x6c9b0f1830ff6416f2702b7742acf59955efb58ced3e4e0b4e841a7649386000)), and 5.02M on 21 May from a top-holder line (not a pump day). **Uncertain attribution → 4.** **Alternative:** if `0x970c…` is a company wallet, this is a team pump-day sale and Selling drops to 3.
- **Arkham (16 Nov 2026)** has no Redbelly network coverage. The same address on Ethereum, [0x970c…2fdc](https://intel.arkm.com/explorer/address/0x970ce12dd52c1c721118ec1d344fcb6eb1e12fdc), carries no entity label; its only tags are generic (first funded via the Across bridge, contract deployer), and its Ethereum activity is Gate withdrawals and bridge or DEX trades. That fits a trading desk or market maker as well as a company wallet, so the label is low confidence and, under the 16 Nov 2026 rule, cannot move Selling on its own. Selling stays **4 (not proven)**. [Tier B] Arkham, read 16 Nov 2026 (signed-in account).

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from MEXC RBNT-USDT UTC daily closes.

## 📊 Tokenomics & supply · 3/10 · ❌ FAIL

- 7B RBNT still to circulate. Monthly ecosystem unlocks.

## 💧 Liquidity & market · 3/10 · ❌ FAIL

- About $0.12M a day, almost all MEXC.

## 🧑‍💻 Product & development · 5/10 · ❌ FAIL

- Mainnet live since Nov 2024; selected for the RBA's Project Acacia.

## 🤝 Adoption & customers · 3/10 · ❌ FAIL

- Little public usage data.

## 🛡️ Security & audits · 6/10 · ✅ PASS

- No exploit found.

## ⚖️ Regulatory · 6/10 · ✅ PASS

- Australian company focused on compliant issuance. No enforcement found.

## 📅 Catalysts & calendar · 3/10 · ❌ FAIL

- Monthly ecosystem unlocks (next 48.7M on 17 Nov 2026).

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | 🟠 Uncertain: treasury-funded 25.5M Gate deposit on a +40.7% day |
| Live mint path | 🟢 No mint; scheduled unlocks |
| Entity concentration | 🔴 Two Safes hold ~43% of supply |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| [0x970c…2fdc](https://intel.arkm.com/explorer/address/0x970ce12dd52c1c721118ec1d344fcb6eb1e12fdc) | Unlabelled (Across first funder; contract deployer; Gate withdrawals) | Arkham (Ethereum profile only) | low | no | Cannot move Selling alone; stays 4 |
| Genesis distribution wallet `0x415c…3c9f` | Received the genesis supply (on-chain) | Routescan (Redbelly) | high | yes (on-chain) | None alone |

## 📚 Sources

- [Tier B] Arkham, read 16 Nov 2026 (signed-in account): the intermediate wallet 0x970c (Ethereum profile; Arkham does not cover Redbelly)
- [Tier A] [Redbelly about page](https://redbelly.network/about-us), [DAO constitution post](https://medium.com/@redbellyblockchain/redbelly-community-dao-constitution-tl-dr-version-a46979ab1b73)
- [Tier A] Routescan Redbelly explorer and API (balances, transfers, transaction status)
- [Tier B] [terminalnox unlocks](https://terminalnox.com/unlocks/RBNT), [VYLOS unlocks](https://www.vylos.io/unlocks/redbelly-network-token)
- [Tier A] CoinGecko `redbelly-network-token` (market, venues); pump days from MEXC RBNT-USDT daily closes

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Genesis distribution wallet → `0x970c…` 29,999,900 RBNT, 15 May 2026 04:42 UTC | [tx](https://redbelly.routescan.io/tx/0xaff6bb70659885d20399ac3fdf5963933470a6db7932149d158d482fef2ba9c6) | A | 16 Nov 2026 |
| `0x970c…` → Gate deposit 25,499,000 RBNT, 15 May 2026 05:41 UTC | [tx](https://redbelly.routescan.io/tx/0x6c9b0f1830ff6416f2702b7742acf59955efb58ced3e4e0b4e841a7649386000) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Who controls `0x970c…2fdc`** (company, market maker or OTC buyer?) | No public label; Arkham (16 Nov 2026) shows only generic tags on Ethereum. Ask Redbelly | Free |
| 2 | **Who controls the two large Safes** | Not published | Arkham |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.

- Research only. Not investment advice.
