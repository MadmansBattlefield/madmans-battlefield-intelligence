---
ticker: CPOOL
name: Clearpool (migrating to CLEAR)
chain: ethereum
contract: "0x66761fa41377003622aee3c7675fc7b5c1c2fac5 (ERC-20 CPOOL on Ethereum)"
overall_score: 3.3
overall_verdict: FAIL
section_scores:
  revenue: 2
  foundation_team: 4
  insider_holdings: 4
  selling_behavior: 0
  tokenomics_supply: 3
  liquidity_market: 3
  product_development: 6
  adoption_customers: 4
  security_audits: 6
  regulatory: 6
  catalysts: 4
gates_failed: [revenue, selling_behavior]
red_lines:
  hack_exploit: none found
  treasury_to_exchange_during_pump: "yes: the 17.17% Reserve allocation (Safe 0x55f6…) was moved to plain EOAs and, from EOA 0x9038…, sent 123.3M CPOOL (~$3.38M) to Bitget, Bybit, Kraken and KuCoin in the last 12 months, 34.6M (~$1.17M) on pump days (26/29/30 Dec 2025, 22/24 Sep 2026)"
  treasury_funded_wallet_to_exchange_during_pump: "yes: peel chains 0x9038 → fresh wallet(s) → Bitget 6, amounts passed through unchanged, often within minutes"
  unenforced_lockups: "yes: docs say team and treasury tokens sit in 'multi-sig cold storage', but every bucket Safe was emptied into plain EOAs on 24–31 Jan 2022"
  mint_path_live: "CPOOL no (fixed 1B). CLEAR yes: 428.6M new tokens at migration plus 1–4% a year, no max supply"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "The origination fee goes to the treasury; buybacks stopped two years ago."
pump_day_price_source: "KuCoin CPOOL-USDT daily closes"
pump_day_disclosure_quality: silence
pump_day_undisclosed_penalty_applied: true
dual_review: not_run
attributions: []
price_usd: 0.02517
price_source: "CoinGecko, 16 Nov 2026 6:51 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### CPOOL · Overall grade **3.3 / 10 · ❌ FAIL**

**Summary:** Clearpool runs on-chain institutional credit (Prime, Credit Vaults, Dynamic pools) with about $1B of lifetime origination, a MiCAR white paper and audited contracts. The token is in poor shape: −99% from its 2021 high, $1.3M a day of volume (mostly Upbit KRW), $14M TVL, and holders get $0 of the ~$1.0M a year in fees (buybacks stopped after Q3 2024). Tomorrow (17 Nov 2026) CPOOL migrates 1:1 into CLEAR, which adds 428.6M new tokens (+42.9%) and an open-ended 1–4% a year. On-chain, the **"multi-sig cold storage" treasury is a fiction since January 2022**: every allocation Safe was emptied into plain wallets, and the Reserve allocation has been fed onto exchanges, pump day after pump day, through throw-away wallets. Both gates fail.

**🚨 Top warning (red line):** The Reserve bucket (17.17%, "daily vesting over 60 months", "multi-sig cold storage") received exactly 171,666,666.67 CPOOL from the genesis Safe into Safe [`0x55f6…69d7`](https://etherscan.io/address/0x55f638da67e1c911cb9d9b03b16128461b1769d7) ([tx](https://etherscan.io/tx/0xb330768122433b98e6d7af12e92ce403a461e521fc8811724a981da8e403f08f)). On 28 Jan 2022 the whole amount went to a plain wallet [`0x60b0…2572`](https://etherscan.io/address/0x60b07a990ab29e1ef333ea037c1ee0bfd7cc2572) ([tx](https://etherscan.io/tx/0xcb9864908480c91c47bc40da0f8288c1b36c22bd5f8e7b950daaadf988a54729)), then 154.77M hopped EOA → EOA ([6 Jun 2024](https://etherscan.io/tx/0xfbaac84ca2ebdc30fc50f62f359c0b5ce4051ab333e0f81316e4693f8190d328), [20 Mar 2025](https://etherscan.io/tx/0x041c0eb8c1dbaafcb814ecbed1eac738886264aff260af052c4ae87404c49bbd)) to [`0x9038…636e`](https://etherscan.io/address/0x9038101003c80ef389c8abb9493a2a2cee42636e). **Since 16 Nov 2025 that wallet has put 123.3M CPOOL (~$3.38M at KuCoin closes) onto Bitget, Bybit, Kraken and KuCoin**, directly or through one- or two-hop fresh wallets that pass the exact amount on. **34.6M (~$1.17M) landed on pump days**: 6M to Bitget on 26 Dec 2025 (+29.4%), six minutes after 0x9038 funded the relay ([fund](https://etherscan.io/tx/0x52a25ae18cf74f5ad7373281d1354507de1be2a2c070b86cbeebf7a69a1d7c01), [deposit](https://etherscan.io/tx/0x4189285ad53fdc101614a1501a6d9b42f461b7eedff188d9c686e34719c9d9db)); 12M on 29–30 Dec 2025 (+10.0%, +13.7%) ([tx](https://etherscan.io/tx/0x839b0ad9b09bda27470e8fba5612afae91edbf554753aae52e7d805a90261345), [tx](https://etherscan.io/tx/0x54591897a1efb48403761632130b162a110b533667d118ccea303b7ff051cdc2)); and 16.62M straight to a Bybit deposit on 22 and 24 Sep 2026 (+25.8%, +25.9%) ([tx](https://etherscan.io/tx/0x5c188b69d5b8d0b30ca134ef4e28cfd9c8e3b6e45e750c076230e02f109e7269), [tx](https://etherscan.io/tx/0x2abcaa79f948cef99671084142c8237c207d86138cb3bda91d13e664828824ca)). 0x9038 is now empty. **Second warning:** the same pattern in 2024: the Reserve EOA `0x60b0` funded `0x46cc` (a wallet Arkham labels **Hex Trust**, a custodian) and `0xdafb` (Arkham: **Clearpool Finance: Deployer**) with 27.5M in Feb–Apr 2024 ([e.g.](https://etherscan.io/tx/0x2c062ccb09a2ab5bf5f935febe6566cb62ca0cf8baf1f1db1ae6e14510f75f1a)), and they sent 16.67M to Bybit deposits on five pump days, including 5.67M on 27 Mar 2024 at **+112%** ([tx](https://etherscan.io/tx/0x84ba2b9afe76225bbf73235ed00cffa23ba5953a11e4b50218fbe90f4cdc2c43)). None of it was announced. Every transfer is in the 🔗 Evidence trail below.

**Sections passed: 3 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 2/10 | ❌ FAIL |
| 🏛️ Foundation & team | 4/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 4/10 | ❌ FAIL |
| 📉 Selling behavior | 0/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 3/10 | ❌ FAIL |
| 💧 Liquidity & market | 3/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 6/10 | ✅ PASS |
| 🤝 Adoption & customers | 4/10 | ❌ FAIL |
| 🛡️ Security & audits | 6/10 | ✅ PASS |
| ⚖️ Regulatory | 6/10 | ✅ PASS |
| 📅 Catalysts & calendar | 4/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 CPOOL · Clearpool · 3.3 / 10 · ❌ FAIL

> **One line:** A real institutional-credit protocol whose "cold-storage" treasury has been quietly walked onto exchanges, now diluting 43% into CLEAR.

**Identity:** CPOOL = Clearpool, clearpool.finance. CoinGecko `clearpool`, symbol CPOOL, Ethereum contract [`0x6676…fac5`](https://etherscan.io/token/0x66761fa41377003622aee3c7675fc7b5c1c2fac5) (listed in the official [Contracts & Audits](https://docs.clearpool.finance/clearpool) page; 1B minted to genesis Safe [`0xe030…04af`](https://etherscan.io/address/0xe0308d5681afe01a8ad1cc0b8c937db699e204af)). Migrates 1:1 to CLEAR [`0x5200…0E00`](https://etherscan.io/address/0x5200f539478f58d9aea962095ba3b16b5e550e00) from 17 Nov 2026 (contract verified as `CLEAR`). Matches the pipeline row (CPOOL, Clearpool).

| 📊 Market (CoinGecko, 16 Nov 2026 6:51 AM MST) | 🔗 On-chain (Etherscan v2 API + RPC, 16 Nov 2026) |
|---|---|
| **Price** $0.02517 | **Supply** 1,000,000,000 (fixed; 6.37M sits at the dead address) |
| **24h / 7d / 30d / 1y** 🟢 +5.9% / 🔴 −0.4% / −14.7% / −53.2% | **Allocation Safes** all emptied into EOAs, 24–31 Jan 2022 |
| **Market cap** not reported · **FDV** $25.17M | **Reserve chain → exchanges, last 12 months** 123.3M (~$3.38M) |
| **24h volume** $1.31M (Upbit KRW $0.93M) | **Holders' revenue** $0 (DefiLlama) |
| **ATH** $2.55 (16 Nov 2021) · now −99.0% | **Largest holder** Upbit deposit `0x9f2a…` 214.7M (21.5%), exchange custody |
| **Pump days, last 365** 68 (CoinGecko closes) | **TVL** $14.06M (DefiLlama) |

---

## 💰 Revenue — Does it make money? · 2/10 · ❌ FAIL

| Metric | Value | Source |
|---|---:|---|
| Fees, 30d / 1y / all time | $30,324 / $1,003,157 / $1,493,712 | [Tier A] [DefiLlama Clearpool](https://defillama.com/protocol/clearpool) (16 Nov 2026) |
| Protocol revenue / holders' revenue | **$0 / $0** | same |
| Historical buybacks (50% of revenue) | $552,767 bought 7.65M CPOOL, Q3 2022 – Q3 2024; none listed since | [Tier A] [docs: Buybacks](https://docs.clearpool.finance/clearpool) |
| CLEAR plan | 50% of protocol revenue to buyback-and-burn; "details at a later date" | [Tier A] docs, tokenomics |

**What it means:** The origination fee goes to the treasury. Holders got about $0.55M of buybacks in two years, then nothing for two more. Score **2**, which **trips the Revenue gate**.

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** The origination fee goes to the treasury; buybacks stopped two years ago.

## 🏛️ Foundation & team — Who is in charge? · 4/10 · ❌ FAIL

| Item | Finding | Source |
|---|---|---|
| Operator | Clearpool team; governance by Snapshot (`clearpoolfinance.eth`) | [Tier A] [Snapshot vote](https://snapshot.org/#/s:clearpoolfinance.eth/proposal/0x392438d143ee5114724940cdc67a44ecf5098c066fc74d56ed860808512d9612) |
| Published wallets | Only the token and three investor vesting contracts. Team and treasury wallets are not published; docs say "multi-sig cold storage" | [Tier A] docs, tokenomics |
| What the chain shows | Every allocation Safe (team, reserve, rewards, partnerships and two more) sent its whole balance to a plain EOA on 24–31 Jan 2022 | [Tier A] chain, see Holdings |
| MiCAR white paper | Published (archive section of docs) | [Tier A] docs |

**What it means:** Real team, real partners, but the docs' custody claim is contradicted on-chain and nothing was disclosed. Score **4**.

## 🪙 Foundation / team holdings — How many coins do they hold? · 4/10 · ❌ FAIL

| Bucket (published) | Genesis wallet (type) | What happened | Now |
|---|---|---|---:|
| Team 15% | [`0x4550…3454`](https://etherscan.io/address/0x455011f2704c6e192b09d9cc1430299c70af3454) (Safe) got 150M ([tx](https://etherscan.io/tx/0x7db94956a59a8245d3a436c3842ca8028380887993d5c0b80a32760ad96ddb51)) | 149,999,990 to EOA [`0xc7f9…4389`](https://etherscan.io/address/0xc7f9bfb34f3f48e72252bf13cbd6abda70704389) on 28 Jan 2022 ([tx](https://etherscan.io/tx/0x11a5889c47d6b9508e0931e7a407b8279b35215e272e67c9425c5a00acb8da58)), then spread to many EOAs | Safe 16.94M · EOA 0 |
| Reserve 17.17% | [`0x55f6…69d7`](https://etherscan.io/address/0x55f638da67e1c911cb9d9b03b16128461b1769d7) (Safe) got 171.67M | → EOA `0x60b0` (Jan 2022) → `0xc0a5` → `0x9038` → exchanges | 0 at every hop |
| Rewards 20% | [`0x9129…ee8a`](https://etherscan.io/address/0x9129f9c97d29d4668fb6c440e2e7b9886f1eee8a) (Safe) got 199.26M | 191.19M to EOA [`0x97e4…20f0`](https://etherscan.io/address/0x97e4f18a84a7504e003c353eac6e913756e820f0) (Jan 2022) | 0 |
| Partnerships 10% | [`0x1e86…f15a`](https://etherscan.io/address/0x1e8642f1ff4da83dd5e6a8831189d4f8470ef15a) (Safe) got 100M | 92M to EOA [`0x1a48…4eb4`](https://etherscan.io/address/0x1a4812b71e1ccd651b8c8666b74181fd91954eb4) (Jan 2022) | 0 |
| Unmatched (≈13.4%) | [`0x2383…6b41`](https://etherscan.io/address/0x2383ee3d0ed91da61ac4b83594820df6c8ee6b41) (Safe) got 133.99M ([tx](https://etherscan.io/tx/0x342a0c7042a2343c3954c4d9d3f6ad00fd0643d1bdb0b1c7164d687da5313915)) | 137.11M to EOA [`0x6352…a675`](https://etherscan.io/address/0x6352c2a2c39e1998dc6481dac74922729e2ca675) on 31 Jan 2022 ([tx](https://etherscan.io/tx/0x08702cc684405e5f0b2d95a391dec447c3c434b32239fd9cae7cf747f2c97fd7)) | 0 |
| Unmatched (7.4%) | [`0x8662…865c`](https://etherscan.io/address/0x8662790291e1554608b3491b835baa8664ea865c) (Safe) got 74.08M | 73.83M to EOA [`0x5972…22a6`](https://etherscan.io/address/0x5972bda688fdfc6ed2e09b5f0e34fb04873b22a6) | 0 |
| Investors (vesting contracts #1–#3) | [`0x512a…`](https://etherscan.io/address/0x512a816d43aa3801d04b3f687895d62d9366c15b) · [`0x7029…`](https://etherscan.io/address/0x702997fd3448346d21cede91bf40beb804764ac5) · [`0x0466…`](https://etherscan.io/address/0x046667c768da32ef1e81a5cbbcd49103a207e72c) | Real contracts, as published | 6.57M left |

- Team Safe `0x4550` **withdrew 9.3M from "Bybit: Wallet 57" on 15 Nov 2026** ([tx](https://etherscan.io/tx/0xedcbd101bb4268c709c73f17db519482616f9ec39e1935c854b5702d94e05d0b)), the day before the migration, so team-side coins also sit on exchanges.
- **Correction:** the biggest holder [`0x9f2a…f7be`](https://etherscan.io/address/0x9f2a5909e771c57a2aa49c95f5982fc75a69f7be) is an **Upbit deposit address** ([Arkham](https://intel.arkm.com/explorer/address/0x9f2a5909e771c57a2aa49c95f5982fc75a69f7be)). It holds 214,703,489 CPOOL (21.5%; 220.7M before a 6M sweep on 16 Nov) and is refilled by **Upbit's hot wallet** [`0x76ff…99da`](https://etherscan.io/address/0x76ffd8d49468092786cedfb69e5153c802dd99da) ([Arkham](https://intel.arkm.com/explorer/address/0x76ffd8d49468092786cedfb69e5153c802dd99da)). This is exchange custody, not an insider.
- **Arkham ([Tier B] Arkham, read 16 Nov 2026 (signed-in account)) confirms the team side:** the genesis Safe [`0xe030…`](https://intel.arkm.com/explorer/address/0xe0308d5681afe01a8ad1cc0b8c937db699e204af) (tagged "CPOOL Team Wallet"), [`0x4550…`](https://intel.arkm.com/explorer/address/0x455011f2704c6e192b09d9cc1430299c70af3454), [`0x55f6…`](https://intel.arkm.com/explorer/address/0x55f638da67e1c911cb9d9b03b16128461b1769d7), [`0x9129…`](https://intel.arkm.com/explorer/address/0x9129f9c97d29d4668fb6c440e2e7b9886f1eee8a), [`0x1e86…`](https://intel.arkm.com/explorer/address/0x1e8642f1ff4da83dd5e6a8831189d4f8470ef15a), [`0x2383…`](https://intel.arkm.com/explorer/address/0x2383ee3d0ed91da61ac4b83594820df6c8ee6b41) and [`0x8662…`](https://intel.arkm.com/explorer/address/0x8662790291e1554608b3491b835baa8664ea865c) are all labelled Clearpool Finance Safes. The EOAs [`0xc7f9…`](https://intel.arkm.com/explorer/address/0xc7f9bfb34f3f48e72252bf13cbd6abda70704389) and [`0x97e4…`](https://intel.arkm.com/explorer/address/0x97e4f18a84a7504e003c353eac6e913756e820f0) are labelled Clearpool Finance. `0x60b0`, `0xc0a5`, `0x9038`, `0x6352` and `0x1a48` are unlabelled, though `0x6352` was first funded by the Clearpool deployer. Safe signers were not read [Unverified].

**What it means:** Insiders' identified wallets are now mostly empty, but that is because they were distributed and sold, not because they are locked. The migration hands the treasury 357M new CLEAR plus 71M for contributors. Score **4**.

## 📉 Selling behavior — Do insiders sell into pumps? · 0/10 · ❌ FAIL

Pump test uses KuCoin CPOOL-USDT daily closes (from 28 Oct 2021). Exchange labels are Etherscan name tags [Tier B]; transfers are Tier A. Dollar figures use the KuCoin close of each day.

| Day (UTC) | Route | CPOOL | 5-day change | Pump? |
|---|---|---:|---:|---|
| 10 May 2022 | `0x2383` Safe → EOA `0x6352` → KuCoin deposit ([tx](https://etherscan.io/tx/0x8fa7a3294fc809d3516538811baa88631314b550152763c23de106b7393df953)) | 14,999,000 | n/a | Exchange deposit |
| 11–19 Feb 2024 | Clearpool Deployer `0xdafb` (8M) and hub `0x6352` (2M) → KuCoin **deposit** [`0x4862…`](https://etherscan.io/address/0x48628c595b004c1a03ca616878fef010f752fefc) (Arkham label) → KuCoin 20 in 1–2M lots ([tx](https://etherscan.io/tx/0x8d0d603a00c6da9a25604ab32ec9d9d8f015f46591a5332548740cc8cd959990), [tx](https://etherscan.io/tx/0x36e079e03ef41ae9a133a08e868ca35b0948b5efdc40c3d7702f9bf37bd3bbed)) | 10,000,000 | +18.5% to +34.9% | 🔴 Yes (5 days) |
| 29 Feb & 27 Mar 2024 | Reserve EOA `0x60b0` (and hub `0x6352`) → **Hex Trust**-labelled custody wallet [`0x46cc…`](https://etherscan.io/address/0x46cc29b97e40945f6cd5f79bd1fd9b8a2253f07b) → Bybit deposit ([tx](https://etherscan.io/tx/0x0cbd4fd2ddbafee408c1ea670ed16d600b84c0492a4925b01f201bfe43520aa6), [tx](https://etherscan.io/tx/0x84ba2b9afe76225bbf73235ed00cffa23ba5953a11e4b50218fbe90f4cdc2c43)) | 10,665,000 | +24.4%, **+112.1%** | 🔴 Yes |
| 13, 25, 28 Mar 2024 | **Clearpool Finance: Deployer** [`0xdafb…`](https://etherscan.io/address/0xdafba3975d8d55e138763125c0841a494dc9f4c3) (Arkham label; funded by `0x60b0`) → Bybit deposit ([tx](https://etherscan.io/tx/0x58eebc024f7a44d16cc2cd27f1dcf906dc4e24d9478e244e255beff0701139fa), [tx](https://etherscan.io/tx/0x9342cb544b4c3a198a11d0d5cf898d28be0228f9272f68f5b6fda67fb2de0d42)) | 6,000,000 | +58.6%, +67.7%, +90.9% | 🔴 Yes |
| **26 Dec 2025** | Reserve `0x9038` → Bitget **deposit** [`0xf61e…`](https://etherscan.io/address/0xf61e622d977c1e572a0ea6c4b28b17fa6b9d65ec) (Arkham label), swept to Bitget 6 within 6 min ([tx](https://etherscan.io/tx/0x4189285ad53fdc101614a1501a6d9b42f461b7eedff188d9c686e34719c9d9db)) | 6,000,000 | **+29.4%** | 🔴 Yes |
| **29–30 Dec 2025** | `0x9038` → relay [`0x6358…`](https://etherscan.io/address/0x6358d84906bba6404518eee69c1aec769cf443cf) → Bitget **deposit** [`0x687c…`](https://etherscan.io/address/0x687cf2c5f938caae0bd95e222ed30ad0db5f7ced) (Arkham label) → Bitget 6 ([tx](https://etherscan.io/tx/0x839b0ad9b09bda27470e8fba5612afae91edbf554753aae52e7d805a90261345), [tx](https://etherscan.io/tx/0x54591897a1efb48403761632130b162a110b533667d118ccea303b7ff051cdc2)) | 12,000,000 | +10.0%, +13.7% | 🔴 Yes |
| Dec 2025 – Apr 2026 (other days) | `0x9038` → Bitget deposits directly or via a relay → Bitget 6, plus a Kraken deposit (12M via `0x6358` on 2 and 4 Jan 2026) and KuCoin 20 (e.g. 7,325,400 into Bitget deposit [`0x71ed…`](https://etherscan.io/address/0x71ed220d03a505d231540d5b26069dc6d7da8aa3) and swept in 6 min: [in](https://etherscan.io/tx/0x1bc0b48608336d26b61df067b3571c32910380e2e85baed87724d98cb06d7884), [out](https://etherscan.io/tx/0xf5780eddb54401db2311b600f59069e5bb8565e671fac6667808abc20a402870)) | 88,708,095 | <10% | Not pump days |
| **22 & 24 Sep 2026** | `0x9038` → Bybit deposit [`0xe95a…`](https://etherscan.io/address/0xe95a685e67dadb390b53900521723407314c088b) ([tx](https://etherscan.io/tx/0x5c188b69d5b8d0b30ca134ef4e28cfd9c8e3b6e45e750c076230e02f109e7269), [tx](https://etherscan.io/tx/0x2abcaa79f948cef99671084142c8237c207d86138cb3bda91d13e664828824ca)) | 16,620,986 | **+25.8%, +25.9%** | 🔴 Yes |
| May 2025 – Oct 2026 | Genesis Safe `0xe030` → weekly lots to [`0xdd65…`](https://etherscan.io/address/0xdd6521159a8ea416f7712a7a98222a196a497849) (51 transfers, 6.54M of its 7.60M inflow) → Bybit deposit; e.g. 1.256M on 13 May 2026 ([tx](https://etherscan.io/tx/0xd8b0901051e0ca18c85f4789b8d1c6c0518c462a10837288b4064bde4fc59893)) | 4,797,023 | 2.65M on pump days (+17.8% to +32.6%) | 🔴 Yes |

- Last 12 months, Reserve chain only: **123.3M CPOOL to exchanges (~$3.38M), 34.6M (~$1.17M) on pump days.**
- **Correction (Arkham, [Tier B] Arkham, read 16 Nov 2026 (signed-in account)):** several addresses first read as relays are **Bitget deposit addresses**: [`0xf61e…`](https://intel.arkm.com/explorer/address/0xf61e622d977c1e572a0ea6c4b28b17fa6b9d65ec), [`0x687c…`](https://intel.arkm.com/explorer/address/0x687cf2c5f938caae0bd95e222ed30ad0db5f7ced), [`0x71ed…`](https://intel.arkm.com/explorer/address/0x71ed220d03a505d231540d5b26069dc6d7da8aa3) and [`0x27ca…`](https://intel.arkm.com/explorer/address/0x27ca78b34b8f1b176674f411130f9859da8ed874). Their exact in-and-out is Bitget's own sweep, so in those cases `0x9038` deposited straight to Bitget. The genuine relays are unlabelled single-use wallets such as [`0x6358…`](https://intel.arkm.com/explorer/address/0x6358d84906bba6404518eee69c1aec769cf443cf) (to Bitget, and to Kraken deposit `0xe360…`) and [`0xe0d9…`](https://intel.arkm.com/explorer/address/0xe0d98119b82161e3a57957a5bae318a62e816fa3). [`0xe95a…`](https://intel.arkm.com/explorer/address/0xe95a685e67dadb390b53900521723407314c088b) is confirmed a Bybit deposit. The 12-month totals are unchanged: the deposit addresses were already counted as exchange endpoints.
- **Hex Trust wallet:** Arkham labels [`0x46cc…`](https://intel.arkm.com/explorer/address/0x46cc29b97e40945f6cd5f79bd1fd9b8a2253f07b) **Hex Trust** (a custodian). On Etherscan it pooled CPOOL from Clearpool's hub `0x6352` (36M from Nov 2023), the Reserve EOA `0x60b0` (13.5M in 2024) and other senders, then sent it to Bybit and other addresses. So the 2024 pump-day deposits through it were custodian-executed for a client Arkham does not name [Unverified]. They still originate mostly from Clearpool wallets.
- **Correction:** Arkham labels [`0x4862`](https://intel.arkm.com/explorer/address/0x48628c595b004c1a03ca616878fef010f752fefc) a **KuCoin deposit address**, not a market-maker account. Its 57.25M of sends to KuCoin hot wallets (2021–2025) are KuCoin's sweeps. Of the deposits into it, **43.0M came from Clearpool wallets**: the deployer `0xdafb` (28.4M), the genesis Safe (8.5M) and `0x6352` (6.1M). So those wallets deposited to KuCoin directly. The earlier "34.2M on 36 pump days" counted every sweep, including other senders' deposits, so it is withdrawn.

**What it means:** Treasury-origin coins hit exchanges on pump days in 2022, 2024, 2025 and 2026, through fresh wallets, with no disclosure. Score **2**, which **trips the Selling gate**.

- **Disclosure quality (16 Nov 2026 rules): silence.** No disclosure of these exchange sends was found. **Penalty applied (16 Nov 2026 rules):** a proven pump-day sale with no disclosure fails Selling (ordinary score at most 3) and then loses 2 points, floored at 0: **2 → 0**. Pump days from KuCoin CPOOL-USDT daily closes.

- **One-hop amendment (16 Nov 2026):** Still a **proven sale** under the amended rule. (c) holds: Clearpool has published no reason for reserve coins reaching exchanges; the Hex Trust custody link comes from an Arkham label, not a Clearpool statement. Silence stands, so the penalty above is unchanged.

## 📊 Tokenomics & supply · 3/10 · ❌ FAIL

- CPOOL: 1B fixed, all vesting schedules from 28 Oct 2021 now complete (Reserve ran 60 months, to Oct 2026).
- CLEAR (from 17 Nov 2026): 1,428,571,429 total = existing holders 70% + Treasury & Partnerships 15% + Ecosystem 10% (each 35% at migration, the rest over 36 months) + Contributors 5% (12-month cliff, 24 months linear). **Circulating jumps to 1.125B on day one (+12.5%)**, then to 1.43B by month 36 (+42.9%), then **1–4% new supply a year with no maximum** ([docs](https://docs.clearpool.finance/clearpool/token/cpool/tokenomics.md), Tier A).

## 💧 Liquidity & market · 3/10 · ❌ FAIL

- $1.31M 24h volume: Upbit KRW $932k, Bybit $278k, BitDelta $262k, Bithumb $142k, Bitget $128k, KuCoin $104k, Kraken $81k (CoinGecko tickers).
- −99.0% from ATH, −53% over a year. Exchanges must handle the migration ("support details coming soon").

## 🧑‍💻 Product & development · 6/10 · ✅ PASS

- Live: Prime (KYC'd institutional pools), Credit Vaults, Dynamic (permissionless) pools on Ethereum, Polygon, Polygon zkEVM, Optimism and Mantle; USDX T-Pool ([docs](https://docs.clearpool.finance/clearpool)).
- GitHub `clearpool-finance` repos pushed Aug–Sep 2026 (`yield-server` 7 Sep, `CPOOL` 11 Aug).

## 🤝 Adoption & customers · 4/10 · ❌ FAIL

- "Nearly $1B in total origination since 2021" and a borrower list of trading firms (docs, self-reported). DefiLlama TVL is only $14.06M and fees ~$1.0M a year.

## 🛡️ Security & audits · 6/10 · ✅ PASS

- Audit reports published for the CLEAR token, USDX T-Pool, Credit Vaults, Prime, Term Pools and Dynamic pools (docs, "Contracts & Audits"); bug bounty paid in CPOOL or USDC, minimum $500.
- No exploit found. Borrower default risk is real by design (unsecured Prime loans; auction plus insurance fund).

## ⚖️ Regulatory · 6/10 · ✅ PASS

- MiCAR white paper published; Prime is KYC/KYB via SecuritizeID; partnership with Hex Trust for custody (docs). No enforcement action found.

## 📅 Catalysts & calendar · 4/10 · ❌ FAIL

| Date | Event |
|---|---|
| **17 Nov 2026** | CPOOL → CLEAR migration opens (1:1); 125M new CLEAR circulating |
| 17 Feb 2027 | Migration deadline |
| 2027 → 2029 | Treasury and ecosystem CLEAR unlock linearly over 36 months; contributor cliff after 12 months |
| TBD | Credit Vaults anchored by the institutional credit fund announced with Ripple and Cicada Partners on 20 Aug 2026; XRP Ledger expansion (approved 2 Oct 2026) |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Treasury → exchange during a pump | 🔴 **Yes:** Reserve chain → Bitget/Bybit on 26/29/30 Dec 2025 and 22/24 Sep 2026. [Sep tx](https://etherscan.io/tx/0x5c188b69d5b8d0b30ca134ef4e28cfd9c8e3b6e45e750c076230e02f109e7269) |
| Unenforced lock-ups | 🔴 **Yes:** all allocation Safes emptied to EOAs in Jan 2022, against the "cold storage" wording |
| Live mint path | 🟡 CLEAR: 1–4% a year, no max supply |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| Reserve Safe `0x55f6…` → EOA `0x9038…` | Clearpool Reserve allocation (17.17%) | Published allocation + Etherscan | high | yes (on-chain) | Selling: 123.3M CPOOL to Bitget, Bybit, Kraken and KuCoin, including pump days |

## 📚 Sources

- [Tier A] Methodology update 16 Nov 2026: no new Arkham lookups; the attribution table uses evidence already cited in this report.
- [Tier A] Etherscan v2 API: `tokentx` for the genesis Safe and ~200 traced wallets (two BFS passes, depth 3 and 2), `getsourcecode` (all genesis wallets are `GnosisSafeProxy`), `eth_getCode` and `balanceOf` via public RPC; Etherscan token-holders page; read 16 Nov 2026 MST
- [Tier B] Etherscan name tags: "Bitget 6", "KuCoin 20", "KuCoin Deposit", "ByBit Deposit", "Bybit: Wallet 57", "Gate Deposit", "Uniswap V3: CPOOL-USDC"
- [Tier A] [docs.clearpool.finance](https://docs.clearpool.finance/clearpool) (tokenomics, CPOOL → CLEAR migration, buybacks, contracts & audits, roadmap) · [Snapshot vote](https://snapshot.org/#/s:clearpoolfinance.eth/proposal/0x392438d143ee5114724940cdc67a44ecf5098c066fc74d56ed860808512d9612) · [GitHub](https://github.com/clearpool-finance)
- [Tier A] DefiLlama fees/revenue/TVL; CoinGecko `clearpool` (16 Nov 2026 6:51 AM MST); KuCoin CPOOL-USDT daily candles for every pump test
- [Tier B] Arkham, read 16 Nov 2026 (signed-in account): Clearpool Finance labels on the genesis and bucket Safes, `0xc7f9`, `0x97e4` and the deployer `0xdafb`; Hex Trust on `0x46cc`; Bitget, Bybit, KuCoin and Upbit deposit labels; Upbit hot wallet `0x76ff` (links in Holdings and Selling). Dates come from Etherscan, not Arkham's relative ages
- [Unverified] owners of `0x9038`, `0x6352` and the client behind the Hex Trust wallet `0x46cc`; the Safe signers; whether any relay is a disclosed market maker; which Safe maps to Ecosystem 10.15% and Liquidity 15%

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Reserve 171.67M to Safe 0x55f6, then to EOA 0x60b0 | [in](https://etherscan.io/tx/0xb330768122433b98e6d7af12e92ce403a461e521fc8811724a981da8e403f08f) · [out](https://etherscan.io/tx/0xcb9864908480c91c47bc40da0f8288c1b36c22bd5f8e7b950daaadf988a54729) | A | 16 Nov 2026 |
| 0x60b0 → 0xc0a5 → 0x9038 (154.77M) | [6 Jun 2024](https://etherscan.io/tx/0xfbaac84ca2ebdc30fc50f62f359c0b5ce4051ab333e0f81316e4693f8190d328) · [20 Mar 2025](https://etherscan.io/tx/0x041c0eb8c1dbaafcb814ecbed1eac738886264aff260af052c4ae87404c49bbd) | A | 16 Nov 2026 |
| 0x9038 pump-day exchange deposits | [26 Dec](https://etherscan.io/tx/0x4189285ad53fdc101614a1501a6d9b42f461b7eedff188d9c686e34719c9d9db) · [29 Dec](https://etherscan.io/tx/0x839b0ad9b09bda27470e8fba5612afae91edbf554753aae52e7d805a90261345) · [22 Sep](https://etherscan.io/tx/0x5c188b69d5b8d0b30ca134ef4e28cfd9c8e3b6e45e750c076230e02f109e7269) · [24 Sep](https://etherscan.io/tx/0x2abcaa79f948cef99671084142c8237c207d86138cb3bda91d13e664828824ca) | A + B tag | 16 Nov 2026 |
| Team Safe 150M in, 149,999,990 out to EOA | [in](https://etherscan.io/tx/0x7db94956a59a8245d3a436c3842ca8028380887993d5c0b80a32760ad96ddb51) · [out](https://etherscan.io/tx/0x11a5889c47d6b9508e0931e7a407b8279b35215e272e67c9425c5a00acb8da58) | A | 16 Nov 2026 |
| 2024 Reserve-funded pump-day deposits | [0x60b0→0x46cc](https://etherscan.io/tx/0x2c062ccb09a2ab5bf5f935febe6566cb62ca0cf8baf1f1db1ae6e14510f75f1a) · [+112%](https://etherscan.io/tx/0x84ba2b9afe76225bbf73235ed00cffa23ba5953a11e4b50218fbe90f4cdc2c43) · [+90.9%](https://etherscan.io/tx/0x9342cb544b4c3a198a11d0d5cf898d28be0228f9272f68f5b6fda67fb2de0d42) | A + B tag | 16 Nov 2026 |
| Allocation and "multi-sig cold storage" wording; CLEAR supply | [docs tokenomics](https://docs.clearpool.finance/clearpool/token/cpool/tokenomics.md) | A | 16 Nov 2026 |
| Fees ~$1.0M/yr; revenue $0 | [DefiLlama](https://defillama.com/protocol/clearpool) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Who controls `0x9038` / `0x60b0`, and whose account is the Hex Trust wallet `0x46cc`?** | Arkham (16 Nov 2026) leaves them unlabelled / custodian-only. Ask Clearpool and Hex Trust | Free |
| 2 | **Ask Clearpool** | Ask why the "cold storage" Safes were emptied into EOAs in Jan 2022, and whether 0x9038 is a disclosed market maker or OTC buyer | Free |
| 3 | **Map the last two buckets** | Match Ecosystem 10.15% and Liquidity 15% to `0x2383`/`0x8662`/`0x1bb8` | Free (chain) |
| 4 | **Migration** | After 17 Nov, read CLEAR treasury and contributor wallets and watch them for exchange deposits | Free |
| 5 | **Safe signers** | Read `getOwners()` on the Clearpool Safes and match the signers [Unverified] | Free (chain) |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
