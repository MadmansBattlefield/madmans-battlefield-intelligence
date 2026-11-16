---
ticker: JASMY
name: JasmyCoin
chain: ethereum
contract: "0x7420B4b9a0110cdC71fB720908340C03F9Bc03EC"
overall_score: 2.8
overall_verdict: FAIL
section_scores:
  revenue: 1
  foundation_team: 3
  insider_holdings: 3
  selling_behavior: 2
  tokenomics_supply: 7
  liquidity_market: 5
  product_development: 2
  adoption_customers: 1
  security_audits: 5
  regulatory: 3
  catalysts: 2
gates_failed: [revenue, selling_behavior]
red_lines:
  one_hop_sale_status: none_found
  admin_or_mint: none (plain ERC-20)
  deployer_exchange_deposits: "yes (1,845,000,000 to Gate.io, 2023 – Jan 2025)"
  pump_day_exchange_deposit_linked_to_issuer: "unverified (29 Sep 2026)"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "Nothing ties token value to business income: no burn, buyback, fee share or fee-funded staking yield."
pump_day_price_source: "Gate JASMY_USDT UTC daily closes, re-run 16 Nov 2026 with scripts/pump_day_test.py (32 of 360 days); the body's earlier count used CoinGecko daily closes"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions:
  - address: "0x722e6c8ef971338bdb46d4e7924e392d6f2a5b50"
    label: "Unlabelled; funded from Binance"
    confidence: low
    independent_corroboration: false
    basis: "Etherscan"
price_usd: 0.003214
price_source: "CoinGecko, 14 Nov 2026 12:12 PM MST"
last_updated: 2026-11-15
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### JASMY · Overall grade **2.8 / 10 · ❌ FAIL**

**Summary:** A plain, fully minted 50B ERC-20 with no admin keys, but no revenue, no verifiable product usage and no disclosed issuer. The deployer wallet has fed 1.845B JASMY into a Gate.io deposit address over the years (Arkham files that address under Jasmy), and JASMY is no longer listed on Upbit.

**🚨 Top warning:** The deployer [`0xf4a5…7BE9`](https://etherscan.io/address/0xf4a5b232DF2De4dd6ad613ba17C3113CEf707BE9) has put **1,845,000,000 JASMY into one Gate.io deposit address** [`0xa2A3…390f`](https://etherscan.io/address/0xa2A3d0d99EC9f3dBd73F36b600A05C89ddF3390f), which Arkham files under Jasmy itself ("Jasmy: Gate Deposit"). On the **29 Sep 2026 pump day (+21.8%)** another 93.5M went into that **same** deposit address ([43.5M](https://etherscan.io/tx/0x816c67ec404493b854dc4076ccb586a361de0f8dd4c3a815eb35086ded2ece55) · [50M](https://etherscan.io/tx/0xc20fe5c8ae95660ed6a2618d60c598c6d8bc647d022bf7dfe300fef87c01be06)), so it most likely credited the same Gate account (issuer link not proven). Check: [Arkham “Jasmy: Gate Deposit”](https://intel.arkm.com/explorer/address/0xa2A3d0d99EC9f3dBd73F36b600A05C89ddF3390f) · [deposit address on Etherscan](https://etherscan.io/address/0xa2A3d0d99EC9f3dBd73F36b600A05C89ddF3390f) · [last deployer send](https://etherscan.io/tx/0x2f3ba2a6f73d8d7d397e2ed018070496f730f470e560c0410988b0b44394f837).

**Sections passed: 1 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 1/10 | ❌ FAIL |
| 🏛️ Foundation & team | 3/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 3/10 | ❌ FAIL |
| 📉 Selling behavior | 2/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 7/10 | ✅ PASS |
| 💧 Liquidity & market | 5/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 2/10 | ❌ FAIL |
| 🤝 Adoption & customers | 1/10 | ❌ FAIL |
| 🛡️ Security & audits | 5/10 | ❌ FAIL |
| ⚖️ Regulatory | 3/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 2/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 JASMY · JasmyCoin · 2.8 / 10 · ❌ FAIL

> **One line:** A plain, fully minted 50B ERC-20 with no admin keys, but no revenue, no verifiable product usage and no disclosed issuer. The deployer wallet has fed 1.845B JASMY into a Gate.io deposit address over the years (Arkham files that address under Jasmy), and JASMY is no longer listed on Upbit.

| 📊 Market (CoinGecko + DexScreener, 14 Nov 2026 ~12:12 PM MST) | 🔗 On-chain (Ethereum RPC + Blockscout, 14 Nov 2026) |
|---|---|
| **Price** $0.003214 | **Token** [`0x7420…03EC`](https://etherscan.io/address/0x7420B4b9a0110cdC71fB720908340C03F9Bc03EC) "JasmyCoin" · Solidity 0.5.15 · verified |
| **24h / 7d / 30d** 🔴 −6.1% / −12.5% / −32.1% | **Supply** 50,000,000,000, all minted 26 Dec 2019 to the deployer |
| **Market cap** $159.0M · **FDV** $160.8M | **Functions** approve / transfer / transferFrom / allowance only. **No owner, mint, pause or blacklist** |
| **24h volume** $6.79M | **Deployer** [`0xf4a5…7BE9`](https://etherscan.io/address/0xf4a5b232DF2De4dd6ad613ba17C3113CEf707BE9) holds 555,000,322 (1.11%) |
| **ATH** $4.79 (15 Feb 2021) · now −99.93% | **Holders** 102,120 |
| **Circulating (CoinGecko)** 49.44B | **Top 4 wallets** ~3.54–3.60B each, funded by Coinbase |

---

## 💰 Revenue — Does it make money? · 1/10 · ❌ FAIL

| Metric | Value | Source |
|---|---|---|
| Protocol fees or revenue | **None found** (no DefiLlama listing) | [Tier A] DefiLlama (absence) |
| Value accrual to the token | **None.** The contract has no fee, burn or buyback logic | [Tier A] verified source |
| Company revenue | Jasmy Corp is private; no figures | Not found |

**What it means:** Nothing ties token value to any business income.

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** Nothing ties token value to business income: no burn, buyback, fee share or fee-funded staking yield.

## 🏛️ Foundation & team — Who is in charge? · 3/10 · ❌ FAIL

| Item | Finding | Source |
|---|---|---|
| Issuer | Jasmy Corporation (Japan) per public materials. The entity and its link to the token were **not verified** from a registry | [Unverified] |
| On-chain control | None. The token has no owner or admin | [Tier A] verified source |
| Deployer | [`0xf4a5b232DF2De4dd6ad613ba17C3113CEf707BE9`](https://etherscan.io/address/0xf4a5b232DF2De4dd6ad613ba17C3113CEf707BE9) (Blockscout "Jasmy Deployer"; [Arkham](https://intel.arkm.com/explorer/address/0xf4a5b232DF2De4dd6ad613ba17C3113CEf707BE9); mint [tx `0xd70022c6…`](https://etherscan.io/tx/0xd70022c67b6536bb811697f38ca2cfaf2cc977a925b76e51ab6c1fe2ca5da219)) | [Tier A] |
| MultiSigWallet | [`0xB0D8Cf2436Ee7a1303dcDA2342611d256EFA5C3a`](https://etherscan.io/address/0xB0D8Cf2436Ee7a1303dcDA2342611d256EFA5C3a) holds 1.296B with active in/out to [`0x28f2E788…`](https://etherscan.io/address/0x28f2E7888bbff2f49e9842E1c6b37fEdAFf7364c). **Owner unknown**; Arkham does **not** include it in its Jasmy entity | [Tier A] balance · owner [Unverified] · [Tier B] Arkham, read 15 Nov 2026 ~11:00 AM MST (signed-in account) |
| Arkham "Jasmy" entity | Only **2 addresses**: the deployer and the Gate deposit address [`0xa2A3…`](https://etherscan.io/address/0xa2A3d0d99EC9f3dBd73F36b600A05C89ddF3390f) (labelled "Jasmy: Gate Deposit"; [Arkham](https://intel.arkm.com/explorer/address/0xa2A3d0d99EC9f3dBd73F36b600A05C89ddF3390f)) | [Tier B] Arkham, read 15 Nov 2026 ~11:00 AM MST (signed-in account) |

**What it means:** No primary document links a named, accountable issuer to the token wallets.

## 🪙 Foundation / team holdings — How many coins do they hold? · 3/10 · ❌ FAIL

| Wallet | Label | 14 Nov 2026 | % supply | Notes |
|---|---|---:|---:|---|
| [`0xf4a5…7BE9`](https://etherscan.io/address/0xf4a5b232DF2De4dd6ad613ba17C3113CEf707BE9) | Jasmy Deployer | 555,000,322 | 1.11% | Has sent out 49.445B in total |
| [`0xB0D8…5C3a`](https://etherscan.io/address/0xB0D8Cf2436Ee7a1303dcDA2342611d256EFA5C3a) | MultiSigWallet, owner unknown | 1,296,095,740 | 2.59% | Active |
| [`0x10287883…`](https://etherscan.io/address/0x102878839368feE2648C0AA4997A70EF4290E8d8) | Received 4,999,999,999 from the deployer on 8 Oct 2020 ([tx `0x9a16e6f5…`](https://etherscan.io/tx/0x9a16e6f571c6ca61c3b8dc76201c290e146e6acf2bd5c9273f74b6d623b65483)) | — | — | Role [Unverified] |
| 4 EOAs | ~3.54–3.60B each (~28.7% total), funded by Coinbase Hot Wallet `0xA9D1e08C…` in Oct and Dec 2025 | ~14.3B | ~28.7% | Likely Coinbase custody, **not insiders** [Unverified] |
| Exchanges | Binance 8 1.94B, Binance 28 1.63B, plus Crypto.com, eToro, Revolut, Coinbase, MEXC, Kraken, BtcTurk | — | — | [Tier A] Blockscout labels |

**What it means:** The known insider balance today is small (~1–4%), but where the deployer's 5B of 2020 went is unknown, so the full insider stake is unclear.

## 📉 Selling behavior — Do insiders sell into pumps? · 2/10 · ❌ FAIL

**Pump test:** 38 of 360 days had a ≥10% 5-day rise (CoinGecko). The runs were 22–28 Aug and 21 Sep–2 Oct 2026.

| Date | Flow | Source |
|---|---|---|
| 2023 – 16 Jan 2025 | The deployer sent many tranches to [`0xa2A3d0d99EC9f3dBd73F36b600A05C89ddF3390f`](https://etherscan.io/address/0xa2A3d0d99EC9f3dBd73F36b600A05C89ddF3390f) ([Arkham](https://intel.arkm.com/explorer/address/0xa2A3d0d99EC9f3dBd73F36b600A05C89ddF3390f)), which forwards within ~1 hour to **Gate.io Hot Wallet** [`0x0D0707963952f2fBA59dD06f2b425ace40b492Fe`](https://etherscan.io/address/0x0D0707963952f2fBA59dD06f2b425ace40b492Fe) (a Gate deposit pattern). **1,845,000,000 in total** (corrected 15 Nov from "~1.99B"; full on-chain sum). Examples: 26 Jun 2023 770M ([700M in](https://etherscan.io/tx/0x499b65b8349f91d547ac2bf10f355274bc5c429770889bc6136762e43f054402), [770M sweep](https://etherscan.io/tx/0xdf55a167d285eee52f273e47f589dba65c23cfc24dec60d33def9d7e7fe94544)) · 1 Aug 2023 140M ([tx `0xa899222a…`](https://etherscan.io/tx/0xa899222ab2f716a6bfa0e416305196cfe3339ed9560204c4f893a4ae92db7ce4)) · 27 Sep 2024 95.1M ([tx `0xbf294e08…`](https://etherscan.io/tx/0xbf294e08da02ff80450c2ae906fedc9268b986f21fe51ec8f5856710749ba4d0)) · **16 Jan 2025 49,999,900 + a 100 test** (last deployer send, [tx `0x2f3ba2a6f73d…`](https://etherscan.io/tx/0x2f3ba2a6f73d8d7d397e2ed018070496f730f470e560c0410988b0b44394f837); sweep [tx `0xfb48b0cf…`](https://etherscan.io/tx/0xfb48b0cf5e51383e78a2098c6b603d128a7a1ba0f7eaf0722a177b7592950464)). Arkham labels `0xa2A3…` **"Jasmy: Gate Deposit"**; with the Gate Hot Wallet label and the sweep pattern, the Gate deposit is **verified** | [Tier A] Blockscout / Etherscan v2 transfers · [Tier B] Arkham, read 15 Nov 2026 ~11:00 AM MST (signed-in account) |
| **29 Sep 2026** (5-day **+21.8% 🔴 pump**) | [`0x722E6c8ef971338BdB46D4e7924E392D6f2a5b50`](https://etherscan.io/address/0x722E6c8ef971338BdB46D4e7924E392D6f2a5b50) ([Arkham](https://intel.arkm.com/explorer/address/0x722E6c8ef971338BdB46D4e7924E392D6f2a5b50); a contract wallet that received 249,999,000 from Binance 14 on 16 Sep 2026, [tx `0x4114d7e5…`](https://etherscan.io/tx/0x4114d7e5d75717657f73deea94555c854e721c451a9f1b1a59094bd9e5af6af1), and still holds 150M) sent 43.5M ([tx `0x816c67ec404493b8…`](https://etherscan.io/tx/0x816c67ec404493b854dc4076ccb586a361de0f8dd4c3a815eb35086ded2ece55)) and 50M ([tx `0xc20fe5c8ae95660e…`](https://etherscan.io/tx/0xc20fe5c8ae95660ed6a2618d60c598c6d8bc647d022bf7dfe300fef87c01be06)) to the **same** Gate deposit address `0xa2A3…`. They were forwarded to Gate at 05:31 UTC ([tx `0x0d8b7e86…`](https://etherscan.io/tx/0x0d8b7e8601956d0513e4313d12f64cc225878bf69ced175ec7a75a14d06ff871)) and 07:30 UTC ([tx `0x8840f8f6…`](https://etherscan.io/tx/0x8840f8f6550befce04b2ae4b219f2cb4a8551f92c06a499bafcd5469ea76f3d7)), i.e. 10:31 PM MST on 28 Sep and 12:30 AM MST on 29 Sep. Deposits arrived 04:10 and 06:21 UTC. Earlier, `0x722E…` got 27.85M from `0xcbfee373…` (30 Jan 2026, [tx `0x62ff4056…`](https://etherscan.io/tx/0x62ff405692d59560779668aafb9762ab9a39bdb2fa8bd6fcf50653b211e53caf)) and sent 24.9999M to `0xa6c3321e…` (23 Feb 2026, [tx `0x8575bddc…`](https://etherscan.io/tx/0x8575bddcfdc4966e1a1769a84c38e8919ccb0ece54a47ac758399ba6066113e9)). Arkham shows **no entity for `0x722E…`** | [Tier A] transfers · link to Jasmy **[Unverified]** (shared-deposit-address heuristic) |
| Other senders into `0xa2A3…` (all time) | Only three non-deployer senders: `0x722E…` 93.5M (above), `0x69ae3e4f…` 53M (Apr 2023), `0x0639556f…` 1.04M (Mar 2025) | [Tier A] Etherscan v2 |

**What it means:** The deployer has a long record of undisclosed exchange deposits (1.845B), and Arkham itself files the deposit address under Jasmy. An exchange deposit address credits one account, so the 93.5M sent on the 29 Sep pump most likely landed in **the same Gate account the deployer used**. That is strong, but `0x722E…` has no label or funding tie to Jasmy (its coins came from Binance), so the issuer link is still not proven. Score unchanged at 2.

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from Gate JASMY_USDT UTC daily closes, re-run 16 Nov 2026 with scripts/pump_day_test.py (32 of 360 days); the body's earlier count used CoinGecko daily closes.

## 📊 Tokenomics & supply · 7/10 · ✅ PASS

| Item | Value | Source |
|---|---|---|
| Max / total | 50,000,000,000, all minted at deploy (26 Dec 2019) | [Tier A] |
| Mint / burn functions | None | [Tier A] verified source |
| Circulating | 49.44B (98.9%) | [Tier B] CoinGecko |
| Unlock schedule | No vesting contract. Unlocks are whatever wallets choose to move | [Tier A] |

**What it means:** No new supply can ever be created, and almost all of it already circulates. The risk is distribution, not inflation.

## 💧 Liquidity & market · 5/10 · ❌ FAIL

| Venue | 24h volume (approx.) | Source |
|---|---:|---|
| HTX | $1.42M | [Tier B] CoinGecko tickers |
| Binance | $880k | [Tier B] |
| Coinbase | $610k | [Tier B] |
| BloFin, WhiteBIT, Poloniex | smaller | [Tier B] |
| Upbit | **No JASMY market** | [Tier A] Upbit market API (delisting date [Unverified]) |
| DEX total | **~$70.6k** liquidity (Uniswap JASMY/WETH $37k) | [Tier A] DexScreener API |

**What it means:** Still on Binance and Coinbase, but volume is thin for a $159M cap, and on-chain depth is negligible.

## 🧑‍💻 Product & development · 2/10 · ❌ FAIL

- No on-chain product contract or usage metric tied to the token was found (Not found).
- IoT and data-sovereignty product claims are marketing only ([Unverified]).

**What it means:** Nothing on-chain shows a product using the token.

## 🤝 Adoption & customers · 1/10 · ❌ FAIL

- No named customer, filing or usage dashboard was verified (Not found).
- About 28.7% of supply in Coinbase-funded custody wallets reflects exchange custody, not product adoption.

**What it means:** No verifiable adoption.

## 🛡️ Security & audits · 5/10 · ❌ FAIL

| Item | Finding | Source |
|---|---|---|
| Contract | Minimal ERC-20, no admin. Nobody can freeze, mint or upgrade | [Tier A] |
| Compiler | Solidity 0.5.15 (old, but a simple surface) | [Tier A] |
| Audit | Not found | Not found |
| Hacks | None found for JASMY | [Tier B] |

**What it means:** The code risk is low because there is almost no code. With no audit on file, it cannot score higher.

## ⚖️ Regulatory · 3/10 · ❌ FAIL

- Upbit: no JASMY market today ([Tier A] Upbit API). Date and reason of removal [Unverified]; earlier notes said 14 Sep 2026.
- BITPOINT / SBI VC notices (28 Oct 2026, earlier notes): **[Unverified]**. Neither venue appears in CoinGecko's ticker list.
- No MiCA white paper or other filing found (Not found).

**What it means:** It has lost at least one major regulated venue, and no compliance documents exist.

## 📅 Catalysts & calendar · 2/10 · ❌ FAIL

| Date | Event | Source |
|---|---|---|
| — | No scheduled unlock (fully minted) | [Tier A] |
| — | No confirmed product, listing or governance event | Not found |
| Watch | Further Japanese exchange actions (BITPOINT / SBI VC) | [Unverified] |

**What it means:** No positive catalysts are visible. The only known risk events are delistings.

## 🚩 Red lines status

| Red line | Status | Evidence |
|---|---|---|
| Admin key, mint or pause | 🟢 None | Verified source |
| Deployer exchange deposits | 🔴 Yes | 1,845,000,000 to Gate via [`0xa2A3…`](https://etherscan.io/address/0xa2A3d0d99EC9f3dBd73F36b600A05C89ddF3390f) (Arkham: "Jasmy: Gate Deposit", [label](https://intel.arkm.com/explorer/address/0xa2A3d0d99EC9f3dBd73F36b600A05C89ddF3390f)), last 16 Jan 2025 ([tx](https://etherscan.io/tx/0x2f3ba2a6f73d8d7d397e2ed018070496f730f470e560c0410988b0b44394f837)) |
| Pump-day exchange deposit tied to the issuer | 🟠 Likely, not proven | 29 Sep 2026, 93.5M into the deployer's Gate deposit address ([43.5M](https://etherscan.io/tx/0x816c67ec404493b854dc4076ccb586a361de0f8dd4c3a815eb35086ded2ece55) · [50M](https://etherscan.io/tx/0xc20fe5c8ae95660ed6a2618d60c598c6d8bc647d022bf7dfe300fef87c01be06)), so probably the same Gate account; `0x722E…` itself has no tie to Jasmy |
| Delisted from a major venue | 🔴 Yes (Upbit) | Upbit market API |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| Deployer → Gate deposit `0xa2A3…` | Jasmy deployer | Etherscan (deployer) + Arkham files the deposit under Jasmy | high | yes (on-chain) | Selling: 1.845B of undisclosed exchange deposits, 2023 – Jan 2025, keep the score at 2 |
| [`0x722E…5b50`](https://etherscan.io/address/0x722E6c8ef971338BdB46D4e7924E392D6f2a5b50) | Unlabelled; funded from Binance | Etherscan | low | no | None: the 29 Sep 2026 pump-day deposit is not proven as an issuer sale |

## 📚 Sources

- [Tier A] Methodology update 16 Nov 2026: no new Arkham lookups; the attribution table uses evidence already cited in this report.
- [Tier A] Ethereum RPC and eth.blockscout.com: verified source, holders, labels and transfers for the deployer, `0xa2A3…`, `0x722E…` and the MultiSigWallet, 14 Nov 2026
- [Tier A] Upbit public market API (no JASMY market)
- [Tier A] DexScreener tokens API · DefiLlama (no listing)
- [Tier B] CoinGecko markets, tickers and daily closes, 14 Nov 2026
- [Tier A] Etherscan v2 API JASMY `tokentx` for `0xa2A3…` (all senders, full history) and `0x722E…`; read 15 Nov 2026 ~11:20 AM MST
- [Tier B] Arkham, read 15 Nov 2026 ~11:00 AM MST (signed-in account): "Jasmy" entity (deployer + `0xa2A3…` "Jasmy: Gate Deposit"); `0x722E…` and the MultiSigWallet have no entity. First page of transfers only; all-time exchange totals Enterprise-locked
- [Tier A] Explorer pages used (Etherscan): deployer [`0xf4a5…`](https://etherscan.io/address/0xf4a5b232DF2De4dd6ad613ba17C3113CEf707BE9) · Gate deposit [`0xa2A3…`](https://etherscan.io/address/0xa2A3d0d99EC9f3dBd73F36b600A05C89ddF3390f) · Gate hot wallet [`0x0D07…`](https://etherscan.io/address/0x0D0707963952f2fBA59dD06f2b425ace40b492Fe) · [`0x722E…`](https://etherscan.io/address/0x722E6c8ef971338BdB46D4e7924E392D6f2a5b50) · MultiSigWallet [`0xB0D8…`](https://etherscan.io/address/0xB0D8Cf2436Ee7a1303dcDA2342611d256EFA5C3a) · [`0x1028…`](https://etherscan.io/address/0x102878839368feE2648C0AA4997A70EF4290E8d8) · token [`0x7420…`](https://etherscan.io/address/0x7420B4b9a0110cdC71fB720908340C03F9Bc03EC)
- [Tier B] Arkham address pages used: [deployer](https://intel.arkm.com/explorer/address/0xf4a5b232DF2De4dd6ad613ba17C3113CEf707BE9) · [0xa2A3… “Jasmy: Gate Deposit”](https://intel.arkm.com/explorer/address/0xa2A3d0d99EC9f3dBd73F36b600A05C89ddF3390f) · [0x722E…](https://intel.arkm.com/explorer/address/0x722E6c8ef971338BdB46D4e7924E392D6f2a5b50)
- [Unverified] Issuer entity; Upbit delisting date; BITPOINT / SBI VC notices; owner of the MultiSigWallet; Jasmy link to `0x722E…`; role of `0x10287883…`

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer) or the label source (Arkham) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| **Deployer → Gate deposit `0xa2A3…`: 1,845,000,000 JASMY (2023 – 16 Jan 2025)**; Arkham labels the address "Jasmy: Gate Deposit" | [deposit address (all transfers)](https://etherscan.io/address/0xa2A3d0d99EC9f3dBd73F36b600A05C89ddF3390f) · [Arkham label](https://intel.arkm.com/explorer/address/0xa2A3d0d99EC9f3dBd73F36b600A05C89ddF3390f) · [26 Jun 2023 700M](https://etherscan.io/tx/0x499b65b8349f91d547ac2bf10f355274bc5c429770889bc6136762e43f054402) · [1 Aug 2023 140M](https://etherscan.io/tx/0xa899222ab2f716a6bfa0e416305196cfe3339ed9560204c4f893a4ae92db7ce4) · [27 Sep 2024 95M](https://etherscan.io/tx/0xbf294e08da02ff80450c2ae906fedc9268b986f21fe51ec8f5856710749ba4d0) · [16 Jan 2025 50M](https://etherscan.io/tx/0x2f3ba2a6f73d8d7d397e2ed018070496f730f470e560c0410988b0b44394f837) | A + B | 15 Nov 2026 ~11:20 AM MST |
| `0xa2A3…` sweeps everything to Gate.io Hot Wallet within ~1 hour (deposit pattern) | [770M sweep](https://etherscan.io/tx/0xdf55a167d285eee52f273e47f589dba65c23cfc24dec60d33def9d7e7fe94544) · [50M sweep](https://etherscan.io/tx/0xfb48b0cf5e51383e78a2098c6b603d128a7a1ba0f7eaf0722a177b7592950464) · [Gate hot wallet](https://etherscan.io/address/0x0D0707963952f2fBA59dD06f2b425ace40b492Fe) | A + B | 15 Nov 2026 |
| **Pump-day deposits, 29 Sep 2026 (+21.8%):** `0x722E…` sent 43.5M + 50M into the same Gate deposit address; swept 05:31 / 07:30 UTC | [43.5M](https://etherscan.io/tx/0x816c67ec404493b854dc4076ccb586a361de0f8dd4c3a815eb35086ded2ece55) · [50M](https://etherscan.io/tx/0xc20fe5c8ae95660ed6a2618d60c598c6d8bc647d022bf7dfe300fef87c01be06) · [sweep 1](https://etherscan.io/tx/0x0d8b7e8601956d0513e4313d12f64cc225878bf69ced175ec7a75a14d06ff871) · [sweep 2](https://etherscan.io/tx/0x8840f8f6550befce04b2ae4b219f2cb4a8551f92c06a499bafcd5469ea76f3d7) | A (issuer link [Unverified]) | 15 Nov 2026 |
| `0x722E…` was funded with 249,999,000 JASMY from Binance 14 on 16 Sep 2026; Arkham shows no entity | [tx](https://etherscan.io/tx/0x4114d7e5d75717657f73deea94555c854e721c451a9f1b1a59094bd9e5af6af1) · [Etherscan](https://etherscan.io/address/0x722E6c8ef971338BdB46D4e7924E392D6f2a5b50) · [Arkham](https://intel.arkm.com/explorer/address/0x722E6c8ef971338BdB46D4e7924E392D6f2a5b50) | A + B | 15 Nov 2026 |
| All 50B JASMY minted to the deployer on 26 Dec 2019; 5B sent to `0x1028…` on 8 Oct 2020 | [mint tx](https://etherscan.io/tx/0xd70022c67b6536bb811697f38ca2cfaf2cc977a925b76e51ab6c1fe2ca5da219) · [5B tx](https://etherscan.io/tx/0x9a16e6f571c6ca61c3b8dc76201c290e146e6acf2bd5c9273f74b6d623b65483) · [0x1028…](https://etherscan.io/address/0x102878839368feE2648C0AA4997A70EF4290E8d8) | A | 15 Nov 2026 |
| MultiSigWallet `0xB0D8…` holds 1.296B; not in Arkham's Jasmy entity | [Etherscan](https://etherscan.io/address/0xB0D8Cf2436Ee7a1303dcDA2342611d256EFA5C3a) | A | 14 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Who controls `0x722E…`** (the 29 Sep pump-day seller) | Second label source (Nansen) for `0x722E…`, `0xcbfee373…` and `0xa6c3321e…`; check whether the contract wallet's owner key matches any deployer-linked address | Nansen paid |
| 2 | **Owner of the MultiSigWallet `0xB0D8…`** | Call `getOwners()` and trace each owner's funding | Free |
| 3 | **Issuer entity and its link to the token** | Japanese corporate registry for Jasmy Corporation; any official statement naming the deployer | Free / small fee |
| 4 | **Upbit delisting date and reason; BITPOINT / SBI VC notices** | Upbit and BITPOINT / SBI VC notice pages | Free |
| 5 | **Role of `0x10287883…`** (5B from the deployer, Oct 2020) | Trace its outflows | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
