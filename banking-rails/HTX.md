---
ticker: HTX
name: HTX DAO
chain: tron
contract: "TUPM7K8REVzD2UdV4R5fe5M8XbnR2DdoJ6"
overall_score: 4.0
overall_verdict: FAIL
section_scores:
  revenue: 5
  foundation_team: 3
  insider_holdings: 2
  selling_behavior: 5
  tokenomics_supply: 6
  liquidity_market: 2
  product_development: 4
  adoption_customers: 4
  security_audits: 3
  regulatory: 4
  catalysts: 5
gates_failed: []
red_lines:
  hack_exploit: "yes, HTX exchange hot wallets and Heco Bridge, 22 Nov 2023 (~$113M)"
  mint_path_live: "no (fixed 999.99T; quarterly burns to a dead address)"
  team_wallet_to_exchange_during_pump: "none seen on the one pump day (7 Jul 2026), but the reserve is itself labelled an HTX exchange hot wallet and feeds other HTX hot wallets, so sales cannot be seen on-chain"
  treasury_in_single_key_wallets: "yes, 221.6T HTX (22% of max supply) in a 1-of-1 TRON account that Arkham labels an HTX exchange hot wallet (HTX Proof of Reserves)"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "The quarterly burn is funded from the HTX reserve, not from protocol fees, and is a company decision. Holders have no live claim on revenue; the score describes the business, not holder accrual."
pump_day_price_source: "Gate HTX/USDT daily closes"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions: []
price_usd: 0.00000147
price_source: "CoinGecko, 16 Nov 2026 8:34 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### HTX · Overall grade **4.0 / 10 · ❌ FAIL**

**Summary:** HTX is the governance token of HTX DAO, tied to the HTX exchange. Supply is fixed at 999.99T, and every quarter HTX DAO burns HTX equal to 50% of platform revenue. The Q3 2026 burn of [9.39T HTX (~$15.5M) on 15 Oct 2026](https://tronscan.org/#/transaction/90c854fe2d9eaa4c0be0b79089b320cd41efdd8828d500073139c5dddcb6d2a8) is verified on-chain. But the burned tokens come out of a **single-key reserve wallet that still holds 221.6T HTX (22% of max supply)**, not from buys anyone can see on-chain. That reserve is counted as "circulating". And **93% of trading volume is on the HTX exchange itself**.

**🚨 Top warning:** [`TDTo…ivA4`](https://tronscan.org/#/address/TDToUxX8sH4z6moQpK3ZLAN24eupu2ivA4) is a 1-of-1 account (TronGrid `getaccount`: owner threshold 1, one key). It holds **221,588,070,386,676 HTX (≈$326M at spot)**, and every quarterly burn is funded from it ([Q3](https://tronscan.org/#/transaction/b075337c3f1b3a429dd1dfe527325556372c511953cd19c5a4be7b7fd1575d9e), [Q2](https://tronscan.org/#/transaction/5ab3a8702f53d12a809d4c12784709bc34006f0050060418b21aa2f173ba32d6)). The "buyback" cannot be told apart from moving reserve tokens to a dead address. Price discovery happens almost entirely on the issuer's own exchange, and that exchange lost ~$113M to a key compromise in Nov 2023.

**Sections passed: 1 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 5/10 | ❌ FAIL |
| 🏛️ Foundation & team | 3/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 2/10 | ❌ FAIL |
| 📉 Selling behavior | 5/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 6/10 | ✅ PASS |
| 💧 Liquidity & market | 2/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 4/10 | ❌ FAIL |
| 🤝 Adoption & customers | 4/10 | ❌ FAIL |
| 🛡️ Security & audits | 3/10 | ❌ FAIL |
| ⚖️ Regulatory | 4/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 5/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 HTX · HTX DAO · 4.0 / 10 · ❌ FAIL

> **One line:** A verified quarterly burn sitting on top of a single-key reserve that is really an exchange hot wallet, and a self-hosted market.

| 📊 Market (CoinGecko, 16 Nov 2026 8:34 AM MST) | 🔗 On-chain (TRON, 16 Nov 2026) |
|---|---|
| **Price** $0.00000147 · 1y −18.7% | **TRC20** [`TUPM…doJ6`](https://tronscan.org/#/address/TUPM7K8REVzD2UdV4R5fe5M8XbnR2DdoJ6) · max 999.99T |
| **Market cap** $1.31B · rank #59 | **Burn address** [`T9yD…mGkn`](https://tronscan.org/#/address/T9yD14Nj9j7xAB4dbGeiX9h8unkKLxmGkn) holds 111.14T |
| **24h volume** $64.1M, of which $59.6M (93%) on HTX | **Reserve** [`TDTo…ivA4`](https://tronscan.org/#/address/TDToUxX8sH4z6moQpK3ZLAN24eupu2ivA4) holds 221.59T (1-of-1 key) |
| **ATH** $0.00000375 (3 Dec 2024) · now −60.9% | **Circulating** 888.8T (= max − burn address; includes the reserve) |

---

## 💰 Revenue — Does it make money? · 5/10 · ❌ FAIL

| Quarter | HTX burned | Value | Source |
|---|---:|---:|---|
| Q1 2026 | 10.83T | ≈$19.2M | [Tier B ×2] [HTX Square](https://square.htx.com/htx-dao-completes-q1-2026-htx-burn-two-year-supply-shrinks-over-11-as-deflation-accelerates/) · [reserve outflow, 15 Apr 2026](https://tronscan.org/#/transaction/6bbb8391c11b4723e0780225b1dc74afcb9005ff01f749942b390062fe16d3a9) |
| Q2 2026 | 7.47T | ≈$13.6M | [reserve outflow, 15 Jul 2026](https://tronscan.org/#/transaction/5ab3a8702f53d12a809d4c12784709bc34006f0050060418b21aa2f173ba32d6) |
| Q3 2026 | **9,386,358,095,816** | ≈$15.48M | [Tier A] [HTX DAO announcement](https://htxdao-1.gitbook.io/announcement-en/announcement-on-usdhtx-burn-by-htx-dao-for-q3-2026) · [burn tx](https://tronscan.org/#/transaction/90c854fe2d9eaa4c0be0b79089b320cd41efdd8828d500073139c5dddcb6d2a8) |

- The burn equals 50% of platform revenue (HTX DAO's claim), which implies ≈$30M of exchange revenue a quarter. Revenue is not audited.
- **On-chain path (Q3):** reserve [`TDTo…ivA4`](https://tronscan.org/#/address/TDToUxX8sH4z6moQpK3ZLAN24eupu2ivA4) → executor `TUf6…uDCgT` ([tx](https://tronscan.org/#/transaction/b075337c3f1b3a429dd1dfe527325556372c511953cd19c5a4be7b7fd1575d9e)) → dead address ([tx](https://tronscan.org/#/transaction/90c854fe2d9eaa4c0be0b79089b320cd41efdd8828d500073139c5dddcb6d2a8)), all on 15 Oct 2026. No market purchase appears on-chain.

**What it means:** The burn is real (~4.9% of market cap a year) but funded from reserve. **5**.

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** The quarterly burn is funded from the HTX reserve, not from protocol fees, and is a company decision. Holders have no live claim on revenue; the score describes the business, not holder accrual.

## 🏛️ Foundation & team — Who is in charge? · 3/10 · ❌ FAIL

- An "HTX DAO Governance Committee" runs the burns; its members and voting are not disclosed. The token is economically tied to the HTX exchange, which is affiliated with TRON's founder.

## 🪙 Foundation / team holdings — How many coins do they hold? · 2/10 · ❌ FAIL

| Wallet | HTX | % of max | Control |
|---|---:|---:|---|
| [`TDTo…ivA4`](https://tronscan.org/#/address/TDToUxX8sH4z6moQpK3ZLAN24eupu2ivA4) reserve / burn funder | 221,588,070,386,676 | 22.2% | **1-of-1 key** (created Oct 2022). [Arkham](https://intel.arkm.com/explorer/address/TDToUxX8sH4z6moQpK3ZLAN24eupu2ivA4): **HTX: Hot Wallet**, tagged **HTX Proof of Reserves** |
| [`TK86…3h1n`](https://tronscan.org/#/address/TK86Qm97uM848dMk8G7xNbJB7zG1uW3h1n) | 380,924,000,000 | 0.04% | [Arkham](https://intel.arkm.com/explorer/address/TK86Qm97uM848dMk8G7xNbJB7zG1uW3h1n): **HTX: Hot Wallet** (Proof of Reserves). It takes user deposits from HTX deposit addresses, so it is an exchange hot wallet, **not a rewards distributor** as first described |

- **What the label means:** the 221.6T "reserve" sits in a wallet HTX counts in its proof of reserves. Some or all of it may be customer balances rather than DAO treasury; Arkham's page does not say which [Unverified]. Either way, one key at the exchange controls 22% of supply, so the score stays **2**. Arkham's tag list on these HTX wallets also includes "EU Sanctioned" and "UK Sanctioned"; Arkham does not show the basis [Unverified].

*Balances: TronGrid `balanceOf`, 16 Nov 2026. A ~2% (19.9998T) dormant wallet and ~7T of HTX on other chains are reported [Tier B, single source → Unverified].*

## 📉 Selling behavior — Do insiders sell into pumps? · 5/10 · ❌ FAIL

*Gate HTX/USDT daily closes (UTC): **1 pump day** in the last 365 days (7 Jul 2026).*

- The reserve's last 50 transfers (Jan 2025 to Oct 2026) go to burn executors and to `TK86…3h1n`, with no outflow on 7 Jul 2026.
- **Correction ([Tier B] Arkham, read 16 Nov 2026 (signed-in account)):** `TK86…3h1n` is an HTX exchange hot wallet, not a rewards distributor, and the reserve is one too. The reserve sent it 7.48T on 15 Jul 2026 ([tx](https://tronscan.org/#/transaction/5ab3a8702f53d12a809d4c12784709bc34006f0050060418b21aa2f173ba32d6)), 1.2T on 11 Apr 2026 ([tx](https://tronscan.org/#/transaction/d252727ec47fa34c6393090e9c2f6ec18f1f01393b1447908fbe1aa27325ac3a)) and 1.0–1.85T five times from Sep to Dec 2025 (TronGrid). The 15 Jul tokens went on through `TYRK…` and `TKXe…` to the Q2 burn ([7.475T burn](https://tronscan.org/#/transaction/06b58562732cbff13ce6a3b2a0556f6ffefd158b4cc4313968750923c779810d)), but the other transfers stayed inside exchange wallets, and `TK86` mixes them with user deposits. [`TFTW…Ju`](https://intel.arkm.com/explorer/address/TFTWNgDBkQ5wQoP8RXpRznnHvAVV8x5jLu), which executed the 2024–Apr 2026 burns, is also labelled HTX: Hot Wallet. `TUf6…uDCgT` (Q3 executor) is unlabelled.

**What it means:** No reserve outflow on the one pump day, but the holder is the exchange itself. Any sale would happen on HTX's own order book and would not show on-chain, so this is not proven clean. **5** (was 6).

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from Gate HTX/USDT daily closes.

## 📊 Tokenomics & supply · 6/10 · ✅ PASS

- Fixed 999.99T; no mint. 111.14T (11.1%) is already at the dead address.
- Circulating supply (888.8T) includes the 221.6T reserve, so the real float is ~667T.

## 💧 Liquidity & market · 2/10 · ❌ FAIL

- 93% of $64.1M daily volume is on HTX itself (CoinGecko tickers). External price discovery is thin.

## 🧑‍💻 Product & development · 4/10 · ❌ FAIL

- Exchange-utility token; staking launched Mar 2026 (~5%, paid from reserve) [Tier B].

## 🤝 Adoption & customers · 4/10 · ❌ FAIL

- Demand comes from HTX exchange users. No independent user metrics.

## 🛡️ Security & audits · 3/10 · ❌ FAIL

- 22 Nov 2023: compromised keys drained HTX hot wallets and the Heco Bridge (~$113M) [Tier B ×2] ([CNBC](https://www.cnbc.com/2023/11/23/htx-heco-chain-crypto-hack-115-million-stolen-so-far.html) · [CertiK](https://www.certik.com/blog/heco-bridge-exploit)).
- A 1-of-1 key controls 22% of supply.

## ⚖️ Regulatory · 4/10 · ❌ FAIL

- 2026 UK action against HTX and an FCA settlement are reported [Unverified]. Exchange-linked tokens carry the exchange's licensing risk.

## 📅 Catalysts & calendar · 5/10 · ❌ FAIL

| Date | Event |
|---|---|
| 15 Jan 2027 | Q4 2026 burn ([HTX DAO](https://htxdao-1.gitbook.io/announcement-en/announcement-on-usdhtx-burn-by-htx-dao-for-q3-2026)) |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🔴 Nov 2023 exchange / bridge hack |
| Team wallet → exchange during a pump | 🟢 None seen (reserve wallet) |
| Live mint path | 🟢 None |
| Treasury in single-key wallets | 🔴 221.6T HTX, 1-of-1 |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| HTX reserve wallet | HTX exchange | Tronscan | high | yes | None: no outflow on the one pump day |

## 📚 Sources

- [Tier A] Methodology update 16 Nov 2026: no new Arkham lookups; the attribution table uses evidence already cited in this report.
- [Tier A] TronGrid `gettransactioninfobyid`, `getaccount`, `balanceOf` and `/v1/accounts/.../transactions/trc20`, read 16 Nov 2026 ~9:45 AM MST
- [Tier A] [HTX DAO Q3 2026 burn announcement](https://htxdao-1.gitbook.io/announcement-en/announcement-on-usdhtx-burn-by-htx-dao-for-q3-2026)
- [Tier B] [HTX Square Q1 2026](https://square.htx.com/htx-dao-completes-q1-2026-htx-burn-two-year-supply-shrinks-over-11-as-deflation-accelerates/) · [TokenPost](https://www.tokenpost.com/news/business/33284) · [CNBC](https://www.cnbc.com/2023/11/23/htx-heco-chain-crypto-hack-115-million-stolen-so-far.html) · [CertiK](https://www.certik.com/blog/heco-bridge-exploit)
- [Tier A] CoinGecko `htx-dao` (16 Nov 2026 8:34 AM MST); Gate HTX/USDT daily candles
- [Tier B] Arkham, read 16 Nov 2026 (signed-in account): HTX: Hot Wallet (HTX Proof of Reserves) on `TDTo`, `TK86` and `TFTW`; [Black Hole Address](https://intel.arkm.com/explorer/address/T9yD14Nj9j7xAB4dbGeiX9h8unkKLxmGkn) (burn address, 111.14T HTX) on `T9yD`; `TUf6` unlabelled
- [Tier A] TronGrid TRC20 transfers for `TK86`, `TKXe` and the burn address (Q2 2026 burn path)

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Q3 burn 9.39T to the dead address | [tx](https://tronscan.org/#/transaction/90c854fe2d9eaa4c0be0b79089b320cd41efdd8828d500073139c5dddcb6d2a8) | A | 16 Nov 2026 |
| Burn funded by the reserve wallet | [tx](https://tronscan.org/#/transaction/b075337c3f1b3a429dd1dfe527325556372c511953cd19c5a4be7b7fd1575d9e) | A | 16 Nov 2026 |
| Reserve is an HTX hot wallet (Proof of Reserves) | [Arkham](https://intel.arkm.com/explorer/address/TDToUxX8sH4z6moQpK3ZLAN24eupu2ivA4) | B | 16 Nov 2026 |
| Reserve holds 221.6T; 1-of-1 | [address](https://tronscan.org/#/address/TDToUxX8sH4z6moQpK3ZLAN24eupu2ivA4) | A | 16 Nov 2026 |
| Earlier burns from the reserve | [Q1 2026](https://tronscan.org/#/transaction/6bbb8391c11b4723e0780225b1dc74afcb9005ff01f749942b390062fe16d3a9) · [Q4 2025](https://tronscan.org/#/transaction/2b29734a61691628d3e6d150c3cdbaa8fff1bc3631688cc977ceb63a30e33d47) | A | 16 Nov 2026 |
| Nov 2023 hack | [CNBC](https://www.cnbc.com/2023/11/23/htx-heco-chain-crypto-hack-115-million-stolen-so-far.html) · [CertiK](https://www.certik.com/blog/heco-bridge-exploit) | B ×2 | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **How much of the 221.6T is customer money vs DAO treasury** | Arkham (16 Nov 2026) labels it an HTX hot wallet in the proof of reserves. Ask HTX DAO to split the PoR figure for HTX [Unverified] | Free |
| 2 | **Is the burn bought or minted from reserve?** | Ask HTX DAO for market-purchase fills, or check whether the reserve is topped up from exchange wallets | Free |
| 3 | **Whether reserve HTX sent to exchange hot wallets was sold** | `TK86…3h1n` is an exchange hot wallet, so on-chain tracing stops there. Ask HTX DAO for its sales and staking-reward records | Free |
| 4 | **UK regulatory action** | Pull the FCA register / notice | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
