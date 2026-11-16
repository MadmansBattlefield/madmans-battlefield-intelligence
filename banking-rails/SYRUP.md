---
ticker: SYRUP
name: Maple Finance
chain: ethereum
contract: "0x643C4E15d7d62Ad0aBeC4a9BD4b001aA3Ef52d66"
overall_score: 5.9
overall_verdict: FAIL
section_scores:
  revenue: 5
  foundation_team: 7
  insider_holdings: 6
  selling_behavior: 4
  tokenomics_supply: 6
  liquidity_market: 6
  product_development: 8
  adoption_customers: 8
  security_audits: 7
  regulatory: 5
  catalysts: 6
gates_failed: []
red_lines:
  hack_exploit: none found on the SYRUP token or the syrup pools
  mint_path_live: "governance only (MapleToken mints only through modules the Maple GovernorTimelock schedules; the Recapitalization Module's issuance window went to 0 on 1 Oct 2026)"
  team_wallet_to_exchange_during_pump: "yes, treasury-labelled wallets (Etherscan 'Maple: Treasury 2', 'Maple: Treasury 1', 'Maple: DAO') funded wallets that put SYRUP into exchange deposit addresses on pump days: 7.0M into a Maple-used Binance deposit on 29 Oct, 10 Nov and 22 Dec 2025; 6.25M into a Binance deposit on the 6 May 2025 pump day; ~1.1M into Gate on 21 Nov 2024. Sales not provable on-chain; a market-maker loan program (~2% of supply) is disclosed"
  one_hop_sale_status: not_proven
  treasury_coins_to_otc_desk: "yes (SSF wallet 0x99f0 sent 4.6M SYRUP, including bought-back tokens, to a FalconX deposit in Jul and Sep 2026; purpose [Unverified])"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "MIP-021 buybacks are a governance rule carried out by the Syrup Strategic Fund through Binance, not an automatic on-chain mechanism, and bought SYRUP is held in the treasury. No fee share or fee-funded staking yield is documented. The binary test is therefore **no**, and Revenue cannot pass: **7 → 5**. A 5 still describes a real lending business, but holders have no live claim on its revenue."
pump_day_price_source: "Gate SYRUP/USDT UTC daily closes"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions:
  - address: "0x9e786e5e2ffe875cdeb3bdd34f932b9baed69423"
    label: "Maple: Treasury 2"
    confidence: high
    independent_corroboration: true
    basis: "Etherscan tag + Maple token-transparency filing"
  - address: "0x6893f4df778358e6967ef899dc440ae20f9ba6bf"
    label: "Maple-controlled EOA (receives buyback SYRUP from Binance 14)"
    confidence: high
    independent_corroboration: true
    basis: "Etherscan flows matching Maple-reported buybacks"
  - address: "0x640e8ccfd0e62e6f7da284c701746eab4cb3fb7d"
    label: "Syrup.fi (Maple Finance)"
    confidence: high
    independent_corroboration: true
    basis: "Arkham + Etherscan treasury funding"
  - address: "0x99f03ca02b232dc124b62b8cf40b2bfd21eae9ca"
    label: "Syrup Strategic Fund EOA"
    confidence: medium
    independent_corroboration: true
    basis: "Etherscan flows + Maple buyback figures"
price_usd: 0.1016
price_source: "CoinGecko, 16 Nov 2026 5:27 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### SYRUP · Overall grade **5.9 / 10 · ❌ FAIL**

**Summary:** Maple is a real on-chain credit business: $4.7B AUM, $1.67B of loans and $4.4M of revenue in Q3 2026, and DefiLlama counts $14.5M of protocol revenue over the last year against a ~$119M market cap. A rules-based buyback (MIP-021: 10–30% of monthly revenue) turns part of that into SYRUP purchases. The treasury is in labelled wallets and a 4-of-7 DAO Safe, and Maple publishes them. The weak spot is Selling: treasury-labelled wallets funded wallets that put about **15M SYRUP into exchange deposit addresses on five pump days** (Nov 2024 – Dec 2025), and the buyback fund later sent 4.6M SYRUP to an OTC desk. A market-maker loan program is disclosed, but no disclosure ties these specific deposits to it. Passes on the weighted average, with Selling as a clear ❌.

**🚨 Top warning:** Etherscan's **"Maple: Treasury 2"** [`0x9e78…9423`](https://etherscan.io/address/0x9e786e5e2ffe875cdeb3bdd34f932b9baed69423) (Maple's own filing calls it the wallet for "day to day operations involving SYRUP eg MM contracts") paid SYRUP into wallet [`0x6893…a6bf`](https://etherscan.io/address/0x6893f4df778358e6967ef899dc440ae20f9ba6bf), which put it into its own **Binance deposit address** [`0xf0c1…db47`](https://etherscan.io/address/0xf0c1445a72d3f5f9355ef846ad8bb14b2e03db47) **within minutes, on pump days**: [10 Nov 2025, 1M in](https://etherscan.io/tx/0x8f580b945198a7aae462a5d6ed7f8e0a57b2e854f2f0f2b88eb336763f165997) → [Binance 2 minutes later](https://etherscan.io/tx/0x5e75fcd136dd5c9bb5158fc43db7fa0c4249e5fbda32e199c7a8d22a6d45fed7) (+11.9% in 5 days) · [22 Dec 2025, 2M in](https://etherscan.io/tx/0x6a75486e7efc85e5ab5c1af22a482fafaffcb12db4bfdc083540202997a22375) → [Binance 6 minutes later](https://etherscan.io/tx/0xf57759519928eaf0b8f3b061dffabb0e4921f869dd6d23bc46334f941ee2c2da) (+21.2%) · [29 Oct 2025, 4M from SSF wallet `0x99f0…`](https://etherscan.io/tx/0x5daa8c8344a45e3048298c90263e56ec857fdd5c11bd757976950278cedab9a0) → [Binance 7 minutes later](https://etherscan.io/tx/0x46e35cc4e8356a9462405ca0ac862dd93e91fc71c56ef3aa64f7ff2c36b10d1d) (+12.8%). That is **7.0M SYRUP (≈ $2.8M at those days' closes)**. `0x6893…` is Maple's: the exact Q3 2026 buyback amounts (852,841 + 676,290 + 1,371,166 = 2.90M, matching Maple's "2.9M SYRUP bought back") were withdrawn from Binance into it ([e.g. 1,371,166](https://etherscan.io/tx/0xde481457b2d08ff9a5f71a9325733b74908a975d94a34e235a4b12dfb244cc55)). Whether the deposits were sold is not visible on-chain. Every transfer is linked in the 🔗 Evidence trail below.

**Sections passed: 8 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 5/10 | ❌ FAIL |
| 🏛️ Foundation & team | 7/10 | ✅ PASS |
| 🪙 Foundation / team holdings | 6/10 | ✅ PASS |
| 📉 Selling behavior | 4/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 6/10 | ✅ PASS |
| 💧 Liquidity & market | 6/10 | ✅ PASS |
| 🧑‍💻 Product & development | 8/10 | ✅ PASS |
| 🤝 Adoption & customers | 8/10 | ✅ PASS |
| 🛡️ Security & audits | 7/10 | ✅ PASS |
| ⚖️ Regulatory | 5/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 6/10 | ✅ PASS |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 SYRUP · Maple Finance · 5.9 / 10 · ❌ FAIL

> **One line:** A real, growing on-chain lender ($4.7B AUM, ~$17.6M revenue run-rate) whose token gets a rules-based slice of revenue through buybacks, with labelled treasury wallets and multisig control. But treasury-funded wallets repeatedly put SYRUP into exchange deposit addresses on pump days, and the buyback fund has since sent tokens to an OTC desk, with no line-by-line disclosure.

| 📊 Market (CoinGecko, 16 Nov 2026 5:27 AM MST) | 🔗 On-chain (Ethereum, 16 Nov 2026) |
|---|---|
| **Price** $0.1016 | **Token** [`0x643C…2d66`](https://etherscan.io/address/0x643C4E15d7d62Ad0aBeC4a9BD4b001aA3Ef52d66) MapleTokenProxy → `MapleToken` impl [`0x6ed7…7aec`](https://etherscan.io/address/0x6ed767ebcff51533e5181f7bf818f2b9bd767aec#code) |
| **24h / 7d / 30d** 🔴 −2.4% / −24.4% / −50.8% · 1y −78.5% | **`totalSupply()`** 1,267,875,000 |
| **Market cap** $118.6M · **FDV** $128.8M | **Circulating (CoinGecko)** 1,167,271,959 (92%) |
| **24h volume** $6.06M | **Mint path** modules only, added by [Maple: Governor](https://etherscan.io/address/0x2efff88747eb5a3ff00d4d8d0f0800e306c0426b) (GovernorTimelock) |
| **ATH** $0.6532 (25 Jun 2025) · now −84% | **DAO Safe** [`0xd6d4…a196`](https://etherscan.io/address/0xd6d4bcde6c816f17889f1dd3000af0261b03a196) 4-of-7, 42.29M SYRUP |
| **Holders** 18,367 (Blockscout) | **Staked** [stSYRUP](https://etherscan.io/address/0xc7E8b36E0766D9B04c93De68A9D47dD11f260B45) 144.6M SYRUP (#1 holder) |

---

## 💰 Revenue — Does it make money? · 5/10 · ❌ FAIL

| Metric | Value | Source |
|---|---:|---|
| Fees, last 30 days / 1 year | **$9.62M / $109.5M** (gross interest and fees across pools) | [Tier A] [DefiLlama Maple fees](https://defillama.com/protocol/maple), read 16 Nov 2026 5:27 AM MST |
| Protocol revenue, last 30 days / 1 year | **$1.47M / $14.46M** | [Tier A] [DefiLlama](https://defillama.com/protocol/maple) |
| Holders revenue (buybacks), last 30 days / 1 year | $192.6k / $2.96M | [Tier A] DefiLlama `dailyHoldersRevenue` |
| Maple's own figures | Q3 2026 revenue **$4.4M** (flat on Q2, +5% YoY), ARR $17.6M; LTM protocol revenue **$21.37M** on its transparency page | [Tier A] [Maple Q3 update](https://maple.finance/insights/maple-q3-ecosystem-update) · [Maple financials](https://maple.finance/transparency/financials) |
| Token link | **MIP-021** (live 13 Jul 2026): the Syrup Strategic Fund buys SYRUP with 10% of monthly revenue under $1.5M, 20% from $1.5–2M, 30% above $2M. 2.90M SYRUP bought in Q3 2026 | [Tier A] [Maple Q3 update](https://maple.finance/insights/maple-q3-ecosystem-update); amounts matched on-chain (see Selling) |
| Market cap ÷ protocol revenue | ~8x (DefiLlama 1y) · ~5.5x (Maple LTM) | derived |

**What it means:** Real revenue from institutional lending, cheap relative to the token's market cap, and a written rule that routes part of it into buybacks. It is not a 7+ business for holders yet: buybacks took only 13.6% of Q3 revenue (and 3.4% in H1 2026, per Alea), bought tokens are held in the treasury rather than burned, and Maple says buybacks "are not a dividend". Also, October revenue fell back under the $1.5M tier [Tier B, Alea Q3 report].

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** MIP-021 buybacks are a governance rule carried out by the Syrup Strategic Fund through Binance, not an automatic on-chain mechanism, and bought SYRUP is held in the treasury. No fee share or fee-funded staking yield is documented. The binary test is therefore **no**, and Revenue cannot pass: **7 → 5**. A 5 still describes a real lending business, but holders have no live claim on its revenue.

## 🏛️ Foundation & team — Who is in charge? · 7/10 · ✅ PASS

| Item | Finding | Source |
|---|---|---|
| Operator | Maple (Maple Labs) with the **Maple DAO Foundation**; co-founder and CEO Sid Powell hosts the quarterly updates | [Tier A] [Maple Q3 update](https://maple.finance/insights/maple-q3-ecosystem-update) |
| Published wallet list | Maple's token-transparency filing names **Treasury 1** [`0x6a01…acff`](https://etherscan.io/address/0x6a01c16eb312b80535f4799e4bf7522b715aacff) ("staging wallet used for OpEx") and **Treasury 2** [`0x9e78…9423`](https://etherscan.io/address/0x9e786e5e2ffe875cdeb3bdd34f932b9baed69423) ("day to day operations involving SYRUP eg MM contracts") | [Tier B] [Blockworks Token Transparency filing](https://blockworks.com/token-transparency/filing/maple-finance/dc60bd1d-3554-4c92-9caf-82e8fc10d4c5) + matching Etherscan tags |
| Governance | `MapleToken.governor()` = [Maple: Governor](https://etherscan.io/address/0x2efff88747eb5a3ff00d4d8d0f0800e306c0426b) (`GovernorTimelock`); DAO Safe [`0xd6d4…`](https://etherscan.io/address/0xd6d4bcde6c816f17889f1dd3000af0261b03a196) is **4-of-7** | [Tier A] RPC reads, 16 Nov 2026 |
| Reporting | Quarterly ecosystem updates and a live financials page | [Tier A] [Maple financials](https://maple.finance/transparency/financials) |

**What it means:** Named leadership, a published wallet list and live financials put Maple well above most tokens. The legal entities and their registers were not read this pass.

## 🪙 Foundation / team holdings — How many coins do they hold? · 6/10 · ✅ PASS

| Bucket | SYRUP | Notes |
|---|---:|---|
| Maple's own figure | **127.55M held by the DAO and the SSF** (≈ 10% of supply); SSF alone 82.42M | [Tier A] [Maple financials](https://maple.finance/transparency/financials) |
| Maple: DAO Safe [`0xd6d4…`](https://etherscan.io/address/0xd6d4bcde6c816f17889f1dd3000af0261b03a196) | 42,290,111 | 4-of-7. Receives every treasury mint ([e.g. 23.2M on 13 Oct 2026](https://etherscan.io/tx/0xd628a262f005c88d41492d15311b4294e94b550639fc759bb844f08cc9351b18)) |
| Safe [`0x58BE…39A1`](https://etherscan.io/address/0x58BE00490D6a5D298d61f24226d2397983Ee39A1) | 48,624,988 | 3-of-5; **3 of its 5 signers also sign the DAO Safe** (Tier A, `getOwners`). Got 76.12M from the DAO on [13 Aug 2025](https://etherscan.io/tx/0x8fd49428373bb8376b114e15d335f14213d737e38742368385233a3555165d9a). Arkham: unnamed Gnosis Safe, 48.625M, counterparties the Maple DAO and Maple-labelled `0x99f0…` ([Arkham](https://intel.arkm.com/explorer/address/0x58be00490d6a5d298d61f24226d2397983ee39a1)) |
| SSF operating EOA [`0x99f0…a9ca`](https://etherscan.io/address/0x99f03ca02b232dc124b62b8cf40b2bfd21eae9ca) | ~2.40M | Funded by `0x58BE…` (27.5M); receives the 2026 buybacks (see Selling). Arkham: **Syrup.fi (Maple Finance)**, 2.402M ([Arkham](https://intel.arkm.com/explorer/address/0x99f03ca02b232dc124b62b8cf40b2bfd21eae9ca)) |
| Maple: Treasury 2 / Treasury 1 | ~2.83M / 0 | EOAs (single keys) |
| Safe [`0x5037…C59`](https://etherscan.io/address/0x50371EcBBbf0EbF062Da49E0Cb314d1eF90DC5ae) | 14,175,559 | Withdrawn from stSYRUP on [16 Jul 2026](https://etherscan.io/tx/0xf176710693596f416648928e97b6772d59f0e98e90060a11df5994705904b22b); Arkham shows an unnamed Gnosis Safe ([Arkham](https://intel.arkm.com/explorer/address/0x50371ecbbbf0ebf062da49e0cb314d1ef90dc5ae)); owner [Unverified] |
| Vesting [`0x9CB9…52Aa`](https://etherscan.io/address/0x9CB93Ceff896a3A9D333f3831272e59333a352Aa) (MerkleVester) | 10,626,905 | Fed 66.1M by distributor [`0x3fcd…7e1a`](https://etherscan.io/address/0x3fcdcc5bc5178c81738c176613818d9d2c7f7e1a) (Arkham: Syrup.fi (Maple Finance), Contract Deployer, with repeated Treasury → MerkleVester flows, [Arkham](https://intel.arkm.com/explorer/address/0x3fcdcc5bc5178c81738c176613818d9d2c7f7e1a)) |
| #2 holder [`0xCA31…9C59`](https://etherscan.io/address/0xCA31C9EF59a6Ab45343f60968148C0Ed07C39C59) | 109,064,092 (8.6%) | Filled from **Coinbase Prime 2** in 8 transfers since Mar 2025. **Arkham files it under ParaFi Capital** (an investment fund), tagged Dormant, with Coinbase Prime's hot wallet as counterparty ([Arkham](https://intel.arkm.com/explorer/address/0xca31c9ef59a6ab45343f60968148c0ed07c39c59)). An outside investor, not a Maple wallet |

**What it means:** Maple says what it holds (~10%), and the wallets it names line up with the chain. Large balances sit in Safes, but day-to-day SYRUP moves through single-key EOAs (Treasury 1, Treasury 2, `0x99f0…`, `0x6893…`). The 109M custody wallet, the biggest unknown before, is an investor fund per Arkham (ParaFi Capital, dormant), not Maple. That is one Tier B label, so it is not counted as fact, but it does not add to team holdings either way. **6, a pass, unchanged.**

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL

*Pump test uses Gate SYRUP/USDT daily closes (UTC days, from 14 Nov 2024). 52 of the last 365 days were pump days.*

**A. Treasury-funded wallets into exchange deposit addresses on pump days**

| Day (UTC) | Route (all links on Etherscan) | SYRUP | Close / 5-day change | Pump? |
|---|---|---:|---:|---|
| 21 Nov 2024 | **Maple: Treasury 1** → [`0x4460…5626`](https://etherscan.io/address/0x446063e301d4a3a064b19562b0aacdc6c8f15626) ([1.0M](https://etherscan.io/tx/0x15fa5a980bb6acab06d3a6810f4c484fee2b7015691fbcfbb049a3fc02b3d05f) · [1.2M](https://etherscan.io/tx/0x88d10c79c077154fc26b767e8eb059afea3d8c51b43d91aa9aeb48192ffa5ac0) · [360,270](https://etherscan.io/tx/0x79c05c69be063ceaee167b6299bdbffb17e3fd7f056da978daa519de4ca41b91)) → Gate deposit [`0x6e50…9ca6`](https://etherscan.io/address/0x6e50d3c6b659db780f21da84fa8194f437239ca6) ([350k, 15 min later](https://etherscan.io/tx/0xbee48bcf5d94a0cdf0fa1fdadd975745f61aebd31c553215ea47089320371ce6) · [150k](https://etherscan.io/tx/0xba09e94c48075914a518b99225f316b16805a0ef1f4602ef6d60f04a3237da87) · [360,270](https://etherscan.io/tx/0xf70f39932ec0b755fea8766be59c48b7c748bd0086a4905c3bb66b11120a1cf3)); plus Treasury-1-funded [`0x9e65…cc28`](https://etherscan.io/address/0x9e6538212ca6afccb03e05d929fe415e6621cc28) → same Gate deposit ([250k](https://etherscan.io/tx/0x714d4bd43322e027af162c0c3335fe5a5ed0235e5033d0e257a84bd8b4600621)) | 1,110,270 | $0.2530 / +10.8% | 🔴 Yes |
| 6 May 2025 | **Maple: DAO** → Safe [`0x4c3b…ea61`](https://etherscan.io/address/0x4c3b453652cc3dd5d004d594e216f44d7541ea61) 11.47M ([tx](https://etherscan.io/tx/0x63e2c646a638df1d7b0e850a74f18f62a1c561760badfa72d2b6e0b349ff04ac)) → [`0x640e…b7fd`](https://etherscan.io/address/0x640e8ccfd0e62e6f7da284c701746eab4cb3fb7d) ([4.25M](https://etherscan.io/tx/0xba1e1f0a73c51c5a61df52fe756f178b22c3bde1c4c392eb9a306b7538751419) · [2.0M](https://etherscan.io/tx/0x9a7e8d72bcb4707ac31f26a573cbffd3f5e551030e52a3225d2da2bbaaa84e33)) → Binance deposit [`0xcf4c…Ef96`](https://etherscan.io/address/0xcf4cc9e56e123df65e34c66925914f2815efef96) ([4.25M, 15 min later](https://etherscan.io/tx/0xfb42eb9f69b491914cb011881e0defc4a66307f3442529ab70a8c55e7791de63) · [2.0M](https://etherscan.io/tx/0x001294ca4044e51513fec205a7568663deaaeb5db4f39c58764a6268afa55109)) | 6,249,900 | $0.2197 / +33.9% | 🔴 Yes |
| 29 Oct 2025 | SSF EOA `0x99f0…` → `0x6893…` ([4M](https://etherscan.io/tx/0x5daa8c8344a45e3048298c90263e56ec857fdd5c11bd757976950278cedab9a0)) → Binance deposit `0xf0c1…` ([7 min later](https://etherscan.io/tx/0x46e35cc4e8356a9462405ca0ac862dd93e91fc71c56ef3aa64f7ff2c36b10d1d)) | 4,000,000 | $0.4244 / +12.8% | 🔴 Yes |
| 10 Nov 2025 | **Maple: Treasury 2** → `0x6893…` ([1M](https://etherscan.io/tx/0x8f580b945198a7aae462a5d6ed7f8e0a57b2e854f2f0f2b88eb336763f165997)) → Binance deposit ([2 min later](https://etherscan.io/tx/0x5e75fcd136dd5c9bb5158fc43db7fa0c4249e5fbda32e199c7a8d22a6d45fed7)); same day Treasury-1-funded `0x9e65…` → Binance deposit [`0x77ab…d5B9`](https://etherscan.io/address/0x77ab7d3d34b80f033f494f95683264690fdcd5b9) ([724,900](https://etherscan.io/tx/0xd7b4fd4facc22cd53502b90b355dcf62a0ab71d71a37fd75122b3bc81fb11478)) | 1,724,900 | $0.4663 / +11.9% | 🔴 Yes |
| 22 Dec 2025 | **Maple: Treasury 2** → `0x6893…` ([2M](https://etherscan.io/tx/0x6a75486e7efc85e5ab5c1af22a482fafaffcb12db4bfdc083540202997a22375)) → Binance deposit ([6 min later](https://etherscan.io/tx/0xf57759519928eaf0b8f3b061dffabb0e4921f869dd6d23bc46334f941ee2c2da)) | 2,000,000 | $0.3320 / +21.2% | 🔴 Yes |

- **Pump-day total: ~15.1M SYRUP (≈ 1.2% of supply, ≈ $4.8M at those days' closes).** Non-pump deposits from the same wallets add more, e.g. [5 Nov 2025, 2M](https://etherscan.io/tx/0xbf359dc45ab8135e75add265d1f38b4ada62bfe5b1dc692f1f819a430db7cda6) and [13 Nov 2025, 1.25M](https://etherscan.io/tx/0x674f6ecda3240bfabb7ca902c21a2fb1e244593cb5cd863c444eea87a21d8f80) into the same Binance deposit.
- **Whose deposit address it is:** `0xf0c1…` received SYRUP **only from `0x6893…`** (10.25M in 5 transfers) and swept all of it to Binance 14. `0x6893…` is Maple's: Binance 14 later paid it exactly 852,841 / 676,290 / 1,371,166 SYRUP ([5 Aug](https://etherscan.io/tx/0x87ef10f94e37e24d7deb4ee25dc13b957219d00b1031e9046564029ec744911c) · [8 Sep](https://etherscan.io/tx/0x98fcb3c1b337b499d50dbe5fbd70fd95d916a4f02dc1c9fc31e4e5a265084915) · [8 Oct 2026](https://etherscan.io/tx/0xde481457b2d08ff9a5f71a9325733b74908a975d94a34e235a4b12dfb244cc55)), which sums to the **2.90M SYRUP** Maple says it bought back in Q3 2026 ([Maple](https://maple.finance/insights/maple-q3-ecosystem-update); August's 676,294 per [TokenPost](https://www.tokenpost.com/news/business/35072)). Those tokens then went to the SSF EOA `0x99f0…` via [`0x6400…bb9c`](https://etherscan.io/address/0x6400e01bc27e185fa74091df362c430252f7bb9c). So `0x6893…`/`0xf0c1…` is a Maple-controlled Binance account. [Tier A] chain + [Tier A] Maple's own buyback figure.
- **The 6 May 2025 Binance deposit `0xcf4c…` is shared** by a cluster (`0x640e…`, [`0xaa58…`](https://etherscan.io/address/0xaa58d64f9ca0d6436f903a4d590ad8e5982c8030), [`0x2c9f…`](https://etherscan.io/address/0x2c9f282067c5962c0a96719400b419add9e7293a) and others; 99.3M SYRUP in total). `0x640e…` was funded by Treasury 1, Treasury 2, the DAO-funded Safe `0x4c3b…` and `0xa7cc…`. This may be a market maker's Binance account [Unverified]. **Arkham pass ([Tier B] Arkham, read 16 Nov 2026 ~7:07–7:18 AM MST (signed-in account)):** Arkham labels `0x640e…` itself **Syrup.fi (Maple Finance)** ([Arkham](https://intel.arkm.com/explorer/address/0x640e8ccfd0e62e6f7da284c701746eab4cb3fb7d)), and `0xcf4c…` a Binance deposit address without naming the account owner ([Arkham](https://intel.arkm.com/explorer/address/0xcf4cc9e56e123df65e34c66925914f2815efef96)). That makes it more likely the 6 May 2025 deposit came from a Maple-run wallet, not a market maker's. It removes a possible excuse rather than adding a new deposit. Arkham also tags Safe `0x4c3b…` as a Maple **Team Wallet** ([Arkham](https://intel.arkm.com/explorer/address/0x4c3b453652cc3dd5d004d594e216f44d7541ea61)) and `0xa7cc…` as Syrup.fi (Maple Finance) ([Arkham](https://intel.arkm.com/explorer/address/0xa7cc8d3e64ea81670181b005a476d0ca46e4c1fc)). `0x6893…` shows Maple only as a *predicted* entity, and its About panel says it is not attributed ([Arkham](https://intel.arkm.com/explorer/address/0x6893f4df778358e6967ef899dc440ae20f9ba6bf)); its tie to Maple rests on the Tier A buyback match above. `0x4460…` ([Arkham](https://intel.arkm.com/explorer/address/0x446063e301d4a3a064b19562b0aacdc6c8f15626)) and `0x9e65…` ([Arkham](https://intel.arkm.com/explorer/address/0x9e6538212ca6afccb03e05d929fe415e6621cc28)) are unlabelled; `0x4460…`'s counterparties are a Binance deposit, Maple's Treasury and a Gate deposit, as traced above.

**B. Disclosed context.** Maple's filing says the DAO Foundation lent "~2% of SYRUP supply" to **GSR, Keyrock and STS** for CeFi liquidity on Binance, Coinbase, Bitget, Gate, KuCoin and MEXC, with loans from Q3 2024 maturing by Q1 2026 ([Blockworks filing](https://blockworks.com/token-transparency/filing/maple-finance/dc60bd1d-3554-4c92-9caf-82e8fc10d4c5)). On-chain, Treasury-1-funded [`0xa161…f9a6`](https://etherscan.io/address/0xa1612e876979768d208b8be6cdc2f85f1f5ff9a6) paid **GSR** 3.0M ([e.g.](https://etherscan.io/tx/0x18c64dfe22ec05764c7c6d5eef4f40eb48c2a77049c29a06d3bff9e56693f644)), matching that program. At launch, Treasury 1 also sent **45.55M to a Gate hot wallet** ([12 Nov 2024](https://etherscan.io/tx/0x85adb3a725c007b7aee1c6a084c59225ef6d2a5db0c6918fb4d61d008c3ac797)) and **17.16M to Kraken 146** ([11 Nov 2024](https://etherscan.io/tx/0xce521fbf531baa18f0747ca30c34f0ebbabfa0eb90c393e6b443367f6c021746)), before Gate trading opened on 14 Nov 2024, so those could not be pump-tested. 62.7M is ~5% of supply, more than the "~2%" loan figure; what it was for is [Unverified].

**C. Last 12 months.** The SSF EOA `0x99f0…` sent **4.6M SYRUP to a FalconX deposit** [`0x7c98…1e63`](https://etherscan.io/address/0x7c982ebe651ee2169aed8fcb121f36a2c6b91e63) (swept to FalconX 1): [2.5M on 9 Jul 2026](https://etherscan.io/tx/0xcfc21703e88a5da48cbf36e6499557e538ab0af0b18517c35139a12ffc3266c4) (+1.4%, not a pump) and [2.1M on 29 Sep 2026](https://etherscan.io/tx/0x64ef0aa34561c2984ecfb5c68cc3bee95e4cfbac3caf9d3cadbd304f5a5f0a39), the day after a +15.2% pump close (29 Sep itself +7.5%). The September send came three weeks after August's buyback (676,290) reached `0x99f0…`. Maple's MIP-019 post says bought-back tokens "are held, not sold". FalconX is an OTC/prime broker, so this could be a sale, a loan or custody. [Unverified].

**What it means:** The rule: a treasury wallet selling, or funding a wallet that deposits to an exchange, on a pump day, without disclosure, failed Selling under the earlier rule. Maple-labelled wallets did that on five pump days. It discloses a market-making program and names the wallets, which is better than most, and the deposits are a small share of supply (~1.2%). But nothing published ties these specific pump-day deposits to that program, and the 2026 OTC sends cut against the "held, not sold" line. Under the 16 Nov 2026 one-hop amendment the disclosed market-making program is a plausible reason and no sale is shown, so Selling is **4 (not proven)**, with no penalty and no hard gate.

- **One-hop amendment (16 Nov 2026):** Maple publishes a market-making loan program in its [Blockworks Token Transparency filing](https://blockworks.com/token-transparency/filing/maple-finance/dc60bd1d-3554-4c92-9caf-82e8fc10d4c5), a plausible reason for the shared Binance deposit flow. Under the amended rule the sale is **not proven**, so disclosure quality is recorded as not applicable. The score stays **4**.

## 📊 Tokenomics & supply · 6/10 · ✅ PASS

- **Origin:** on 12 Sep 2024 the token minted 1,000,000,000 SYRUP to the **Maple: Migrator** [`0x9c94…8f2c`](https://etherscan.io/address/0x9c9499edd0cd2dcbc3c9dd5070baf54777ad8f2c) for MPL holders (1 MPL : 100 SYRUP) and 154.93M to the Maple Treasury ([tx](https://etherscan.io/tx/0x501a85d22af5d7e41bc3d302396be99b6fc38166be04d485daba1d0314f35a2c)).
- **Inflation (Tier A, module events):** the [Recapitalization Module](https://etherscan.io/address/0x5dfe0460f66fa06bfcbb3211e723556be6b3f69d) issued to the treasury at ~56.5M/yr (Q4 2024), ~59.6M/yr (2025) and ~52.3M/yr (Jan–Sep 2026; [schedule tx](https://etherscan.io/tx/0x3c7050893d938ddd683a4b6e4e28166e14acf0571c8eeb63c367897924051937)). That is **~4–5% a year**. Eight treasury mints totalled 189.07M; the last was 23.2M on [9 Oct 2026](https://etherscan.io/tx/0x3bab89ef0729cb48f722f2a9392e334612ee7336d210795fcc343e8d11f72ac6). `currentIssuanceRate()` is **0** from 1 Oct 2026, so issuance has stopped unless governance schedules a new window.
- **Unclaimed-migration recycle:** on [3 Jul 2025](https://etherscan.io/tx/0x584bbc248e5098e63024e26d601dd0fd9c092842e9d04c8ad3613cd28a2bc8fa) a one-off module burned 76.12M unmigrated SYRUP from the Migrator and minted the same amount to the treasury (→ DAO → Safe `0x58BE…`). That moved dormant supply to the DAO.
- `totalSupply()` 1,267,875,000; ~92% circulating per CoinGecko. No hard cap: new modules can be added, but only through the timelocked Governor.

## 💧 Liquidity & market · 6/10 · ✅ PASS

- $6.06M of volume in 24h on a $118.6M cap (≈ 5.1% turnover). Binance, Kraken, Gate, FalconX and an Upbit deposit appear among the top-50 holders (Blockscout). Uniswap v3/v4 pools hold a few million SYRUP.
- The price fell 84% from the ATH and 51% in 30 days. Market makers on six exchanges per Maple's filing.

## 🧑‍💻 Product & development · 8/10 · ✅ PASS

- syrupUSDC, syrupUSDT and syrupUSDG yield tokens and permissioned Maple Institutional pools. syrupUSDG launched on Arbitrum, Ink and Solana in Q3 2026, plus new allocation strategies ([Maple Q3](https://maple.finance/insights/maple-q3-ecosystem-update)).
- DefiLlama TVL ~$2.21B (Bitcoin collateral $1.70B, Ethereum $268M, XRPL $242M) plus $1.54B borrowed ([DefiLlama](https://defillama.com/protocol/maple)).
- Public contracts verified on Etherscan (token, Governor, modules). A public GitHub commit date was not found in the scan.

## 🤝 Adoption & customers · 8/10 · ✅ PASS

- AUM $4.7B (+18% YoY), loans $1.67B, 17% of tracked DeFi loans outstanding; Robinhood Earn above $136M ([Maple Q3](https://maple.finance/insights/maple-q3-ecosystem-update)).
- Ethena held $304M in Maple Institutional at 30 Sep 2026, then requested redemptions on 28 Oct and 6 Nov [Tier B, Alea Q3 report]. syrupUSDC AUM fell 12% to $2.36B from 19 Oct [Tier B, TokenPost]. Two Tier B sources agree outflows are under way, so the trend is a watch item.

## 🛡️ Security & audits · 7/10 · ✅ PASS

- Audits listed on DefiLlama: [Cantina portfolio](https://cantina.xyz/portfolio/ffedd548-be82-4f0e-ad3d-9fc5a3ea00c5) and [Spearbit, Nov 2025](https://github.com/maple-labs/maple-core-v2/blob/main/audits/2025-november/Spearbit-Maple-Finance-WM-Nov-2025.pdf).
- Token controls (Tier A): `mint` and `burn` only from `isModule` addresses; modules are added only by the Governor through a **scheduled (timelocked) call** (`onlyScheduled("MT:ADD_MODULE")`). Only two modules were ever added ([2024](https://etherscan.io/tx/0xe194e692025314b8a495f1ffda39c08b07413dd2f817b95fc77ad25745b9c4de), and the 2025 one-off that was removed in the same tx).
- No exploit of the SYRUP token found. Maple v1 suffered borrower defaults in 2022 (credit losses, not a contract hack) [Unverified this pass].
- Weak spot: operational SYRUP moves through single-key EOAs (Treasury 1 and 2, `0x99f0…`, `0x6893…`).

## ⚖️ Regulatory · 5/10 · ❌ FAIL

- Maple's filing says SYRUP "does not represent equity" and buybacks are "not a dividend, distribution, profit share" ([Blockworks filing](https://blockworks.com/token-transparency/filing/maple-finance/dc60bd1d-3554-4c92-9caf-82e8fc10d4c5) · [Maple Q3](https://maple.finance/insights/maple-q3-ecosystem-update)).
- No enforcement action found, but no licence or MiCA white paper for SYRUP was checked this pass. Not proven either way.

## 📅 Catalysts & calendar · 6/10 · ✅ PASS

| Date | Event |
|---|---|
| Early each month | MIP-021 buyback for the prior month's revenue (October revenue was under the $1.5M tier) |
| ~Jan 2027 | Q4 2026 ecosystem update |
| Any time | Governance could schedule a new issuance window (rate is 0 since 1 Oct 2026) |
| Ongoing | Ethena / Sky allocator redemptions; syrupUSDG growth |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | 🔴 **Yes:** treasury-funded wallets into exchange deposits on 5 pump days, ~15.1M SYRUP. [22 Dec 2025 in](https://etherscan.io/tx/0x6a75486e7efc85e5ab5c1af22a482fafaffcb12db4bfdc083540202997a22375) → [Binance](https://etherscan.io/tx/0xf57759519928eaf0b8f3b061dffabb0e4921f869dd6d23bc46334f941ee2c2da) · [6 May 2025 → Binance](https://etherscan.io/tx/0xfb42eb9f69b491914cb011881e0defc4a66307f3442529ab70a8c55e7791de63) |
| Live mint path | 🟡 Governance only (timelocked module adds); issuance rate 0 since 1 Oct 2026. [Governor](https://etherscan.io/address/0x2efff88747eb5a3ff00d4d8d0f0800e306c0426b) |
| Treasury coins to an OTC desk | 🟡 4.6M from the SSF EOA to FalconX, Jul and Sep 2026. [29 Sep tx](https://etherscan.io/tx/0x64ef0aa34561c2984ecfb5c68cc3bee95e4cfbac3caf9d3cadbd304f5a5f0a39) |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| [Maple: Treasury 2](https://etherscan.io/address/0x9e786e5e2ffe875cdeb3bdd34f932b9baed69423) | Maple: Treasury 2 | Etherscan tag + Maple token-transparency filing | high | yes | Selling: funded pump-day exchange deposits |
| [0x6893…a6bf](https://etherscan.io/address/0x6893f4df778358e6967ef899dc440ae20f9ba6bf) | Maple-controlled EOA (receives buyback SYRUP from Binance 14) | Etherscan flows matching Maple-reported buybacks | high | yes (on-chain match to disclosed buybacks) | Selling: deposited to Binance minutes after treasury funding on pump days |
| [0x640e…b7fd](https://etherscan.io/address/0x640e8ccfd0e62e6f7da284c701746eab4cb3fb7d) | Syrup.fi (Maple Finance) | Arkham + Etherscan treasury funding | high | yes | Selling: 6 May 2025 row |
| [SSF 0x99f0…e9ca](https://etherscan.io/address/0x99f03ca02b232dc124b62b8cf40b2bfd21eae9ca) | Syrup Strategic Fund EOA | Etherscan flows + Maple buyback figures | medium | yes | Selling: FalconX sends [Unverified purpose] |

## 📚 Sources

- [Tier A] Methodology update 16 Nov 2026: no new Arkham lookups; the attribution table uses evidence already cited in this report.
- [Tier A] Etherscan v2 API `tokentx` full SYRUP history for Maple: Treasury, Treasury 1, Treasury 2, DAO, `0x58BE…`, `0x99f0…`, `0x4c3b…`, `0x3fcd…`, `0x6893…`, `0x6400…`, `0x640e…`, `0x4460…`, `0xa7cc…`, `0x9e65…`, `0xa161…`, `0x957d…`, the Migrator and every deposit address named; `getLogs` for mints, burns and module events; `getsourcecode` for the token, implementation and modules; read 16 Nov 2026 ~5:30–6:10 AM MST
- [Tier A] Ethereum RPC (publicnode): `globals()`, `governor()`, `mapleTreasury()`, `totalSupply()`, `currentIssuanceRate()`, Safe `getOwners()`/`getThreshold()`, 16 Nov 2026
- [Tier B] Etherscan name tags read from address pages, 16 Nov 2026: "Maple: Treasury", "Maple: Treasury 1", "Maple: Treasury 2", "Maple: DAO", "Maple: Governor", "Maple: Migrator", "Maple: Recapitalization Module", "Maple: Syrup Drip", "Gate Deposit", "Binance Deposit", "Binance 14", "Kraken 146", "FalconX Deposit", "FalconX 1", "GSR", "BingX 26", "Coinbase Prime 2", "Upbit Deposit"
- [Tier A] Blockscout v2: top-50 holders and holder count, 16 Nov 2026
- [Tier A] [DefiLlama Maple](https://defillama.com/protocol/maple) fees, revenue, holders revenue, TVL, 16 Nov 2026 5:27 AM MST
- [Tier A] [Maple Q3 2026 update](https://maple.finance/insights/maple-q3-ecosystem-update) · [Maple financials](https://maple.finance/transparency/financials) · [MIP-019](https://community.maple.finance/t/mip-019-activate-the-ssf-and-sunset-staking/1042) · [What SYRUP holders hold](https://maple.finance/insights/what-syrup-holders-actually-hold)
- [Tier B] [Blockworks Token Transparency filing](https://blockworks.com/token-transparency/filing/maple-finance/dc60bd1d-3554-4c92-9caf-82e8fc10d4c5) · [Alea Q3 2026 report](https://www.alearesearch.io/reports/benchmark/maple-q3-2026) · [TokenPost, 19 Oct 2026](https://www.tokenpost.com/news/business/35072) · [TokenPost, 11 Nov 2026](https://www.tokenpost.com/news/business/53791)
- [Tier B] Arkham, read 16 Nov 2026 ~7:07–7:18 AM MST (signed-in account): Syrup.fi (Maple Finance) [0x640e…](https://intel.arkm.com/explorer/address/0x640e8ccfd0e62e6f7da284c701746eab4cb3fb7d), [0x99f0…](https://intel.arkm.com/explorer/address/0x99f03ca02b232dc124b62b8cf40b2bfd21eae9ca), [0xa7cc…](https://intel.arkm.com/explorer/address/0xa7cc8d3e64ea81670181b005a476d0ca46e4c1fc), [0x3fcd…](https://intel.arkm.com/explorer/address/0x3fcdcc5bc5178c81738c176613818d9d2c7f7e1a) · Maple Team Wallet Safe [0x4c3b…](https://intel.arkm.com/explorer/address/0x4c3b453652cc3dd5d004d594e216f44d7541ea61) · predicted-only Maple [0x6893…](https://intel.arkm.com/explorer/address/0x6893f4df778358e6967ef899dc440ae20f9ba6bf) · ParaFi Capital [0xCA31…](https://intel.arkm.com/explorer/address/0xca31c9ef59a6ab45343f60968148c0ed07c39c59) · Binance Deposit [0xcf4c…](https://intel.arkm.com/explorer/address/0xcf4cc9e56e123df65e34c66925914f2815efef96) · unnamed Safes [0x5037…](https://intel.arkm.com/explorer/address/0x50371ecbbbf0ebf062da49e0cb314d1ef90dc5ae), [0x58BE…](https://intel.arkm.com/explorer/address/0x58be00490d6a5d298d61f24226d2397983ee39a1) · unlabelled [0x4460…](https://intel.arkm.com/explorer/address/0x446063e301d4a3a064b19562b0aacdc6c8f15626), [0x9e65…](https://intel.arkm.com/explorer/address/0x9e6538212ca6afccb03e05d929fe415e6621cc28). Token filter is Enterprise-only; first transfer page only
- [Tier A] CoinGecko `syrup` price and market data (16 Nov 2026 5:27 AM MST); Gate SYRUP/USDT daily candles (14 Nov 2024 – 16 Nov 2026)
- [Unverified] owner of `0xCA31…` (109M; one Tier B label: ParaFi Capital), `0x5037…`, the shared Binance deposit `0xcf4c…` cluster; purpose of the Nov 2024 Gate/Kraken transfers and the 2026 FalconX sends; whether any pump-day deposit was sold

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Arkham labels: `0x640e…`, `0x99f0…`, `0xa7cc…`, `0x3fcd…` = Syrup.fi (Maple Finance); `0x4c3b…` = Maple Team Wallet Safe; `0xCA31…` = ParaFi Capital; `0xcf4c…` = Binance deposit | [0x640e](https://intel.arkm.com/explorer/address/0x640e8ccfd0e62e6f7da284c701746eab4cb3fb7d) · [0x99f0](https://intel.arkm.com/explorer/address/0x99f03ca02b232dc124b62b8cf40b2bfd21eae9ca) · [0xa7cc](https://intel.arkm.com/explorer/address/0xa7cc8d3e64ea81670181b005a476d0ca46e4c1fc) · [0x3fcd](https://intel.arkm.com/explorer/address/0x3fcdcc5bc5178c81738c176613818d9d2c7f7e1a) · [0x4c3b](https://intel.arkm.com/explorer/address/0x4c3b453652cc3dd5d004d594e216f44d7541ea61) · [0xCA31](https://intel.arkm.com/explorer/address/0xca31c9ef59a6ab45343f60968148c0ed07c39c59) · [0xcf4c](https://intel.arkm.com/explorer/address/0xcf4cc9e56e123df65e34c66925914f2815efef96) | B | 16 Nov 2026 ~7:07–7:18 AM MST |
| Treasury 1 / Treasury 2 are Maple wallets (Etherscan tags + Maple's filing) | [Treasury 1](https://etherscan.io/address/0x6a01c16eb312b80535f4799e4bf7522b715aacff) · [Treasury 2](https://etherscan.io/address/0x9e786e5e2ffe875cdeb3bdd34f932b9baed69423) · [filing](https://blockworks.com/token-transparency/filing/maple-finance/dc60bd1d-3554-4c92-9caf-82e8fc10d4c5) | 2 × B | 16 Nov 2026 |
| `0x6893…` is Maple's: received the exact Q3 2026 buyback amounts from Binance 14 and passed them to the SSF EOA | [852,841](https://etherscan.io/tx/0x87ef10f94e37e24d7deb4ee25dc13b957219d00b1031e9046564029ec744911c) · [676,290](https://etherscan.io/tx/0x98fcb3c1b337b499d50dbe5fbd70fd95d916a4f02dc1c9fc31e4e5a265084915) · [1,371,166](https://etherscan.io/tx/0xde481457b2d08ff9a5f71a9325733b74908a975d94a34e235a4b12dfb244cc55) · [→ 0x6400](https://etherscan.io/tx/0x23df4c4dd838dbe5f85737a98bc4e4b00c170296cb2b4734779d0c7912062d24) · [→ 0x99f0](https://etherscan.io/tx/0x8ff384d50bbb2e413e0d53b67e9969ed377011149b8f956902d04f45a3c220bd) · [Maple: 2.9M bought](https://maple.finance/insights/maple-q3-ecosystem-update) | A | 16 Nov 2026 |
| 29 Oct / 10 Nov / 22 Dec 2025 pump days: 7.0M into Binance deposit `0xf0c1…` | [29 Oct in](https://etherscan.io/tx/0x5daa8c8344a45e3048298c90263e56ec857fdd5c11bd757976950278cedab9a0) · [→ Binance](https://etherscan.io/tx/0x46e35cc4e8356a9462405ca0ac862dd93e91fc71c56ef3aa64f7ff2c36b10d1d) · [10 Nov in](https://etherscan.io/tx/0x8f580b945198a7aae462a5d6ed7f8e0a57b2e854f2f0f2b88eb336763f165997) · [→ Binance](https://etherscan.io/tx/0x5e75fcd136dd5c9bb5158fc43db7fa0c4249e5fbda32e199c7a8d22a6d45fed7) · [22 Dec in](https://etherscan.io/tx/0x6a75486e7efc85e5ab5c1af22a482fafaffcb12db4bfdc083540202997a22375) · [→ Binance](https://etherscan.io/tx/0xf57759519928eaf0b8f3b061dffabb0e4921f869dd6d23bc46334f941ee2c2da) · [deposit](https://etherscan.io/address/0xf0c1445a72d3f5f9355ef846ad8bb14b2e03db47) | A + B tag | 16 Nov 2026 |
| 6 May 2025 pump day: DAO → Safe 0x4c3b → 0x640e → Binance deposit, 6.25M | [DAO → 0x4c3b](https://etherscan.io/tx/0x63e2c646a638df1d7b0e850a74f18f62a1c561760badfa72d2b6e0b349ff04ac) · [→ 0x640e](https://etherscan.io/tx/0xba1e1f0a73c51c5a61df52fe756f178b22c3bde1c4c392eb9a306b7538751419) · [→ Binance 4.25M](https://etherscan.io/tx/0xfb42eb9f69b491914cb011881e0defc4a66307f3442529ab70a8c55e7791de63) · [→ Binance 2.0M](https://etherscan.io/tx/0x001294ca4044e51513fec205a7568663deaaeb5db4f39c58764a6268afa55109) | A + B tag | 16 Nov 2026 |
| 21 Nov 2024 pump day: Treasury 1 → 0x4460 → Gate deposit | [T1 → 0x4460](https://etherscan.io/tx/0x15fa5a980bb6acab06d3a6810f4c484fee2b7015691fbcfbb049a3fc02b3d05f) · [→ Gate](https://etherscan.io/tx/0xbee48bcf5d94a0cdf0fa1fdadd975745f61aebd31c553215ea47089320371ce6) · [0x9e65 → Gate](https://etherscan.io/tx/0x714d4bd43322e027af162c0c3335fe5a5ed0235e5033d0e257a84bd8b4600621) | A + B tag | 16 Nov 2026 |
| Launch transfers: Treasury 1 → Gate 45.55M and Kraken 17.16M | [Gate](https://etherscan.io/tx/0x85adb3a725c007b7aee1c6a084c59225ef6d2a5db0c6918fb4d61d008c3ac797) · [Kraken](https://etherscan.io/tx/0xce521fbf531baa18f0747ca30c34f0ebbabfa0eb90c393e6b443367f6c021746) | A + B tag | 16 Nov 2026 |
| SSF EOA → FalconX deposit 4.6M (2026) | [9 Jul](https://etherscan.io/tx/0xcfc21703e88a5da48cbf36e6499557e538ab0af0b18517c35139a12ffc3266c4) · [29 Sep](https://etherscan.io/tx/0x64ef0aa34561c2984ecfb5c68cc3bee95e4cfbac3caf9d3cadbd304f5a5f0a39) · [deposit](https://etherscan.io/address/0x7c982ebe651ee2169aed8fcb121f36a2c6b91e63) | A + B tag | 16 Nov 2026 |
| Safe 0x58BE shares 3 of 5 signers with the DAO Safe; got 76.12M from the DAO | [0x58BE](https://etherscan.io/address/0x58BE00490D6a5D298d61f24226d2397983Ee39A1) · [DAO Safe](https://etherscan.io/address/0xd6d4bcde6c816f17889f1dd3000af0261b03a196) · [transfer](https://etherscan.io/tx/0x8fd49428373bb8376b114e15d335f14213d737e38742368385233a3555165d9a) | A | 16 Nov 2026 |
| Genesis mint and the 2025 burn-and-remint of 76.12M | [genesis](https://etherscan.io/tx/0x501a85d22af5d7e41bc3d302396be99b6fc38166be04d485daba1d0314f35a2c) · [burn/remint](https://etherscan.io/tx/0x584bbc248e5098e63024e26d601dd0fd9c092842e9d04c8ad3613cd28a2bc8fa) | A | 16 Nov 2026 |
| Issuance windows (~4–5%/yr) and rate 0 from 1 Oct 2026 | [2024 schedule](https://etherscan.io/tx/0xe194e692025314b8a495f1ffda39c08b07413dd2f817b95fc77ad25745b9c4de) · [2025 schedule](https://etherscan.io/tx/0x3c7050893d938ddd683a4b6e4e28166e14acf0571c8eeb63c367897924051937) · [module code](https://etherscan.io/address/0x5dfe0460f66fa06bfcbb3211e723556be6b3f69d#code) | A | 16 Nov 2026 |
| Mint only via timelocked Governor-added modules | [token impl code](https://etherscan.io/address/0x6ed767ebcff51533e5181f7bf818f2b9bd767aec#code) · [Governor](https://etherscan.io/address/0x2efff88747eb5a3ff00d4d8d0f0800e306c0426b#code) | A | 16 Nov 2026 |
| Revenue $14.46M (1y), buybacks $2.96M (1y) | [DefiLlama](https://defillama.com/protocol/maple) | A | 16 Nov 2026 5:27 AM MST |
| Disclosed MM loans (~2%, GSR/Keyrock/STS) | [filing](https://blockworks.com/token-transparency/filing/maple-finance/dc60bd1d-3554-4c92-9caf-82e8fc10d4c5) · [0xa161 → GSR](https://etherscan.io/tx/0x18c64dfe22ec05764c7c6d5eef4f40eb48c2a77049c29a06d3bff9e56693f644) | B + A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Arkham pass: done 16 Nov 2026** (first transfer page per wallet). Maple-labelled: `0x640e…`, `0x99f0…`, `0xa7cc…`, `0x3fcd…`, Team Wallet Safe `0x4c3b…`; `0x6893…` predicted only. `0xCA31…` = ParaFi Capital. Still unnamed: Safes `0x5037…`, `0x58BE…`; EOAs `0x4460…`, `0x9e65…` | Ask Maple to confirm `0x640e…` and `0x6893…` and who runs `0x5037…` | Free |
| 2 | **Were the five pump-day deposits market-maker loan deliveries or sales?** | Ask Maple which counterparty owns Binance deposits `0xf0c1…` and `0xcf4c…`; compare with the quarterly treasury reports | Free |
| 3 | **What were the Nov 2024 Gate (45.55M) and Kraken (17.16M) transfers for?** | Maple Q4 2024 treasury report; ask Maple | Free |
| 4 | **Why did the SSF send 4.6M SYRUP to FalconX in 2026?** | Watch for a FalconX return transfer; ask Maple whether it was a loan, custody or a sale | Free |
| 5 | **Confirm the 109M wallet `0xCA31…` belongs to ParaFi Capital** (Arkham label, one Tier B source) | A second source: ParaFi portfolio disclosure or Maple's cap table | Free |
| 6 | **New issuance window?** | Watch `WindowScheduled` events on the [Recapitalization Module](https://etherscan.io/address/0x5dfe0460f66fa06bfcbb3211e723556be6b3f69d) and Maple governance | Free |
| 7 | **Licences and entity registers** | Check the entity behind Maple Labs and the DAO Foundation on their company registers | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
