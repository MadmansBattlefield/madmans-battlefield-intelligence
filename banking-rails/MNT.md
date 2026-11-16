---
ticker: MNT
name: Mantle
formerly: "BitDAO (BIT), migrated 1 BIT = 1 MNT in 2023"
chain: ethereum + mantle
contract: 0x3c3a81e81dc49a522a592e7622a7e711c06bf354
l2_native: 0xdeaddeaddeaddeaddeaddeaddeaddeaddead0000
overall_score: 4.5
overall_verdict: FAIL
section_scores:
  revenue: 2
  foundation_team: 4
  insider_holdings: 4
  selling_behavior: 6
  tokenomics_supply: 5
  liquidity_market: 6
  product_development: 7
  adoption_customers: 5
  security_audits: 4
  regulatory: 4
  catalysts: 5
gates_failed: [revenue]
red_lines:
  one_hop_sale_status: none_found
  hack_exploit: none_on_mantle_contracts
  treasury_sells_on_pump_days: none_found_onchain
  treasury_offchain_positions_unlisted: open
  mint_cap_enabled: "no (mintCapNumerator = 0)"
  l2_instant_upgrades_stage0: tripped
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "Fee income is tiny and no binding mechanism passes treasury or product cash to MNT holders."
pump_day_price_source: "Gate MNT_USDT UTC daily closes, re-run 16 Nov 2026 with scripts/pump_day_test.py (28 of 360 days); the body's earlier count used CoinGecko daily closes"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions: []
price_usd: 0.379084
price_source: "CoinGecko mantle, 15 Nov 2026 6:45 AM MST"
chain_read_height: 26420823
last_updated: 2026-11-15
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### MNT · Overall grade **4.5 / 10 · ❌ FAIL**

**Summary:** A large, mostly transparent treasury: $1.68B, with 2.9B MNT sitting untouched in one published multisig since Oct 2024. But the network earns about $189k a year in fees, none of it reaches MNT holders, the treasury controls 47% of supply, the token owner can switch on a 2%-a-year mint, and the L2 is Stage 0 with instant upgrades. Fails the revenue gate.

**🚨 Top warning:** The treasury controls **~47% of all MNT** (2.9B in one 3-of-7 Safe, [`0x7860…B73D`](https://etherscan.io/address/0x78605Df79524164911C144801f41e9811B7DB73D)), the token owner Safe [`0x4e59…d40f`](https://etherscan.io/address/0x4e59e778a0fb77fbb305637435c62faed9aed40f) (6 of 14) can switch on a **2%-a-year mint**, and token-holders get **none** of the ~$189k/yr in fees. The main Safe has not moved since Oct 2024. Check: [treasury Safe on Etherscan](https://etherscan.io/address/0x78605Df79524164911C144801f41e9811B7DB73D) · [MNT token contract](https://etherscan.io/address/0x3c3a81e81dc49a522a592e7622a7e711c06bf354).

**Sections passed: 3 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 2/10 | ❌ FAIL |
| 🏛️ Foundation & team | 4/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 4/10 | ❌ FAIL |
| 📉 Selling behavior | 6/10 | ✅ PASS |
| 📊 Tokenomics & supply | 5/10 | ❌ FAIL |
| 💧 Liquidity & market | 6/10 | ✅ PASS |
| 🧑‍💻 Product & development | 7/10 | ✅ PASS |
| 🤝 Adoption & customers | 5/10 | ❌ FAIL |
| 🛡️ Security & audits | 4/10 | ❌ FAIL |
| ⚖️ Regulatory | 4/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 5/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 MNT · Mantle · 4.5 / 10 · ❌ FAIL

> **One line:** A large, mostly transparent treasury: $1.68B, with 2.9B MNT sitting untouched in one published multisig since Oct 2024. But the network earns about $189k a year in fees, none of it reaches MNT holders, the treasury controls 47% of supply, the token owner can switch on a 2%-a-year mint, and the L2 is Stage 0 with instant upgrades. Fails the revenue gate.

ℹ️ **Adapted for an L2 with a DAO treasury.** "Revenue" = fees users pay on Mantle Network and anything that flows to MNT holders. "Foundation" = Mantle governance (ex-BitDAO), its operating entities and Bybit ties. "Holdings / Selling" = the Mantle Treasury's published wallets, checked against pump days.

⚠️ **Not to be confused with** MANTRA (OM) or Mantle's liquid-staking token mETH.

| 📊 Market (CoinGecko, 15 Nov 2026 6:45 AM MST) | 🔗 On-chain (Ethereum block 26,420,823 · Mantle block ~103.31M) |
|---|---|
| **Price** $0.379084 | **L1 token** [`0x3c3a81e8…f354`](https://etherscan.io/address/0x3c3a81e81dc49a522a592e7622a7e711c06bf354) · upgradeable proxy · impl. `L1MantleToken` |
| **24h / 7d / 30d** 🔴 −5.0% / −16.2% / −29.9% | **Total supply** 6,219,316,794.89 MNT |
| **Market cap** $1.256B · **FDV** $2.358B | **Treasury holdings (Mantle API)** 2,907,313,412 MNT (**46.7%**) |
| **24h volume** $43.1M (Bybit ≈ 31%) | **Main treasury Safe** [`0x78605Df7…B73D`](https://etherscan.io/address/0x78605Df79524164911C144801f41e9811B7DB73D): 2,900,022,409 MNT · **3-of-7** |
| **ATH** $2.86 (8 Oct 2025) · now **−86.7%** | **Token owner** Safe [`0x4e59e778…d40f`](https://etherscan.io/address/0x4e59e778a0fb77fbb305637435c62faed9aed40f) · **6-of-14** · can enable mint up to 2%/yr |
| **Circulating** 3,312,003,383 (Mantle API = total − treasury) | **Treasury total (Mantle site)** $1.680B · non-MNT $520.5M |

---

## 💰 Revenue — Does it make money? · 2/10 · ❌ FAIL

| Metric | Value | Source |
|---|---:|---|
| Mantle Network 24h fees | $345 | [Tier A] DefiLlama `mantle` fees, 15 Nov 2026 |
| 7-day / 30-day fees | $1,838 / $8,028 | [Tier A] DefiLlama |
| **12-month fees** | **$189,225** (revenue the same) | [Tier A] DefiLlama |
| All-time fees | $10,603,133 | [Tier A] DefiLlama |
| Where fees go | Sequencer fee vault [`0x4200…0011`](https://mantlescan.xyz/address/0x4200000000000000000000000000000000000011) (5,166 MNT now); collected by Mantle. **No burn, no buyback found** | [Tier A] docs (Protocol Related wallets) + RPC |
| mETH Protocol (Mantle product) | Revenue 30d $110,247 · 12 months $1,307,607 · TVL $440.0M | [Tier A] DefiLlama `meth-protocol` |
| Treasury non-MNT assets | ETH $214.4M · BTC $191.5M · stablecoins $111.7M · COOK $3.0M = **$520.5M** | [Tier A] [group.mantle.xyz/treasury](https://group.mantle.xyz/treasury), updated 15 Nov 2026 6:53 AM MST |
| Value to MNT holders | Past "Rewards Station" airdrops to MNT stakers: 4M ENA, 570k EIGEN (Dec 2024 – Mar 2025), 200M COOK (2024). **None listed since Mar 2025** | [Tier A] Mantle treasury page |
| Gas | MNT is the gas token on Mantle Network | [Tier A] tokenomics docs |
| 12-month fees ÷ market cap | ≈ **0.015%** | Calculated |

**What it means:** The chain's own fee income is tiny. Mantle's real economic weight is its treasury and side products (mETH, UR, MI4), and none of them has a published, binding way to pass cash to MNT holders.

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** Fee income is tiny and no binding mechanism passes treasury or product cash to MNT holders.

## 🏛️ Foundation & team — Who is in charge? · 4/10 · ❌ FAIL

| Item | Finding | Source |
|---|---|---|
| Governance | DAO votes on Snapshot `bitdao.eth`; "All Treasury actions are authorized by Governance proposals" (e.g. MIP-31 budgets, MIP-28 liquidity) | [Tier A] [docs: Treasury](https://docs.mantle.xyz/governance/parameters/treasury) |
| Legal entity | "Mantle Foundation S.A.", BVI, registered 12 Apr 2023 | [Unverified] one third-party registry mirror |
| Related entity | **MantleLSP Limited** (BVI) filed the mETH MiCA white paper with the Central Bank of Ireland, 22 May 2026 | [Tier A] ESMA interim register |
| Named staff | Tim Chen, Global Head of Strategy (quoted Aug 2025). No single CEO is named | [Tier A] Mantle blog |
| **Bybit ties** | Bybit **Co-CEO Helen Liu** and Bybit **Head of Spot Emily Bao** named "Key Advisors" (5 Aug 2025) "for deeper alignment with Bybit's scale" | [Tier A] [Mantle blog](https://group.mantle.xyz/blog/announcements/mantle-welcomes-bybit-luminaries-to-advisory-board) |
| Bybit-linked fund and BIT | Mirana (Bybit-linked) agreed to buy the FTX estate's **105,469,781 BIT** for $52.73M in the Oct 2024 FTX–Bybit settlement | [Tier B ×2] CoinDesk, Bloomberg Law · [Tier A] Kroll docket exhibit |
| Treasury signers | Main treasury Safe `0x78605Df7…`: **3 of 7** owners. Token owner Safe `0x4e59e778…`: **6 of 14**. Two addresses (`0xf5b16239…`, `0xe75d7324…`) sign both | [Tier A] Safe `getOwners`/`getThreshold` |
| Upgrade path for the token | Proxy admin owned by a **timelock with a 1-day minimum delay** ([`0x65331ff6…`](https://etherscan.io/address/0x65331ff6F8B0fc2612F2a0deBD9d04Fce60a447F)) | [Tier A] RPC `getMinDelay` = 86,400 s |
| Developer org | GitHub `mantle-xyz`: `mantle-v2` (52 commits/13 wk, v1.6.3 on 21 Sep 2026), `reth` (50 commits/13 wk, mantle-v1.6.3 on 5 Nov 2026) | [Tier A] GitHub API |

**What it means:** The treasury rules are written down and signers are on-chain multisigs. But no one is publicly accountable as the head, the legal entity is unconfirmed, and Bybit executives sit close to strategy.

## 🪙 Foundation / team holdings — How many coins do they hold? · 4/10 · ❌ FAIL

| Wallet (from Mantle docs) | Chain | MNT now | Counted as treasury by Mantle's API? | Source |
|---|---|---:|---|---|
| MTreasuryL1 [`0x78605Df79524164911C144801f41e9811B7DB73D`](https://etherscan.io/address/0x78605Df79524164911C144801f41e9811B7DB73D) | Ethereum | **2,900,022,409** | Yes | [Tier A] `balanceOf` + Blockscout |
| MTreasuryL2-FF [`0xcD9Dab9Fa5B55EE4569EdC402d3206123B1285F4`](https://mantlescan.xyz/address/0xcD9Dab9Fa5B55EE4569EdC402d3206123B1285F4) | Mantle | 5,291,001 | Yes | [Tier A] RPC |
| MTreasuryL2 [`0x94FEC56BBEcEaCC71c9e61623ACE9F8e1B1cf473`](https://mantlescan.xyz/address/0x94FEC56BBEcEaCC71c9e61623ACE9F8e1B1cf473) | Mantle | 2,000,001 | Yes | [Tier A] RPC |
| MTreasuryFB-FF (Fireblocks) [`0x61cA90679eBF73F592115b5d3ca21532059CB3fC`](https://etherscan.io/address/0x61cA90679eBF73F592115b5d3ca21532059CB3fC) | Ethereum | **34,377,131** | **No** (listed as "Primary" treasury in docs but missing from the API) | [Tier A] Blockscout |
| MBudgetL2 [`0xb9d507990c009Ed1Ee853a07B6A20c0925DD8A08`](https://mantlescan.xyz/address/0xb9d507990c009Ed1Ee853a07B6A20c0925DD8A08) | Mantle | 19,075,383 | No ("Other Holdings", counted as circulating) | [Tier A] RPC |
| **Treasury per API** | | **2,907,313,412 (46.7%)** | | [Tier A] api.mantle.xyz |
| At launch (7 Jul 2023) | | 3,046,328,614 (49.0%) | | [Tier A] tokenomics docs |

- Mantle's site values its MNT at $1,159.6M. That implies ~$0.399 a coin on 2.907B, about yesterday's price, so it matches the API. No hidden extra stack shows up.
- **Off-chain:** "We also hold assets at centralized venues for bridging, rebalancing, and flexible-yield purposes; those are not listed here." Amounts not disclosed ([Tier A] docs).
- **Inflow worth noting:** 105,000,000 MNT arrived in the main treasury on **26 Aug 2025** from `0x9deAA906…`, close to the 105.47M FTX-estate BIT bought by Mirana. Link [Unverified].

**What it means:** One governance-controlled stack holds almost half of all MNT, and its main wallet can be checked. Concentration that size, plus unlisted CEX positions, is a structural risk even when it is not selling.

## 📉 Selling behavior — Do insiders sell into pumps? · 6/10 · ✅ PASS

**Pump test:** CoinGecko daily closes, 16 Nov 2025 – 15 Nov 2026: **27 of 360 days** were pump days (7.5%): 27 Nov; 12–16 Dec 2025; 6–7 Jan; 1 Mar; 15–18 Mar (peak +24.8%); 11 May; 21–25 Aug; 3, 7–9, 19, 21–23 and 26 Sep 2026. Last pump day 26 Sep 2026.

**Every MNT outflow from published treasury and budget wallets, 12 months** ([Tier A] Blockscout ERC-20 transfers on Ethereum; Routescan internal transfers on Mantle):

| Date (UTC) | From → To | MNT | Pump day? | Tx |
|---|---|---:|:---:|---|
| — | **MTreasuryL1 [`0x78605…`](https://etherscan.io/address/0x78605Df79524164911C144801f41e9811B7DB73D): no outflow since 16 Oct 2024** (100M to MBudgetL1 [`0x1b9c…81b9`](https://etherscan.io/address/0x1b9cef6bdd029f378c511e5e6c20ee556b6781b9)) | 0 | — | — |
| 3 Dec 2025 | MBudgetL1 → Safes | 4,796,721 (2 tx) | No | [tx `0x146d0a22…f898`](https://etherscan.io/tx/0x146d0a22b8ec8877e951942133f0795e6340eb383e28a2c2af03990c9a33f898), [tx `0xe93da20a…825d`](https://etherscan.io/tx/0xe93da20a403fa02b60316f521f3cb172eb79b4d4c0c4587bfed9ea0d5416825d) |
| 21 Jan – 26 Oct 2026 | MBudgetL1 → Safes [`0xc2110F2B…`](https://etherscan.io/address/0xc2110F2BC454F73cF8f1405cEaA49261b953b0E2) / [`0x705199fE…`](https://etherscan.io/address/0x705199fE234a7A2F1Bc8B95Dd7d08284c8F467F1) | ~11.0M (11 tx) | No | e.g. [tx `0xa58860cb…8729`](https://etherscan.io/tx/0xa58860cbf0740594e08d434fb9deca12f06b8b9b0be7223ae1590b3445b88729) (3.96M, 24 Mar) |
| 3 Mar 2026 | MTreasuryL1-FF → MBudgetL1 | 10,000,000 | No | [tx `0x3b21fc43…e294`](https://etherscan.io/tx/0x3b21fc4348ad402d0c7f9828d1083ba13db48d90c5703728a345e2480442e294) (from [`L1-FF 0x34ca…`](https://etherscan.io/address/0x34cafa03d9750124102059ee35619a9c5d5af7df)) |
| 3 Mar 2026 | MTreasuryL2 → MBudgetL2 (stayed in MBudgetL2; see correction below) | 15,000,000 | No (pump day was 1 Mar) | [tx `0xd741c804…ada4`](https://mantlescan.xyz/tx/0xd741c8043ff5edc30f622614239f1f1eda13c260821f8ed3086ebbf4a04eada4) (Mantle) |
| 28 Apr 2026 | MTreasuryL1-FF → FB-FF (Fireblocks) | 24,350,357 | No | [tx `0x03beacd9…aa70`](https://etherscan.io/tx/0x03beacd9abe02610a1597fe2afa6d5200c8b55ce0e75d8119b9f6f466112aa70) |
| 21 Jul / 11 Sep 2026 | MBudgetL2 → `0x6117a8af…2d2d` | 2,009,653 / 238,961 | No | [tx `0xc90c21c0…9302`](https://mantlescan.xyz/tx/0xc90c21c0fb20b49e749cc43fa7e8b67267a34e504158347da39e0cf9e0fd9302), [tx `0xeb324a8a…ae03`](https://mantlescan.xyz/tx/0xeb324a8a6d0acb070a82e85069c67765092292083ecd1eee4e9aec784bdeae03) (Mantle) |
| 10 Nov 2026 | MTreasuryL1-RB (being retired) → FB-FF | 10,000,000 | No | [tx `0x421e5681…268b`](https://etherscan.io/tx/0x421e568120aea049185f7e3efe92baf7d80326939029afaa0edfcfb9956f268b) (from [`L1-RB 0x164c…`](https://etherscan.io/address/0x164cf077d3004bc1f26e7a46ad8fa54df4449e3f)) |

- **0 of these moves fell on a pump day.** The 2.9B main stack has not moved at all in 13 months.
- **Correction (15 Nov 2026, after an Arkham check):** the earlier draft listed [`0xfb1bffc9d739b8d520daf37df666da4c687191ea`](https://mantlescan.xyz/address/0xfb1bffc9d739b8d520daf37df666da4c687191ea) ([Arkham](https://intel.arkm.com/explorer/address/0xfb1bffc9d739b8d520daf37df666da4c687191ea)) as a recipient of 21.6M MNT. It is not a wallet. Arkham labels it "Safe: GnosisSafeL2", and on-chain it is the **shared Safe v1.3.0 L2 master contract**: 23,800 bytes of code, deployed by the Safe singleton factory `0x914d7fec…`, the same code on Ethereum and Mantle, holding 0 MNT, and every one of its 499 internal entries on Mantle is a `delegatecall` ([Tier A] Mantle RPC + Routescan chain 5000 internal txs, 15 Nov ~10:50 AM MST). Every Safe runs its code through this contract, so explorers show the Safe's incoming value "passing to" it. No MNT ever moved there:
  - 3 Mar 2026: the 15,000,000 went MTreasuryL2 → MBudgetL2 and stayed in MBudgetL2.
  - 1 Oct 2026: 291,000 MNT came **into** MTreasuryL2-FF from [`0x61af7a48…`](https://mantlescan.xyz/address/0x61af7a48b0eea8481e5a055a35f829d0e8505fe3) ([tx `0xa664c102…14e4`](https://mantlescan.xyz/tx/0xa664c1027a845cdd38d6bef56486946d15235569bbf5eb50ba767f7edab314e4)), an inflow, not an outflow.
  - 26 Oct 2026: 6,328,254 MNT came **into** MBudgetL2 from Safe [`0xa19ab990…`](https://mantlescan.xyz/address/0xa19ab9905dc9e4bcb8f982b063710a508b612434) ([tx `0x4eace766…c4e0`](https://mantlescan.xyz/tx/0x4eace766971ba59033e98430fda4540c0b172bddd642d08f59e28bdee4a7c4e0)), an inflow, not an outflow.
  - That fits MBudgetL2's live balance of 19.08M (15M + 6.33M in, 2.25M out to `0x6117a8af…`).
- Budget spending to outside wallets is therefore **~18.0M MNT over the year** (4.8M + ~11.0M from MBudgetL1 to Safes, 2.25M from MBudgetL2 to `0x6117a8af…`), not ~37M. It is governance-authorized (MIP-33, Sep 2025). Where the budget Safes send it next was not traced.
- **Blind spot:** treasury balances held at centralized exchanges and Fireblocks off-chain can't be seen. Fireblocks wallet FB-FF received 34.4M in 2026 and still holds it.

**What it means:** On everything published, the treasury does not sell into rallies. Removing the false 21.6M "recipient" lowers real outside budget spending to ~18M MNT, but it adds no new evidence about selling. It still passes only at the 6 floor (score unchanged), because CEX-held positions and the budget Safes' onward flows can't be checked.

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from Gate MNT_USDT UTC daily closes, re-run 16 Nov 2026 with scripts/pump_day_test.py (28 of 360 days); the body's earlier count used CoinGecko daily closes.

## 📊 Tokenomics & supply · 5/10 · ❌ FAIL

| Item | Value | Source |
|---|---|---|
| Total supply | 6,219,316,794.89 | [Tier A] `totalSupply()` |
| Mint | `mint()` by owner is allowed **once per 365 days, up to `mintCapNumerator`/10,000 of supply; the hard ceiling is 200/10,000 = 2%** | [Tier A] verified source `L1MantleToken` (Blockscout) |
| Mint status | `mintCapNumerator` = **0** today (no mint possible until the 6-of-14 owner Safe raises it); `nextMint` already passed (19 Jun 2024) | [Tier A] RPC |
| Upgradeability | Proxy, admin behind a **1-day timelock** | [Tier A] RPC |
| Circulating definition | Total − Treasury Holdings; budget and liquidity wallets count as circulating | [Tier A] docs |
| Unlocks | No vesting schedule; treasury MNT is released by governance proposals | [Tier A] docs |
| BIT → MNT migration | Rate 1:1. **Migrator v2 "Not Available (Halted)"**. MIP-27 (2023) blocked automatic migration of FTX Group's BIT | [Tier A] migratebit.mantle.xyz; MIP-27 forum post |
| Burn | ~3B unconverted BIT burned under MIP-23 (2023) | [Unverified] old-draft finding, not re-read |

**What it means:** No schedule-driven unlocks, but almost half of supply can be released by governance, and the token owner keeps an optional 2%-a-year mint switch plus an upgradeable contract.

## 💧 Liquidity & market · 6/10 · ✅ PASS

| Venue (CoinGecko tickers, 15 Nov 2026) | Pair | 24h volume | Bid depth to −2% |
|---|---|---:|---:|
| Bybit | MNT/USDT | $16.49M | $1,829k |
| Bybit | MNT/USDC | $0.91M | $45k |
| Coinbase Exchange | MANTLE/USD | $0.66M | $274k |
| Gate | MNT/USDT | $0.38M | $247k |
| Kraken | MNT/USD | $0.19M | $251k |
| Upbit | MNT/KRW | $0.20M | $74k |
| KuCoin | MNT/USDT | $0.04M | $133k |
| FameEX / GroveX / Zoomex / OrangeX | various | $29.8M combined | — |
| **Major-venue total −2% depth** | | | **≈ $2.85M** (64% on Bybit) |

- **Not seen** on Binance or OKX in CoinGecko's first 100 tickers.
- Mantle chain TVL $92.3M ([Tier A] DefiLlama); MNT bridged on Mantle $131.0M (L2BEAT).

**What it means:** Liquid enough, but heavily dependent on one exchange, Bybit. Much of the rest of the reported volume is on smaller venues.

## 🧑‍💻 Product & development · 7/10 · ✅ PASS

| Item | Detail | Source |
|---|---|---|
| Mantle Network | Ethereum L2. **OP Succinct ZK validity proofs since 16 Sep 2025**; **Ethereum blobs only for data since the Arsia upgrade, 16 Apr 2026** (EigenDA removed) | [Tier A] L2BEAT project page (with tx links) |
| Client | Moved to Reth; mantle-v1.6.3 (5 Nov 2026) backported an upstream Reth state-root fix; the network kept running | [Tier A] GitHub release · [Tier B] TokenPost + Tronweekly |
| Activity | `mantle-v2` 52 commits and `reth` 50 commits in 13 weeks | [Tier A] GitHub API |
| Other products | mETH (liquid staking, $440M TVL), UR neobank app, MI4 index fund, Function (fBTC) | [Tier A] Mantle treasury page / DefiLlama |
| Verification gap | Some OP-Succinct verification keys "not verified, because reproducing them currently requires a private dependency" | [Tier A] L2BEAT |

## 🤝 Adoption & customers · 5/10 · ❌ FAIL

| Item | Finding | Source |
|---|---|---|
| User transactions | ≈ **20,000/day** (460 sampled blocks: 0.48 user tx per 2-second block, after removing the 1 system tx per block) | [Tier A] RPC sample, calculated |
| Total value secured | $1.05B (−13.1% w/w); stablecoins $543M of it | [Tier A] L2BEAT |
| Stablecoins on Mantle | $526.3M | [Tier A] DefiLlama stablecoins |
| DeFi TVL | $92.3M | [Tier A] DefiLlama |
| UR neobank | Live (IBAN, Mastercard, SEPA/SWIFT); users and volume not published | [Tier A] Mantle blog (old draft) · numbers Not found |
| Halo Prime / mStocks | MIP-36 proposes recognizing Halo Prime as a strategic partner and mStocks issuer; vote through 16 Nov 2026 | [Tier B] Mantle forum + CoinMarketCal |

**What it means:** Real stablecoin balances, but light daily use, and the flagship consumer app does not publish usage.

## 🛡️ Security & audits · 4/10 · ❌ FAIL

| Item | Finding | Source |
|---|---|---|
| L2BEAT stage | **Stage 0** ZK rollup | [Tier A] L2BEAT |
| Upgrades | "There is no delay on code upgrades (CRITICAL)"; **exit window: none** | [Tier A] L2BEAT |
| Proposer | Only whitelisted proposers post state roots. If they stop, withdrawals freeze | [Tier A] L2BEAT |
| Forced inclusion | Users can force transactions via L1 with up to a 12h delay | [Tier A] L2BEAT |
| rsETH incident (20 Apr 2026) | A third-party rsETH / LayerZero configuration exploit led to ~$190M of bad borrows on Aave's Mantle market. Mantle contracts were not hacked; Mantle paused some bridge functions and discussed treasury help for recovery | [Tier A] Mantle PR Newswire release + Aave governance incident report |
| Token contract | Verified source; mint capped and currently off; 1-day upgrade timelock | [Tier A] |

**What it means:** No direct hack, but users must trust Mantle's multisigs: contracts can be upgraded instantly, and withdrawals depend on a permissioned proposer.

## ⚖️ Regulatory · 4/10 · ❌ FAIL

| Item | Finding | Source |
|---|---|---|
| US | MNT is **not** listed in SEC release 33-11412's digital-commodity examples. Mantle's own docs carry a **US-persons transfer restriction** ("shall not be reoffered, resold or transferred within the United States…") | [Tier A] SEC release; [Tier A] tokenomics docs |
| EU MiCA | Third-party white papers only: Crypto Risk Metrics via BaFin (25 Sep 2026, FFG QH1GF1J5H); LCX AG via FMA Liechtenstein (12 Sep 2025). MantleLSP Limited filed for **mETH**, not MNT | [Tier A] ESMA interim register |
| Entity transparency | BVI foundation, no published directors | [Unverified] |
| Bybit exposure | Close operational ties to an exchange that is not licensed in the US | [Tier A] Mantle blog (ties) |

## 📅 Catalysts & calendar · 5/10 · ❌ FAIL

| Date | Event | Effect |
|---|---|---|
| Through 16 Nov 2026 | MIP-36 vote (Halo Prime / mStocks) | Product / partner |
| Any time | Governance-authorized treasury releases (budget cycles: MIP-33 Sep 2025, so the next cycle is plausibly due) | Supply ↑ into circulation |
| Any time (owner Safe) | `setMintCapNumerator` up to 2%/yr, then `mint` | Supply ↑ (none signalled) |
| Open | Stage 1 requirements (exit window, Security Council) | Security upgrade |
| 8–9 Dec 2026 | FOMC meeting | Macro |

## 🚩 Red lines status

| Red line | Status | Evidence |
|---|---|---|
| Hack on Mantle contracts | 🟢 None (rsETH was third-party) | L2BEAT, Mantle release |
| Treasury sells on pump days | 🟢 None found on-chain | 0 of 12 months' published-wallet outflows on pump days ([main Safe](https://etherscan.io/address/0x78605Df79524164911C144801f41e9811B7DB73D), [MBudgetL1](https://etherscan.io/address/0x1b9cef6bdd029f378c511e5e6c20ee556b6781b9), [MBudgetL2](https://mantlescan.xyz/address/0xb9d507990c009Ed1Ee853a07B6A20c0925DD8A08)) |
| Off-chain (CEX) treasury positions unlisted | 🟡 Open | Mantle docs |
| Mint switch turned on | 🟢 No (`mintCapNumerator` = 0) | RPC read of [token contract](https://etherscan.io/address/0x3c3a81e81dc49a522a592e7622a7e711c06bf354) |
| Instant L2 upgrades / Stage 0 | 🔴 Tripped | L2BEAT |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| Mantle treasury Safes | Mantle treasury (published) | Treasury reports + chain | high | yes | None: no pump-day sale found |

## 📚 Sources

- [Tier A] Methodology update 16 Nov 2026: no new Arkham lookups; the attribution table uses evidence already cited in this report.
- [Tier A] Ethereum mainnet RPC (publicnode) + Blockscout `eth.blockscout.com` (token transfers, balances, verified `L1MantleToken` source), block ~26,420,823; Mantle RPC `rpc.mantle.xyz` and Routescan (chain 5000) normal + internal txlists; 15 Nov 2026 ~6:50–7:10 AM MST
- [Tier A] [Mantle docs: Treasury](https://docs.mantle.xyz/governance/parameters/treasury) · [Tokenomics](https://docs.mantle.xyz/governance/parameters/tokenomics) · `api.mantle.xyz/api/v1/token-data`
- [Tier A] [Mantle treasury page](https://group.mantle.xyz/treasury) (15 Nov 2026 13:53 UTC) · [Bybit advisors post](https://group.mantle.xyz/blog/announcements/mantle-welcomes-bybit-luminaries-to-advisory-board) · [migratebit.mantle.xyz](https://migratebit.mantle.xyz/) · MIP-27 forum post
- [Tier A] L2BEAT `layer2s/projects/mantle` (stage, risks, upgrade history)
- [Tier A] DefiLlama fees (`mantle`, `meth-protocol`), chain TVL, stablecoins; CoinGecko market data, tickers with depth and 365 daily closes
- [Tier A] GitHub API `mantle-xyz/mantle-v2`, `mantle-xyz/reth`
- [Tier A] ESMA interim MiCA register; SEC release 33-11412
- [Tier B] CoinDesk / Bloomberg Law (FTX–Bybit settlement); TokenPost / Tronweekly (Reth fix); Mantle forum + CoinMarketCal (MIP-36)
- [Tier A] Mantle RPC `eth_getCode` / `getThreshold` / `VERSION` and Routescan (chain 5000) normal + internal txs for `0xfb1bffc9…`; `eth_getTransactionByHash` for `0xa664c102…`; 15 Nov 2026 ~10:50 AM MST
- [Tier B] Arkham Intelligence, read 15 Nov 2026 ~10:40 AM MST (signed-in account): `0xfb1bffc9…` = "Safe: GnosisSafeL2" (contract), no exchange activity; Arkham did not show a Mantle balance
- [Tier A] Explorer pages used: Etherscan [`MTreasuryL1`](https://etherscan.io/address/0x78605Df79524164911C144801f41e9811B7DB73D) · [`MBudgetL1`](https://etherscan.io/address/0x1b9cef6bdd029f378c511e5e6c20ee556b6781b9) · [`L1-FF`](https://etherscan.io/address/0x34cafa03d9750124102059ee35619a9c5d5af7df) · [`L1-RB`](https://etherscan.io/address/0x164cf077d3004bc1f26e7a46ad8fa54df4449e3f) · [`FB-FF`](https://etherscan.io/address/0x61cA90679eBF73F592115b5d3ca21532059CB3fC) · [`owner Safe`](https://etherscan.io/address/0x4e59e778a0fb77fbb305637435c62faed9aed40f) · [`timelock`](https://etherscan.io/address/0x65331ff6F8B0fc2612F2a0deBD9d04Fce60a447F) · [`token`](https://etherscan.io/address/0x3c3a81e81dc49a522a592e7622a7e711c06bf354); Mantlescan [`MTreasuryL2`](https://mantlescan.xyz/address/0x94FEC56BBEcEaCC71c9e61623ACE9F8e1B1cf473) · [`L2-FF`](https://mantlescan.xyz/address/0xcD9Dab9Fa5B55EE4569EdC402d3206123B1285F4) · [`MBudgetL2`](https://mantlescan.xyz/address/0xb9d507990c009Ed1Ee853a07B6A20c0925DD8A08) · [`Safe L2 master 0xfb1b…`](https://mantlescan.xyz/address/0xfb1bffc9d739b8d520daf37df666da4c687191ea)
- [Tier B] Arkham address page used: [0xfb1b… “Safe: GnosisSafeL2”](https://intel.arkm.com/explorer/address/0xfb1bffc9d739b8d520daf37df666da4c687191ea)
- [Unverified] Mantle Foundation S.A. registry entry; MIP-23 burn size; link between the 105M MNT inflow and Mirana's BIT; UR usage

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer) or the label source (Arkham) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Main treasury Safe holds 2,900,022,409 MNT; no outflow since 16 Oct 2024 | [MTreasuryL1 on Etherscan](https://etherscan.io/address/0x78605Df79524164911C144801f41e9811B7DB73D) | A | 15 Nov 2026 |
| Token owner Safe (6 of 14) can enable a 2%/yr mint; proxy upgrades behind a 1-day timelock | [owner Safe](https://etherscan.io/address/0x4e59e778a0fb77fbb305637435c62faed9aed40f) · [timelock](https://etherscan.io/address/0x65331ff6F8B0fc2612F2a0deBD9d04Fce60a447F) · [token](https://etherscan.io/address/0x3c3a81e81dc49a522a592e7622a7e711c06bf354) | A | 15 Nov 2026 |
| Budget spending to outside Safes ~18.0M MNT in a year (MBudgetL1 4.8M + ~11.0M; MBudgetL2 2.25M) | [3 Dec tx 1](https://etherscan.io/tx/0x146d0a22b8ec8877e951942133f0795e6340eb383e28a2c2af03990c9a33f898) · [3 Dec tx 2](https://etherscan.io/tx/0xe93da20a403fa02b60316f521f3cb172eb79b4d4c0c4587bfed9ea0d5416825d) · [24 Mar 3.96M](https://etherscan.io/tx/0xa58860cbf0740594e08d434fb9deca12f06b8b9b0be7223ae1590b3445b88729) · [21 Jul](https://mantlescan.xyz/tx/0xc90c21c0fb20b49e749cc43fa7e8b67267a34e504158347da39e0cf9e0fd9302) · [11 Sep](https://mantlescan.xyz/tx/0xeb324a8a6d0acb070a82e85069c67765092292083ecd1eee4e9aec784bdeae03) | A | 15 Nov 2026 |
| Internal treasury moves (not sales) | [3 Mar L1-FF→MBudgetL1](https://etherscan.io/tx/0x3b21fc4348ad402d0c7f9828d1083ba13db48d90c5703728a345e2480442e294) · [3 Mar L2→MBudgetL2](https://mantlescan.xyz/tx/0xd741c8043ff5edc30f622614239f1f1eda13c260821f8ed3086ebbf4a04eada4) · [28 Apr → FB-FF](https://etherscan.io/tx/0x03beacd9abe02610a1597fe2afa6d5200c8b55ce0e75d8119b9f6f466112aa70) · [10 Nov L1-RB → FB-FF](https://etherscan.io/tx/0x421e568120aea049185f7e3efe92baf7d80326939029afaa0edfcfb9956f268b) | A | 15 Nov 2026 |
| **Correction:** `0xfb1b…` is the shared Safe L2 master contract, not a 21.6M recipient | [Mantlescan](https://mantlescan.xyz/address/0xfb1bffc9d739b8d520daf37df666da4c687191ea) · [Arkham “Safe: GnosisSafeL2”](https://intel.arkm.com/explorer/address/0xfb1bffc9d739b8d520daf37df666da4c687191ea) | A + B | 15 Nov 2026 ~10:50 AM MST |
| Inflows mistaken for outflows earlier (1 Oct 291k; 26 Oct 6.33M) | [1 Oct](https://mantlescan.xyz/tx/0xa664c1027a845cdd38d6bef56486946d15235569bbf5eb50ba767f7edab314e4) · [26 Oct](https://mantlescan.xyz/tx/0x4eace766971ba59033e98430fda4540c0b172bddd642d08f59e28bdee4a7c4e0) | A | 15 Nov 2026 |
| FB-FF (Fireblocks) holds 34.4M MNT but is missing from Mantle's treasury API | [FB-FF on Etherscan](https://etherscan.io/address/0x61cA90679eBF73F592115b5d3ca21532059CB3fC) | A | 15 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Treasury MNT held at centralized exchanges / Fireblocks off-chain** | Mantle says read-only APIs exist but won't publish them. Ask Mantle governance for a custodian attestation (forum.mantle.xyz or Mantle's official Discord). Partial check: Treasury Monitor (treasurymonitor.mantle.xyz) totals vs the on-chain sum of every listed wallet; a gap = off-chain | Free to ask; attestation needs Mantle's cooperation |
| 2 | **Where budget MNT goes next** (Safes `0xc2110F2B…`, `0x705199fE…`, `0x6117a8af…`). ✅ **`0xfb1bffc9…` closed:** it is the Safe L2 master contract, not a recipient, so no MNT went there (see 📉 correction). Also open: who sent 6.33M MNT into MBudgetL2 from Safe `0xa19ab990…` (26 Oct 2026) and 291,000 into MTreasuryL2-FF from `0x61af7a48…` (1 Oct 2026) | Trace onward with Routescan (chain 5000) `txlist`/`txlistinternal` and Blockscout token transfers on Ethereum, **ignoring `delegatecall` entries**; flag any CEX deposits on pump days | Free |
| 3 | **Why FB-FF (`0x61cA9067…`, 34.4M MNT) is missing from `api.mantle.xyz` treasuryBalance** although the docs list it as a Primary treasury wallet | Ask Mantle docs maintainers; compare with Treasury Monitor | Free |
| 4 | **Legal entity and directors** ("Mantle Foundation S.A.", BVI) | BVI Registry of Corporate Affairs (VIRRGIN) search: confirms the name, number and status; directors are not public. Check Mantle's terms of service page for the contracting entity | Small BVI search fee |
| 5 | **Link between the 105,000,000 MNT inflow (26 Aug 2025, from `0x9deAA906…`) and Mirana's 105.47M FTX-estate BIT** | Read the FTX–Bybit settlement exhibit on the Kroll FTX docket (restructuring.ra.kroll.com/FTX); trace `0x9deAA906…`'s funding on Etherscan/Blockscout back to BIT migrator calls | Free |
| 6 | **MIP-23 BIT burn size** | MIP-23 text on Snapshot `bitdao.eth` / forum archive; BIT token (`0x1A4b46696b2bB4794Eb3D4c26f1c55F9170fa4C5`) burn events on Blockscout | Free |
| 7 | **UR neobank users and volume** | Ask Mantle / UR for published metrics; UR's Swiss-regulated partner disclosures. Nothing on-chain separates UR flows | Request to team |
| 8 | **Timelock proposers/executors** behind the token's 1-day upgrade delay (`0x65331ff6…`) | Read `hasRole(PROPOSER_ROLE, …)` / RoleGranted events on Blockscout for that contract | Free |
| 9 | **Bybit's own MNT holdings** | Bybit proof-of-reserves page (lists user-asset reserves by token, not Bybit's corporate holdings); corporate holdings Not available without disclosure | Free (partial) |
| 10 | **MIP-36 outcome and next budget cycle** | Snapshot space `bitdao.eth` results after 16 Nov 2026 | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
