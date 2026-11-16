---
ticker: TRB
name: Tellor
chain: ethereum
contract: "0x88df592f8eb5d7bd38bfef7deb0fbc02cf3778a0"
overall_score: 3.8
overall_verdict: FAIL
section_scores:
  revenue: 2
  foundation_team: 5
  insider_holdings: 6
  selling_behavior: 1
  tokenomics_supply: 4
  liquidity_market: 4
  product_development: 6
  adoption_customers: 3
  security_audits: 6
  regulatory: 6
  catalysts: 4
gates_failed: [revenue, selling_behavior]
red_lines:
  hack_exploit: "none found"
  mint_path_live: "yes by design: 4,000 TRB/month dev share to the team plus ~4,000 TRB/month to reporters and validators (hard-coded); no max supply"
  team_wallet_to_exchange_during_pump: "yes: two pass-through wallets funded only by the Tellor MultiSig (directly or via its payout wallet 0x1b8e) sent 24,035 TRB (~$2.93M) to the Etherscan-labelled Coinbase 10 address on seven pump days, Jun 2023 to May 2025, including 7,000 TRB at $243 on 29 Dec 2023; the payout Safe 0x1b8e itself sent 11,000 TRB to Arkham-labelled Coinbase deposits on three pump days in Aug–Oct 2026; no disclosure found"
  entity_concentration: "Tellor MultiSig holds 76,302 TRB (2.6%)"
price_usd: 12.97
price_source: "CoinGecko, 16 Nov 2026 ~8:40 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### TRB · Overall grade **3.8 / 10 · ❌ FAIL**

**Summary:** Tellor is a permissionless oracle. It now runs its own chain (Tellor Layer), bridged to the ERC20 on Ethereum. The team gets a hard-coded **4,000 TRB a month** dev share, minted into the Etherscan-labelled **Tellor MultiSig**, and the same amount again goes to reporters and validators. Usage is minimal, there are no published fees and value secured is near zero, so the revenue gate fails. The selling gate also fails: TRB paid out of the MultiSig reached **Coinbase on seven pump days**, including the Dec 2023 squeeze.

**🚨 Top warning:** team-funded wallets sold into pumps. Two wallets funded only by the **Tellor MultiSig** (directly, or through its payout wallet 0x1b8e…9190) sent **24,035 TRB (~$2.93M)** to the Etherscan-labelled **Coinbase 10** address on **seven pump days**. The largest was **7,000 TRB on 29 Dec 2023** at a $243.47 close, +33.9% vs five days earlier, two days before the $593 peak ([tx](https://etherscan.io/tx/0x5d352036a488022c60eebc40d916767e952a5dc455bee46920cff1a8e155517d)). Another 3,300 TRB went on 29 May 2025, a +99% day ([tx](https://etherscan.io/tx/0xd3c1c469a72a17a41226a492b9fd71b27d49b0b8a872b5198722853188188f84)). It has not stopped: in Aug–Oct 2026 the MultiSig-funded payout Safe sent **11,000 TRB** straight to Arkham-labelled Coinbase deposit addresses on three pump days. Supply also grows by about 96,000 TRB a year with no cap. Every link is in the 🔗 Evidence trail below.

**Sections passed: 4 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 2/10 | ❌ FAIL (hard gate) |
| 🏛️ Foundation & team | 5/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 6/10 | ✅ PASS |
| 📉 Selling behavior | 1/10 | ❌ FAIL (hard gate) |
| 📊 Tokenomics & supply | 4/10 | ❌ FAIL |
| 💧 Liquidity & market | 4/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 6/10 | ✅ PASS |
| 🤝 Adoption & customers | 3/10 | ❌ FAIL |
| 🛡️ Security & audits | 6/10 | ✅ PASS |
| ⚖️ Regulatory | 6/10 | ✅ PASS |
| 📅 Catalysts & calendar | 4/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 TRB · Tellor · 3.8 / 10 · ❌ FAIL

> **One line:** A small-float oracle token that mints for its team every month, with team-funded wallets selling into the pumps.

| 📊 Market (CoinGecko, 16 Nov 2026 ~8:40 AM MST) | 🔗 On-chain ([Etherscan](https://etherscan.io/token/0x88df592f8eb5d7bd38bfef7deb0fbc02cf3778a0), 16 Nov 2026 ~9:05 AM MST) |
|---|---|
| **Price** $12.97 | **Total supply** 2,912,567 TRB (no cap) |
| **24h / 7d / 30d** 🔴 −0.8% / −15.5% / −28.3% | **Circulating** 2.84M (CoinGecko) |
| **Market cap** $36.8M · **FDV** $37.8M | **Tellor MultiSig** 76,302 TRB (2.6%) |
| **24h volume** $6.05M (BloFin $0.99M, Binance $0.63M, GroveX $0.59M, OKX $0.56M, WhiteBIT $0.41M) | **Team mint** 4,000 TRB/month into the MultiSig (220,487 TRB received from mints in the last 1,000 transfers) |
| **ATH** $593.09 (31 Dec 2023) · now −97.8% | **Tellor Layer** 20 validators, 62 reporters (operator dashboard) |
| **Pump days** 29 in the last year (largest +47.2% on 23 Aug 2026) | |

---

## 💰 Revenue — Does it make money? · 2/10 · ❌ FAIL (hard gate)

- Users pay reporters in tips; there is no protocol fee to holders. DefiLlama has no fee record. [Unverified] A secondary source puts total value secured at about $0. **2 → hard-gate FAIL.**

## 🏛️ Foundation & team — Who is in charge? · 5/10 · ❌ FAIL

- A US-based core team since 2019 (no ICO). The team is funded by the hard-coded monthly dev share. Leaders are described by role only.

## 🪙 Foundation / team holdings — How many coins do they hold? · 6/10 · ✅ PASS

- The [Tellor MultiSig](https://etherscan.io/address/0x39e419ba25196794b595b2a595ea8e527ddc9856) holds 76,302 TRB (2.6%); [Arkham](https://intel.arkm.com/explorer/address/0x39e419ba25196794b595b2a595ea8e527ddc9856) labels it **MultiSig** (no signers shown). It receives the mints and pays team wallets. The largest outflows are 187,100 TRB to [0x1b8e…9190](https://etherscan.io/address/0x1b8e06e7133b89ea5a799bf2bf0221ae71959190) (2022–2026) and 32,882 TRB to [0x3a05…9d75](https://etherscan.io/address/0x3a05689137b23c136744799735867da74e9b9d75) (39 monthly transfers).

## 📉 Selling behavior — Do insiders sell into pumps? · 1/10 · ❌ FAIL (hard gate)

Path: Tellor MultiSig → payout wallet [0x1b8e…9190](https://etherscan.io/address/0x1b8e06e7133b89ea5a799bf2bf0221ae71959190) → pass-through [0xe372…f24b](https://etherscan.io/address/0xe37211aa9bf358e1edcd707c0ea9e3913d9bf24b) (only funder: 0x1b8e) or [0x3f9c…a52e](https://etherscan.io/address/0x3f9c8aca305a7ab4de20d4e9eedc48285d0fa52e) (only funders: 0x1b8e and the MultiSig) → [Coinbase 10](https://etherscan.io/address/0xa9d1e08c7793af67e9d92fe308d5697fb81d3e43) (Etherscan label; [Arkham](https://intel.arkm.com/explorer/address/0xa9d1e08c7793af67e9d92fe308d5697fb81d3e43): **Coinbase: Hot Wallet**, an exchange wallet, not a staking contract).

**Arkham ([Tier B] Arkham, read 16 Nov 2026 (signed-in account)):** [0x1b8e…9190](https://intel.arkm.com/explorer/address/0x1b8e06e7133b89ea5a799bf2bf0221ae71959190) is a **Gnosis Safe**, and one of its signers is an individual-labelled ENS wallet (not named here). [0x3a05…9d75](https://intel.arkm.com/explorer/address/0x3a05689137b23c136744799735867da74e9b9d75) is unlabelled; Arkham's first page shows only its monthly MultiSig payouts, so its 2023 Binance send rests on Etherscan.

| Date | Pump (vs 5d) | From | TRB | Close | ≈ USD | Tx |
|---|---|---|---:|---:|---:|---|
| 23 Jun 2023 | +15.1% | 0xe372 | 5,000 | $10.04 | $50k | [0x2155…](https://etherscan.io/tx/0x21558603d8ed4fc426d59710af0e2cdbc9567b746c6cab2fd603077b8023f4c3) |
| 14 Dec 2023 | +31.3% | 0xe372 | 735 | $124.78 | $92k | [0x5b1f…](https://etherscan.io/tx/0x5b1f7006d7602b1c9c0f49d1658dbc01ca4cc84d25b93ba897be8eb97bb50e56) |
| 29 Dec 2023 | +33.9% | 0xe372 | 7,000 | $243.47 | $1.70M | [0x5d35…](https://etherscan.io/tx/0x5d352036a488022c60eebc40d916767e952a5dc455bee46920cff1a8e155517d) |
| 8 May 2024 | +82.9% | 0x3f9c | 4,000 | $128.34 | $513k | [0x58f1…](https://etherscan.io/tx/0x58f194a960bf6b3ffe393b34de6782b8bab3a6b29ece4b4331233e04ccbd7124) |
| 5 Dec 2024 | +13.5% | 0x3f9c | 1,000 | $88.97 | $89k | [0xddfe…](https://etherscan.io/tx/0xddfe7d680dcec57b6c0676c7aad5aa9a1a13918eee226dceae17670f9409f140) |
| 6 Dec 2024 | +18.1% | 0x3f9c | 3,000 | $94.56 | $284k | [0x21a7…](https://etherscan.io/tx/0x21a725535d8755881e79d1989305a0ea9882fda3495d4706669df648937e02e8) |
| 29 May 2025 | +99.0% | 0x3f9c | 3,300 | $60.35 | $199k | [0xd3c1…](https://etherscan.io/tx/0xd3c1c469a72a17a41226a492b9fd71b27d49b0b8a872b5198722853188188f84) |

- Total: **24,035 TRB, about $2.93M, on seven pump days.** These two wallets passed on everything they received to Coinbase 10 (30,947 and 36,300 TRB). A separate monthly payout wallet, 0x3a05…9d75, also sent 34,692 TRB to Binance on 20 Nov 2023 ([tx](https://etherscan.io/tx/0xd54150337c1b0340d48ecff3bdbe90d8cde162308d2c49aa3018fad6d4c6aea6)), not a pump day.
- **2026, direct from the payout Safe** (Etherscan dates and amounts; Coinbase Deposit labels from Arkham; 5-day change from Gate TRB/USDT closes):

| Date | Pump (vs 5d) | To | TRB | Close | ≈ USD | Tx |
|---|---|---|---:|---:|---:|---|
| 24 Aug 2026 | **+34.7%** | Coinbase Deposit `0x5920…` | 3,500 | $18.68 | $65k | [0x862c…](https://etherscan.io/tx/0x862c467ebd035449906962e5e07088e7d8d2ebb98f354b325b4869537d8f55d5) |
| 21 Sep 2026 | **+12.1%** | Coinbase Deposit `0xc750…` | 3,500 | $19.15 | $67k | [0x158a…](https://etherscan.io/tx/0x158a49382b3c03f081337279aab1b5439eb0f2e9450bd8a64ab496f539c3ee8c) |
| 28 Sep 2026 | +1.6% | Coinbase Deposit `0x9f42…` | 2,000 | $19.06 | $38k | [0x003b…](https://etherscan.io/tx/0x003b4a2b63b052853c891fee5a1f00ad8ade4799fa994e373509ba8b55683a87) |
| 1 Oct 2026 | +3.4% | Coinbase Deposit `0xa109…` | 4,000 | $20.68 | $83k | [0x4ff2…](https://etherscan.io/tx/0x4ff2793dcec3b7cf5edc08132f6843dee41f972d83c0515813a045dd2c12cc85) |
| 6 Oct 2026 | **+10.6%** | Coinbase Deposit `0xd7fb…` | 4,000 | $22.87 | $91k | [0x709b…](https://etherscan.io/tx/0x709b84b41db3b7851b33b5030610d6ad997aeb159843d6e6c09c352c34ece0e1) |

  Pump-day total: **11,000 TRB, about $224k**. Each send followed a MultiSig top-up of the Safe (8,000 TRB on 24 Aug, 10,000 on 1 Oct). The Safe also sent 3,000–4,000 TRB to unlabelled addresses on 26 Jan, 15 Apr, 1 May (+11.0%) and 17 Jul 2026, and ~60–90 TRB a month to Coinbase Deposit `0x8397…`.
- The dev share is disclosed, but no disclosure was found of these sales being timed into rallies. Every linked transaction returned status 1 (success).

## 📊 Tokenomics & supply · 4/10 · ❌ FAIL

- No max supply. About 8,000 TRB is minted each month (team plus rewards), roughly 3.3% a year, hard-coded.

## 💧 Liquidity & market · 4/10 · ❌ FAIL

- $6.05M of 24h volume (16% of market cap), but the float is small and the token has a record of squeezes.

## 🧑‍💻 Product & development · 6/10 · ✅ PASS

- Tellor Layer is live with 20 validators and 62 reporters, and rewards fully moved to the Layer in May 2026.

## 🤝 Adoption & customers · 3/10 · ❌ FAIL

- Few known integrations; value secured is near zero (Tier B).

## 🛡️ Security & audits · 6/10 · ✅ PASS

- No exploit found. Bonded value is about $0.97M (operator dashboard), so the oracle has little economic security.

## ⚖️ Regulatory · 6/10 · ✅ PASS

- No enforcement found.

## 📅 Catalysts & calendar · 4/10 · ❌ FAIL

- No dated catalysts.

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | 🔴 Yes: 24,035 TRB to Coinbase on seven pump days |
| Live mint path | 🟠 Yes, by design (team plus rewards) |
| Entity concentration | 🟢 2.6% in the MultiSig |

## 📚 Sources

- [Tier A] Etherscan token, MultiSig and transaction pages; receipts checked through the Etherscan API on 16 Nov 2026
- [Tier A] [Tellor whitepaper 2026](https://tellor.io/wp-content/uploads/2026/08/Tellor-Whitepaper-2026-1.pdf) (4,000 TRB/month dev share)
- [Tier A] [Tellor operator dashboard](https://operator.tellor.io/) (validators, reporters, bonded value)
- [Tier A] CoinGecko `tellor`; pump days from Binance TRBUSDT daily closes
- [Tier A] Etherscan address label "Coinbase 10" for 0xa9d1…3e43, read 16 Nov 2026
- [Tier B] Secondary token dossier on value secured ([Unverified], single source)
- [Tier B] Arkham, read 16 Nov 2026 (signed-in account): MultiSig label on 0x39e4; Gnosis Safe with an individual-labelled ENS signer on 0x1b8e; Coinbase Deposit labels on its 2026 recipients; Coinbase Hot Wallet on 0xa9d1
- [Tier A] Etherscan v2 API `tokentx` for 0x1b8e (2026); Gate TRB/USDT daily closes for the 2026 transfers

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| MultiSig receives mints, holds 76,302 TRB | [Tellor MultiSig](https://etherscan.io/address/0x39e419ba25196794b595b2a595ea8e527ddc9856) | A | 16 Nov 2026 |
| Team-funded wallet → Coinbase, 7,000 TRB at the Dec 2023 squeeze | [tx 0x5d35…](https://etherscan.io/tx/0x5d352036a488022c60eebc40d916767e952a5dc455bee46920cff1a8e155517d), [Coinbase 10 label](https://etherscan.io/address/0xa9d1e08c7793af67e9d92fe308d5697fb81d3e43) | A | 16 Nov 2026 |
| Payout wallet → Binance, 34,692 TRB | [tx 0xd541…](https://etherscan.io/tx/0xd54150337c1b0340d48ecff3bdbe90d8cde162308d2c49aa3018fad6d4c6aea6) | A | 16 Nov 2026 |
| Payout wallet → Binance, 9,183 TRB | [tx 0xc61a…](https://etherscan.io/tx/0xc61a7097342552d3ded6c8bac1ab15970e7dbb0442dd7e1bfcedecb872d7764e) | A | 16 Nov 2026 |
| 4,000 TRB/month dev share | [whitepaper](https://tellor.io/wp-content/uploads/2026/08/Tellor-Whitepaper-2026-1.pdf) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Who signs 0x1b8e, and who controls 0xe372 and 0x3f9c** | Arkham (16 Nov 2026) shows 0x1b8e as a Safe with one individual-labelled signer and leaves the pass-throughs unlabelled. Ask Tellor for its treasury disclosures [Unverified] | Free |
| 2 | **Any team disclosure of these sales** | Search Tellor's blog and forum posts from 2023–2025 for treasury reports | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.

- Research only. Not investment advice.
