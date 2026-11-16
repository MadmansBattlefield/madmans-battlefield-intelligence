---
ticker: HYPER
name: Hyperlane
chain: ethereum
contract: "0x93a2db22b7c736b341c32ff666307f4a9ed910f5 (ERC-20 on Ethereum, Hyperlane warp route; also BNB Chain, Base, Arbitrum, Optimism)"
overall_score: 3.4
overall_verdict: FAIL
section_scores:
  revenue: 2
  foundation_team: 4
  insider_holdings: 3
  selling_behavior: 0
  tokenomics_supply: 3
  liquidity_market: 4
  product_development: 7
  adoption_customers: 5
  security_audits: 5
  regulatory: 6
  catalysts: 4
gates_failed: [revenue, selling_behavior]
red_lines:
  hack_exploit: "no protocol-level exploit found; an app-configured warp route (Autheo THEO, TrustedRelayerIsm) lost ~$1.76M on 12 Oct 2026; a public 'critical' vault-insolvency report (issue #9068) has been open since 18 Jul 2026"
  treasury_to_exchange_during_pump: "yes, via foundation-funded wallets (8 wallets funded with 9.5M HYPER by the foundation-allocation Safe 0x87fc… on 21-22 Apr 2025 sent 9.5M to Binance/Bybit deposits on 10-12 Jul 2025, +351% to +472%)"
  treasury_funded_wallet_to_exchange_during_pump: "yes (above; plus Safe 0x1686…, paid monthly by foundation-funded 0x0102…, sent 250k to a Binance deposit on the 22 Sep 2026 pump day, +15.1%)"
  mint_path_live: "yes by design (Staking Rewards 20% minted quarterly over 25 years)"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "Fees are small and none reaches holders; stakers are paid in new HYPER."
pump_day_price_source: "KuCoin HYPER-USDT daily closes"
pump_day_disclosure_quality: silence
pump_day_undisclosed_penalty_applied: true
dual_review: not_run
attributions: []
price_usd: 0.03968
price_source: "CoinGecko, 16 Nov 2026 6:50 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### HYPER · Overall grade **3.4 / 10 · ❌ FAIL**

**Summary:** Hyperlane is real, busy software: an open interoperability network on 150+ chains with a monorepo that ships every day. The token is a different story. HYPER is down 94% from its July 2025 high, earns its holders nothing (about $362k a year of protocol fees, $0 to holders), and still has about 60% of supply to unlock, with insider unlocks every month. On-chain, the two genesis wallets match the published allocation almost exactly: one got 358.74M (Core Team 25% + Early Backers 10.87% = 358.7M), the other 443.93M (the foundation and community buckets). Wallets funded by the foundation-side Safe sold into the July 2025 spike. Both gates fail: Revenue and Selling.

**🚨 Top warning (red line):** On launch day (21–22 Apr 2025) the foundation-allocation Safe [`0x87fc…4b`](https://etherscan.io/address/0x87fcecb180e0275c22cef213ff301816bb24e74b) (funded with 443.9M by "Hyperlane: Deployer", [tx](https://etherscan.io/tx/0x2e010a4acc5d1ad8ee75a02a9c56e999c71e8ba38a5aa6f8a6948116f9da1bd6)) sent round lots of 1.0–1.5M HYPER, **9.5M in total**, to eight fresh wallets in three batch transactions ([tx 1](https://etherscan.io/tx/0x2dcd7a3a2a2087fec33415f3a024022fe40315cc23f0522bc08a35f12bf9679a) · [tx 2](https://etherscan.io/tx/0x795bcc89d2cce219674f71943262fc24a80ad30611b92480f31287226835f30c) · [tx 3](https://etherscan.io/tx/0xfc704bbad57eb1f081fc47e5e00001f47c0e06c8a46f4a5ee74295f2abe1d479)). Those wallets held the coins for 11 weeks, then sent **all 9.5M to Binance and Bybit deposit addresses on 10–12 Jul 2025**, the three days HYPER was **+472%, +445% and +351%** against five days earlier (KuCoin closes): **≈ $5.2M at those closes**. Five of the eight used the *same* Bybit deposit [`0xd8da…7290`](https://etherscan.io/address/0xd8da1644c722930369b6fb77bc8a8c5b40c07290), so they are one account holder (e.g. [0x730c → Bybit, 999,900](https://etherscan.io/tx/0xd7f15399ee79006b0d2770fbe76cf4acf71e3ecbb0c182b26c329d441d900b88) · [0x33ee → Binance, 1,099,900](https://etherscan.io/tx/0xf65db08b17cb3629f20fc3318c1327450ea7e6e7f33bcad98b8ee4e598ba60c6)). Who that is (market maker, launch partner, KOL) was never disclosed. **Second warning:** the pattern continues in small size. Safe [`0x1686…2e7c`](https://etherscan.io/address/0x16864253e0ab1d3e6844c24896899f99e5272e7c) is paid 390,625 HYPER every month on unlock day by [`0x0102…8f8f`](https://etherscan.io/address/0x0102c5805b8f2dbb2717f233285a246418c98f8f) (an EOA funded with 74.3M by the foundation Safe, still holding 61.9M) and has sent every coin, 5.47M so far, to Binance deposit [`0x1b20…9202`](https://etherscan.io/address/0x1b20b200a78c6068ce5ea96226d1b53e0a119202), including [250,000 on the 22 Sep 2026 pump day (+15.1%)](https://etherscan.io/tx/0x925bcc6666d40853f544e3f4a016959b75f7c6e023f3cc95257d1f41cd09ca17). Every transfer is in the 🔗 Evidence trail below.

**Sections passed: 2 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 2/10 | ❌ FAIL |
| 🏛️ Foundation & team | 4/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 3/10 | ❌ FAIL |
| 📉 Selling behavior | 0/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 3/10 | ❌ FAIL |
| 💧 Liquidity & market | 4/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 7/10 | ✅ PASS |
| 🤝 Adoption & customers | 5/10 | ❌ FAIL |
| 🛡️ Security & audits | 5/10 | ❌ FAIL |
| ⚖️ Regulatory | 6/10 | ✅ PASS |
| 📅 Catalysts & calendar | 4/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 HYPER · Hyperlane · 3.4 / 10 · ❌ FAIL

> **One line:** Excellent open-source plumbing with a token that pays holders nothing, unlocks every month, and whose foundation-funded wallets cashed out $5M into the one big spike.

**Identity:** HYPER = Hyperlane (CoinGecko `hyperlane`, symbol HYPER; Ethereum contract [`0x93a2…10f5`](https://etherscan.io/token/0x93a2db22b7c736b341c32ff666307f4a9ed910f5), deployed by Etherscan's "Hyperlane: Deployer" [`0x79fa…f31c`](https://etherscan.io/address/0x79fa1f70fbba4dd07510b21b32525b602fadf31c)). Not Hyperliquid (HYPE), and not the other small tokens using the HYPER symbol. Matches the pipeline row (Hyperlane, hyperlane.xyz).

| 📊 Market (CoinGecko, 16 Nov 2026 6:50 AM MST) | 🔗 On-chain (Etherscan v2 API, 16 Nov 2026) |
|---|---|
| **Price** $0.03968 | **Ethereum supply** 592.07M HYPER (`tokensupply`); the rest sits on BNB Chain, Base, Arbitrum, Optimism |
| **24h / 7d / 30d** 🔴 −3.6% / −27.1% / −37.2% · 1y −74.7% | **Genesis mint** 802.67M to the deployer, 14 Apr 2025 ([tx](https://etherscan.io/tx/0xd7fb6a4562fa340f0ca493f0d408f1cdeb18f557c0e9ee27342c9d7037275b58)) |
| **Market cap** $13.42M · **FDV** $32.19M | **Team + backers wallet (EOA)** [`0xa7ec…d9ba`](https://etherscan.io/address/0xa7eccdb9be08178f896c26b7bbd8c3d4e844d9ba): 358,740,626 in, 0 left |
| **24h volume** $1.18M | **Foundation-side Safe** [`0x87fc…4b`](https://etherscan.io/address/0x87fcecb180e0275c22cef213ff301816bb24e74b): 443,926,041 in, 0 left |
| **ATH** $0.664 (10 Jul 2025) · now −94.0% | **Circulating / total / max** 338.2M / 811.3M / 1B (CoinGecko) |
| **Pump days, last 365** 44 (CoinGecko closes) | **TVL** $58.2M (DefiLlama) |

---

## 💰 Revenue — Does it make money? · 2/10 · ❌ FAIL

| Metric | Value | Source |
|---|---:|---|
| Protocol fees, 30d / 1y / all time | $50,200 / $361,773 / $1.72M | [Tier A] [DefiLlama Hyperlane](https://defillama.com/protocol/hyperlane) (16 Nov 2026) |
| Revenue (DefiLlama "revenue") | same as fees | same |
| Revenue to HYPER holders | **$0** (`dailyHoldersRevenue` = 0) | same |
| Staking rewards | New HYPER (20% of supply over 25 years), not fees | [Tier A] [Hyperlane Foundation, "Introducing HYPER"](https://medium.com/@hyperlane_fdn/introducing-hyper-f3846883f1f5) |

**What it means:** $362k a year is 2.7% of market cap and none of it reaches holders; stakers are paid in newly minted HYPER. Score **2**, which **trips the Revenue gate**.

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** Fees are small and none reaches holders; stakers are paid in new HYPER.

## 🏛️ Foundation & team — Who is in charge? · 4/10 · ❌ FAIL

| Item | Finding | Source |
|---|---|---|
| Issuer | Hyperlane Foundation (token, treasury, Strategic Launch Provision); core developers at Abacus Works | [Tier A] [Foundation post](https://medium.com/@hyperlane_fdn/introducing-hyper-f3846883f1f5) · [hyperlane.foundation](https://www.hyperlane.foundation/) |
| Published allocation | Expansion Rewards 25.5%, Staking 20%, Core Team 25%, Strategic Launch Provision 11.52%, Early Backers 10.87%, Foundation Treasury 7.11% | same |
| Published wallets | None found for the treasury, team or SLP. The on-chain Safes match the buckets (358.74M = team + backers, to within 0.01%) | Not found (official) · [Tier A] chain |
| Disclosure of SLP use | "bootstrap HYPER liquidity and early market access", but no recipients, market-maker names or loan terms | [Tier A] foundation post |
| Security disclosure | A researcher said in Apr 2026 that the repo had no security policy or private reporting channel ([#8589](https://github.com/hyperlane-xyz/hyperlane-monorepo/issues/8589), since closed) | [Tier A] GitHub |

**What it means:** Public team and a clear allocation table, but the 9.5M that was sold into the July spike went out with no disclosure of who got it or why. Score **4**.

## 🪙 Foundation / team holdings — How many coins do they hold? · 3/10 · ❌ FAIL

| Bucket (Ethereum only) | HYPER now | Notes |
|---|---:|---|
| [`0x0102…8f8f`](https://etherscan.io/address/0x0102c5805b8f2dbb2717f233285a246418c98f8f) (EOA; 74.3M from the foundation Safe) | **61,919,229** | Pays monthly 22nd-of-month amounts to Safes 0x1686, 0x640d, 0x78ee, 0x407b; sent 15M to [`0xd2b2…8742`](https://etherscan.io/address/0xd2b26db232b1b29d4fd3fe8e583e6c98772f8742) (Aug 2026) |
| [`0xbff1…675d`](https://etherscan.io/address/0xbff145eeb5112538b7c3a0c143a889fca4dd675d) (EOA; 89.1M from the team wallet + 20M from foundation Safe) | **67,759,068** | |
| [`0x7462…6ebf`](https://etherscan.io/address/0x7462aaeb71510d947447cbb1283461e0153b6ebf) (EOA; 98.9M from the team wallet) | 13,965,374 | Split 11.34M lots to five wallets on 7–9 Jul 2025 |
| [`0xd2b2…8742`](https://etherscan.io/address/0xd2b26db232b1b29d4fd3fe8e583e6c98772f8742) | 11,000,000 | Sent 4M to a Bybit deposit on 1 Oct 2026 |
| Two 11–14.6M holders funded by `0x7462` ([0x9ec8](https://etherscan.io/address/0x9ec88f8cbcacbbad82638349807a9d31568830c7) · [0x8c86](https://etherscan.io/address/0x8c862ba0c51eb2bc0d96af114d42c885b131ec61)) | 25,959,130 | Never moved |
| [`0xa6c3…fe89d`](https://bscscan.com/address/0xa6c34f2ebd3051164401968550f4de16894fe89d) on **BNB Chain** (EOA; got 192.5M from the foundation-side Safe on 21 Apr 2025 and bridged it out of Ethereum the next day) | **168,437,500** | Sent 12.03M each to two wallets; the rest has not moved. Balance read by BNB Chain RPC `balanceOf` on HYPER's BSC contract [`0xc9d2…a5c4`](https://bscscan.com/token/0xc9d23ed2adb0f551369946bd377f8644ce1ca5c4) [Tier A]; Arkham shows the same 168.438M and tags it "HYPER Whale" with no owner ([Arkham](https://intel.arkm.com/explorer/address/0xa6c34f2ebd3051164401968550f4de16894fe89d)) |
| **Visible insider-tree total (Ethereum + BNB Chain)** | **≈ 348M (≈ 35% of max, more than the 338.2M circulating)** | Was ≈ 180M on Ethereum alone before the BNB Chain balance was found |

**Arkham check ([Tier B] Arkham, read 16 Nov 2026 (signed-in account)):** Arkham labels [`0xbff1…`](https://intel.arkm.com/explorer/address/0xbff145eeb5112538b7c3a0c143a889fca4dd675d) (67.759M) and [`0x7462…`](https://intel.arkm.com/explorer/address/0x7462aaeb71510d947447cbb1283461e0153b6ebf) as **Hyperlane**, which confirms they are team-side. `0xbff1…` sent 12M to `0x7462…`, and `0x7462…` has been paying out to Safes and wallets in the last month. Arkham labels the team + backers wallet [`0xa7ec…`](https://intel.arkm.com/explorer/address/0xa7eccdb9be08178f896c26b7bbd8c3d4e844d9ba) "Hyperlane: Deployer". It is an EOA (its code is an EIP-7702 delegation, not a Safe), so the 358.74M team-and-backer allocation passed through a single key. The foundation-side Safe [`0x87fc…`](https://intel.arkm.com/explorer/address/0x87fcecb180e0275c22cef213ff301816bb24e74b) is unlabelled, with 13 unlabelled signers [Unverified who they are]. Besides the large lots, it paid airdrop-sized amounts (about 3k–12k HYPER) to many users. [`0x0102…`](https://intel.arkm.com/explorer/address/0x0102c5805b8f2dbb2717f233285a246418c98f8f) (61.919M) is an unlabelled "HYPER Whale" that also stakes through Everstake.

**What it means:** Insiders still hold more than the whole free float, mostly in plain EOAs rather than published vesting contracts. The new BNB Chain finding (168.4M in one unlabelled EOA) nearly doubles the visible insider tree. Score **3** (was 4).

## 📉 Selling behavior — Do insiders sell into pumps? · 0/10 · ❌ FAIL

Pump test uses KuCoin HYPER-USDT daily closes (from 22 Apr 2025); CoinGecko closes agree for the last 365 days. Exchange labels are Etherscan name tags [Tier B]; transfers are Tier A.

| Day (UTC) | Route | HYPER | 5-day change | Pump? |
|---|---|---:|---:|---|
| 21–22 Apr 2025 | Foundation Safe `0x87fc` → 8 fresh wallets, round 1.0–1.5M lots ([1](https://etherscan.io/tx/0x2dcd7a3a2a2087fec33415f3a024022fe40315cc23f0522bc08a35f12bf9679a) · [2](https://etherscan.io/tx/0x795bcc89d2cce219674f71943262fc24a80ad30611b92480f31287226835f30c) · [3](https://etherscan.io/tx/0xfc704bbad57eb1f081fc47e5e00001f47c0e06c8a46f4a5ee74295f2abe1d479)) | 9,500,000 | launch | — |
| **10 Jul 2025** | 0x33ee, 0x4cc6, 0x730c, 0x7f8f, 0xf513 → Binance deposits [`0x0450…`](https://etherscan.io/address/0x0450d14321acf6f59e33d748405bf63a9b875a92), [`0x70eb…`](https://etherscan.io/address/0x70eb78ce74c9c71bd26b41e7693ebfd3db40cb13), [`0xe816…`](https://etherscan.io/address/0xe81692033dfad8516899af0ec0b35ae1932f547d) and Bybit [`0xd8da…`](https://etherscan.io/address/0xd8da1644c722930369b6fb77bc8a8c5b40c07290) ([0x33ee](https://etherscan.io/tx/0xf65db08b17cb3629f20fc3318c1327450ea7e6e7f33bcad98b8ee4e598ba60c6) · [0x4cc6](https://etherscan.io/tx/0x0a6357a08fc942a7211ee95148e383c78dea286102b338d00212c87a2c7827dc) · [0x730c](https://etherscan.io/tx/0xd7f15399ee79006b0d2770fbe76cf4acf71e3ecbb0c182b26c329d441d900b88) · [0x7f8f](https://etherscan.io/tx/0xa823951d0dfd794d55016695f570d2389ed18007f12f185b31e2580b3027620b) · [0xf513](https://etherscan.io/tx/0xb5394c6ad09f7c59bf200f8e2c179497a7b4caa9fa8e6a2ab7f33cfc2a0ce2c2)) | 5,399,800 | **+471.9%** | 🔴 Yes |
| **11 Jul 2025** | 0x5649, 0x7f8f → Bybit `0xd8da` ([0x5649](https://etherscan.io/tx/0xfcf0e15a35b15c6edda7537538e6f4f832c5084c769bc3b83aed779c75f55f38) · [0x7f8f](https://etherscan.io/tx/0x8c153cda29e2d5425ab63faddc0c19da19830b378d5bc6965fccaa7ed430c365)) | 1,700,000 | **+445.2%** | 🔴 Yes |
| **12 Jul 2025** | 0x6855, 0xe0ac, 0xf513 → Bybit `0xd8da`, Bybit [`0x660b…`](https://etherscan.io/address/0x660ba81fa5e9e4efa3142402f2009e01b0761a62), Binance `0xe816` ([0x6855](https://etherscan.io/tx/0x1fe54bf2d3da75f65f3ca7fb8e1d66578cb5efde279979213b84c2bb85bf2152) · [0xe0ac](https://etherscan.io/tx/0xd70755ba8722418558ade5978e06d7121b7fb85f0d21075d3fd6c89634ce5896)) | 2,399,900 | **+351.1%** | 🔴 Yes |
| 21 Aug 2026 | Team-side Safe [`0xa59e…`](https://etherscan.io/address/0xa59e59c95313f28ca4d1669356169f1c91f57166) (3.53M from the team wallet) → [`0x3fc8…`](https://etherscan.io/address/0x3fc83bd96b1fe997633ed0959aa3a7b793a2d37f) → Binance `0x1b20` ([tx](https://etherscan.io/tx/0xab52ccf58367336e3c80c037fe70eb3d3bd7f3a6853093f6e2664b22a64c8344)) | 220,515 | +14.4% | 🔴 Yes |
| 22 Sep 2026 | `0x0102` → Safe `0x1686` → Binance `0x1b20` ([tx](https://etherscan.io/tx/0x925bcc6666d40853f544e3f4a016959b75f7c6e023f3cc95257d1f41cd09ca17)) | 250,000 | +15.1% | 🔴 Yes |
| 31 Jul – 23 Oct 2026 | Safe `0x1686` → Binance `0x1b20` every month, 11 deposits ([first](https://etherscan.io/tx/0x75ab163469776ae444c1c2e2766378ccd6f79e08a46c6a2b0b523d81b575b9ca) · [latest](https://etherscan.io/tx/0x6bcf6bd07462e3855f7bc358d24a4cf3eb7ae994193ca1b24748bb83a87a8c8f)) | 5,468,750 total | mostly <10% | Sells everything it is paid |

- **Arkham ([Tier B] Arkham, read 16 Nov 2026 (signed-in account)):** all eight July sellers ([0x730c](https://intel.arkm.com/explorer/address/0x730c11deddd8243ae4f4541f7cbd324c54f31e75) · [0x33ee](https://intel.arkm.com/explorer/address/0x33ee451bf69a668a0dd146342d3cc189f899a2ff) · [0x4cc6](https://intel.arkm.com/explorer/address/0x4cc67796b4eeaac5c8c4cf92d09f3081afccb204) · [0x7f8f](https://intel.arkm.com/explorer/address/0x7f8fb5dcd6c51d280ae71e2a5db2be10515bef90) · [0xf513](https://intel.arkm.com/explorer/address/0xf513e4f8cf8a6baafa189f6c97c7c1314761ac4b) · [0x5649](https://intel.arkm.com/explorer/address/0x56490c6df53dd7016ff748fd38469c9fb0420a55) · [0x6855](https://intel.arkm.com/explorer/address/0x6855bbf38f9e93c6ba7f90bda3e51383ce974a09) · [0xe0ac](https://intel.arkm.com/explorer/address/0xe0ac71529c2480d8d60d26bdd4aa0cc65d72e0d5)) are unlabelled and tagged only "Early HYPER Holder". Their gas came from Binance and OKX hot wallets. Arkham names no owner and no market maker. [`0xd8da1644…c07290`](https://intel.arkm.com/explorer/address/0xd8da1644c722930369b6fb77bc8a8c5b40c07290) is labelled a **Bybit Deposit** (full address checked), and [`0x1b20…`](https://intel.arkm.com/explorer/address/0x1b20b200a78c6068ce5ea96226d1b53e0a119202) a **Binance Deposit**. The dates in the table come from Etherscan, not Arkham's relative ages.
- **One holder behind the July sales:** five of the eight wallets deposited to the same Bybit address `0xd8da…`, and the other three share Binance deposits `0x0450`, `0x70eb` and `0xe816` with them, so the eight are one exchange customer. That customer was funded only by the foundation Safe.
- **Team and foundation money ends up in one Binance account:** `0x1686` (paid by the foundation-funded `0x0102`) and `0x3fc8` (paid by team-side Safe `0xa59e`) both deposit into the same Binance deposit `0x1b20…`.
- Launch day (22 Apr 2025): foundation-funded `0x2af1`, `0x7445`, `0xbbd5` and `0x3b18` moved 12.1M (4.0M + 3.6M + 3.0M + 1.5M) to Binance, Bybit and Gate deposits. That fits the SLP's stated "initial token liquidity" purpose. `0x7445` then collected ~14M from seven wallets and sent it to Binance deposit [`0xdc99…`](https://etherscan.io/address/0xdc99ff848013c8349ae366acc0f3ab5a4d6ebd6e) in Jun–Jul 2026 ([6M](https://etherscan.io/tx/0x56a0f7b58cc724efc89d4087d4d6973a1fe86f1c86136a2b7d4272b6fe9f402a) · [8M](https://etherscan.io/tx/0x9201d2b8cc54f9c2572cca65e2f3188ed0cbfceca0d37292767da4dac38e97ca)), not on pump days.
- Trading wallet [`0x9ec1…7b21`](https://etherscan.io/address/0x9ec1f2b052b4534b387c73c69b3e87324c1c7b21) was paid 833,333 a month by Safe [`0x2999…`](https://etherscan.io/address/0x2999e84ed6271de2b829d9cea16fc42e3d45692c) (9.0M bridged in on 23 Apr 2025; it also pays `0x0102` and launch wallet `0x3b18`) and then by `0x0102`. It also withdraws from Binance and Bybit (market-maker pattern), and it deposited on six pump days (e.g. [2M on 10 Jul 2025](https://etherscan.io/tx/0x57350e02184c6c9d7417522771f1236243dba854734fd516bca5de87ed556f47)). Arkham labels it **Manifold Trading**, a trading firm ([Arkham](https://intel.arkm.com/explorer/address/0x9ec1f2b052b4534b387c73c69b3e87324c1c7b21)), so these are market-maker flows, not team sales.

**What it means:** Foundation-funded wallets sold 9.5M HYPER (≈ $5.2M) into the biggest pump in the token's history, with no disclosure, and foundation- and team-paid wallets are still selling on pump days in 2026. Score **2**, which **trips the Selling gate**.

- **Disclosure quality (16 Nov 2026 rules): silence.** No disclosure of these sales was found. **Penalty applied (16 Nov 2026 rules):** a proven pump-day sale with no disclosure fails Selling (ordinary score at most 3) and then loses 2 points, floored at 0: **2 → 0**. Pump days from KuCoin HYPER-USDT daily closes.

## 📊 Tokenomics & supply · 3/10 · ❌ FAIL

- 1B max, reached in 25 years. CoinGecko shows 338.2M circulating; third-party unlock trackers show ~39% unlocked [Tier B].
- Core Team and Early Backers: 25% cliff at 12 months (22 Apr 2026), then 24 months linear. Foundation Treasury: 6-month cliff, then 30 months linear ([foundation post](https://medium.com/@hyperlane_fdn/introducing-hyper-f3846883f1f5)).
- The team wallet emptied in its first week into unpublished EOAs (0x7462 98.9M, 0xbff1 89.1M) and dozens of smaller Safes, not into published vesting contracts. `0x7462` moved five 11.34M lots on 7–9 Jul 2025, *inside* the team/backer cliff. Two of those wallets later sent 6.5M to FalconX deposits (Sep 2026, after the cliff: [2.48M](https://etherscan.io/tx/0xf378c75495cf4758b9a955d2d0c1338efc8c7d305f00f19fcc55cba4ca4f06f2) · [4M](https://etherscan.io/tx/0xfcd7a4255cab72a47efe63bd6171c607e14ce9c9c214bdf797ade49be57f62e8)). On-chain lockup enforcement is [Unverified].
- Monthly unlocks run to 2028 (13.58M on 22 Nov 2026; 27.61M on 22 Jan 2027, per [CoinLaunch](https://coinlaunch.space/projects/hyperlane/vesting/) [Tier B]).

## 💧 Liquidity & market · 4/10 · ❌ FAIL

- $1.18M of 24h volume on a $13.4M cap (8.8%). Listed on Binance, Upbit (KRW), Bybit, Bitget, Gate, KuCoin and Coinbase. Biggest single book ≈ $150k a day (Binance HYPER/USDT, CoinGecko tickers).
- Down 94% from the ATH and 27% this week; a 1M-HYPER sale is ~$40k, so the books are thin in dollar terms.

## 🧑‍💻 Product & development · 7/10 · ✅ PASS

- [`hyperlane-xyz/hyperlane-monorepo`](https://github.com/hyperlane-xyz/hyperlane-monorepo) committed on 16 Nov 2026 (validator-set expansion #10060; relayer fixes).
- Live on 150+ chains: TRON (Apr 2026), Circle Arc (Sep 2026), Predicate compliance hooks (Jul 2026) ([blog](https://www.hyperlane.xyz/blog)).

## 🤝 Adoption & customers · 5/10 · ❌ FAIL

- TVL $58.2M; fees $362k a year ([DefiLlama](https://defillama.com/protocol/hyperlane)). Canonical bridge for Eclipse, Injective EVM, Lumia, SOON, SonicSVM and Form (foundation post).
- Usage is real but small in fee terms, and Expansion Rewards (paid in HYPER) subsidise it.

## 🛡️ Security & audits · 5/10 · ❌ FAIL

- Audits listed for protocol v1–v3, Sealevel, CosmWasm, Starknet, the HyperToken and a Q2 2025 review ([docs](https://docs.hyperlane.xyz/docs/resources/audits)).
- **12 Oct 2026:** Autheo's THEO warp route on Base minted 19M unbacked THEO through a single-key `TrustedRelayerIsm`; ~$1.76M was lost ([0xCERT](https://www.0xcert.com/advisory/0xCERT-2026-0237) · [OAK](https://onchainattack.org/document/examples/2026-10-autheo-theo-hyperlane-trusted-relayer-ism-unbacked-mint/), Tier B ×2). That was an app configuration Hyperlane's docs warn against ([docs](https://docs.hyperlane.xyz/docs/guides/production/warp-route-deployment/remove-trusted-relayer)), and the CLI's default.
- Open GitHub issue [#9068 "[CRITICAL] LpCollateralRouter Accounting Mismatch Leading to Vault Insolvency"](https://github.com/hyperlane-xyz/hyperlane-monorepo/issues/9068), open since 18 Jul 2026. A WeightedMultisigIsm fund-freeze bug was fixed (Immunefi #66748, PR #8483) [Tier B].

## ⚖️ Regulatory · 6/10 · ✅ PASS

- No enforcement action found. KYC/sanctions hooks are available for warp routes (Predicate, Jul 2026). Listed on Upbit and Coinbase. The foundation's jurisdiction was not confirmed this pass.

## 📅 Catalysts & calendar · 4/10 · ❌ FAIL

| Date | Event |
|---|---|
| **22 Nov 2026** | Monthly unlock, ~13.58M HYPER (team, backers, treasury) [Tier B] |
| 22 Dec 2026 | ~13.58M |
| **22 Jan 2027** | ~27.61M (quarterly Expansion/Staking adds) |
| Ongoing | Foundation-paid Safe `0x1686` sells its monthly payment on Binance |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟡 None at protocol level; THEO app exploit (Oct 2026); open critical issue [#9068](https://github.com/hyperlane-xyz/hyperlane-monorepo/issues/9068) |
| Treasury → exchange during a pump | 🔴 **Yes, via foundation-funded wallets:** 9.5M HYPER on 10–12 Jul 2025 (+351% to +472%). [example](https://etherscan.io/tx/0xd7f15399ee79006b0d2770fbe76cf4acf71e3ecbb0c182b26c329d441d900b88) |
| Treasury-funded wallet → exchange during a pump | 🔴 **Yes, 2026:** [22 Sep 2026](https://etherscan.io/tx/0x925bcc6666d40853f544e3f4a016959b75f7c6e023f3cc95257d1f41cd09ca17) · [21 Aug 2026](https://etherscan.io/tx/0xab52ccf58367336e3c80c037fe70eb3d3bd7f3a6853093f6e2664b22a64c8344) |
| Live mint path | 🟡 By design: staking emissions over 25 years |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| Foundation-funded selling wallets | Hyperlane Foundation (funding on-chain) | Etherscan transfers from Foundation wallets | high | yes (on-chain) | Selling: 9.5M HYPER sold into the largest pump, more on 2026 pump days |

## 📚 Sources

- [Tier A] Methodology update 16 Nov 2026: no new Arkham lookups; the attribution table uses evidence already cited in this report.
- [Tier A] Etherscan v2 API: `tokentx` for the HYPER contract and ~120 wallets traced from "Hyperlane: Deployer"; `tokenbalance`, `tokensupply`, `getsourcecode` (Safe proxies), `getcontractcreation`; read 16 Nov 2026 MST
- [Tier B] Etherscan name tags: "Hyperlane: Deployer", "Hyperlane: stHYPER Token", "Hyperlane: HYPER Airdrop Merkle Distributor", "Binance Deposit" (0x0450, 0x70eb, 0xe816, 0x1b20, 0xdc99, 0x2b60), "ByBit Deposit" (0xd8da, 0x660b, 0x17de, 0x66b4), "FalconX Deposit", "Binance 14"
- [Tier A] [Hyperlane Foundation, "Introducing HYPER" (3 Apr 2025)](https://medium.com/@hyperlane_fdn/introducing-hyper-f3846883f1f5) · [Hyperlane audits](https://docs.hyperlane.xyz/docs/resources/audits) · [blog](https://www.hyperlane.xyz/blog) · [GitHub monorepo](https://github.com/hyperlane-xyz/hyperlane-monorepo)
- [Tier B] Arkham, read 16 Nov 2026 (signed-in account), 'All networks' view: Hyperlane labels on `0xbff1…`, `0x7462…` and `0xa7ec…` ("Hyperlane: Deployer"); Manifold Trading on `0x9ec1…`; Bybit and Binance deposit labels; "Early HYPER Holder" tags on the eight July sellers; `0x87fc…` and `0x1686…` unlabelled Safes; `0xa6c3…` 168.438M (links in Holdings and Selling)
- [Tier A] BNB Chain RPC `balanceOf(0xa6c3…)` on HYPER BSC contract `0xc9d2…a5c4` = 168,437,500; Ethereum `eth_getCode(0xa7ec…)` = EIP-7702 delegation (EOA); read 16 Nov 2026
- [Tier A] DefiLlama fees/revenue/TVL; CoinGecko `hyperlane` (16 Nov 2026 6:50 AM MST); KuCoin HYPER-USDT daily candles for every pump test
- [Tier B] [0xCERT](https://www.0xcert.com/advisory/0xCERT-2026-0237) · [OAK](https://onchainattack.org/document/examples/2026-10-autheo-theo-hyperlane-trusted-relayer-ism-unbacked-mint/) · [CoinLaunch unlocks](https://coinlaunch.space/projects/hyperlane/vesting/)
- [Unverified] who controls the eight July 2025 wallets, `0x0102` and `0xa6c3`; who the signers of Safes `0x87fc` and `0x1686` are; whether team lockups are enforced on-chain

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| 802.67M minted to "Hyperlane: Deployer"; 358.74M to wallet 0xa7ec and 443.93M to Safe 0x87fc | [mint](https://etherscan.io/tx/0xd7fb6a4562fa340f0ca493f0d408f1cdeb18f557c0e9ee27342c9d7037275b58) · [358.74M tx](https://etherscan.io/tx/0x3e661136472dea1b9d0bc2458d08b173fd9b4edcfa3cd7ef88fc4282b9f1c040) · [443.93M tx](https://etherscan.io/tx/0x2e010a4acc5d1ad8ee75a02a9c56e999c71e8ba38a5aa6f8a6948116f9da1bd6) · [0xa7ec](https://etherscan.io/address/0xa7eccdb9be08178f896c26b7bbd8c3d4e844d9ba) · [0x87fc](https://etherscan.io/address/0x87fcecb180e0275c22cef213ff301816bb24e74b) | A | 16 Nov 2026 |
| Published allocation (team 25%, backers 10.87%, treasury 7.11%, SLP 11.52%) | [foundation post](https://medium.com/@hyperlane_fdn/introducing-hyper-f3846883f1f5) | A | 16 Nov 2026 |
| Foundation Safe funded 8 wallets with 9.5M on 21–22 Apr 2025 | [tx 1](https://etherscan.io/tx/0x2dcd7a3a2a2087fec33415f3a024022fe40315cc23f0522bc08a35f12bf9679a) · [tx 2](https://etherscan.io/tx/0x795bcc89d2cce219674f71943262fc24a80ad30611b92480f31287226835f30c) · [tx 3](https://etherscan.io/tx/0xfc704bbad57eb1f081fc47e5e00001f47c0e06c8a46f4a5ee74295f2abe1d479) | A | 16 Nov 2026 |
| The 8 wallets sent 9.5M to Binance/Bybit deposits on 10–12 Jul 2025 | [0x730c](https://etherscan.io/tx/0xd7f15399ee79006b0d2770fbe76cf4acf71e3ecbb0c182b26c329d441d900b88) · [0x33ee](https://etherscan.io/tx/0xf65db08b17cb3629f20fc3318c1327450ea7e6e7f33bcad98b8ee4e598ba60c6) · [0x5649](https://etherscan.io/tx/0xfcf0e15a35b15c6edda7537538e6f4f832c5084c769bc3b83aed779c75f55f38) · [0x6855](https://etherscan.io/tx/0x1fe54bf2d3da75f65f3ca7fb8e1d66578cb5efde279979213b84c2bb85bf2152) | A + B tag | 16 Nov 2026 |
| Safe 0x1686 (paid by 0x0102) → Binance deposit on 22 Sep 2026 pump day | [tx](https://etherscan.io/tx/0x925bcc6666d40853f544e3f4a016959b75f7c6e023f3cc95257d1f41cd09ca17) · [0x1686](https://etherscan.io/address/0x16864253e0ab1d3e6844c24896899f99e5272e7c) | A + B tag | 16 Nov 2026 |
| `0xa6c3` holds 168,437,500 HYPER on BNB Chain | [BscScan](https://bscscan.com/address/0xa6c34f2ebd3051164401968550f4de16894fe89d) · [Arkham](https://intel.arkm.com/explorer/address/0xa6c34f2ebd3051164401968550f4de16894fe89d) | A (RPC) + B | 16 Nov 2026 |
| `0xbff1`, `0x7462` labelled Hyperlane; `0x9ec1` labelled Manifold Trading; `0xd8da…7290` labelled Bybit Deposit | [0xbff1](https://intel.arkm.com/explorer/address/0xbff145eeb5112538b7c3a0c143a889fca4dd675d) · [0x7462](https://intel.arkm.com/explorer/address/0x7462aaeb71510d947447cbb1283461e0153b6ebf) · [0x9ec1](https://intel.arkm.com/explorer/address/0x9ec1f2b052b4534b387c73c69b3e87324c1c7b21) · [0xd8da](https://intel.arkm.com/explorer/address/0xd8da1644c722930369b6fb77bc8a8c5b40c07290) | B (Arkham) | 16 Nov 2026 |
| 0x0102 holds 61.9M; 0xbff1 holds 67.8M | [0x0102](https://etherscan.io/address/0x0102c5805b8f2dbb2717f233285a246418c98f8f) · [0xbff1](https://etherscan.io/address/0xbff145eeb5112538b7c3a0c143a889fca4dd675d) | A | 16 Nov 2026 |
| Fees $361,773 / 1y; holder revenue $0; TVL $58.2M | [DefiLlama](https://defillama.com/protocol/hyperlane) | A | 16 Nov 2026 |
| Open critical-vulnerability issue #9068 | [GitHub](https://github.com/hyperlane-xyz/hyperlane-monorepo/issues/9068) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Who owns the eight July 2025 wallets, `0x0102` and `0xa6c3`?** | Arkham (16 Nov 2026) tags them only "Early HYPER Holder" / "HYPER Whale". Ask the Hyperlane Foundation, and name the signers of Safes `0x87fc` and `0x1686` [Unverified] | Free |
| 2 | **Who got the 9.5M?** | Ask the Hyperlane Foundation whether these were SLP market-maker loans or partner/KOL allocations, and whether any HYPER was returned | Free |
| 3 | **BNB Chain holdings** | `0xa6c3` holds 168.44M on BNB Chain (found 16 Nov 2026). Trace the two 12.03M recipients and watch for exchange deposits | Free (BscScan UI) |
| 4 | **Lockup enforcement** | Ask for the vesting-contract addresses for team and backers; compare with the EOAs that hold the tokens now | Free |
| 5 | **Issue #9068** | Watch for a maintainer response or fix | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
