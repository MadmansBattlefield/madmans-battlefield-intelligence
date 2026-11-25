---
ticker: INJ
name: Injective
chain: injective
contract: "0xe28b3B32B6c345A34Ff64674606124Dd5Aceca30 (ERC-20 on Ethereum); native denom inj"
overall_score: 3.9
overall_verdict: FAIL
section_scores:
  revenue: 2
  foundation_team: 4
  insider_holdings: 4
  selling_behavior: 4
  tokenomics_supply: 4
  liquidity_market: 6
  product_development: 5
  adoption_customers: 3
  security_audits: 3
  regulatory: 6
  catalysts: 5
gates_failed: [revenue]
red_lines:
  one_hop_sale_status: none_found
  hack_exploit: "yes (31 Aug 2026 binary-options settlement exploit, ~$4.9M reported; chain stopped ~3h42m for emergency release v1.20.3-safeharbor.1; second block-production stop 9 Nov 2026; no full postmortem published)"
  treasury_to_exchange_during_pump: "yes, not on a pump day (Arkham 'Injective: Treasury' 0x7e23… sent 5,999,999 INJ to a Binance deposit on 22 Aug 2022); the 650,000 INJ sent to a Binance deposit on 1-8 Dec 2020 pump days came from 0x7ee1…, which Arkham files under GSR Markets: treasury-funded market-maker flow, not a direct treasury sale"
  treasury_funded_wallet_to_exchange_during_pump: "yes, 2020-2024 (e.g. 200k from unlabelled 0x0e64…, funded by an Arkham-labelled Injective wallet, to a Binance deposit on 11-12 Feb 2022, +55%/+41%; 650k via market maker GSR Markets in Dec 2020; 379k from team-chain wallet inj1derhu… to a memo hot wallet on 2023-24 pump days); nothing traced on 2025-26 pump days"
  closed_source_core: "yes (InjectiveFoundation/injective-core releases: 'Starting from 09-09-2026 source code will no longer be published')"
  mint_path_live: "yes by design (x/mint inflation 4.4%, 5.45M INJ/yr; read 16 Nov 2026)"
methodology_effective: 2026-11-16
revenue_reaches_holders: "yes"
revenue_mechanism: "The weekly burn auction is funded from dApp fees and burns INJ on-chain automatically, but stakers receive about 11× more in new INJ; Revenue stays 2."
pump_day_price_source: "Gate and KuCoin INJ-USDT daily closes"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions:
  - address: "0x7e233eafc76243474369bd080238fd6eb36a73ce"
    label: "Injective: Treasury (Arkham), funded by the mint recipient"
    confidence: high
    independent_corroboration: true
    basis: "Etherscan funding + Arkham"
price_usd: 6.65
price_source: "CoinGecko, 16 Nov 2026 5:26 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### INJ · Overall grade **3.9 / 10 · ❌ FAIL**

**Summary:** Injective sells itself as "ultrasound money", but the chain says otherwise: native supply is **123.77M INJ**, not the 100M CoinGecko shows, and the chain still mints about 5.45M INJ a year against roughly 0.3M a year of buyback burns. Fees are about $3.2M a year on a $665M token. On 31 Aug 2026 a bug in the core binary-options code was exploited for a reported ~$4.9M and the chain stopped for almost four hours. On 9 Sep 2026 the core code went closed-source, and block production stopped again on 9 Nov 2026. The genesis distribution chain has a long record of sending INJ into Binance deposit addresses, directly and through market maker GSR Markets, including on pump days in 2020–2024. The Revenue gate fails.

**🚨 Top warning (red line):** The wallet that received **83.3M of the 100M genesis INJ**, [`0x7e23…73ce`](https://etherscan.io/address/0x7e233eafc76243474369bd080238fd6eb36a73ce) (Arkham: **"Injective: Treasury"**, [Arkham](https://intel.arkm.com/explorer/address/0x7e233eafc76243474369bd080238fd6eb36a73ce); funded by the mint recipient [`0x7103…dfcc`](https://etherscan.io/address/0x7103e07e404d2bc6ce354688e52ac1f4629edfcc), Arkham "Injective: Mint" [Arkham](https://intel.arkm.com/explorer/address/0x7103e07e404d2bc6ce354688e52ac1f4629edfcc), [tx](https://etherscan.io/tx/0x9128044be1fe7303da7716c1a013133f3095153891b7705fccd5c17465bb1d8b)), sent **5,999,999 INJ (6% of the then supply, ≈ $10.6M) in one transfer to Etherscan's "Binance Deposit" [`0x29bc…5a81`](https://etherscan.io/address/0x29bcaef59d8a9178455ba262a7fe6f3d5a0a5a81) on 22 Aug 2022** ([tx](https://etherscan.io/tx/0x7804a7fa8f962a67da99a0b31132e05cc18d18344b67124515c8512d92933308)). Not a pump day, and no disclosure of it was found. On pump days, [`0x7ee1…2a86`](https://etherscan.io/address/0x7ee13ec682ac7727d2c82c25d7c5d712683d2a86), a wallet the mint recipient funded with 1M INJ and which Arkham files under **market maker GSR Markets** ([Arkham](https://intel.arkm.com/explorer/address/0x7ee13ec682ac7727d2c82c25d7c5d712683d2a86)), put **650,000 INJ into Binance deposit [`0x2b26…f065`](https://etherscan.io/address/0x2b263f27527f826b2816c349198aea974f9ef065) on 1–8 Dec 2020 (+16% to +39%)** ([4 Dec, 150k](https://etherscan.io/tx/0x6f844acfc7ebf448631be22880abacb4d5b2bd3cd5608e6da7f17259c7e451e1)). That is treasury-funded market-maker flow, not a direct team sale, and no market-maker agreement was disclosed. **Second warning:** the chain's core source code is no longer public ([release notes](https://github.com/InjectiveFoundation/injective-core/releases/tag/v1.20.4-safeharbor.5-1794335565): "Starting from `09-09-2026` source code will no longer be published"), only 9 days after the exploit patch [v1.20.3-safeharbor.1](https://github.com/InjectiveFoundation/injective-core/releases/tag/v1.20.3-safeharbor.1-1788190988) (31 Aug 2026). Every transfer is in the 🔗 Evidence trail below.

**Sections passed: 2 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 2/10 | ❌ FAIL |
| 🏛️ Foundation & team | 4/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 4/10 | ❌ FAIL |
| 📉 Selling behavior | 4/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 4/10 | ❌ FAIL |
| 💧 Liquidity & market | 6/10 | ✅ PASS |
| 🧑‍💻 Product & development | 5/10 | ❌ FAIL |
| 🤝 Adoption & customers | 3/10 | ❌ FAIL |
| 🛡️ Security & audits | 3/10 | ❌ FAIL |
| ⚖️ Regulatory | 6/10 | ✅ PASS |
| 📅 Catalysts & calendar | 5/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 INJ · Injective · 3.9 / 10 · ❌ FAIL

> **One line:** A finance-focused Cosmos chain with a US staking ETF and loud "deflationary" marketing, whose real supply is 24% above its starting 100M, whose fees are tiny, whose core code went private after a ~$4.9M exploit, and whose genesis wallets fed Binance deposit addresses for years, directly and through a market maker.

| 📊 Market (CoinGecko, 16 Nov 2026 5:26 AM MST) | 🔗 On-chain (Injective LCD + Ethereum, 16 Nov 2026) |
|---|---|
| **Price** $6.65 | **Native supply** `bank/supply/inj` **123,765,401 INJ** ([LCD](https://sentry.lcd.injective.network/cosmos/bank/v1beta1/supply/by_denom?denom=inj)) |
| **24h / 7d / 30d** 🔴 −5.19% / −17.15% / −23.55% · 1y −1.40% | **Inflation** 4.4% · annual provisions 5,445,678 INJ ([LCD](https://sentry.lcd.injective.network/cosmos/mint/v1beta1/annual_provisions)) |
| **Market cap** $664.8M · **FDV** $664.8M (CoinGecko uses 100M supply; at 123.77M the cap is ≈ $823M) | **Staked** 56,270,875 INJ (45.5%) ([LCD](https://sentry.lcd.injective.network/cosmos/staking/v1beta1/pool)) |
| **24h volume** $72.57M | **Buyback burn** round 235 burned 24,006.78 INJ; round 236 ends 25 Nov 2026 6:00 AM MST ([LCD](https://sentry.lcd.injective.network/injective/auction/v1beta1/module_state)) |
| **ATH** $52.62 (14 Mar 2024) · now −87.4% | **ERC-20** [`0xe28b…ca30`](https://etherscan.io/address/0xe28b3B32B6c345A34Ff64674606124Dd5Aceca30) · 94.97M locked in the Peggy bridge [`0xF955…D6f3`](https://etherscan.io/address/0xF955C57f9EA9Dc8781965FEaE0b6A2acE2BAD6f3) |
| **Pump days, last 365** 64 (CoinGecko closes) | **TVL** $15.77M (DefiLlama, peak $71.3M Jun 2024) |

---

## 💰 Revenue — Does it make money? · 2/10 · ❌ FAIL

| Metric | Value | Source |
|---|---:|---|
| Chain fees, 30d / 1y | $120,573 / $3,209,168 | [Tier A] [DefiLlama Injective](https://defillama.com/chain/Injective) (16 Nov 2026) |
| Revenue to holders (burn), 30d / 1y | same: $120,573 / $3,209,168 | same (`dailyHoldersRevenue`) |
| Last monthly buyback burn | 24,006.78 INJ (≈ $160k) | [Tier A] [auction module](https://sentry.lcd.injective.network/injective/auction/v1beta1/module_state) |
| New INJ minted to stakers | ~5.45M INJ a year (≈ $36M at $6.65) | [Tier A] [annual_provisions](https://sentry.lcd.injective.network/cosmos/mint/v1beta1/annual_provisions) |

**What it means:** $3.2M a year of fees on a $665M token is 0.5% of market cap. The chain pays stakers about 11 times more in new INJ than it burns. Score **2**, and that **trips the Revenue gate**.

- **Reaches holders (binary test, 16 Nov 2026 rules): Yes.** The weekly burn auction is funded from dApp fees and burns INJ on-chain automatically, but stakers receive about 11× more in new INJ; Revenue stays 2.

## 🏛️ Foundation & team — Who is in charge? · 4/10 · ❌ FAIL

| Item | Finding | Source |
|---|---|---|
| Entities | Injective Labs, Inc., Injective, LLC and Injective Foundation (named together in an SEC Crypto Task Force meeting memo, 13 Jan 2026) | [Tier A] [SEC memo](https://www.sec.gov/about/crypto-task-force/crypto-task-force-meetings/ctf-memo-injective-labs-011326) |
| Leaders | CEO Eric Chen (public) | [Tier B] [Cryptopolitan, 9 Nov 2026](https://www.cryptopolitan.com/injective-halts-block-production-again/) |
| Code control | Core repo moved to `InjectiveFoundation/injective-core`; old `injective-chain-releases` archived 21 Sep 2026; **source closed from 9 Sep 2026** | [Tier A] [GitHub releases](https://github.com/InjectiveFoundation/injective-core/releases) · [archive notice](https://github.com/InjectiveLabs/injective-chain-releases) |
| Incident communication | 1 Sep 2026 statement called the 31 Aug stop "an accelerated network upgrade"; no full postmortem; nothing said about the 9 Nov stop | [Tier B] [Cryptopolitan](https://www.cryptopolitan.com/injective-halts-block-production-again/) · [Lookonchain](https://www.lookonchain.com/feeds/70895) |
| Published treasury wallets | None published by Injective. Arkham files `0x7e23…` as "Injective: Treasury" ([Arkham](https://intel.arkm.com/explorer/address/0x7e233eafc76243474369bd080238fd6eb36a73ce)), `0x7103…` as "Injective: Mint" ([Arkham](https://intel.arkm.com/explorer/address/0x7103e07e404d2bc6ce354688e52ac1f4629edfcc)) and `0xf96b…` as "Injective: Copper Deposit" ([Arkham](https://intel.arkm.com/explorer/address/0xf96b0274840c6a268aac084c32208e56c67756a8)) | Not found (official) · [Tier B] Arkham, read 16 Nov 2026 ~6:50–6:52 AM MST (signed-in account) |

**What it means:** Known people and real entities, but the foundation controls closed-source chain code, publishes no treasury wallets and played down an exploit. Score **4**.

## 🪙 Foundation / team holdings — How many coins do they hold? · 4/10 · ❌ FAIL

| Bucket | INJ | Notes |
|---|---:|---|
| Genesis mint recipient [`0x7103…dfcc`](https://etherscan.io/address/0x7103e07e404d2bc6ce354688e52ac1f4629edfcc) (Arkham "Injective: Mint", [Arkham](https://intel.arkm.com/explorer/address/0x7103e07e404d2bc6ce354688e52ac1f4629edfcc)) | 100,000,000 (Oct 2020) → 0 now | 83.28M → `0x7e23…`, 9M + 1M → Binance deposits, 4.72M → `0x6ef4…`, 1M each → `0xc545…` and GSR Markets' `0x7ee1…` ([mint tx](https://etherscan.io/tx/0xb0dea3bff21634bdead00b464edf346659fb5d2b60d0bb83c4c4a61ab9349d21)) |
| Main distributor [`0x7e23…73ce`](https://etherscan.io/address/0x7e233eafc76243474369bd080238fd6eb36a73ce) (Arkham "Injective: Treasury", [Arkham](https://intel.arkm.com/explorer/address/0x7e233eafc76243474369bd080238fd6eb36a73ce)) and its 2nd-tier wallets | ~0 on Ethereum and on their Injective twins | 15 traced wallets: ERC-20 balance 18 INJ, native ~0.91M (RPC/LCD, 16 Nov 2026) |
| [`inj1trhx…u3ex`](https://explorer.injective.network/account/inj1trhxpuzkl30wh4d89rkcdkv9h5mauzq6fxu3ex/) (funded by 3.45M bridged from `0x58ee…`) | 913,797 liquid + 2,349,344 staked | [LCD](https://sentry.lcd.injective.network/cosmos/staking/v1beta1/delegations/inj1trhxpuzkl30wh4d89rkcdkv9h5mauzq6fxu3ex) |
| [`inj14vdm…mqew`](https://explorer.injective.network/account/inj14vdmf48q3u06sfj3txerln3fpyjhtu6e0xmqew/) | 19,856 + 599,999 staked | LCD |
| **Visible team-chain total** | **~3.9M (≈ 3%)** | Where the rest of the 83M went after bridging is not traced |

**What it means:** The genesis wallets on Ethereum are empty; most INJ was bridged into the native chain, where no treasury address is published. Only ~3.9M is visibly on team-chain wallets now. That is not proof of a small holding, only of an opaque one. Score **4**.

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL

Pump test uses Gate (Nov 2020–Oct 2021) and KuCoin (Oct 2021 on) INJ-USDT daily closes. Exchange labels are Etherscan name tags [Tier B]; the transfers are Tier A. Wallet owners below come from [Tier B] Arkham, read 16 Nov 2026 ~6:50–6:52 AM MST (signed-in account).

| Day (UTC) | Route | INJ | 5-day change | Pump? |
|---|---|---:|---:|---|
| 18 Oct 2020 | Mint recipient `0x7103…` → "Binance Deposit" [`0xa0df…`](https://etherscan.io/address/0xa0df95265400327e704a77af6036a24417e2bf00) ([tx](https://etherscan.io/tx/0x8f01c3fadaf4f296cf9a0e658933a6a9d86d016f1c8d21f16a3a5b6b1a2a38dc)) + 2 × 500k to two more Binance deposits | 10,000,000 | before trading | — |
| 1, 2, 4, 8 Dec 2020 | Mint-funded `0x7ee1…`, **GSR Markets** (market maker; [Arkham](https://intel.arkm.com/explorer/address/0x7ee13ec682ac7727d2c82c25d7c5d712683d2a86)) → "Binance Deposit" `0x2b26…` ([1 Dec](https://etherscan.io/tx/0x86dc75d5f27606c0657a021685f743591878b7991d629448502ec6b55268bc1c) · [2 Dec](https://etherscan.io/tx/0x3ca573e8fa36cb994e8acea2952ebf712d26706933c975f9a811edf1e3092c1c) · [4 Dec](https://etherscan.io/tx/0x6f844acfc7ebf448631be22880abacb4d5b2bd3cd5608e6da7f17259c7e451e1) · [8 Dec](https://etherscan.io/tx/0xc7e339717da47346f07be155949837ae888e92fa862e0099d3236fe8fe209a53) · [8 Dec](https://etherscan.io/tx/0xdcbed3d35b453c35a3ccf08a3582ff22029998eb68caaad412aed5b5698afb50)) | 650,000 | +16% to +39% | 🟠 Yes, market-maker flow funded by the mint wallet |
| 22 Apr 2021 | Distributor → `0xf96b…`, Arkham "Injective: Copper Deposit" ([Arkham](https://intel.arkm.com/explorer/address/0xf96b0274840c6a268aac084c32208e56c67756a8)) → "Copper 5" custody ([tx](https://etherscan.io/tx/0xd90781d8afb72a3b17d0c9fd549d8d5515f6fb0dbd1f2d0dfb14f251c1a8c38f)) | 8,000,000 | +13.6% | 🟡 Injective's own Copper custody account, not an exchange |
| 11–12 Feb 2022 | Unlabelled [`0x0e64…`](https://etherscan.io/address/0x0e649d9a119c525716bf00fe76b6bababf90537e) ([Arkham](https://intel.arkm.com/explorer/address/0x0e649d9a119c525716bf00fe76b6bababf90537e); funded by `0xf282…`, which Arkham files under entity Injective, [Arkham](https://intel.arkm.com/explorer/address/0xf282d55d253ae36135c0797b43b51b55735d28bf)) → "Binance Deposit" `0xb65f…`, 2 × 100k (Arkham also tags it Binance Deposit) ([11 Feb](https://etherscan.io/tx/0x287d4530391a750934a648c54afe272eb55f6dd99158f8c649bfd10597d01002) · [12 Feb](https://etherscan.io/tx/0x97258bbf0cea1d475e75f59ae3f2200fddf429adb2ac90c2bcfd11696bf4811b)) | 200,000 | +55.5% / +40.6% | 🔴 Yes |
| 6 Jul 2022 | 2nd-tier `0x65e3…` → "Binance Deposit" `0x4e90…` ([tx](https://etherscan.io/tx/0x257e26ac9d6b8641beb631801e51e3d522be2a793a2e7a24aa97cb53adfbfe1d)) | 1,500,000 | <10% | No |
| 22 Aug 2022 | "Injective: Treasury" `0x7e23…` → "Binance Deposit" `0x29bc…` ([tx](https://etherscan.io/tx/0x7804a7fa8f962a67da99a0b31132e05cc18d18344b67124515c8512d92933308)) | 5,999,999 | <10% | No |
| 12 Dec 2023 · 20 May 2024 · 6 Jun 2024 (+ others) | Team-chain [`inj1derhu…`](https://explorer.injective.network/account/inj1derhu7tj7vuh69qm0xnjmwd7npllt6gu3ve4l0/) → memo hot wallet [`inj1u2raj…`](https://explorer.injective.network/account/inj1u2rajhqtptzvu23leheta9yg99k3hazf4waf43/) ([12 Dec](https://explorer.injective.network/transaction/0x0939c457151b5032ca09d366a7da0cfbef07f2e3b62da178ec9c29c62b5899a7/) · [20 May](https://explorer.injective.network/transaction/0x11ec28d94805e69b672ae33a6cda32cbb592f0f1afc20dfc5f2ac88d670ace84/) · [6 Jun](https://explorer.injective.network/transaction/0x7c7a52c22855b952494beba019b720ac535c044e6ea371126060225d7b3506de/)) | 379,000 on pump days (1,244,665 in total, Apr 2023–Jun 2024) | +40.3% / +19.7% / +14.5% | 🔴 Yes |

- Totals from a 106-wallet trace of the genesis tree on Ethereum: **34.7M INJ** went to labelled exchange or custody addresses, **10.3M on pump days** (most of that is the 8M move into Injective's own Copper custody). Labelled-exchange-only pump-day total ≈ **1.9M INJ**, of which 650k went through GSR Markets, leaving ≈ **1.25M** from wallets in the team's own tree.
- `inj1derhu…` was funded by `0x25f9…` (bridge, 300k, [tx](https://etherscan.io/tx/0xf996df00ddf3053bcaf3592b0bd62982948a9577ce6b4f48d0d14119905f5682)) and its Injective twin `inj1yhuk…` (600k). `0x25f9…` was funded by `0x37d0…`, which was funded by the main distributor. Arkham files `0x25f9…` under entity Injective ([Arkham](https://intel.arkm.com/explorer/address/0x25f96510d3563b97e0fcbb723b7fe83257aee37d)) and shows it receiving 500k and 1M from "Injective: Treasury" and bridging them out; `0x37d0…` is unlabelled there. `inj1u2raj…` takes ~100 numeric-memo deposits every 6–7 hours, the pattern of an exchange hot wallet; which exchange is [Unverified].
- **2025–26:** none of the traced wallets sent INJ to an exchange on any of the 64 pump days in the last year. The native-chain trace only reached 10 accounts, so this is "not found", not "cleared".

**What it means:** Arkham changes who did one of these, not the score. The biggest pump-day flow (650k, Dec 2020) was a market maker, GSR Markets, trading coins the mint wallet gave it. That is treasury-funded market-maker flow, not a team sale, but it was never disclosed. At the same time Arkham ties the funders of the 2022 and 2023–24 pump-day flows (`0xf282…`, `0x25f9…`) to the Injective entity, which makes those more clearly the team's own. Add the single 6M deposit from "Injective: Treasury". All of it is 2020–2024, and none of it was found in the last year. **Selling stays 4**, one point above the gate.

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from Gate and KuCoin INJ-USDT daily closes.

## 📊 Tokenomics & supply · 4/10 · ❌ FAIL

- **Supply is 123,765,401 INJ, not 100M** ([LCD](https://sentry.lcd.injective.network/cosmos/bank/v1beta1/supply/by_denom?denom=inj)). CoinGecko still shows 100M circulating/total, so its market cap understates the token by ~24%.
- Injective's own blog says 6.87M INJ had been burned by Jan 2026 ([blog](https://injective.com/blog/introducing-the-inj-supply-squeeze)). Inflation minted more than that. IIP-617 "Supply Squeeze" (Jan 2026, 99.96% yes) cuts the inflation band to 2.2–4.4%. The current rate is 4.4%, the top of the band ([LCD](https://sentry.lcd.injective.network/cosmos/mint/v1beta1/inflation)).
- Every genesis allocation has been unlocked since early 2024. No vesting cliffs are left.

## 💧 Liquidity & market · 6/10 · ✅ PASS

- $72.6M of 24h volume on a $665M cap (11%). INJ trades on Binance, Coinbase (INJ-USD online), KuCoin, Upbit and Bithumb, and through the Nasdaq ETF INJC.
- Korean exchanges and Binance froze deposits and withdrawals during both chain stops ([Lookonchain](https://www.lookonchain.com/feeds/70895) · [Cryptopolitan](https://www.cryptopolitan.com/injective-halts-block-production-again/)). Down 87% from the high.

## 🧑‍💻 Product & development · 5/10 · ❌ FAIL

- The chain is live and shipping: v1.20.4 (18 Sep 2026), the v1.20.4-bl.3 and safeharbor.5 fixes (9–10 Nov 2026), and v1.21.0-beta on testnet ([releases](https://github.com/InjectiveFoundation/injective-core/releases)).
- But only binaries are published from 9 Sep 2026, and validators are asked to run code nobody outside can read. The SDKs (`sdk-go`, `injective-ts`) are still public.

## 🤝 Adoption & customers · 3/10 · ❌ FAIL

- Chain TVL is **$15.77M**, down from $71.3M in Jun 2024 ([DefiLlama](https://defillama.com/chain/Injective)). Fees are $120k a month.
- The Canary ETF held $16.1M after two sessions, with a flat share count ([Cryptopolitan](https://www.cryptopolitan.com/injective-halts-block-production-again/)) [Tier B].

## 🛡️ Security & audits · 3/10 · ❌ FAIL

- **31 Aug 2026 exploit:** a market-ID collision plus a missing insurance-fund denomination check in core binary-options settlement. Reported loss ~1,979.8 ETH (≈ $4.9M), bridged to Ethereum. Emergency release [v1.20.3-safeharbor.1](https://github.com/InjectiveFoundation/injective-core/releases/tag/v1.20.3-safeharbor.1-1788190988) (31 Aug 2026, 8:43 AM MST); block production stopped ~3h42m at height 181,027,006 ([Lookonchain](https://www.lookonchain.com/feeds/70895) · [Metaverse Post](https://mpost.io/injective-exploited-for-4-9m-via-market-id-collision-in-binary-options-settlement-logic/)). The loss figure rests on two Tier B sources; Injective has not given its own.
- **9 Nov 2026:** block production stopped again; releases [v1.20.4-bl.3](https://github.com/InjectiveFoundation/injective-core/releases/tag/v1.20.4-bl.3-1794240970) and [safeharbor.5](https://github.com/InjectiveFoundation/injective-core/releases/tag/v1.20.4-safeharbor.5-1794335565) followed. Cause not disclosed.
- With the code closed, outside review of the fixes is no longer possible.

## ⚖️ Regulatory · 6/10 · ✅ PASS

- Nasdaq listed the **Canary Staked INJ ETF (INJC) on 5 Nov 2026** ([Nasdaq trader alert ETP2026-179](https://www.nasdaqtrader.com/TraderNews.aspx?id=ETP2026-179)).
- The Injective entities met the SEC Crypto Task Force on 13 Jan 2026 ([memo](https://www.sec.gov/about/crypto-task-force/crypto-task-force-meetings/ctf-memo-injective-labs-011326)). No enforcement action was found this pass.
- Upbit named INJ a "Trading Attention" asset after the August stop ([Lookonchain](https://www.lookonchain.com/feeds/70895)) [Tier B].

## 📅 Catalysts & calendar · 5/10 · ❌ FAIL

| Date | Event |
|---|---|
| **25 Nov 2026 6:00 AM MST** | Round 236 Community BuyBack burn ends (every 28 days) |
| Now | Whether Upbit/Bithumb lift the INJ deposit freeze, and whether a postmortem for the 9 Nov stop comes |
| Ongoing | INJC flows (share count was flat after launch) |
| Quarterly | Inflation-band reductions under IIP-617 |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🔴 **Yes:** ~$4.9M binary-options exploit, 31 Aug 2026, plus a chain stop; another stop on 9 Nov 2026. [patch](https://github.com/InjectiveFoundation/injective-core/releases/tag/v1.20.3-safeharbor.1-1788190988) |
| Treasury → exchange during a pump | 🟠 **Via a market maker (2020):** mint-funded `0x7ee1…`, which Arkham files under GSR Markets ([Arkham](https://intel.arkm.com/explorer/address/0x7ee13ec682ac7727d2c82c25d7c5d712683d2a86)), → Binance deposit, 650k INJ on 1–8 Dec 2020. [4 Dec tx](https://etherscan.io/tx/0x6f844acfc7ebf448631be22880abacb4d5b2bd3cd5608e6da7f17259c7e451e1). Direct: "Injective: Treasury" → Binance 6M on 22 Aug 2022 (not a pump day). [tx](https://etherscan.io/tx/0x7804a7fa8f962a67da99a0b31132e05cc18d18344b67124515c8512d92933308) |
| Treasury-funded wallet → exchange during a pump | 🔴 **Yes, 2022–2024:** [11 Feb 2022](https://etherscan.io/tx/0x287d4530391a750934a648c54afe272eb55f6dd99158f8c649bfd10597d01002) · [12 Dec 2023](https://explorer.injective.network/transaction/0x0939c457151b5032ca09d366a7da0cfbef07f2e3b62da178ec9c29c62b5899a7/); none found in 2025–26 |
| Closed-source core | 🔴 **Yes,** from 9 Sep 2026. [release notes](https://github.com/InjectiveFoundation/injective-core/releases/tag/v1.20.4-safeharbor.5-1794335565) |
| Live mint path | 🟡 By design: 4.4% inflation. [LCD](https://sentry.lcd.injective.network/cosmos/mint/v1beta1/inflation) |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| [`0x7e23…73ce`](https://etherscan.io/address/0x7e233eafc76243474369bd080238fd6eb36a73ce) | Injective: Treasury (Arkham), funded by the mint recipient | Etherscan funding + Arkham | high | yes (on-chain) | Selling: 6M to Binance on 22 Aug 2022, not a pump day |
| `0xf282…`, `0x25f9…` funders | Injective (Arkham only) | Arkham | low | no | None: cannot move Selling |
| `0x7ee1…` | GSR Markets (Arkham) | Arkham | medium | no | None: market-maker flow, not a team sale |

## 📚 Sources

- [Tier A] Methodology update 16 Nov 2026: no new Arkham lookups; the attribution table uses evidence already cited in this report.
- [Tier A] Etherscan v2 API `tokentx` (INJ ERC-20), `getcontractcreation`; 106-wallet trace from the mint recipient; read 16 Nov 2026 MST
- [Tier A] Ethereum RPC (`eth_call balanceOf`, `eth_getTransactionReceipt` for Peggy `SendToInjective` destinations)
- [Tier A] Injective LCD (`sentry.lcd.injective.network`): supply, mint, staking pool, auction module, balances, delegations · Injective explorer API `accountTxs`
- [Tier B] Etherscan name tags: "Injective Protocol: Deployer", "Injective: Peggy Bridge Proxy", "Binance Deposit" (`0xa0df…`, `0x2b26…`, `0x29bc…`, `0x4e90…`, `0xb65f…`), "KuCoin Deposit", "Gate Deposit", "Copper 5", "HTX 2", "Crypto.com 1", "Coinbase Prime 1"
- [Tier A] [GitHub InjectiveFoundation/injective-core releases](https://github.com/InjectiveFoundation/injective-core/releases) · [archived injective-chain-releases](https://github.com/InjectiveLabs/injective-chain-releases)
- [Tier A] [Injective blog: Supply Squeeze](https://injective.com/blog/introducing-the-inj-supply-squeeze) · [SEC CTF memo](https://www.sec.gov/about/crypto-task-force/crypto-task-force-meetings/ctf-memo-injective-labs-011326) · [Nasdaq ETP2026-179](https://www.nasdaqtrader.com/TraderNews.aspx?id=ETP2026-179)
- [Tier B] [Cryptopolitan, 9 Nov 2026](https://www.cryptopolitan.com/injective-halts-block-production-again/) · [Lookonchain, 1 Sep 2026](https://www.lookonchain.com/feeds/70895) · [Metaverse Post](https://mpost.io/injective-exploited-for-4-9m-via-market-id-collision-in-binary-options-settlement-logic/)
- [Tier A] DefiLlama chain fees/TVL; CoinGecko `injective-protocol` (16 Nov 2026 5:26 AM MST); Gate and KuCoin INJ-USDT daily candles for every pump test
- [Tier B] Arkham, read 16 Nov 2026 ~6:50–6:52 AM MST (signed-in account): "Injective: Mint" [Arkham](https://intel.arkm.com/explorer/address/0x7103e07e404d2bc6ce354688e52ac1f4629edfcc) · "Injective: Treasury" [Arkham](https://intel.arkm.com/explorer/address/0x7e233eafc76243474369bd080238fd6eb36a73ce) · GSR Markets [0x7ee1…](https://intel.arkm.com/explorer/address/0x7ee13ec682ac7727d2c82c25d7c5d712683d2a86) · "Injective: Copper Deposit" [Arkham](https://intel.arkm.com/explorer/address/0xf96b0274840c6a268aac084c32208e56c67756a8) · unlabelled [0x0e64…](https://intel.arkm.com/explorer/address/0x0e649d9a119c525716bf00fe76b6bababf90537e) (2 × 100k to Binance Deposit 0xb65) · entity Injective on `0xf282…` and `0x25f9…`; `0x37d0…` unlabelled; `0x8061…` only an OpenSea name. Token filter is Enterprise-only, so only the default transfer page was read
- [Unverified] who controls `0x0e64…` and `inj1derhu…`; whether GSR had a disclosed market-making agreement; which exchange runs `inj1u2raj…`; what the 6M Binance deposit was for; original allocation table

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Full 100M ERC-20 mint went to `0x7103…`; 83.28M on to `0x7e23…` | [contract creation](https://etherscan.io/tx/0xb0dea3bff21634bdead00b464edf346659fb5d2b60d0bb83c4c4a61ab9349d21) · [83.28M](https://etherscan.io/tx/0x9128044be1fe7303da7716c1a013133f3095153891b7705fccd5c17465bb1d8b) | A | 16 Nov 2026 |
| 22 Aug 2022: 5,999,999 INJ from `0x7e23…` to a Binance deposit | [tx](https://etherscan.io/tx/0x7804a7fa8f962a67da99a0b31132e05cc18d18344b67124515c8512d92933308) · [deposit](https://etherscan.io/address/0x29bcaef59d8a9178455ba262a7fe6f3d5a0a5a81) | A + B tag | 16 Nov 2026 |
| Dec 2020 pump days: 650k from `0x7ee1…` (GSR Markets per Arkham [Arkham](https://intel.arkm.com/explorer/address/0x7ee13ec682ac7727d2c82c25d7c5d712683d2a86); mint-funded, [tx](https://etherscan.io/tx/0xc0a5756ef5953d4c474172a7891825afb53ca9a3dd08f7f1a50d335f48b0bf76)) to Binance deposit | [1 Dec](https://etherscan.io/tx/0x86dc75d5f27606c0657a021685f743591878b7991d629448502ec6b55268bc1c) · [4 Dec](https://etherscan.io/tx/0x6f844acfc7ebf448631be22880abacb4d5b2bd3cd5608e6da7f17259c7e451e1) · [8 Dec](https://etherscan.io/tx/0xc7e339717da47346f07be155949837ae888e92fa862e0099d3236fe8fe209a53) | A + B | 16 Nov 2026 |
| Feb 2022 pump days: 200k from unlabelled `0x0e64…` ([Arkham](https://intel.arkm.com/explorer/address/0x0e649d9a119c525716bf00fe76b6bababf90537e)) to Binance deposit | [11 Feb](https://etherscan.io/tx/0x287d4530391a750934a648c54afe272eb55f6dd99158f8c649bfd10597d01002) · [12 Feb](https://etherscan.io/tx/0x97258bbf0cea1d475e75f59ae3f2200fddf429adb2ac90c2bcfd11696bf4811b) | A + B | 16 Nov 2026 |
| `0x25f9…` bridged 8.71M to its own native twin `inj1yhuk…` | [1.61M tx](https://etherscan.io/tx/0xfcaa50d8d8fa7c66bbc9cc8c42f20d2e56acc3ff3dd8cc672f34ae105bb6d872) · [inj1yhuk](https://explorer.injective.network/account/inj1yhuk2yxn2cae0c8uhderkllgxft6acmagqwyhg/) | A | 16 Nov 2026 |
| 2023–24 pump days: `inj1derhu…` → memo hot wallet | [12 Dec 2023](https://explorer.injective.network/transaction/0x0939c457151b5032ca09d366a7da0cfbef07f2e3b62da178ec9c29c62b5899a7/) · [20 May 2024](https://explorer.injective.network/transaction/0x11ec28d94805e69b672ae33a6cda32cbb592f0f1afc20dfc5f2ac88d670ace84/) · [6 Jun 2024](https://explorer.injective.network/transaction/0x7c7a52c22855b952494beba019b720ac535c044e6ea371126060225d7b3506de/) | A · exchange [Unverified] | 16 Nov 2026 |
| Arkham labels: `0x7103…` Injective: Mint, `0x7e23…` Injective: Treasury, `0xf96b…` Injective: Copper Deposit (8M in from Treasury, 8M out to Copper hot wallet) | [0x7103](https://intel.arkm.com/explorer/address/0x7103e07e404d2bc6ce354688e52ac1f4629edfcc) · [0x7e23](https://intel.arkm.com/explorer/address/0x7e233eafc76243474369bd080238fd6eb36a73ce) · [0xf96b](https://intel.arkm.com/explorer/address/0xf96b0274840c6a268aac084c32208e56c67756a8) | B | 16 Nov 2026 ~6:50–6:52 AM MST |
| Native supply 123,765,401 INJ; inflation 4.4% | [supply](https://sentry.lcd.injective.network/cosmos/bank/v1beta1/supply/by_denom?denom=inj) · [inflation](https://sentry.lcd.injective.network/cosmos/mint/v1beta1/inflation) | A | 16 Nov 2026 |
| Source code closed from 9 Sep 2026 | [release notes](https://github.com/InjectiveFoundation/injective-core/releases/tag/v1.20.4-safeharbor.5-1794335565) | A | 16 Nov 2026 |
| 31 Aug 2026 exploit patch and ~$4.9M loss | [safeharbor.1](https://github.com/InjectiveFoundation/injective-core/releases/tag/v1.20.3-safeharbor.1-1788190988) · [Lookonchain](https://www.lookonchain.com/feeds/70895) · [Cryptopolitan](https://www.cryptopolitan.com/injective-halts-block-production-again/) | A (patch) + 2 × B (loss) | 16 Nov 2026 |
| Fees $3.21M / 1y; TVL $15.77M | [DefiLlama](https://defillama.com/chain/Injective) | A | 16 Nov 2026 |
| INJC ETF listed 5 Nov 2026 | [Nasdaq](https://www.nasdaqtrader.com/TraderNews.aspx?id=ETP2026-179) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Arkham pass: done for Ethereum, 16 Nov 2026.** Still open: owner of `0x0e64…` (unlabelled), `0x37d0…` and `0x8061…`; Arkham does not cover the native Injective chain, so `inj1derhu…`, `inj1u2raj…` and `inj1trhx…` stay unlabelled | Ask Injective; check Mintscan/Injective explorer labels; ask GSR or Injective whether a market-making agreement covered the 2020 flow | Free |
| 2 | **What was the 6M INJ Binance deposit of 22 Aug 2022?** | Search Injective blog/forum and Binance announcements for Aug 2022 (OTC, market-maker or ecosystem fund) | Free |
| 3 | **Native-chain trace for 2025–26** | Extend the explorer `accountTxs` trace past depth 2 from `inj1yhuk…`, `inj1trhx…` and the 8061/0x65e3 bridge destinations; test every 2025–26 pump day | Free, slow (explorer API) |
| 4 | **Original allocation table** | Read the Injective tokenomics paper and match each bucket to a genesis wallet | Free |
| 5 | **Postmortems** | Watch for an official report on the 31 Aug and 9 Nov 2026 stops | Free |

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

### Holder mix (top 100 holders)
- Nansen's holders pass returned no ownership percentages for INJ, so no exchange share or issuer-held figure is reported.
- Unscored: this line has no effect on the score, badge or ranking. Labels are Nansen's (a third-party labeler) and are leads, not confirmed ownership.
