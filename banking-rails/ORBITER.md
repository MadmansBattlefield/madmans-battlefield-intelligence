---
ticker: ORBITER
name: Orbiter Finance (OBT)
chain: ethereum
contract: "0x4af322ff4a6f2858f6b51e546b9ec499654493c5"
overall_score: 3.8
overall_verdict: FAIL
section_scores:
  revenue: 3
  foundation_team: 5
  insider_holdings: 3
  selling_behavior: 4
  tokenomics_supply: 4
  liquidity_market: 2
  product_development: 6
  adoption_customers: 4
  security_audits: 5
  regulatory: 6
  catalysts: 3
gates_failed: [revenue]
red_lines:
  hack_exploit: "none found"
  mint_path_live: "no; 10B minted once"
  team_wallet_to_exchange_during_pump: "not proven: the genesis wallet only bridged to Arbitrum; the one pump-day Bybit deposit found came from a wallet Arkham labels as Bithumb's hot wallet (exchange-to-exchange)"
  entity_concentration: "genesis wallet 3.7B (37%) on Ethereum; the 4.14B Arbitrum holder is Bithumb's hot wallet (exchange custody)"
price_usd: 0.00021095
price_source: "CoinGecko, 16 Nov 2026 ~12:30 PM MST"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "discretionary buyback-and-burn (~100M OBT burned since Oct 2025, partly bought from strategic investors); not automatic"
pump_day_price_source: "Gate OBT_USDT daily closes (UTC); Binance unavailable (451), Gate is next in the hierarchy"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions:
  - address: "0x34dce6febeedacd6fa9be09b45e825a62f84cd1d"
    label: "OBT genesis wallet (received the full 10B mint)"
    confidence: high
    independent_corroboration: true
    basis: "on-chain mint of 9.99999B OBT from the zero address (direct, independent of Arkham); the official tokenomics post says most allocations were unreleased at launch; Arkham gives only a generic Gnosis Safe label"
  - address: "0x40b8080938ac85e7f2ff2c0503c19d696c8bef9a"
    label: "Bithumb: Hot Wallet (4.145B OBT)"
    confidence: medium
    independent_corroboration: true
    basis: "Arkham entity label; flows with Bithumb deposit addresses on Arkham page 1"
  - address: "0x4024435a9bc141eed6d8ffdc48b9a43c23f0e087"
    label: "Bithumb: Hot Wallet"
    confidence: medium
    independent_corroboration: true
    basis: "Arkham entity label; funded by the Bithumb hot wallet 0x40b8 and forwards to Bybit and Gate deposits"
  - address: "0x3ce5e6ae2caf91fbcefb11d1f8269b3ae05727c0"
    label: "OKX Blockdream Ventures (Arkham); bridges OBT to Arbitrum"
    confidence: medium
    independent_corroboration: false
    basis: "Arkham single-source label; Etherscan shows 1.42B OBT in from the genesis wallet and all of it out through the Arbitrum gateway router"
  - address: "0x2f313a0bd2f885ddc4a3d990d4effccfc659c202"
    label: "HTX: Hot Wallet"
    confidence: medium
    independent_corroboration: false
    basis: "Arkham entity label"
  - address: "0x5cbd15d48ac85035f57736dffd3f279f923d267d"
    label: "Bybit deposit"
    confidence: medium
    independent_corroboration: false
    basis: "Etherscan cross-chain deposit tag only"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### ORBITER · Overall grade **3.8 / 10 · ❌ FAIL**

**Summary:** Orbiter Finance runs a cross-rollup bridge, and OBT launched in Mar 2025. The team burned ~100M OBT in discretionary buybacks, partly bought from its own strategic investors, but no automatic mechanism pays holders. The genesis wallet still holds 37% of supply and moved coins to Arbitrum on two pump days. On Arbitrum, the largest holder is Bithumb's hot wallet, and no team sale is proven. Volume is ~$37k a day, 79% of it on Bithumb. OBT is down 99.4% from its peak. The revenue gate fails.

**🚨 Top warning:** **37% of supply sits in the genesis wallet, which keeps bridging coins out.** Genesis wallet [`0x34dc…cd1d`](https://etherscan.io/address/0x34dce6febeedacd6fa9be09b45e825a62f84cd1d) received the full 10B mint and still holds **3.7B OBT**. Since Dec 2025 it has bridged **1.3B** to Arbitrum, including 60M on 26 Aug 2026 (+10.9%) and 140M on 21 Sep 2026 (+17.2%). They went through two wallets, one Arkham-labelled OKX Blockdream Ventures (an investor), that bridged them through the Arbitrum gateway; where they went next on Arbitrum isn't traced. Every link is in the 🔗 Evidence trail below.

**Sections passed: 2 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 3/10 | ❌ FAIL (hard gate) |
| 🏛️ Foundation & team | 5/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 3/10 | ❌ FAIL |
| 📉 Selling behavior | 4/10 | ❌ FAIL (not proven) |
| 📊 Tokenomics & supply | 4/10 | ❌ FAIL |
| 💧 Liquidity & market | 2/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 6/10 | ✅ PASS |
| 🤝 Adoption & customers | 4/10 | ❌ FAIL |
| 🛡️ Security & audits | 5/10 | ❌ FAIL |
| ⚖️ Regulatory | 6/10 | ✅ PASS |
| 📅 Catalysts & calendar | 3/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 ORBITER · Orbiter Finance (OBT) · 3.8 / 10 · ❌ FAIL

> **One line:** A working bridge with a discretionary burn, a 37% genesis overhang and thin, Bithumb-heavy trading.

| 📊 Market (CoinGecko, 16 Nov 2026 ~12:30 PM MST) | 🔗 Chain (Etherscan / Arbiscan) |
|---|---|
| **Price** $0.000211 | **Supply** 6.3B circulating / 10B |
| **24h / 7d / 30d** 🔴 −5.4% / 🔴 −8.7% / 🔴 −30.5% | **Genesis wallet** 3.7B (37%) |
| **Market cap** $1.33M · **FDV** $2.11M | **Arbitrum gateway escrow** 5.16B · **Base bridge** 745M |
| **24h volume** ~$37.4k (Bithumb KRW $29.6k, Gate $2.5k, KuCoin $2.4k, Bybit $2.1k) | **Top Arbitrum holder** 4.14B (Bithumb hot wallet) |
| **ATH** $0.0329 (13 Mar 2025) · now −99.4% | |
| **Pump days** 14 in the last year (Gate OBT_USDT; largest +18.3% on 25 Aug 2026) | |

---

## 💰 Revenue — Does it make money? · 3/10 · ❌ FAIL (hard gate)

- The bridge earns fees. Since Oct 2025 the team has burned ~100M OBT. That includes 82.5M bought back from strategic investors, paid for with protocol revenue and returns on a WLFI investment ([Bloomingbit](https://en.bloomingbit.io/feed/news/98926)) [Tier B]. The burn is discretionary, not an automatic fee mechanism.

**What it means:** the token has no claim on revenue; holders benefit only when the team chooses to buy. **Holder test: no.** **3 → hard-gate FAIL.**

## 🏛️ Foundation & team — Who is in charge? · 5/10 · ❌ FAIL

- Built by the Orbiter Finance team, described here by role. No on-chain governance over the treasury.

## 🪙 Foundation / team holdings — How many coins do they hold? · 3/10 · ❌ FAIL

- Genesis wallet [`0x34dc…cd1d`](https://etherscan.io/address/0x34dce6febeedacd6fa9be09b45e825a62f84cd1d) received the **full 10B mint** and still holds **3.7B (37%)**. **Attribution confidence:** high (on-chain mint record, plus the [official tokenomics](https://orbiter-finance.medium.com/obtokenomics-and-airdrop-eligibility-guide-3549dd00807a), which show community, ecosystem and team allocations unreleased at launch).
- On Arbitrum, [0x40b8…ef9a](https://intel.arkm.com/explorer/address/0x40b8080938ac85e7f2ff2c0503c19d696c8bef9a) holds **4.145B**. Arkham labels it **Bithumb: Hot Wallet**, and its page-1 flows are with Bithumb deposit addresses, so this is exchange custody of customer coins, not a team or insider holding. It is excluded from the insider count. [Tier B] Arkham, read 16 Nov 2026 (signed-in account).
- Arkham gives the genesis wallet only a generic Gnosis Safe label (low confidence on its own). Its project link rests on the on-chain record that it received the full 10B mint, which is direct and independent of Arkham. The score therefore stays 3, based on the genesis wallet's 37% alone; the Bithumb balance never counted toward it.

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL (not proven)

- **Trail:** since 16 Nov 2025 the genesis wallet has sent coins only to two wallets, [0x3ce5…27c0](https://intel.arkm.com/explorer/address/0x3ce5e6ae2caf91fbcefb11d1f8269b3ae05727c0) (Arkham: **OKX Blockdream Ventures**, single source, medium confidence) and [`0x1443…847c`](https://etherscan.io/address/0x1443114e33db68a64bdc20bfbe64c9d8ad96847c) (unlabelled), which passed every OBT they received to the Arbitrum gateway router ([0x3ce5 on Etherscan](https://etherscan.io/address/0x3ce5e6ae2caf91fbcefb11d1f8269b3ae05727c0)): **1.3B OBT**, including **60M on 26 Aug** and **140M on 21 Sep 2026**, both pump days (status 1). A transfer to an investor that then bridges isn't an exchange deposit, and the Arbitrum receivers weren't traced.
- **Pump-day deposit:** Arbitrum hot wallet [0x4024…e087](https://intel.arkm.com/explorer/address/0x4024435a9bc141eed6d8ffdc48b9a43c23f0e087) (Arkham: **Bithumb: Hot Wallet**) (funded with 2.66B by [`0x40b8…ef9a`](https://arbiscan.io/address/0x40b8080938ac85e7f2ff2c0503c19d696c8bef9a)) sent **22.5M OBT (~$8k)** to a Bybit deposit on 26 Aug 2026 (+10.9%): [tx](https://arbiscan.io/tx/0xa42f951c310918ab1c474e9cdeec6d00ac579ade8bf04a9e392c25f772098a34) (status 1). Overall it has sent 262M to that Bybit deposit.
- **Attribution:** Arkham labels both the sender and its funder as Bithumb hot wallets, so this is an exchange moving customer coins to Bybit, not a team sale. A third wallet once queried for Gate and Bybit deposits, [0x2f31…c202](https://intel.arkm.com/explorer/address/0x2f313a0bd2f885ddc4a3d990d4effccfc659c202), is labelled **HTX: Hot Wallet**. [Tier B] Arkham, read 16 Nov 2026 (signed-in account).
- No team wallet is shown selling on a pump day: **not proven → 4.** **Disclosure quality:** not applicable.

## 📊 Tokenomics & supply · 4/10 · ❌ FAIL

- 10B minted once; 63% circulating. Team 15% is ~42–44% unlocked on a linear schedule to Jun 2028; investors (10%) fully unlocked 20 Jun 2026; next unlock ~90.5M on 19 Nov 2026 [Tier B: Tokenomics.com, CoinGlass, DropsTab].

## 💧 Liquidity & market · 2/10 · ❌ FAIL

- About $37k a day, 79% on Bithumb's KRW pair.

## 🧑‍💻 Product & development · 6/10 · ✅ PASS

- The bridge is live across many rollups.

## 🤝 Adoption & customers · 4/10 · ❌ FAIL

- Real bridge users; token use is mostly trading.

## 🛡️ Security & audits · 5/10 · ❌ FAIL

- No OBT exploit found. Bridges are a high-risk category.

## ⚖️ Regulatory · 6/10 · ✅ PASS

- No enforcement found.

## 📅 Catalysts & calendar · 3/10 · ❌ FAIL

- Unlock on 19 Nov 2026; any further buybacks are at the team's discretion.

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | ⚪ Not proven: genesis wallet sent to an investor-labelled bridging wallet on pump days; the Bybit sender is Bithumb's hot wallet |
| Live mint path | 🟢 None |
| Entity concentration | 🔴 Genesis 37%; the 4.14B Arbitrum holder is Bithumb's hot wallet (exchange) |

## 📚 Sources

- [Tier B] Arkham, read 16 Nov 2026 (signed-in account): entity labels for the genesis Safe, the OKX Blockdream Ventures wallet, the Bithumb and HTX hot wallets
- [Tier A] Etherscan and Arbiscan: holders, mint record and traced transfers (linked above)
- [Tier A] [Orbiter tokenomics post](https://orbiter-finance.medium.com/obtokenomics-and-airdrop-eligibility-guide-3549dd00807a)
- [Tier B] [Bloomingbit on the buyback and burn](https://en.bloomingbit.io/feed/news/98926); Tokenomics.com, CoinGlass and DropsTab unlock data
- [Tier A] CoinGecko `orbiter-finance` (market, venues); pump days from Gate OBT_USDT daily closes (UTC), per the price-source hierarchy

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Genesis wallet received the 10B mint, holds 3.7B | [`0x34dc…cd1d`](https://etherscan.io/address/0x34dce6febeedacd6fa9be09b45e825a62f84cd1d) | A | 16 Nov 2026 |
| Pump-day bridge transfers to Arbitrum | [60M, 26 Aug](https://etherscan.io/tx/0xeb4b2634a4f73aa52a12dda08c2e0bcfc5c6224964687cd67dad8acbd6ce8560) · [140M, 21 Sep](https://etherscan.io/tx/0x93a085b00452abd6e8223cbf4cc871f185899eef141733d5e6185fe4a288cc64) | A | 16 Nov 2026 |
| Unlabelled Arbitrum wallet → Bybit deposit on a pump day | [tx](https://arbiscan.io/tx/0xa42f951c310918ab1c474e9cdeec6d00ac579ade8bf04a9e392c25f772098a34) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Who controls the 4.14B Arbitrum holder and its hot wallet?** | Closed 16 Nov 2026: Arkham labels [0x40b8…ef9a](https://intel.arkm.com/explorer/address/0x40b8080938ac85e7f2ff2c0503c19d696c8bef9a) and [0x4024…e087](https://intel.arkm.com/explorer/address/0x4024435a9bc141eed6d8ffdc48b9a43c23f0e087) Bithumb: Hot Wallet | Done |
| 2 | **Where the genesis wallet's bridged coins landed** | Read each bridge deposit's L2 recipient and trace it | Free (explorers) |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.

- Research only. Not investment advice.
