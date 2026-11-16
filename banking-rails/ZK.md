---
ticker: ZK
name: ZKsync
chain: zksync-era
contract: "0x5a7d6b2f92c77fad6ccabd7ee0624e64907eaf3e"
overall_score: 3.5
overall_verdict: FAIL
section_scores:
  revenue: 2
  foundation_team: 6
  insider_holdings: 4
  selling_behavior: 0
  tokenomics_supply: 4
  liquidity_market: 6
  product_development: 6
  adoption_customers: 3
  security_audits: 4
  regulatory: 6
  catalysts: 3
gates_failed: [revenue, selling_behavior]
red_lines:
  hack_exploit: "yes: 13 Apr 2025 a compromised 1-of-1 admin key minted 111.9M unclaimed airdrop ZK (~$5M); 90% returned 23 Apr 2025"
  mint_path_live: "yes: 15.50B of the 21B cap minted; the docs say supply can be raised by a protocol governance upgrade; capped minters keep minting"
  team_wallet_to_exchange_during_pump: "yes: a Foundation-linked wallet sent 44.7M ZK to a Binance deposit on a +18.3% day (25 Apr 2025); a wallet funded weekly by Foundation Treasury 2 sent 252.2M ZK (~$14.7M) to a Binance deposit, 53.8M of it on pump days incl. 4-6 Nov 2025 (+117% to +161%)"
  one_hop_sale_status: proven
  treasury_selling: "Foundation has minted its whole 4.18B ecosystem allocation; no wallet-level treasury report published"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "Sequencer revenue is tiny and none goes to ZK."
pump_day_price_source: "Gate ZK_USDT UTC daily closes, re-run 16 Nov 2026 with scripts/pump_day_test.py (40 of 360 days); the body's earlier count used the daily closes cited in the body"
pump_day_disclosure_quality: silence
pump_day_undisclosed_penalty_applied: true
dual_review: not_run
attributions: []
price_usd: 0.00788
price_source: "CoinGecko, 16 Nov 2026 6:58 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### ZK · Overall grade **3.5 / 10 · ❌ FAIL**

**Summary:** ZKsync is an Ethereum layer-2 (ZKsync Era plus other ZK Stack chains). ZK is a governance token with **no claim on revenue**: DefiLlama counts $322k of chain revenue in 12 months and none for holders. The token is −85% in a year and −97.5% from its high. **15.5B of 21B ZK is already minted**, and investor and team tokens (7.0B) unlock monthly until mid-2028. On-chain, wallets funded by the **ZKsync Foundation's own treasury multisigs** put about **297M ZK into Binance deposit addresses**, much of it on pump days. Both hard gates fail.

**🚨 Top warning:** [ZKsync Foundation Treasury 2 `0xea81…7619`](https://explorer.zksync.io/address/0xea81e12b73696599fdc8ba407e858d7163977619) paid ~20M ZK a week to [`0x1091…0732`](https://explorer.zksync.io/address/0x1091d81f562f5c3df9cb56a823c135a860080732). That wallet forwarded **252.2M ZK (~$14.7M)** in 29 transfers to the Binance deposit [`0x78b5…94c9`](https://explorer.zksync.io/address/0x78b5e3b3b4366f2a981d337d0c4c946233c094c9). During the November 2025 spike the Foundation sent [14.2M on 4 Nov](https://explorer.zksync.io/tx/0x79b1de2d204ffb3a5ee2a3beccbe849b8448c6df37df22a015cde0af834f5555) and [20.4M on 5 Nov](https://explorer.zksync.io/tx/0x4d1c200ab948d41ac6697f44f54556f4777acc588bd4295af16c5b315f4fcb8e), and the wallet deposited [8.0M (4 Nov, +117%)](https://explorer.zksync.io/tx/0xee3bd5d3729ec710e84500c7ebd7f0b4904e22c0c74e8b68473d044ad6ffdfce), [6.2M (5 Nov, +161%)](https://explorer.zksync.io/tx/0x2c7f9f3367a34bf0c23e4489bbe75d6597d5c4dd8cc61c1a8ce5590a2eafdc10) and [16.4M (6 Nov)](https://explorer.zksync.io/tx/0xe959ad22e1497492a89aae65b98e8e618db733e27d5e83ff61bf58e3fed46ed2) to Binance. A second Foundation-linked wallet sent [44.7M ZK to Binance on a +18.3% day](https://explorer.zksync.io/tx/0xae62d1cd8a8d6434e04de6cd3f01be2e9503e35c39e8a87174a7663a20c19a75) (25 Apr 2025). Every link is in the 🔗 Evidence trail below.

**Sections passed: 4 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 2/10 | ❌ FAIL (hard gate) |
| 🏛️ Foundation & team | 6/10 | ✅ PASS |
| 🪙 Foundation / team holdings | 4/10 | ❌ FAIL |
| 📉 Selling behavior | 0/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 4/10 | ❌ FAIL |
| 💧 Liquidity & market | 6/10 | ✅ PASS |
| 🧑‍💻 Product & development | 6/10 | ✅ PASS |
| 🤝 Adoption & customers | 3/10 | ❌ FAIL |
| 🛡️ Security & audits | 4/10 | ❌ FAIL |
| ⚖️ Regulatory | 6/10 | ✅ PASS |
| 📅 Catalysts & calendar | 3/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 ZK · ZKsync · 3.5 / 10 · ❌ FAIL

> **One line:** A well-built L2 governance system around a token with no revenue, heavy ongoing unlocks, and a Foundation treasury whose ZK keeps reaching Binance through funded wallets, including on spike days.

| 📊 Market (CoinGecko, 16 Nov 2026 6:58 AM MST) | 🔗 On-chain (ZKsync Era, 16 Nov 2026) |
|---|---|
| **Price** $0.00788 | **Contract** [`0x5A7d…f3E`](https://explorer.zksync.io/address/0x5a7d6b2f92c77fad6ccabd7ee0624e64907eaf3e) |
| **24h / 7d / 30d** 🔴 −2.3% / −13.2% / −49.8% · 1y −85.2% | **`totalSupply()`** 15,503,229,713 ZK (cap 21B) |
| **Market cap** $86.8M · **FDV** $165.4M | **Foundation capped minters** [`0xd78d…8405`](https://explorer.zksync.io/address/0xd78dc27d4db8f428c67f542216a2b23663838405) 3.489B/3.489B minted · [`0x00d3…6382`](https://explorer.zksync.io/address/0x00d3dc9676572d04665a64ee72a78cf0358f6382) 0.69B minted |
| **24h volume** $5.9M (Binance $1.12M, WhiteBIT, BTCC, Bybit, OKX) | **Matter Labs allocation minter** (investors + team) [`0xa97f…f7e6`](https://explorer.zksync.io/address/0xa97fbc75ccbc7d4353c4d2676ed18cd0c5aaf7e6) 7.0B/7.0B minted |
| **ATH** $0.321 (16 Jun 2024) · now −97.5% | **Circulating (CoinGecko)** 11.02B |
| **Pump days, last 365 days** 41 (Binance ZKUSDT closes) | **TVL** $10.9M (DefiLlama, ZKsync Era) |

---

## 💰 Revenue — Does it make money? · 2/10 · ❌ FAIL (hard gate)

| Metric | Value | Source |
|---|---:|---|
| Chain fees, last 12 months | **$350,537** (30 days: $10,740) | [Tier A] [DefiLlama fees, `zksync-era`](https://api.llama.fi/summary/fees/zksync-era?dataType=dailyFees) |
| Chain revenue, last 12 months | **$322,083** (30 days: $10,298) | [Tier A] [DefiLlama revenue](https://api.llama.fi/summary/fees/zksync-era?dataType=dailyRevenue) |
| To ZK holders | **None** (no holders-revenue series) | [Tier A] [ZK token docs](https://docs.zknation.io/zk-token/zk-token): ZK is a governance token |

**What it means:** Sequencer revenue is tiny against an $87M cap, and none of it goes to ZK. **2 → hard-gate FAIL.**

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** Sequencer revenue is tiny and none goes to ZK.

## 🏛️ Foundation & team — Who is in charge? · 6/10 · ✅ PASS

| Item | Finding | Source |
|---|---|---|
| Entities | **ZKsync Foundation** (Cayman) runs ecosystem funds. **ZKsync Association** (Austrian Verein) set up governance and ran the airdrop. **Matter Labs** is the developer | [Tier A] [Governance procedures](https://docs.zknation.io/zksync-governance-procedures/zksync-governance-procedures-overview) |
| Governance | Three governors (Protocol, Token, GovOps) with timelocks on Era; 12-seat Security Council (9-of-12 floor); Guardians | [Tier A] [Contract addresses](https://docs.zknation.io/zk-nation/zksync-governance-contract-addresses) |
| Foundation multisig (L1) | [`0xbC16…B51c`](https://etherscan.io/address/0xbc1653bd3829dfec575afc3816d4899cd103b51c) | [Tier A] same docs |
| Foundation treasuries (Era) | [Treasury 1 `0xc853…9da4`](https://explorer.zksync.io/address/0xc8538a03282eae418237264a3957070efa679da4) and [Treasury 2 `0xea81…7619`](https://explorer.zksync.io/address/0xea81e12b73696599fdc8ba407e858d7163977619), both 3-of-5 | [Tier B] [Blockworks transparency filing](https://blockworks.com/token-transparency/filing/zksync) + on-chain flows below |

**What it means:** The governance design is one of the most structured among L2s. The weak spot is that the Foundation has not published a wallet-level treasury report, although the community asked for one in [the forum](https://forum.zknation.io/t/zksync-foundation-treasury-report/856). **6.**

## 🪙 Foundation / team holdings — How many coins do they hold? · 4/10 · ❌ FAIL

| Allocation (docs) | ZK | Status on-chain |
|---|---:|---|
| Token Assembly | 6.146B (29.3%) | Unminted; released only through Token Program Proposals (~183M minted by Oct 2025 per a [forum post](https://forum.zknation.io/t/serious-concerns-about-treasury-spending-transparency-and-the-direction-of-the-zksync-ecosystem/932)) |
| Ecosystem (Foundation) | 4.179B (19.9%) | **Fully minted** (3.489B + 0.690B on the two Foundation minters, read via `minted()`) |
| Investors | 4.155B (19.8%) | Minted (7.0B together with team) to vesting; 1-year cliff from Jun 2024, then 3 years |
| Team (Matter Labs) | 2.845B (13.6%) | Same |
| Airdrop | 3.675B (17.5%) | Claimed or swept |

- The Foundation minter route runs through contract [`0x1054…86d9`](https://explorer.zksync.io/address/0x1054cb76ff7d77c387c82d1e0afc374fd0ca86d9) (2.884B ZK minted to it). It paid out to Treasury 1 (600M), [`0xe640…5D2B`](https://explorer.zksync.io/address/0xe64004d545c8deef9c83ae712878c5db50515d2b) (547M), [`0x6240…cc1f`](https://explorer.zksync.io/address/0x62404c448436405acb0e0b8f0f4f557022c9cc1f) (525M), [`0xd0b2…b252`](https://explorer.zksync.io/address/0xd0b23d3c71a66242891577ca7863750ef979b252) (400M), [`0xc3c1…4D3`](https://explorer.zksync.io/address/0xc3c12eeed5fabc6eadae50ba4253b52d7a0044d3) (352M) and [`0x8d61…93a1`](https://explorer.zksync.io/address/0x8d617d5e76567a96aefd2865cc22a6fca6fe93a1) (350M, still held).
- `0xe640…` is Foundation-linked: it sent [200M back to Treasury 1](https://explorer.zksync.io/address/0xc8538a03282eae418237264a3957070efa679da4) and received 189M from it. Treasury 1 now holds 0 and Treasury 2 holds 200k.

**What it means:** The Foundation has already minted and moved its whole allocation through a web of wallets. Its current holdings and spending are not reported. **4.**

## 📉 Selling behavior — Do insiders sell into pumps? · 0/10 · ❌ FAIL

Pump days come from Binance ZKUSDT closes. Exchange tags are Etherscan's Ethereum labels for the same addresses (exchange deposit addresses are the same across EVM chains), confirmed here by each deposit sweeping to the tagged hot wallet "Binance 83" [`0x7aed…7d76`](https://explorer.zksync.io/address/0x7aed074ca56f5050d5a2e512ecc5bf7103937d76).

| Date | From | To | ZK | Pump day? | Tx |
|---|---|---|---:|:---:|---|
| 25 Apr 2025 | `0xe640…` (Foundation-linked) | Binance deposit `0x2b60…114e` | 44,682,742 | **Yes, +18.3%** | [tx](https://explorer.zksync.io/tx/0xae62d1cd8a8d6434e04de6cd3f01be2e9503e35c39e8a87174a7663a20c19a75) |
| 29 Apr – 20 Nov 2025 | `0x1091…` (funded by Treasury 2 and `0xe640…`) | Binance deposit `0x78b5…94c9` | **252,241,483** in 29 tx (≈ $14.7M at the day's price) | **6 tx / 53.8M on pump days** | see below |
| 2 Nov 2025 | `0x1091…` | Binance deposit | 10,430,344 | **Yes, +94.7%** | [tx](https://explorer.zksync.io/tx/0x76346895dbc31785a55d5e2976cfee8febae76dd3aad7224a4fb3bcc067c3227) |
| 4 Nov 2025 | `0x1091…` | Binance deposit | 8,000,000 | **Yes, +117.2%** | [tx](https://explorer.zksync.io/tx/0xee3bd5d3729ec710e84500c7ebd7f0b4904e22c0c74e8b68473d044ad6ffdfce) |
| 5 Nov 2025 | `0x1091…` | Binance deposit | 6,215,562 | **Yes, +161.4%** | [tx](https://explorer.zksync.io/tx/0x2c7f9f3367a34bf0c23e4489bbe75d6597d5c4dd8cc61c1a8ce5590a2eafdc10) |
| 6 Nov 2025 | `0x1091…` | Binance deposit | 16,396,521 | **Yes, +34.2%** | [tx](https://explorer.zksync.io/tx/0xe959ad22e1497492a89aae65b98e8e618db733e27d5e83ff61bf58e3fed46ed2) |

- `0x1091…` is an EOA. Treasury 2 funded it ~20M ZK at a time, about weekly, from Jun to Nov 2025 (247.6M), and it sent almost everything on to Binance. It may be a contractor, market maker or OTC buyer paid by the Foundation; its identity is [Unverified]. Either way, a Foundation treasury funded the wallet that sold, including on spike days, and no disclosure of these sales was found.
- Wallet `0xc3c1…`, funded with 352M by the Foundation route, also **received** ZK from Wintermute (8.7M, Sep 2024) and Bybit's hot wallet (3.5M). That points to market-making or OTC activity [Unverified].

**What it means:** A Foundation-funded pipeline into Binance sold on the biggest pump days of the past year. Per the rules this is a hard-gate fail. **2.**

- **Disclosure quality (16 Nov 2026 rules): silence.** No disclosure of these sales was found. **Penalty applied (16 Nov 2026 rules):** a proven pump-day sale with no disclosure fails Selling (ordinary score at most 3) and then loses 2 points, floored at 0: **2 → 0**. 4–6 Nov 2025 are pump days on Gate prices (+34% to +161%). Pump days from Gate ZK_USDT UTC daily closes, re-run 16 Nov 2026 with scripts/pump_day_test.py (40 of 360 days); the body's earlier count used the daily closes cited in the body.

- **One-hop amendment (16 Nov 2026):** Still a **proven sale** under the amended rule. (c) holds: no Foundation post or governance item explaining the Binance pipeline was found; the receiver's identity is [Unverified]. Silence stands, so the penalty above is unchanged.

## 📊 Tokenomics & supply · 4/10 · ❌ FAIL

- 15.50B minted of a 21B cap. The docs state "token supply can be increased through a protocol governance upgrade" ([ZK token docs](https://docs.zknation.io/zk-token/zk-token)).
- Investor and team tokens (7.0B, 33% of supply) unlock monthly from June 2025 for three years, and Token Assembly programs mint more (e.g. the 2026 Protocol & Network Development allocation of 804M).

## 💧 Liquidity & market · 6/10 · ✅ PASS

- $5.9M of 24h volume on an $87M cap (~6.8%), with Binance, Bybit and OKX among the venues (CoinGecko, 16 Nov 2026 6:58 AM MST). Price −49.8% in 30 days.

## 🧑‍💻 Product & development · 6/10 · ✅ PASS

- ZKsync Era and the ZK Stack (Abstract, Lens and other chains) run on a shared protocol governed on-chain ([governance 101](https://docs.zknation.io/voting-and-delegation/zksync-governance-101)). Development is active.

## 🤝 Adoption & customers · 3/10 · ❌ FAIL

- ZKsync Era TVL is **$10.9M** and 30-day chain fees are $10.7k (DefiLlama, 16 Nov 2026). Usage has collapsed from 2024 levels.

## 🛡️ Security & audits · 4/10 · ❌ FAIL

- **13 Apr 2025:** a compromised 1-of-1 admin key on the airdrop distributors minted **111,881,122 ZK** (~$5M; [mint tx](https://explorer.zksync.io/tx/0x14b120ff26e8d678fdaa26eef81cf166cb8bc1a20e9bdef6a02fd2af2ee0071e)). 90% was returned on 23 Apr 2025 ([incident report](https://www.zksync.io/blog/incident-report-compromised-admin-key)). The ZK contract and governance were not affected.

## ⚖️ Regulatory · 6/10 · ✅ PASS

- No enforcement action against ZK found. The entities sit in the Cayman Islands and Austria. Listed on major venues.

## 📅 Catalysts & calendar · 3/10 · ❌ FAIL

| Date | Event |
|---|---|
| Monthly to mid-2028 | Investor/team unlocks (7.0B total) |
| Ongoing | Token Program mints (e.g. 804M for 2026 development; 268M minted so far) |
| None | No revenue-sharing mechanism adopted |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🔴 Apr 2025 airdrop-admin key compromise, 111.9M ZK minted; 90% returned |
| Team wallet → exchange during a pump | 🔴 Foundation-funded wallets → Binance on pump days ([4 Nov 2025](https://explorer.zksync.io/tx/0xee3bd5d3729ec710e84500c7ebd7f0b4904e22c0c74e8b68473d044ad6ffdfce), [25 Apr 2025](https://explorer.zksync.io/tx/0xae62d1cd8a8d6434e04de6cd3f01be2e9503e35c39e8a87174a7663a20c19a75)) |
| Live mint path | 🟡 Capped minters plus supply raisable by governance upgrade |
| Treasury selling | 🔴 ~297M ZK from Foundation-funded wallets to Binance deposits (2025) |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| Wallet funded weekly by Foundation Treasury 2 | ZKsync Foundation-funded (end owner [Unverified]) | Explorer funding (on-chain) | high | yes (on-chain) | Selling: 252.2M ZK into a Binance deposit, 53.8M on pump days incl. 4–6 Nov 2025 |

## 📚 Sources

- [Tier A] Methodology update 16 Nov 2026: no new Arkham lookups; the attribution table uses evidence already cited in this report.
- [Tier A] ZKsync Era block-explorer API and RPC: ZK `totalSupply()`, `CAP()`/`minted()` on the capped minters, `balanceOf`; full ZK transfers for Treasury 1, Treasury 2, `0x1054…`, `0xe640…`, `0xc3c1…`, `0x1091…`, the Binance deposits and other recipients; receipts (status 1) for every linked tx, 16 Nov 2026 ~7:10–7:40 AM MST
- [Tier A] ZK Nation docs: [ZK token](https://docs.zknation.io/zk-token/zk-token) · [contract addresses](https://docs.zknation.io/zk-nation/zksync-governance-contract-addresses) · [governance procedures](https://docs.zknation.io/zksync-governance-procedures/zksync-governance-procedures-overview); [incident report](https://www.zksync.io/blog/incident-report-compromised-admin-key); ZK Nation forum threads linked above
- [Tier B] [Blockworks transparency filing](https://blockworks.com/token-transparency/filing/zksync) (Foundation treasury addresses); Etherscan Ethereum labels for exchange addresses reused on Era
- [Tier B] Arkham, read 16 Nov 2026 ~7:35 AM MST (signed-in account): **ZKsync Era is not supported.** The network selector lists only Ethereum, Polygon, BNB Chain, Optimism, Avalanche, Arbitrum, Base, Bitcoin, Tron, Flare, Solana, Dogecoin, Zcash, HyperEVM, Hypercore, Robinhood Chain. The first address looked up, `0xc853…9da4`, showed no assets and no transfers ([Arkham](https://intel.arkm.com/explorer/address/0xc8538a03282eae418237264a3957070efa679da4)). No Arkham labels were available for this report
- [Tier A] CoinGecko `zksync` market data (16 Nov 2026 6:58 AM MST); Binance ZKUSDT daily closes; DefiLlama `zksync-era` fees, revenue and TVL
- [Unverified] identity of `0x1091…`, `0xe640…`, `0xc3c1…` and the other large Foundation-route recipients; investor/team vesting recipients' selling. Arkham does not support ZKsync Era (checked 16 Nov 2026)

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Supply cap, allocation, governance-raisable supply | [ZK token docs](https://docs.zknation.io/zk-token/zk-token) · [token](https://explorer.zksync.io/address/0x5a7d6b2f92c77fad6ccabd7ee0624e64907eaf3e) | A | 16 Nov 2026 |
| Foundation and Matter Labs minters fully minted | [Foundation minter](https://explorer.zksync.io/address/0xd78dc27d4db8f428c67f542216a2b23663838405) · [Matter Labs minter](https://explorer.zksync.io/address/0xa97fbc75ccbc7d4353c4d2676ed18cd0c5aaf7e6) · [addresses](https://docs.zknation.io/zk-nation/zksync-governance-contract-addresses) | A | 16 Nov 2026 |
| Foundation treasuries | [Blockworks](https://blockworks.com/token-transparency/filing/zksync) · [T1](https://explorer.zksync.io/address/0xc8538a03282eae418237264a3957070efa679da4) · [T2](https://explorer.zksync.io/address/0xea81e12b73696599fdc8ba407e858d7163977619) | B + A chain | 16 Nov 2026 |
| Treasury 2 funded `0x1091…` during the Nov 2025 spike | [4 Nov](https://explorer.zksync.io/tx/0x79b1de2d204ffb3a5ee2a3beccbe849b8448c6df37df22a015cde0af834f5555) · [5 Nov](https://explorer.zksync.io/tx/0x4d1c200ab948d41ac6697f44f54556f4777acc588bd4295af16c5b315f4fcb8e) | A | 16 Nov 2026 |
| `0x1091…` → Binance on pump days | [2 Nov](https://explorer.zksync.io/tx/0x76346895dbc31785a55d5e2976cfee8febae76dd3aad7224a4fb3bcc067c3227) · [4 Nov](https://explorer.zksync.io/tx/0xee3bd5d3729ec710e84500c7ebd7f0b4904e22c0c74e8b68473d044ad6ffdfce) · [5 Nov](https://explorer.zksync.io/tx/0x2c7f9f3367a34bf0c23e4489bbe75d6597d5c4dd8cc61c1a8ce5590a2eafdc10) · [6 Nov](https://explorer.zksync.io/tx/0xe959ad22e1497492a89aae65b98e8e618db733e27d5e83ff61bf58e3fed46ed2) · [deposit](https://explorer.zksync.io/address/0x78b5e3b3b4366f2a981d337d0c4c946233c094c9) | A chain · identity [Unverified] | 16 Nov 2026 |
| `0xe640…` → Binance 44.7M on a +18.3% day | [tx](https://explorer.zksync.io/tx/0xae62d1cd8a8d6434e04de6cd3f01be2e9503e35c39e8a87174a7663a20c19a75) · [sweep to Binance 83](https://explorer.zksync.io/address/0x2b60d59e76c46ea6fc267d23829ae9fce7a8114e) | A chain | 16 Nov 2026 |
| No holder revenue | [DefiLlama revenue](https://api.llama.fi/summary/fees/zksync-era?dataType=dailyRevenue) | A | 16 Nov 2026 |
| Apr 2025 key compromise | [incident report](https://www.zksync.io/blog/incident-report-compromised-admin-key) · [mint tx](https://explorer.zksync.io/tx/0x14b120ff26e8d678fdaa26eef81cf166cb8bc1a20e9bdef6a02fd2af2ee0071e) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Who is `0x1091…0732`, and was the Foundation paying it to sell?** | Arkham does not cover ZKsync Era. Ask the Foundation in the treasury-report forum thread; check whether `0x1091…` also appears on an Arkham-supported chain (Ethereum) under a label | Free |
| 2 | **Where did the 525M (`0x6240…`) and 400M (`0xd0b2…`) Foundation-route tranches end up?** | Follow their recipients (`0xe6dc…`, `0xf12a…`) on the Era explorer and check for exchange sweeps | Free |
| 3 | **Investor and team vesting sales** | Find the vesting contracts minted from the Matter Labs minter and trace claimants to exchanges | Free, slow |
| 4 | **Foundation treasury report** | Watch the [forum thread](https://forum.zknation.io/t/zksync-foundation-treasury-report/856) | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.

- Research only. Not investment advice.
