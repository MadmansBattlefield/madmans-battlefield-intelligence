---
ticker: SWCH
name: SwissCheese
chain: polygon
contract: "0x3ce1327867077b551ae9a6987bf10c9fd08edce1"
overall_score: 2.5
overall_verdict: FAIL
section_scores:
  revenue: 1
  foundation_team: 2
  insider_holdings: 4
  selling_behavior: 4
  tokenomics_supply: 4
  liquidity_market: 2
  product_development: 2
  adoption_customers: 1
  security_audits: 3
  regulatory: 3
  catalysts: 2
gates_failed: [revenue]
red_lines:
  hack_exploit: "none found"
  mint_path_live: "no: 120M minted once on 14 Jul 2023"
  team_wallet_to_exchange_during_pump: "not proven: mint-line wallets sent ~5.1M SWCH to Gate, Bitget and MEXC in Jan-Jun 2026, none on a pump day (MEXC closes)"
  entity_concentration: "not proven: the mint wallet spread all 120M to 11 wallets in 2023-2024; current holders mostly exchanges"
price_usd: 0.01695
price_source: "CoinGecko, 16 Nov 2026 ~9:35 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### SWCH · Overall grade **2.5 / 10 · ❌ FAIL**

**Summary:** SwissCheese is a small Polygon token for a platform that sells tokenised stocks. The full 120M supply was minted to one wallet in July 2023, which passed it all to a handful of wallets. Those wallets are now empty, and the tokens I could locate sit mainly on exchanges. There's no revenue, the team can't be verified, and the market cap is about $2M, or $0.6M on CoinMarketCap's supply figure. Price is down 98% from its Dec 2023 high.

**🚨 Top warning:** wallets funded from the mint wallet keep sending to exchanges. The mint wallet [0xe875…61b3](https://polygonscan.com/address/0xe8755bcaaddb9e6d857077a04f4366e5587b61b3) sent 6M SWCH to [0x1931…ede3](https://polygonscan.com/address/0x1931b3278732cafd3d6bf21783a5af7b31eede3c) on 24 Jul 2023 ([tx](https://polygonscan.com/tx/0xb086616fb592b0db02cb630b08f85f4361ca640826bb20ef801dd7369ff7ed5e)). 0x1931 then funded 0x9735, which sent **509,186 SWCH** to Gate on 26 Jan 2026 ([tx](https://polygonscan.com/tx/0x4501f50da06f34029d599a173279280a4796d1e9592b26e43c296b378c52de52)) and **1.29M** to Bitget a week later. Other mint-line wallets sent 2.3M more in Feb and 1.0M in Jun 2026. None of these fell on a pump day by MEXC closes, but nothing was disclosed, and 98M of the supply can't be located. Every link is in the 🔗 Evidence trail below.

**Sections passed: 0 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 1/10 | ❌ FAIL (hard gate) |
| 🏛️ Foundation & team | 2/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 4/10 | ❌ FAIL |
| 📉 Selling behavior | 4/10 | ❌ FAIL (not proven) |
| 📊 Tokenomics & supply | 4/10 | ❌ FAIL |
| 💧 Liquidity & market | 2/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 2/10 | ❌ FAIL |
| 🤝 Adoption & customers | 1/10 | ❌ FAIL |
| 🛡️ Security & audits | 3/10 | ❌ FAIL |
| ⚖️ Regulatory | 3/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 2/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 SWCH · SwissCheese · 2.5 / 10 · ❌ FAIL

> **One line:** A $2M tokenised-stock token with no revenue, an unverifiable team and mint-line wallets feeding exchanges.

| 📊 Market (CoinGecko, 16 Nov 2026 ~9:35 AM MST) | 🔗 On-chain ([Polygonscan](https://polygonscan.com/token/0x3ce1327867077b551ae9a6987bf10c9fd08edce1), 16 Nov 2026 ~9:40 AM MST) |
|---|---|
| **Price** $0.01695 | **Supply** 120,000,000 SWCH (one mint, 14 Jul 2023) |
| **24h / 7d / 30d** 🟢 +5.7% / ⚪ −1.6% / 🔴 −31.9% | **Mint wallet** 0 left (spread to 11 wallets, 2023–24) |
| **Market cap** $2.02M (CoinMarketCap: $0.61M on 43.7M circulating) | **LBank** 6.41M · **Gate** 5.99M · **MEXC** 2.39M · **Cobo custody** 1.77M |
| **24h volume** $0.26M (LBank $0.11M, BingX $0.10M, MEXC $0.09M, Gate $0.05M) | **Staking contract** 0.77M |
| **ATH** $1.006 (8 Dec 2023) · now −98.3% | **Located** ~22M of 120M (rest not found with free tools) |
| **Pump days** 31 in the last year on MEXC SWCH/USDT closes (largest +113.0% on 29 Jun 2026) | |

---

## 💰 Revenue — Does it make money? · 1/10 · ❌ FAIL (hard gate)

- No fee or revenue data. **1 → hard-gate FAIL.**

## 🏛️ Foundation & team — Who is in charge? · 2/10 · ❌ FAIL

- No verifiable leadership. An independent risk rater flags missing team data (Tier B).

## 🪙 Foundation / team holdings — How many coins do they hold? · 4/10 · ❌ FAIL

- The mint wallet distributed 18M, 18M, 12M, 10.3M, 10M, 10M, 6.9M and 6M ×3 in Jul 2023 and Jul 2024. All of those wallets are now empty. Who holds the 98M I couldn't locate is unknown.

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL (not proven)

| Date | From | To | SWCH | Close | ≈ USD | Pump? | Tx |
|---|---|---|---:|---:|---:|---|---|
| 26 Jan 2026 | 0x9735 (mint → 0x1931 → 0x9735) | Gate | 509,186 | $0.1169 | $60k | No (+9.3%) | [0x4501…](https://polygonscan.com/tx/0x4501f50da06f34029d599a173279280a4796d1e9592b26e43c296b378c52de52) |
| 2–3 Feb 2026 | 0x9735 | Bitget | 1,290,814 | $0.092 | $118k | No | [0x3522…](https://polygonscan.com/tx/0x3522f7484486315efeb82a5d013a60fac56a8402ac73d6405c15079dbcdddc87) |
| 3 Feb 2026 | 0x1acf (mint → 0x85d0 → 0x1acf) | Bitget | 1,000,062 | $0.0907 | $91k | No | [0x8fc4…](https://polygonscan.com/tx/0x8fc4581d60508508ed680762ccab6a342622e623f81a4dda893845610ea6c9a6) |
| 5–6 Feb 2026 | 0x4a81 (mint → 0xfab9 → 0x4a81) | Gate, MEXC | 1,275,000 | $0.087 | $112k | No | [0x4d3f…](https://polygonscan.com/tx/0x4d3ff67d497bf866831c6d8f88828e7aef9e0ecedfffb1db6b3887937dd925a9) |

- Method: a 3-hop trace from the mint wallet on Polygon (Etherscan v2 API, Polygonscan labels), counting transfers of 500k+ SWCH. Pump days use MEXC SWCH/USDT daily closes. CoinGecko's series for this coin swings wildly (for example $0.134 → $0.061 → $0.185 in a week of Mar 2026), so I did not use it. All linked transactions returned status 1. The deposits are steady, but none fell on a pump day, and 98M SWCH is unlocated → **not proven, 4.**

## 📊 Tokenomics & supply · 4/10 · ❌ FAIL

- Fully minted, with no further mint. Circulating figures conflict: CoinGecko 119.2M against CoinMarketCap 43.7M.

## 💧 Liquidity & market · 2/10 · ❌ FAIL

- $0.26M a day on mid-tier venues. Bitget delisted the pair on 17 Apr 2026 [Unverified, one source].

## 🧑‍💻 Product & development · 2/10 · ❌ FAIL

- A tokenised-stock trading and staking app. I found no on-chain usage of the tokenised stocks.

## 🤝 Adoption & customers · 1/10 · ❌ FAIL

- No usage data.

## 🛡️ Security & audits · 3/10 · ❌ FAIL

- The only audit is an uploaded document with no named firm (Tier B).

## ⚖️ Regulatory · 3/10 · ❌ FAIL

- Selling tokenised US stocks to retail users without disclosed licensing is a regulatory risk (industry warnings: [WFE](https://www.world-exchanges.org/news/articles/world-federation-exchanges-urges-crackdown-tokens-mimic-equities)).

## 📅 Catalysts & calendar · 2/10 · ❌ FAIL

- None found.

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | ⚪ Not proven (mint-line deposits, none on pump days) |
| Live mint path | 🟢 None |
| Entity concentration | ⚪ Not proven (98M not located) |

## 📚 Sources

- [Tier A] Polygonscan / Etherscan v2 (chain 137) transfers, balances, labels; receipts checked 16 Nov 2026
- [Tier A] CoinGecko `swisscheese` (market, venues); pump days from MEXC SWCHUSDT daily closes
- [Tier B] [CoinMarketCap](https://coinmarketcap.com/currencies/swisscheese/) (circulating 43.7M), [Token Vitals](https://tokenvitals.com/token/swch) (team, audit, Bitget delisting)
- Arkham was not run for this report

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| 120M minted to one wallet | [tx 0x51ab…](https://polygonscan.com/tx/0x51ab28fe51e4361c2406ad8b992efe59b0892c13fdeb6dc0978063db2dbae96f) | A | 16 Nov 2026 |
| 6M mint → 0x1931 | [tx 0xb086…](https://polygonscan.com/tx/0xb086616fb592b0db02cb630b08f85f4361ca640826bb20ef801dd7369ff7ed5e) | A | 16 Nov 2026 |
| 0x1931 → 0x9735 (2.5M) | [tx 0x5aa4…](https://polygonscan.com/tx/0x5aa43a5b7f072282f0bcc7f7a758862c77fe8cf2f1ecae45f7f0ccb83cccb487) | A | 16 Nov 2026 |
| 26 Jan 2026 Gate deposit | [tx 0x4501…](https://polygonscan.com/tx/0x4501f50da06f34029d599a173279280a4796d1e9592b26e43c296b378c52de52) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Who controls the mint wallet and its 11 recipients** | Look up the mint wallet and its recipients on Arkham (Polygon is covered), or ask the issuer | Free account |
| 2 | **Where the other ~98M SWCH sits** | Read Polygonscan's holder page (blocked for scripts) or use Arkham | Free account |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.

- Research only. Not investment advice.
