---
ticker: CFG
name: Centrifuge
chain: ethereum
contract: "0xcccCCCcCCC33D538DBC2EE4fEab0a7A1FF4e8A94"
overall_score: 4.4
overall_verdict: FAIL
section_scores:
  revenue: 3
  foundation_team: 6
  insider_holdings: 3
  selling_behavior: 4
  tokenomics_supply: 3
  liquidity_market: 4
  product_development: 7
  adoption_customers: 7
  security_audits: 5
  regulatory: 5
  catalysts: 5
gates_failed: [revenue]
red_lines:
  hack_exploit: none found on the CFG token
  mint_path_live: "yes, by design (immutable InflationMinter mints ~3%/yr to treasury EOA 0xb3da; Root (48h delay) can add minters)"
  team_wallet_to_exchange_during_pump: "yes, small and partly explained (Centrifuge Treasury EOA 0xb3da sent 835k CFG to a Binance deposit on the 18 Mar 2026 pump day; its pump-day FalconX deposits on 26 Feb and 16 Mar 2026 were returned 1:1 within weeks; the CNF Safe's 23.06M to Gate on the 23 May 2025 pump day falls under CP149's disclosed exchange-migration purpose)"
  one_hop_sale_status: not_proven
  treasury_in_single_key_wallets: "yes (~117M CFG, ≈ 17% of supply, in two EOAs: 0xD052 106.07M and treasury 0xb3da 11.22M; docs call 10.5% of supply 'locked' incentives but no lock contract was found)"
  token_to_equity_conversion: "CP172 passed 10 Sep 2026; Centrifuge says it will wind down funding for CFG liquidity (listings, market-maker loans) after the conversion window"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "None of the business income reaches CFG and the team says none will; there is no burn, buyback, fee share or fee-funded staking yield."
pump_day_price_source: "Gate CFG/USDT daily closes"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions: []
price_usd: 0.07006
price_source: "CoinGecko, 16 Nov 2026 5:27 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### CFG · Overall grade **4.4 / 10 · ❌ FAIL**

**Summary:** Centrifuge is a real tokenization platform: Janus Henderson, Apollo and New York Life funds run on it, and DefiLlama counts $5.2M of protocol revenue in the last year. But **the CFG token gets none of it**, by the team's own words ("no buyback", "CFG does not directly confer economic rights"). Holders voted 98.5% for CP172, which lets KYC'd holders swap CFG 1:1 for shares in a Cayman company, after which Centrifuge says it will **stop funding CFG liquidity**. Supply inflates 3% a year to a single-key treasury wallet, and ~17% of supply sits in two plain EOAs. Revenue trips the hard gate.

**🚨 Top warning:** the token is being turned into a stub. Centrifuge's [CP172 FAQ](https://centrifuge.io/blog/centrifuge-releases-cp172-faqs) says that **"after the window closes, the company will wind down funding public token liquidity: listing agreements, market maker loans"**, that there will be **no buyback**, and that US holders must be accredited to convert. CP172 [passed on 10 Sep 2026](https://gov.centrifuge.io/t/cp172-exploring-token-to-equity-to-maximize-long-term-cfg-value/7525?page=9) with 73.3M CFG from 35 addresses, but no conversion window has been set. Meanwhile **~117M CFG (≈ 17% of supply) sits in two single-key EOAs**: [`0xD052…93Cb`](https://etherscan.io/address/0xD052A46b8e0C89fAcB393805E1917AfD20f293Cb) (106.07M, fed by the CP149 mint Safe and by migration mints, e.g. [59.8M on 4 Jun 2026](https://etherscan.io/tx/0x8c44d82dca81cd17cac72c2a32e4d0c004dc9523a945c16a5aa2601ebe40cac3)) and the **Centrifuge Treasury** [`0xb3da…1ab9`](https://etherscan.io/address/0xb3dacc732509ba6b7f25ad149e56ca44fe901ab9) (the hard-coded `target` of the [InflationMinter](https://etherscan.io/address/0x50a168cd6957e07b6de6c1a99b2f940475f70def#code)). The treasury put **835k CFG into a Binance deposit on the 18 Mar 2026 pump day** ([tx](https://etherscan.io/tx/0x82459d78436ead4718d8ec0fbcbf380edad6d7947e908dd5a013673fc1f0f864)). Every transfer is linked in the 🔗 Evidence trail below.

**Sections passed: 3 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 3/10 | ❌ FAIL |
| 🏛️ Foundation & team | 6/10 | ✅ PASS |
| 🪙 Foundation / team holdings | 3/10 | ❌ FAIL |
| 📉 Selling behavior | 4/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 3/10 | ❌ FAIL |
| 💧 Liquidity & market | 4/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 7/10 | ✅ PASS |
| 🤝 Adoption & customers | 7/10 | ✅ PASS |
| 🛡️ Security & audits | 5/10 | ❌ FAIL |
| ⚖️ Regulatory | 5/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 5/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 CFG · Centrifuge · 4.4 / 10 · ❌ FAIL

> **One line:** A real RWA tokenization business whose token gets no revenue and is being replaced by company shares. Supply inflates 3% a year into a single-key treasury, and the company plans to stop paying for CFG liquidity after the share conversion.

| 📊 Market (CoinGecko, 16 Nov 2026 5:27 AM MST) | 🔗 On-chain (Ethereum, 16 Nov 2026) |
|---|---|
| **Price** $0.07006 | **Token** [`0xcccC…8A94`](https://etherscan.io/address/0xcccCCCcCCC33D538DBC2EE4fEab0a7A1FF4e8A94#code) `CFG` (DelegationToken, wards auth, not a proxy) |
| **24h / 7d / 30d** 🔴 −2.4% / −20.8% / −44.8% · 1y −55.6% | **`totalSupply()`** 705,907,685 |
| **Market cap** $26.65M · **FDV** $47.6M (CoinGecko, on 680M) | **Circulating (CoinGecko)** 380,384,016 (54%) |
| **24h volume** $3.32M | **Wards** [Root](https://etherscan.io/address/0x7ed48c31f2fdc40d37407cbabf0870b2b688368f) (48h delay) · [InflationMinter](https://etherscan.io/address/0x50a168cd6957e07b6de6c1a99b2f940475f70def) |
| **ATH** $0.4004 (24 Aug 2025) · now −82.5% | **Treasury EOA** [`0xb3da…1ab9`](https://etherscan.io/address/0xb3dacc732509ba6b7f25ad149e56ca44fe901ab9) 11.22M · **EOA** [`0xD052…93Cb`](https://etherscan.io/address/0xD052A46b8e0C89fAcB393805E1917AfD20f293Cb) 106.07M |
| **Holders** 11,795 (Blockscout) | **Grove** [Foundation SubProxy](https://etherscan.io/address/0x1369f7b2b38c76B6478c0f0E66D94923421891Ba) 33.75M |

---

## 💰 Revenue — Does it make money? · 3/10 · ❌ FAIL

| Metric | Value | Source |
|---|---:|---|
| Fees, last 30 days / 1 year | **$3.16M / $57.7M** (fund-level fees across issuers) | [Tier A] [DefiLlama Centrifuge Protocol](https://defillama.com/protocol/centrifuge-protocol), read 16 Nov 2026 5:27 AM MST |
| Protocol revenue, last 30 days / 1 year | **$284.6k / $5.23M** | [Tier A] DefiLlama |
| Holders revenue | **$0** | [Tier A] DefiLlama `dailyHoldersRevenue` |
| Team's own words | "As a token, CFG does not directly confer economic rights to token holders" · "Will there be a buyback? No." | [Tier A] [CP172 FAQ](https://centrifuge.io/blog/centrifuge-releases-cp172-faqs) |
| TVL | $1B at end Q3 2026 (−38% QoQ) | [Tier A] [Centrifuge Q3 2026 recap](https://centrifuge.io/blog/centrifuge-q3-2026-recap) |

**What it means:** The business earns money (about 5x market cap on a P/S basis, cheap on paper), but none of it reaches CFG, and the team says none will. The value route it offers is to swap CFG for illiquid shares, with KYC, and accredited status for US holders. **3, which trips the Revenue gate.**

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** None of the business income reaches CFG and the team says none will; there is no burn, buyback, fee share or fee-funded staking yield.

## 🏛️ Foundation & team — Who is in charge? · 6/10 · ✅ PASS

| Item | Finding | Source |
|---|---|---|
| Entity | **Centrifuge Network Foundation, Inc.** (Cayman foundation company); under CP172 it would re-register as "Centrifuge, Inc." | [Tier A] [CP172 FAQ](https://centrifuge.io/blog/centrifuge-releases-cp172-faqs) |
| Governance | **CP171** (approved 3 Nov 2025) handed governance and oversight to the Foundation; the DAO "retains the ability to reassume" it | [Tier A] [Centrifuge docs](https://docs.centrifuge.io/getting-started/token-summary/) |
| People | CEO posted CP172 (17 Aug 2026). The board includes a Grove co-founder and a Janus Henderson executive [Tier B, Alea] | [Tier B] [Alea](https://alearesearch.io/newsletters/centrifuge-derwa-holders) |
| Disclosure rating | DefiLlama UTR: insider identities 9/10, **insider wallet disclosure 2/10, market-maker transparency 0/10** | [Tier B] [DefiLlama UTR](https://defillama.com/universal-token-rating/token/centrifuge-2) |

**What it means:** A known team and a real entity, but control is now centralised in the Foundation, whose board includes its largest customer (Grove). It publishes almost nothing about its wallets or market makers.

## 🪙 Foundation / team holdings — How many coins do they hold? · 3/10 · ❌ FAIL

| Bucket | CFG | Notes |
|---|---:|---|
| Published allocation (Jun 2026) | Ecosystem/treasury **14.3%** · Team **12%** (vests to May 2030) · Locked incentives **10.5%** (vest to Apr 2029) · other stakeholders (to Mar 2028) · released 54.6% | [Tier A] [Centrifuge docs](https://docs.centrifuge.io/getting-started/token-summary/) |
| EOA [`0xD052…93Cb`](https://etherscan.io/address/0xD052A46b8e0C89fAcB393805E1917AfD20f293Cb) (#1 holder) | **106,067,866 (15.0%)** | Got 72.04M from the CP149 Safe and 209.0M of migration mints (incl. [59.8M in the 4 Jun 2026 governance tx](https://etherscan.io/tx/0x8c44d82dca81cd17cac72c2a32e4d0c004dc9523a945c16a5aa2601ebe40cac3)); sends only to the treasury EOA (231M so far). **Single key**. Arkham: unlabelled, tagged Whale; does not name Centrifuge ([Arkham](https://intel.arkm.com/explorer/address/0xd052a46b8e0c89facb393805e1917afd20f293cb)) |
| Centrifuge Treasury EOA [`0xb3da…1ab9`](https://etherscan.io/address/0xb3dacc732509ba6b7f25ad149e56ca44fe901ab9) | 11,221,334 | Hard-coded `target()` of the [InflationMinter](https://etherscan.io/address/0x50a168cd6957e07b6de6c1a99b2f940475f70def#code); docs say inflation "accrue[s] to the Centrifuge Treasury". **Single key**. Arkham shows no Centrifuge label ([Arkham](https://intel.arkm.com/explorer/address/0xb3dacc732509ba6b7f25ad149e56ca44fe901ab9)); the treasury identity rests on the Tier A minter target |
| CP149 mint Safe [`0x30d3…0997`](https://etherscan.io/address/0x30d3bbae8623d0e9c0db5c27b82dcda39de40997) (2-of-6) | 128,150 | Got the [115M CP149 mint](https://etherscan.io/tx/0xb2feea2d885009aae9a629a8b73fadc9c487faf650acacedd4523c0433a781a6) that CP149 says goes "to the Centrifuge Network Foundation"; now nearly empty. Arkham shows only a tentative "Centrifuge?" tag on a signer, not a firm label ([Arkham](https://intel.arkm.com/explorer/address/0x30d3bbae8623d0e9c0db5c27b82dcda39de40997)) |
| Where team tokens sit | **Not found** | No vesting contract for the 12% team or 10.5% incentive buckets was found among the top holders [Unverified] |

**What it means:** The CP149 Safe passed most of its 115M to `0xD052…`, a plain EOA. So the "locked" incentives are locked by policy only: in code, one key could move them. About 17% of supply sits in two single-key wallets, and the 12% team allocation is not visible on-chain.

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL

*Pump test uses Gate CFG/USDT daily closes (UTC). 66 of the last 365 days were pump days. CFG listed on Upbit in late Feb 2026 and on Binance in mid-Mar 2026 [Tier B, Alea], which were its two biggest daily gains of the year.*

| Day (UTC) | Route | CFG | Close / 5-day change | Pump? | Outcome |
|---|---|---:|---:|---|---|
| 23 May 2025 | CNF Safe `0x30d3…` → Gate hot wallet [`0x0d07…`](https://etherscan.io/address/0x0d0707963952f2fba59dd06f2b425ace40b492fe) ([tx](https://etherscan.io/tx/0xbfe86a3b54b21c4536c6a6f52efd465545821000f2405a31ce51ba4cef6f8d58)) | 23,056,302 | $0.2094 / +11.0% | 🔴 Yes | Migration week; CP149 says these tokens "support the migration … with exchanges and market makers" |
| 27–28 May 2025 | CNF Safe → [`0x1136…509a`](https://etherscan.io/address/0x1136a49f3a1e3a3b6b2b6de30f8244d16f18509a) ([tx](https://etherscan.io/tx/0x1cf4f39fce6911964f8925dff8276c2b7408447632e1a98bb51704f850e46499)) → KuCoin 20 ([tx](https://etherscan.io/tx/0x5d189ba1144c3f6c95de35d29b87732d3e54b78e2b1f027b3b8f37eb29e39c8c)) | 23,413,205 | +8.9% | No | Same purpose |
| 26 Feb 2026 | **Treasury `0xb3da…`** → FalconX deposit [`0x64ac…85f7`](https://etherscan.io/address/0x64ac897b8b3cd9ee86d0b64363a290f66a7585f7) ([tx](https://etherscan.io/tx/0x34b1606f95a62c6304e2aefa9c4897b93d2525e99c79e91dcce6677d415a2d34)) | 3,125,000 | $0.1448 / **+60.4%** | 🔴 Yes | **Returned** by FalconX 1 on 5 Mar ([tx](https://etherscan.io/tx/0xb3d5c9d5f67f1cbc6eec9d9c167375ab31639a6fe322155e53abae774251d9b9)) |
| 16 Mar 2026 | Treasury → FalconX deposit ([tx](https://etherscan.io/tx/0x7c314124c541fd408c3c98bbc73d574559aea77f8f24067e5d9b7dfa8210d35e)) | 2,499,990 | $0.1878 / **+42.1%** | 🔴 Yes | **Returned** 25 Mar ([tx](https://etherscan.io/tx/0x45e73d275d7e1b84facb0723bbad2a20c05493204cf390c439e3dad0d5186632)) |
| 18 Mar 2026 | Treasury → Binance deposit [`0x0a36…d6f0`](https://etherscan.io/address/0x0a367f918340d47d36b21c93e9a2b6853cc9d6f0) ([tx](https://etherscan.io/tx/0x82459d78436ead4718d8ec0fbcbf380edad6d7947e908dd5a013673fc1f0f864)) | 834,989 | $0.1426 / +15.5% | 🔴 Yes | Not returned; no disclosure found |

- **FalconX in total:** the treasury sent 36.02M CFG to FalconX deposit `0x64ac…` in 16 transfers (Oct 2025 – Oct 2026). FalconX 1 sent back 15.69M, matching earlier deposits almost 1:1, which looks like a loan or collateral arrangement. **~20.3M has not come back**, including 13.2M in Sep–Oct 2026 ([e.g. 6.6M on 20 Oct](https://etherscan.io/tx/0xfd461009b3675337db377deb4b70c4bad57345ae07222df0d7b71412e2071da1)). The treasury also lent through [`0xaa9f…db3c`](https://etherscan.io/address/0xaa9f8b6c6d1ca0d5abd96357a7871864173edb3c) to **Wintermute 4**, which [returned 5.5M on 19 Oct 2026](https://etherscan.io/tx/0x32bd8787290aef092e8f73f6ee374f5d64562d984c3ea606897073e103d0e854).
- **Large non-pump transfers:** the treasury sent 43.99M to high-volume [`0x9938…e8d5`](https://etherscan.io/address/0x9938ee74ba7a5c1abcd157272a18fcfc9ec9e8d5) (which feeds OKX 219) on [3 Nov 2025](https://etherscan.io/tx/0x6748eb3c056e02e58640fd65170bacf8e9856c004125667d8d6df9eae79f9815), the day migration mints closed (−18.9% in 5 days), and 26.92M to [`0xa8c8…eeaf`](https://etherscan.io/address/0xa8c8feff4c02835684c86b01c7ab512bdaadeeaf) (which feeds Kraken 245/246) on [6 Oct 2025](https://etherscan.io/tx/0xd313ee7f0b15c5caea18f8e75b0efb3282260f38269a6061a92334d2cba50a5c). Both look like exchanges migrating customer balances. **Arkham ([Tier B] Arkham, read 16 Nov 2026 ~7:07–7:18 AM MST (signed-in account)) labels `0x9938…` an OKX Hot Wallet** ([Arkham](https://intel.arkm.com/explorer/address/0x9938ee74ba7a5c1abcd157272a18fcfc9ec9e8d5)) **and `0xa8c8…` a Kraken Hot Wallet** ([Arkham](https://intel.arkm.com/explorer/address/0xa8c8feff4c02835684c86b01c7ab512bdaadeeaf)), not market makers. With the Etherscan tags on where they forward (OKX 219, Kraken 245/246), that is two Tier B sources for exchange wallets. Moving 70.9M to exchange hot wallets during the migration, on non-pump days, fits customer-balance migration. Not counted as selling, and the score does not change.
- **Grove:** the treasury sent Grove's Foundation SubProxy 33.75M in Jun and Aug 2026 ([e.g.](https://etherscan.io/tx/0x3d92ccaece9f37f4400e624c4f5d078515a155748b3eb043c08f3da62f70d41c)). Grove disclosed a "37.8 million CFG" strategic position on [25 Aug 2026](https://grove.finance/blog/grove-announces-strategic-stake-in-centrifuge-ecosystem-deepening-long-term-partnership); the price was not disclosed.

**What it means:** The biggest pump-day moves were loans that came back, or migration support that CP149 disclosed. That leaves the 835k Binance deposit on a listing-week pump day, plus ~20M sitting with FalconX, with no counterparty disclosure (DefiLlama rates market-maker transparency 0/10). Under the 16 Nov 2026 one-hop amendment these moves have a published reason (CP149 exchange and market-maker support) and no proof of sale, so Selling is **4 (not proven)**, with no penalty and no hard gate.

- **One-hop amendment (16 Nov 2026):** Centrifuge published a plausible reason for this movement: [CP149](https://github.com/centrifuge/cps/blob/main/cps/CP149/CP149.md) says the minted tokens support the migration "with exchanges and market makers", and the [CP172 FAQ](https://centrifuge.io/blog/centrifuge-releases-cp172-faqs) lists listing agreements and market-maker loans. The 835k Binance deposit came in the listing week, and the FalconX loans were returned. (a) No: the Binance account is not attributed to the team. (b) No: no swap, proceeds return or statement shows a sale. Under the amended rule the one-hop link is no longer enough on its own, so Selling scores **4 (not proven)** with no silence penalty. This replaces the earlier penalty described above.

## 📊 Tokenomics & supply · 3/10 · ❌ FAIL

- **Extra mint at migration:** CP149 raised supply from 560.2M to 675M by minting **115M (+20.5%)** to the Foundation ([CP149](https://github.com/centrifuge/cps/blob/main/cps/CP149/CP149.md) · [mint tx](https://etherscan.io/tx/0xb2feea2d885009aae9a629a8b73fadc9c487faf650acacedd4523c0433a781a6)).
- **Perpetual inflation in code:** the [InflationMinter](https://etherscan.io/address/0x50a168cd6957e07b6de6c1a99b2f940475f70def#code) has immutable `rate` 566,665,722,130,821 per week (≈ 0.0567%/wk ≈ **3.0%/yr compounding**) and immutable `target` = treasury EOA `0xb3da…`. Recent mints: [5.12M on 4 Jun](https://etherscan.io/tx/0xd2f7dd2504565304da3c5b65a61d7ba440015b5e6d55bdb25c7077e0cc7db7e7), [3.17M on 3 Aug](https://etherscan.io/tx/0xfc52bee1bc7db5f761f46a2f71e9422e6125cdcaa36b8f688bab4535344e4566), [5.58M on 4 Nov 2026](https://etherscan.io/tx/0x26de7e34b8547b079f54f1dd090a4996f6c91702ff3c8859b5f88f9de557026d). CP172 says inflation stops only "once the conversion is complete".
- `totalSupply()` 705.9M vs 697.2M in the June docs (inflation since); ~1.50M burned at migration. CoinGecko counts 380M (54%) as circulating.

## 💧 Liquidity & market · 4/10 · ❌ FAIL

- $3.32M of volume in 24h on a $26.65M cap (12% turnover). Binance, OKX 219, Kraken 245/246, Gate, Bybit and Coinbase wallets are among the top holders. Arkham adds an **Upbit deposit** holding 48.70M ([Arkham](https://intel.arkm.com/explorer/address/0x40d31dd5682b4813899a19bfa5d7453048fa2201)). Arkham also shows these unlabelled whales: [`0x845f…5467`](https://etherscan.io/address/0x845f7623e756370e8d4e7d3ac8fb6ba6574d5467) (26.19M, funded by **Bitcoin Suisse** [`0x8C45…A46f`](https://etherscan.io/address/0x8C4558543804b97221Ff37bb903e13B8aEb1A46f), owner not named, [Arkham](https://intel.arkm.com/explorer/address/0x845f7623e756370e8d4e7d3ac8fb6ba6574d5467)); [`0xb185…df6d`](https://etherscan.io/address/0xb185814ec5a0823e712f47de957748f6e950df6d) (16.31M, funded by the treasury `0xb3da…`, owner not named, [Arkham](https://intel.arkm.com/explorer/address/0xb185814ec5a0823e712f47de957748f6e950df6d)); and [`0x3c71…0f54`](https://etherscan.io/address/0x3c716d252b53891753de883894ff29a9ebee0f54) (10.57M CFG plus 12.09M SYRUP, owner not named, [Arkham](https://intel.arkm.com/explorer/address/0x3c716d252b53891753de883894ff29a9ebee0f54)).
- **Forward risk:** Centrifuge says it will wind down "listing agreements, market maker loans, and the infrastructure around them" after the conversion window ([CP172 FAQ](https://centrifuge.io/blog/centrifuge-releases-cp172-faqs)). Expect thinner books for holders who keep CFG.

## 🧑‍💻 Product & development · 7/10 · ✅ PASS

- Centrifuge V3.3 institutional vaults; New York Life's HYB expanded to Solana and Avalanche; Janus Henderson announced its first institutional vault ([Q3 recap](https://centrifuge.io/blog/centrifuge-q3-2026-recap)).
- The token, Root and spells are verified on Etherscan, and Root shows regular governance spells. The old `centrifuge-chain` repo's last commit was 22 May 2025 (the chain is deprecated).

## 🤝 Adoption & customers · 7/10 · ✅ PASS

- Funds on Centrifuge include Janus Henderson JTRSY/JAAA, Apollo ACRDX and NYLIM HYB. Grove says $1.27B is deployed through Centrifuge ([Grove](https://grove.finance/blog/grove-announces-strategic-stake-in-centrifuge-ecosystem-deepening-long-term-partnership)).
- **Concentration:** Grove held 87–89% of fund value; ~$750M left in September 2026 [Tier B, Alea + Coindaro: two sources]. TVL fell 38% QoQ to $1B ([Tier A] Centrifuge).

## 🛡️ Security & audits · 5/10 · ❌ FAIL

- Audits are published on the [security docs page](https://docs.centrifuge.io/developer/security/) (DefiLlama UTR rates auditor disclosure 8/10). No exploit of the CFG token found.
- Token admin (Tier A): wards are the [Root](https://etherscan.io/address/0x7ed48c31f2fdc40d37407cbabf0870b2b688368f) (`delay()` = 172,800 s = **48h**) and the InflationMinter. Root's current wards include the Protocol Guardian, Token Recoverer and messaging contracts.
- **Weak spot:** ~117M CFG of treasury and incentive tokens in single-key EOAs (see Holdings).

## ⚖️ Regulatory · 5/10 · ❌ FAIL

- CP172 FAQ: CFG "not securities as a matter of Cayman Islands law"; the new shares **would be securities**; US persons must be Reg D accredited. Ogier is legal adviser [Tier B, Coindaro].
- The conversion's legal structure is not final. No regulator approval was found.

## 📅 Catalysts & calendar · 5/10 · ❌ FAIL

| Date | Event |
|---|---|
| TBA | Board and supervisor approval of the CP172 restructure; then a subscription window with KYC (none set as of 6 Nov 2026) |
| After the window | Centrifuge winds down CFG liquidity funding; 3% inflation ends once conversion completes |
| Quarterly | InflationMinter mints to the treasury |
| Ongoing | Grove / Ethena allocations; Janus Henderson US product (target within a year) |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | 🟡 Treasury 835k → [Binance deposit](https://etherscan.io/tx/0x82459d78436ead4718d8ec0fbcbf380edad6d7947e908dd5a013673fc1f0f864) on 18 Mar 2026; pump-day FalconX deposits were [returned](https://etherscan.io/tx/0xb3d5c9d5f67f1cbc6eec9d9c167375ab31639a6fe322155e53abae774251d9b9) |
| Live mint path | 🔴 Yes, by design: immutable 3%/yr [InflationMinter](https://etherscan.io/address/0x50a168cd6957e07b6de6c1a99b2f940475f70def#code) to an EOA; Root can add minters after a 48h delay |
| Treasury in single-key wallets | 🔴 ~117M CFG in [`0xD052…`](https://etherscan.io/address/0xD052A46b8e0C89fAcB393805E1917AfD20f293Cb) and [`0xb3da…`](https://etherscan.io/address/0xb3dacc732509ba6b7f25ad149e56ca44fe901ab9) |
| Token being replaced | 🔴 [CP172 passed](https://gov.centrifuge.io/t/cp172-exploring-token-to-equity-to-maximize-long-term-cfg-value/7525?page=9); liquidity funding to end after conversion |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| Treasury EOA `0xb3da…` | Centrifuge Treasury (receives the InflationMinter mint) | Etherscan + the immutable minter contract | high | yes (on-chain) | Selling: 834,989 CFG straight into Binance deposit [`0x0a36…d6f0`](https://etherscan.io/address/0x0a367f918340d47d36b21c93e9a2b6853cc9d6f0) on the 18 Mar 2026 pump day (+15.5%), not returned |
| CNF Safe → Gate (23 May 2025) | Centrifuge Network Foundation | CP149 disclosure | high | yes | None: disclosed exchange-migration purpose |
| Treasury → FalconX (26 Feb, 16 Mar 2026) | Centrifuge Treasury | Etherscan (returned 1:1) | high | yes | None: loans returned |

## 📚 Sources

- [Tier A] Methodology update 16 Nov 2026: no new Arkham lookups; the attribution table uses evidence already cited in this report.
- [Tier A] Etherscan v2 API `tokentx` full CFG history for `0xb3da…`, `0xD052…`, `0x30d3…`, `0x1136…`, `0x40D3…`, `0x845f…`, `0x01c7…`, `0x4e34…` and every deposit and hop named; `getLogs` for all 10,822 mint events, burns, Rely/Deny on the token and Rely on Root; `getsourcecode` for the token, InflationMinter and Root; read 16 Nov 2026 ~6:15–6:50 AM MST
- [Tier A] Ethereum RPC (publicnode): `totalSupply()`, `wards()`, InflationMinter `rate()`/`target()`/`period()`, Root `delay()`, Safe `getOwners()`/`getThreshold()`, balances, 16 Nov 2026
- [Tier B] Etherscan / Blockscout name tags, 16 Nov 2026: "Centrifuge: Root", "Grove: Foundation" / "Grove Subproxy", "Gate Deposit", "KuCoin 20", "FalconX Deposit", "FalconX 1", "Binance Deposit", "Wintermute 4", "OKX 219", "Kraken 245/246", "Centrifuge: Protocol Guardian"
- [Tier B] Arkham, read 16 Nov 2026 ~7:07–7:18 AM MST (signed-in account): OKX Hot Wallet [0x9938…](https://intel.arkm.com/explorer/address/0x9938ee74ba7a5c1abcd157272a18fcfc9ec9e8d5) · Kraken Hot Wallet [0xa8c8…](https://intel.arkm.com/explorer/address/0xa8c8feff4c02835684c86b01c7ab512bdaadeeaf) · Upbit Deposit [0x40D3…](https://intel.arkm.com/explorer/address/0x40d31dd5682b4813899a19bfa5d7453048fa2201) · Bitcoin Suisse-funded whale [0x845f…](https://intel.arkm.com/explorer/address/0x845f7623e756370e8d4e7d3ac8fb6ba6574d5467) · treasury-funded whale [0xB185…](https://intel.arkm.com/explorer/address/0xb185814ec5a0823e712f47de957748f6e950df6d) · whale [0x3c71…](https://intel.arkm.com/explorer/address/0x3c716d252b53891753de883894ff29a9ebee0f54) · unlabelled [0xD052…](https://intel.arkm.com/explorer/address/0xd052a46b8e0c89facb393805e1917afd20f293cb), [0xb3da…](https://intel.arkm.com/explorer/address/0xb3dacc732509ba6b7f25ad149e56ca44fe901ab9) · Safe with a tentative signer tag [0x30d3…](https://intel.arkm.com/explorer/address/0x30d3bbae8623d0e9c0db5c27b82dcda39de40997). Token filter is Enterprise-only; first transfer page only
- [Tier A] [DefiLlama Centrifuge Protocol](https://defillama.com/protocol/centrifuge-protocol) fees and revenue, 16 Nov 2026 5:27 AM MST
- [Tier A] [Centrifuge token docs](https://docs.centrifuge.io/getting-started/token-summary/) · [CP149](https://github.com/centrifuge/cps/blob/main/cps/CP149/CP149.md) · [CP172 FAQ](https://centrifuge.io/blog/centrifuge-releases-cp172-faqs) · [CP172 vote result](https://gov.centrifuge.io/t/cp172-exploring-token-to-equity-to-maximize-long-term-cfg-value/7525?page=9) · [Q3 2026 recap](https://centrifuge.io/blog/centrifuge-q3-2026-recap) · [Grove announcement](https://grove.finance/blog/grove-announces-strategic-stake-in-centrifuge-ecosystem-deepening-long-term-partnership)
- [Tier B] [Alea newsletter](https://alearesearch.io/newsletters/centrifuge-derwa-holders) · [Coindaro project page](https://www.coindaro.com/projects/centrifuge/) · [DefiLlama Universal Token Rating](https://defillama.com/universal-token-rating/token/centrifuge-2)
- [Tier A] CoinGecko `centrifuge-2` market data (16 Nov 2026 5:27 AM MST); Gate CFG/USDT daily candles
- [Unverified] who holds the keys to `0xD052…` and `0xb3da…`; where the 12% team allocation sits; what ~20.3M CFG still at FalconX is for; whether the 3 Nov 2025 and 6 Oct 2025 transfers to OKX and Kraken hot wallets (Arkham) were customer migrations; who owns `0xB185…` (16.31M from the treasury); Grove's purchase price

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| `0xb3da…` is the Centrifuge Treasury (immutable InflationMinter target; docs: inflation accrues to the treasury) | [InflationMinter code](https://etherscan.io/address/0x50a168cd6957e07b6de6c1a99b2f940475f70def#code) · [mint to 0xb3da](https://etherscan.io/tx/0x26de7e34b8547b079f54f1dd090a4996f6c91702ff3c8859b5f88f9de557026d) · [docs](https://docs.centrifuge.io/getting-started/token-summary/) | A | 16 Nov 2026 |
| `0x9938…` = OKX Hot Wallet, `0xa8c8…` = Kraken Hot Wallet, `0x40D3…` = Upbit Deposit | [0x9938](https://intel.arkm.com/explorer/address/0x9938ee74ba7a5c1abcd157272a18fcfc9ec9e8d5) · [0xa8c8](https://intel.arkm.com/explorer/address/0xa8c8feff4c02835684c86b01c7ab512bdaadeeaf) · [0x40D3](https://intel.arkm.com/explorer/address/0x40d31dd5682b4813899a19bfa5d7453048fa2201) | B | 16 Nov 2026 ~7:07–7:18 AM MST |
| 115M CP149 mint to the CNF Safe `0x30d3…`, which passed 72M to EOA `0xD052…` | [mint](https://etherscan.io/tx/0xb2feea2d885009aae9a629a8b73fadc9c487faf650acacedd4523c0433a781a6) · [0x30d3](https://etherscan.io/address/0x30d3bbae8623d0e9c0db5c27b82dcda39de40997) · [0xD052](https://etherscan.io/address/0xD052A46b8e0C89fAcB393805E1917AfD20f293Cb) · [CP149](https://github.com/centrifuge/cps/blob/main/cps/CP149/CP149.md) | A | 16 Nov 2026 |
| 59.8M minted to `0xD052…` in the 4 Jun 2026 governance tx (Root swap) | [tx](https://etherscan.io/tx/0x8c44d82dca81cd17cac72c2a32e4d0c004dc9523a945c16a5aa2601ebe40cac3) | A | 16 Nov 2026 |
| 18 Mar 2026 pump day: treasury 835k → Binance deposit | [tx](https://etherscan.io/tx/0x82459d78436ead4718d8ec0fbcbf380edad6d7947e908dd5a013673fc1f0f864) · [deposit](https://etherscan.io/address/0x0a367f918340d47d36b21c93e9a2b6853cc9d6f0) | A + B tag | 16 Nov 2026 |
| 26 Feb / 16 Mar 2026 pump days: treasury → FalconX, returned 1:1 | [26 Feb out](https://etherscan.io/tx/0x34b1606f95a62c6304e2aefa9c4897b93d2525e99c79e91dcce6677d415a2d34) · [5 Mar back](https://etherscan.io/tx/0xb3d5c9d5f67f1cbc6eec9d9c167375ab31639a6fe322155e53abae774251d9b9) · [16 Mar out](https://etherscan.io/tx/0x7c314124c541fd408c3c98bbc73d574559aea77f8f24067e5d9b7dfa8210d35e) · [25 Mar back](https://etherscan.io/tx/0x45e73d275d7e1b84facb0723bbad2a20c05493204cf390c439e3dad0d5186632) | A + B tag | 16 Nov 2026 |
| ~20.3M CFG at FalconX not returned (e.g. 6.6M, 20 Oct 2026) | [tx](https://etherscan.io/tx/0xfd461009b3675337db377deb4b70c4bad57345ae07222df0d7b71412e2071da1) · [FalconX deposit](https://etherscan.io/address/0x64ac897b8b3cd9ee86d0b64363a290f66a7585f7) | A | 16 Nov 2026 |
| 23 May 2025 pump day: CNF Safe 23.06M → Gate (migration support) | [tx](https://etherscan.io/tx/0xbfe86a3b54b21c4536c6a6f52efd465545821000f2405a31ce51ba4cef6f8d58) | A + B tag | 16 Nov 2026 |
| Wintermute loan returned 5.5M | [return](https://etherscan.io/tx/0x32bd8787290aef092e8f73f6ee374f5d64562d984c3ea606897073e103d0e854) · [loan hop](https://etherscan.io/address/0xaa9f8b6c6d1ca0d5abd96357a7871864173edb3c) | A + B tag | 16 Nov 2026 |
| Treasury → Grove 33.75M; Grove disclosed 37.8M | [5M tx](https://etherscan.io/tx/0x3d92ccaece9f37f4400e624c4f5d078515a155748b3eb043c08f3da62f70d41c) · [Grove blog](https://grove.finance/blog/grove-announces-strategic-stake-in-centrifuge-ecosystem-deepening-long-term-partnership) | A | 16 Nov 2026 |
| 3% inflation rate and target are immutable | [code](https://etherscan.io/address/0x50a168cd6957e07b6de6c1a99b2f940475f70def#code) | A | 16 Nov 2026 |
| Root delay 48h; token wards | [Root](https://etherscan.io/address/0x7ed48c31f2fdc40d37407cbabf0870b2b688368f#code) · [token](https://etherscan.io/address/0xcccCCCcCCC33D538DBC2EE4fEab0a7A1FF4e8A94#code) | A | 16 Nov 2026 |
| No buyback; liquidity funding to wind down; CP172 passed | [FAQ](https://centrifuge.io/blog/centrifuge-releases-cp172-faqs) · [vote](https://gov.centrifuge.io/t/cp172-exploring-token-to-equity-to-maximize-long-term-cfg-value/7525?page=9) | A | 16 Nov 2026 |
| Revenue $5.23M (1y), holders $0 | [DefiLlama](https://defillama.com/protocol/centrifuge-protocol) | A | 16 Nov 2026 5:27 AM MST |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Arkham pass: done 16 Nov 2026** (first transfer page per wallet). Named: `0x9938…` OKX Hot Wallet, `0xa8c8…` Kraken Hot Wallet, `0x40D3…` Upbit Deposit; `0x845f…` funded by Bitcoin Suisse. Not named: `0xD052…`, `0xb3da…` (no Centrifuge label), `0x30d3…` (tentative signer tag only), `0xB185…`, `0x3c71…` | Ask the Foundation to publish its wallet list | Free |
| 2 | **Who holds the keys to `0xD052…` and `0xb3da…`?** | Ask the Foundation to publish its wallet list and signer setup | Free |
| 3 | **Where is the 12% team allocation, and is any of it locked on-chain?** | Ask for the vesting contract addresses; search for vesting contracts holding CFG | Free |
| 4 | **What is the ~20.3M CFG still at FalconX?** | Watch for FalconX 1 → `0xb3da…` returns; ask Centrifuge to name its market makers | Free |
| 5 | **CP172 conversion window and what happens to treasury, unvested and exchange-held CFG** | Watch the governance forum and centrifuge.foundation | Free |
| 6 | **Were the Oct–Nov 2025 transfers to `0x9938…` / `0xa8c8…` exchange migrations?** Arkham confirms both are exchange hot wallets (OKX, Kraken) | Ask OKX / Kraken or Centrifuge whether they were customer-balance migrations | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
