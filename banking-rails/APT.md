---
ticker: APT
name: Aptos
chain: aptos
contract: "0x1::aptos_coin::AptosCoin (native)"
overall_score: 5.0
overall_verdict: FAIL
section_scores:
  revenue: 2
  foundation_team: 5
  insider_holdings: 4
  selling_behavior: 4
  tokenomics_supply: 6
  liquidity_market: 7
  product_development: 8
  adoption_customers: 6
  security_audits: 7
  regulatory: 8
  catalysts: 5
gates_failed: [revenue]
red_lines:
  hack_exploit: none
  foundation_210m_lock_proof: open_not_published
  foundation_wallets_published: open_none
  burn_below_issuance: tripped
price_usd: 0.455249
price_source: "CoinGecko, 15 Nov 2026 6:45 AM MST"
chain_read_ledger_version: 8063744811
last_updated: 2026-11-15
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### APT · Overall grade **5.0 / 10 · ❌ FAIL**

**Summary:** Fast, actively built chain that fixed its token rules in 2026 (2.1B cap vote, staking cut to 2.6%, gas up ~10×). Still, fees burn only ~11% of new issuance, the Foundation publishes no wallets and no proof of its 210M "permanent lock", and the price is down 84% in a year.

**⚠️ Top warning:** Fee burns cover only **~11% of new APT issuance**, and the Foundation's **210M "permanent lock" has no published address or contract**; its wallets (322.6M APT still locked) are unpublished, so insider selling can't be tested. Check it: [pledge (Foundation blog)](https://aptosnetwork.com/currents/aptos-tokenomics-update) · [DefiLlama fees/burn](https://defillama.com/chain/aptos) · [on-chain rewards rate](https://api.mainnet.aptoslabs.com/v1/accounts/0x1/resource/0x1::staking_config::StakingRewardsConfig) · [unlock schedule](https://defillama.com/unlocks/aptos) · [Arkham: no Foundation entity](https://intel.arkm.com/explorer/entity/aptos-foundation).

**Sections passed: 6 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 2/10 | ❌ FAIL |
| 🏛️ Foundation & team | 5/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 4/10 | ❌ FAIL |
| 📉 Selling behavior | 4/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 6/10 | ✅ PASS |
| 💧 Liquidity & market | 7/10 | ✅ PASS |
| 🧑‍💻 Product & development | 8/10 | ✅ PASS |
| 🤝 Adoption & customers | 6/10 | ✅ PASS |
| 🛡️ Security & audits | 7/10 | ✅ PASS |
| ⚖️ Regulatory | 8/10 | ✅ PASS |
| 📅 Catalysts & calendar | 5/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below. Overall fails the **Revenue gate** (2 ≤ 3).*

---


# 🪪 APT · Aptos · 5.0 / 10 · ❌ FAIL

> **One line:** Fast, actively built chain that fixed its token rules in 2026 (2.1B cap vote, staking cut to 2.6%, gas up ~10×). Still, fees burn only ~11% of new issuance, the Foundation publishes no wallets and no proof of its 210M "permanent lock", and the price is down 84% in a year.

ℹ️ **Adapted for a layer-1 with a foundation.** "Revenue" = gas fees (100% burned) set against staking issuance. "Foundation" = Aptos Foundation plus Aptos Labs, the main developer. "Holdings / Selling" = Foundation, community, investor and core-contributor allocations and their unlocks.

⚠️ **Corrections to the old (10 Nov) draft:** (1) It said "210M permanent stake on-chain (Proposal #183)". No address, contract or transaction proving the lock has been published, so this is **[Unverified]**. (2) The explorer-tagged "Foundation Wallet 1" [`0xc739…bdfd`](https://explorer.aptoslabs.com/account/0xc739507214d0e1bf9795485299d709e00024e92f7c0d055a4c2c39717882bdfd?network=mainnet) now holds **0.71 APT**, not ~17.4M.

| 📊 Market (CoinGecko, 15 Nov 2026 6:45 AM MST) | 🔗 On-chain (Aptos fullnode, ledger version 8,063,744,811, block 1,185,817,334) |
|---|---|
| **Price** $0.4552 | **Total supply** 1,211,621,565 APT ([`0x1::coin::supply`](https://api.mainnet.aptoslabs.com/v1/accounts/0x1/resource/0x1::coin::CoinInfo%3C0x1::aptos_coin::AptosCoin%3E)) |
| **24h / 7d / 30d / 1y** 🔴 −10.3% / −23.3% / −47.9% / −84.5% | **Staked** 763,960,041 APT (**63.1%**) across 82 active validators |
| **Market cap** $404.9M · **FDV** $551.8M · rank #111 | **Staking reward rate** **2.60%/yr** (on-chain [`StakingRewardsConfig`](https://api.mainnet.aptoslabs.com/v1/accounts/0x1/resource/0x1::staking_config::StakingRewardsConfig)) |
| **24h volume** $60.4M | **Min gas units per tx** 27.6 (gas schedule v53) · gas price 100 octas |
| **ATH** $19.92 (26 Jan 2023) · now −97.7% · ATL $0.4333 | **Epoch** 2 hours · epoch 18,008 |
| **1 year ago** $2.92 (16 Nov 2025 close) | **Circulating (CoinGecko)** 889.0M (73.4%) · **cap** 2.1B (governance) |

---

## 💰 Revenue — Does it make money? · 2/10 · ❌ FAIL

| Metric | Value | Source |
|---|---:|---|
| 24h fees | $3,208 | [Tier A] [DefiLlama `aptos` fees](https://defillama.com/chain/aptos), 15 Nov 2026 |
| 30-day fees | $119,589 | [Tier A] DefiLlama |
| 12-month fees | $1,228,255 | [Tier A] DefiLlama |
| All-time fees (since Oct 2022) | $5,918,045 | [Tier A] DefiLlama |
| Fees by month | Nov 25 $55.3k · Dec $40.8k · Jan $30.1k · **Feb $18.5k** · Mar $97.3k · **Apr $162.4k** · May $193.4k · Jun $148.0k · Jul $118.3k · Aug $90.1k · Sep $116.9k · Oct $134.7k · Nov 1–14 $52.8k | [Tier A] DefiLlama |
| Where fees go | **100% burned** ("All transaction or 'gas' fees, paid in the form of APT, are burned") | [Tier A] Aptos Foundation blog, 18 Feb 2026 |
| APT burned since 26 Apr 2026 (DefiLlama burn series) | $884,110 ≈ **1.24M APT** | [Tier A] DefiLlama revenue · calculated at daily closes |
| Burn pace, last 30 days | ≈179k APT → **~2.18M APT a year** | Calculated |
| New issuance | 2.60% × 763.96M staked ≈ **19.9M APT a year** | [Tier A] on-chain rewards rate × stake · calculated |
| **Burn as share of issuance** | **≈11%** → net supply still grows ~17.7M APT a year (~1.5%) | Calculated (Blockworks Research also says "~10%", [Tier B]) |
| Programmatic buyback | "exploring", not live | [Tier A] Foundation blog, 18 Feb 2026 |

**What it means:** The burn design is right, and the gas increase multiplied fee income about 8× from February to April. Still, ~$1.2M a year of fees on a ~$400M token is small, and validators are still paid mostly in new coins. The token does not earn more than it issues.

## 🏛️ Foundation & team — Who is in charge? · 5/10 · ❌ FAIL

| Item | Finding | Source |
|---|---|---|
| Aptos Foundation | Publisher of the network site and tokenomics; contact via the terms address listed on its privacy page. **Its jurisdiction and registered entity are not stated** on the privacy page read this pass | [Tier A] [aptosnetwork.com/privacy](https://aptosnetwork.com/privacy) |
| Aptos Labs | Terms of use name **"Matonee Inc., d/b/a Aptos Labs"** | [Tier A] [aptoslabs.com/terms](https://aptoslabs.com/terms) |
| Leaders | Not re-verified this pass | [Unverified] — see Open items |
| Code | `aptos-labs/aptos-core`: last push 15 Nov 2026; **435 commits in 13 weeks**; aptos-node v1.50.1 (13 Nov 2026), v1.49.8 (4 Nov) plus hotfix builds 27–29 Oct | [Tier A] GitHub API |
| Governance | On-chain proposals by staked APT. **#183 "Hard Supply Cap: 2.1 Billion APT"**, voting 26 Feb – 1 Mar 2026, **executed 9 Mar 2026**, 335,184,203 APT for vs 1,541 against (min 300M) | [Tier A] [governance.aptosfoundation.org/proposal/183](https://governance.aptosfoundation.org/proposal/183) |
| Validator concentration | 82 active validators; top 5 = 15.7% and top 10 = 27.2% of voting power; **14 validators together exceed 1/3** | [Tier A] [`0x1::stake::ValidatorSet`](https://api.mainnet.aptoslabs.com/v1/accounts/0x1/resource/0x1::stake::ValidatorSet) |
| Foundation wallet list | **Not published** | [Tier A] (absence) |

**What it means:** The code is very active and governance runs on-chain. But the Foundation does not publish its legal entity, its wallets or a treasury report, so who controls the unvested supply can't be checked.

## 🪙 Foundation / team holdings — How many coins do they hold? · 4/10 · ❌ FAIL

**Genesis allocation and unlock status** ([Tier A] [DefiLlama unlocks dataset](https://defillama.com/unlocks/aptos), documented schedule):

| Bucket | Allocation | Unlocked by 15 Nov 2026 | Still locked | Unlocked in the last 12 months | Scheduled next 12 months |
|---|---:|---:|---:|---:|---:|
| Community (Foundation-administered) | 510.2M | 282.3M | **227.9M** | 38.5M | 38.5M |
| Foundation | 165.0M | 70.3M | **94.7M** | 16.0M | 16.0M |
| Core contributors | 190.0M | 190.0M | 0 | 47.5M | **0** (ended 12 Oct 2026) |
| Investors | 134.8M | 134.8M | 0 | 33.7M | **0** (ended 12 Oct 2026) |
| Staking rewards (to date) | 211.7M | 211.7M | — | 41.1M | ~19.9M at 2.6% |
| **Still locked, Foundation + community** | | | **322.6M (26.6% of supply)** | | |

**The 210M "permanent lock":**
- Pledge: "Aptos Foundation will ensure that 210 million APT will be locked and permanently staked… never be sold or distributed" (about 37% of what it held at mainnet) ([Tier A] [Foundation blog](https://aptosnetwork.com/currents/aptos-tokenomics-update), 18 Feb 2026).
- **Proof: none published.** No address, staking contract or transaction has been named ([Tier B] TrustSwap and AMBCrypto, Oct 2026, both say so; no Foundation document found that contradicts them). → [Unverified]
- If honoured, it would leave ~113M of the 322.6M locked balance to be distributed through 2032 (Blockworks says ~125M, [Tier B]).

**Explorer-tagged wallet:** [`0xc739507214d0e1bf9795485299d709e00024e92f7c0d055a4c2c39717882bdfd`](https://explorer.aptoslabs.com/account/0xc739507214d0e1bf9795485299d709e00024e92f7c0d055a4c2c39717882bdfd?network=mainnet) ("Aptos Foundation: Wallet 1", a third-party label) holds **0.70777765 APT** and has sequence number 115 ([Tier A] fullnode). It is not a meaningful holding.

**What it means:** About a quarter of supply is still in Foundation-run buckets, and none of it can be watched on-chain because the wallets are not named. The lock pledge helps only once the Foundation proves it.

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL

**Pump test:** CoinGecko daily closes, 16 Nov 2025 – 15 Nov 2026: **39 of 360 testable days (10.8%)** were pump days. Clusters: 3–6 Jan; 14–15 Jan; 30–31 Jan; 26 Feb – 2 Mar; 17–18 Apr; 9–12 May; 22–24 Aug; 4–7 Sep; **19–26 Sep (peak +43.5%)**; last 14 Oct 2026 (+13.6%).

| Check | Finding | Source |
|---|---|---|
| Insider unlocks in the last 12 months | **135.7M APT** (contributors 47.5M + investors 33.7M + community 38.5M + Foundation 16.0M), monthly on the 12th | [Tier A] [DefiLlama unlocks](https://defillama.com/unlocks/aptos) |
| Unlock days that were pump days | **1 of 12** (12 May 2026, 5-day +10.2%) | Calculated |
| Foundation / investor wallets → exchange on pump days | **Cannot be tested.** No wallets are published | Not found |
| Tagged "Foundation Wallet 1" | No outbound sends in the prior 12-month window; balance now 0.71 APT | [Tier A] [Aptos Explorer](https://explorer.aptoslabs.com/account/0xc739507214d0e1bf9795485299d709e00024e92f7c0d055a4c2c39717882bdfd?network=mainnet) · prior 3 Nov trace |
| Old draft's "NO_PUMP_SEND" verdict | Rested on one near-empty third-party-tagged wallet, so it does not count as a pass | — |

**What it means:** About 136M APT reached insiders and the community fund during a year in which the price fell 84%. Where it went can't be seen. Under this method "not found, wallets unpublished" is a fail. It is not scored at the hard-gate level because no pump-day sale was actually found.

## 📊 Tokenomics & supply · 6/10 · ✅ PASS

| Item | Value | Source |
|---|---|---|
| Supply | 1,211,621,565 APT (1B at genesis + ~211.7M staking rewards) | [Tier A] `0x1::coin::supply` |
| Hard cap | 2.1B approved and executed (#183, 9 Mar 2026). The proposal text says "code implementation will follow". The coin's on-chain supply aggregator still shows the default u128 limit, so **where the cap is enforced in code is not confirmed** | [Tier A] governance portal · `CoinInfo<AptosCoin>` read |
| Staking rewards | **2.60%/yr**: `rewards_rate` 109501220528869 / 2⁶⁴ per 2-hour epoch × 4,380 epochs; `min_rewards_rate` is the same, so no further decay is scheduled | [Tier A] `0x1::staking_config::StakingRewardsConfig` |
| Gas | [`txn.min_transaction_gas_units`](https://api.mainnet.aptoslabs.com/v1/accounts/0x1/resource/0x1::gas_schedule::GasScheduleV2) 27,600,000 (scaling 1,000,000 → 27.6 units); fee income ~8× after March, consistent with the "10× gas" proposal | [Tier A] `GasScheduleV2` · DefiLlama · [Tier B] Blockworks (10× repricing, #185) |
| Unlock cliff | Investor and core-contributor vesting **ended 12 Oct 2026**; the scheduled flow drops from ~135.7M to ~54.5M a year | [Tier A] DefiLlama unlocks · Foundation blog ("concludes in October 2026") |
| Net inflation | ~19.9M issuance − ~2.2M burn ≈ **+17.7M APT a year (~1.5%)**, plus ~54.5M scheduled unlocks into circulation | Calculated |

## 💧 Liquidity & market · 7/10 · ✅ PASS

| Venue | Pair | 24h volume | Cost to move price +2% / −2% |
|---|---|---:|---:|
| Binance | APT/USDT | $8.69M | $51k / $178k |
| Upbit | APT/KRW | $3.87M | $36k / $65k |
| Bybit | APT/USDT | $3.54M | $56k / $74k |
| OKX | APT/USDT | $3.29M | $60k / $94k |

- Listed on Binance, Coinbase, Kraken, OKX, Bybit, Upbit, Bitvavo and 90+ others ([Tier A] CoinGecko tickers, 15 Nov 2026).
- Top-venue order books are thin for a $400M asset: about **$178k** of bids within 2% on Binance on a −10% day.
- On-chain: DEX volume $145.4M (30d), $3.73M (24h); chain DeFi TVL $38.6M ([Tier A] DefiLlama).

## 🧑‍💻 Product & development · 8/10 · ✅ PASS

- aptos-node v1.50.1 released 13 Nov 2026; 435 commits in 13 weeks on `aptos-core`; 6,439 stars ([Tier A] GitHub API).
- Throughput: **~25.8 blocks a second**; ~15.8M ledger versions in the last 24h. Net of the two system transactions per block, that is **~11.3M user transactions a day** ([Tier A] fullnode reads · calculated).
- **Decibel** (fully on-chain perps order book, incubated by Aptos Labs) went live 26 Feb 2026 ([Tier B] CoinDesk; [Tier A] Foundation blog). TVL $29.0M ([Tier A] DefiLlama).

## 🤝 Adoption & customers · 6/10 · ✅ PASS

| Metric | Value | Source |
|---|---:|---|
| Stablecoins on Aptos | $805.9M | [Tier A] DefiLlama stablecoins, 15 Nov |
| App fees on Aptos, 12 months | $18.5M | [Tier A] DefiLlama fees overview |
| Top fee earners, 30 days | BlackRock BUIDL $519k · Decibel $474k · Apollo Diversified Credit (Securitize) $153k · Aptos chain $120k · Echelon $50k | [Tier A] DefiLlama |
| Chain DeFi TVL | $38.6M | [Tier A] DefiLlama |
| User transactions | ~11.3M a day | Calculated from fullnode |

- **Confirmed by on-chain products:** BlackRock BUIDL and Apollo/Securitize funds earn fees on Aptos (DefiLlama tracks the contracts).
- "Nearly 500 active monthly developers… app revenue up 1,552% to $33.5M": the Foundation's own claim ([Tier A] blog, Feb 2026), not independently re-counted.

**What it means:** Real institutional products and steady traffic, but most of the money stays with the apps. Very little reaches APT.

## 🛡️ Security & audits · 7/10 · ✅ PASS

| Item | Finding | Source |
|---|---|---|
| Protocol hack | None found ("zero major exploits", Foundation) | [Tier A] Foundation blog (self-report) |
| Halts | No block-production halt found in 2026; a third-party status page lists none since Jan 2024 | [Unverified] one source (ChainReport) |
| Recent hotfixes | aptos-node v1.49.7 / v1.49.8 hotfix builds 27–29 Oct 2026 (reason not read) | [Tier A] GitHub releases |
| Validator spread | 14 validators exceed 1/3 of stake | [Tier A] |
| Framework audits | Not re-read this pass | Not found — see Open items |

## ⚖️ Regulatory · 8/10 · ✅ PASS

- **US:** SEC Release 33-11412 (17 Mar 2026, joined by the CFTC) names **Aptos (APT)** as a **digital commodity**, which is not a security ([Tier A] sec.gov).
- **EU:** two MiCA white-paper notifications for "Aptos Coin" (DTI FFG `C4CQCGLH2`): **Bitstamp Europe S.A.** to Luxembourg's CSSF (22 Jan 2026) and **Crypto Risk Metrics GmbH** to BaFin (29 Jan 2026) ([Tier A] ESMA interim register). Both are notifications, not approvals, and neither was filed by the Foundation.
- No US spot APT ETF trading as of Sep 2026 ([Unverified], one secondary list).

## 📅 Catalysts & calendar · 5/10 · ❌ FAIL

| Date | Event | Effect |
|---|---|---|
| 12th of each month | Community + Foundation unlocks (~4.5M APT a month) | Supply ↑ (smaller since Oct) |
| Every 2 hours | Staking rewards at 2.6%/yr (~54k APT a day) | Supply ↑ |
| Open | Proof (address or contract) of the 210M permanent lock | Would lift Holdings |
| Open | Code-level enforcement of the 2.1B cap | Would confirm Tokenomics |
| Open | "Programmatic buyback": still at the "exploring" stage | Demand, if launched |
| Open | Performance-gated grants ("more details to come") | Supply control |

**What it means:** The October unlock cliff has passed, which is good, but the remaining catalysts are promises without dates.

## 🚩 Red lines status

| Red line | Status | Evidence |
|---|---|---|
| Hack / exploit | 🟢 None found | — |
| Proof of 210M lock published | 🟡 Open — none | No address or contract named ([pledge](https://aptosnetwork.com/currents/aptos-tokenomics-update)) |
| Foundation wallets published | 🟡 Open — none | — |
| Burn ≥ issuance | 🔴 **Tripped** (burn ≈11% of issuance) | [DefiLlama burn/fees](https://defillama.com/chain/aptos) · [rewards rate](https://api.mainnet.aptoslabs.com/v1/accounts/0x1/resource/0x1::staking_config::StakingRewardsConfig) · Revenue section |

## 📚 Sources

- [Tier A] Aptos fullnode API ([`api.mainnet.aptoslabs.com/v1`](https://api.mainnet.aptoslabs.com/v1)): ledger info, `0x1::coin::supply`, `CoinInfo<AptosCoin>`, `stake::ValidatorSet`, `staking_config::StakingConfig` + `StakingRewardsConfig`, `block::BlockResource`, `gas_schedule::GasScheduleV2`, blocks by height, account [`0xc739…bdfd`](https://explorer.aptoslabs.com/account/0xc739507214d0e1bf9795485299d709e00024e92f7c0d055a4c2c39717882bdfd?network=mainnet); 15 Nov 2026 ~6:52 AM MST. Direct reads: [supply](https://api.mainnet.aptoslabs.com/v1/accounts/0x1/resource/0x1::coin::CoinInfo%3C0x1::aptos_coin::AptosCoin%3E) · [rewards config](https://api.mainnet.aptoslabs.com/v1/accounts/0x1/resource/0x1::staking_config::StakingRewardsConfig) · [validator set](https://api.mainnet.aptoslabs.com/v1/accounts/0x1/resource/0x1::stake::ValidatorSet) · [gas schedule](https://api.mainnet.aptoslabs.com/v1/accounts/0x1/resource/0x1::gas_schedule::GasScheduleV2)
- [Tier A] [Aptos Foundation tokenomics update](https://aptosnetwork.com/currents/aptos-tokenomics-update) (18 Feb 2026) · [privacy notice](https://aptosnetwork.com/privacy) · [Aptos Labs terms](https://aptoslabs.com/terms)
- [Tier A] [Aptos governance proposal #183](https://governance.aptosfoundation.org/proposal/183)
- [Tier A] DefiLlama: [fees/revenue `aptos`](https://defillama.com/chain/aptos), [unlocks dataset `aptos`](https://defillama.com/unlocks/aptos), chains TVL, stablecoins, DEX volume, fee overview, Decibel protocol; 15 Nov 2026
- [Tier A] [CoinGecko `aptos`](https://www.coingecko.com/en/coins/aptos): coin data, 365-day daily closes, tickers with depth; 15 Nov 2026 6:45 AM MST
- [Tier A] GitHub API [`aptos-labs/aptos-core`](https://github.com/aptos-labs/aptos-core)
- [Tier A] SEC Release 33-11412 · ESMA interim MiCA register `OTHER.csv` (updated 11 Nov 2026)
- [Tier B] Blockworks Research "Aptos Tokenomics: Path to Deflation" · TrustSwap and AMBCrypto (lock not proven) · CoinDesk (Decibel launch)
- [Tier B] Arkham, read 15 Nov 2026 ~11:05 AM MST (signed-in account): searched "Aptos Foundation". **No Aptos Foundation entity** ([`/explorer/entity/aptos-foundation`](https://intel.arkm.com/explorer/entity/aptos-foundation) = not found); the only "Aptos" entity ([Arkham entity “Aptos”](https://intel.arkm.com/explorer/entity/aptos)) is 3 unrelated addresses holding $14.85. Aptos is not on Arkham's supported-network list, so the Foundation and investor wallets cannot be labelled there. Open items #2 and #3 stay open
- [Unverified] 210M lock location; Foundation entity and jurisdiction; leadership; investor and contributor wallet destinations; framework audits; halt history

## 🔗 Evidence trail

*Strongest findings first. Aptos is not supported by Arkham, so most evidence is official pages and direct fullnode API reads (each link opens the live read).*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Burn ≈ 11% of issuance: ~2.18M APT/yr burned vs ~19.9M APT/yr staking issuance (2.60% × 763.96M staked) | [DefiLlama fees/burn](https://defillama.com/chain/aptos) · [StakingRewardsConfig](https://api.mainnet.aptoslabs.com/v1/accounts/0x1/resource/0x1::staking_config::StakingRewardsConfig) · [supply](https://api.mainnet.aptoslabs.com/v1/accounts/0x1/resource/0x1::coin::CoinInfo%3C0x1::aptos_coin::AptosCoin%3E) | A | 15 Nov 2026 |
| 210M "permanent lock" pledged but no address, contract or tx published | [Foundation blog, 18 Feb 2026](https://aptosnetwork.com/currents/aptos-tokenomics-update) | A (pledge) · proof Not found | 15 Nov 2026 |
| 322.6M APT still locked in Foundation + community buckets; 135.7M unlocked to insiders in the last 12 months | [DefiLlama unlocks](https://defillama.com/unlocks/aptos) | A | 15 Nov 2026 |
| Third-party-tagged "Foundation Wallet 1" holds 0.71 APT (not a meaningful holding) | [Aptos Explorer](https://explorer.aptoslabs.com/account/0xc739507214d0e1bf9795485299d709e00024e92f7c0d055a4c2c39717882bdfd?network=mainnet) | A | 15 Nov 2026 |
| Arkham has no Aptos Foundation entity and does not support Aptos | [entity search (not found)](https://intel.arkm.com/explorer/entity/aptos-foundation) · [“Aptos” entity](https://intel.arkm.com/explorer/entity/aptos) | B | 15 Nov 2026 ~11:05 AM MST |
| 2.1B hard cap approved and executed (proposal #183, 9 Mar 2026) | [Governance portal #183](https://governance.aptosfoundation.org/proposal/183) | A | 15 Nov 2026 |
| 14 validators exceed 1/3 of voting power | [ValidatorSet](https://api.mainnet.aptoslabs.com/v1/accounts/0x1/resource/0x1::stake::ValidatorSet) | A | 15 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exact path to close it | Cost / access |
|---|---|---|---|
| 1 | **Where the 210M "permanently staked" APT is**, and whether it can be withdrawn | Ask the Aptos Foundation for the stake-pool / vesting-contract addresses. Then read `0x1::stake::StakePool` (`locked_until_secs`, `operator_address`, owner capability) and any `0x1::vesting` contract at those addresses on the fullnode API. A truly permanent lock needs the owner capability destroyed or held by an immutable contract | Request to Foundation (no published channel beyond the terms contact address on aptosnetwork.com/privacy); chain reads free |
| 2 | Foundation and community-fund wallet list (322.6M still locked) | **Arkham checked 15 Nov 2026: no Aptos Foundation entity and Aptos not supported, so this stays open.** Genesis write set: fullnode `GET /v1/transactions/by_version/0`, which lists every genesis stake pool and vesting contract with owners and beneficiaries. Then map beneficiaries with `GET /v1/accounts/{addr}/resources` | Free, but heavy (large JSON); script |
| 3 | Did investors or contributors send unlocked APT to exchanges on pump days (incl. 12 May 2026)? | **Arkham checked 15 Nov 2026: Aptos not supported, so its exchange labels cannot be used here; stays open.** After #2: `GET /v1/accounts/{beneficiary}/transactions` around each 12th, plus Aptos Indexer GraphQL `fungible_asset_activities` (owner_address, amount, transaction_timestamp) matched against exchange deposit addresses | Indexer GraphQL free with rate limits (an API key from Aptos Build raises them); exchange labels need Nansen or Arkham (paid) |
| 4 | Where the 2.1B cap is enforced in code | AIP-140 text (`github.com/aptos-foundation/AIPs/blob/main/aips/aip-140.md`) and the implementing PR in `aptos-labs/aptos-core` (`aptos-move/framework/aptos-framework/sources/` — `stake.move` / `coin.move`); confirm the framework upgrade proposal that shipped it | Free |
| 5 | The 10× gas proposal number and before/after values | Governance portal proposals #184–#185; `GasScheduleV2` history from the framework git log (`aptos-move/aptos-gas-schedule`) | Free |
| 6 | Aptos Foundation legal entity and jurisdiction | Cayman Islands General Registry company search (if Cayman, as secondary sources say), or the Foundation's terms at aptosfoundation.org/terms | Cayman registry search is paid per search |
| 7 | Leadership of the Foundation and Aptos Labs | Foundation "About" page and Aptos Labs team page; for Matonee Inc., the Delaware or California SOS business search | Free |
| 8 | Framework audit list | `aptos-labs/aptos-core` repo security/audits folder or the Aptos docs security page; auditors' public report libraries (e.g. OtterSec, Zellic) | Free |
| 9 | Network halt history | Aptos status page and Aptos Labs post-mortems on the blog; cross-check block-height gaps via fullnode `/blocks/by_height` timestamps | Free |
| 10 | Whether any US spot APT ETF is filed | SEC EDGAR full-text search "Aptos" + "S-1" | Free |

**Unverified items: 10**

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
