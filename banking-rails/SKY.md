---
ticker: SKY
name: Sky (formerly Maker)
chain: ethereum
contract: "0x56072C95FAA701256059aa122697B133aDEd9279"
overall_score: 6.8
overall_verdict: PASS
section_scores:
  revenue: 8
  foundation_team: 7
  insider_holdings: 6
  selling_behavior: 6
  tokenomics_supply: 7
  liquidity_market: 6
  product_development: 8
  adoption_customers: 8
  security_audits: 7
  regulatory: 5
  catalysts: 6
gates_failed: []
red_lines:
  hack_exploit: none
  mint_path_live: "governance only (Pause Proxy is the only SKY ward; no SKY minted since Jul 2025)"
  team_wallet_to_exchange_during_pump: "none found (Pause Proxy, Sky Frontier Foundation, Fortification Foundation and Liquidity Bootstrapping multisig: no direct exchange deposits)"
  one_hop_sale_status: none_found
  treasury_coins_to_exchange_via_market_maker: "yes, disclosed program (320M SKY Liquidity Bootstrapping loan; 32.3M reached KuCoin 32 on its 2 Oct 2024 listing day, not a pump day; market maker is Wintermute per Arkham, Tier B)"
  funded_contributor_wallet_pump_day_sales: "yes, small (Launch Project-funded Safe 0xeaef sold ~9.8M SKY ≈ $0.69M on CoW Swap on pump days, Aug–Oct 2026; owner [Unverified])"
methodology_effective: 2026-11-16
revenue_reaches_holders: "yes"
revenue_mechanism: "The Smart Burn Engine buys SKY on-chain from protocol surplus and USDS staking rewards are paid from net revenue under the Stage 2 split (Q3 2026: $5.60M of buybacks and $3.12M of USDS to stakers; burns on-chain), so revenue reaches holders."
pump_day_price_source: "CoinGecko SKY daily closes (as published; named last resort)"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions:
  - address: "0xca5183fb9997046fbd9ba8113139bf5a5af122a0"
    label: "Sky Frontier Foundation Safe"
    confidence: high
    independent_corroboration: true
    basis: "Governance votes + on-chain Lock events"
  - address: "0xeaef8fb615a7d5ab6a356dec0549fd749460e970"
    label: "Generic Gnosis Safe paid by the Launch Project multisig"
    confidence: low
    independent_corroboration: false
    basis: "Arkham (generic) + Etherscan funding"
price_usd: 0.05135
price_source: "CoinGecko, 16 Nov 2026 5:06 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### SKY · Overall grade **6.8 / 10 · ✅ PASS**

**Summary:** Sky (the rebranded MakerDAO) runs the USDS/DAI stablecoin system and earns real money: $99.3M gross revenue and $37.2M net revenue in Q3 2026, $129.1M net over the last twelve months. A fixed share of that net now buys SKY back, pays USDS to SKY stakers and burns SKY, so holders do get paid. The treasury SKY sits in governance-controlled multisigs whose every grant was voted on-chain, and none of them sent SKY straight to an exchange. Two yellow flags: a 320M-SKY treasury loan to a market maker (Arkham: Wintermute) partly ended up on KuCoin, and a Launch Project-funded contributor Safe sold about 9.8M SKY on pump days.

**🚨 Top warning (yellow, not a red line):** a Safe paid 1.76M SKY a month by Sky's **Launch Project multisig** ([`0x3C51…D02F`](https://etherscan.io/address/0x3c5142f28567e6a0f172fd0baaf1f2847f49d02f), named in the [5 Sep 2024 spell](https://github.com/sky-ecosystem/spells-mainnet/blob/master/archive/2024-09-05-DssSpell/DssSpell.sol)) **unstaked 6.3M SKY and sold it through CoW Swap within minutes on the 20 Aug 2026 pump day (+22.2%)**, then did the same on the 3 Oct 2026 pump day (+15.2%). That is ~9.8M SKY (≈ $0.69M) sold on pump days. Who owns the Safe is not public. Check it yourself: [Safe `0xeaef…e970`](https://etherscan.io/address/0xeaef8fb615a7d5ab6a356dec0549fd749460e970) · [first Launch Project payment](https://etherscan.io/tx/0xf182eaa17889810c96d179598815af55d8e056e64ebb58b8dca10a01e335e31a) · [20 Aug unstake](https://etherscan.io/tx/0xfe71909e5d977ea286d1418de3f5c842d7c36ea3dabf1627b5acc32a1c12c361) · [first sale six minutes later](https://etherscan.io/tx/0xc3a525d1554cde9558be546391191d48d0c9b1b7b0842f9ed1195a5bf1fa4ae9). **Second flag:** the 320M SKY [Liquidity Bootstrapping loan](https://etherscan.io/tx/0xcc39d178f17bdcb7bd5340578e0ba750be232e0ca66d09359953d818dfe9becb) went to a **Wintermute** deposit wallet ([Arkham](https://intel.arkm.com/explorer/address/0xb9681a75e296b7caa4ec4fd92aee809a36a4fc7e), [Tier B] Arkham, read 16 Nov 2026 ~6:10 AM MST (signed-in account)), and [32.3M of it](https://etherscan.io/tx/0xd5be66d8aea7ff4005f83075a751761b620ff62edd579e5a0fcd83eef5251f8a) reached [KuCoin 32](https://etherscan.io/tx/0xd860ce91488a04672586ce9b379556118e54b380dae7a9ffa010c74209eb7d06) through Wintermute's own KuCoin deposit seven hours later, on KuCoin's SKY listing day (market-making for the listing, which the program was for). The loan was [repaid in Sep 2025](https://etherscan.io/tx/0x6782d226711fd429a1648942094953ea2f5b4eef0f5efd86368221a663bfe0d9). Every transfer is linked in the 🔗 Evidence trail below.

**Sections passed: 10 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 8/10 | ✅ PASS |
| 🏛️ Foundation & team | 7/10 | ✅ PASS |
| 🪙 Foundation / team holdings | 6/10 | ✅ PASS |
| 📉 Selling behavior | 6/10 | ✅ PASS |
| 📊 Tokenomics & supply | 7/10 | ✅ PASS |
| 💧 Liquidity & market | 6/10 | ✅ PASS |
| 🧑‍💻 Product & development | 8/10 | ✅ PASS |
| 🤝 Adoption & customers | 8/10 | ✅ PASS |
| 🛡️ Security & audits | 7/10 | ✅ PASS |
| ⚖️ Regulatory | 5/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 6/10 | ✅ PASS |

*Pass = 6 or more out of 10. Full details for every section follow below.*

> **Arkham pass, 16 Nov 2026:** no score change. Arkham names the Liquidity Bootstrapping market maker (**Wintermute**), labels three big "unlabelled" holders as Coinbase-linked (custody / deposit), and finds **no** owner label for the pump-day seller Safe `0xeaef…`, so the yellow flags stand as written.

---


# 🪪 SKY · Sky (formerly Maker) · 6.8 / 10 · ✅ PASS

> **One line:** Sky (the rebranded MakerDAO) runs the USDS/DAI stablecoin system and earns real money: $99.3M gross revenue and $37.2M net revenue in Q3 2026, $129.1M net over the last twelve months. A fixed share of that net now buys SKY back, pays USDS to SKY stakers and burns SKY, so holders do get paid. The treasury SKY sits in governance-controlled multisigs whose every grant was voted on-chain, and none of them sent SKY straight to an exchange. Two yellow flags: a 320M-SKY treasury loan to a market maker (Arkham: Wintermute) partly ended up on KuCoin, and a Launch Project-funded contributor Safe sold about 9.8M SKY on pump days.

| 📊 Market (CoinGecko, 16 Nov 2026 5:06 AM MST) | 🔗 On-chain (Ethereum, 16 Nov 2026) |
|---|---|
| **Price** $0.05135 | **Token** [`0x5607…9279`](https://etherscan.io/address/0x56072C95FAA701256059aa122697B133aDEd9279) SKY; only ward is the governance [Pause Proxy](https://etherscan.io/address/0xBE8E3e3618f7474F8cB1d074A26afFef007E98FB) (RPC read) |
| **24h / 7d / 30d** 🔴 −4.6% / −16.9% / −27.5% · 1y +1.9% | **`totalSupply()`** 23,452,431,915.6 SKY |
| **Market cap** $1.203B · **FDV** $1.205B | **Staked in LockstakeEngine** [10.29B (43.9%)](https://etherscan.io/address/0xCe01C90dE7FD1bcFa39e237FE6D8D9F569e8A6a3) · **in Chief (voting)** [7.14B (30.4%)](https://etherscan.io/address/0x929d9A1435662357F54AdcF64DcEE4d6b867a6f9) |
| **24h volume** $10.2M | **MKR→SKY converter** [`0xA1Ea…f03a`](https://etherscan.io/address/0xA1Ea1bA18E88C381C724a75F23a130420c403f9a) holds 2.02B SKY (8.6%) for remaining MKR |
| **ATH** $0.1009 (5 Oct 2026) · now −49.1% | **Burns by the Pause Proxy** 426.3M (30 Jun 2025), 2.86M (13 Sep 2026), 7.37M (12 Oct 2026) |
| **Holders** 17,453 (Blockscout) | **Treasury-controlled SKY** ≈ 3.0B (≈ 12.8%), see Holdings |

---

## 💰 Revenue — Does it make money? · 8/10 · ✅ PASS

| Metric | Value | Source |
|---|---:|---|
| Gross protocol revenue, Q3 2026 | **$99.29M** (+14.2% y/y; $397.2M annualised) | [Tier A] [Sky Ecosystem Q3 2026 report (Sky Frontier Foundation)](https://insights.skyeco.com/insights/sky-ecosystem-q3-2026-quarterly-report) · [press release, 29 Oct 2026](https://www.prnewswire.com/news-releases/institutional-use-of-sky-protocol-deepens-in-q3-as-net-revenue-rises-11-8-and-galaxy-adds-100m-of-susds-to-its-balance-sheet-302923644.html) |
| Net revenue, Q3 2026 / trailing 12 months | **$37.19M** / **$129.09M** | same report |
| DefiLlama: fees / revenue / holders revenue, last 365 days | **$383.8M / $189.2M / $53.9M** | [Tier A] [DefiLlama Sky](https://defillama.com/protocol/sky), API read 16 Nov 2026 ~5:10 AM MST |
| How net revenue is split (Stage 2, approved 13 Aug 2026) | 22.5% SKY buybacks for staking rewards, 22.5% USDS to SKY stakers, 5% buy-and-burn, up to 50% to Sky Reserves until $150M | [Tier A] Q3 report |
| Paid to SKY holders in Q3 2026 | $5.60M of buybacks (87.5M SKY at ~$0.064) + $3.12M USDS to stakers | [Tier A] Q3 report |
| Cumulative buybacks since Nov 2024 | $126.8M for 2.01B SKY | [Tier A] Q3 report; on-chain, the Pause Proxy received **3.07B SKY from the [Uniswap V2 SKY-USDS pool](https://etherscan.io/address/0x2621CC0B3F3c079c1Db0E80794AA24976F0b9e3c)** (Smart Burn Engine buys) |
| Burns | [2.86M on 13 Sep 2026](https://etherscan.io/tx/0xcd57535f7a9e60e61d34b31f793501fa6178b4ae37fe0b2900f76efd54e192c3) · [7.37M on 12 Oct 2026](https://etherscan.io/tx/0x93389082b75a9e278b6b2a2d7dde53618c38214b5d71699fd60461dbe1e10275) | [Tier A] chain |

**What it means:** A real business with hundreds of millions in yearly interest income, and a written rule that sends about half of net revenue to SKY holders through buybacks, USDS staking rewards and burns. The payout today is modest (~$35M a year at the Q3 rate, ≈ 2.9% of market cap), and governance can change the split or set it to zero, which the Foundation itself warns. Not a 9 because reserves get paid first and the holder share is small next to gross revenue.

- **Reaches holders (binary test, 16 Nov 2026 rules): Yes.** The Smart Burn Engine buys SKY on-chain from protocol surplus and USDS staking rewards are paid from net revenue under the Stage 2 split (Q3 2026: $5.60M of buybacks and $3.12M of USDS to stakers; burns on-chain), so revenue reaches holders.

## 🏛️ Foundation & team — Who is in charge? · 7/10 · ✅ PASS

| Item | Finding | Source |
|---|---|---|
| Governance | On-chain SKY voting (Chief, 7.14B SKY) → executive spells → Pause Proxy, with a 24-hour GSM delay (Aug 2025) | [Tier A] [executive vote 21 Aug 2025](https://github.com/sky-ecosystem/executive-votes/blob/master/2025/executive-vote-2025-08-21.md) |
| Sky Frontier Foundation (SFF) | Cayman Islands foundation that publishes the quarterly reports. Got the treasury's SKY (1,977,443,914) on 25 Aug 2025 at Safe [`0xca51…22A0`](https://etherscan.io/address/0xca5183FB9997046fbd9bA8113139bf5a5Af122A0) | [Tier A] [spell 2025-08-21, `SKY_FRONTIER_FOUNDATION`](https://github.com/sky-ecosystem/spells-mainnet/blob/master/archive/2025-08-21-DssSpell/DssSpell.sol) · [tx](https://etherscan.io/tx/0x9dff3cf283969f0d6b54347829463aabbcad43e79ebb7ad20c5154e951586e3f) |
| Fortification Foundation | 200M SKY + 10M USDS grant for legal, lobbying and risk work, Safe [`0x4834…91C6`](https://etherscan.io/address/0x483413ccCD796Deddee88E4d3e202425d5E891C6) | [Tier A] same spell and vote |
| Launch Project | Funding multisig [`0x3C51…D02F`](https://etherscan.io/address/0x3c5142f28567e6a0f172fd0baaf1f2847f49d02f) (`LAUNCH_PROJECT_FUNDING`) | [Tier A] [spell 2024-09-05](https://github.com/sky-ecosystem/spells-mainnet/blob/master/archive/2024-09-05-DssSpell/DssSpell.sol) |
| Founder | Rune Christensen (public figure). Personal wallets are not attributed in this report | [Unverified] for wallets |

**What it means:** Every treasury move is a public spell with a named address, which is better disclosure than almost any other token in this list. The foundations are separate legal entities that receive large grants; the people behind each Safe's signers are not published.

## 🪙 Foundation / team holdings — How many coins do they hold? · 6/10 · ✅ PASS

| Bucket | SKY | Notes |
|---|---:|---|
| Pause Proxy (governance treasury) | **33,457,851** | RPC `balanceOf`, 16 Nov 2026. The spell kept 16M back on purpose |
| Sky Frontier Foundation Safe, liquid | 37,685,590 | [`0xca51…`](https://etherscan.io/address/0xca5183FB9997046fbd9bA8113139bf5a5Af122A0) |
| SFF, staked in LockstakeEngine | **≈ 2,714,074,036 (11.6%)** | 27 `Lock` events (3.355B) minus 2 `Free` events (640.6M, both back to SFF). Urns [`0x832c…`](https://etherscan.io/address/0x832c0f94ccacaf7bc48849875abd35fe06082d72) and [`0x3d25…`](https://etherscan.io/address/0x3d25235b7c414cb67bf09561a33fd6ce62c11dcf). SFF also **drew 37.1M USDS of debt** against it (5 `Draw` events) |
| Fortification Foundation, staked | ≈ 216,686,569 | [lock tx](https://etherscan.io/tx/0xea09dbda9a70c0aa9d544963556d874b4411304d8e1c63a1aa5cf8b60848932d); 95,533 liquid |
| Liquidity Bootstrapping multisig | 0 | [`0xD850…AFdD`](https://etherscan.io/address/0xD8507ef0A59f37d15B5D7b630FA6EEa40CE4AFdD); its SKY was sent on to SFF and others in Sep 2025 – Jan 2026 |
| **Total treasury / foundation-controlled** | **≈ 3.00B (≈ 12.8%)** | All granted by public spells |
| Large outside holders (Arkham) | [`0xbaF2…7897`](https://etherscan.io/address/0xbaF24C32652c35f14687eA1EA997e6348f731897) 379.4M (Coinbase-associated, trades with Coinbase Hot Wallet; owner not named) [Arkham](https://intel.arkm.com/explorer/address/0xbaf24c32652c35f14687ea1ea997e6348f731897) · [`0xb4ca…5bb8`](https://etherscan.io/address/0xb4cadC735c00F07E880144db8C3e9c4bABc25bb8) 210.9M **Coinbase Prime Custody** [Arkham](https://intel.arkm.com/explorer/address/0xb4cadc735c00f07e880144db8c3e9c4babc25bb8) · [`0x3FB1…74D5`](https://etherscan.io/address/0x3FB15d3CFA5327a243A7aE18EFCcD91dE66B74D5) 210.4M **Coinbase Deposit** [Arkham](https://intel.arkm.com/explorer/address/0x3fb15d3cfa5327a243a7ae18efccd91de66b74d5) · [`0x3c71…0f54`](https://etherscan.io/address/0x3c716d252b53891753de883894ff29a9ebee0f54) 125.4M (no owner label) [Arkham](https://intel.arkm.com/explorer/address/0x3c716d252b53891753de883894ff29a9ebee0f54) · [`0xe92e…a03f`](https://etherscan.io/address/0xe92e65049b3c2ca12806e9567b08895118c5a03f) 22.4M **GSR Markets** [Arkham](https://intel.arkm.com/explorer/address/0xe92e65049b3c2ca12806e9567b08895118c5a03f) | [Tier B] Arkham, read 16 Nov 2026 ~6:10 AM MST (signed-in account). None is labelled as a Sky insider |

**What it means:** About an eighth of supply is controlled by the treasury and two foundations, mostly staked (earning rewards and voting weight). The amount is high, but every grant is on-chain and voted, and the SFF actually **bought** SKY: wallet [`0x7e09…278f`](https://etherscan.io/address/0x7e09e1c3459b2ade356b250055c99e9e17a4278f) (a generic Safe on Arkham, no SFF label [Arkham](https://intel.arkm.com/explorer/address/0x7e09e1c3459b2ade356b250055c99e9e17a4278f)) bought 642.7M SKY on CoW Swap (Aug–Dec 2025) and passed 611.9M to SFF ([first hand-off](https://etherscan.io/tx/0x06dd5554a4a7db84843e0f131be85b3e1d93c5ee49ee8c6105298cc39d8d45ec)). Score **6**: disclosed and not dumped, but concentrated, and SFF borrows against it.

## 📉 Selling behavior — Do insiders sell into pumps? · 6/10 · ✅ PASS

**A. Treasury and foundation wallets (full SKY history, Etherscan `tokentx`):**

| Wallet | SKY out (to) | Exchange deposits? |
|---|---|---|
| Pause Proxy (19,341 transfers) | SFF 1.98B, rewards distributors 1.44B, burns 436.5M, LB 320M, Fortification 200M, Launch Project 96M | **None** |
| Sky Frontier Foundation | Only into LockstakeEngine (3.35B) and back to the Pause Proxy ([500M, 3 Nov 2025](https://etherscan.io/tx/0xb42e7fe76390124fb8026fbd564c373c7f3dc5674ed61b5ce1534a5da8bfb623)). Both `Free` events paid SFF itself | **None** |
| Fortification Foundation | Only into LockstakeEngine | **None** |
| Liquidity Bootstrapping multisig | 320M to `0xb968…` (Oct 2024), then SFF 251M, `0xfa22…` 70M, `0xa87e…` 37.4M, `0x767e…` 36.6M and contributor Safes (Sep 2025) | **None direct** |
| Launch Project multisig | ~100M in 1–15M lots to ~17 contributor Safes, Oct 2024 – Aug 2025 | **None direct** |

**B. The Liquidity Bootstrapping loan (disclosed program; Arkham names the counterparty as Wintermute).** The [27 Sep 2024 executive vote](https://github.com/sky-ecosystem/community/blob/master/governance/votes/Executive%20Vote%20-%20September%2027%2C%202024.md) sent 320M SKY to the LB multisig ([tx](https://etherscan.io/tx/0xfc1d79ef313c8b5af720830fb9f7f029bf700cbdfc0a472e12df1c72cce6be43)). On 2 Oct 2024 the multisig [sent all 320M](https://etherscan.io/tx/0xcc39d178f17bdcb7bd5340578e0ba750be232e0ca66d09359953d818dfe9becb) to [`0xb968…4fc7e`](https://etherscan.io/address/0xb9681a75e296b7caa4ec4fd92aee809a36a4fc7e), a **Wintermute Deposit** address on Arkham ([Arkham](https://intel.arkm.com/explorer/address/0xb9681a75e296b7caa4ec4fd92aee809a36a4fc7e)). That wallet sent [32.3M](https://etherscan.io/tx/0xd5be66d8aea7ff4005f83075a751761b620ff62edd579e5a0fcd83eef5251f8a) to [`0x5c4c…534d`](https://etherscan.io/address/0x5c4c6c6d0358baf2ade28ffb1723e70139cd534d) (**Wintermute: KuCoin Deposit** [Arkham](https://intel.arkm.com/explorer/address/0x5c4c6c6d0358baf2ade28ffb1723e70139cd534d)), which deposited it at **KuCoin 32** [`0x58ed…6a51`](https://etherscan.io/address/0x58edf78281334335effa23101bbe3371b6a36a51) seven hours later ([tx](https://etherscan.io/tx/0xd860ce91488a04672586ce9b379556118e54b380dae7a9ffa010c74209eb7d06)), and [287.7M](https://etherscan.io/tx/0xd8b459359361a3e62b1e655751778e158f2851894a94b1e47a32d65ca87ea87b) to [`0xdbf5…c080`](https://etherscan.io/address/0xdbf5e9c5206d0db70a90108bf936da60221dc080) (**Wintermute: Hot Wallet** [Arkham](https://intel.arkm.com/explorer/address/0xdbf5e9c5206d0db70a90108bf936da60221dc080)). 2 Oct 2024 was KuCoin's SKY-USDT listing day (first KuCoin candle), and MKR fell 14.9% over the five days before, so it **was not a pump day**. `0x5c4c…` has since sent 160.7M SKY to KuCoin in 132 deposits, 21 of them on pump days in the last year (≈ 9.6M SKY), but that is market-making inventory that cannot be tied to the treasury loan. [`0xf819…73aa`](https://etherscan.io/address/0xf8191d98ae98d2f7abdfb63a9b0b812b93c873aa) (**Wintermute: Hot Wallet** [Arkham](https://intel.arkm.com/explorer/address/0xf8191d98ae98d2f7abdfb63a9b0b812b93c873aa)) **repaid 320.46M SKY** to the LB multisig on 16–17 Sep 2025 ([tx](https://etherscan.io/tx/0x6782d226711fd429a1648942094953ea2f5b4eef0f5efd86368221a663bfe0d9)). Market maker: **Wintermute** ([Tier B] Arkham, read 16 Nov 2026 ~6:10 AM MST (signed-in account); Sky governance has not named it in the sources read). The 21 pump-day KuCoin deposits from `0x5c4c…` are Wintermute's market-making inventory, not treasury sales.

**C. Launch Project-funded Safe selling on pump days.** [`0xeaef…e970`](https://etherscan.io/address/0xeaef8fb615a7d5ab6a356dec0549fd749460e970) got 1.76M SKY a month from the Launch Project multisig from Feb 2025 ([first](https://etherscan.io/tx/0xf182eaa17889810c96d179598815af55d8e056e64ebb58b8dca10a01e335e31a)), staked it, and sold 24.7M SKY through CoW Swap between Jul 2025 and Oct 2026. On pump days:

| Day (UTC) | What happened | SKY | 5-day change |
|---|---|---:|---:|
| 20 Aug 2026 | [Unstaked 6.32M + 0.37M rewards](https://etherscan.io/tx/0xfe71909e5d977ea286d1418de3f5c842d7c36ea3dabf1627b5acc32a1c12c361) at 11:50, first CoW sale [6 minutes later](https://etherscan.io/tx/0xc3a525d1554cde9558be546391191d48d0c9b1b7b0842f9ed1195a5bf1fa4ae9), ~20 sales by 15:02 | ≈ 6.7M | +22.2% |
| 3 Oct 2026 | [Unstaked 6.69M](https://etherscan.io/tx/0xaf51486fc1fd1445ece3ab63cda19d996ea5ac378650120ddbf55223884b4b9c) on 2 Oct, then sold in small lots overnight, e.g. [04:48](https://etherscan.io/tx/0xfbb04af1d95f594786abb9022b15089d834b273cc5ef63149dae82670287db89) | ≈ 3.1M | +15.2% |

- **Pump-day total ≈ 9.8M SKY ≈ $0.69M** at those days' closes (41 CoW trades). That is 0.04% of supply.
- These were contributor payments approved by governance, and the sales went to a DEX, not an exchange deposit address. Whose Safe this is is not public: Arkham shows only a generic "Gnosis Safe Proxy" [Arkham](https://intel.arkm.com/explorer/address/0xeaef8fb615a7d5ab6a356dec0549fd749460e970) [Unverified]. `0x767e…`, which received 36.6M from the LB multisig, is unlabelled; Arkham's first-funder hint is a tentative "Amber Group?" [Arkham](https://intel.arkm.com/explorer/address/0x767e06d0c870fec6c38e101dbe5dbb226c5fd091).

**What it means:** No treasury or foundation wallet sold into a pump, and the treasury has been a net **buyer**. The rule still counts a team-funded wallet selling on pump days, and the market-maker loan put treasury SKY on a centralised exchange without naming the firm. Small amounts and full disclosure of the programs keep it at **6**, a narrow pass. Not tested: MKR-era (pre-Sep 2024) sales by the Maker Foundation and founders.

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from CoinGecko SKY daily closes (as published; named last resort).

## 📊 Tokenomics & supply · 7/10 · ✅ PASS

- **Supply:** 23,452,431,915.6 SKY (RPC). 1 MKR converts to 24,000 SKY; the converter holds 2.02B SKY for MKR not yet upgraded.
- **Mint path:** the Pause Proxy is the only address with `wards = 1` on the SKY token (RPC read: MkrSky converter 0, SFF 0). So new SKY needs an executive vote plus the GSM delay. **No SKY has been minted since early Jul 2025** (Etherscan `getLogs`, Transfer-from-zero, block 22,830,000 → now: 0 events). Earlier mints were MKR conversions and the 2024–25 USDS-staking SKY rewards.
- **Emissions now come from buybacks, not minting:** the Pause Proxy sends bought-back SKY to [VestedRewardsDistribution `0x6756…`](https://etherscan.io/address/0x675671a8756ddb69f7254afb030865388ef699ee) (1.32B in 72 transfers, Nov 2025 – Nov 2026).
- **Burns:** 426.3M on [30 Jun 2025](https://etherscan.io/tx/0x666eb7807c1b4098f9b91658eb008e8931063c5050e4dbe28bd6fac3a2948d02), then the first programmatic burns in Sep and Oct 2026.
- **Risk:** governance can mint, and holder payouts can be voted to zero.

## 💧 Liquidity & market · 6/10 · ✅ PASS

- $10.2M of volume in 24h on a $1.2B cap (≈ 0.85% turnover), thin for its size. Binance, Kraken, OKX, Bybit, Gemini, Crypto.com, Robinhood and eToro wallets all hold SKY (Blockscout tags). Uniswap V4 and V2 pools hold 142M and 76.5M SKY.
- 45 pump days in the last 365 (CoinGecko daily closes), clustered in late Nov 2025, Aug 2026 and 18 Sep – 5 Oct 2026. Price is −49% from the 5 Oct 2026 ATH.

## 🧑‍💻 Product & development · 8/10 · ✅ PASS

- USDS/DAI, the Sky Savings Rate (sUSDS), staked-SKY borrowing (LockstakeEngine), stUSDS, and the "Sky Agent" network (Spark, Grove and others) ([Q3 report](https://insights.skyeco.com/insights/sky-ecosystem-q3-2026-quarterly-report)).
- GitHub `sky-ecosystem`: 100 repos, **41 pushed in the last 90 days**, spells pushed 16 Nov 2026.

## 🤝 Adoption & customers · 8/10 · ✅ PASS

| Item | Value | Source |
|---|---|---|
| USDS supply / sUSDS | $9.70B / $4.52B (end Q3 2026) | [Tier A] Q3 report |
| Protocol collateral | $11.41B | [Tier A] Q3 report |
| Galaxy | Added $100M sUSDS to its balance sheet; Grove–Galaxy $500M warehouse facility 75% used | [Tier A] Q3 report; Galaxy's own confirmation not read [Unverified] |

## 🛡️ Security & audits · 7/10 · ✅ PASS

- Seven-year-old core (MCD) with no core-contract exploit found in this pass. New modules (SKY, LockstakeEngine, USDS) are audited by multiple firms per Sky docs; audit PDFs not re-read this pass [Unverified].
- **Live stress:** stUSDS showed $0 available to withdraw in mid-Nov 2026 because it is all lent to staked-SKY borrowers, and governance is reviewing a stop to new borrowing on ETH/wstETH core vaults ([CoinMarketCap summary, 14 Nov 2026](https://coinmarketcap.com/top-stories/6af8784519ea3e3530cd9918/), [Tier B]; on-chain check open).

## ⚖️ Regulatory · 5/10 · ❌ FAIL

- Foundations are offshore (SFF: Cayman Islands per its press release). No licence for USDS or SKY was found. USDS is not a MiCA-authorised stablecoin as far as this pass found [Unverified].
- SFF says Moody's gave Sky Protocol a counterparty rating and S&P a stable outlook ([Tier A] self-reported in the Q3 report; agencies' own pages not read).

## 📅 Catalysts & calendar · 6/10 · ✅ PASS

| Date | Event |
|---|---|
| 19 Nov 2026 | Executive spell: Osero Base USDC vault (proposal) |
| Nov 2026 | Vote on stopping new borrowing in ETH/wstETH core vaults |
| Monthly | Net-revenue settlement: buybacks, USDS staking rewards, burns |
| Late Jan 2027 | Q4 2026 quarterly report from SFF (pattern) |
| When reserves hit $150M | Buyback share rises automatically |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found on core contracts |
| Team / treasury wallet → exchange during a pump | 🟢 None found: [Pause Proxy](https://etherscan.io/address/0xBE8E3e3618f7474F8cB1d074A26afFef007E98FB), [SFF](https://etherscan.io/address/0xca5183FB9997046fbd9bA8113139bf5a5Af122A0), [Fortification](https://etherscan.io/address/0x483413ccCD796Deddee88E4d3e202425d5E891C6), [LB multisig](https://etherscan.io/address/0xD8507ef0A59f37d15B5D7b630FA6EEa40CE4AFdD) |
| Treasury coins reaching an exchange via a market maker | 🟡 32.3M SKY → [KuCoin 32](https://etherscan.io/tx/0xd860ce91488a04672586ce9b379556118e54b380dae7a9ffa010c74209eb7d06) on listing day 2 Oct 2024 (not a pump day); program disclosed; firm is Wintermute per Arkham (Tier B) |
| Team-funded wallet selling on pump days | 🟡 Launch Project-funded [`0xeaef…`](https://etherscan.io/address/0xeaef8fb615a7d5ab6a356dec0549fd749460e970) ≈ 9.8M SKY on CoW Swap, 20 Aug and 3 Oct 2026 |
| Live mint path | 🟡 Governance only (Pause Proxy ward); unused since Jul 2025 |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| [SFF 0xca51…22A0](https://etherscan.io/address/0xca5183FB9997046fbd9bA8113139bf5a5Af122A0) | Sky Frontier Foundation Safe | Governance votes + on-chain Lock events | high | yes | Holdings: ~11.6% staked |
| [0xeaef…e970](https://etherscan.io/address/0xeaef8fb615a7d5ab6a356dec0549fd749460e970) | Generic Gnosis Safe paid by the Launch Project multisig | Arkham (generic) + Etherscan funding | low | no | Cannot move Selling on its own (contributor-payment recipient; owner unknown) |

## 📚 Sources

- [Tier A] Methodology update 16 Nov 2026: no new Arkham lookups; the attribution table uses evidence already cited in this report.
- [Tier A] Etherscan v2 API `tokentx` full SKY history for the Pause Proxy (19,341 transfers), SFF, Fortification Foundation, Liquidity Bootstrapping and Launch Project multisigs, and every second-hop wallet named above; `getLogs` on the SKY token (mints/burns) and LockstakeEngine (`Open`, `Lock`, `Free`, `Draw`); read 16 Nov 2026 ~5:10–5:45 AM MST
- [Tier A] Ethereum RPC (publicnode): SKY `wards`, `totalSupply`, `balanceOf`, 16 Nov 2026 ~5:30 AM MST
- [Tier A] Sky governance: [executive vote 21 Aug 2025](https://github.com/sky-ecosystem/executive-votes/blob/master/2025/executive-vote-2025-08-21.md) · [spell 2025-08-21](https://github.com/sky-ecosystem/spells-mainnet/blob/master/archive/2025-08-21-DssSpell/DssSpell.sol) · [executive vote 27 Sep 2024](https://github.com/sky-ecosystem/community/blob/master/governance/votes/Executive%20Vote%20-%20September%2027%2C%202024.md) · [spell 2024-09-05](https://github.com/sky-ecosystem/spells-mainnet/blob/master/archive/2024-09-05-DssSpell/DssSpell.sol)
- [Tier A] [Sky Ecosystem Q3 2026 report](https://insights.skyeco.com/insights/sky-ecosystem-q3-2026-quarterly-report) and [press release](https://www.prnewswire.com/news-releases/institutional-use-of-sky-protocol-deepens-in-q3-as-net-revenue-rises-11-8-and-galaxy-adds-100m-of-susds-to-its-balance-sheet-302923644.html) (issuer-published)
- [Tier A] DefiLlama fees API (`sky`), 16 Nov 2026
- [Tier B] Blockscout name tags and top-50 holders (exchange hot wallets, "Sky: MCD Pause Proxy", "LockstakeEngine", "Chief"); the private exchange-address list used for earlier reports
- [Tier B] Arkham, read 16 Nov 2026 ~6:10 AM MST (signed-in account): Wintermute labels on [0xb968…](https://intel.arkm.com/explorer/address/0xb9681a75e296b7caa4ec4fd92aee809a36a4fc7e), [0xdbf5…](https://intel.arkm.com/explorer/address/0xdbf5e9c5206d0db70a90108bf936da60221dc080), [0x5c4c…](https://intel.arkm.com/explorer/address/0x5c4c6c6d0358baf2ade28ffb1723e70139cd534d), [0xf819…](https://intel.arkm.com/explorer/address/0xf8191d98ae98d2f7abdfb63a9b0b812b93c873aa); GSR Markets [0xe92e…](https://intel.arkm.com/explorer/address/0xe92e65049b3c2ca12806e9567b08895118c5a03f); Coinbase Prime Custody / Coinbase Deposit / Coinbase-associated on `0xb4ca…`, `0x3FB1…`, `0xbaF2…`; generic Safes `0xeaef…`, `0x7e09…`; no owner label on `0x3c71…`, `0x767e…`. Arkham's token filter is Enterprise-only, so counterparties come from the default first page.
- [Tier A] CoinGecko `sky` price and 365-day closes; KuCoin SKY-USDT daily candles (from 2 Oct 2024); Binance MKRUSDT daily klines (Sep–Oct 2024)
- [Tier B] [CoinMarketCap AI summary on stUSDS and core vaults, 14 Nov 2026](https://coinmarketcap.com/top-stories/6af8784519ea3e3530cd9918/)
- [Unverified] Sky's own confirmation of the market maker; owner of `0xeaef…`; owners of `0xbaF2…`, `0x3c71…`, `0x767e…`; audit PDFs; MiCA status; MKR-era insider sales

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| 1.977B SKY granted to the Sky Frontier Foundation and staked the same day | [spell constant](https://github.com/sky-ecosystem/spells-mainnet/blob/master/archive/2025-08-21-DssSpell/DssSpell.sol) · [grant tx](https://etherscan.io/tx/0x9dff3cf283969f0d6b54347829463aabbcad43e79ebb7ad20c5154e951586e3f) · [lock tx](https://etherscan.io/tx/0xae030a406ec39fe487e3b2f87a0a8a372c6d01a1a38e6fa8742d1f8cc8934bcb) · [SFF Safe](https://etherscan.io/address/0xca5183FB9997046fbd9bA8113139bf5a5Af122A0) | A | 16 Nov 2026 |
| 200M SKY to the Fortification Foundation, staked | [vote](https://github.com/sky-ecosystem/executive-votes/blob/master/2025/executive-vote-2025-08-21.md) · [lock tx](https://etherscan.io/tx/0xea09dbda9a70c0aa9d544963556d874b4411304d8e1c63a1aa5cf8b60848932d) · [Safe](https://etherscan.io/address/0x483413ccCD796Deddee88E4d3e202425d5E891C6) | A | 16 Nov 2026 |
| SFF returned 500M SKY to the Pause Proxy | [tx](https://etherscan.io/tx/0xb42e7fe76390124fb8026fbd564c373c7f3dc5674ed61b5ce1534a5da8bfb623) | A | 16 Nov 2026 |
| SFF-side wallet bought 642.7M SKY on CoW Swap and passed it to SFF | [first buy](https://etherscan.io/tx/0x6c1fff18219ec54a97e917b62bd828bb4cca37caf3c4f5b426be729bc44f5910) · [first hand-off](https://etherscan.io/tx/0x06dd5554a4a7db84843e0f131be85b3e1d93c5ee49ee8c6105298cc39d8d45ec) · [wallet](https://etherscan.io/address/0x7e09e1c3459b2ade356b250055c99e9e17a4278f) | A chain · owner [Unverified] | 16 Nov 2026 |
| 320M SKY Liquidity Bootstrapping loan; 32.3M to KuCoin 32 on listing day; repaid Sep 2025 | [vote](https://github.com/sky-ecosystem/community/blob/master/governance/votes/Executive%20Vote%20-%20September%2027%2C%202024.md) · [PP → LB](https://etherscan.io/tx/0xfc1d79ef313c8b5af720830fb9f7f029bf700cbdfc0a472e12df1c72cce6be43) · [LB → 0xb968](https://etherscan.io/tx/0xcc39d178f17bdcb7bd5340578e0ba750be232e0ca66d09359953d818dfe9becb) · [→ 0x5c4c](https://etherscan.io/tx/0xd5be66d8aea7ff4005f83075a751761b620ff62edd579e5a0fcd83eef5251f8a) · [→ KuCoin 32](https://etherscan.io/tx/0xd860ce91488a04672586ce9b379556118e54b380dae7a9ffa010c74209eb7d06) · [→ 0xdbf5](https://etherscan.io/tx/0xd8b459359361a3e62b1e655751778e158f2851894a94b1e47a32d65ca87ea87b) · [repayment](https://etherscan.io/tx/0x6782d226711fd429a1648942094953ea2f5b4eef0f5efd86368221a663bfe0d9) | A chain + B exchange label | 16 Nov 2026 |
| Launch Project-funded Safe sold on the 20 Aug and 3 Oct 2026 pump days | [funding](https://etherscan.io/tx/0xf182eaa17889810c96d179598815af55d8e056e64ebb58b8dca10a01e335e31a) · [unstake 20 Aug](https://etherscan.io/tx/0xfe71909e5d977ea286d1418de3f5c842d7c36ea3dabf1627b5acc32a1c12c361) · [sale 20 Aug](https://etherscan.io/tx/0xc3a525d1554cde9558be546391191d48d0c9b1b7b0842f9ed1195a5bf1fa4ae9) · [unstake 2 Oct](https://etherscan.io/tx/0xaf51486fc1fd1445ece3ab63cda19d996ea5ac378650120ddbf55223884b4b9c) · [sale 3 Oct](https://etherscan.io/tx/0xfbb04af1d95f594786abb9022b15089d834b273cc5ef63149dae82670287db89) · [Launch Project in spell](https://github.com/sky-ecosystem/spells-mainnet/blob/master/archive/2024-09-05-DssSpell/DssSpell.sol) | A chain · owner [Unverified] | 16 Nov 2026 |
| LB loan counterparty is Wintermute (deposit, hot wallets, KuCoin deposit) | [0xb968…](https://intel.arkm.com/explorer/address/0xb9681a75e296b7caa4ec4fd92aee809a36a4fc7e) · [0xdbf5…](https://intel.arkm.com/explorer/address/0xdbf5e9c5206d0db70a90108bf936da60221dc080) · [0x5c4c…](https://intel.arkm.com/explorer/address/0x5c4c6c6d0358baf2ade28ffb1723e70139cd534d) · [0xf819…](https://intel.arkm.com/explorer/address/0xf8191d98ae98d2f7abdfb63a9b0b812b93c873aa) | B (Arkham) | 16 Nov 2026 ~6:10 AM MST |
| Large holders are Coinbase custody / deposit and GSR, not Sky insiders | [0xb4ca…](https://intel.arkm.com/explorer/address/0xb4cadc735c00f07e880144db8c3e9c4babc25bb8) · [0x3FB1…](https://intel.arkm.com/explorer/address/0x3fb15d3cfa5327a243a7ae18efccd91de66b74d5) · [0xbaF2…](https://intel.arkm.com/explorer/address/0xbaf24c32652c35f14687ea1ea997e6348f731897) · [0xe92e…](https://intel.arkm.com/explorer/address/0xe92e65049b3c2ca12806e9567b08895118c5a03f) | B (Arkham) | 16 Nov 2026 ~6:10 AM MST |
| Programmatic burns 2.86M and 7.37M SKY | [13 Sep 2026](https://etherscan.io/tx/0xcd57535f7a9e60e61d34b31f793501fa6178b4ae37fe0b2900f76efd54e192c3) · [12 Oct 2026](https://etherscan.io/tx/0x93389082b75a9e278b6b2a2d7dde53618c38214b5d71699fd60461dbe1e10275) | A | 16 Nov 2026 |
| Net revenue $37.19M (Q3) / $129.09M (TTM); buyback split | [Q3 report](https://insights.skyeco.com/insights/sky-ecosystem-q3-2026-quarterly-report) · [press release](https://www.prnewswire.com/news-releases/institutional-use-of-sky-protocol-deepens-in-q3-as-net-revenue-rises-11-8-and-galaxy-adds-100m-of-susds-to-its-balance-sheet-302923644.html) · [DefiLlama](https://defillama.com/protocol/sky) | A (issuer) + A (DefiLlama) | 16 Nov 2026 |
| Only the Pause Proxy can mint SKY | [SKY token code](https://etherscan.io/address/0x56072C95FAA701256059aa122697B133aDEd9279#code) · [Pause Proxy](https://etherscan.io/address/0xBE8E3e3618f7474F8cB1d074A26afFef007E98FB) | A (RPC `wards`) | 16 Nov 2026 ~5:30 AM MST |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | ~~Arkham pass on 12 unlabelled wallets~~ **Done 16 Nov 2026** (the wallet list): Wintermute, GSR and Coinbase labels folded in. Still unnamed: `0xeaef…`, `0x7e09…`, `0x3c71…`, `0x767e…` | Re-check with Arkham Enterprise's token filter for full SKY counterparty history | Arkham Enterprise |
| 2 | **Partly answered:** Arkham says Wintermute got the 320M SKY loan. Still open: Sky's own confirmation and the loan terms | Ask Sky governance / the LB program facilitators; read the [LB budget forum thread](https://forum.sky.money/t/utilization-of-the-sky-ecosystem-liquidity-bootstrapping-budget-a-5-6-1-9/25537) | Free |
| 3 | **Who owns `0xeaef…`?** (Arkham: generic Safe, no owner) | Match it against Launch Project payment lists in the forum; read its Safe signers on Etherscan | Free |
| 4 | **stUSDS liquidity and the core-vault borrowing stop** | Read stUSDS contract balances and the Nov 2026 spell after it executes | Free |
| 5 | **MKR-era insider selling (pre-Sep 2024)** | Run the same exchange-deposit test on Maker Foundation / founder MKR wallets for 2021–2024 | Free |
| 6 | **Audits for SKY, USDS, LockstakeEngine** | Open the audit PDFs linked in Sky's developer docs and record findings | Free |
| 7 | **Regulatory status of USDS** | Check ESMA's MiCA register and any US actions | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
