---
ticker: EXA
name: Exactly Protocol
chain: optimism
contract: "0x1e925de1c68ef83bd98ee3e130ef14a50309c01b"
overall_score: 3.1
overall_verdict: FAIL
section_scores:
  revenue: 1
  foundation_team: 5
  insider_holdings: 4
  selling_behavior: 4
  tokenomics_supply: 4
  liquidity_market: 1
  product_development: 5
  adoption_customers: 3
  security_audits: 3
  regulatory: 5
  catalysts: 3
gates_failed: [revenue]
red_lines:
  hack_exploit: "yes: 18 Aug 2023 exploit; the DAO gave 1,000,000 EXA (10% of supply) to 117 affected users (EXAIP-03)"
  mint_path_live: "indirect: EXA is an upgradeable contract whose admin is the TimelockController (24h delay, 3-of-6 Safe executor), so supply rules can be changed by upgrade"
  team_wallet_to_exchange_during_pump: "no CEX deposit found (EXA has no CEX market); a team/investor Sablier-stream recipient sold ~200k EXA on DEXs, 8.9k of it on pump days in the last 12 months; Arkham shows a wallet fed by another stream recipient also selling into Velodrome pools"
  one_hop_sale_status: none_found
  treasury_selling: "DAO treasury sent 500,000 EXA to a new wallet on 18 Mar 2025, described as the Uphold deal (EXAIP-21); Arkham does not label it Uphold, so that link stays [Unverified]; that wallet staked it; no treasury DEX selling found"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "$37k a year of protocol revenue and none reaches EXA holders."
pump_day_price_source: "no exchange-native series with history (CoinGecko-era test in the body)"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions: []
price_usd: 0.06744
price_source: "CoinGecko, 16 Nov 2026 5:11 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### EXA · Overall grade **3.1 / 10 · ❌ FAIL**

**Summary:** Exactly is a fixed/variable-rate lending protocol on OP Mainnet and Base. EXA is its governance token. **The protocol keeps almost nothing:** DefiLlama shows $356.6k of fees but only **$37.2k of protocol revenue in 12 months and $0 to holders**. That fails the revenue gate. EXA trades **about $734 a day**, only on Velodrome, Aerodrome and Uniswap v4. It is −99.4% from its high and −84% in a year, and the market cap is $370k. The protocol was hacked in August 2023, and 10% of supply was given to the victims. Insiders still unlock 4.5M EXA (45% of supply) through Sablier streams until 2028.

**🚨 Top warning:** The 4.5M team/advisor/investor allocation sits in [Sablier streams](https://optimistic.etherscan.io/address/0x6f68516c21e248cddfaf4898e66b2b0adee0e0d6) (Arkham: "Sablier V2 Lockup Dynamic", 2.67M EXA, [Arkham](https://intel.arkm.com/explorer/address/0x6f68516c21e248cddfaf4898e66b2b0adee0e0d6)) funded by the [Timelock](https://optimistic.etherscan.io/address/0x92024c4bda9da602b711b9abb610d072018eb58b) ([e.g. 6 Oct 2023](https://optimistic.etherscan.io/tx/0xd30f0e2e63a067ceab967e8290a1fbb45347384ea6f68744afeafe85d0de6b2c)). **1.64M EXA has already been streamed out to 34 recipients**, and the protocol-owner Safe has pulled 5.2M back and re-issued streams. One recipient, [`0x8ed6…76e6`](https://optimistic.etherscan.io/address/0x8ed6dfe0e99aee74bb76f0b910691591de5c76e6), has sold ~200k EXA through the Velodrome pool and aggregators, including on pump days ([26 Nov 2025](https://optimistic.etherscan.io/tx/0xff50476565099331f20a62fb43e4779a40cf3aab10c158a6e854a506c3a514ad), [22 Aug 2026](https://optimistic.etherscan.io/tx/0xe6f710ab35eb416541099e29c1e8fea86827b5a0d31ae3fc830668571e933f21)). Against a ~$700-a-day market, that unlock flow is the price. Every link is in the 🔗 Evidence trail below.

**Sections passed: 0 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 1/10 | ❌ FAIL (hard gate) |
| 🏛️ Foundation & team | 5/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 4/10 | ❌ FAIL |
| 📉 Selling behavior | 4/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 4/10 | ❌ FAIL |
| 💧 Liquidity & market | 1/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 5/10 | ❌ FAIL |
| 🤝 Adoption & customers | 3/10 | ❌ FAIL |
| 🛡️ Security & audits | 3/10 | ❌ FAIL |
| ⚖️ Regulatory | 5/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 3/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 EXA · Exactly Protocol · 3.1 / 10 · ❌ FAIL

> **One line:** A working lending protocol with a near-untradeable governance token: no holder revenue, ~$700 a day of volume, a 2023 hack, and insider streams unlocking into thin DEX pools until 2028.

| 📊 Market (CoinGecko, 16 Nov 2026 5:11 AM MST) | 🔗 On-chain (OP Mainnet, 16 Nov 2026) |
|---|---|
| **Price** $0.0674 | **Contract** [`0x1e92…c01b`](https://optimistic.etherscan.io/token/0x1e925de1c68ef83bd98ee3e130ef14a50309c01b) (same address on Base) |
| **24h / 7d / 30d** 🔴 −1.8% / −40.3% / −54.6% · 1y −84.2% | **`totalSupply()` on OP** 9,762,828 EXA (max 10M; rest on Base) |
| **Market cap** $369.7k · **FDV** $674k | **Circulating (CoinGecko)** 5.48M |
| **24h volume** $734 (Velodrome, Aerodrome, Uniswap v4 only; no CEX) | **Team/investor Sablier streams** [`0x6f68…e0d6`](https://optimistic.etherscan.io/address/0x6f68516c21e248cddfaf4898e66b2b0adee0e0d6) 2.67M EXA |
| **ATH** $11.89 · now −99.4% | **Timelock (DAO treasury)** [`0x9202…8b`](https://optimistic.etherscan.io/address/0x92024c4bda9da602b711b9abb610d072018eb58b) 348k EXA · **Staking (stEXA)** [`0xCEed…752b`](https://optimistic.etherscan.io/address/0xceed2bfe740f02db6094ebe89ff93b1031be752b) 2.24M |
| **Pump days, last 365 days** 35 (CoinGecko daily prices) | **TVL** $10.9M (DefiLlama) |

---

## 💰 Revenue — Does it make money? · 1/10 · ❌ FAIL (hard gate)

| Metric | Value | Source |
|---|---:|---|
| Fees, last 12 months | **$356,573** | [Tier A] [DefiLlama fees, `exactly`](https://api.llama.fi/summary/fees/exactly?dataType=dailyFees), 16 Nov 2026 |
| Protocol revenue, last 12 months | **$37,167** | [Tier A] [DefiLlama revenue](https://api.llama.fi/summary/fees/exactly?dataType=dailyRevenue) |
| Holders revenue | **$0** | [Tier A] [DefiLlama holders revenue](https://api.llama.fi/summary/fees/exactly?dataType=dailyHoldersRevenue) |

**What it means:** Almost all interest goes to lenders. $37k a year of protocol revenue does not cover a development team, and none reaches EXA holders. **1 → hard-gate FAIL.**

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** $37k a year of protocol revenue and none reaches EXA holders.

## 🏛️ Foundation & team — Who is in charge? · 5/10 · ❌ FAIL

| Item | Finding | Source |
|---|---|---|
| Admin | `TimelockController` (24h delay) is admin of the protocol and of the upgradeable Auditor, Markets **and EXA** | [Tier A] [Exactly docs: Access control](https://docs.exact.ly/security/access-control) |
| Executor | 3-of-6 Safe ([OP owner Safe `0xC0d6…86D3`](https://optimistic.etherscan.io/address/0xc0d6bc5d052d1e74523ad79dd5a954276c9286d3); Arkham: plain Gnosis Safe Proxy, no entity, first page shows EXA going into Sablier Linear streams, [Arkham](https://intel.arkm.com/explorer/address/0xc0d6bc5d052d1e74523ad79dd5a954276c9286d3)); 2 team signers, 4 community signers, per the docs | [Tier A] same page |
| Deployer | [`0xe61B…665a`](https://optimistic.etherscan.io/address/0xe61bdef3fff4c3cf7a07996dcb8802b5c85b665a) deployed EXA and StakedEXA, and sent the full 10M to the Safe [`0x23fd…5019`](https://optimistic.etherscan.io/address/0x23fd464e0b0ee21cedeb929b19cabf9bd5215019) ([21 Jul 2023](https://optimistic.etherscan.io/tx/0xec06a6ccd0234d34e521c76f4bb1406ae0b128a121e9573734e7ebe7cdc2d7e3)), which passed [9.78M to the Timelock](https://optimistic.etherscan.io/tx/0xd8c7a7e6b0088f17a176c20d2322fe8bb2035c81614d00e3362d81f1e9fcfe66) | [Tier A] Blockscout contract-creator data |

**What it means:** Governance and the timelock are public, and community signers form a majority on the multisig. But the team can upgrade the token itself through that path, and the Safe actively manages insider streams. **5.**

## 🪙 Foundation / team holdings — How many coins do they hold? · 4/10 · ❌ FAIL

| Bucket (docs) | EXA | On-chain |
|---|---:|---|
| Community | 4.5M (45%) | Rewards, esEXA ([`0xbea5…bc18`](https://optimistic.etherscan.io/address/0xbea586a167853adddef12818f264f1f9823fbc18), 382k left), airdrop streams ([Sablier Linear](https://optimistic.etherscan.io/address/0xb923abdca17aed90eb5ec5e407bd37164f632bfd)), and 1M to hack victims |
| Team, advisors, investors | 4.5M (45%) | 48-month linear lockup from 1 Jun 2024 via Sablier. The Timelock funded [Sablier Dynamic `0x6f68…e0d6`](https://optimistic.etherscan.io/address/0x6f68516c21e248cddfaf4898e66b2b0adee0e0d6) with 4.5M, which **still holds 2.67M** (Arkham agrees: 2.668M EXA, [Arkham](https://intel.arkm.com/explorer/address/0x6f68516c21e248cddfaf4898e66b2b0adee0e0d6)) |
| DAO treasury | 1M (10%) | Timelock holds **348k**. It sent [500k on 18 Mar 2025](https://optimistic.etherscan.io/tx/0x250591d7a380baf4c2d6ece549be8b9f5385391ec8f434f550de58e52ba11a30) to [`0x598e…5344`](https://optimistic.etherscan.io/address/0x598e7fc64331f80d1fc573ded1b9f2b660c05344) (the Uphold deal under EXAIP-21, which names 1M; the wallet's owner is [Unverified], and Arkham does **not** label it Uphold, [Arkham](https://intel.arkm.com/explorer/address/0x598e7fc64331f80d1fc573ded1b9f2b660c05344)), and that wallet staked 755k in stEXA |

Source: [Tier A] [EXA tokenomics](https://docs.exact.ly/governance/exactly-token-exa/tokenomics); Blockscout holders and transfers, 16 Nov 2026.

**What it means:** The insider allocation is real and on a public schedule. But the owner Safe has pulled 5.2M EXA back out of the streams and re-funded them ([Sablier Dynamic history](https://optimistic.etherscan.io/address/0x6f68516c21e248cddfaf4898e66b2b0adee0e0d6)), and the recipient list is not published. **4.**

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL

- **No CEX:** EXA has no centralized exchange market, so "selling" means DEX swaps. None of the team/treasury wallets sent EXA to a tagged exchange.
- **Team/investor streams:** 1.64M EXA has been withdrawn by 34 stream recipients since June 2024. Top recipients:
  - [`0xfb1e…2728`](https://optimistic.etherscan.io/address/0xfb1e9918fba266797e1191597b64ed6be1ee2728) took 522k and forwarded 372k to [`0x7665…8Da9`](https://optimistic.etherscan.io/address/0x7665a96cce3049852853dcee382d8a2ad4958da9). Neither is labelled on Arkham ([0xfb1e](https://intel.arkm.com/explorer/address/0xfb1e9918fba266797e1191597b64ed6be1ee2728) · [0x7665](https://intel.arkm.com/explorer/address/0x7665a96cce3049852853dcee382d8a2ad4958da9)), but Arkham's first page for `0x7665…` shows it **selling EXA into Velodrome pools** (the EXA/WETH VolatileV2 AMM and two CL pools). Dates and amounts of those sales were not matched to pump days this pass.
  - [`0x749a…52ee`](https://optimistic.etherscan.io/address/0x749ad5e67f52e9885b33f6f6625574dddadb52ee) (a Safe) took 333k and staked it (Arkham: Gnosis Safe Proxy, no entity, [Arkham](https://intel.arkm.com/explorer/address/0x749ad5e67f52e9885b33f6f6625574dddadb52ee)).
  - **[`0x8ed6…76e6`](https://optimistic.etherscan.io/address/0x8ed6dfe0e99aee74bb76f0b910691591de5c76e6) took 311k and sold ~200k** into the [Velodrome EXA/WETH pool](https://optimistic.etherscan.io/address/0xf3c45b45223df6071a478851b9c17e0630fdf535) (99.6k), Magpie and 0x Settler. Arkham has no label for it and does not say team or investor ([Arkham](https://intel.arkm.com/explorer/address/0x8ed6dfe0e99aee74bb76f0b910691591de5c76e6)).
- **Pump days** (CoinGecko prices cover only the last 365 days; 35 pump days): `0x8ed6…` sold on [26 Nov 2025](https://optimistic.etherscan.io/tx/0xff50476565099331f20a62fb43e4779a40cf3aab10c158a6e854a506c3a514ad) (2.9k), 20 Dec 2025 (1.4k) and [22 Aug 2026](https://optimistic.etherscan.io/tx/0xe6f710ab35eb416541099e29c1e8fea86827b5a0d31ae3fc830668571e933f21) (4.6k). `0xfb1e…` sent 26k to another wallet on a pump day. Amounts are small, but so is the market.
- **Treasury:** the original Safe `0x23fd…` paid 362k EXA into a Velodrome `BribeVotingReward` contract (vote incentives, 2023–2025). No direct treasury sale was found. Arkham shows `0x23fd…` as a Gnosis Safe with no entity, now used for general Exactly positions ([Arkham](https://intel.arkm.com/explorer/address/0x23fd464e0b0ee21cedeb929b19cabf9bd5215019)).

**What it means:** No hidden CEX dumping, but stream recipients sell into a pool that trades ~$700 a day, sometimes on pump days, and the recipients aren't disclosed. Whether `0x8ed6…` is a team member or an investor is [Unverified]. **4, unchanged after the Arkham pass:** Arkham adds a second selling wallet (`0x7665…`, fed by a stream recipient) but labels none of the recipients, and its sales were not dated against pump days.

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from no exchange-native series with history (CoinGecko-era test in the body).

## 📊 Tokenomics & supply · 4/10 · ❌ FAIL

- Max 10M; 9.76M on OP (`totalSupply()` via `eth_call`), the rest bridged to Base (EXAIP-30).
- **EXA is upgradeable by the Timelock** (docs), so supply rules can change by governance upgrade.
- Insider unlocks run monthly until **June 2028** (2.67M still in the streams, about half the 5.48M circulating). Escrowed EXA rewards also release until May 2028.

## 💧 Liquidity & market · 1/10 · ❌ FAIL

- **$734 of 24h volume** on a $370k cap. The Velodrome pool holds 278k EXA; Uniswap v4 holds 68k (Blockscout holders, 16 Nov 2026).
- −40% in 7 days and −84% in a year. Any sale of a few thousand dollars moves the price.

## 🧑‍💻 Product & development · 5/10 · ❌ FAIL

- Markets live on OP Mainnet and Base, with a staking program (stEXA) and the Exa app ([contract addresses](https://docs.exact.ly/guides/smart-contract-addresses)). Development continues, but usage is small.

## 🤝 Adoption & customers · 3/10 · ❌ FAIL

- TVL **$10.9M** ([DefiLlama](https://api.llama.fi/tvl/exactly)); fees $357k a year. 3,694 EXA holders on OP (Blockscout).

## 🛡️ Security & audits · 3/10 · ❌ FAIL

- **18 Aug 2023 exploit** of the protocol. The DAO compensated **117 affected users with 1,000,000 EXA** (10% of supply) under EXAIP-03 ([tokenomics docs](https://docs.exact.ly/governance/exactly-token-exa/tokenomics)). The dollar loss (widely reported at ~$7M) is [Unverified] here.
- Mitigations now: 24h timelock, a pauser role (withdrawals stay open) and a Hypernative pauser contract ([access control](https://docs.exact.ly/security/access-control)).

## ⚖️ Regulatory · 5/10 · ❌ FAIL

- No enforcement action found. The token is DAO-governed but team-launched. Through the Uphold deal (EXAIP-21) a regulated US company is linked to the treasury; terms beyond the docs are [Unverified], and Arkham does not label the receiving wallet as Uphold ([Arkham](https://intel.arkm.com/explorer/address/0x598e7fc64331f80d1fc573ded1b9f2b660c05344)).

## 📅 Catalysts & calendar · 3/10 · ❌ FAIL

| Date | Event |
|---|---|
| Monthly to Jun 2028 | Team/investor Sablier unlocks (~94k EXA a month at a straight-line pace) |
| To May 2028 | esEXA reward releases |
| None scheduled | No dated launch found |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🔴 18 Aug 2023 exploit; 1M EXA paid to 117 victims |
| Team wallet → exchange during a pump | 🟡 No CEX; a stream recipient sold on DEXs on pump days ([tx](https://optimistic.etherscan.io/tx/0xe6f710ab35eb416541099e29c1e8fea86827b5a0d31ae3fc830668571e933f21)) |
| Live mint path | 🟡 Token upgradeable by the Timelock (3-of-6 Safe, 24h) |
| Treasury selling | 🟢 None found; 500k to the wallet described as the Uphold deal (not labelled Uphold on Arkham, [Arkham](https://intel.arkm.com/explorer/address/0x598e7fc64331f80d1fc573ded1b9f2b660c05344)) ([tx](https://optimistic.etherscan.io/tx/0x250591d7a380baf4c2d6ece549be8b9f5385391ec8f434f550de58e52ba11a30)), 362k to Velodrome vote incentives |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| Stream recipient `0x8ed6…` and `0x7665…` | Unlabelled (team or investor unverified) | Etherscan streams | low | no | None: cannot move Selling; stays 4 |

## 📚 Sources

- [Tier A] Methodology update 16 Nov 2026: no new Arkham lookups; the attribution table uses evidence already cited in this report.
- [Tier A] OP Mainnet via Blockscout API (explorer.optimism.io): EXA holders; full EXA transfers of the Timelock, owner Safe, initial Safe `0x23fd…`, Sablier Dynamic (942 rows), Sablier Linear, `0x598e…` and top stream recipients; contract names and creators; tx status for every linked tx; `totalSupply()` via OP RPC, 16 Nov 2026 ~6:00–7:00 AM MST
- [Tier A] Exactly docs: [tokenomics](https://docs.exact.ly/governance/exactly-token-exa/tokenomics) · [access control](https://docs.exact.ly/security/access-control) · [contract addresses](https://docs.exact.ly/guides/smart-contract-addresses)
- [Tier A] DefiLlama fees/revenue/holders revenue and TVL (`exactly`); CoinGecko `exactly` market data and 365 daily prices (16 Nov 2026 5:11 AM MST)
- [Tier B] Arkham, read 16 Nov 2026 ~6:53–6:54 AM MST (signed-in account): Sablier V2 Lockup Dynamic [0x6f68…](https://intel.arkm.com/explorer/address/0x6f68516c21e248cddfaf4898e66b2b0adee0e0d6) (2.668M EXA) · Gnosis Safes with no entity [0x23fd…](https://intel.arkm.com/explorer/address/0x23fd464e0b0ee21cedeb929b19cabf9bd5215019), [0xC0d6…](https://intel.arkm.com/explorer/address/0xc0d6bc5d052d1e74523ad79dd5a954276c9286d3), [0x749a…](https://intel.arkm.com/explorer/address/0x749ad5e67f52e9885b33f6f6625574dddadb52ee) · unlabelled [0x8ed6…](https://intel.arkm.com/explorer/address/0x8ed6dfe0e99aee74bb76f0b910691591de5c76e6), [0xfb1e…](https://intel.arkm.com/explorer/address/0xfb1e9918fba266797e1191597b64ed6be1ee2728), [0x7665…](https://intel.arkm.com/explorer/address/0x7665a96cce3049852853dcee382d8a2ad4958da9) (sells into Velodrome pools) · `0x598e…` not labelled Uphold [0x598e…](https://intel.arkm.com/explorer/address/0x598e7fc64331f80d1fc573ded1b9f2b660c05344). Individual ENS names shown by Arkham are not reproduced. Token filter is Enterprise-only; first transfer page only
- [Unverified] owners of stream recipients and of `0x598e…` (Uphold or not); hack dollar amount

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| 10M EXA from deployer to Safe, then 9.78M to Timelock | [mint/transfer](https://optimistic.etherscan.io/tx/0xec06a6ccd0234d34e521c76f4bb1406ae0b128a121e9573734e7ebe7cdc2d7e3) · [to Timelock](https://optimistic.etherscan.io/tx/0xd8c7a7e6b0088f17a176c20d2322fe8bb2035c81614d00e3362d81f1e9fcfe66) | A | 16 Nov 2026 |
| Timelock is admin; EXA upgradeable; 3-of-6 Safe | [access control](https://docs.exact.ly/security/access-control) · [Timelock](https://optimistic.etherscan.io/address/0x92024c4bda9da602b711b9abb610d072018eb58b) | A | 16 Nov 2026 |
| 4.5M team/investor allocation in Sablier, 48 months from Jun 2024 | [tokenomics](https://docs.exact.ly/governance/exactly-token-exa/tokenomics) · [funding tx](https://optimistic.etherscan.io/tx/0xd30f0e2e63a067ceab967e8290a1fbb45347384ea6f68744afeafe85d0de6b2c) · [streams](https://optimistic.etherscan.io/address/0x6f68516c21e248cddfaf4898e66b2b0adee0e0d6) | A | 16 Nov 2026 |
| Stream recipient sold on DEX on pump days | [26 Nov 2025](https://optimistic.etherscan.io/tx/0xff50476565099331f20a62fb43e4779a40cf3aab10c158a6e854a506c3a514ad) · [22 Aug 2026](https://optimistic.etherscan.io/tx/0xe6f710ab35eb416541099e29c1e8fea86827b5a0d31ae3fc830668571e933f21) · [wallet](https://optimistic.etherscan.io/address/0x8ed6dfe0e99aee74bb76f0b910691591de5c76e6) | A chain · identity [Unverified] | 16 Nov 2026 |
| 500k EXA from Timelock (Uphold deal) | [tx](https://optimistic.etherscan.io/tx/0x250591d7a380baf4c2d6ece549be8b9f5385391ec8f434f550de58e52ba11a30) · [tokenomics: EXAIP-21](https://docs.exact.ly/governance/exactly-token-exa/tokenomics) · Arkham: no Uphold label [Arkham](https://intel.arkm.com/explorer/address/0x598e7fc64331f80d1fc573ded1b9f2b660c05344) | A chain · recipient [Unverified] | 16 Nov 2026 |
| `0x7665…` (372k from stream recipient `0xfb1e…`) sold EXA into Velodrome pools | [Arkham](https://intel.arkm.com/explorer/address/0x7665a96cce3049852853dcee382d8a2ad4958da9) · [wallet](https://optimistic.etherscan.io/address/0x7665a96cce3049852853dcee382d8a2ad4958da9) | B · dates not matched | 16 Nov 2026 ~6:54 AM MST |
| Revenue $37.2k, holders $0 | [revenue](https://api.llama.fi/summary/fees/exactly?dataType=dailyRevenue) · [holders](https://api.llama.fi/summary/fees/exactly?dataType=dailyHoldersRevenue) | A | 16 Nov 2026 |
| 2023 hack; 1M EXA to 117 users | [tokenomics: EXAIP-03](https://docs.exact.ly/governance/exactly-token-exa/tokenomics) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Who are the 34 stream recipients (team vs investors)?** Arkham (16 Nov 2026) labels none of the ones checked | Read the Sablier stream NFTs for each; ask Exactly for the allocation list; date `0x7665…`'s Velodrome sales against pump days | Free |
| 2 | **Why did the owner Safe pull 5.2M EXA out of the streams?** | Read the Safe's Sablier `cancel`/`create` calls and the matching governance posts | Free |
| 3 | **Is `0x598e…` Uphold, and what are the deal terms?** Not labelled Uphold on Arkham | Read EXAIP-21 on the Exactly forum/Snapshot; ask Uphold or Exactly to confirm the address | Free |
| 4 | **Base-side EXA flows** | Repeat this pass on Base (Etherscan's free API does not cover Base; use Blockscout) | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.

- Research only. Not investment advice.
