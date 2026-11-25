---
ticker: JST
name: JUST
chain: tron
contract: "TCFLL5dx5ZJdKnWuesXxi1VPwjLVmWZZy9"
overall_score: 5.5
overall_verdict: FAIL
section_scores:
  revenue: 5
  foundation_team: 5
  insider_holdings: 5
  selling_behavior: 5
  tokenomics_supply: 7
  liquidity_market: 6
  product_development: 7
  adoption_customers: 7
  security_audits: 5
  regulatory: 4
  catalysts: 6
gates_failed: []
red_lines:
  hack_exploit: none found in this pass
  mint_path_live: "not checked on the contract; docs give a fixed 9.9B max supply"
  team_wallet_to_exchange_during_pump: "none found: the burn wallet (TZJV…) sends only to the black hole and JUST proposal contracts; the wallet that funded the burns (TFTW…) is an HTX hot wallet per Arkham, so its HTX transfers are exchange-internal"
  one_hop_sale_status: none_found
  buyback_source: "first round (19 Oct 2025): 600M JST from unlabelled whale TPyjyZ… deposited to HTX nine minutes before withdrawal and burn; owner [Unverified]"
  revenue_claims_mismatch: "self-reported net income far above DefiLlama protocol revenue; claimed cumulative burn exceeds black-hole balance by ~106.7M"
  future_unlocks_cut: "n/a, fully unlocked"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "The buyback-and-burn is large and executed, but the buying runs through HTX rather than an automatic on-chain mechanism, and its funding cannot be matched to protocol revenue (DefiLlama shows $0.79M for the year). Holders have no live claim on revenue; the score describes the business, not holder accrual."
pump_day_price_source: "Gate JST_USDT UTC daily closes, re-run 16 Nov 2026 with scripts/pump_day_test.py (29 of 360 days); the body's earlier count used CoinGecko daily closes"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions: []
price_usd: 0.143425
price_source: "CoinGecko, 16 Nov 2026 6:00 AM MST"
last_updated: 2026-11-17
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### JST · Overall grade **5.5 / 10 · ❌ FAIL**

**Summary:** JST is the governance token of the JUST DeFi suite on Tron, whose main product, JustLend DAO, holds about **$5.97B** in deposits (DefiLlama). Since Oct 2025 a buyback-and-burn has sent **1.775B JST** (≈ 17.9% of the 9.9B max) to the Tron black hole in five quarterly rounds, which is real and on-chain. Arkham labels the wallet that supplied the first three burns as an **HTX hot wallet**, so that JST came off the exchange, consistent with buying, and the earlier "insider deposits to HTX" flag is withdrawn (they were HTX-internal moves). Two problems remain: the self-reported income behind the burns (e.g. $9.28M net income in Q3 2026) is far above DefiLlama's protocol revenue ($0.79M for the whole last year), and the first round's 600M JST arrived at HTX from one unlabelled whale nine minutes before it was withdrawn and burned. Supply is fully unlocked, and liquidity is good ($20.2M a day), but 58% of volume is on HTX and Poloniex.

**🚨 Top warning (yellow):** the buyback's money trail does not match outside data. JUST reports $9.28M of Q3 2026 net income ([announcement](https://support.justlend.org/hc/en-us/articles/63334976912025-Announcement-on-Completion-of-the-5th-JST-Buyback-and-Burn)), but DefiLlama shows **$0.79M** of JustLend protocol revenue for the entire last year ([DefiLlama](https://defillama.com/protocol/justlend)), and the claimed cumulative burn (1,881,973,007 JST) is **≈ 106.7M more** than the black hole holds ([`T9yD14…uWwb`](https://tronscan.org/#/address/T9yD14Nj9j7xAB4dbGeiX9h8unkKHxuWwb)). The first and largest round also looks like a single pre-arranged block, not open-market buying: on 19 Oct 2025 the unlabelled whale [`TPyjyZ…Nan5`](https://tronscan.org/#/address/TPyjyZfsYaXStgz2NmAraF1uZcMtkgNan5) (660.9M JST, ≈ 1.88B TRX) sent [600M JST to HTX deposit TMVMe… at 5:50 AM MST](https://tronscan.org/#/transaction/38262da44768119ea440220e4a48c7a78eef22b0ed35d12febbd6a9d50d2bea9), HTX moved it to its hot wallet [`TFTWNg…5jLu`](https://tronscan.org/#/address/TFTWNgDBkQ5wQoP8RXpRznnHvAVV8x5jLu) [nine minutes later](https://tronscan.org/#/transaction/859f3133a07a6d2095a467dfd23c9885d9c8fe11cc3800ba89681ce7a082055d), and 559.9M went to the burn wallet [at 6:02 AM MST](https://tronscan.org/#/transaction/563506a06877da773461a3c7870b64ed1aadc7b1c6cde0cb629e9a45a4e43826) and was [burned at 6:08 AM MST](https://tronscan.org/#/transaction/471bef34bb013dad46f9f132cd1fbca6bd3de584c54b7190718acd5949d4453d). Who owns the whale is not public [Unverified]. (Exchange labels: [Tier B] Arkham, read 16 Nov 2026 ~6:10 AM MST (signed-in account).)

**Sections passed: 5 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 5/10 | ❌ FAIL |
| 🏛️ Foundation & team | 5/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 5/10 | ❌ FAIL |
| 📉 Selling behavior | 5/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 7/10 | ✅ PASS |
| 💧 Liquidity & market | 6/10 | ✅ PASS |
| 🧑‍💻 Product & development | 7/10 | ✅ PASS |
| 🤝 Adoption & customers | 7/10 | ✅ PASS |
| 🛡️ Security & audits | 5/10 | ❌ FAIL |
| ⚖️ Regulatory | 4/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 6/10 | ✅ PASS |

*Pass = 6 or more out of 10. Full details for every section follow below.*

> **Re-scored 16 Nov 2026 after the Arkham pass:** Selling behavior **3 → 5** (the hard-gate fail is lifted), overall **5.2 → 5.5**. Reason: Arkham labels the burn-funding wallet [`TFTWNg…5jLu`](https://tronscan.org/#/address/TFTWNgDBkQ5wQoP8RXpRznnHvAVV8x5jLu) as an HTX hot wallet, so its 774.9M of transfers to other HTX hot wallets were exchange-internal, not a JUST wallet depositing to an exchange. Still a FAIL on the overall average.

---


# 🪪 JST · JUST · 5.5 / 10 · ❌ FAIL

> **One line:** JST is the governance token of the JUST DeFi suite on Tron, whose main product, JustLend DAO, holds about **$5.97B** in deposits (DefiLlama). Since Oct 2025 a buyback-and-burn has sent **1.775B JST** (≈ 17.9% of the 9.9B max) to the Tron black hole in five quarterly rounds, which is real and on-chain. Arkham labels the wallet that supplied the first three burns as an **HTX hot wallet**, so that JST came off the exchange, consistent with buying, and the earlier "insider deposits to HTX" flag is withdrawn (they were HTX-internal moves). Two problems remain: the self-reported income behind the burns (e.g. $9.28M net income in Q3 2026) is far above DefiLlama's protocol revenue ($0.79M for the whole last year), and the first round's 600M JST arrived at HTX from one unlabelled whale nine minutes before it was withdrawn and burned. Supply is fully unlocked, and liquidity is good ($20.2M a day), but 58% of volume is on HTX and Poloniex.

| 📊 Market (CoinGecko, 16 Nov 2026 6:00 AM MST) | 🔗 On-chain (Tronscan / TronGrid, 16 Nov 2026) |
|---|---|
| **Price** $0.1434 | **Token** TRC-20 [`TCFLL5dx5ZJdKnWuesXxi1VPwjLVmWZZy9`](https://tronscan.org/#/address/TCFLL5dx5ZJdKnWuesXxi1VPwjLVmWZZy9) |
| **24h / 7d / 30d** 🔴 −1.2% / −1.2% / 🟢 +6.4% · 1y +294% | **Burned** [`Black hole T9yD…uHwb`](https://tronscan.org/#/address/T9yD14Nj9j7xAB4dbGeiX9h8unkKHxuWwb): **1,775,315,545 JST** ([holders list](https://tronscan.org/#/token20/TCFLL5dx5ZJdKnWuesXxi1VPwjLVmWZZy9/holders)) |
| **Market cap** $1.150B (circulating 8.018B) | **Burn wallet** [`TZJVQu…pEag`](https://tronscan.org/#/address/TZJVQuU3CJqBScwoxhRtkxQ7JjsNNrpEag) (Tronscan tag "JUST Treasury"; unlabelled on Arkham): 500.0M JST, not yet burned |
| **24h volume** $20.2M (HTX 36.2%, Poloniex 22.1%, Binance 7.7%) | **Governance lock (WJST)** [`TXk9Ln…4ZD6`](https://tronscan.org/#/address/TXk9LnTnLN7oH96H3sKxJayMxLxR9M4ZD6): 700.0M |
| **ATH** $0.1933 (4 Apr 2021) · now −25.8% | **Pump days** in the last 365 (CoinGecko closes): **29** |

---

## 💰 Revenue — Does it make money? · 5/10 · ❌ FAIL

| Metric | Value | Source |
|---|---:|---|
| JustLend fees, last 365 days | **$15.52M** | [Tier A] [DefiLlama JustLend](https://defillama.com/protocol/justlend), API read 16 Nov 2026 |
| JustLend protocol revenue, last 365 days / last 30 days | **$0.79M / $0.30M** | same |
| DefiLlama holders revenue | $0 (buyback not tracked) | same |
| Self-reported Q3 2026 net income used for the 5th burn | **$9,280,216**, plus $10,340,249 from a historical allocation; 170,723,144 JST burned (≈ $23.53M) | [Tier B] [5th buyback announcement](https://support.justlend.org/hc/en-us/articles/63334976912025-Announcement-on-Completion-of-the-5th-JST-Buyback-and-Burn) |
| Buyback rule | All JustLend DAO net income, plus USDD income above $10M, buys and burns JST (approved 21 Oct 2025) | [Tier B] [JustLend docs: tokenomics](https://docs.justlend.org/governance/tokenomics/) |
| Burns on-chain | Five rounds, **1,775.3M JST** total (table below) | [Tier A] Tronscan |
| Where the burned JST came from | Rounds 1–3 (1,356M): withdrawn from **HTX hot wallet** [`TFTWNg…5jLu`](https://tronscan.org/#/address/TFTWNgDBkQ5wQoP8RXpRznnHvAVV8x5jLu) minutes before each burn | [Tier A] transfers · [Tier B] Arkham, read 16 Nov 2026 ~6:10 AM MST (signed-in account) [Arkham](https://intel.arkm.com/explorer/address/TFTWNgDBkQ5wQoP8RXpRznnHvAVV8x5jLu) |

| Burn date (UTC) | JST burned | Burn tx (→ black hole) | Funded by |
|---|---:|---|---|
| 19 Oct 2025 | 559,890,000 (rounded) | [471bef34bb…](https://tronscan.org/#/transaction/471bef34bb013dad46f9f132cd1fbca6bd3de584c54b7190718acd5949d4453d) | [HTX hot wallet TFTW…](https://tronscan.org/#/transaction/563506a06877da773461a3c7870b64ed1aadc7b1c6cde0cb629e9a45a4e43826) |
| 14 Jan 2026 | 525,000,000 | [5c7cd68483…](https://tronscan.org/#/transaction/5c7cd68483f1d32aebe1084b3dc9a6b742092bde1153db72b79a866617c14314) | [HTX hot wallet TFTW…](https://tronscan.org/#/transaction/c8a8a84ee337161d427a51549bb9a4489466a8e020547aa3bd85a3c5c3da7265) |
| 15 Apr 2026 | 271,340,000 (rounded) | [1e9f55e8ff…](https://tronscan.org/#/transaction/1e9f55e8ffa8033c238f34f5ebe57f544d424f7016810dd0f1ba792392eeb1e5) | [HTX hot wallet TFTW…](https://tronscan.org/#/transaction/8b7d2a08a0b37bb2648c003c06edf00ac6de2098a8f569444895722ae40db2c0) |
| 17 Jul 2026 | 248,360,000 (rounded) | [59c47582de…](https://tronscan.org/#/transaction/59c47582de15ed1028ca29fe860a09a8149d463ce553432506b95d924256341f) | other wallets (not HTX-labelled in this pass) |
| 16 Oct 2026 | 170,723,144 | [0cb7d79bd0…](https://tronscan.org/#/transaction/0cb7d79bd0511ed98b061edb586bf36a868cb510158071ca6fbe3dc56ff86f93) | other wallets (not HTX-labelled in this pass) |

**What it means:** The burns are real and large, about 17.9% of max supply in one year, and Arkham's HTX label on the funding wallet fits buying on HTX. But the money behind them cannot be matched to independent numbers: DefiLlama shows $0.79M of protocol revenue for the whole year, while JUST reports $9.28M of net income for one quarter. The announcement also claims a cumulative 1,881,973,007 JST burned (19.01%), about **106.7M more** than the black hole holds. Part of each burn came from a one-off "historical allocation", and round 1 was one 600M block from a single whale (see Selling). Score **5** (unchanged).

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** The buyback-and-burn is large and executed, but the buying runs through HTX rather than an automatic on-chain mechanism, and its funding cannot be matched to protocol revenue (DefiLlama shows $0.79M for the year). Holders have no live claim on revenue; the score describes the business, not holder accrual.

## 🏛️ Foundation & team — Who is in charge? · 5/10 · ❌ FAIL

| Item | Finding | Source |
|---|---|---|
| Governance | JustLend DAO: JST holders vote with WJST (700M JST locked in the WJST contract) | [Tier A] [`WJST contract`](https://tronscan.org/#/address/TXk9LnTnLN7oH96H3sKxJayMxLxR9M4ZD6) · [Tier B] [docs](https://docs.justlend.org/governance/tokenomics/) |
| Burn wallet | [`TZJVQu…pEag`](https://tronscan.org/#/address/TZJVQuU3CJqBScwoxhRtkxQ7JjsNNrpEag) is tagged "JUST Treasury" by Tronscan; Arkham shows it **unlabelled** (JST and STRX whale tags only). It has also moved 200M JST at a time through four contracts Arkham names as **JUST governance proposals**: [ProposalUpdateEthbCf45Rf](https://intel.arkm.com/explorer/address/TBbdnCLz5x9U9WMj9RvXxUGoPVJ5MFpmrD), [ProposalUpgradeComptroller](https://intel.arkm.com/explorer/address/TLRp7D7BamAbcwhGLzuBNCshpngyTpiUVW), [ProposalAddUMarket](https://intel.arkm.com/explorer/address/TNRzQV5ZigUD2y5Ko7MfAqjU7dFcWFMiqN), [ProposalAddHtxMarket](https://intel.arkm.com/explorer/address/TWhSr8MnZ3KdMPH9qosLqHTjpgZxHfRHgg) | [Tier A] transfers · [Tier B] Tronscan tag · [Tier B] Arkham, read 16 Nov 2026 ~6:10 AM MST (signed-in account) |
| Team / founders | The JUST ecosystem is part of the TRON ecosystem; team members and wallets are not published | [Tier B] [whitepaper](https://just.network/docs/white_paper_en.pdf) |

**What it means:** Governance exists and is used: the burn wallet itself votes 200M JST through proposal contracts (including one named `ProposalAddHtxMarket`). But the wallet is not publicly claimed by JUST, so the same unnamed holder both runs the burns and casts large votes. Score **5**.

## 🪙 Foundation / team holdings — How many coins do they hold? · 5/10 · ❌ FAIL

- **Original split** (whitepaper): Ecosystem 30%, Strategic partners 26%, Team 19%, Seed 11%, Airdrop 10%, LaunchBase public sale 4%. Team tokens finished vesting by Apr 2022 ([Tier B] [whitepaper](https://just.network/docs/white_paper_en.pdf); [docs](https://docs.justlend.org/governance/tokenomics/)).
- **Burn wallet** [`TZJVQu…pEag`](https://tronscan.org/#/address/TZJVQuU3CJqBScwoxhRtkxQ7JjsNNrpEag) holds **500.0M JST** (≈ 6.2% of circulating) that has not been burned. 300M arrived from HTX hot wallet [`TFTWNg…5jLu`](https://tronscan.org/#/address/TFTWNgDBkQ5wQoP8RXpRznnHvAVV8x5jLu) on 15 Apr 2026 ([066f6b9b0c…](https://tronscan.org/#/transaction/066f6b9b0c7cbab2c6e55784d42dcca6077282d778ae59175be3c0c881deb805)). The 200M lots it sent out and got back (May–Aug 2026) went through JUST proposal contracts, i.e. governance votes, not sales ([Tier B] Arkham, read 16 Nov 2026 ~6:10 AM MST (signed-in account)).
- **Largest unlabelled holders** ([Tronscan holders](https://tronscan.org/#/token20/TCFLL5dx5ZJdKnWuesXxi1VPwjLVmWZZy9/holders)), all **unlabelled on Arkham** too: [`TPyjyZ…Nan5`](https://tronscan.org/#/address/TPyjyZfsYaXStgz2NmAraF1uZcMtkgNan5) 660.9M (also ≈ 1.88B TRX) [Arkham](https://intel.arkm.com/explorer/address/TPyjyZfsYaXStgz2NmAraF1uZcMtkgNan5), [`TSFUtq…T6h9`](https://tronscan.org/#/address/TSFUtqxZyADSmkgLbpoRwyDinr3BWuT6h9) 400.0M [Arkham](https://intel.arkm.com/explorer/address/TSFUtqxZyADSmkgLbpoRwyDinr3BWuT6h9) (votes through JUST proposal contracts `ProposalAddWbtcMarket` and `ProposalAddRecorder`), [`TT2T17…kU9N`](https://tronscan.org/#/address/TT2T17KZhoDu47i2E4FWxfG79zdkEWkU9N) 386.1M (also ≈ 1.95B TRX) [Arkham](https://intel.arkm.com/explorer/address/TT2T17KZhoDu47i2E4FWxfG79zdkEWkU9N). Together ≈ 18% of circulating. Owners not published [Unverified].

**What it means:** About a quarter of circulating supply sits in a few unlabelled wallets plus the burn wallet, and two of them are active governance voters. Score **5** (unchanged).

## 📉 Selling behavior — Do insiders sell into pumps? · 5/10 · ❌ FAIL

**Method:** TronGrid TRC-20 transfers for the burn wallet, the wallets that funded it, and the four largest unlabelled holders. Exchange wallets: Tronscan labels in the JST holder list (Binance, Upbit, Bithumb, OKX) plus **Arkham** labels for HTX ([Tier B] Arkham, read 16 Nov 2026 ~6:10 AM MST (signed-in account)).

| Flow | JST | Pump-day part | Evidence |
|---|---:|---:|---|
| Burn wallet [`TZJVQu…pEag`](https://tronscan.org/#/address/TZJVQuU3CJqBScwoxhRtkxQ7JjsNNrpEag) → exchanges | **0** | 0 | TronGrid; outflows go only to the black hole and JUST proposal contracts |
| HTX hot wallet [`TFTWNg…5jLu`](https://tronscan.org/#/address/TFTWNgDBkQ5wQoP8RXpRznnHvAVV8x5jLu) → burn wallet (rounds 1–3) | 1,656.2M in 5 transfers | n/a | [19 Oct 2025](https://tronscan.org/#/transaction/563506a06877da773461a3c7870b64ed1aadc7b1c6cde0cb629e9a45a4e43826), [14 Jan 2026](https://tronscan.org/#/transaction/c8a8a84ee337161d427a51549bb9a4489466a8e020547aa3bd85a3c5c3da7265), [15 Apr 2026](https://tronscan.org/#/transaction/8b7d2a08a0b37bb2648c003c06edf00ac6de2098a8f569444895722ae40db2c0) · [Arkham: HTX Hot Wallet](https://intel.arkm.com/explorer/address/TFTWNgDBkQ5wQoP8RXpRznnHvAVV8x5jLu) |
| HTX hot wallet [`TFTWNg…5jLu`](https://tronscan.org/#/address/TFTWNgDBkQ5wQoP8RXpRznnHvAVV8x5jLu) ↔ HTX hot wallets [`TDToUx…ivA4`](https://tronscan.org/#/address/TDToUxX8sH4z6moQpK3ZLAN24eupu2ivA4) and [`TK86Qm…3h1n`](https://tronscan.org/#/address/TK86Qm97uM848dMk8G7xNbJB7zG1uW3h1n) | 774.9M out / 630.8M back; 399.0M out / 357.6M back | (internal) | [Arkham: HTX Hot Wallet (TDToU)](https://intel.arkm.com/explorer/address/TDToUxX8sH4z6moQpK3ZLAN24eupu2ivA4) · [Arkham: HTX Hot Wallet (TK86Q)](https://intel.arkm.com/explorer/address/TK86Qm97uM848dMk8G7xNbJB7zG1uW3h1n). **Withdrawn:** these were treated as insider deposits in the first draft |
| Unlabelled whale [`TPyjyZ…Nan5`](https://tronscan.org/#/address/TPyjyZfsYaXStgz2NmAraF1uZcMtkgNan5) → HTX deposit [`TMVMeC…Jz4E`](https://tronscan.org/#/address/TMVMeCpcR5hh1WG36Yih68t3GuChABJz4E) → HTX hot wallet → burn | 600M, 19 Oct 2025 | 0 (not a pump day) | [deposit 12:50 UTC](https://tronscan.org/#/transaction/38262da44768119ea440220e4a48c7a78eef22b0ed35d12febbd6a9d50d2bea9) · [sweep 12:59 UTC](https://tronscan.org/#/transaction/859f3133a07a6d2095a467dfd23c9885d9c8fe11cc3800ba89681ce7a082055d) · [Arkham: HTX Deposit](https://intel.arkm.com/explorer/address/TMVMeCpcR5hh1WG36Yih68t3GuChABJz4E) |
| `TPyjyZ…`, `TSFUtq…`, `TT2T17…` → other labelled exchanges | 0 | 0 | TronGrid |

**What it means:** No JUST-linked wallet was found sending JST to an exchange, on pump days or otherwise. The large HTX flows are HTX moving its own inventory. What keeps this from passing: the biggest holders are unnamed, and one of them delivered the whole first buyback block through HTX, which could be an OTC sale to the buyback by an insider or simply a large holder selling [Unverified]. Score **5** (was 3; the hard-gate fail is lifted).

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from Gate JST_USDT UTC daily closes, re-run 16 Nov 2026 with scripts/pump_day_test.py (29 of 360 days); the body's earlier count used CoinGecko daily closes.

## 📊 Tokenomics & supply · 7/10 · ✅ PASS

- Max supply **9.9B**; fully unlocked; no future unlocks ([Tier B] [whitepaper](https://just.network/docs/white_paper_en.pdf), [docs](https://docs.justlend.org/governance/tokenomics/)).
- **1.775B burned** so far (Tier A); circulating 8.018B per CoinGecko.
- Mint function on the contract **not checked** in this pass (open item).

## 💧 Liquidity & market · 6/10 · ✅ PASS

- $20.2M a day of volume on a $1.15B market cap (1.8% turnover). Binance, OKX, Upbit and Bithumb all hold JST in labelled wallets.
- **58% of volume is on HTX and Poloniex.** Ties between those exchanges and the TRON founder are widely reported but not verified here [Unverified].
- SunSwap JST-USDT pool [`TW68dB…Fkk2`](https://tronscan.org/#/address/TW68dBGdy9gtk16BfzmvaCZ9pEti3KFkk2) holds 50.0M JST; JST-TRX pool [`TUDo1P…aNTT`](https://tronscan.org/#/address/TUDo1PuMG6j4aDSg6rsCNiz5gR5cnQaNTT) 25.7M.

## 🧑‍💻 Product & development · 7/10 · ✅ PASS

- JustLend DAO (lending), plus the USDD stablecoin and SunSwap in the same ecosystem. The jJST market contract [`TWQhCX…czts`](https://tronscan.org/#/address/TWQhCXaWz4eHK4Kd1ErSDHjMFPoPc9czts) holds 90.0M JST.
- TVL **$5.97B** ([Tier A] [DefiLlama](https://defillama.com/protocol/justlend) API, 16 Nov 2026).

## 🤝 Adoption & customers · 7/10 · ✅ PASS

- $5.97B TVL and $15.52M of fees in the last year make JustLend one of the largest lending markets outside Ethereum ([Tier A] DefiLlama).
- Most deposits are TRX and stablecoins from the wider Tron ecosystem; how much of the TVL comes from JUST- or TRON-linked wallets was not checked.

## 🛡️ Security & audits · 5/10 · ❌ FAIL

- No JustLend hack found in this pass. Audit reports were **not re-checked** (open item).
- The buyback depends on a single burn wallet whose key controls are not disclosed.

## ⚖️ Regulatory · 4/10 · ❌ FAIL

- JST trades on large regulated venues (Binance, Upbit, Bithumb).
- The TRON founder has faced US regulatory action. **Tier A:** [SEC Litigation Release 26496](https://www.sec.gov/enforcement-litigation/litigation-releases/lr-26496), 5 Mar 2026 — a proposed final judgment would have Rainberry pay a $10M civil penalty and would dismiss, with prejudice, the remaining claims against Rainberry and all claims against Sun, Tron Foundation and BitTorrent Foundation, **subject to court approval**. This pass did not confirm that the judgment has been entered. Concentrated control by one ecosystem remains a regulatory and governance risk.

## 📅 Catalysts & calendar · 6/10 · ✅ PASS

- Burns have run every quarter (Oct, Jan, Apr, Jul, Oct). Next round expected around **mid-Jan 2027** if the pattern holds [Tier A pattern; date not announced].
- 500M JST already sits in the burn wallet; whether it will be burned is not announced.

---

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack or exploit | 🟢 None found in this pass |
| Live mint path | 🟡 Not checked on-chain; docs give a fixed 9.9B cap |
| Team / treasury wallet to exchange during a pump | 🟢 None found (burn wallet has no exchange outflows; HTX flows are exchange-internal per Arkham) |
| Unlock cliff ahead | 🟢 None, fully unlocked |
| Revenue claims that don't match data | 🔴 Self-reported income ≫ DefiLlama revenue; claimed cumulative burn exceeds the black-hole balance by ≈ 106.7M |
| Buyback sourced from one holder | 🟡 Round 1: 600M from unlabelled [`TPyjyZ…Nan5`](https://tronscan.org/#/address/TPyjyZfsYaXStgz2NmAraF1uZcMtkgNan5) via HTX, nine minutes before the burn |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| Burn wallet `TZJV…` | JUST burn wallet | Tronscan | high | yes | None: sends only to the black hole and JUST contracts |
| Funding wallet | HTX (Arkham) | Arkham | medium | no | None: HTX inventory flows, not an insider sale |

## 📚 Sources

- [Tier A] Methodology update 16 Nov 2026: no new Arkham lookups; the attribution table uses evidence already cited in this report.
- [Tier A] Tronscan / TronGrid TRC-20 transfers and the [JST holder list](https://tronscan.org/#/token20/TCFLL5dx5ZJdKnWuesXxi1VPwjLVmWZZy9/holders), read 16 Nov 2026
- [Tier A] [DefiLlama JustLend](https://defillama.com/protocol/justlend) fees, revenue and TVL APIs, read 16 Nov 2026
- [Tier B] Arkham, read 16 Nov 2026 ~6:10 AM MST (signed-in account): entity labels for [TFTW… (HTX Hot Wallet)](https://intel.arkm.com/explorer/address/TFTWNgDBkQ5wQoP8RXpRznnHvAVV8x5jLu), [TDToU… (HTX Hot Wallet)](https://intel.arkm.com/explorer/address/TDToUxX8sH4z6moQpK3ZLAN24eupu2ivA4), [TK86Q… (HTX Hot Wallet)](https://intel.arkm.com/explorer/address/TK86Qm97uM848dMk8G7xNbJB7zG1uW3h1n), [TMVMe… (HTX Deposit)](https://intel.arkm.com/explorer/address/TMVMeCpcR5hh1WG36Yih68t3GuChABJz4E), the four JUST proposal contracts, and "no label" for [TZJV…](https://intel.arkm.com/explorer/address/TZJVQuU3CJqBScwoxhRtkxQ7JjsNNrpEag), [TPyjyZ…](https://intel.arkm.com/explorer/address/TPyjyZfsYaXStgz2NmAraF1uZcMtkgNan5), [TSFUtq…](https://intel.arkm.com/explorer/address/TSFUtqxZyADSmkgLbpoRwyDinr3BWuT6h9), [TT2T17…](https://intel.arkm.com/explorer/address/TT2T17KZhoDu47i2E4FWxfG79zdkEWkU9N). Arkham's token filter is Enterprise-only, so counterparties are from the default first page only.
- [Tier B] [JustLend docs: tokenomics](https://docs.justlend.org/governance/tokenomics/)
- [Tier B] [5th buyback-and-burn announcement](https://support.justlend.org/hc/en-us/articles/63334976912025-Announcement-on-Completion-of-the-5th-JST-Buyback-and-Burn)
- [Tier B] [JUST whitepaper](https://just.network/docs/white_paper_en.pdf)
- [Tier B] CoinGecko `/coins/just` market data and 365-day closes, 16 Nov 2026 6:00 AM MST

## 🔗 Evidence trail

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| 1.775B JST in the black hole | [`T9yD14…uWwb`](https://tronscan.org/#/address/T9yD14Nj9j7xAB4dbGeiX9h8unkKHxuWwb) · [holders](https://tronscan.org/#/token20/TCFLL5dx5ZJdKnWuesXxi1VPwjLVmWZZy9/holders) | A | 16 Nov 2026 |
| Five burns from the burn wallet | [19 Oct 2025](https://tronscan.org/#/transaction/471bef34bb013dad46f9f132cd1fbca6bd3de584c54b7190718acd5949d4453d), [14 Jan 2026](https://tronscan.org/#/transaction/5c7cd68483f1d32aebe1084b3dc9a6b742092bde1153db72b79a866617c14314), [15 Apr 2026](https://tronscan.org/#/transaction/1e9f55e8ffa8033c238f34f5ebe57f544d424f7016810dd0f1ba792392eeb1e5), [17 Jul 2026](https://tronscan.org/#/transaction/59c47582de15ed1028ca29fe860a09a8149d463ce553432506b95d924256341f), [16 Oct 2026](https://tronscan.org/#/transaction/0cb7d79bd0511ed98b061edb586bf36a868cb510158071ca6fbe3dc56ff86f93) | A | 16 Nov 2026 |
| Burn wallet funded by HTX hot wallet TFTW… | [19 Oct 2025](https://tronscan.org/#/transaction/563506a06877da773461a3c7870b64ed1aadc7b1c6cde0cb629e9a45a4e43826) · [14 Jan 2026](https://tronscan.org/#/transaction/c8a8a84ee337161d427a51549bb9a4489466a8e020547aa3bd85a3c5c3da7265) · [15 Apr 2026](https://tronscan.org/#/transaction/066f6b9b0c7cbab2c6e55784d42dcca6077282d778ae59175be3c0c881deb805) · [Arkham](https://intel.arkm.com/explorer/address/TFTWNgDBkQ5wQoP8RXpRznnHvAVV8x5jLu) | A (transfers) + B (Arkham label) | 16 Nov 2026 |
| TFTW ↔ TDToU / TK86 are HTX-internal | [Arkham TDToU](https://intel.arkm.com/explorer/address/TDToUxX8sH4z6moQpK3ZLAN24eupu2ivA4) · [Arkham TK86Q](https://intel.arkm.com/explorer/address/TK86Qm97uM848dMk8G7xNbJB7zG1uW3h1n) · [409.1M back, 14 Jan](https://tronscan.org/#/transaction/4bec0231b9fb01c824d75a756fba0b301b13a602e0924a31b00754d4ef99bb69) | A + B | 16 Nov 2026 |
| Round 1 block came from whale TPyjyZ… via HTX deposit | [deposit](https://tronscan.org/#/transaction/38262da44768119ea440220e4a48c7a78eef22b0ed35d12febbd6a9d50d2bea9) · [sweep](https://tronscan.org/#/transaction/859f3133a07a6d2095a467dfd23c9885d9c8fe11cc3800ba89681ce7a082055d) · [Arkham](https://intel.arkm.com/explorer/address/TMVMeCpcR5hh1WG36Yih68t3GuChABJz4E) | A + B | 16 Nov 2026 |
| Burn wallet's 200M round trips are JUST proposal votes | [ProposalUpdateEthbCf45Rf](https://intel.arkm.com/explorer/address/TBbdnCLz5x9U9WMj9RvXxUGoPVJ5MFpmrD) · [ProposalUpgradeComptroller](https://intel.arkm.com/explorer/address/TLRp7D7BamAbcwhGLzuBNCshpngyTpiUVW) · [ProposalAddUMarket](https://intel.arkm.com/explorer/address/TNRzQV5ZigUD2y5Ko7MfAqjU7dFcWFMiqN) · [ProposalAddHtxMarket](https://intel.arkm.com/explorer/address/TWhSr8MnZ3KdMPH9qosLqHTjpgZxHfRHgg) | B | 16 Nov 2026 |
| Q3 2026 net income $9.28M | [announcement](https://support.justlend.org/hc/en-us/articles/63334976912025-Announcement-on-Completion-of-the-5th-JST-Buyback-and-Burn) | B | 16 Nov 2026 |
| Protocol revenue $0.79M a year | [DefiLlama](https://defillama.com/protocol/justlend) | A | 16 Nov 2026 |
| Allocation and vesting | [whitepaper](https://just.network/docs/white_paper_en.pdf) · [docs](https://docs.justlend.org/governance/tokenomics/) | B | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | ~~Arkham pass on JST wallets~~ **Done 16 Nov 2026** (the wallet list): TFTW, TDToU and TK86 are HTX hot wallets, TMVMe an HTX deposit, the four 200M counterparties are JUST proposal contracts; the burn wallet and the three biggest holders are unlabelled | Re-check with Arkham Enterprise's token filter for full JST counterparty history | Arkham Enterprise |
| 2 | **Who owns the burn wallet TZJV… and whale TPyjyZ…?** | Ask JustLend DAO to publish its treasury/burn wallets and how round 1's 600M block was bought (OTC or open market) | Free |
| 3 | **Why the 106.7M gap between the claimed cumulative burn and the black hole?** | Compare each announcement's round totals with the five burn txs above | Free |
| 4 | **Income check** | Reconcile JustLend's reported net income with DefiLlama revenue, or with reserve-contract balances on-chain | Free |
| 5 | **Mint function** | Read the JST contract on Tronscan for a mint or owner role | Free |
| 6 | **Audits** | Find JustLend audit reports in the docs or GitHub | Free |
| 7 | **Who funded rounds 4–5?** | Trace the inflows to the burn wallet on 17 Jul and 16 Oct 2026 (TQVScc…, TMwuqc…) and look them up on Arkham | Free |
| 8 | **Has the LR-26496 proposed judgment been entered?** | SDNY docket 1:23-cv-02433, or a later SEC litigation release confirming court approval | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.

## Nansen-month findings, 24 Nov 2026 (MST) — reported only, unscored

This appendix publishes findings from the desk's 24 Nov 2026 holder and treasury research. It does not change the v3 score, badge, gates, formula or `revenue_reaches_holders`. Labels marked **Nansen-labeled** come from one third-party labeler and are treated as leads. Under process rule P12, every Nansen balance or holder figure used here was checked against a direct on-chain read before use, and mismatches were discarded. Hypotheses are labelled **Unverified**. Times are MST.

### Tracking update: buyback-and-burn confirmed on-chain
- **94% of the reported burns trace to one wallet.** [`TZJVQu…pEag`](https://tronscan.org/#/address/TZJVQuU3CJqBScwoxhRtkxQ7JjsNNrpEag) made five quarterly burns to the TRON black-hole address [`T9yD14…uWwb`](https://tronscan.org/#/address/T9yD14Nj9j7xAB4dbGeiX9h8unkKHxuWwb). Together they total **1,775,309,275 JST, 94% of the 1,881,973,007 JST the project reports as burned** as of 17 Oct 2026. Source: TronGrid TRC-20 history, read 24 Nov 2026, about 4:45 AM MST.

| Date | Time (MST) | JST burned | Burn tx | Funded from |
|---|---|---:|---|---|
| 19 Oct 2025 | 6:08 AM | 559,890,753 | [tx `471bef34…`](https://tronscan.org/#/transaction/471bef34bb013dad46f9f132cd1fbca6bd3de584c54b7190718acd5949d4453d) | **Nansen-labeled** HTX hot wallet |
| 14 Jan 2026 | 5:57 AM | 525,000,000 | [tx `5c7cd684…`](https://tronscan.org/#/transaction/5c7cd68483f1d32aebe1084b3dc9a6b742092bde1153db72b79a866617c14314) | **Nansen-labeled** HTX hot wallet |
| 15 Apr 2026 | 5:03 AM | 271,337,579 | [tx `1e9f55e8…`](https://tronscan.org/#/transaction/1e9f55e8ffa8033c238f34f5ebe57f544d424f7016810dd0f1ba792392eeb1e5) | **Nansen-labeled** HTX hot wallet |
| 17 Jul 2026 | 1:49 AM | 248,357,799 | [tx `59c47582…`](https://tronscan.org/#/transaction/59c47582de15ed1028ca29fe860a09a8149d463ce553432506b95d924256341f) | unlabelled wallet |
| 16 Oct 2026 | 6:27 AM | 170,723,144 | [tx `0cb7d79b…`](https://tronscan.org/#/transaction/0cb7d79bd0511ed98b061edb586bf36a868cb510158071ca6fbe3dc56ff86f93) | unlabelled wallet |

- Each burn was funded minutes earlier with the same amount.
- **Not burned:** the wallet also received 300,000,000 JST from the same HTX hot wallet on 15 Apr 2026 and still holds it (299,999,995 on-chain). It also moves 200,000,001-JST lots out and back; the latest left on 22 Nov 2026, 5:28 AM MST.
- **Labelled hypothesis (likely; Unverified for the 300M):** this is the buyback-and-burn execution wallet. What the unburned 300M is for is not known. The wallet is on the desk's monthly treasury watch.
- **Re-based percentages:** Nansen's holder percentages use a smaller supply base (about 8.13B). The holder-mix lines below are re-based on on-chain `totalSupply()` (9,793,336,268 JST).

### Holder mix (top 100 holders)
- Exchange share of the top 100 holders: **about 10.7%** of on-chain supply in Nansen-labeled exchange and DEX-pool wallets (Nansen shows 12.92% on its smaller supply base; holders pass, 24 Nov 2026).
- Issuer and other named holders: No issuer treasury is labeled in the top 10. Nansen-labeled JustLend DAO contracts (WJST and jJST) hold 9.19% and 0.84% of on-chain supply (users' lending deposits). Two unlabeled wallets hold 4.08% and 3.06%. The 3.06% one is the burn wallet described above; the 4.08% one has no confirmed attribution.
- Checked on-chain: TronGrid account reads and on-chain `totalSupply()`, 24 Nov 2026, about 4:34 AM MST; amounts matched, but Nansen's percentages use a smaller supply base (about 8.13B), so they are re-based here on on-chain total supply (9,793,336,268 JST).
- Unscored: this line has no effect on the score, badge or ranking. Labels are Nansen's (a third-party labeler) and are leads, not confirmed ownership.
