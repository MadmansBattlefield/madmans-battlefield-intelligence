---
ticker: W
name: Wormhole
chain: solana + ethereum (NTT multichain)
contract: "0xb0ffa8000886e57f86dd5264b9582b2ad87b2b91 (ERC-20 W on Ethereum, Base, Arbitrum); Solana SPL 85VBFQZC9TZkfaptBWjvUw7YbZjy52A6mjtPGjstQAmQ"
overall_score: 3.9
overall_verdict: FAIL
section_scores:
  revenue: 2
  foundation_team: 5
  insider_holdings: 3
  selling_behavior: 4
  tokenomics_supply: 3
  liquidity_market: 4
  product_development: 7
  adoption_customers: 5
  security_audits: 4
  regulatory: 6
  catalysts: 4
gates_failed: [revenue]
red_lines:
  one_hop_sale_status: none_found
  hack_exploit: "yes (historic): Feb 2022 Solana bridge exploit, 120,000 wETH (~$320M), losses replaced by a backer"
  treasury_to_exchange_during_pump: "yes: wallets paid out of the Hedgey lockup contract sent 25.3M W (~$2.06M) to Binance and OKX on 10 pump days"
  treasury_funded_wallet_to_exchange_during_pump: "yes: e.g. distributor 0x712e → 0xcef7 → Binance deposit, 5.80M W on 21 Sep 2026 (+29.1%)"
  unenforced_lockups: "partly: Core Contributor tokens now unlock to the Foundation bi-weekly and are held 'in escrow' under off-chain contracts only"
  mint_path_live: "no new supply (10B cap); NTT mints on Ethereum mirror burns/locks on Solana"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "No revenue reaches holders; the yield is new tokens."
pump_day_price_source: "KuCoin W-USDT daily closes"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions: []
price_usd: 0.008656
price_source: "CoinGecko, 16 Nov 2026 6:51 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### W · Overall grade **3.9 / 10 · ❌ FAIL**

**Summary:** Wormhole is a large, live cross-chain messaging network (Guardians, Portal, NTT, Settlement, Queries; 40+ chains). The W token is in bad shape: −99.5% from its April 2024 high, −84% over a year, $58.9M market cap against $86.6M FDV, and holders receive **$0** of protocol revenue (DefiLlama shows Portal fees of ~$319k a year and $0 revenue). The "W 2.0" plan (Sep 2025) promises a Wormhole Reserve and a 4% target yield, but the yield is paid from existing supply. On Ethereum, two unlabelled wallets bridged 812M W in and built the Hedgey lockups; wallets paid from those lockups have sent **119.8M W (~$6.23M)** to exchanges and a market maker, **25.3M (~$2.06M) of it on pump days**. Both gates fail.

**🚨 Top warning (red line):** NTT mint recipients [`0x4672…0803`](https://etherscan.io/address/0x4672fd919b11d18e442faf4b205d5df6e0970803) (508.8M minted, Jul–Aug 2024, e.g. [mint](https://etherscan.io/tx/0x3ae3f0b64689b29518f0fee5eadd3f45a3be6214f6d78040fedc26bfab4aba82)) and [`0x0d59…4593`](https://etherscan.io/address/0x0d59e76e009dd6e83b9b5a751478a3a9c8654593) (303.2M, Sep 2025–Apr 2026, e.g. [mint](https://etherscan.io/tx/0xad04b2158be3f34bf999c7331d6771263be5c33586df8c8cedb14679e5e53f61)) passed almost everything into the Hedgey Batch Planner ([337.5M](https://etherscan.io/tx/0x592d1a4fca2b7290e61bb92965cb8dc83c424ff2cba367f0efcd7af0a214fd22), [130.65M](https://etherscan.io/tx/0xa64a60f411e9ac5bdb3e854b5cb687dce0c7f7474e2ca76056e45dabc40b6d3f)), which funded the lockup contract [`0x73cd…ec3d`](https://etherscan.io/address/0x73cd8626b3cd47b009e68380720cfe6679a3ec3d) (still holds 245.0M W). Beneficiaries claim out of it and forward to exchanges. Example: lockup → [`0xb016…`](https://etherscan.io/address/0xb01665c07c58086603eacb1e7c488fb99bad0c28) (22.5M, [tx](https://etherscan.io/tx/0x4b1105508d7d3b7e98c7c49dc977704eca3f07768911249c0fdf8ec51d54b23b)) → distributor [`0x712e…4462`](https://etherscan.io/address/0x712e7991800bc4d88ee6e164361af077ec844462) ([tx](https://etherscan.io/tx/0x0036569d2e6bf08dea5c04dfaf0ce27277b3bfac4961e14293228cdfd4cdd7bf)), which pays [`0xcef7…38e5`](https://etherscan.io/address/0xcef78991df18b131eed7bbf91c3c7da2e78338e5) mid-month ([14 Sep 2026](https://etherscan.io/tx/0x29ac5bfe7376e88b79ff3af55671c8391a7194f1e90d4c774c9b30b7678e6120)); **0xcef7 sent 5,804,270 W to a Binance deposit on 21 Sep 2026, a +29.1% day** ([tx](https://etherscan.io/tx/0x0859566dd69423820f524de310ed231e79203cfe0d511dbd41a6de65c1fb104b)). In May 2025 the lockup → 0xb016 → [`0xb660…`](https://etherscan.io/address/0xb660c71b23d0baef6878e014008644e7c8ee9c18) → [`0x2331…`](https://etherscan.io/address/0x2331f0549d687411c94c6c75ebd5a69a15e98186) chain put **7.5M on OKX on a +21.3% day**, the same morning it arrived ([in](https://etherscan.io/tx/0x142e82884fd62b1249b704c5a9046e9f873e76c54f921bf66fc4a4744826fb74), [out](https://etherscan.io/tx/0x4b1fe85a0f5503aea09b17f616e53ed07bdd0dcf780634e8ed7982274c7a78a8)). **Second warning:** 3.2B W (32% of supply) is still locked and now releases bi-weekly until ~2030; circulating supply rose from ~4.76B (Sep 2025, official) to 6.80B today, a pace of ~1.75B a year (~$15M at today's price, about a quarter of the market cap). Every transfer is in the 🔗 Evidence trail below.

**Sections passed: 2 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 2/10 | ❌ FAIL |
| 🏛️ Foundation & team | 5/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 3/10 | ❌ FAIL |
| 📉 Selling behavior | 4/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 3/10 | ❌ FAIL |
| 💧 Liquidity & market | 4/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 7/10 | ✅ PASS |
| 🤝 Adoption & customers | 5/10 | ❌ FAIL |
| 🛡️ Security & audits | 4/10 | ❌ FAIL |
| ⚖️ Regulatory | 6/10 | ✅ PASS |
| 📅 Catalysts & calendar | 4/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 W · Wormhole · 3.9 / 10 · ❌ FAIL

> **One line:** Real cross-chain plumbing with no cash flow to the token, and lockup money that keeps reaching Binance on pump days.

**Identity:** W = Wormhole, wormhole.com. CoinGecko `wormhole`, symbol W; native SPL on Solana (`85VBFQ…QAmQ`) and NTT ERC-20 [`0xb0ff…2b91`](https://etherscan.io/token/0xb0ffa8000886e57f86dd5264b9582b2ad87b2b91) on Ethereum, Base and Arbitrum (same address; listed by CoinGecko and in the official [W 2.0 post](https://wormhole.com/blog/wormhole-announces-w-token-2-0-upgrade) as "native ERC-20 and Solana SPL using NTT"). Matches the pipeline row (W, Wormhole).

| 📊 Market (CoinGecko, 16 Nov 2026 6:51 AM MST) | 🔗 On-chain (Etherscan v2 API, 16 Nov 2026) |
|---|---|
| **Price** $0.008656 | **Max supply** 10,000,000,000 · **circulating** 6,801,048,499 |
| **24h / 7d / 30d / 1y** 🔴 −2.3% / −20.4% / −40.2% / −84.0% | **Hedgey lockup `0x73cd`** 245.0M W left |
| **Market cap** $58.87M · **FDV** $86.56M | **Lockup-paid wallets → exchanges / market maker** 119.8M (~$6.23M) |
| **24h volume** $10.26M | **Holders' revenue** $0 (DefiLlama) |
| **ATH** $1.66 (3 Apr 2024) · now −99.5% | **Largest ETH holders** Hedgey lockup 245.0M · Binance: Cold Wallet 20 224.5M |
| **Pump days, last 365** 40 (KuCoin closes) | **Not traced** Solana side (free RPCs refuse largest-account queries) |

---

## 💰 Revenue — Does it make money? · 2/10 · ❌ FAIL

| Metric | Value | Source |
|---|---:|---|
| Portal fees, 30d / 1y / all time | $15,395 / $319,037 / $1,005,239 | [Tier A] [DefiLlama Portal](https://defillama.com/protocol/portal) (16 Nov 2026) |
| Protocol revenue / holders' revenue | **$0 / $0** | same |
| W 2.0 plan | "onchain and offchain protocol revenues" to flow into a Wormhole Reserve, "coming soon"; staking yield "from a combination of the existing token supply and protocol revenues"; rewards "are emissions, not interest" | [Tier A] [W 2.0 post](https://wormhole.com/blog/wormhole-announces-w-token-2-0-upgrade) (17 Sep 2025) |

**What it means:** Fourteen months after W 2.0 was announced, no revenue reaches holders on DefiLlama. The "yield" is new tokens from supply. Score **2**, which **trips the Revenue gate**.

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** No revenue reaches holders; the yield is new tokens.

## 🏛️ Foundation & team — Who is in charge? · 5/10 · ❌ FAIL

| Item | Finding | Source |
|---|---|---|
| Operator | Wormhole Foundation administers the treasury, ecosystem and escrowed contributor buckets; core development by contributor companies | [Tier A] W 2.0 post |
| Governance | W staking-based governance (MultiGov) | [Tier A] W 2.0 post |
| Published wallets | No Foundation or bucket wallets published for Ethereum; the NTT mint recipients and lockup creators are unlabelled on Etherscan | [Tier A] chain |

**What it means:** A well-known team and Foundation, but the on-chain allocation is not mapped publicly. Score **5**.

## 🪙 Foundation / team holdings — How many coins do they hold? · 3/10 · ❌ FAIL

| Wallet | Role (what the chain shows) | Flow | Now |
|---|---|---|---:|
| [`0x4672…0803`](https://etherscan.io/address/0x4672fd919b11d18e442faf4b205d5df6e0970803) | NTT mint recipient, Jul–Aug 2024 | 508.8M minted; 483.0M to Hedgey Batch Planner ([112.5M](https://etherscan.io/tx/0x369b1013cccbcb36cf93f6203a2426e7b30ff9d97a15e3f3b61fd85fdf810241), [337.5M](https://etherscan.io/tx/0x592d1a4fca2b7290e61bb92965cb8dc83c424ff2cba367f0efcd7af0a214fd22)) | 0 |
| [`0x0d59…4593`](https://etherscan.io/address/0x0d59e76e009dd6e83b9b5a751478a3a9c8654593) | NTT mint recipient, Sep 2025–Apr 2026 | 303.2M minted + 34.4M in; 335.4M to Hedgey Batch Planner ([e.g.](https://etherscan.io/tx/0xa64a60f411e9ac5bdb3e854b5cb687dce0c7f7474e2ca76056e45dabc40b6d3f)) | ~1.75M |
| [`0x3466…c646`](https://etherscan.io/address/0x3466eb008edd8d5052446293d1a7d212cb65c646) | Hedgey Finance: Batch Planner (Etherscan tag) | 887.1M straight into the lockup contract | 0 |
| [`0x73cd…ec3d`](https://etherscan.io/address/0x73cd8626b3cd47b009e68380720cfe6679a3ec3d) | Hedgey Finance: Voting Token Lockups (Etherscan tag) | 923.3M in, 678.3M claimed out to 165 recipient addresses (lots of 7.5M, 22.5M, 30M) | **245.0M** |
| [`0x712e…4462`](https://etherscan.io/address/0x712e7991800bc4d88ee6e164361af077ec844462) | Beneficiary and payroll-style distributor | 102.3M in (23.8M direct from lockup, rest from other beneficiaries); 82.3M out to 15 wallets | 19.98M |

- **Arkham ([Tier B] Arkham, read 16 Nov 2026 (signed-in account)):** [Hedgey VotingTokenLockupPlans](https://intel.arkm.com/explorer/address/0x73cd8626b3cd47b009e68380720cfe6679a3ec3d) holds **245.026M W**, but Arkham does not list the lockup beneficiaries (individual NFT plans) [Unverified]. The mint wallets [`0x4672…`](https://intel.arkm.com/explorer/address/0x4672fd919b11d18e442faf4b205d5df6e0970803), [`0x0d59…`](https://intel.arkm.com/explorer/address/0x0d59e76e009dd6e83b9b5a751478a3a9c8654593) and [`0x55a3…`](https://intel.arkm.com/explorer/address/0x55a3d7d63fefa5e480829bb9a0af6a6e19c7d5b0) are unlabelled. On Solana, Arkham labels the W mint [`85VB…AQmQ`](https://intel.arkm.com/explorer/address/85VBFQZC9TZkfaptBWjvUw7YbZjy52A6mjtPGjstQAmQ) "Wormhole Token (W)", but it shows no top holders or Foundation unlock wallets [Unverified].
- The bucket behind the lockups is not stated anywhere public [Unverified]; the 7.5M/22.5M lot sizes look like investor or contributor tranches.
- The official post says Core Contributor tokens "unlock to the WF on a bi-weekly basis to essentially be held in escrow", with the annual schedule enforced only by "legal agreements". That lock is off-chain.

**What it means:** Over 800M W sits in, or has flowed through, lockups whose owners are not disclosed, and a large share of claims ends on exchanges. Score **3**.

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL

Pump test uses KuCoin W-USDT daily closes (from 3 Apr 2024). Exchange labels are Etherscan name tags [Tier B]; transfers are Tier A. Dollar figures use the KuCoin close of each day. BFS from the lockup contract, depth 3, ≥1M W edges (75 wallets).

| Day (UTC) | Route | W | 5-day change | Pump? |
|---|---|---:|---:|---|
| 22 Apr 2025 | lockup → [`0x55a3…`](https://etherscan.io/address/0x55a3d7d63fefa5e480829bb9a0af6a6e19c7d5b0) → [`0xf52f…`](https://etherscan.io/address/0xf52f5a27698d547d76bf37c266f90a129addb768) → Binance deposit ([tx](https://etherscan.io/tx/0xde1c98f83e71634b858ce44f00f007803a25de1367593d4fff649e009934b678)) | 3,225,009 | +21.1% | 🔴 Yes |
| 12 May 2025 | lockup → [`0x5604…`](https://etherscan.io/address/0x5604cdde0626872514b48a336848fc724fd60810) ([fund](https://etherscan.io/tx/0x1ca67564102d2839bdfb32683d080c4d916befea6297019f782c8f921926e74f)) → Binance deposit ([tx](https://etherscan.io/tx/0x5cc66dffa8107009843cd1647c8d3fd2d89e036d4c0676f2526571965dcbb3e9)) | 1,699,901 | +32.2% | 🔴 Yes |
| **13 May 2025** | lockup → `0xb016` → `0xb660` ([tx](https://etherscan.io/tx/0xa1e32a33f49a10a5b547bc76e6bf769961313fd30eee76621118ef3a47dd0428)) → `0x2331` → OKX 154 ([in](https://etherscan.io/tx/0x142e82884fd62b1249b704c5a9046e9f873e76c54f921bf66fc4a4744826fb74), [out](https://etherscan.io/tx/0x4b1fe85a0f5503aea09b17f616e53ed07bdd0dcf780634e8ed7982274c7a78a8)) | 7,500,000 | **+21.3%** | 🔴 Yes |
| **18 Sep 2025** | lockup-funded [`0xdd83…`](https://etherscan.io/address/0xdd831352762e9de7ad5a264990e1bb9f87a6fc21) → [`0xb8c6…`](https://etherscan.io/address/0xb8c6e43f37e04a2411562a13c1c48b3ad5975cf4) (both labelled **Inotel**, an infrastructure operator, by Arkham) ([fund](https://etherscan.io/tx/0x47579386cf57da5fe8ea4d78f46de2b02704ed58b0ada037aa23efe34f05264e)) → Binance deposit same day ([tx](https://etherscan.io/tx/0x659ba7f4d4461c467967f0f37ee9b06c47518ad0ad7c6dc5e7a972d376b99b48)) | 5,499,990 | **+28.6%** | 🔴 Yes |
| 10 Sep 2025 – 18 Sep 2026 (4 days) | lockup beneficiaries → [`0xb926…`](https://etherscan.io/address/0xb926e25e08fb3f06eafccd8a7c1f389238313ea4) → Binance 14 ([e.g.](https://etherscan.io/tx/0x26b2d56e7dc5485d47971a0b1dd799d90a78ca0274f22b7feca15e730ff8db20)) | 832,915 | +10.7% to +20.9% | 🔴 Yes |
| 15 & 22 Jun 2026 | `0x5604` and [`0xac8c…`](https://etherscan.io/address/0xac8c3ebe1929ec8850bc754af1cb298535b2436b) → Binance deposits ([tx](https://etherscan.io/tx/0x092fabb8f8753342a47a99e7629062493c61c25781be7285d0bdca8d744c7cc7), [tx](https://etherscan.io/tx/0x89f4752a8d19518b9a56acd6eccb2127b8427c20324474d106bda8de9a5a69ca)) | 771,389 | +16.7%, +17.7% | 🔴 Yes |
| **21 Sep 2026** | lockup → `0xb016` → distributor `0x712e` → `0xcef7` → Binance deposit ([tx](https://etherscan.io/tx/0x0859566dd69423820f524de310ed231e79203cfe0d511dbd41a6de65c1fb104b)) | 5,804,270 | **+29.1%** | 🔴 Yes |
| Aug 2024 – Nov 2026 (other days) | 13 lockup-paid wallets → 9 Binance deposits, Binance 14, Wintermute (7.5M, 3 Apr 2025, [tx](https://etherscan.io/tx/0x3bdf12d11c15e4a225bb24a1ddc3697f0920175ac70d700845198f6472917ccd)) and an Abyss Finance depositor (6.8M, from the lockup contract itself) | 94,430,328 | <10% | Not pump days |

- All time: **119.8M W (~$6.23M) from lockup-paid wallets to exchanges, a market maker and a staking depositor; 105.4M of it to Binance and OKX. 25.3M (~$2.06M) landed on 10 pump days.**
- Last 12 months: 60.7M (~$0.79M at much lower prices), 7.0M on pump days (0xcef7, 0xb926, 0x5604 and 0xac8c).
- **Arkham ([Tier B] Arkham, read 16 Nov 2026 (signed-in account)):** several sellers are identifiable third parties, not the Foundation. [`0xdd83…`](https://intel.arkm.com/explorer/address/0xdd831352762e9de7ad5a264990e1bb9f87a6fc21) and [`0xb8c6…`](https://intel.arkm.com/explorer/address/0xb8c6e43f37e04a2411562a13c1c48b3ad5975cf4) are **Inotel**, a blockchain-infrastructure operator and lockup beneficiary. [`0x57cd…`](https://intel.arkm.com/explorer/address/0x57cd900b4d0e8cba660056bffbe7f560410e4bbb) is a **Wintermute deposit**, so the 7.5M from the lockup contract went to a market maker. Arkham shows a Wintermute label beside [`0xf52f…`](https://intel.arkm.com/explorer/address/0xf52f5a27698d547d76bf37c266f90a129addb768)'s 3.225M Binance deposit, so that deposit may belong to Wintermute [Unverified]. [`0x5604…`](https://intel.arkm.com/explorer/address/0x5604cdde0626872514b48a336848fc724fd60810) was first funded by Chorus One (a staking provider). [`0x2331…`](https://intel.arkm.com/explorer/address/0x2331f0549d687411c94c6c75ebd5a69a15e98186) is an OKX deposit and [`0xb926…`](https://intel.arkm.com/explorer/address/0xb926e25e08fb3f06eafccd8a7c1f389238313ea4) a Binance deposit. Distributor [`0x712e…`](https://intel.arkm.com/explorer/address/0x712e7991800bc4d88ee6e164361af077ec844462) and [`0xcef7…`](https://intel.arkm.com/explorer/address/0xcef78991df18b131eed7bbf91c3c7da2e78338e5) are unlabelled; `0x712e…` also pays Figment (a staking provider) and a Safe. [`0xb016…`](https://intel.arkm.com/explorer/address/0xb01665c07c58086603eacb1e7c488fb99bad0c28) is a verified **VotingVault contract**, not a person's wallet. Pump-day dates come from Etherscan, not Arkham's relative ages.
- `0xcef7` deposits are followed within minutes by zero-value transfers from look-alike `0xead7…49e2` addresses (address-poisoning spam), so the real deposit address is `0xead7ff…49e2` [Tier A, chain].

**What it means:** The sellers are lockup beneficiaries, not proven Foundation wallets, and Arkham now names some of them: an infrastructure operator (Inotel) and a market maker (Wintermute). and part of it may be contractual vesting for investors or contributors. But money paid out of the official-looking lockups keeps reaching Binance on pump days, with nothing disclosed. Score **3** (unchanged; the 21 Sep 2026 sale runs through the unlabelled distributor `0x712e`), which **trips the Selling gate**.

- **Re-scored under the 16 Nov 2026 attribution rule: 3 → 4.** The pump-day sellers are lockup beneficiaries (Arkham names an infrastructure operator and a market maker), not proven Foundation or team wallets, and an unproven attribution cannot move Selling. Selling is therefore "not proven", which scores 4, and the Selling hard gate no longer trips. Revenue still trips its gate.
- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from KuCoin W-USDT daily closes.

## 📊 Tokenomics & supply · 3/10 · ❌ FAIL

- 10B cap. Allocation (official): Guardian Nodes 5.1%, Community & Launch 17%, Ecosystem & Incubation 31%, Strategic Network Participants 11.6%, Foundation Treasury 23.3%, Core Contributors 12%.
- From 3 Oct 2025 the first four buckets unlock **bi-weekly over 4.5 years**; Foundation Treasury keeps its daily 4-year schedule; contributor tokens unlock bi-weekly to the Foundation "in escrow" ([W 2.0 post](https://wormhole.com/blog/wormhole-announces-w-token-2-0-upgrade), Tier A).
- Circulating: ~4.76B (official, Sep 2025) → 6.80B (CoinGecko, today). **3.2B still to unlock**, ~1.75B a year at the recent pace.

## 💧 Liquidity & market · 4/10 · ❌ FAIL

- $10.26M 24h volume on a $58.87M market cap (17% turnover); listed on Binance, OKX, KuCoin and others (CoinGecko tickers).
- −99.5% from ATH, −84% over a year, −40% in 30 days.

## 🧑‍💻 Product & development · 7/10 · ✅ PASS

- Live: Guardian-signed messaging, Portal bridge, NTT (used by W itself and many issuers), Settlement, Queries; 40+ chains (W 2.0 post).
- Open-source code under the `wormhole-foundation` GitHub organisation [activity not re-checked this pass].

## 🤝 Adoption & customers · 5/10 · ❌ FAIL

- NTT is widely used by token issuers, and Wormhole is among the main bridges. But Portal's measured fees are only ~$319k a year (DefiLlama), so usage does not convert into value for the token.

## 🛡️ Security & audits · 4/10 · ❌ FAIL

- **Feb 2022 exploit:** a signature-verification flaw in the Solana contract let an attacker mint 120,000 unbacked wETH (~$320M). Losses were replaced so the bridge stayed backed ([official incident report](https://wormholecrypto.medium.com/wormhole-incident-report-02-02-22-ad9b8f21eec6), Tier A; [CertiK analysis](https://www.certik.com/blog/wormhole-bridge-exploit-incident-analysis), Tier B).
- Since then: a 19-Guardian multisig and many published audits plus a large bug bounty [Tier B, project materials]. No new exploit found.

## ⚖️ Regulatory · 6/10 · ✅ PASS

- No enforcement action against Wormhole or W found. The W 2.0 post disclaims staking rewards as "emissions, not interest".

## 📅 Catalysts & calendar · 4/10 · ❌ FAIL

| Date | Event |
|---|---|
| Every 2 weeks to ~2030 | Bi-weekly unlocks of four buckets (started 3 Oct 2025) |
| Daily to 2028 | Foundation Treasury daily unlock |
| TBD | Wormhole Reserve launch ("coming soon" since Sep 2025); Portal Earn boosts |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🔴 **Yes (historic):** Feb 2022, ~$320M, made whole |
| Treasury → exchange during a pump | 🔴 **Yes:** lockup-paid wallets → Binance/OKX on 10 pump days, 25.3M W. [21 Sep 2026 tx](https://etherscan.io/tx/0x0859566dd69423820f524de310ed231e79203cfe0d511dbd41a6de65c1fb104b) |
| Unenforced lock-ups | 🟡 Contributor lock is contractual only; tokens already sit with the Foundation |
| Live mint path | 🟢 None beyond the 10B cap |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| Hedgey lockup beneficiaries (Inotel, Wintermute, others) | Infrastructure operator and market maker (Arkham); others unknown | Arkham + Etherscan | medium | no | None: not proven Foundation or team wallets |

## 📚 Sources

- [Tier A] Methodology update 16 Nov 2026: no new Arkham lookups; the attribution table uses evidence already cited in this report.
- [Tier A] Etherscan v2 API: `tokentx` for the lockup contract and ~75 traced wallets (BFS depth 3, ≥1M W), NTT mint records; Etherscan token-holders page; read 16 Nov 2026 MST
- [Tier B] Etherscan name tags: "Hedgey Finance: Voting Token Lockups", "Hedgey Finance: Batch Planner", "Binance Deposit", "Binance 14", "Binance: Cold Wallet 20", "OKX 154", "Wintermute", "Abyss Finance: Eth2 Depositor 29"
- [Tier A] [W 2.0 post](https://wormhole.com/blog/wormhole-announces-w-token-2-0-upgrade) · [incident report](https://wormholecrypto.medium.com/wormhole-incident-report-02-02-22-ad9b8f21eec6)
- [Tier A] DefiLlama Portal fees/revenue; CoinGecko `wormhole` (16 Nov 2026 6:51 AM MST); KuCoin W-USDT daily candles for every pump test
- [Tier B] Arkham, read 16 Nov 2026 (signed-in account): Inotel on `0xdd83`/`0xb8c6`; Wintermute Deposit `0x57cd`; OKX Deposit `0x2331`; Binance Deposit `0xb926`; VotingVault contract `0xb016`; Hedgey contracts; Solana W mint (links in Holdings and Selling)
- [Unverified] owners of `0x4672`, `0x0d59`, `0x712e`, `0xcef7`; the Hedgey lockup beneficiary list; the top holders of the Solana W mint; which allocation bucket the Hedgey lockups hold; the whole Solana side

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| NTT mints to 0x4672 / 0x0d59 | [0x4672 mint](https://etherscan.io/tx/0x3ae3f0b64689b29518f0fee5eadd3f45a3be6214f6d78040fedc26bfab4aba82) · [0x0d59 mint](https://etherscan.io/tx/0x5a5e563bfa77dd895cdf4bdacef1315ee04924b99d91576c6f1b2fb97ccd4fcf) | A | 16 Nov 2026 |
| Mint wallets → Hedgey Batch Planner | [337.5M](https://etherscan.io/tx/0x592d1a4fca2b7290e61bb92965cb8dc83c424ff2cba367f0efcd7af0a214fd22) · [130.65M](https://etherscan.io/tx/0xa64a60f411e9ac5bdb3e854b5cb687dce0c7f7474e2ca76056e45dabc40b6d3f) · [30.69M](https://etherscan.io/tx/0x45b20b543ef51382a67560777496179532d5bf98b547b50f50d211eb36cf8be7) | A + B tag | 16 Nov 2026 |
| Lockup → 0xb016 → 0x712e → 0xcef7 → Binance (+29.1%) | [lockup→0xb016](https://etherscan.io/tx/0x4b1105508d7d3b7e98c7c49dc977704eca3f07768911249c0fdf8ec51d54b23b) · [0xb016→0x712e](https://etherscan.io/tx/0x0036569d2e6bf08dea5c04dfaf0ce27277b3bfac4961e14293228cdfd4cdd7bf) · [0x712e→0xcef7](https://etherscan.io/tx/0x29ac5bfe7376e88b79ff3af55671c8391a7194f1e90d4c774c9b30b7678e6120) · [deposit](https://etherscan.io/tx/0x0859566dd69423820f524de310ed231e79203cfe0d511dbd41a6de65c1fb104b) | A + B tag | 16 Nov 2026 |
| Lockup → … → OKX on +21.3% day | [0xb016→0xb660](https://etherscan.io/tx/0xa1e32a33f49a10a5b547bc76e6bf769961313fd30eee76621118ef3a47dd0428) · [0xb660→0x2331](https://etherscan.io/tx/0x142e82884fd62b1249b704c5a9046e9f873e76c54f921bf66fc4a4744826fb74) · [deposit](https://etherscan.io/tx/0x4b1fe85a0f5503aea09b17f616e53ed07bdd0dcf780634e8ed7982274c7a78a8) | A + B tag | 16 Nov 2026 |
| 0xb8c6 → Binance on +28.6% day | [fund](https://etherscan.io/tx/0x47579386cf57da5fe8ea4d78f46de2b02704ed58b0ada037aa23efe34f05264e) · [deposit](https://etherscan.io/tx/0x659ba7f4d4461c467967f0f37ee9b06c47518ad0ad7c6dc5e7a972d376b99b48) | A + B tag | 16 Nov 2026 |
| Unlock schedule, Reserve, escrow wording | [W 2.0 post](https://wormhole.com/blog/wormhole-announces-w-token-2-0-upgrade) | A | 16 Nov 2026 |
| Fees ~$319k/yr; revenue $0 | [DefiLlama](https://defillama.com/protocol/portal) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Lockup beneficiaries and mint wallets** | Arkham (16 Nov 2026) leaves `0x4672`, `0x0d59`, `0x712e` and `0xcef7` unlabelled and does not list Hedgey beneficiaries. Read the Hedgey plan NFTs' owners on-chain, or ask the Foundation [Unverified] | Free |
| 2 | **Solana side** | Arkham shows the W mint but not its top holders [Unverified]. Use a paid Solana RPC or Solscan Pro to list the largest W accounts and Foundation unlock wallets, then run the same pump test | Paid RPC |
| 3 | **Ask Wormhole Foundation** | Which bucket the Hedgey lockups hold, and whether `0x712e` is a Foundation or contributor payroll wallet | Free |
| 4 | **Reserve** | Watch for the Reserve contract and any real revenue flow into it | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
