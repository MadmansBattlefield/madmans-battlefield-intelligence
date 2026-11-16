---
ticker: EDEL
name: Edel Finance
chain: base
contract_base: "0xFb31f85A8367210B2e4Ed2360D2dA9Dc2D2Ccc95"
overall_score: 2.5
overall_verdict: FAIL
section_scores:
  revenue: 1
  foundation_team: 4
  insider_holdings: 3
  selling_behavior: 3
  tokenomics_supply: 3
  liquidity_market: 4
  product_development: 3
  adoption_customers: 1
  security_audits: 1
  regulatory: 4
  catalysts: 2
gates_failed: [revenue, selling_behavior]
red_lines:
  hack_exploit: tripped_twice
  official_liquidity_pulled: tripped
  founder_or_director_exit: none_found
  team_cluster_wallet_outflow_to_sales_12_13_Nov_2026: found_not_pump_days
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "About $4.8k of lifetime revenue and none flows to the token."
pump_day_price_source: "MEXC EDELUSDT UTC daily closes, re-run 16 Nov 2026 with scripts/pump_day_test.py (87 of 330 days); the body's earlier count used the report's own 5-close window test"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions: []
price_usd: 0.01082
price_source: "CoinGecko, 14 Nov 2026 9:08 AM MST"
last_updated: 2026-11-15
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### EDEL · Overall grade **2.5 / 10 · ❌ FAIL**

**Summary:** A renounced, fixed-supply Base token from a BVI company, with two security incidents in 2026, a lending product that was shut down, no revenue to the token, and 60% of supply taken by insiders in the launch transaction.

**🚨 Top warning (red line):** On 12 Nov 2026 the team-cluster wallet `0x0c3e` itself signed out **11.5M EDEL**, which with 5.6M more became **17.14M EDEL (≈ $300k)** and was sold on DEXs or sent to exchange-scale wallets within hours, the same amount the team then called a "theft". Check it: [tx `0x0c3e send`](https://basescan.org/tx/0x4d2937f6852ff859d98285139c8a56aeb5fa51bb661a55eb6757083090417b66) · [tx `17.14M hop`](https://basescan.org/tx/0xf9221f6608171eb6fd2eb8dbf79dc9e60ec2a164ca107c9ef8c7ca5ebda95746) · [tx `first sale into old pool`](https://basescan.org/tx/0x97a243a901f9ea7b68d04b9f32b88c8c1a095cd681f2c1c2624ef17e03f250dc) · [0x0c3e on Arkham](https://intel.arkm.com/explorer/address/0x0c3eA09eD6798BFF724588e07EACA8278AD64E07) · [0x0c3e on Basescan](https://basescan.org/address/0x0c3eA09eD6798BFF724588e07EACA8278AD64E07). Full route in the 🔗 Evidence trail below.

**Sections passed: 0 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 1/10 | ❌ FAIL |
| 🏛️ Foundation & team | 4/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 3/10 | ❌ FAIL |
| 📉 Selling behavior | 3/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 3/10 | ❌ FAIL |
| 💧 Liquidity & market | 4/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 3/10 | ❌ FAIL |
| 🤝 Adoption & customers | 1/10 | ❌ FAIL |
| 🛡️ Security & audits | 1/10 | ❌ FAIL |
| ⚖️ Regulatory | 4/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 2/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 EDEL · Edel Finance · 2.5 / 10 · ❌ FAIL

> **One line:** A renounced, fixed-supply Base token from a BVI company, with two security incidents in 2026, a lending product that was shut down, no revenue to the token, and 60% of supply taken by insiders in the launch transaction.

| 📊 Market (CoinGecko, 14 Nov 2026 9:08 AM MST) | 🔗 On-chain (Base RPC, 12–13 Nov 2026) |
|---|---|
| **Price** $0.01082 | **Canonical token** [`0xFb31…Ccc95`](https://basescan.org/address/0xFb31f85A8367210B2e4Ed2360D2dA9Dc2D2Ccc95) (Base, 18 dp) |
| **24h / 7d / 30d** 🔴 −1.6% / −52.5% / −64.8% | **Supply** 1,000,000,000 fixed · owner `0x0` · levy 0 |
| **Market cap** $7.65M · **FDV** $10.82M | **Hedgey vesting** 293.66M (29.4%) |
| **24h volume** $708,941 | **Launch-tx insider take** 602.39M (60.24%) |
| **ATH** $0.1109 (19 Nov 2025) · now −90% | **New LP controlled by one wallet** ~98.6%, none locked |
| **Circulating (CoinGecko)** 706.66M | **Solana mint authority** still set |
| **Holders** 34,365 · top 10 = 48.96% (GeckoTerminal) | **Bridges** ETH, BNB, Solana, Robinhood Chain (LayerZero OFT) |

---

## 💰 Revenue — Does it make money? · 1/10 · ❌ FAIL

| Metric | Value | Source |
|---|---:|---|
| DefiLlama all-time fees | $47,728.86 | [Tier A] DefiLlama `edel` |
| DefiLlama all-time revenue | $4,771.47 | [Tier A] DefiLlama |
| 30-day fees / revenue | $0 / $0 | [Tier A] DefiLlama |
| TVL | ~$838 (borrowed 0) | [Tier A] DefiLlama |
| TVL before 30 Jun 2026 exploit | $632,753 → $952 a day later | [Tier A] DefiLlama |
| Markets (Canton perps) API | 13 markets, open interest 0, dust USDCx volume | [Tier A] Edel Markets API, 12 Nov |
| Token's claim on revenue | **None.** MiCAR paper: "does not grant any legally enforceable or contractual rights" | [Tier A] MiCAR white paper |

- Marketing says "share in protocol revenue." The legal filing says no. The filing wins.
- Official X, 10 Nov 2026: TVL $0, paused because "the economics don't justify the operation."

**What it means:** The business earned about $4.8k of revenue in its whole life, and none of it flows to the token.

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** About $4.8k of lifetime revenue and none flows to the token.

## 🏛️ Foundation & team — Who is in charge? · 4/10 · ❌ FAIL

| Item | Finding | Source |
|---|---|---|
| Issuer | Titan Labs Limited, BVI company 2194169, LEI `529900E9GA8R99VOHV41` (ACTIVE) | [Tier A] MiCAR paper, GLEIF |
| Registered | 25 Nov 2025 (paper) · GLEIF creation 24 Nov 2025 | [Tier A] |
| Token launched | 12 Nov 2025, **13 days before** the company existed | [Tier A] Base launch tx |
| Terms of Service operator | "TITAN LIMITED", P.O. Box 3189 (paper/GLEIF use Titan Labs Limited, Box 3198) | [Tier A] docs.edel.finance/legal/terms |
| Directors (MiCAR) | Andrés Soltermann · James Sherborne | [Tier A] MiCAR A.12 / D.5 |
| CTO (site only) | Roman Fritschi, **not named** in the MiCAR filing | [Tier A] site · [Tier A] filing |
| Prior company | Grizzly Development AG (Zug): Fritschi board president, Soltermann board member. Bankruptcy opened 17 Jun 2025, discontinued for lack of assets 19 Sep 2025 | [Tier A] SHAB / Zefix |
| Sherborne | Director of Saxon Advisors Ltd (UK 11443641, Active) | [Tier A] Companies House |
| Head office | "No head office"; no published financial statements | [Tier A] MiCAR |
| Investors | "Titan Labs, private investors and/or ecosystem partners" — no rounds, prices or leads | [Unverified] |

**What it means:** Real, findable people and a real BVI shell, but the company was formed after the token, and two founders' last company went bankrupt with no assets.

## 🪙 Foundation / team holdings — How many coins do they hold? · 3/10 · ❌ FAIL

| Wallet / contract | EDEL | % of 1B | Locked? |
|---|---:|---:|---|
| Hedgey TokenVestingPlans [`0x2CDE9919e81b20B4B33DD562a48a84b54C48F00C`](https://basescan.org/address/0x2CDE9919e81b20B4B33DD562a48a84b54C48F00C) | 293,656,323.85 | 29.37% | Vesting (mixed schedules) |
| · Team re-lock (26 Mar 2026) | 127,000,000 | 12.70% | 🔒 cliff 26 Mar 2027, end 25 Mar 2029 |
| · Reserves | 99,945,543 + 699,735 redeemable | ~10.06% | Vesting to 11 Nov 2028 |
| · Investors 4 | 28,167,986 + 197,214 redeemable | ~2.84% | Vesting to 11 Nov 2028 |
| · Investors 1–3 (50 plans) | 0 + 5,550,146 unclaimed | 0.56% | 🔓 fully vested 11 Feb 2026 |
| Cluster wallet [`0x0c3eA09eD6798BFF724588e07EACA8278AD64E07`](https://basescan.org/address/0x0c3eA09eD6798BFF724588e07EACA8278AD64E07) ([Arkham](https://intel.arkm.com/explorer/address/0x0c3eA09eD6798BFF724588e07EACA8278AD64E07)) | 3,842,840 on 12 Nov → **222,035 on Base, 15 Nov** (sent out 13 Nov, see Selling) | 0.02% | 🔓 liquid. Arkham: no entity; tags Whale, Contract Deployer, ERC20 Token Deployer; shows **10.222M EDEL** across the chains it tracks (Base figure is [Tier A]; the rest is [Unverified]) |
| Same wallet: new-pool LP | 60,497.87 of 61,331.64 LP (~98.6%) | — | 🔓 none locked |
| OFT adapter owner (EOA) [`0x9a1f4408252d524419c2d8ccb4845e47799c1376`](https://basescan.org/address/0x9a1f4408252d524419c2d8ccb4845e47799c1376) | 980,461 | 0.10% | 🔓 |
| MiCAR "issuer retained" | 150,000,000 | 15% | Matches reserves lock |

Snapshot: Base block 56,602,263 (12 Nov 2026, 12:13 PM MST) and 13 Nov re-reads.

**What it means:** About 29% sits in vesting, and one wallet that the team uses controls almost all of the main pool's liquidity with no lock.

## 📉 Selling behavior — Do insiders sell into pumps? · 3/10 · ❌ FAIL

| Date (MST) | Event | Evidence | Verdict |
|---|---|---|---|
| 12 Nov 2025 10:00 AM | Deploy tx [tx `0x66505d60…0e86e`](https://basescan.org/tx/0x66505d60309bb82c419ec80865e66b010773125122fe7075604ac8eb7790e86e) swapped 5.622 ETH for **602,385,686 EDEL (60.24%)** behind a 50% levy that paid the deployer's own chosen wallet | [Tier A] Base receipt | Insider acquisition at launch |
| 12 Nov 2025 | 100 deployer-chosen levy wallets collected ~195M EDEL from outside buyers and **sold it into Uniswap V3 pool [`0x97fcf528…3c06`](https://basescan.org/address/0x97fcf52883266c822538e34af7764773c1323c06)** within ~1,100 blocks. All 100 hold 0 today | [Tier A] Base logs | Insider-linked dumping at launch (not a "pump window" under the 5-day test) |
| 12 Nov 2025 | Funder sent 53,799,721 EDEL to 63 unknown addresses | [Tier A] logs · destinations [Unverified] | Open |
| 12 Nov 2026 3:17–3:26 PM | Official Aerodrome LP lock expired 2:23 PM; `0x0c3e` withdrew 60,219.35 LP, took 162.48 WETH + 22.37M EDEL (~$656k), re-deposited into new pool [`0xb01cc306…0a33`](https://basescan.org/address/0xb01cc306bc018535aa0425efa0cf735008100a33) (created 28 Oct by [`0x859bc5fe…`](https://basescan.org/address/0x859bc5fe903dfe749fe3331512ff7297d2e924f3)). **No sale in those five txs.** No announcement | [Tier A] Base receipts, e.g. [tx `withdraw`](https://basescan.org/tx/0xad6a51cd504d0419ea0df25cc53ad05ca222c0d0a578f7fa9ac49edd9b3f7989) · [tx `re-deposit`](https://basescan.org/tx/0x8858621d35f0c64e01a031b9473151e95bf008de57c971d5ef1dc8a1ece88aae) · [tx `withdraw 2`](https://basescan.org/tx/0x6197c90a1a2387f0a23ff2c05a08378116bc1c3d8ec11c86d2a7f9dec0710582) · [tx `re-deposit 2`](https://basescan.org/tx/0x9cc37529f0dae68d83f41a2bce5468fad77658f40803b23834dcd3e9da437313) | Liquidity pulled and re-parked under one wallet |
| 12 Nov 2026 8:31 AM | Team: "$300k worth of $EDEL tokens have been stolen and sold"; MEXC and BloFin blocked the rest | [Tier A] official X | Second incident |
| 12 Nov 2026 6:15–8:21 AM (13:15–15:21 UTC) | `0x0c3e` itself signed a transfer of **11,507,480 EDEL** to contract [`0xba2b4157…3ef2`](https://basescan.org/address/0xba2b4157c594d32c0ea402472ca3cc896e0b3ef2) ([tx `0x4d2937f6852f…`](https://basescan.org/tx/0x4d2937f6852ff859d98285139c8a56aeb5fa51bb661a55eb6757083090417b66)). With 5,635,377 more from contract [`0xe99f8380…0730`](https://basescan.org/address/0xe99f8380a3821f523dee97ec42f94b0fc8040730) ([tx `0x595f3166…`](https://basescan.org/tx/0x595f31664ea8eac6e33957c44b73bda1fe158df92905eff28b587696709e6046)), `0xba2b…` sent **17,142,857 EDEL** to contract [`0x6008a44f…f019`](https://basescan.org/address/0x6008a44fa5160256f4cf36bf17d50d9fac1cf019) (13:47 UTC, [tx `0xf9221f66…`](https://basescan.org/tx/0xf9221f6608171eb6fd2eb8dbf79dc9e60ec2a164ca107c9ef8c7ca5ebda95746)), which split it within 1.5 h: 7,002,867 EDEL to [`0x887dab59…65fa`](https://basescan.org/address/0x887dab59f0b45df625b2fa5becd2141f092865fa) ([tx `0x60be1417…`](https://basescan.org/tx/0x60be141720a5c98067fa161b5d4838cb94eba638447821f91d602808622bcc17)); `0x887d…` also got 4.3M from [`0x9494…`](https://basescan.org/address/0x94942fd66dbf788bb98b6c83727c160fc6d82421) just before that hop ([tx `4.3M`](https://basescan.org/tx/0xbbd4ff30485ac874d82f8c693882a17c11534b871ec6c2c30705bace5277cdc8)) and **sold 11.30M in total into the old official pool [`0x566bee…5A31`](https://basescan.org/address/0x566bee7ef7b39f29d150ab3be6b6242c17cc5a31)** (swaps 15:17–15:27 UTC: the 4.3M first, then the 7.0M; e.g. [tx `first`](https://basescan.org/tx/0x97a243a901f9ea7b68d04b9f32b88c8c1a095cd681f2c1c2624ef17e03f250dc) · [tx `last`](https://basescan.org/tx/0x4d903d18fb711f714e57af2aaf1df80d36e86cdbae03f7e20b6464433b50eb9d)); 3.0M via [`0xf2e5a903…`](https://basescan.org/address/0xf2e5a903e7622e7262bf5b533875a234232dabdd) to [`0x4e3ae00e…1b60`](https://basescan.org/address/0x4e3ae00e8323558fa5cac04b152238924aa31b60) ([tx `1M`](https://basescan.org/tx/0x439dc067e57f78c05947fb2c49e76318f52dc0fedd3da2e4c2e9cc1832d03644) · [tx `2M`](https://basescan.org/tx/0x9d439da6213a567de0c57921387abaeff19db291d2341e8d027481fe7aa1bd74); 2.59M txs, 297 ETH: exchange-scale hot wallet, label Not found); 1.14M via [`0x5f9d5a2d…`](https://basescan.org/address/0x5f9d5a2d855ff9414d2f3671a9400bce50cabf03) to [`0x7ff8bbf9…cce5`](https://basescan.org/address/0x7ff8bbf9c8ab106db589e7863fb100525f61cce5) ([tx `0.5M`](https://basescan.org/tx/0x7ca67ed87bb76fb389ef8a87faf40c3b6bf0b78c3bb1da9226a99dac753b13d3); 30,502 txs, exchange-like); 6.0M to contract [`0x94942fd6…`](https://basescan.org/address/0x94942fd66dbf788bb98b6c83727c160fc6d82421) ([tx `0x06160dab…`](https://basescan.org/tx/0x06160dab4477628fd2262403fea179c86bae798d375c82fd9c1c93584903828b); 4.3M of that went to `0x887d…` in one transfer, the rest in ~100k pieces) | [Tier A] Base RPC logs and receipts, read 15 Nov 2026 ~11:20 AM MST | **17.14M EDEL ≈ $300k at ~$0.0177, the same figure the team gave for the "theft" an hour later. It left from the team-cluster wallet itself** |
| 13 Nov 2026 4:58 AM (11:58 UTC) | `0x0c3e` sent its remaining **3,842,840 EDEL** to EOA [`0xd3655c7f…F0A9`](https://basescan.org/address/0xd3655c7f473358e731C4B11DD884F664b0F7f0A9) ([tx `0x486e1042…`](https://basescan.org/tx/0x486e10424a2cac8176c6f3ef2fa92c6ae2b2ffbc7958d1c86eb1f978f72d5ca6); Arkham: "2d ago" to `0xd3655c…`, [Arkham](https://intel.arkm.com/explorer/address/0xd3655c7f473358e731C4B11DD884F664b0F7f0A9)), which had just received 8,928,723 from `0xe99f…` ([tx `0xa46fc202…`](https://basescan.org/tx/0xa46fc202f787416c3c803d1b7c93194531c9c1a7ef61a113b72f3ef48d5b2474)). `0xd3655c…` sent 7,407,397 to [`0xd103b996…8d4b`](https://basescan.org/address/0xd103b9963b404da18ea6389c56250d4cd0618d4b) ([tx `0x5489e652…`](https://basescan.org/tx/0x5489e6529f5916ffc313e73b6486b4991a49004d4b99568dba1bea2f330179c3)), which **sold it into the new pool [`0xb01cc306…0a33`](https://basescan.org/address/0xb01cc306bc018535aa0425efa0cf735008100a33)** (that `0x0c3e` controls) in 100k–1M pieces from 13:13 UTC (e.g. [tx `1M`](https://basescan.org/tx/0x04cdb1739172cf84409d48fa733c631d643b24ca665fe025d12a07803ec7de23) · [tx `0.5M`](https://basescan.org/tx/0x38de90cce2d93289937946407a5cd937e1dfbb021d83b36467c215db925da0c8)) | [Tier A] Base RPC logs | Team-cluster tokens sold into the team-controlled pool the day after the "theft" notice |

- Formal pump test (Real Rails v69): 97 windows of ≥10% over 5 daily closes since launch. **No two-label team → exchange deposit found.** Year-long Base routing only partly recovered.
- **12–13 Nov 2026 were not pump days** (5-day moves −24.3% and −36.5%), so the new trace does not change the pump test.
- **Was 12 Nov the theft?** The amount and timing fit the team's "$300k stolen and sold" post, and the coins came out of `0x0c3e`, a wallet the team uses (it pulled the official LP the same afternoon at 3:17 PM MST). Either the key of a team wallet that also controls ~98.6% of the main pool's LP was compromised, or the "theft" left from a team-controlled wallet. Which one is [Unverified]; the team's post-mortem has not appeared.
- **Arkham on `0x0c3e`** ([Tier B] Arkham, read 15 Nov 2026 ~11:05 AM MST (signed-in account)): no named entity (Titan Labs is not shown); its ~30-day exchange panel shows deposits to **Kraken $12.0k and MEXC $7.48k** and a **Bitunix withdrawal of $19.8k**, but not which tokens or chains. On Base, `0x0c3e` made no EDEL transfer to an exchange-type address from 9 Nov 2026 11:12 AM MST to 15 Nov (all 21 EDEL transfers read); earlier weeks of the Arkham window were not re-read on-chain (see Open items).

**What it means:** Still no proven sale into a pump, but insider-chosen wallets dumped outside buyers' tax at launch, the official liquidity was pulled without a word, and on 12–13 Nov about 15.3M EDEL left the team-cluster wallet and, together with ~14.6M from contract `0xe99f…` that moved alongside it, was sold on DEXs or sent to exchange-scale wallets within hours, whether by the team or by whoever took its key. Treat as hostile until shown otherwise. Score unchanged at 3/10 (already a gate fail).

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from MEXC EDELUSDT UTC daily closes, re-run 16 Nov 2026 with scripts/pump_day_test.py (87 of 330 days); the body's earlier count used the report's own 5-close window test.

## 📊 Tokenomics & supply · 3/10 · ❌ FAIL

| Item | Value | Source |
|---|---|---|
| Total supply | 1,000,000,000 (Base canonical, fixed, no mint/pause/blacklist) | [Tier A] Sourcify + RPC |
| Bridged copies | ETH OFT 8.51M · BNB OFT 5.86M · Solana 27.99M · Robinhood Chain 55.11M | [Tier A] RPC |
| Base OFT adapter lockbox | 97.45M (balances to remotes within ~0.02%) | [Tier A] |
| Solana mint authority | **Still set** (`2zw5h8BMFA29tp1DN9m9itiL8QmkKazeEynGc6WFN9ra`) | [Tier A] Solana RPC |
| Official tokenomics post | Investors 15.8%, 10% TGE then 12-month linear | [Tier A] official X, 13 Nov 2025 |
| On-chain reality | Investors 1–3 vested in **3 months**, not 12. Percentages sum to 99.2% | [Tier A] Hedgey decode |
| Burns | No schedule; dead balance 67.76 EDEL | [Tier A] |
| Upcoming | Team cliff 26 Mar 2027; reserves + Investors 4 through Nov 2028 | [Tier A] |

**What it means:** The Base token is clean code. The schedule around it does not match what the team posted.

## 💧 Liquidity & market · 4/10 · ❌ FAIL

| Pool | Reserves | Indicative USD | Who controls LP |
|---|---|---:|---|
| New Aerodrome V2 WETH/EDEL [`0xb01cc306…0a33`](https://basescan.org/address/0xb01cc306bc018535aa0425efa0cf735008100a33) (12 Nov read) | 165.40 WETH + 22.74M EDEL | ~$667k | `0x0c3e` ~98.6%, unlocked |
| Old official pool [`0x566bee…5A31`](https://basescan.org/address/0x566bee7ef7b39f29d150ab3be6b6242c17cc5a31) | 3.89 WETH + 532,605 EDEL | ~$15.7k | Locker balance 0 |

- 24h volume $708,941; price −52.5% over 7 days.

**What it means:** There is depth today, but the owner of almost all of it can withdraw at will.

## 🧑‍💻 Product & development · 3/10 · ❌ FAIL

- White paper: Aave V3-style lending for tokenized stocks/RWAs. **Officially sunset 11 Aug 2026** ("We sunset EVM lending as our vision expanded").
- Live: Canton instruments (SPYe, QQQe, NVDAe, SPCXe, EDELx) listed on Cantex; Markets API up and empty.
- GitHub `Edel-Finance`: 4 public repos; `edel-v3-core` is a retitled Aave V3 fork; `edel-ai-config` pushed 6 Nov 2026.

**What it means:** The flagship product is gone and the replacement has no users yet.

## 🤝 Adoption & customers · 1/10 · ❌ FAIL

- Confirmed: Cantex listing, Aerodrome pool, LayerZero OFTs.
- [Unverified] Anchorage, Flowdesk, DTCC working group, Ondo, Chainlink, a live Kraken listing — none confirmed by those parties.
- Self-reported volume, APY and user counts: [Unverified].

**What it means:** No paying customer you can point to.

## 🛡️ Security & audits · 1/10 · ❌ FAIL

| Incident | Date | Loss | Status |
|---|---|---|---|
| Lending price-feed exploit, [tx `0xe2320086…2612`](https://basescan.org/tx/0xe2320086b2815d21b0927839bd0e306466c29a68d38d5361e99dd21ec5472612) | 30 Jun 2026, 5:24 PM MST | ~$403k bad debt (official); 204,215.57 USDC net to attacker | Tranche 1 repaid 205,878.53 USDC (51%) to 238 wallets; tranche 2 **never created** |
| "$300k EDEL stolen and sold" | 12 Nov 2026 | ~$300k (official) | Post-mortem promised. **Likely route now found on-chain:** 17.14M EDEL from team-cluster wallet `0x0c3e` ([tx `first move`](https://basescan.org/tx/0x4d2937f6852ff859d98285139c8a56aeb5fa51bb661a55eb6757083090417b66)) via `0xba2b…` and `0x6008…` ([tx `17.14M hop`](https://basescan.org/tx/0xf9221f6608171eb6fd2eb8dbf79dc9e60ec2a164ca107c9ef8c7ca5ebda95746)), sold or sent to exchange-scale wallets 6:51–8:21 AM MST (see Selling) [route Tier A; "theft" label Unverified] |

- "Trust & Security" page lists **seven contract IDs that do not exist** (six empty EVM addresses, one invalid Solana key).
- The "full protocol audit" (Adevar) is a 3-day deployment-script review: 0 Fixed, 0 Acknowledged.

**What it means:** Two incidents in five months, half-paid restitution, and a fake contract list on a page titled "Built to Be Verified."

## ⚖️ Regulatory · 4/10 · ❌ FAIL

- MiCAR white paper **notified** 14 Jan 2026 (home state Ireland). A notification is not a licence or an approval.
- No licence found on any regulator register. No court records found.

**What it means:** Paperwork exists; no regulator has vetted anything.

## 📅 Catalysts & calendar · 2/10 · ❌ FAIL

| Date | Event |
|---|---|
| Pending | Post-mortem on the 12 Nov theft |
| Pending | Merkl restitution tranche 2 (promised for "next week" on 7 Jul 2026) |
| 26 Mar 2027 | Team re-lock cliff (127M) |
| Through 11 Nov 2028 | Reserves + Investors 4 vesting |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit on the protocol | 🔴 **Tripped twice** (30 Jun [tx `exploit tx`](https://basescan.org/tx/0xe2320086b2815d21b0927839bd0e306466c29a68d38d5361e99dd21ec5472612) and 12 Nov 2026 [tx `route start`](https://basescan.org/tx/0x4d2937f6852ff859d98285139c8a56aeb5fa51bb661a55eb6757083090417b66)) |
| Official liquidity pulled or unlocked | 🔴 **Tripped** (12 Nov 2026: [tx `LP withdraw`](https://basescan.org/tx/0xad6a51cd504d0419ea0df25cc53ad05ca222c0d0a578f7fa9ac49edd9b3f7989) · [tx `re-deposit`](https://basescan.org/tx/0x8858621d35f0c64e01a031b9473151e95bf008de57c971d5ef1dc8a1ece88aae)) |
| Founder or director exit | 🟢 None found |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| Team-cluster wallet (12–13 Nov 2026 outflows) | Team cluster | Base chain trace | medium | no | Selling: the score of 3 rests on proven launch-tax dumping and pulled liquidity, not on a pump-day sale |

## 📚 Sources

- [Tier A] Methodology update 16 Nov 2026: no new Arkham lookups; the attribution table uses evidence already cited in this report.
- [Tier A] Base RPC reads and receipts (launch, Hedgey, UNCX, LP migration), 12–13 Nov 2026
- [Tier A] [MiCAR white paper](https://assets.edel.finance/docs/2026-01-14-White-paper-Edel-FFG-R2MQ3JKN7.xhtml) · [GLEIF](https://search.gleif.org/#/record/529900E9GA8R99VOHV41)
- [Tier A] [docs.edel.finance](https://docs.edel.finance) · [terms](https://docs.edel.finance/legal/terms)
- [Tier A] Official X @edeldotfinance (statuses 2072154468058022033, 2074732155201097928, 2087168780669538679, 2120902181104611616, 2120908165168422923, 1989009678702088366)
- [Tier A] DefiLlama `edel` fees/revenue/TVL · Merkl campaign API
- [Tier A] Swiss SHAB / Zefix; UK Companies House 11443641
- [Tier A] CoinGecko `edel`, 14 Nov 2026 9:08 AM MST
- [Tier B] DL News 27 Nov 2025 and Cointelegraph (Bubblemaps sniping claim; on-chain first-60-block count is 19.18%, not 30%)
- [Tier A] Base RPC (`base-rpc.publicnode.com`, `mainnet.base.org`): EDEL Transfer logs to/from [`0x0c3e`](https://basescan.org/address/0x0c3eA09eD6798BFF724588e07EACA8278AD64E07), [`0xba2b…`](https://basescan.org/address/0xba2b4157c594d32c0ea402472ca3cc896e0b3ef2), [`0x6008…`](https://basescan.org/address/0x6008a44fa5160256f4cf36bf17d50d9fac1cf019), [`0xd3655c…`](https://basescan.org/address/0xd3655c7f473358e731C4B11DD884F664b0F7f0A9), [`0xd103…`](https://basescan.org/address/0xd103b9963b404da18ea6389c56250d4cd0618d4b), [`0xe99f…`](https://basescan.org/address/0xe99f8380a3821f523dee97ec42f94b0fc8040730) and the next hop (re-pulled 15 Nov 2026 ~12:10 PM MST for exact tx hashes, all linked inline); `balanceOf`, `eth_getCode`, nonces; 12–15 Nov 2026, read 15 Nov 2026 ~11:20 AM MST
- [Tier B] Arkham, read 15 Nov 2026 ~11:05 AM MST (signed-in account): [`0x0c3e` address page](https://intel.arkm.com/explorer/address/0x0c3eA09eD6798BFF724588e07EACA8278AD64E07) no entity, tags Whale / Contract Deployer / ERC20 Token Deployer, 10.222M EDEL, exchange panel Kraken $12.0k + MEXC $7.48k deposits, Bitunix $19.8k withdrawal. Limits: relative ages only; ~30-day exchange window, all-time is Enterprise-locked; first page of 2,141 transfers read
- [Unverified] Investors; partner claims; whether the 12 Nov route was a theft or a team move; owners of `0x4e3ae00e…` and `0x7ff8bbf9…`; 63 TGE-day recipients

## 🔗 Evidence trail

*Strongest findings first. Each link opens the primary record (block explorer) or the label source (Arkham) for the claim, so any number can be checked by hand.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| **12 Nov 2026 13:15 UTC:** `0x0c3e` sends 11,507,480 EDEL to contract `0xba2b…` | [tx `0x4d2937f6…`](https://basescan.org/tx/0x4d2937f6852ff859d98285139c8a56aeb5fa51bb661a55eb6757083090417b66) · [0x0c3e](https://basescan.org/address/0x0c3eA09eD6798BFF724588e07EACA8278AD64E07) · [Arkham (no entity, Whale/Deployer tags)](https://intel.arkm.com/explorer/address/0x0c3eA09eD6798BFF724588e07EACA8278AD64E07) | A (+B label) | 15 Nov 2026 ~12:10 PM MST |
| 13:43 UTC: +5,635,377 EDEL from contract `0xe99f…` into `0xba2b…` | [tx `0x595f3166…`](https://basescan.org/tx/0x595f31664ea8eac6e33957c44b73bda1fe158df92905eff28b587696709e6046) · [0xe99f…](https://basescan.org/address/0xe99f8380a3821f523dee97ec42f94b0fc8040730) | A | 15 Nov 2026 |
| 13:47 UTC: `0xba2b…` → `0x6008…` **17,142,857 EDEL** (≈ $300k at ~$0.0177) | [tx `0xf9221f66…`](https://basescan.org/tx/0xf9221f6608171eb6fd2eb8dbf79dc9e60ec2a164ca107c9ef8c7ca5ebda95746) · [0x6008…](https://basescan.org/address/0x6008a44fa5160256f4cf36bf17d50d9fac1cf019) | A | 15 Nov 2026 |
| 15:15 UTC: `0x9494…` → `0x887d…` 4.3M; 15:21 UTC: `0x6008…` → `0x887d…` 7,002,867 EDEL; `0x887d…` sold 11.30M into the old official pool `0x566b…` in ~1M swaps (15:17–15:27 UTC: the 4.3M first, then the 7.0M) | [tx `4.3M`](https://basescan.org/tx/0xbbd4ff30485ac874d82f8c693882a17c11534b871ec6c2c30705bace5277cdc8) · [tx `7.0M hop`](https://basescan.org/tx/0x60be141720a5c98067fa161b5d4838cb94eba638447821f91d602808622bcc17) · sales [tx `1`](https://basescan.org/tx/0x97a243a901f9ea7b68d04b9f32b88c8c1a095cd681f2c1c2624ef17e03f250dc) · [tx `2`](https://basescan.org/tx/0xefdc78f0f1c0d0a5232f40d5eda1fa2ee4dd7109416aa75d3e1af031cc178ab0) · [tx `last`](https://basescan.org/tx/0x4d903d18fb711f714e57af2aaf1df80d36e86cdbae03f7e20b6464433b50eb9d) · [pool](https://basescan.org/address/0x566bee7ef7b39f29d150ab3be6b6242c17cc5a31) | A | 15 Nov 2026 |
| 13:51–14:40 UTC: 3.0M via `0xf2e5…` to exchange-scale `0x4e3a…` (label Not found) | [tx `1M in`](https://basescan.org/tx/0xf7c505d5232e3ffa73f789499d8ffde4550c86dea538139775c7dd40dd46d7ea) · [tx `1M out`](https://basescan.org/tx/0x439dc067e57f78c05947fb2c49e76318f52dc0fedd3da2e4c2e9cc1832d03644) · [tx `2M in`](https://basescan.org/tx/0xaab8102c36534f421cf155402f3cac3893632a4ce34ccb1f4d5e4fb245cfaead) · [tx `2M out`](https://basescan.org/tx/0x9d439da6213a567de0c57921387abaeff19db291d2341e8d027481fe7aa1bd74) · [0x4e3a…](https://basescan.org/address/0x4e3ae00e8323558fa5cac04b152238924aa31b60) | A | 15 Nov 2026 |
| 14:18–15:21 UTC: 1.14M via `0x5f9d…` to exchange-like `0x7ff8…` | [tx `0.5M in`](https://basescan.org/tx/0x77929bd4beea76f9bfe9f9342a8318e89e80114ae69ac553ccf519c15d8189df) · [tx `0.5M out`](https://basescan.org/tx/0x7ca67ed87bb76fb389ef8a87faf40c3b6bf0b78c3bb1da9226a99dac753b13d3) · [0x7ff8…](https://basescan.org/address/0x7ff8bbf9c8ab106db589e7863fb100525f61cce5) | A | 15 Nov 2026 |
| 14:51 UTC: 6.0M to contract `0x9494…`; 4.3M went to `0x887d…` at 15:15 UTC, the rest in ~100k pieces | [tx `0x06160dab…`](https://basescan.org/tx/0x06160dab4477628fd2262403fea179c86bae798d375c82fd9c1c93584903828b) · [tx `4.3M`](https://basescan.org/tx/0xbbd4ff30485ac874d82f8c693882a17c11534b871ec6c2c30705bace5277cdc8) · [0x9494…](https://basescan.org/address/0x94942fd66dbf788bb98b6c83727c160fc6d82421) | A | 15 Nov 2026 |
| 13 Nov 11:58 UTC: `0x0c3e` sends last 3,842,840 EDEL to `0xd365…`; `0xd365…` → `0xd103…` 7.41M, sold into the `0x0c3e`-controlled new pool | [tx `0x0c3e → 0xd365`](https://basescan.org/tx/0x486e10424a2cac8176c6f3ef2fa92c6ae2b2ffbc7958d1c86eb1f978f72d5ca6) · [tx `0xe99f → 0xd365`](https://basescan.org/tx/0xa46fc202f787416c3c803d1b7c93194531c9c1a7ef61a113b72f3ef48d5b2474) · [tx `0xd365 → 0xd103`](https://basescan.org/tx/0x5489e6529f5916ffc313e73b6486b4991a49004d4b99568dba1bea2f330179c3) · sales [tx `1M`](https://basescan.org/tx/0x04cdb1739172cf84409d48fa733c631d643b24ca665fe025d12a07803ec7de23) · [tx `0.5M`](https://basescan.org/tx/0x38de90cce2d93289937946407a5cd937e1dfbb021d83b36467c215db925da0c8) · [Arkham 0xd365](https://intel.arkm.com/explorer/address/0xd3655c7f473358e731C4B11DD884F664b0F7f0A9) | A (+B) | 15 Nov 2026 |
| 12 Nov 22:17–22:26 UTC (3:17–3:26 PM MST): official LP pulled by `0x0c3e` after lock expiry and re-parked in pool `0xb01c…` it controls (~98.6% of LP, unlocked) | [tx `withdraw 1`](https://basescan.org/tx/0xad6a51cd504d0419ea0df25cc53ad05ca222c0d0a578f7fa9ac49edd9b3f7989) · [tx `re-deposit 1`](https://basescan.org/tx/0x8858621d35f0c64e01a031b9473151e95bf008de57c971d5ef1dc8a1ece88aae) · [tx `withdraw 2`](https://basescan.org/tx/0x6197c90a1a2387f0a23ff2c05a08378116bc1c3d8ec11c86d2a7f9dec0710582) · [tx `re-deposit 2`](https://basescan.org/tx/0x9cc37529f0dae68d83f41a2bce5468fad77658f40803b23834dcd3e9da437313) · [new pool](https://basescan.org/address/0xb01cc306bc018535aa0425efa0cf735008100a33) | A | 13–15 Nov 2026 |
| Launch tx took 602.39M EDEL (60.24%) behind a 50% levy | [tx `0x66505d60…`](https://basescan.org/tx/0x66505d60309bb82c419ec80865e66b010773125122fe7075604ac8eb7790e86e) · [launch pool](https://basescan.org/address/0x97fcf52883266c822538e34af7764773c1323c06) | A | 12 Nov 2026 |
| 30 Jun 2026 lending exploit (~$403k bad debt) | [tx `0xe2320086…`](https://basescan.org/tx/0xe2320086b2815d21b0927839bd0e306466c29a68d38d5361e99dd21ec5472612) | A | 12 Nov 2026 |
| Arkham exchange panel for `0x0c3e`: Kraken $12.0k + MEXC $7.48k deposits, Bitunix $19.8k withdrawal (tokens/chains not shown) | [Arkham](https://intel.arkm.com/explorer/address/0x0c3eA09eD6798BFF724588e07EACA8278AD64E07) | B (one source) | 15 Nov 2026 ~11:05 AM MST |
| Hedgey vesting holds 293.66M EDEL (29.4%) | [Hedgey contract](https://basescan.org/address/0x2CDE9919e81b20B4B33DD562a48a84b54C48F00C) · [EDEL holdings](https://basescan.org/token/0xFb31f85A8367210B2e4Ed2360D2dA9Dc2D2Ccc95?a=0x2CDE9919e81b20B4B33DD562a48a84b54C48F00C) | A | 12 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exact path to close it | Cost / access |
|---|---|---|---|
| 1 | Was the 12 Nov 17.14M EDEL route a theft or a team move? | Team post-mortem (promised); ask which wallet was compromised; check whether `0x0c3e` signs anything after 13 Nov that a thief would not (e.g. LP management) | Free / request to team |
| 2 | Which tokens and chains are behind Arkham's Kraken $12.0k / MEXC $7.48k deposits and Bitunix withdrawal for `0x0c3e` | Arkham transfer list filtered by exchange (Enterprise for all-time); otherwise scan `0x0c3e` on Ethereum, BNB Chain and Robinhood Chain (EDEL OFTs) for sends to exchange-labelled addresses | Arkham account (have) · free RPC |
| 3 | Owners of `0x4e3ae00e…1b60` and `0x7ff8bbf9…cce5` | Arkham or Basescan name tags | Arkham account (have) |
| 4 | Where the other ~6.8M EDEL of Arkham's 10.222M for `0x0c3e` sits | Arkham portfolio by chain; `balanceOf` on each OFT chain | Arkham account (have) · free |
| 5 | Restitution tranche 2 | Merkl campaign API for Edel | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
