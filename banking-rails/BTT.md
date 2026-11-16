---
ticker: BTT
name: BitTorrent
chain: tron
contract: "TAFjULxiVgT4qWk6UZwjqwZXTSaGaqnVp4"
overall_score: 4.7
overall_verdict: FAIL
section_scores:
  revenue: 5
  foundation_team: 4
  insider_holdings: 2
  selling_behavior: 5
  tokenomics_supply: 8
  liquidity_market: 4
  product_development: 5
  adoption_customers: 5
  security_audits: 6
  regulatory: 3
  catalysts: 6
gates_failed: []
red_lines:
  hack_exploit: none found
  mint_path_live: "no (fixed 990T supply; quarterly revenue buyback-and-burn since Q3 2026)"
  team_wallet_to_exchange_during_pump: "none on the 10 pump days in the last 365 days; but the team wallet sent 212B BTT straight to a Poloniex deposit on 19 Aug 2026 (two days before a pump) and 943.9B to an HTX hot wallet on the 29 Feb 2024 pump day"
  one_hop_sale_status: none_found
  treasury_in_single_key_wallets: "yes, two unnamed 1-of-1 wallets hold 374.6T BTT (37.8%); team wallet 52.46T, also 1-of-1"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "The quarterly buyback-and-burn is a company decision, its BTT came from exchange hot wallets, and funding from revenue is unproven. Holders have no live claim on revenue; the score describes the business, not holder accrual."
pump_day_price_source: "Gate BTT_USDT UTC daily closes, re-run 16 Nov 2026 with scripts/pump_day_test.py (10 of 360 days); the body's earlier count used Gate BTT/USDT daily closes"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions:
  - address: "TH7L3aCyBhGBDgBJZqzotUxAuk8nt9wjqZ"
    label: "6.2T recipient"
    confidence: medium
    independent_corroboration: false
    basis: "Tronscan"
price_usd: 0.00000030696
price_source: "CoinGecko, 16 Nov 2026 8:34 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### BTT · Overall grade **4.7 / 10 · ❌ FAIL**

**Summary:** BTT is the token of BitTorrent (owned by TRON since 2018) and its BTTC chain. Supply is fixed at 990T, with no inflation and all vesting finished except a small release wallet. Since Q3 2026, BitTorrent says 100% of its decentralised-service revenue buys back and burns BTT every quarter. The first burn, [21.62T BTT (~2.2% of supply, ~$7.6M) on 16 Oct 2026](https://tronscan.org/#/transaction/4d9596617780e329bbd4e644ee0dffd780ec4cf3749f324d03eb98157eb04ae5), is verified on-chain. All of the burned BTT came out of exchange wallets: **60% from an HTX hot wallet and the rest via wallets fed the same day by a Poloniex hot wallet and another HTX hot wallet** (Arkham labels). That fits buying on exchanges, but both exchanges are linked to TRON's founder and no fills are published. Ownership is extremely concentrated: two unnamed single-key wallets hold 37.8% and Upbit 27.2%. No insider wallet moved BTT on a pump day in the last year, but the team wallet does deposit straight to exchanges. No hard gate trips, but the average fails.

**🚨 Top warning:** Tronscan's top-holder list, checked balance by balance and key by key on TronGrid (16 Nov 2026), shows [`TWpM…zQo2`](https://tronscan.org/#/address/TWpMnUh9pZS1Mf8yyw9WPiS82WYevKzQo2) with **261.99T (26.5%)** and [`TPyj…Nan5`](https://tronscan.org/#/address/TPyjyZfsYaXStgz2NmAraF1uZcMtkgNan5) with **112.60T (11.4%)**. Both are untagged 1-of-1 accounts, and both were filled by the 2022–23 redenomination contract. The team wallet [`TT2T…kU9N`](https://tronscan.org/#/address/TT2T17KZhoDu47i2E4FWxfG79zdkEWkU9N) holds 52.46T on one key. The Q3 burn was assembled the same day from [`TDTo…ivA4`](https://tronscan.org/#/address/TDToUxX8sH4z6moQpK3ZLAN24eupu2ivA4) ([12.87T](https://tronscan.org/#/transaction/49768eabffb05554935685a3191e63d303c8fd7debe30060dc4e9d8a2ce4eb6d)), which Arkham labels an **HTX Hot Wallet** (HTX Proof of Reserves), plus two wallets fed by Poloniex and HTX hot wallets. The top two trading venues are HTX and Poloniex, both linked to TRON's founder. A 2026 SEC settlement is reported [Unverified].

**Sections passed: 3 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 5/10 | ❌ FAIL |
| 🏛️ Foundation & team | 4/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 2/10 | ❌ FAIL |
| 📉 Selling behavior | 5/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 8/10 | ✅ PASS |
| 💧 Liquidity & market | 4/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 5/10 | ❌ FAIL |
| 🤝 Adoption & customers | 5/10 | ❌ FAIL |
| 🛡️ Security & audits | 6/10 | ✅ PASS |
| ⚖️ Regulatory | 3/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 6/10 | ✅ PASS |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 BTT · BitTorrent · 4.7 / 10 · ❌ FAIL

> **One line:** Fixed supply plus a real, verified revenue burn, held back by heavy ownership concentration, affiliated venues and legal overhang.

| 📊 Market (CoinGecko, 16 Nov 2026 8:34 AM MST) | 🔗 On-chain (TRON, 16 Nov 2026) |
|---|---|
| **Price** $0.00000030696 | **TRC20** [`TAFj…qVp4`](https://tronscan.org/#/token20/TAFjULxiVgT4qWk6UZwjqwZXTSaGaqnVp4) · max 990T |
| **24h / 7d / 30d** 🔴 −1.5% / −14.3% / −13.5% · 1y −30.8% | **Circulating** 968.37T (CoinGecko) |
| **Market cap** $297.1M · **FDV** $297.1M | **Q3 2026 burn** 21,621,611,510,729.6 BTT to the zero address ([tx](https://tronscan.org/#/transaction/4d9596617780e329bbd4e644ee0dffd780ec4cf3749f324d03eb98157eb04ae5)) |
| **24h volume** $13.29M (HTX, Poloniex, Paribu) | **Burn sender** [`TMwu…VeaFg`](https://tronscan.org/#/address/TMwuqc5Wa7YiEzp9FTLwtfdv2bufcVeaFg) |
| **ATH** $0.00000343 (20 Jan 2022) · now −91.1% | **Rank** #126 |

---

## 💰 Revenue — Does it make money? · 5/10 · ❌ FAIL

| Metric | Value | Source |
|---|---:|---|
| Policy | "All revenue generated from BitTorrent's decentralized services will be used to buy back BTT on a quarterly basis" | [Tier A] [BitTorrent announcement, 6 Jul 2026](https://medium.com/@BitTorrent/announcement-on-the-launch-of-btt-buyback-and-burn-8b5a2b6af78d) |
| Q3 2026 burn | **21.62T BTT** on 16 Oct 2026 (≈2.2% of supply) | [Tier A] [TRON tx](https://tronscan.org/#/transaction/4d9596617780e329bbd4e644ee0dffd780ec4cf3749f324d03eb98157eb04ae5) (TronGrid receipt: Transfer to the zero address) |
| Dollar value | ≈$7.6M for the quarter (≈$30M a year if repeated, ≈10% of market cap) | [Tier B ×2] [KuCoin News](https://www.kucoin.com/news/flash/bittorrent-completes-q3-btt-buyback-and-burn-worth-7-6m) · [TokenPost](https://www.tokenpost.com/news/business/35123) |

- **Where the burned BTT came from (TronGrid, Tier A):** the burn wallet [`TMwu…eaFg`](https://tronscan.org/#/address/TMwuqc5Wa7YiEzp9FTLwtfdv2bufcVeaFg) was filled on 16 Oct 2026 by:
  - [12,869.6B](https://tronscan.org/#/transaction/49768eabffb05554935685a3191e63d303c8fd7debe30060dc4e9d8a2ce4eb6d) from [`TDTo…ivA4`](https://tronscan.org/#/address/TDToUxX8sH4z6moQpK3ZLAN24eupu2ivA4), [labelled HTX Hot Wallet / HTX Proof of Reserves by Arkham](https://intel.arkm.com/explorer/address/TDToUxX8sH4z6moQpK3ZLAN24eupu2ivA4): an exchange wallet, not a project reserve (see the HTX report's correction).
  - [5,700.4B](https://tronscan.org/#/transaction/319dc0a2a6cc303c8f562a70e3c551b1ccbe0bc73048bff43a732db946c039c5) from [`TNXp…FnD1`](https://tronscan.org/#/address/TNXpb7aBoxow5X9drTskkjSo1mgKpNFnD1), fed two minutes earlier with [7,040B](https://tronscan.org/#/transaction/c611a137af76d2d20308ec45759cbae38281f7f22006acb1ef22daed3646eead) by the high-volume router [`TWhD…5M2`](https://tronscan.org/#/address/TWhDfwC8QE6pQyiYy248dNor3uphPEw5M2), which Arkham labels [Poloniex Hot Wallet](https://intel.arkm.com/explorer/address/TWhDfwC8QE6pQyiYy248dNor3uphPEw5M2) (a centralized exchange linked to TRON's founder).
  - [3,044.3B](https://tronscan.org/#/transaction/d5d2c9b75c7937ad8c9e10cf28723a5ae381e0a9c66ff9ef07b1bee2cd7e4915) from [`TYRK…CdAr`](https://tronscan.org/#/address/TYRKcXR9ULbvgEvKBSaQ2ANVEw3FiBCdAr), filled three minutes earlier by `TK86…3h1n`, an HTX exchange hot wallet (Arkham; see the HTX report's correction), not a rewards distributor.
- The burn sender [TMwu…eaFg](https://intel.arkm.com/explorer/address/TMwuqc5Wa7YiEzp9FTLwtfdv2bufcVeaFg) itself is unlabelled on Arkham. A month ago it also sent 5.39B BTT, 8.45B WIN and other tokens to one unlabelled wallet.
- Earlier in Aug–Oct 2026, `TDTo…ivA4` received BTT from several wallets, which fits accumulation on HTX. But the order-book purchases themselves can't be seen on-chain. On Arkham, the token contract's largest visible inflows also come from Binance, Bybit and Indodax hot wallets.

**What it means:** The burn is real and the amount checks out. All of the BTT came out of HTX and Poloniex exchange hot wallets, which fits exchange buying, but both venues are affiliated with TRON's founder and no fills are published. Whether it was bought with revenue is unproven. The revenue is not audited, and there is one quarter of history. **5**.

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** The quarterly buyback-and-burn is a company decision, its BTT came from exchange hot wallets, and funding from revenue is unproven. Holders have no live claim on revenue; the score describes the business, not holder accrual.

## 🏛️ Foundation & team — Who is in charge? · 4/10 · ❌ FAIL

- BitTorrent Inc. has been owned by TRON since Jul 2018 [Tier A, BitTorrent]. The Oct 2026 white paper describes BTTC governance by validators, but BTT allocation and release were set by the company.
- Disclosure: burn hashes are published; there is no wallet list or financial statement.

## 🪙 Foundation / team holdings — How many coins do they hold? · 2/10 · ❌ FAIL

| Allocation (white paper) | Share | Release |
|---|---:|---|
| Team & BitTorrent Foundation | 19.0% | Fully released by Dec 2021 |
| TRON Foundation | 20.0% | Fully released by Dec 2021 |
| BitTorrent Ecosystem | 19.9% | Tapering, reported through 2029 |
| Seed / Private / Public | 17.0% | Released in 2019 |

*Source: [Tier A] [BitTorrent white paper, Oct 2026](https://www.bittorrent.com/btt/btt-docs/BitTorrent_(BTT)_White_Paper_2026_Oct_EN.pdf), Tables 7-1 and 7-2.*

**Current top holders** (Tronscan holder list; every balance re-read with TronGrid `balanceOf`, and key setup read with `getaccount`, 16 Nov 2026):

| Wallet | BTT | % of 990T | Keys | Note |
|---|---:|---:|---|---|
| [`TASU…NKot`](https://tronscan.org/#/address/TASUAUKXCqvwYjesEWv22pFjRsCeF4NKot) | 269.66T | 27.2% | 1-of-1 | Tagged Upbit hot wallet |
| [`TWpM…zQo2`](https://tronscan.org/#/address/TWpMnUh9pZS1Mf8yyw9WPiS82WYevKzQo2) | 261.99T | 26.5% | **1-of-1** | Untagged ([Arkham: whale tags only](https://intel.arkm.com/explorer/address/TWpMnUh9pZS1Mf8yyw9WPiS82WYevKzQo2); repeated USDT funding from a Wintermute hot wallet). 268T in from the redenomination contract (Aug 2023); last outflow [6.2T on 18 Jan 2026](https://tronscan.org/#/transaction/294077f0094103f0c6a76c561cb395f0be05e63622f2e514647690da8d7dfe68) |
| [`TPyj…Nan5`](https://tronscan.org/#/address/TPyjyZfsYaXStgz2NmAraF1uZcMtkgNan5) | 112.60T | 11.4% | **1-of-1** | Untagged ([Arkham: whale tags only](https://intel.arkm.com/explorer/address/TPyjyZfsYaXStgz2NmAraF1uZcMtkgNan5)); no outflow since Jan 2025 |
| [`TT2T…kU9N`](https://tronscan.org/#/address/TT2T17KZhoDu47i2E4FWxfG79zdkEWkU9N) | 52.46T | 5.3% | **1-of-1** | Team wallet ([Arkham: unlabelled, whale tags](https://intel.arkm.com/explorer/address/TT2T17KZhoDu47i2E4FWxfG79zdkEWkU9N)); regular 40–900B payouts |
| [`TF1F…NCt5`](https://tronscan.org/#/address/TF1FYTupPzcCvXRX8vEKQi5HBPzV1fNCt5) | 3.94T | 0.4% | 1-of-1 | Release wallet; [last outflow 30 Jan 2025](https://tronscan.org/#/transaction/fe9618a3b86cce03f0dad8ec3028781688adefa2f59562c3d7bc9136e500f1c3) |

- Arkham ([Tier B] Arkham, read 16 Nov 2026 (signed-in account)) gives none of the four non-exchange wallets an entity label; it tags `TF1F…NCt5` as first-funded by the team wallet. 374.6T BTT (37.8%) sits in two untagged single-key wallets. Ownership is not published, but both were filled by the issuer's redenomination contract, which fits the TRON Foundation and BitTorrent allocations (39% combined) [inference].

## 📉 Selling behavior — Do insiders sell into pumps? · 5/10 · ❌ FAIL

*Gate BTT/USDT daily closes (UTC): 10 of the last 365 days were pump days.*

- **Pump days (365d):** 5–6 Jan, 15 Mar, 21–23 Aug, 21–22 Sep and 24–25 Sep 2026.
- **Result:** none of the five non-exchange wallets above, nor the 6.2T recipient [`TH7L…wjqZ`](https://tronscan.org/#/address/TH7L3aCyBhGBDgBJZqzotUxAuk8nt9wjqZ), sent BTT on any pump day in the last 365 days (full TronGrid TRC20 histories).
  - The nearest move was the team wallet's [212B on 19 Aug 2026](https://tronscan.org/#/transaction/3b0504d74e48ebb7088a8d96b42fe33e2cc35a60803f1f4899c457c4d83ad831) (+5.1%, not a pump day), two days before the 21 Aug pump. **Correction:** the recipient `TGAo…2Hvr` is a **Poloniex deposit address** (Arkham), so this was a direct team-wallet deposit to an exchange, and the "high-volume router" it fed is the Poloniex Hot Wallet.
  - **Correction:** `TH7L…jqZ` forwarded [820B on 22 Jan 2026](https://tronscan.org/#/transaction/84bd6a998fc97bc315468cebca7217bdb8158d1d7e6da429d73f693fcca950c2) (−4.4%) to a **Binance deposit address**, not an untagged wallet, then 30.5B on 18 Apr 2026 (−1.3%) and 73.9B on 6 Jul 2026 (+2.1%) to a **Bitget deposit address** ([Arkham](https://intel.arkm.com/explorer/address/TH7L3aCyBhGBDgBJZqzotUxAuk8nt9wjqZ)). So BTT from the 26.5% wallet reaches exchanges through this wallet, though not on pump days.
  - The team payout address [TVFB…zqkp](https://intel.arkm.com/explorer/address/TVFBd9TBHkk4L6FEfjQ5Fa1XABTfEdzqkp) is unlabelled. Its BTT payouts (Jan 2025–Jul 2026) went to unlabelled wallets, none on a pump day, and it sends TRX and USDT to Poloniex deposits.
- **Older history (correction):** the team wallet sent [943.9B to `TDTo…ivA4` on 29 Feb 2024](https://tronscan.org/#/transaction/f7689e443091c6d96fe57d6ceeb943f7f455eac8dbef9390e2f2cac155fc21a3), a pump day (+14.0%). Arkham labels `TDTo` an HTX Hot Wallet, so this was a team-wallet deposit to an exchange on a pump day, not an intra-group move. It falls outside the 365-day window, so it doesn't trip the gate.
- **Re-score:** no pump-day sale in 365 days, so the gate holds. But the team wallet deposits straight to exchanges, did so on a 2024 pump day, and the 26.5% holder's BTT reaches Binance and Bitget. Not clean → **5** (was 6).

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from Gate BTT_USDT UTC daily closes, re-run 16 Nov 2026 with scripts/pump_day_test.py (10 of 360 days); the body's earlier count used Gate BTT/USDT daily closes.

## 📊 Tokenomics & supply · 8/10 · ✅ PASS

- Fixed 990T; no mint. Staking rewards (~6.9%) come from an already-circulating pot [Tier B].
- Quarterly burns cut supply ~2.2% a quarter at the current revenue rate.

## 💧 Liquidity & market · 4/10 · ❌ FAIL

- $13.3M of 24h volume on a $297M cap (4.5%). Top venues are HTX and Poloniex (founder-affiliated), then Paribu. Korean exchanges hold about a third of supply [Tier B].
- −91% from ATH, −31% in a year: much less damage than its peers.

## 🧑‍💻 Product & development · 5/10 · ❌ FAIL

- BTTC 2.0, BTTInferGrid (AI inference marketplace) and BitTorrent apps (Neo PRO for Mac, Nov 2026) [Tier A white paper; Tier B news].

## 🤝 Adoption & customers · 5/10 · ❌ FAIL

- BitTorrent apps reach ~40.7M people with 8.65M daily users (company claim, Tier B). How much decentralised-service revenue they produce is not broken out.

## 🛡️ Security & audits · 6/10 · ✅ PASS

- No exploit of BTT or BTTC found in this pass.

## ⚖️ Regulatory · 3/10 · ❌ FAIL

- The SEC sued TRON's founder and affiliated entities in Mar 2023, alleging BTT and TRX were unregistered securities. A $10M settlement in Mar 2026 is reported [Tier B, single source → Unverified].
- The affiliated exchange HTX faced UK action in 2026 [Unverified].

## 📅 Catalysts & calendar · 6/10 · ✅ PASS

| Date | Event |
|---|---|
| Mid-Jan 2027 | Q4 2026 buyback-and-burn report (est. ~21.4T BTT, Tier B) |
| Quarterly | Further burns |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | 🟡 None on the 10 pump days (365d); team wallet → HTX hot wallet on the 29 Feb 2024 pump day |
| Live mint path | 🟢 None (fixed supply) |
| Treasury in single-key wallets | 🔴 37.8% in two 1-of-1 wallets; team 5.3% 1-of-1 |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| [`TH7L…wjqZ`](https://tronscan.org/#/address/TH7L3aCyBhGBDgBJZqzotUxAuk8nt9wjqZ) | 6.2T recipient | Tronscan | medium | no | None: no BTT sent on a pump day |

## 📚 Sources

- [Tier A] Methodology update 16 Nov 2026: no new Arkham lookups; the attribution table uses evidence already cited in this report.
- [Tier A] TronGrid `gettransactioninfobyid` for the Q3 burn, read 16 Nov 2026 ~9:35 AM MST
- [Tier A] [BitTorrent white paper (Oct 2026)](https://www.bittorrent.com/btt/btt-docs/BitTorrent_(BTT)_White_Paper_2026_Oct_EN.pdf) · [Buyback announcement](https://medium.com/@BitTorrent/announcement-on-the-launch-of-btt-buyback-and-burn-8b5a2b6af78d)
- [Tier B] [KuCoin News](https://www.kucoin.com/news/flash/bittorrent-completes-q3-btt-buyback-and-burn-worth-7-6m) · [TokenPost](https://www.tokenpost.com/news/business/35123) · [MrNasDog supply research](https://mrnasdog.com/research/btt)
- [Tier A] CoinGecko `bittorrent` (16 Nov 2026 8:34 AM MST); Gate BTT/USDT daily candles
- [Tier A] TronGrid `balanceOf`, `getaccount` and full TRC20 histories for the top holders and the burn path; Tronscan top-holder list (read 16 Nov 2026 ~10:05 AM MST)
- [Tier B] Arkham, read 16 Nov 2026 (signed-in account): HTX Hot Wallet on TDTo; Poloniex Hot Wallet on TWhD; Poloniex, Binance and Bitget deposit labels; no entity label on the top wallets, the team wallet, the payout address or the burn sender
- [Unverified] SEC settlement terms; who owns the two untagged top wallets

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| 21.62T BTT burned 16 Oct 2026 | [tx](https://tronscan.org/#/transaction/4d9596617780e329bbd4e644ee0dffd780ec4cf3749f324d03eb98157eb04ae5) | A | 16 Nov 2026 |
| 100% of decentralised-service revenue to buybacks | [announcement](https://medium.com/@BitTorrent/announcement-on-the-launch-of-btt-buyback-and-burn-8b5a2b6af78d) | A | 16 Nov 2026 |
| Allocation and release schedule | [white paper](https://www.bittorrent.com/btt/btt-docs/BitTorrent_(BTT)_White_Paper_2026_Oct_EN.pdf) | A | 16 Nov 2026 |
| 37.8% in two 1-of-1 wallets; team 52.46T | [TWpM…zQo2](https://tronscan.org/#/address/TWpMnUh9pZS1Mf8yyw9WPiS82WYevKzQo2) · [TPyj…gNan5](https://tronscan.org/#/address/TPyjyZfsYaXStgz2NmAraF1uZcMtkgNan5) · [TT2T…MgU9N](https://tronscan.org/#/address/TT2T17KZhoDu47i2E4FWxfG79zdkEWkU9N) | A | 16 Nov 2026 |
| 60% of Q3 burn supplied by an HTX hot wallet | [tx](https://tronscan.org/#/transaction/49768eabffb05554935685a3191e63d303c8fd7debe30060dc4e9d8a2ce4eb6d) | A | 16 Nov 2026 |
| ~$7.6M burn value | [KuCoin](https://www.kucoin.com/news/flash/bittorrent-completes-q3-btt-buyback-and-burn-worth-7-6m) · [TokenPost](https://www.tokenpost.com/news/business/35123) | B ×2 | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Who owns the two untagged 1-of-1 wallets (26.5% and 11.4%)** | Arkham (16 Nov 2026) gives them whale tags only. Ask BitTorrent / TRON DAO to publish allocation wallets | Free |
| 2 | **Where the team payouts end up** | `TVFB…zqkp` is unlabelled; trace its BTT recipients (`TSLL…`, `TGTz…`, `TFMA…`, `TUMP…`) to exchanges | Free |
| 3 | **Was the burn bought with revenue?** | Ask BitTorrent for buyback fills on HTX and Poloniex | Free |
| 4 | **SEC settlement terms** | Pull the SEC litigation release or court docket | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
