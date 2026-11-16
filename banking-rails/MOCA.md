---
ticker: MOCA
name: Moca Network
chain: ethereum
contract: "0xf944e35f95e819e752f3ccb5faf40957d311e8c5"
overall_score: 3.7
overall_verdict: FAIL
section_scores:
  revenue: 1
  foundation_team: 6
  insider_holdings: 3
  selling_behavior: 6
  tokenomics_supply: 3
  liquidity_market: 3
  product_development: 5
  adoption_customers: 4
  security_audits: 6
  regulatory: 5
  catalysts: 3
gates_failed: [revenue]
red_lines:
  hack_exploit: "none found"
  mint_path_live: "no (fixed 8,888,888,888; token has burn but no mint)"
  team_wallet_to_exchange_during_pump: "none found: no exchange outflow from any traced insider wallet in 365 days; the pump-day high-turnover cluster is Upbit exchange inventory"
  one_hop_sale_status: none_found
  treasury_in_single_key_wallets: "yes, five dormant EOAs hold ~3.71B MOCA (42%); several 1-of-2 Safes"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "No revenue reaches holders."
pump_day_price_source: "Gate MOCA/USDT daily closes"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions: []
price_usd: 0.00602025
price_source: "CoinGecko, 16 Nov 2026 8:34 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### MOCA · Overall grade **3.7 / 10 · ❌ FAIL**

**Summary:** MOCA is the token of Moca Network, Animoca Brands' identity and loyalty chain (AIR Kit, MocaPortfolio staking). Supply is fixed at 8.89B with no mint function. But **only 53.5% circulates, and ~30.9M MOCA unlocks every week, about 34% of the float a year** (DefiLlama unlocks), plus a 125.7M unlock on 11 Dec 2026. There is no fee revenue: DefiLlama tracks Moca Network as a chain with no fees and no TVL. **Five dormant EOAs hold 3.71B MOCA (42% of supply)**, and three treasury Safes need only 1 of 2 signatures. The price is −82.7% in a year and −98.7% from ATH. Revenue trips the hard gate.

**🚨 Top warning:** Dilution, not dumping. ~1.6B MOCA a year is still scheduled to unlock against a $28.6M market cap and $3M of daily volume. 44% of that volume is on Aivora, a little-known exchange. The largest holders are plain EOAs (e.g. [`0x4AB8…E444`](https://etherscan.io/address/0x4AB86fe77f1C3971640E8e91af474eB48843E444) 1.13B, [`0x92A6…3F30`](https://etherscan.io/address/0x92A6623456971161d6fd3dd7F016571578413F30) 1.09B, [`0xdcA7…a858`](https://etherscan.io/address/0xdcA7EEFF29309FC709851658dfD16aEF16dda858) 933M) with no published ownership. Arkham traces their funding to labelled Mocaverse wallets (a Mocaverse Safe, the Strategic Partner multisig and the Network Incentives Fund).

**Sections passed: 3 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 1/10 | ❌ FAIL |
| 🏛️ Foundation & team | 6/10 | ✅ PASS |
| 🪙 Foundation / team holdings | 3/10 | ❌ FAIL |
| 📉 Selling behavior | 6/10 | ✅ PASS |
| 📊 Tokenomics & supply | 3/10 | ❌ FAIL |
| 💧 Liquidity & market | 3/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 5/10 | ❌ FAIL |
| 🤝 Adoption & customers | 4/10 | ❌ FAIL |
| 🛡️ Security & audits | 6/10 | ✅ PASS |
| ⚖️ Regulatory | 5/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 3/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 MOCA · Moca Network · 3.7 / 10 · ❌ FAIL

> **One line:** Backed by a big studio, but no revenue, a third of the float unlocking every year, and concentrated single-key holdings.

| 📊 Market (CoinGecko, 16 Nov 2026 8:34 AM MST) | 🔗 On-chain (Ethereum, 16 Nov 2026) |
|---|---|
| **Price** $0.00602 · 24h / 7d / 30d 🔴 −1.8% / −18.0% / −30.9% · 1y −82.7% | **ERC-20** [`0xf944…e8c5`](https://etherscan.io/address/0xf944e35f95e819e752f3ccb5faf40957d311e8c5) · 8,888,888,888 supply · 10,779 holders |
| **Market cap** $28.6M · **FDV** $53.5M · rank #604 | **Circulating** 4.75B (53.5%) |
| **24h volume** $3.05M: Aivora $1.34M (44%), HTX $1.14M, Upbit $0.19M | **Staking** `SimpleStaking` holds 212.3M |
| **ATH** $0.4774 (24 Dec 2024) · now −98.7% | **Base** bridge adapter holds 128.1M |

---

## 💰 Revenue — Does it make money? · 1/10 · ❌ FAIL

- DefiLlama lists Moca Network (Chain) with no fees, revenue or TVL [Tier A].
- No buyback (Tokenomist buyback page shows none, Tier B). Staking rewards come in partner tokens (e.g. 2.195M ME via MocaPortfolio, [Moca blog](https://moca.network/blog/mocaportfolio-live-2195000-me-allocated-to-moca-stakers/)), not from MOCA revenue.

**What it means:** no revenue. **1 (hard gate).**

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** No revenue reaches holders.

## 🏛️ Foundation & team — Who is in charge? · 6/10 · ✅ PASS

- The Moca Foundation is backed by Animoca Brands; there is a public product line (AIR Kit, MocaPortfolio) [Tier A project site].
- The token contract is immutable: no owner, no mint, no proxy (verified `MocaToken` ABI).

## 🪙 Foundation / team holdings — How many coins do they hold? · 3/10 · ❌ FAIL

| Wallet | MOCA | % of supply | Control | Activity |
|---|---:|---:|---|---|
| [`0x4AB8…E444`](https://etherscan.io/address/0x4AB86fe77f1C3971640E8e91af474eB48843E444) | 1,133.33M | 12.7% | EOA | No outflow in 365d |
| [`0x92A6…3F30`](https://etherscan.io/address/0x92A6623456971161d6fd3dd7F016571578413F30) | 1,091.36M | 12.3% | EOA | No outflow in 365d |
| [`0xdcA7…a858`](https://etherscan.io/address/0xdcA7EEFF29309FC709851658dfD16aEF16dda858) | 933.33M | 10.5% | EOA | No outflow in 365d |
| [`0x0C94…4Fb7`](https://etherscan.io/address/0x0C94Ae6BaeD9a17cdb37DA8E291aF9740f924Fb7) ([Arkham: Mocaverse Team MultiSig](https://intel.arkm.com/explorer/address/0x0C94Ae6BaeD9a17cdb37DA8E291aF9740f924Fb7)) | 711.11M | 8.0% | Safe 2-of-3 | Monthly releases to a 1-of-2 Safe |
| [`0xda01…4e1F`](https://etherscan.io/address/0xda01561cd0F9d656A416994747f86Bb62Bbc4e1F) | 664.04M | 7.5% | Safe 1-of-2 | Sent 356M to the EOA below |
| [`0xbfB2…9B95`](https://etherscan.io/address/0xbfB280fB9663ddE8C65C808d009c07c72F4f9B95) | 356.00M | 4.0% | EOA | Dormant |
| [`0x80F6…eEdb`](https://etherscan.io/address/0x80F67aB0759df2eb02fFF6a51d8Ed611083DeEdb) | 355.56M | 4.0% | Safe 1-of-2 | Receives monthly releases |
| [`0x8Ca3…E672`](https://etherscan.io/address/0x8Ca3c5990BadA51BD41D31c43d4375bA911eE672) | 345.68M | 3.9% | Safe 1-of-2 | Receives monthly releases |

*Balances: Blockscout holders API; Safe thresholds from `getThreshold` / `getOwners`, 16 Nov 2026.* [`0xD965…81b7`](https://etherscan.io/address/0xD965266D814e3DB76445e4f5f3cCb488Dba881b7) (975M) is an [Upbit Cold Wallet](https://intel.arkm.com/explorer/address/0xD965266D814e3DB76445e4f5f3cCb488Dba881b7) (exchange), not counted as insider.

- **Arkham ([Tier B] Arkham, read 16 Nov 2026 (signed-in account)):** the dormant EOAs were funded by labelled Mocaverse wallets: [0x4AB8](https://intel.arkm.com/explorer/address/0x4AB86fe77f1C3971640E8e91af474eB48843E444) by a Mocaverse Gnosis Safe, [0x92A6](https://intel.arkm.com/explorer/address/0x92A6623456971161d6fd3dd7F016571578413F30) by the MOCA Strategic Partner MultiSig, and [0xdcA7](https://intel.arkm.com/explorer/address/0xdcA7EEFF29309FC709851658dfD16aEF16dda858) by the Mocaverse Network Incentives Fund. [0xbfB2](https://intel.arkm.com/explorer/address/0xbfB280fB9663ddE8C65C808d009c07c72F4f9B95) got its gas from an Animoca Brands wallet. So these are allocation wallets, still on single keys. Holdings stays **3**.

## 📉 Selling behavior — Do insiders sell into pumps? · 6/10 · ✅ PASS

*Gate MOCA/USDT daily closes (UTC): 17 pump days in the last 365.*

- **Insider Safes:** the 2-of-3 Safes pay fixed monthly tranches (35.56M and 34.57M) into 1-of-2 Safes on the 11th. One tranche fell on the 11 May 2026 pump day ([tx](https://etherscan.io/tx/0xc8bd5fb13e57bb9e9abc9803b2d27ca02b82b1bdbaacc8bda0f1e4bd81fdd227)). That is a scheduled Safe-to-Safe release, not an exchange deposit.
- **Dormant EOAs:** no outflows in 365 days.
- **High-turnover cluster:** [`0xD965…81b7`](https://etherscan.io/address/0xD965266D814e3DB76445e4f5f3cCb488Dba881b7) and [`0x64f4…81c6`](https://etherscan.io/address/0x64f4861d2a60947146c0e487f965656cf23a81c6) (2,613 transactions) shuttle hundreds of millions of MOCA between each other and two other wallets, including [75M MOCA](https://etherscan.io/tx/0x848bc5d5d76c6a028ebc69332a97999426c8d34010cb0e5206234b36c2ca4934) and [32M MOCA](https://etherscan.io/tx/0xf23e4e5a3919246085b1929b4a7dc7657878b2157843c6de26e424f83ba92395) on the 21 Aug 2026 pump day. **Correction:** Arkham labels [0xD965](https://intel.arkm.com/explorer/address/0xD965266D814e3DB76445e4f5f3cCb488Dba881b7) an **Upbit Cold Wallet** and [0x64f4](https://intel.arkm.com/explorer/address/0x64f4861d2a60947146c0e487f965656cf23a81c6) an **Upbit Hot Wallet** (the other two wallets, `0x6e6e` and `0xbc9a`, appear as Upbit hot wallets on Arkham). The 21 Aug 2026 movements are Upbit moving its own inventory between hot and cold wallets, not team selling.
- **Other insider exits (Etherscan, 365 days):** the two receiving 1-of-2 Safes, the three dormant EOAs and `0xbfB2` sent nothing. The 1-of-2 Safe `0xda01` sent [84M MOCA to `0x2029…ff66` on 28 Jul 2026](https://etherscan.io/tx/0x8a275de46bea3526259ddc2c2b20ad449f60f74d4c6f9cea31fd8b267dc1e5d3) (−7.1%, not a pump day), and that wallet still holds it.

**What it means:** the high-turnover cluster is an exchange, and no traced insider wallet sent MOCA to an exchange in 365 days. Releases are Safe-to-Safe. **6** (was 5).

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from Gate MOCA/USDT daily closes.

## 📊 Tokenomics & supply · 3/10 · ❌ FAIL

- Fixed 8,888,888,888 MOCA; burn only.
- ~30.89M MOCA unlocks a week (team, launch contributors / advisors, strategic partners), **≈34% of circulating a year**. Next discrete unlock: 125.68M on 11 Dec 2026 [Tier B ×2] ([DefiLlama unlocks](https://defillama.com/unlocks/moca-network) · [Blockworks](https://app.blockworks.com/projects/mocaverse/token-unlocks)).

## 💧 Liquidity & market · 3/10 · ❌ FAIL

- $3.05M of 24h volume on a $28.6M cap. The top venue is Aivora (44%); HTX 37%; Upbit KRW small.
- −98.7% from ATH.

## 🧑‍💻 Product & development · 5/10 · ❌ FAIL

- AIR Kit identity SDK, MocaPortfolio staking and Moca Chain [Tier A project blog]. No fee-generating on-chain activity visible on DefiLlama.

## 🤝 Adoption & customers · 4/10 · ❌ FAIL

- 10,779 Ethereum holders; 212M MOCA in the staking contract. No usage metrics verified.

## 🛡️ Security & audits · 6/10 · ✅ PASS

- No exploit found. The token is immutable with no owner. Several large treasuries sit behind 1-of-2 Safes, which is weak key hygiene.

## ⚖️ Regulatory · 5/10 · ❌ FAIL

- No enforcement found. Animoca Brands is a regulated-market-adjacent group; nothing specific to MOCA.

## 📅 Catalysts & calendar · 3/10 · ❌ FAIL

| Date | Event |
|---|---|
| Weekly | ~30.89M MOCA unlock |
| 11 Dec 2026 | 125.68M unlock (partners, team, advisors) |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | 🟢 None found (scheduled Safe releases only) |
| Live mint path | 🟢 None |
| Treasury in single-key wallets | 🔴 ~3.71B in 5 EOAs; 1-of-2 Safes |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| Pump-day high-turnover cluster | Exchange (Upbit) | Etherscan + Arkham | high | yes | None: exchange, not insider |

## 📚 Sources

- [Tier A] Methodology update 16 Nov 2026: no new Arkham lookups; the attribution table uses evidence already cited in this report.
- [Tier A] Blockscout holders / verified source; Etherscan v2 transfers; Ethereum RPC Safe reads, 16 Nov 2026 ~11:45 AM MST
- [Tier A] DefiLlama `moca-network` (no fees / TVL); [Moca blog](https://moca.network/blog/mocaportfolio-live-2195000-me-allocated-to-moca-stakers/)
- [Tier B] [DefiLlama unlocks](https://defillama.com/unlocks/moca-network) · [Blockworks unlocks](https://app.blockworks.com/projects/mocaverse/token-unlocks) · [Tokenomist buyback](https://tokenomist.ai/mocaverse/buyback)
- [Tier A] CoinGecko `mocaverse` (16 Nov 2026 8:34 AM MST); Gate MOCA/USDT daily candles
- [Tier B] Arkham, read 16 Nov 2026 (signed-in account): Upbit Cold and Hot Wallet labels; Mocaverse Team MultiSig; Mocaverse Gnosis Safe, Strategic Partner MultiSig and Network Incentives Fund as funders of the dormant EOAs

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Scheduled Safe release on a pump day | [tx](https://etherscan.io/tx/0xc8bd5fb13e57bb9e9abc9803b2d27ca02b82b1bdbaacc8bda0f1e4bd81fdd227) | A | 16 Nov 2026 |
| Upbit cold → hot wallet 75M on a pump day (exchange inventory) | [tx](https://etherscan.io/tx/0x848bc5d5d76c6a028ebc69332a97999426c8d34010cb0e5206234b36c2ca4934) | A | 16 Nov 2026 |
| Top EOAs dormant | [0x4AB8…E444](https://etherscan.io/address/0x4AB86fe77f1C3971640E8e91af474eB48843E444) · [0x92A6…3F30](https://etherscan.io/address/0x92A6623456971161d6fd3dd7F016571578413F30) | A | 16 Nov 2026 |
| ~34% of float unlocks a year | [DefiLlama](https://defillama.com/unlocks/moca-network) · [Blockworks](https://app.blockworks.com/projects/mocaverse/token-unlocks) | B ×2 | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Who controls the 1-of-2 Safes and `0x2029…ff66`** | Arkham (16 Nov 2026) labels the funders, not the holders. Ask Moca Foundation for its signer and allocation disclosures [Unverified] | Free |
| 2 | **Watch the 213M release of 12 Nov 2026** | Track `0x80F6…eEdb` for exchange deposits on pump days | Free |
| 3 | **Who owns the dormant EOAs** | Match the 1.13B / 1.09B / 933M wallets to allocation buckets | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
