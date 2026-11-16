---
ticker: REQ
name: Request Network
chain: ethereum
contract: "0x8f8221afbb33998d8584a2b05749ba73c37a938a"
overall_score: 3.9
overall_verdict: FAIL
section_scores:
  revenue: 2
  foundation_team: 5
  insider_holdings: 3
  selling_behavior: 1
  tokenomics_supply: 6
  liquidity_market: 6
  product_development: 6
  adoption_customers: 5
  security_audits: 5
  regulatory: 6
  catalysts: 4
gates_failed: [revenue, selling_behavior]
red_lines:
  hack_exploit: "none found (DefiLlama hacks list empty)"
  mint_path_live: "no: fixed 1B supply, burn only (999,416,741 left)"
  team_wallet_to_exchange_during_pump: "yes: the Etherscan-labelled Team Wallet sent 600,000 REQ to Bitfinex on 30 Mar 2021, a +37.1% pump day; no disclosure found"
  one_hop_sale_status: proven
  entity_concentration: "Team Wallet holds 184.8M (18.5%); wallets it funded hold another 63.5M (6.3%)"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "No fee totals are published and no executed holder mechanism of measurable size is shown."
pump_day_price_source: "the daily closes cited in the body (2021 pump days)"
pump_day_disclosure_quality: silence
pump_day_undisclosed_penalty_applied: true
dual_review: not_run
attributions: []
price_usd: 0.04510
price_source: "CoinGecko, 16 Nov 2026 ~8:40 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### REQ · Overall grade **3.9 / 10 · ❌ FAIL**

**Summary:** Request Network is an invoicing and payments protocol that has been live on Ethereum since 2017. A separate company built Request Finance on top of it. The product is real, but the token captures almost nothing. The only link between usage and REQ is a buy-and-burn, which has removed **583,259 REQ in total (0.06% of supply, about $26k)**. No protocol fee totals are published, so the revenue gate fails. The selling gate also fails: the Etherscan-labelled **Team Wallet** sent REQ straight to an exchange on a pump day, and wallets it funded have since moved 55.9M REQ to Kraken.

**🚨 Top warning:** the **Team Wallet** contract sent **600,000 REQ to Bitfinex on 30 Mar 2021**, when the close was **37.1% above** the close five days earlier ([tx](https://etherscan.io/tx/0x09d8a7671f160b01b8cddd7fbdb6daaaa30718df7fd23f98655af691f36edcc3)). It also sent 15.0M REQ to Binance on 12 May 2021 ([tx](https://etherscan.io/tx/0xd892f52d4764664602385e2ce4f15f3b2acd16ac3035a280c897908f44342049)). No disclosure of either transfer was found. It still holds **184.8M REQ (18.5%)**, which can move at any time. Every link is in the 🔗 Evidence trail below.

**Sections passed: 4 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 2/10 | ❌ FAIL (hard gate) |
| 🏛️ Foundation & team | 5/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 3/10 | ❌ FAIL |
| 📉 Selling behavior | 1/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 6/10 | ✅ PASS |
| 💧 Liquidity & market | 6/10 | ✅ PASS |
| 🧑‍💻 Product & development | 6/10 | ✅ PASS |
| 🤝 Adoption & customers | 5/10 | ❌ FAIL |
| 🛡️ Security & audits | 5/10 | ❌ FAIL |
| ⚖️ Regulatory | 6/10 | ✅ PASS |
| 📅 Catalysts & calendar | 4/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 REQ · Request Network · 3.9 / 10 · ❌ FAIL

> **One line:** A working payments protocol whose token earns a rounding-error burn, with a team wallet that has sold into a pump.

| 📊 Market (CoinGecko, 16 Nov 2026 ~8:40 AM MST) | 🔗 On-chain ([Etherscan](https://etherscan.io/token/0x8f8221afbb33998d8584a2b05749ba73c37a938a), 16 Nov 2026 ~8:40 AM MST) |
|---|---|
| **Price** $0.04510 | **Total supply** 999,416,741 REQ (1B minus 583,259 burned) |
| **24h / 7d / 30d** 🟢 +5.2% / 🔴 −6.2% / −15.9% | **Circulating** 796.7M (CoinGecko) |
| **Market cap** $35.9M · **FDV** $45.1M | **Team Wallet** 184.8M (18.5%) |
| **24h volume** $9.0M (Bithumb $2.2M, WEEX $2.2M, Binance $2.2M, Coinbase, Kraken) | **Wallets funded by the Team Wallet** 44.0M + 19.5M |
| **ATH** $1.059 (5 Jan 2018) · now −95.7% | **TVL** none listed (DefiLlama) |
| **Pump days** 12 in the last year (largest +47.3% on 18 Apr 2026) | **Burned to date** 583,259 REQ |

---

## 💰 Revenue — Does it make money? · 2/10 · ❌ FAIL (hard gate)

- The protocol charges a payment fee (the pricing page says a flat 0.9%, capped at $500). The fee rate "can change over time" and is not published in the docs, and no fee totals are published. DefiLlama lists no fees or revenue.
- The only on-chain value going to REQ is the buy-and-burn: 583,259 REQ burned in total (0.06% of supply), worth about $26k at today's price. **2 → hard-gate FAIL.**

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** No fee totals are published and no executed holder mechanism of measurable size is shown.

## 🏛️ Foundation & team — Who is in charge? · 5/10 · ❌ FAIL

- The protocol is run by a community-owned foundation. REQ holders vote on the protocol and the foundation. Request Finance is a separate company ([REQ token page](https://request.network/req-token/)). The foundation's leaders are not described on the token page, and no audited foundation accounts were found.

## 🪙 Foundation / team holdings — How many coins do they hold? · 3/10 · ❌ FAIL

| Wallet | REQ | % | Note |
|---|---:|---:|---|
| [Team Wallet (contract)](https://etherscan.io/address/0x0632dcc37b1fabf2cad20538a5390d23c830962e) | 184,825,674 | 18.5% | Etherscan label; [Arkham](https://intel.arkm.com/explorer/address/0x0632dcc37b1fabf2cad20538a5390d23c830962e) labels it **Request Network: Team** (184.826M); no lock found |
| [0xda5d…ee25](https://etherscan.io/address/0xda5d8915e2d7880eae1a5efa51a8da150871ee25) | 44,000,000 | 4.4% | **Coinbase Prime Custody** ([Arkham](https://intel.arkm.com/explorer/address/0xda5d8915e2d7880eae1a5efa51a8da150871ee25)). Funded on 27 Mar 2025 by [`0x60a7…37fc`](https://intel.arkm.com/explorer/address/0x60a73a0629df1d8191e541fcbd3fd321042a37fc), also Coinbase Prime Custody, which received 100M from the Team Wallet in Feb–Mar 2021. Team funds held at a custodian |
| [0x4919…fc15](https://etherscan.io/address/0x4919f5da960edaf34b36473c05a543d4c18bfc15) | 19,450,945 | 1.9% | Received 17.5M from the Team Wallet (18 Feb 2021) and sent 55M back to it in 2025 ([25M](https://etherscan.io/tx/0x325da1b31306288938d5b3b1f0080c84e9f1f0a3980d3ab1e4adfc823ecb67a4), [20M](https://etherscan.io/tx/0x4bd79d33fb6310b499a09852886198c8babb57917e1a2fe60ca0212013f6d55d), [10M](https://etherscan.io/tx/0x216ba76fe74b865b6ac373260cece9391246575fd3de3a17c31df58ef2f32885)). Unlabelled on [Arkham](https://intel.arkm.com/explorer/address/0x4919f5da960edaf34b36473c05a543d4c18bfc15) (which shows 32.7M across all networks) |

- Team-linked wallets hold about **24.8%**, all of it movable.

## 📉 Selling behavior — Do insiders sell into pumps? · 1/10 · ❌ FAIL

| Date | From | To | REQ | ≈ USD | Pump? | Tx |
|---|---|---|---:|---:|---|---|
| 30 Mar 2021 | Team Wallet | Bitfinex 3 | 600,000 | $98k | **Yes, +37.1%** | [0x09d8…cc3](https://etherscan.io/tx/0x09d8a7671f160b01b8cddd7fbdb6daaaa30718df7fd23f98655af691f36edcc3) |
| 12 May 2021 | Team Wallet | Binance 14 | 15,000,000 | $1.69M | No | [0xd892…049](https://etherscan.io/tx/0xd892f52d4764664602385e2ce4f15f3b2acd16ac3035a280c897908f44342049) |
| 23 Jul 2021 | 0x4919…fc15 | Bitfinex 3 | 1,200,000 | — | No | [0x42aa…ddf](https://etherscan.io/tx/0x42aaa3fc89127941a8cc478b8889f83a659ed98efd21135cb47d1de5dd857ddf) |
| 14 Jun 2022 | 0x4919…fc15 | Binance 14 | 5,000,000 | — | No | [0x569c…cd8](https://etherscan.io/tx/0x569cff0bfb95d179337f0421baac8b4a6c8b1977d4e1179b9bfb6e91d234ecd8) |
| 13 Jun 2025 | 0xda5d…ee25 | Kraken 163 | 25,000,000 | $3.46M | No | [0x4117…b1d](https://etherscan.io/tx/0x411735548747b955e7181acd452a581e92d62e585fc4b84dddc550b9604b3d1b) |
| 31 Jul 2025 | 0xda5d…ee25 | Kraken 163 | 19,901,500 | $2.91M | No | [0x7ce7…60b](https://etherscan.io/tx/0x7ce7d4125b1ce635ba9e05ea222883c272cae36bc3e72a4ea04be0706ec0260b) |
| 7 Nov 2025 | 0xda5d…ee25 | Kraken 163 | 1,000,000 | $0.13M | No (+5.7%, Gate) | [0x9288…](https://etherscan.io/tx/0x928874129cee10123b4ea10ba9c75f55805e48c1cceb69276a22da58b2c0133d) |
| 12 Nov 2025 | 0xda5d…ee25 | Kraken 163 | 10,000,000 | $1.27M | No | [0x9db3…33d](https://etherscan.io/tx/0x9db382ada08206585169d1993e39537d831595cadc59848d5199c940ce22633f) |

- The Team Wallet sent tokens straight to an exchange on a pump day, with no disclosure found. Because of that the score is 3, even though the transfer was small and old. The 2025 Kraken transfers (55.9M REQ, about $7.8M) came from a wallet two hops from the Team Wallet. They were not on pump days. **Arkham ([Tier B] Arkham, read 16 Nov 2026 (signed-in account)) labels `0x60a7` and `0xda5d` Coinbase Prime Custody and `0x26cb…` (Etherscan's Kraken 163) a Kraken Deposit**, so this is a custody flow from team funds into a Kraken account, not a direct sale by the Team Wallet; whether it was sold is not shown. The 55.9M total includes the 1M on 7 Nov 2025; `0x60a7` also sent 100k to the same Kraken deposit on 27 Mar 2025. On 14 Nov 2025 a wallet Arkham labels Kraken Hot Wallet sent 17.5M REQ back to the Team Wallet ([tx](https://etherscan.io/tx/0xed62448dbb0663286f2b89780f7819c28cf189b2052489be80912a15816692c7)), so part of the Kraken flow may be a round trip [Unverified]. Exchange names in the table are Etherscan's tags. All linked transactions show status 1 (success).

- **Disclosure quality (16 Nov 2026 rules): silence.** No disclosure was found. **Penalty applied (16 Nov 2026 rules):** a proven pump-day sale with no disclosure fails Selling (ordinary score at most 3) and then loses 2 points, floored at 0: **3 → 1**. Pump days from the daily closes cited in the body (2021 pump days).

- **One-hop amendment (16 Nov 2026):** Still a **proven sale** under the amended rule. (c) holds: the Team Wallet paid Bitfinex directly on a pump day, and no published payroll, grant, market-making or custody reason covers it. Silence stands, so the penalty above is unchanged.

## 📊 Tokenomics & supply · 6/10 · ✅ PASS

- Fixed supply of 1B with no mint function in use. The burn is deflationary but negligible. About 80% is circulating; the overhang is the 18.5% Team Wallet.

## 💧 Liquidity & market · 6/10 · ✅ PASS

- $9.0M of 24h volume (25% of market cap), led by Bithumb and WEEX, with Binance, Coinbase and Kraken pairs.

## 🧑‍💻 Product & development · 6/10 · ✅ PASS

- A live API for invoices, batch, conversion and cross-chain payments, documented in the [protocol fee docs](https://docs.request.network/api-features/protocol-fees).

## 🤝 Adoption & customers · 5/10 · ❌ FAIL

- [Unverified] One secondary source reports 4,034 Request Finance payments worth $23.8M in January 2026. No second source was found.

## 🛡️ Security & audits · 5/10 · ❌ FAIL

- No hacks are listed. DefiLlama shows "0" audits on record, and no current audit was found for the fee contracts.

## ⚖️ Regulatory · 6/10 · ✅ PASS

- Payments run through the payer's own wallet with no custody (according to the pricing page). No enforcement action was found.

## 📅 Catalysts & calendar · 4/10 · ❌ FAIL

- No dated catalysts. The monthly burn is the only recurring event, and it is immaterial.

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | 🔴 Yes: 600k REQ to Bitfinex, 30 Mar 2021 |
| Live mint path | 🟢 None |
| Entity concentration | 🟠 ~24.8% in team-linked wallets |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| Request: Team Wallet | Request team | Etherscan name tag | high | yes | Selling: 600,000 REQ to Bitfinex on 30 Mar 2021 (+37.1% pump day) and later sends |

## 📚 Sources

- [Tier A] Methodology update 16 Nov 2026: no new Arkham lookups; the attribution table uses evidence already cited in this report.
- [Tier A] Etherscan token, wallet and transaction pages (links above). Transaction receipts were checked through the Etherscan API on 16 Nov 2026
- [Tier A] [REQ token page](https://request.network/req-token/), [pricing](https://request.network/pricing/), [protocol fee docs](https://docs.request.network/api-features/protocol-fees)
- [Tier A] CoinGecko `request-network`. Pump days are from Binance REQUSDT daily closes, with REQBTC × BTCUSDT used before the USDT pair was listed
- [Tier A] [DefiLlama protocol record](https://api.llama.fi/protocol/request-network) (no TVL, no fees, no hacks)
- [Tier B] Secondary article on January 2026 Request Finance volume ([Unverified], single source)
- [Tier B] Arkham, read 16 Nov 2026 (signed-in account): Request Network: Team label; Coinbase Prime Custody on `0x60a7` and `0xda5d`; Kraken Deposit on `0x26cb`. Arkham's first transfers page does not reach 2021, so the Bitfinex and Binance claims rest on the Etherscan transactions above. Arkham's page showed the 2025 10M/20M/25M transfers as going to `0x4919`; Etherscan shows they went from `0x4919` to the Team Wallet, and the report follows Etherscan
- [Tier A] Gate REQ/USDT daily close for 2 and 7 Nov 2025

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Team Wallet → Bitfinex on a pump day | [tx 0x09d8…](https://etherscan.io/tx/0x09d8a7671f160b01b8cddd7fbdb6daaaa30718df7fd23f98655af691f36edcc3) | A | 16 Nov 2026 |
| Team Wallet → Binance, 15M | [tx 0xd892…](https://etherscan.io/tx/0xd892f52d4764664602385e2ce4f15f3b2acd16ac3035a280c897908f44342049) | A | 16 Nov 2026 |
| Team Wallet balance 184.8M | [Team Wallet](https://etherscan.io/address/0x0632dcc37b1fabf2cad20538a5390d23c830962e) | A | 16 Nov 2026 |
| 55.9M to a Kraken deposit from team funds held at Coinbase Prime Custody | [0xda5d…ee25](https://etherscan.io/address/0xda5d8915e2d7880eae1a5efa51a8da150871ee25) | A | 16 Nov 2026 |
| Supply 999,416,741 (583,259 burned) | [token page](https://etherscan.io/token/0x8f8221afbb33998d8584a2b05749ba73c37a938a) | A | 16 Nov 2026 |
| Burn is the token's only value link | [REQ token page](https://request.network/req-token/) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Whose Kraken account received the 55.9M, and was it sold?** | Arkham (16 Nov 2026) shows Coinbase Prime Custody → Kraken Deposit but not the account owner. Ask Request Network for its treasury report [Unverified] | Free |
| 2 | **Protocol fee totals** | Ask the foundation for its fee-wallet address and sum the inflows | Free |
| 3 | **Disclosure of the 2021 Team Wallet transfers** | Search the foundation's 2021 blog and governance posts for treasury reports | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.

- Research only. Not investment advice.
