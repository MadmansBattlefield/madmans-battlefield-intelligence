---
ticker: SWFTC
name: SWFTCOIN (SWFT Blockchain)
chain: ethereum
contract: "0x0bb217e40f8a5cb79adf04e1aab60e5abd0dfc1e (Ethereum); 0xe64e30276c2f826febd3784958d6da7b55dfbad3 (BNB Chain)"
overall_score: 3.8
overall_verdict: FAIL
section_scores:
  revenue: 2
  foundation_team: 4
  insider_holdings: 4
  selling_behavior: 4
  tokenomics_supply: 7
  liquidity_market: 4
  product_development: 4
  adoption_customers: 3
  security_audits: 5
  regulatory: 5
  catalysts: 3
gates_failed: [revenue]
red_lines:
  hack_exploit: "none found"
  mint_path_live: "no: 10B fully issued in 2017"
  team_wallet_to_exchange_during_pump: "not proven: an unlabelled wallet two hops from a 2017 genesis recipient (which Arkham labels Aeternity, not SWFT) sent 5M SWFTC (~$28k) to an OKX deposit on 30 Nov 2025 (+14.7%); no team label"
  entity_concentration: "unknown: the 2017 plan allotted 50% to founders, team and development; current team balances not published"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "Swap fees go to the company; no fee share, buyback or verified burn record was found, so revenue does not reach holders."
pump_day_price_source: "KuCoin SWFTC-USDT UTC daily closes"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions:
  - address: "0x29c8e72a92944f4fc8f871e1217dbd3d00cf4054"
    label: "Unlabelled EOA"
    confidence: low
    independent_corroboration: false
    basis: "Arkham"
  - address: "0x73d46e1262ec7a2d21a58da2c379ed63b191c65c"
    label: "OKX Deposit"
    confidence: medium
    independent_corroboration: false
    basis: "Arkham"
  - address: "0x1371e6c4d3797f2182282b9fea41d87bbe767dd5"
    label: "OKX Deposit"
    confidence: medium
    independent_corroboration: false
    basis: "Arkham"
  - address: "0xd9f7404dd006d3f5dc823561711bfc4d54df3d4a"
    label: "Aeternity (not SWFT)"
    confidence: medium
    independent_corroboration: false
    basis: "Arkham"
  - address: "0x38570825d2c35db1b5fc603b1215dcfe1607bfb4"
    label: "Unlabelled (\"High Transacting\")"
    confidence: low
    independent_corroboration: false
    basis: "Arkham"
  - address: "0xadb9ed6e0faf9a08d5a9644e8bdec8d8682e6844"
    label: "Coinbase: Cold Wallet"
    confidence: high
    independent_corroboration: true
    basis: "Arkham; Coinbase funding on-chain"
  - address: "0xe935e29c66e4e01479bb036d1f6dfd9ff5ed2d5a"
    label: "Coinbase: Cold Wallet"
    confidence: high
    independent_corroboration: true
    basis: "Arkham; Coinbase funding on-chain"
  - address: "0x4f41c3a640275b98ca842c639549e900b12ee825"
    label: "\"SWFTC Whale\" tag only"
    confidence: low
    independent_corroboration: false
    basis: "Arkham"
price_usd: 0.00223568
price_source: "CoinGecko, 16 Nov 2026 ~9:45 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### SWFTC · Overall grade **3.8 / 10 · ❌ FAIL**

**Summary:** SWFTC is the fee-discount token of SWFT Blockchain, a cross-chain swap aggregator running since 2017 that now also markets an AI service, SWFTGPT. All 10B tokens were issued in 2017. The 2018 whitepaper gave half to founders, employees and business development. Holders get swap-fee discounts but no fee share, and I found no verified burn record. One wallet traced back to a 2017 genesis recipient sent tokens to OKX on a pump day, but the link to the team is weak. The revenue gate fails.

**🚨 Top warning:** **a dormant 2017-era wallet sold into a pump.** `0x29c8…4054` received 288.5M SWFTC from `0x3857…` in 2017. That wallet had in turn received tokens from `0xd9f7…3d4a`, which got 464M at genesis. After years of near-silence, `0x29c8…4054` sent **5M SWFTC (~$28k) to OKX on 30 Nov 2025**, when the price was 14.7% above five days earlier ([tx](https://etherscan.io/tx/0xb164faf2302dc9aa5803160557cb9cbdff2ea93e3eea544ec7467b74edec38c1), status 1). Whether these wallets are the team's is [Unverified]. Every link is in the 🔗 Evidence trail below.

**Sections passed: 1 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 2/10 | ❌ FAIL (hard gate) |
| 🏛️ Foundation & team | 4/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 4/10 | ❌ FAIL |
| 📉 Selling behavior | 4/10 | ❌ FAIL (not proven) |
| 📊 Tokenomics & supply | 7/10 | ✅ PASS |
| 💧 Liquidity & market | 4/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 4/10 | ❌ FAIL |
| 🤝 Adoption & customers | 3/10 | ❌ FAIL |
| 🛡️ Security & audits | 5/10 | ❌ FAIL |
| ⚖️ Regulatory | 5/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 3/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 SWFTC · SWFTCOIN (SWFT Blockchain) · 3.8 / 10 · ❌ FAIL

> **One line:** A 2017 swap-aggregator token with discounts but no fee share, and opaque team holdings.

| 📊 Market (CoinGecko, 16 Nov 2026 ~9:45 AM MST) | 🔗 Chain (Etherscan) |
|---|---|
| **Price** $0.002236 | **Supply** 10B, fully issued (2017) |
| **24h / 7d / 30d** 🟢 +1.4% / 🔴 −8.0% / 🔴 −22.0% | **Top holders** `0xadb9…6844` 1.25B and six 393.9M wallets, mostly funded from Coinbase; OKX cold wallet 586M |
| **Market cap** $22.4M · **FDV** $22.4M | |
| **24h volume** $0.34M (HTX $89k, Bitunix $70k, Coinbase $47k, Biconomy, KuCoin, OKX, Gate) | |
| **ATH** $0.0467 (31 Jan 2025) · now −95.2% | |
| **Pump days** 28 in the last year (KuCoin SWFTC-USDT; largest +64.6% on 5 Jan 2026) | |

---

## 💰 Revenue — Does it make money? · 2/10 · ❌ FAIL (hard gate)

- SWFT earns swap fees, and paying them in SWFTC gives a discount ([whitepaper](https://www.allcryptowhitepapers.com/wp-content/uploads/2018/05/Swft.pdf)) [Tier B mirror]. No fee share, buyback or verified burn record was found. **2 → hard-gate FAIL.**

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** Swap fees go to the company; no fee share, buyback or verified burn record was found, so revenue does not reach holders.

## 🏛️ Foundation & team — Who is in charge? · 4/10 · ❌ FAIL

- An identifiable company team, but analysts describe development as "maintenance mode" with no public engineering artifacts ([Token Vitals](https://tokenvitals.com/token/swftc)) [Tier B, one source].

## 🪙 Foundation / team holdings — How many coins do they hold? · 4/10 · ❌ FAIL

- The 2018 plan gave 50% to founders, team and development (20% team, 25% business development, 5% research) and 50% to community programmes over four years ([whitepaper](https://www.allcryptowhitepapers.com/wp-content/uploads/2018/05/Swft.pdf)). Current team balances aren't published. The largest unlabelled holders were funded from Coinbase, so they look like custody or customer wallets rather than team wallets. Arkham confirms it: [0xadb9…6844](https://intel.arkm.com/explorer/address/0xadb9ed6e0faf9a08d5a9644e8bdec8d8682e6844) (1.25B SWFTC) and [0xe935…2d5a](https://intel.arkm.com/explorer/address/0xe935e29c66e4e01479bb036d1f6dfd9ff5ed2d5a) (393.9M) are **Coinbase: Cold Wallet**s. [0x4f41…e825](https://intel.arkm.com/explorer/address/0x4f41c3a640275b98ca842c639549e900b12ee825) (491M) carries only a "SWFTC Whale" tag; about five years ago it sent ~500M SWFTC to an address Arkham labels "Swft Blockchain". [Tier B] Arkham, read 16 Nov 2026 (signed-in account).

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL (not proven)

- I traced the genesis recipients and the top 15 holders two hops out, for transfers of 5M SWFTC or more. One hit in the window: `0x29c8…` (two hops from genesis recipient `0xd9f7…`) sent 5M to OKX on a +14.7% day. The link back to the team runs through 2017 transfers and is [Unverified] → **not proven, 4.** **Alternative:** if `0x29c8…` is a team wallet, Selling becomes 3 (gate fails) and the overall becomes 3.7.
- **Arkham (16 Nov 2026):** [0x29c8…4054](https://intel.arkm.com/explorer/address/0x29c8e72a92944f4fc8f871e1217dbd3d00cf4054) is an **unlabelled EOA** (first funder [0x9890…55CB](https://intel.arkm.com/explorer/address/0x9890eD07DB289fa528e776d4920fCCaEb95a55CB); holds 15.0M SWFTC). It confirms both OKX deposits: 5M to OKX Deposit [0x73d4…c65c](https://intel.arkm.com/explorer/address/0x73d46e1262ec7a2d21a58da2c379ed63b191c65c) on 30 Nov 2025 ([tx](https://etherscan.io/tx/0xb164faf2302dc9aa5803160557cb9cbdff2ea93e3eea544ec7467b74edec38c1)) and 3.8M to OKX Deposit [0x1371…7dd5](https://intel.arkm.com/explorer/address/0x1371e6c4d3797f2182282b9fea41d87bbe767dd5) on 26 Jan 2025 ([tx](https://etherscan.io/tx/0xc60ac41709cd17c3d2f14b1637e310f599783be426ee963103de06961bb2021d), outside the window). The 2017 funder [0x3857…bfb4](https://intel.arkm.com/explorer/address/0x38570825d2c35db1b5fc603b1215dcfe1607bfb4) is unlabelled ("High Transacting"), and the genesis recipient [0xd9f7…3d4a](https://intel.arkm.com/explorer/address/0xd9f7404dd006d3f5dc823561711bfc4d54df3d4a) is labelled **Aeternity**, not SWFT. Nothing ties the chain to the SWFT team, so under the 16 Nov 2026 rule the unlabelled link cannot move Selling: it stays **not proven, 4**. [Tier B] Arkham, read 16 Nov 2026 (signed-in account).

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from KuCoin SWFTC-USDT UTC daily closes.

## 📊 Tokenomics & supply · 7/10 · ✅ PASS

- Fully issued, so no unlock overhang.

## 💧 Liquidity & market · 4/10 · ❌ FAIL

- $0.34M a day, but on good venues (Coinbase, OKX, KuCoin, HTX, Gate).

## 🧑‍💻 Product & development · 4/10 · ❌ FAIL

- A cross-chain swap aggregator plus the SWFTGPT AI membership. Many competing aggregators charge zero fees.

## 🤝 Adoption & customers · 3/10 · ❌ FAIL

- No public volume or fee dashboard.

## 🛡️ Security & audits · 5/10 · ❌ FAIL

- No exploit found.

## ⚖️ Regulatory · 5/10 · ❌ FAIL

- 2017 token distribution with no enforcement found. Governance is centralized.

## 📅 Catalysts & calendar · 3/10 · ❌ FAIL

- None dated.

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | ⚪ Not proven: 5M SWFTC to OKX on 30 Nov 2025 from an unlabelled wallet; Arkham shows no team tie |
| Live mint path | 🟢 None |
| Entity concentration | ⚪ Unknown |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| [0x29c8…4054](https://intel.arkm.com/explorer/address/0x29c8e72a92944f4fc8f871e1217dbd3d00cf4054) | Unlabelled EOA | Arkham | low | no | None: Selling stays 4 |
| [0x73d4…c65c](https://intel.arkm.com/explorer/address/0x73d46e1262ec7a2d21a58da2c379ed63b191c65c), [0x1371…7dd5](https://intel.arkm.com/explorer/address/0x1371e6c4d3797f2182282b9fea41d87bbe767dd5) | OKX Deposit | Arkham | medium | no | None |
| [0xd9f7…3d4a](https://intel.arkm.com/explorer/address/0xd9f7404dd006d3f5dc823561711bfc4d54df3d4a) | Aeternity (not SWFT) | Arkham | medium | no | Weakens the team link |
| [0x3857…bfb4](https://intel.arkm.com/explorer/address/0x38570825d2c35db1b5fc603b1215dcfe1607bfb4) | Unlabelled ("High Transacting") | Arkham | low | no | None |
| [0xadb9…6844](https://intel.arkm.com/explorer/address/0xadb9ed6e0faf9a08d5a9644e8bdec8d8682e6844), [0xe935…2d5a](https://intel.arkm.com/explorer/address/0xe935e29c66e4e01479bb036d1f6dfd9ff5ed2d5a) | Coinbase: Cold Wallet | Arkham; Coinbase funding on-chain | high | yes (on-chain Coinbase funding) | Holdings: exchange custody, not team |
| [0x4f41…e825](https://intel.arkm.com/explorer/address/0x4f41c3a640275b98ca842c639549e900b12ee825) | "SWFTC Whale" tag only | Arkham | low | no | None |

## 📚 Sources

- [Tier B] Arkham, read 16 Nov 2026 (signed-in account): the 2017 trail (0xd9f7, 0x3857, 0x29c8), the two OKX deposits and the largest holders (two Coinbase cold wallets and a SWFTC Whale tag); dates from Etherscan
- [Tier B] [SWFT whitepaper (2018 mirror)](https://www.allcryptowhitepapers.com/wp-content/uploads/2018/05/Swft.pdf), [Token Vitals](https://tokenvitals.com/token/swftc)
- [Tier A] Etherscan transfers and holders for `0x0bb2…fc1e`
- [Tier A] CoinGecko `swftcoin` (market, venues); pump days from KuCoin SWFTC-USDT daily closes
- swftblockchain.ai returned a server error on 16 Nov 2026

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| 5M SWFTC → OKX on a pump day | [tx](https://etherscan.io/tx/0xb164faf2302dc9aa5803160557cb9cbdff2ea93e3eea544ec7467b74edec38c1) | A | 16 Nov 2026 |
| 2018 allocation | [whitepaper mirror](https://www.allcryptowhitepapers.com/wp-content/uploads/2018/05/Swft.pdf) | B | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Is `0x29c8…4054` a team wallet?** | Arkham (16 Nov 2026): unlabelled, and the genesis recipient is labelled Aeternity. Ask SWFT to publish its team and treasury wallets | Free |
| 2 | **Fee and burn figures** | Ask SWFT; official site was down | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.

- Research only. Not investment advice.
