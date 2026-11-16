---
ticker: PROPC
name: Propchain
chain: ethereum
contract: "0x9ff58067bd8d239000010c154c6983a325df138e"
overall_score: 3.6
overall_verdict: FAIL
section_scores:
  revenue: 3
  foundation_team: 5
  insider_holdings: 3
  selling_behavior: 4
  tokenomics_supply: 5
  liquidity_market: 2
  product_development: 4
  adoption_customers: 3
  security_audits: 5
  regulatory: 4
  catalysts: 3
gates_failed: [revenue]
red_lines:
  hack_exploit: none found
  mint_path_live: "no (fixed 100M minted in the constructor; 36.24M burned; admin can only burn its own balance)"
  team_wallet_to_exchange_during_pump: "yes, small (the EOA paid by the Liquidity Vesting contract deposited 178.6k PROPC into Arkham-labelled MEXC deposit addresses on 4 pump days since Dec 2024, including 144.5k on two Sep 2026 pump days)"
  one_hop_sale_status: not_proven
  treasury_in_single_key_wallets: "yes (~10.6M PROPC, 16.6% of supply, sits in four EOAs that the Treasury, Team, Operations and Liquidity vesting contracts paid out to)"
  vesting_mutable: "yes (the deployer has pulled tokens back out of the Team, Treasury and Operations vesting contracts, and the docs record buckets being moved and team vesting being extended)"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "The team says the token was cut off from the business, and the buyback stopped after 5 Oct 2025."
pump_day_price_source: "Gate PROPC/USDT daily closes"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions: []
price_usd: 0.065131
price_source: "CoinGecko, 16 Nov 2026 7:13 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### PROPC · Overall grade **3.6 / 10 · ❌ FAIL**

**Summary:** Propchain sells real-estate data and workflow software and is tied to Prop.com, a property buyer in Europe and the UAE. It has done more than most tiny tokens to publish its wallets: every vesting contract and the buyback wallet are listed in its docs. But **no protocol revenue is verified**. The "Revenue Conversion Layer" that is meant to turn 100% of revenue into PROPC buybacks has **not bought a single token on-chain since 5 Oct 2025**. In the last 12 months, the Foundation-side EOAs deposited **1.49M PROPC into MEXC deposit addresses**. The token trades about $54k a day and is down 98.8% from its high. Revenue trips the hard gate.

**🚨 Top warning:** the buyback stopped while the selling did not. The Foundation's buyback wallet [`0x44b9…6B38`](https://etherscan.io/address/0x44b9ccadef7ef8003085022c6413dd22fb456b38) last received PROPC on [5 Oct 2025](https://etherscan.io/tx/0x73ee3f1b527d31a6e63ca0e45da61385cd4eb00eca873ec7d68179c5342d06fb). Since 16 Nov 2025, the EOAs paid by the [Liquidity Vesting contract](https://etherscan.io/address/0x31a9aa9ff0e3e3df58452fe9113ce5905a70cc19) and the Operations and Treasury buckets have deposited **1.49M PROPC (2.3% of the 63.76M left after burns)** into addresses Arkham labels as MEXC deposits. That includes two **Sep 2026 pump days**: 44.5k on 9 Sep (+24.6%) and **100k on 22 Sep (+32.1%, [tx](https://etherscan.io/tx/0x5b436006e2297955766221e8c4d980bc0ce9b453d60e5653da4a0fb6eb7b8a8f))**. Separately, ~10.6M PROPC paid out of the Treasury, Team, Operations and Liquidity vesting contracts sits in four plain EOAs. Every transfer is linked in the 🔗 Evidence trail below.

**Sections passed: 0 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 3/10 | ❌ FAIL |
| 🏛️ Foundation & team | 5/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 3/10 | ❌ FAIL |
| 📉 Selling behavior | 4/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 5/10 | ❌ FAIL |
| 💧 Liquidity & market | 2/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 4/10 | ❌ FAIL |
| 🤝 Adoption & customers | 3/10 | ❌ FAIL |
| 🛡️ Security & audits | 5/10 | ❌ FAIL |
| ⚖️ Regulatory | 4/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 3/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 PROPC · Propchain · 3.6 / 10 · ❌ FAIL

> **One line:** A real-estate data company whose token buyback went quiet in Oct 2025, while its liquidity wallets kept feeding MEXC. Fixed supply and well-documented wallets, but no verified revenue and almost no trading volume.

| 📊 Market (CoinGecko, 16 Nov 2026 7:13 AM MST) | 🔗 On-chain (Ethereum, 16 Nov 2026) |
|---|---|
| **Price** $0.065131 | **Token** [`0x9ff5…138e`](https://etherscan.io/address/0x9ff58067bd8d239000010c154c6983a325df138e#code) `PlatformToken` (not a proxy) |
| **24h / 7d / 30d** 🟢 +8.4% / 🔴 −16.0% / −38.3% · 1y −74.5% | **`totalSupply()`** 100,000,000 · **burned** 36,236,663 to `0x…dEaD` |
| **Market cap** $2.84M · **FDV** $4.15M | **Circulating (CoinGecko)** 43,665,854 |
| **24h volume** $53.9k | **Deployer** [`0x6Ce7…aFE6`](https://etherscan.io/address/0x6ce7c64f5fe2cc61dab806975808806c9a9cafe6) (Etherscan: "PropChainGlobal: Deployer") |
| **ATH** $5.38 (27 Mar 2024) · now −98.8% | **Buyback wallet** [`0x44b9…6B38`](https://etherscan.io/address/0x44b9ccadef7ef8003085022c6413dd22fb456b38) 1,270,348 |
| **Holders** 10,967 (Blockscout) | **Antisnipe hook** permanently disabled (`antisnipeDisable()` = true) |

---

## 💰 Revenue — Does it make money? · 3/10 · ❌ FAIL

| Metric | Value | Source |
|---|---:|---|
| Protocol revenue | **Not found.** Not listed on DefiLlama; no audited figures published | [Tier A] DefiLlama (no listing), 16 Nov 2026 |
| Team's own words | "Although the Propchain technology infrastructure … generated verifiable revenue, none of this activity was reflected on-chain"; "PROPC is missing a strong revenue and token connection" | [Tier A] [Ecosystem V1 docs](https://docs.propchain.com/propchain-foundation/ecosystem-v1) |
| Promised fix | The Revenue Conversion Layer converts "100% of recognized technology and protocol revenues" into PROPC; "executions are currently discretionary" | [Tier A] same page |
| Buybacks actually seen | The buyback wallet received **1,270,348 PROPC in 43 transfers from MEXC 16**, 3 Jul – 5 Oct 2025, and **nothing since** | [Tier A] [buyback wallet](https://etherscan.io/address/0x44b9ccadef7ef8003085022c6413dd22fb456b38) · [Dune](https://dune.com/propchain/propchain-ecosystem) |
| Prop.com figures | "$2.35M already realised" and "$24.78M forecasted" revenue from Prop.com's portfolio. This is property revenue, not Propchain's, and it is unaudited | [Tier B] [Propchain news channel](https://tg.me/propchainnews), 1 Oct 2026 |

**What it means:** The team says itself that the token was cut off from the business. The fix it built stopped buying after 5 Oct 2025, and no revenue figure for Propchain itself can be checked. **3, which trips the Revenue gate.**

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** The team says the token was cut off from the business, and the buyback stopped after 5 Oct 2025.

## 🏛️ Foundation & team — Who is in charge? · 5/10 · ❌ FAIL

| Item | Finding | Source |
|---|---|---|
| Entity | Propchain Foundation runs the token; Prop.com is the affiliated real-estate business | [Tier A] [Propchain docs](https://docs.propchain.com/propchain-foundation/operational-token-management) |
| Wallet disclosure | **Good.** The docs list the deployer, staking contracts and all 13 vesting contracts | [Tier A] [Addresses page](https://docs.propchain.com/propchain-foundation/usdpropc-utility-token/addresses) |
| Bucket changes | The docs' changelog records seed and private tokens moved to a "DBM" bucket, 4.63M moved from Team to Operations, team vesting extended by 6 months, and two large burns | [Tier A] [Changelog / Burns](https://docs.propchain.com/propchain-foundation/operational-token-management/changelog-burns) |
| Gaps | The EOAs that now hold the released Treasury, Team, Operations and Liquidity tokens are not on the addresses page. Market makers are not named | — |

**What it means:** Better disclosure than most microcaps, but the Foundation can and does rewrite its own vesting buckets, and the wallets that hold released tokens are not disclosed.

## 🪙 Foundation / team holdings — How many coins do they hold? · 3/10 · ❌ FAIL

| Holder | PROPC | Notes |
|---|---:|---|
| Treasury → EOA [`0x96dE…81B3`](https://etherscan.io/address/0x96de9a881ef1334bf735084134f73691d37e81b3) | **4,011,639** | Got 4.06M from Treasury Vesting (e.g. [3.07M on 13 May 2025](https://etherscan.io/tx/0xd80421824ec82835040ac79d660cdc9dace172ef5e04cc1d511e5e4ebfdb9c32)). **Single key** |
| Team/Dev → EOA [`0x0E9C…888F`](https://etherscan.io/address/0x0e9c02de1608104bfa6de41f99604fbd5c30888f) | **2,374,951** | From Team Vesting ([1.34M on 13 May 2025](https://etherscan.io/tx/0x06c6c8aefa8b45246becfcdaf9c7796841529d2431c8a461e0e9bf3d1411f65e), [1.04M on 23 Sep 2025](https://etherscan.io/tx/0x49bb82d6123d135e4a13b6e5885df2319e3bebc7751f4e2fb7691935b2b6e009)); never moved. **Single key** |
| Operations → EOA [`0x6a64…F231`](https://etherscan.io/address/0x6a64f2cef8688205c3990e1c2c8ebb75d1e3f231) | **2,078,246** | From Operations Vesting ([1.92M on 13 May 2025](https://etherscan.io/tx/0xd155d6787282ce19f485d6313bee6a0a9fd157cd27733f63f0fd1a37b5f0aa04)); also traded with MEXC 16. **Single key** |
| Liquidity → EOA [`0x6379…2e09`](https://etherscan.io/address/0x6379942cc525ead26fb6f6998cb16d60220d2e09) | 847,410 | From Liquidity Vesting; deposits into MEXC deposit addresses (see Selling) |
| Buyback wallet `0x44b9…` | 1,270,348 | Foundation buyback wallet, never moved |
| Unvested in vesting contracts | ~16.9M | Rewards 4.55M, Community 4.20M, Team 3.25M, Treasury 3.09M, Operations 1.12M, Advisors 0.73M (Blockscout holder list) |
| **Total team-side** | **~27.5M (43% of the 63.76M left after burns)** | Of which ~10.6M is in single-key EOAs |

**Arkham check ([Tier B] Arkham, read 16 Nov 2026 (signed-in account)):** the four EOAs show the same balances: [0x96dE](https://intel.arkm.com/explorer/address/0x96de9a881ef1334bf735084134f73691d37e81b3) 4.012M, [0x0E9C](https://intel.arkm.com/explorer/address/0x0e9c02de1608104bfa6de41f99604fbd5c30888f) 2.375M (tagged dormant), [0x6a64](https://intel.arkm.com/explorer/address/0x6a64f2cef8688205c3990e1c2c8ebb75d1e3f231) 2.078M and [0x6379](https://intel.arkm.com/explorer/address/0x6379942cc525ead26fb6f6998cb16d60220d2e09) 847.41K. Arkham tags each as a "PROPC Whale", names no controller, and shows PlatformVesting contracts as their PROPC sources.

**What it means:** Close to half the surviving supply is controlled by the Foundation side, and about a sixth of it sits in plain EOAs. The vesting contracts are not a hard lock: the deployer pulled [1.875M back out of Team Vesting](https://etherscan.io/tx/0xf47b1ed527f7d89cf6a3fe4080f1bd4aa055c6a1c9055dbe71bc7a01b3f734ab) and [2.85M out of Treasury Vesting](https://etherscan.io/tx/0x40095da9cd9f3b27aa435e2d1d3df6a154c6d0bcd031d6e8ca56c59437963948) on 2 Sep 2024 (for the PCF-3 burn).

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL

*Pump test uses Gate PROPC/USDT daily closes (UTC), which start on 19 Dec 2024. 29 of the last 365 days were pump days. The route is Liquidity Vesting [`0x31a9…`](https://etherscan.io/address/0x31a9aa9ff0e3e3df58452fe9113ce5905a70cc19) → `0x6379…` → [`0xb558…4d30`](https://etherscan.io/address/0xb558f929b5d84b8015d97d5034879ae474644d30) / [`0xb501…f17c`](https://etherscan.io/address/0xb50192c2adadf73db15556820322efe25c1ef17c) / [`0x0487…cf12`](https://etherscan.io/address/0x0487a9387644bb33822cb7410739ddb0615dcf12) → MEXC 3 / MEXC 16 hot wallets. Arkham labels all three middle addresses **MEXC Deposit** ([0xb558](https://intel.arkm.com/explorer/address/0xb558f929b5d84b8015d97d5034879ae474644d30) · [0xb501](https://intel.arkm.com/explorer/address/0xb50192c2adadf73db15556820322efe25c1ef17c) · [0x0487](https://intel.arkm.com/explorer/address/0x0487a9387644bb33822cb7410739ddb0615dcf12); [Tier B] Arkham, read 16 Nov 2026 (signed-in account)), so they are exchange deposit addresses, not team hop wallets. They also take deposits from unrelated wallets, so the table counts only deposits sent **directly by the team-side EOAs**. `0xb558…` also took PROPC from the Operations and Treasury EOAs.*

| Day (UTC) | Route | PROPC | Gate close / 5-day change | Pump? |
|---|---|---:|---:|---|
| 26 Mar 2025 | `0x6379…` → MEXC deposit `0xb558…` ([tx](https://etherscan.io/tx/0xe287bfcb623f229f408e0b2535c3cf4fceb742ea541eb607ab27a8a70d3f5c01)) | 15,000 | $0.73 / +39.8% | 🔴 Yes |
| 12 May 2025 | `0x6379…` → MEXC deposit `0xb501…` ([tx](https://etherscan.io/tx/0xe19bdff0b840ed7abc81d087e193d8ca73a01337db20151331003e1e6fb4488a)) | 19,070 | $0.73 / +38.6% | 🔴 Yes |
| 31 Mar 2026 | `0x6a64…` (Operations) and `0x6379…` → MEXC deposit `0xb558…` ([250k](https://etherscan.io/tx/0xc7f9a796f8abb5a7683c57325914e0a79f9c8c0c513c9bf4858a3c77bdd4006e) · [175k](https://etherscan.io/tx/0xb8d95cd70df3337370f10ab6bb08a86e271c18be75fa617d8a7e43b90d0e5028)) | 425,000 | +9.3% | No (just under) |
| 9 Sep 2026 | `0x6379…` → MEXC deposit `0x0487…` ([tx](https://etherscan.io/tx/0xba84d2d5b79a9115dd3d36d6437c668406c1273970984672e87f0f7a863998d5)) | 44,539 | $0.112 / +24.6% | 🔴 Yes |
| **22 Sep 2026** | `0x6379…` → MEXC deposit `0x0487…` ([tx](https://etherscan.io/tx/0x5b436006e2297955766221e8c4d980bc0ce9b453d60e5653da4a0fb6eb7b8a8f)) | **100,000** | $0.122 / **+32.1%** | 🔴 Yes |

- **Totals:** the Liquidity, Operations and Treasury EOAs deposited **3.19M PROPC** into the three MEXC deposit addresses (Liquidity 2.77M, Operations 365k, Treasury 50k). Since the Gate listing (19 Dec 2024) that is 2.55M, of which **178.6k (7.0%) on 4 pump days**. In the last 12 months the figure is **1.49M**, while the buyback wallet received nothing.
- **Correction (16 Nov 2026):** an earlier draft counted all PROPC these three addresses passed on to exchanges (7.63M in total; 291k on 8 pump days; 1.80M in 12 months). Once Arkham showed they are MEXC deposit addresses, the deposits from unrelated wallets came out. That removes 4 Jan 2025 (13.6k), 21 Mar 2025 (9.1k), 12 Aug 2025 (50k) and **3 Sep 2026 (40k, which came from a Gate hot wallet, [tx](https://etherscan.io/tx/0xaa9f95ba18a90210fa9603968ccc12ebcd07e13a0ad2aedcf9c051667e018be8))**.
- **Two-way flow:** MEXC deposit `0x0487…` also received 120k from Gate Hot Wallet [`0x0D07…92fe`](https://etherscan.io/address/0x0d0707963952f2fba59dd06f2b425ace40b492fe) (Arkham label), and `0x6a64…` received 300k from MEXC 16. So whoever owns this MEXC account also moves PROPC between Gate and MEXC, which looks like market-making rather than pure dumping. Arkham names no market maker [Unverified].

**What it means:** The Liquidity bucket is disclosed, so routing it to exchanges is not hidden. But the EOAs doing it are not disclosed, it continues into pumps (two Sep 2026 pump days), and it outran the buybacks by a wide margin. The corrected totals are smaller, but the pattern holds. **4** (unchanged).

- **Disclosure quality (16 Nov 2026 rules): not applicable** (cleanup 16 Nov 2026: the sale is not proven under the one-hop amendment, so no disclosure grade applies). Context: The Liquidity bucket is disclosed but the EOAs and their exchange sends are not, so disclosure is partial and no penalty applies; Selling stays 4. Pump days from Gate PROPC/USDT daily closes.

## 📊 Tokenomics & supply · 5/10 · ❌ FAIL

- **Fixed supply:** 100M minted once in the constructor ([code](https://etherscan.io/address/0x9ff58067bd8d239000010c154c6983a325df138e#code)); no mint function. 36.24M burned: [10M on 26 Jul 2023](https://etherscan.io/tx/0xb1e9389198abbfcafcc7ad09ee7e913adbe03caf5883d77b8ea366f20cdb74c7) and [21.15M on 2 Sep 2024](https://etherscan.io/tx/0x75aa2ae36ee810d133c46c55b1da43e3b1d5fb16cc11d6351ec120f02d3e15f1) (DAO proposal PCF-3).
- **Mutable vesting:** buckets have been moved and extended by the Foundation (see Foundation & team); releases came in lumps (e.g. 13 May 2025) rather than the documented daily drip.
- Token admin powers: `burn` (own balance), set the vesting and staking addresses; the antisnipe transfer hook is permanently disabled.

## 💧 Liquidity & market · 2/10 · ❌ FAIL

- **$53.9k of 24h volume** on a $2.84M cap. Main venues are MEXC and Gate, plus a Uniswap V2 pool [`0x4F9F…346C`](https://etherscan.io/address/0x4f9fc4e0b79c1cbf16e68863ad5e9de6a94a346c) holding 1.54M PROPC.
- **−98.8% from ATH**; Gate close fell from $0.52 (5 Oct 2025) to $0.065 (16 Nov 2026).

## 🧑‍💻 Product & development · 4/10 · ❌ FAIL

- Propchain positions itself as a real-estate data and validation layer, operating in Germany and the UAE ([propchain.com](https://www.propchain.com/)). It says its "historical on-chain yield products are being migrated to a regulated asset-management framework".
- Wormhole NTT bridging to Solana launched Aug 2025 [Tier B, CoinMarketCap + Propchain posts]. No public code activity was checked.

## 🤝 Adoption & customers · 3/10 · ❌ FAIL

- 10,967 Ethereum holders (Blockscout). Prop.com reports a ~€400M acquisition pipeline [Tier B, company post]. No on-chain usage metric links the business to PROPC.

## 🛡️ Security & audits · 5/10 · ❌ FAIL

- No exploit found. The token is simple and verified; the antisnipe hook is off.
- Audit reports were not located in this pass [Unverified]. ~10.6M PROPC sits in single-key EOAs.

## ⚖️ Regulatory · 4/10 · ❌ FAIL

- On-chain yield products are being moved under a regulated asset manager, which suggests the old products did not fit the rules [Unverified]. No enforcement action found.

## 📅 Catalysts & calendar · 3/10 · ❌ FAIL

| Date | Event |
|---|---|
| Ongoing to ~2027 | Team, Treasury, Operations and Community vesting releases (lumpy) |
| Unknown | Restart of RCL buybacks (none since 5 Oct 2025) |
| 2026 | Prop.com acquisitions pipeline (~€400M) |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | 🟡 Liquidity EOA → MEXC deposit addresses on 4 pump days (178.6k), e.g. [22 Sep 2026](https://etherscan.io/tx/0x5b436006e2297955766221e8c4d980bc0ce9b453d60e5653da4a0fb6eb7b8a8f) |
| Live mint path | 🟢 None |
| Treasury in single-key wallets | 🔴 ~10.6M PROPC in [`0x96dE…`](https://etherscan.io/address/0x96de9a881ef1334bf735084134f73691d37e81b3), [`0x0E9C…`](https://etherscan.io/address/0x0e9c02de1608104bfa6de41f99604fbd5c30888f), [`0x6a64…`](https://etherscan.io/address/0x6a64f2cef8688205c3990e1c2c8ebb75d1e3f231), [`0x6379…`](https://etherscan.io/address/0x6379942cc525ead26fb6f6998cb16d60220d2e09) |
| Buyback promise not kept | 🔴 No buyback since [5 Oct 2025](https://etherscan.io/tx/0x73ee3f1b527d31a6e63ca0e45da61385cd4eb00eca873ec7d68179c5342d06fb) |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| Liquidity Vesting `0x31a9…` → EOA | Propchain Liquidity bucket | Etherscan (contract payout) | high | yes (on-chain) | Selling: exchange deposits on two Sep 2026 pump days |

## 📚 Sources

- [Tier A] Methodology update 16 Nov 2026: no new Arkham lookups; the attribution table uses evidence already cited in this report.
- [Tier A] Etherscan v2 API `tokentx` (PROPC) for the deployer, all 13 vesting contracts, the buyback wallet and every hop named; `getsourcecode` and `getcontractcreation` for the token; Ethereum RPC `balanceOf`, `antisnipeDisable()`, `eth_getCode`; read 16 Nov 2026 ~7:20–8:00 AM MST
- [Tier B] Etherscan name tags ("PropChainGlobal: Deployer", "MEXC 3", "MEXC 16"); Blockscout holder list
- [Tier B] Arkham, read 16 Nov 2026 (signed-in account): [0xb558](https://intel.arkm.com/explorer/address/0xb558f929b5d84b8015d97d5034879ae474644d30), [0xb501](https://intel.arkm.com/explorer/address/0xb50192c2adadf73db15556820322efe25c1ef17c) and [0x0487](https://intel.arkm.com/explorer/address/0x0487a9387644bb33822cb7410739ddb0615dcf12) are labelled MEXC Deposit; the four EOAs are unlabelled "PROPC Whale" addresses; [0x9af6](https://intel.arkm.com/explorer/address/0x9af697a1de82d74a423732624c41cd9320882e4e) carries a "Contract Deployer" tag with no named controller. No market maker is named on any page
- [Tier A] [Propchain docs: tokenomics](https://docs.propchain.com/propchain-foundation/usdpropc-utility-token/tokenomics) · [addresses](https://docs.propchain.com/propchain-foundation/usdpropc-utility-token/addresses) · [Ecosystem V1](https://docs.propchain.com/propchain-foundation/ecosystem-v1) · [changelog / burns](https://docs.propchain.com/propchain-foundation/operational-token-management/changelog-burns) · [Dune dashboard](https://dune.com/propchain/propchain-ecosystem)
- [Tier B] [Propchain news channel](https://tg.me/propchainnews) · [CoinMarketCap updates](https://coinmarketcap.com/cmc-ai/propchain/latest-updates/) · [propchain.com](https://www.propchain.com/)
- [Tier A] CoinGecko `propchain` (16 Nov 2026 7:13 AM MST); Gate PROPC/USDT daily candles
- [Unverified] who controls the four EOAs; who owns the MEXC account behind deposit addresses `0xb558…`/`0xb501…`/`0x0487…`, and whether it is a market maker; Propchain's own revenue; audits

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Fixed 100M supply, no mint | [code](https://etherscan.io/address/0x9ff58067bd8d239000010c154c6983a325df138e#code) | A | 16 Nov 2026 |
| 36.24M burned in two main burns | [10M](https://etherscan.io/tx/0xb1e9389198abbfcafcc7ad09ee7e913adbe03caf5883d77b8ea366f20cdb74c7) · [21.15M](https://etherscan.io/tx/0x75aa2ae36ee810d133c46c55b1da43e3b1d5fb16cc11d6351ec120f02d3e15f1) | A | 16 Nov 2026 |
| Last buyback 5 Oct 2025; wallet unchanged since | [tx](https://etherscan.io/tx/0x73ee3f1b527d31a6e63ca0e45da61385cd4eb00eca873ec7d68179c5342d06fb) · [wallet](https://etherscan.io/address/0x44b9ccadef7ef8003085022c6413dd22fb456b38) | A | 16 Nov 2026 |
| Treasury / Team / Ops vesting paid to EOAs | [Treasury 3.07M](https://etherscan.io/tx/0xd80421824ec82835040ac79d660cdc9dace172ef5e04cc1d511e5e4ebfdb9c32) · [Team 1.34M](https://etherscan.io/tx/0x06c6c8aefa8b45246becfcdaf9c7796841529d2431c8a461e0e9bf3d1411f65e) · [Ops 1.92M](https://etherscan.io/tx/0xd155d6787282ce19f485d6313bee6a0a9fd157cd27733f63f0fd1a37b5f0aa04) | A | 16 Nov 2026 |
| Deployer pulled tokens back out of vesting contracts | [Team 1.875M](https://etherscan.io/tx/0xf47b1ed527f7d89cf6a3fe4080f1bd4aa055c6a1c9055dbe71bc7a01b3f734ab) · [Treasury 2.85M](https://etherscan.io/tx/0x40095da9cd9f3b27aa435e2d1d3df6a154c6d0bcd031d6e8ca56c59437963948) | A | 16 Nov 2026 |
| Liquidity Vesting → `0x6379…` | [1.14M, 13 May 2025](https://etherscan.io/tx/0x36461d81f9885ac91f811436ea9cf66b58dba601bae91614cec39c35bd00f73c) · [496k, 23 Sep 2025](https://etherscan.io/tx/0x1341628aa43e0a717a7aae20a514f18a89f04a308852882a62a2e5a295bb7515) | A | 16 Nov 2026 |
| Pump-day deposits by the Liquidity EOA, Sep 2026 | [9 Sep](https://etherscan.io/tx/0xba84d2d5b79a9115dd3d36d6437c668406c1273970984672e87f0f7a863998d5) · [22 Sep](https://etherscan.io/tx/0x5b436006e2297955766221e8c4d980bc0ce9b453d60e5653da4a0fb6eb7b8a8f) (swept on to MEXC 16: [9 Sep](https://etherscan.io/tx/0xe77b2585aa3d87aac0997966f5181ada6eed59539f40ed0b14393dceb90842d5) · [22 Sep](https://etherscan.io/tx/0x24370457b81c85a43ae9e83a3cb29eca6519cb5154f09ab1221cecac1d26dbf6)) | A + B tag | 16 Nov 2026 |
| `0xb558…`, `0xb501…`, `0x0487…` are MEXC deposit addresses | [0xb558](https://intel.arkm.com/explorer/address/0xb558f929b5d84b8015d97d5034879ae474644d30) · [0xb501](https://intel.arkm.com/explorer/address/0xb50192c2adadf73db15556820322efe25c1ef17c) · [0x0487](https://intel.arkm.com/explorer/address/0x0487a9387644bb33822cb7410739ddb0615dcf12) | B (Arkham) | 16 Nov 2026 |
| 3 Sep 2026 deposit came from a Gate hot wallet, not the team | [tx](https://etherscan.io/tx/0xaa9f95ba18a90210fa9603968ccc12ebcd07e13a0ad2aedcf9c051667e018be8) · [Gate Hot Wallet](https://intel.arkm.com/explorer/address/0x0d0707963952f2fba59dd06f2b425ace40b492fe) | A + B (Arkham) | 16 Nov 2026 |
| Revenue Conversion Layer promise; "currently discretionary" | [Ecosystem V1](https://docs.propchain.com/propchain-foundation/ecosystem-v1) | A | 16 Nov 2026 |
| Vesting addresses published | [Addresses page](https://docs.propchain.com/propchain-foundation/usdpropc-utility-token/addresses) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Who controls the four team-side EOAs** | Arkham (16 Nov 2026) tags them only as "PROPC Whale" with no controller; ask the Foundation to add them to its addresses page | Free |
| 2 | **Who owns the MEXC account behind deposit addresses `0xb558…` / `0xb501…` / `0x0487…`, and is it a market maker?** | Arkham labels them MEXC deposits but names no owner. Ask the Foundation to name its market makers and publish the loan terms | Free |
| 3 | **Why have RCL buybacks stopped?** | Watch the buyback wallet and the Dune dashboard; ask the Foundation for recognized revenue since Oct 2025 | Free |
| 4 | **Propchain's own revenue** | Ask for audited accounts or the RCL's recognized revenue figure | Free |
| 5 | **Audits** | Find audit reports for the token and vesting contracts | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
