---
ticker: AERO
name: Aero (Aerodrome + Velodrome merger)
not_to_be_confused_with: "Legacy Aerodrome AERO 0x9401…8631 (pre-upgrade token, still trades)"
chain: base
contract: "0x3f5bF3EdAc59d650D8fDf9657a71F2f904A3a4Ee"
legacy_contract: "0x940181a94A35A4569E4529A3CDfB74e38FD98631"
overall_score: 6.6
overall_verdict: PASS
section_scores:
  revenue: 8
  foundation_team: 5
  insider_holdings: 6
  selling_behavior: 6
  tokenomics_supply: 5
  liquidity_market: 9
  product_development: 8
  adoption_customers: 7
  security_audits: 6
  regulatory: 5
  catalysts: 5
gates_failed: []
red_lines:
  hack_exploit: none_found
  team_sale_into_pump: not_found_12_months_traced
  migration_budget_burn_by_owner: possible_not_used
  emissions_above_revenue: borderline (~$1.9M/week minted vs ~$1.7M/week paid to stakers)
methodology_effective: 2026-11-16
revenue_reaches_holders: "yes"
revenue_mechanism: "sAERO stakers receive 100% of the exchange revenue of the pools they vote for, paid on-chain every epoch (DefiLlama holders revenue $7.3M in 30 days), so revenue reaches holders."
pump_day_price_source: "CoinGecko AERO daily closes (as published; named last resort)"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions:
  - address: "0xbde0c70bdc242577c52dfad53389f82fd149ea5a"
    label: "Aerodrome team Safe (4/7)"
    confidence: high
    independent_corroboration: true
    basis: "Basescan + team-emission receipts"
  - address: "0x22a2f7340a3fb4c7c389d91ee954766b12476721"
    label: "AerodromeMigration (verified contract)"
    confidence: high
    independent_corroboration: true
    basis: "Basescan verified source"
price_usd: 0.4427
price_source: "CoinGecko (tracks legacy contract; new-token DEX price $0.4416), 14 Nov 2026 12:12 PM MST"
chain_read_block: 57475111
last_updated: 2026-11-15
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### AERO · Overall grade **6.6 / 10 · ✅ PASS**

**Summary:** A real exchange that pays its stakers: about $7.3M of the last 30 days' fees went to sAERO holders. **Correction (15 Nov):** new supply since the merger is about 4.3M AERO (~$1.9M) a week, not $0.27M, so minting now roughly matches what stakers are paid. The team Safe's 2026 outflows are now fully traced: two locks into the vote-escrow, ~0.4M to two unknown wallets, and the migration, with no exchange sales. Weak spots: falling revenue, dilution about equal to payouts, and an owner Safe that can burn the unclaimed migration budget.

**🚨 Top warning:** No team selling found, but supply is not fixed: new AERO is being minted at roughly **10% a year**, and the migration owner Safe [`0x4225…4ce0`](https://basescan.org/address/0x42255e3c2d0b71a0b006243148fdf1a71d054ce0) (3 of 7) can `pause()` and `burnRemaining()` the 314.7M unclaimed upgrade budget in [`0x22a2…6721`](https://basescan.org/address/0x22a2f7340a3fb4c7c389d91ee954766b12476721). Team Safe [`0xbde0…ea5a`](https://basescan.org/address/0xbde0c70bdc242577c52dfad53389f82fd149ea5a) ([Arkham “Aerodrome Foundation and Incentives”](https://intel.arkm.com/explorer/address/0xbde0c70bdc242577c52dfad53389f82fd149ea5a)) has sent only **9 new AERO** since migrating.

**Sections passed: 7 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 8/10 | ✅ PASS |
| 🏛️ Foundation & team | 5/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 6/10 | ✅ PASS |
| 📉 Selling behavior | 6/10 | ✅ PASS |
| 📊 Tokenomics & supply | 5/10 | ❌ FAIL |
| 💧 Liquidity & market | 9/10 | ✅ PASS |
| 🧑‍💻 Product & development | 8/10 | ✅ PASS |
| 🤝 Adoption & customers | 7/10 | ✅ PASS |
| 🛡️ Security & audits | 6/10 | ✅ PASS |
| ⚖️ Regulatory | 5/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 5/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 AERO · Aero · 6.6 / 10 · ✅ PASS

> **One line:** A real exchange that pays its stakers: about $7.3M of the last 30 days' fees went to sAERO holders. **Correction (15 Nov):** new supply since the merger is about 4.3M AERO (~$1.9M) a week, not $0.27M, so minting now roughly matches what stakers are paid. The team Safe's 2026 outflows are now fully traced: two locks into the vote-escrow, ~0.4M to two unknown wallets, and the migration, with no exchange sales. Weak spots: falling revenue, dilution about equal to payouts, and an owner Safe that can burn the unclaimed migration budget.

⚠️ **Two tokens share the AERO ticker.** The post-merger token is `0x3f5b…a4Ee` (Base). The legacy Aerodrome token `0x9401…8631` still trades with ~$7.9M of DEX liquidity, and CoinGecko still maps "aerodrome-finance" to the legacy contract.

| 📊 Market (CoinGecko + DexScreener, 14 Nov 2026 ~12:12–12:40 PM MST) | 🔗 On-chain (Base, block 57,475,111) |
|---|---|
| **Price** $0.4427 (CoinGecko) · $0.4416 (new-token AERO/WETH pool) | **New token** `0x3f5bF3Ed…A3a4Ee` "Aero"/"AERO", 18 decimals ([Tier A] Dromos-Labs `root-base.json`) |
| **24h / 7d / 30d** 🔴 −8.2% / −26.6% / −49.9% | **Supply** 2,141,606,727 (2,127,000,000 at launch, 21 Oct) |
| **Market cap** $121.1M · **FDV** $889.2M (CoinGecko figures use the legacy contract; circulating 273.5M is not reconciled) | **Staked as sAERO** 1,076,771,313 (50.3%) in VotingEscrow [`0xBF79…3915`](https://basescan.org/address/0xBF7977E1521e9a3032bf7243Ee4712f311f13915) |
| **24h volume** $27.1M | **Unclaimed migration budget** 314,704,674 (Aerodrome) + 20,581,584 (Velodrome) |
| **ATH** $2.32 (7 Dec 2024) · now −81% | **Owner of migration** Safe [`0x4225…4ce0`](https://basescan.org/address/0x42255e3c2d0b71a0b006243148fdf1a71d054ce0), **3 of 7** |

---

## 💰 Revenue — Does it make money? · 8/10 · ✅ PASS

| Metric | Value | Source |
|---|---:|---|
| 24h fees / revenue / holders revenue | $458,470 / $392,183 / $385,711 | [Tier A] DefiLlama `aero-protocol`, pulled 14 Nov 2026 |
| 30-day fees | $9,854,446 | [Tier A] DefiLlama |
| 30-day revenue | $7,578,291 | [Tier A] DefiLlama |
| 30-day **holders revenue** (paid to stakers) | **$7,298,985** | [Tier A] DefiLlama |
| All-time fees / revenue | $615.0M / $541.7M | [Tier A] DefiLlama |
| Monthly revenue 2026 | Jun $5.15M · Jul $4.85M · Aug $4.97M · Sep $15.34M · Oct $7.86M · Nov 1–14 $3.87M | [Tier A] DefiLlama daily series |
| Official quarterly exchange revenue | Q1 2026 $20.5M · Q2 $16.4M · Q3 $25.8M · **Q4 2026 $11.3M so far, projected $21.2M** (peak Q4 2024 $111.2M) | [Tier A] aero.xyz/economics, data pulled 14 Nov 2026 07:22 UTC |
| Lifetime exchange revenue | $586M (Base $515.1M, OP Mainnet $64.9M) | [Tier A] aero.xyz/economics |
| How it reaches the token | sAERO stakers allocate AERO rewards to pools and get "a pro rata share of 100% of the exchange revenue" of those pools | [Tier A] aero.xyz/economics |
| New AERO minted since launch | **Corrected 15 Nov:** 2,127,000,000 (block 52,900,000, 21 Oct 13:29 UTC) → 2,141,606,727 (block 57,475,111, 14 Nov 19:43 UTC) = **14.61M in 24 days (~4.3M/week ≈ $1.9M/week)**. Read again 15 Nov 18:18 UTC: 2,142,465,035. Mints are thousands of small reward redemptions (mint-on-redeem). The old figure ("2,139,556,960 on 21 Oct", ~2.05M in 24 days) used block 56,435,217, which is actually **12 Nov 09:57 UTC**: Base blocks now come much faster than 2 s, so block-to-date estimates were wrong | [Tier A] Base RPC `totalSupply()` + block timestamps |
| 30-day holder revenue vs. new supply | ~$1.7M/week paid out vs. **~$1.9M/week minted** (at $0.4427) | Calculated |

- Before the merger (10 Oct 2026 read), the old Minter issued ~4.91M AERO/week, about 2.2× weekly revenue. After the merger, new supply is ~4.3M/week, only a little lower (corrected 15 Nov; the earlier "far smaller" line was based on mis-dated blocks). Rewards are "mint-on-redeem", so rewards that have been earned but not yet redeemed are not in `totalSupply`. That unredeemed amount was **not read** [Unverified].

**What it means:** Yes. The token earns real fees, and they are paid to stakers in real time. Revenue is down about 80% from the 2024 peak, and Q4 2026 is tracking below Q3.

- **Reaches holders (binary test, 16 Nov 2026 rules): Yes.** sAERO stakers receive 100% of the exchange revenue of the pools they vote for, paid on-chain every epoch (DefiLlama holders revenue $7.3M in 30 days), so revenue reaches holders.

## 🏛️ Foundation & team — Who is in charge? · 5/10 · ❌ FAIL

| Item | Finding | Source |
|---|---|---|
| Builder | Dromos Labs (Velodrome / Aerodrome team). Public repo `Dromos-Labs/metadex-public` | [Tier A] GitHub |
| Foundation | "Aero Foundation" (formerly Aerodrome Foundation). Legal entity, jurisdiction and directors **not checked** | [Unverified] |
| Migration / protocol owner | Safe [`0x42255e3c2d0b71a0b006243148fdf1a71d054ce0`](https://basescan.org/address/0x42255e3c2d0b71a0b006243148fdf1a71d054ce0), **3 of 7**. Owners: `0x9939…21ba`, `0x3cc4…3e46`, `0x0ebe…cb52`, `0x3e4e…1d4c`, `0xc6e5…9652`, `0x3c15…afe2`, `0x0aed…41ac`. `owner()` of AerodromeMigration [`0x22a2…6721`](https://basescan.org/address/0x22a2f7340a3fb4c7c389d91ee954766b12476721) | [Tier A] `getThreshold`, `getOwners`, `owner()` |
| Team-emissions Safe | [`0xbde0c70bdc242577c52dfad53389f82fd149ea5a`](https://basescan.org/address/0xbde0c70bdc242577c52dfad53389f82fd149ea5a) ([Arkham](https://intel.arkm.com/explorer/address/0xbde0c70bdc242577c52dfad53389f82fd149ea5a)), **4 of 7** (legacy Minter `team`). Shares signer `0x3cc4…3e46` with the owner Safe. Arkham: **"Aerodrome Finance: Aerodrome Foundation and Incentives"**, tagged AERO Team Wallet. Team ownership is now confirmed by the Minter `team` read (Tier A) plus Arkham | [Tier A] · [Tier B] Arkham, read 15 Nov 2026 ~11:00 AM MST (signed-in account) |
| Named individuals | Not verified this pass | [Unverified] |
| Investors | No private token sale disclosed in the sources reviewed. Base Ecosystem Fund / Coinbase involvement | [Unverified] |

**What it means:** The keys are multisigs, and they overlap. The people and the legal entity behind them were not confirmed from primary filings.

## 🪙 Foundation / team holdings — How many coins do they hold? · 6/10 · ✅ PASS

| Wallet | Role | New AERO (14 Nov) | % of supply | Locked? |
|---|---|---:|---:|---|
| [`0xbde0…ea5a`](https://basescan.org/address/0xbde0c70bdc242577c52dfad53389f82fd149ea5a) | Team Safe (4/7) | 4,064,090 | 0.19% | 🔓 liquid. Also holds 29 sAERO NFTs, **all with 0 voting power**. Arkham also shows ~$2.9M cbBTC and ~1.9M USDC in it |
| [`0x4225…4ce0`](https://basescan.org/address/0x42255e3c2d0b71a0b006243148fdf1a71d054ce0) | Owner Safe (3/7) | 0 | 0% | — |
| AerodromeMigration [`0x22a2…6721`](https://basescan.org/address/0x22a2f7340a3fb4c7c389d91ee954766b12476721) | Unclaimed 1:1 upgrade budget (owner-controlled) | 314,704,674 | 14.69% | 🔒 claimable by legacy holders; owner can `pause()` + `burnRemaining()` |
| Velodrome migration entry [`0x6daE…66c0`](https://basescan.org/address/0x6dae95fe833f190640db1176f8c8a2e50c6a66c0) | Unclaimed VELO upgrade budget | 20,581,584 | 0.96% | same |
| Splitter [`0x9Beb…1156`](https://basescan.org/address/0x9Beb95ccED809C0667bbb6577EE4066aC5cC1156) | Protocol splitter | 714,305 | 0.03% | contract |
| Aero Foundation "Momentum Fund" | Upgraded early, per hub | **Not found** (size and address not published) | — | [Unverified] |

- Allocation design: 94.5% of new AERO to Aerodrome holders and 5.5% to Velodrome, split by 52-epoch revenue ($260M vs $15M) ([Tier A] Aerodrome Foundation FAQ, 25 Nov 2025).

**What it means:** The team's visible liquid stack is small (0.19%). The big swing item is the ~335M unclaimed migration budget, which the owner Safe could burn but cannot take for itself under the published source.

## 📉 Selling behavior — Do insiders sell into pumps? · 6/10 · ✅ PASS

**Pump test:** 75 of 360 days in the last year had a ≥10% 5-day rise (CoinGecko daily closes). The last one was 15 Oct 2026.

| Window | Wallet | What the chain shows | Pump? |
|---|---|---|---|
| 22 Oct – 15 Nov 2026 (since migrating) | Team Safe `0xbde0…`, new AERO | Received 3,877,587 from AerodromeMigration and 186,512 from the Velodrome entry `0x6daE…66c0` on 22 Oct ([tx `0x0d2d9f49c1d8…`](https://basescan.org/tx/0x0d2d9f49c1d88f41248d282fb2d2dc45a90c72486800d1b0bedb5f44f7b0ff95)). Only outflow since: **9 AERO** ([tx `0xf3f857cf…`](https://basescan.org/tx/0xf3f857cf5cf194e0353f2aed719d5e4fb2750a4a804b3310299fed160a7554e8)). Balance 4,064,090 | ✅ No sale |
| 21 Oct – 14 Nov 2026 | Owner Safe `0x4225…` | 0 new AERO held throughout | ✅ No move |
| **22 Oct 2026** 19:33 UTC | Team Safe, legacy AERO | **3,877,587 → AerodromeMigration [`0x22a2…6721`](https://basescan.org/address/0x22a2f7340a3fb4c7c389d91ee954766b12476721)** ([tx `0xdbeefa2c0b7a…`](https://basescan.org/tx/0xdbeefa2c0b7a185a3e03e55a483264400b55a50007c7805002e8f4a4a0840611)), swapped 1:1 into new AERO in the same tx. Arkham shows the same send. 5-day −7.1% | ✅ Upgrade, not a sale |
| **17 Jul 2026** 15:53–16:00 UTC | Team Safe, legacy AERO | **250,000 → `0x3ca55150…b3e8`** and **150,000 → `0xaf8360d4…b7cc`**, each after a 10-AERO test. Both are plain wallets with no label; `0x3ca5…` has since emptied. 5-day −8.9% | ❌ Not a pump · receivers unknown |
| **22 Jun 2026** 19:35 UTC | Team Safe, legacy AERO | **3,220,000 → legacy VotingEscrow `0xeBf418Fe…6B4`** (tx `0x57d015fd0a5d…`), i.e. locked as veAERO. 5-day +8.5% (23 Jun was a pump day) | ✅ Lock, not a sale |
| **11 Mar 2026** 17:57 UTC | Team Safe, legacy AERO | **1,864,895 → legacy VotingEscrow** (tx `0xfc53a71b7b53…`). 5-day −14.5% | ✅ Lock, not a sale |
| 15 Nov 2025 – 23 Oct 2026, all other days | Team Safe, legacy AERO | Daily `balanceOf` reads show only rises (weekly team emissions) apart from the four dates above | ✅ |

- **How it was traced (15 Nov):** daily `balanceOf` reads on the legacy token for the team Safe from 15 Nov 2025 to 23 Oct 2026 via Base archive RPC, then each drop pinned to its block and transaction. The new token's Transfer logs since launch were read in full.
- **Correction:** the earlier "~17 Jul – ~16 Aug, 3,317,309 → 0, one pump day (8 Aug)" row was mis-dated. Base blocks now arrive much faster than 2 s, so dates estimated from block heights were wrong. The drop was the **22 Jun 3.22M lock**, and the "730,105 (~28 Apr)" balance was really the 18 Jul reading.
- **Arkham:** the Safe's only exchange activity in Arkham's window is **$1M of USDC** to a Coinbase deposit address (two 500K sends, about 19 and 6 days before the read). That is stablecoin treasury spending, not AERO. Arkham's all-time exchange view is Enterprise-locked, and the browser read only the first transfers page ([Tier B] Arkham, read 15 Nov 2026 ~11:00 AM MST (signed-in account)).
- Daily sampling could miss a same-day in-and-out, and the Momentum Fund wallet is still unpublished.

**What it means:** The team Safe sold no AERO in the last 12 months. Its outflows were two locks into the vote-escrow, the 22 Oct migration and ~0.4M (about $0.2M) to two unknown wallets on a falling day. None landed on a pump day or at an exchange. The old ~3.3M mystery is closed, so the section moves from 5 to a pass at 6. It is held at 6 because the 0.4M receivers and the Momentum Fund are unknown.

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from CoinGecko AERO daily closes (as published; named last resort).

## 📊 Tokenomics & supply · 5/10 · ❌ FAIL

| Item | Value | Source |
|---|---|---|
| New supply | 2,141,606,727 (official page: "2.14B", staked 1.08B = 50.3%, avg stake 3.93 years). Up 14.61M from 2,127,000,000 at launch in 24 days, **~4.3M/week, about 10% a year** if it continues | [Tier A] RPC + aero.xyz/economics |
| Legacy AERO supply | 2,008,099,184 (unchanged since mid-Oct 2026). Legacy VotingEscrow still holds 1,734,579,120 old AERO | [Tier A] RPC |
| Upgrade ratios | 1 AERO → 1 new AERO · 1 VELO → ~0.044 new AERO · veAERO/veVELO → sAERO | [Tier A] aero.xyz/aero-upgrade |
| Migration opened | `migrationOpen` = 1,792,620,000 → **21 Oct 2026 22:00 UTC (3:00 PM MST)** | [Tier A] migration constructor args |
| Deadline | Hub: "no set deadline". Code: owner can pause and burn what is left | [Tier A] hub + source |
| New-token powers | `mint` MINTER-only; `burn` limited to VotingEscrow / migration | [Tier A] repo `Token.sol` (deployed match **not** independently verified) |

**What it means:** Corrected 15 Nov: supply growth since launch is **not** small. About 4.3M AERO a week is being minted as rewards are redeemed, roughly 10% a year and about the same dollar value as staker payouts. Add the unredeemed rewards and the owner-controlled migration budget, and this falls to a fail (6 → 5).

## 💧 Liquidity & market · 9/10 · ✅ PASS

| Pool (Base) | Pair | Liquidity | 24h volume |
|---|---|---:|---:|
| Aero `0xc85D…c9B3` | AERO/WETH | $3,254,580 | $7,616,400 |
| Aero `0xD0Ac…6816` | AERO/USDC | $3,192,760 | $142,403 |
| Aero `0xe6A7…afA4` | AERO/cbBTC | $1,896,334 | $1,233,625 |
| Aero `0x422d…A1cF` | AERO/USDC | $790,809 | $7,116,667 |
| **All new-token pools (22)** | | **$10,266,080** | |
| Legacy AERO pools (30) | | $7,941,194 | |

- CEX: Coinbase ($7.86M 24h), Binance ($2.79M), LBank, MEXC, Bybit, Kraken. Upbit KRW/USDT/BTC markets are listed ([Tier A] Upbit API; [Tier B] CoinGecko tickers).

**What it means:** Deep and widely listed. The only problem is the two-token confusion.

## 🧑‍💻 Product & development · 8/10 · ✅ PASS

- Live on 8 chains: Base, Ethereum, Robinhood, ARC, OP Mainnet, Arbitrum, Ink and Elysium. TVL $285.34M, cumulative volume $504.95B, cumulative fees $410.83M ([Tier A] aero.xyz/economics).
- New design: Predictive Allocation (no voting, no epochs), Autopilot and Metaswaps ([Tier A] aero.xyz).
- Deployment files exist for every chain in `Dromos-Labs/metadex-public/deployment-addresses` ([Tier A] GitHub).

## 🤝 Adoption & customers · 7/10 · ✅ PASS

- Paying users are real: $9.85M of fees in 30 days ([Tier A] DefiLlama).
- TVL fell from $383.9M (10 Oct 2026) to **$285.3M** (14 Nov), down 26% ([Tier A] aero.xyz, both dates).
- Coinbase swapped legacy AERO/VELO 1-for-1 on 2–4 Nov 2026 ([Tier A] Coinbase Status, from the v2 note; not re-fetched).

## 🛡️ Security & audits · 6/10 · ✅ PASS

| Item | Finding | Source |
|---|---|---|
| Audits listed in repo | Blackthorn (2 phases), ChainSecurity (3 scopes), Riley Holterhus, GregoAI scan, Sherlock contest guide. Contents **not reviewed** | [Tier A] repo `/audits/reports` |
| Admin | Migration is Ownable + Pausable. Owner = 3-of-7 Safe. `paused()` = false today | [Tier A] |
| Incidents | Nov 2025 front-end / DNS hijack (~$700k user losses, contracts unaffected) | [Unverified] — no primary post-mortem on file |
| Token contract hack | None found | [Tier A] (absence) |

## ⚖️ Regulatory · 5/10 · ❌ FAIL

- No licence, filing or enforcement record was checked this pass. Not proven either way.

## 📅 Catalysts & calendar · 5/10 · ❌ FAIL

| Date | Event | Effect |
|---|---|---|
| Ongoing | Legacy holders can still upgrade 1:1 (~335M budget left) | Supply moves from legacy to new |
| Any time | Owner can pause and `burnRemaining()` | Shrinks supply; strands legacy holders |
| Q4 2026 | Official projection $21.2M revenue (Q3 was $25.8M) | Falling revenue |

## 🚩 Red lines status

| Red line | Status | Evidence |
|---|---|---|
| Hack / exploit on token contracts | 🟢 None found | — |
| Team sale into a pump | 🟢 Not found in 12 months (fully traced 15 Nov) | Daily balances + tx-level trace: 2 vote-escrow locks, 0.4M to 2 unknown wallets, 1 migration |
| Emissions above revenue | 🟡 Borderline (corrected 15 Nov) | ~4.3M/week (~$1.9M) minted vs ~$1.7M/week paid to stakers |
| Migration budget burned | 🟡 Possible, not used | `paused()` = false |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| [0xbde0…ea5a](https://basescan.org/address/0xbde0c70bdc242577c52dfad53389f82fd149ea5a) | Aerodrome team Safe (4/7) | Basescan + team-emission receipts | high | yes (on-chain) | Holdings and Selling: traced, no pump-day sale |
| [0x22a2…6721](https://basescan.org/address/0x22a2f7340a3fb4c7c389d91ee954766b12476721) | AerodromeMigration (verified contract) | Basescan verified source | high | yes | Holdings: unclaimed budget, not team |

## 📚 Sources

- [Tier A] Methodology update 16 Nov 2026: no new Arkham lookups; the attribution table uses evidence already cited in this report.
- [Tier A] Base RPC (`base.drpc.org`, `mainnet.base.org`, `base-rpc.publicnode.com`): `totalSupply`, `balanceOf`, Safe `getThreshold`/`getOwners`, VotingEscrow `tokenOfOwnerByIndex` / `balanceOfNFT`, migration `owner()` / `paused()`; blocks 52.3M–57,475,111, 14 Nov 2026
- [Tier A] [Dromos-Labs/metadex-public](https://github.com/Dromos-Labs/metadex-public) `deployment-addresses/root-base.json`, `migration-base.json`, V3 source
- [Tier A] [aero.xyz/economics](https://aero.xyz/economics) (data pulled 14 Nov 2026 07:22 UTC) · [aero.xyz/aero-upgrade](https://aero.xyz/aero-upgrade/)
- [Tier A] DefiLlama `aero-protocol` fees / revenue / holders revenue, 14 Nov 2026
- [Tier A] Upbit market API · [Tier B] CoinGecko market data + tickers · DexScreener pools, 14 Nov 2026
- [Tier A] Prior forensic read, 10 Oct 2026 (legacy Minter, emissions 4.91M/week)
- [Tier A] Base archive RPC (`base.drpc.org`, `base-rpc.publicnode.com`), 15 Nov 2026 ~11:30 AM MST: daily legacy-AERO `balanceOf` for the team Safe (15 Nov 2025 – 23 Oct 2026), block lookups and receipts for the four outflows, new-token Transfer logs to/from the Safe since 21 Oct, `totalSupply` with block timestamps, recent mint logs
- [Tier B] Arkham, read 15 Nov 2026 ~11:00 AM MST (signed-in account): team Safe label "Aerodrome Finance: Aerodrome Foundation and Incentives", its holdings and exchange flows; "Aerodrome Finance" entity (47.7K addresses, ~$891M; all-time exchange view Enterprise-locked)
- [Tier A] Explorer pages used (Basescan): team Safe [`0xbde0…`](https://basescan.org/address/0xbde0c70bdc242577c52dfad53389f82fd149ea5a) · owner Safe [`0x4225…`](https://basescan.org/address/0x42255e3c2d0b71a0b006243148fdf1a71d054ce0) · migration [`0x22a2…`](https://basescan.org/address/0x22a2f7340a3fb4c7c389d91ee954766b12476721) · Velodrome entry [`0x6daE…`](https://basescan.org/address/0x6dae95fe833f190640db1176f8c8a2e50c6a66c0) · VotingEscrow [`0xBF79…`](https://basescan.org/address/0xBF7977E1521e9a3032bf7243Ee4712f311f13915) · new token [`0x3f5b…`](https://basescan.org/address/0x3f5bF3EdAc59d650D8fDf9657a71F2f904A3a4Ee) · legacy token [`0x9401…`](https://basescan.org/address/0x940181a94A35A4569E4529A3CDfB74e38FD98631). Base RPC `eth_getLogs` (drpc) for the 22 Oct transfers. Hashes for the 11 Mar, 22 Jun and 17 Jul 2026 legacy sends were not re-pulled this pass (free Base log APIs refused the range); open the team Safe's token-transfer tab to see them
- [Tier B] Arkham address page used: [team Safe 0xbde0…](https://intel.arkm.com/explorer/address/0xbde0c70bdc242577c52dfad53389f82fd149ea5a)
- [Unverified] Foundation entity and directors; Momentum Fund size and address (not visible on Arkham's entity page); Nov 2025 DNS-hijack figures; owners of `0x3ca55150…` and `0xaf8360d4…` (17 Jul, 0.4M); unredeemed reward liability; deployed bytecode match to repo source

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer) or the label source (Arkham) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Team Safe `0xbde0…` is Aero's team wallet (legacy Minter `team` + Arkham "Aerodrome Foundation and Incentives") | [Basescan](https://basescan.org/address/0xbde0c70bdc242577c52dfad53389f82fd149ea5a) · [Arkham](https://intel.arkm.com/explorer/address/0xbde0c70bdc242577c52dfad53389f82fd149ea5a) | A + B | 15 Nov 2026 ~11:00 AM MST |
| 22 Oct 2026: team Safe upgraded 3,877,587 legacy AERO 1:1 via AerodromeMigration (not a sale) | [migration tx](https://basescan.org/tx/0xdbeefa2c0b7a185a3e03e55a483264400b55a50007c7805002e8f4a4a0840611) · [AerodromeMigration](https://basescan.org/address/0x22a2f7340a3fb4c7c389d91ee954766b12476721) | A | 15 Nov 2026 |
| 22 Oct 2026: 186,512 AERO from the Velodrome entry | [tx](https://basescan.org/tx/0x0d2d9f49c1d88f41248d282fb2d2dc45a90c72486800d1b0bedb5f44f7b0ff95) | A | 15 Nov 2026 |
| Only outflow of new AERO since migrating: 9 AERO | [tx](https://basescan.org/tx/0xf3f857cf5cf194e0353f2aed719d5e4fb2750a4a804b3310299fed160a7554e8) | A | 15 Nov 2026 |
| 11 Mar / 22 Jun 2026 legacy sends were veAERO locks; 17 Jul 0.4M to two unlabeled wallets | [team Safe token transfers](https://basescan.org/address/0xbde0c70bdc242577c52dfad53389f82fd149ea5a) (full tx hashes not re-pulled this pass) | A | 15 Nov 2026 |
| Migration owner Safe `0x4225…` (3/7) controls `pause()` / `burnRemaining()` on 314.7M unclaimed AERO | [owner Safe](https://basescan.org/address/0x42255e3c2d0b71a0b006243148fdf1a71d054ce0) · [migration contract](https://basescan.org/address/0x22a2f7340a3fb4c7c389d91ee954766b12476721) | A | 15 Nov 2026 |
| New-token supply 2,141,606,727 (+14.61M in 24 days, ~10%/yr pace) | [new AERO token (Basescan)](https://basescan.org/address/0x3f5bF3EdAc59d650D8fDf9657a71F2f904A3a4Ee) · [aero.xyz/economics](https://aero.xyz/economics) | A | 15 Nov 2026 |
| 1,076,771,313 AERO staked as sAERO (50.3%) | [VotingEscrow](https://basescan.org/address/0xBF7977E1521e9a3032bf7243Ee4712f311f13915) | A | 15 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Who got 0.4M legacy AERO on 17 Jul 2026** (`0x3ca55150…b3e8` 250K, `0xaf8360d4…b7cc` 150K) | Arkham / Nansen labels; trace `0x3ca5…` onward sends (it has since emptied); ask Aero whether these are contributor payments | Free / Nansen paid |
| 2 | **Momentum Fund address and size** | Aero Foundation disclosure; Arkham shows no separate wallet for it in the "Aerodrome Finance" entity | Free (request) |
| 3 | **Exact mint rate and unredeemed rewards** | Sum Transfer-from-zero logs on `0x3f5b…a4Ee` per day since 21 Oct (needs a log API that allows many results, e.g. an Etherscan v2 paid key for Base or a Dune query) and read the reward contracts' pending totals | Dune free / paid API |
| 4 | **Foundation entity and directors** | Registry search for Aero Foundation / Aerodrome Foundation | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
