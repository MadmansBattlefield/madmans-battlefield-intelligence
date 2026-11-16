---
ticker: ZBCN
name: Zebec Network
chain: solana
mint: ZBCNpuD7YMXzTHB2fhGkGi78MNsHGLRXUhRewNRm9RU
overall_score: 4.0
overall_verdict: FAIL
section_scores:
  revenue: 4
  foundation_team: 3
  insider_holdings: 4
  selling_behavior: 1
  tokenomics_supply: 6
  liquidity_market: 7
  product_development: 5
  adoption_customers: 6
  security_audits: 3
  regulatory: 3
  catalysts: 4
gates_failed: [selling_behavior]
red_lines:
  one_hop_sale_status: proven
  hack_exploit: none_on_file
  buybacks_sold_rather_than_held: cannot_be_ruled_out
  treasury_funded_wallets_sell_into_pumps: tripped_30_Sep_4_Oct_2026
  founder_leadership_change: founder_dropped_from_team_page_role_unverified
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "The buyback (~$100k a quarter) is a company decision, is not automatic on-chain, and the bought ZBCN is held, not burned. No fee share or fee-funded staking yield. Holders have no live claim on revenue; the score describes the business, not holder accrual."
pump_day_price_source: "Gate ZBCN_USDT UTC daily closes, re-run 16 Nov 2026 with scripts/pump_day_test.py (48 of 360 days); the body's earlier count used CoinGecko daily closes"
pump_day_disclosure_quality: silence
pump_day_undisclosed_penalty_applied: true
dual_review: not_run
attributions: []
price_usd: 0.0017262
price_source: "CoinGecko, 14 Nov 2026 9:08 AM MST"
last_updated: 2026-11-15
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### ZBCN · Overall grade **4.0 / 10 · ❌ FAIL**

**Summary:** Real payment products (cards, stablecoin payroll) with self-reported volume, but payments run in USDC, buybacks are tiny and parked on an exchange, the issuer entity is undisclosed, and one plain key can upgrade the core programs. New on-chain tracing shows ZBCN from the published treasury cluster split through fresh wallets and sold into DEX pools and sent to exchange-scale wallets on the 30 Sep – 4 Oct 2026 pump days, which trips the Selling gate.

> ⚠️ **Top warning:** ZBCN from Zebec's published treasury hub [`9Sq2…`](https://solscan.io/account/9Sq2nZ481aiEkoDB9gavcfD6v7pr4LEcPnUdky4TEine) and program vaults went via [`71LxiE4P…`](https://solscan.io/account/71LxiE4PvxdZxLmtGcoKAJEWKofPqYw5Wdn6PSpXHodV) → [`EsDV3m3x…`](https://solscan.io/account/EsDV3m3xUZ7g8QKa1kFdbZT18nNz8ddGJRcTK84WDQ7k) ([tx: 333.3M on 30 Sep](https://solscan.io/tx/4HbiXD2wPnmWd8xz7KzoDuhfezbpikN1scNPQoXEgWUDf3v1ZwVK7vDF6SzBa5fVXBCsZ6rx9iXA9HmzPvXsz1m), [tx: 62.5M on 4 Oct](https://solscan.io/tx/3frtonWRYHyLMmw46Bv7mei6R7eEDZLMeMc6Z4GKXpLQoJUFQqbCQ65wmSq9iboyoyqGxg9x8sx4xCRyaC1LFHPm)) to fresh wallets that sold into **DEX pools on the 1 Oct pump** ([tx: swap](https://solscan.io/tx/3NGf2C9JaZhkjrjzGc7KZkMgS5x3mEv8X9xStCmrJ5QHXQA4BCzrYDLQDAh83cwk2dWdmX5hHaENLnjLRuVrjA3p), [tx: swap](https://solscan.io/tx/3fxRyAcu5d196XgwZhUEem2FQ7NNMN9xtEoyvsS6TcoFSDXoRB1HBBKQq9A7VrCWSHggJVJYPFs3jXRZcsSHqiPc)) and paid **exchange-scale wallets** [`u6PJ8DtQ…`](https://solscan.io/account/u6PJ8DtQuPFnfmwHbGFULQ4u4EgjDiyYKjVEsynXq2w) and [`A77HErqt…`](https://solscan.io/account/A77HErqtfN1hLLpvZ9pCtu66FEtM8BveoaKbbMoZ4RiR) — wallets undisclosed. The hub also pays an [Arkham-labelled Gate deposit](https://intel.arkm.com/explorer/address/ACjqBWqMhcbDTbnWitdFohrJebHmSA7tmX23Awt7n54e) twice a month ([tx: 1 Oct](https://solscan.io/tx/mTGdw8d3HVX46WbdZchqB3KxHPf7ZqQW4nCeKMcaN4s3MKuuSzwKooARg1awuSv1waRdjuT4p1sQRenUvHqZou2)).

**Sections passed: 3 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 4/10 | ❌ FAIL |
| 🏛️ Foundation & team | 3/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 4/10 | ❌ FAIL |
| 📉 Selling behavior | 1/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 6/10 | ✅ PASS |
| 💧 Liquidity & market | 7/10 | ✅ PASS |
| 🧑‍💻 Product & development | 5/10 | ❌ FAIL |
| 🤝 Adoption & customers | 6/10 | ✅ PASS |
| 🛡️ Security & audits | 3/10 | ❌ FAIL |
| ⚖️ Regulatory | 3/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 4/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 ZBCN · Zebec Network · 4.0 / 10 · ❌ FAIL

> **One line:** Real payment products (cards, stablecoin payroll) with self-reported volume, but payments run in USDC, buybacks are tiny and parked on an exchange, the issuer entity is undisclosed, and one plain key can upgrade the core programs. New on-chain tracing shows ZBCN from the published treasury cluster split through fresh wallets and sold into DEX pools and sent to exchange-scale wallets on the 30 Sep – 4 Oct 2026 pump days, which trips the Selling gate.

| 📊 Market (CoinGecko, 14 Nov 2026 9:08 AM MST) | 🔗 On-chain (Solana RPC census, 10 Oct / 3 Nov 2026) |
|---|---|
| **Price** $0.0017262 | **Mint** `ZBCNpuD7…NRm9RU` (SPL, 6 dp) |
| **24h / 7d / 30d** 🔴 −6.0% / −6.1% / −19.8% | **Supply** 99,998,768,429 · mint + freeze **revoked** |
| **Market cap = FDV** $172.6M (fully unlocked) | **Top 10 / 20 / 100 wallets** 53.7% / 60.2% / 71.9% |
| **24h volume** $8.43M | **Nonzero wallets** ~110,967 |
| **ATH** $0.0070 (29 May 2025) · now −75% | **Largest holder** Uphold wallet `5rhms…r5rHb` 20.358B (20.4%) |
| **Final unlock** Mar 2026 (per Zebec) | **Program upgrade keys** single plain wallets (not multisig) |

---

## 💰 Revenue — Does it make money? · 4/10 · ❌ FAIL

| Metric | Value | Source |
|---|---:|---|
| Card volume (cumulative) | $72.3M · 25,233 cards | [Unverified] Zebec Sep 2026 recap (self-reported, unaudited) |
| Payroll | ~$55M / month · 271 business clients | [Unverified] Zebec recap |
| Q3 2026 buyback | 40,536,539 ZBCN (~$100k, ~0.04% of market cap) | [Tier A] Zebec report + buyback wallet |
| Buyback wallet [`EkXEg6de172aoLvr7w86YzQ2rf5oEFD3iUt8uQsLQuQW`](https://solscan.io/account/EkXEg6de172aoLvr7w86YzQ2rf5oEFD3iUt8uQsLQuQW) | 108.26M ZBCN | [Tier A] Solana RPC, 3 Nov |
| Burned, all time | ~1.23M ZBCN (0.0012%) · buyback wallet burned 0 | [Tier A] supply math |
| Token needed to use product? | **No.** Payroll settles in USDC / EURC | [Tier A] docs.zebec.io |

- 2023 promise "card revenue funds buyback-and-burn" was **abandoned** by ZIP-4 (20 Jan 2024).

**What it means:** The company may make money; the token gets a ~$100k-a-quarter buyback that is held, not burned. No audited figures.

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** The buyback (~$100k a quarter) is a company decision, is not automatic on-chain, and the bought ZBCN is held, not burned. No fee share or fee-funded staking yield. Holders have no live claim on revenue; the score describes the business, not holder accrual.

## 🏛️ Foundation & team — Who is in charge? · 3/10 · ❌ FAIL

| Item | Finding | Source |
|---|---|---|
| Token issuer / foundation | **No legal entity or registry filing found** in Zebec docs | [Tier A] docs (absence) |
| CEO (official team page) | Simon Babakhani, CEO & co-founder | [Tier A] zebec.io/team · person [Unverified] |
| Founder (2021–2025 press) | Sam Thapaliya — omitted from current team page. Verified as a person via SEC Form D (Kalki, Inc., Chairman) | [Tier A] EDGAR · current role [Unverified] |
| Other names | Sajjan Thapaliya, Elena Solovyov, Neal Padhye, Parth Shah, Stelios Gerogiannakis, Ashish Shrestha, JJ Ortiz, Eike Reichert, JV Vink | [Unverified] (site titles only) |
| Funding filing | Shima Zebec SPV LLC, Form D, $2,890,000 sold (CIK 0001941922) | [Tier A] EDGAR |
| Seed (Nov 2021) | Breyer Capital, Republic Capital, Shima Capital co-leads | [Tier B] BusinessWire |
| Series A (Feb 2022) | Solana Ventures, Distributed Global lead; Circle, Coinbase Ventures, Lightspeed, Alameda, DST | [Tier B] The Block |
| Personnel verified | 1 of 11 | Real Rails personnel register |

**What it means:** Big-name backers on paper, but you cannot tell which company issues the token, and the founder quietly left the team page.

## 🪙 Foundation / team holdings — How many coins do they hold? · 4/10 · ❌ FAIL

| Wallet | ZBCN | % of supply | Notes |
|---|---:|---:|---|
| Two vaults run by a Zebec-deployed program ([`H8Hr964A…`](https://solscan.io/account/H8Hr964ApEP3ie1rwRTT7wkSrgvUqJQb8oNAKspkDDfR) 7.0B, [`3J7n5Usm…`](https://solscan.io/account/3J7n5Usmei8BqgUHan5xuBiJkAx6M1AQQhGwbKiVdQ17) 5.5B) | ≥12.5B | ≥12.5% | Provable link. Arkham: no entity on either, but [`H8Hr96…`](https://solscan.io/account/H8Hr964ApEP3ie1rwRTT7wkSrgvUqJQb8oNAKspkDDfR) received 3.5B from "Zebec Network: Zebec Vault (43wqg)". No exchange deposits in Arkham's ~30-day window. [`3J7n5U…`](https://solscan.io/account/3J7n5Usmei8BqgUHan5xuBiJkAx6M1AQQhGwbKiVdQ17) sent 500M to the hub on 21 Aug 2026; [`H8Hr96…`](https://solscan.io/account/H8Hr964ApEP3ie1rwRTT7wkSrgvUqJQb8oNAKspkDDfR) sent 318M via [`FNuqKqgJ…`](https://solscan.io/account/FNuqKqgJLzJExhZQo1r8ZjQDQRp7hJX2j4bvE2hjcgtM) to the hub on 4 Oct 2026 |
| Linked recipient | ~0.53B | 0.53% | |
| Staked (staking program) | ~4.95B | 4.95% | |
| Buyback wallet `EkXEg6…QuQW` | 108.26M | 0.11% | Published |
| Published treasury hub [`9Sq2nZ481aiEkoDB9gavcfD6v7pr4LEcPnUdky4TEine`](https://solscan.io/account/9Sq2nZ481aiEkoDB9gavcfD6v7pr4LEcPnUdky4TEine) | 6,743,884 (15 Nov) | <0.01% | **Correction:** not drained for good. It is a pass-through disbursement wallet, refilled from [`71LxiE4P…`](https://solscan.io/account/71LxiE4PvxdZxLmtGcoKAJEWKofPqYw5Wdn6PSpXHodV) and the vaults, paying a fixed list of wallets on the 1st and 16th of each month (see Selling). Arkham: no entity |
| Treasury-linked [`71LxiE4PvxdZxLmtGcoKAJEWKofPqYw5Wdn6PSpXHodV`](https://solscan.io/account/71LxiE4PvxdZxLmtGcoKAJEWKofPqYw5Wdn6PSpXHodV) | 338,300,464 (15 Nov) | 0.34% | Gets ZBCN from the hub through Zebec streaming-program accounts (500M on 21 Aug, 353M on 4 Oct 2026), tops the hub back up, and feeds [`EsDV3m3x…`](https://solscan.io/account/EsDV3m3xUZ7g8QKa1kFdbZT18nNz8ddGJRcTK84WDQ7k) (the wallet that funded vault [`3J7n5U…`](https://solscan.io/account/3J7n5Usmei8BqgUHan5xuBiJkAx6M1AQQhGwbKiVdQ17)). Owner not disclosed |
| Uphold [`5rhms6jZQaXnQc6wbicnrxDTkKqKi4iwfWW3612r5rHb`](https://solscan.io/account/5rhms6jZQaXnQc6wbicnrxDTkKqKi4iwfWW3612r5rHb) | 20,357,918,028 (15 Nov) | 20.4% | **Uphold confirmed** by two labels: Nansen ("hot wallet 3") and Arkham (entity Uphold, "Cold Wallet (5rhms)", Fireblocks custody). Holds pooled buyback inventory + other customers |
| Team, ecosystem, market-making wallets | **Not published** | — | |
| Legacy ZBC unmigrated | 326,903,502 ZBC (~3.27B ZBCN-equivalent) | ~3.3% | Reserve for late migrations [Unverified] |

**What it means:** At least ~13% is in Zebec-controlled vaults, the team wallets are not disclosed, and buyback tokens sit on an exchange where they can be sold. Arkham's "Zebec Network" entity covers only small wallets ($386k); the big vaults and the hub are unlabelled there. Score unchanged at 4/10.

## 📉 Selling behavior — Do insiders sell into pumps? · 1/10 · ❌ FAIL

| Test | Result | Source |
|---|---|---|
| Treasury / buyback / team sends to exchanges in Apr and Aug 2026 pump windows | None found by Nansen. **Superseded for Sep–Oct 2026 by the trace below** | [Tier B] Nansen pack (third-party labels) |
| Top sellers on 27–28 Apr 2026 pump | Unlabeled / "STONK Whale" wallets, not the treasury or buyback wallet | [Tier B] Nansen |
| CEX flow on 27 Apr / 28 Apr | 957.9M in / 910.8M out · 837.3M in / 757.2M out | [Tier B] Nansen |
| Buyback custody | ~378M bought-back ZBCN went to Uphold hot wallet 2, pooled with customers, then to hot wallet 3. Zebec disclosed "held with Uphold Institutional" (Jul 2026) | [Tier A] chain · [Tier A] Zebec blog |
| Early backers | Zebec Jan 2026 tokenomics blog: early backers "have realized significant returns" | [Tier A] Zebec blog |

### A. Treasury cluster → fresh wallets → DEX pools and exchange wallets on the 30 Sep – 4 Oct 2026 pump days

How the money moves ([Tier A] Solana RPC `getSignaturesForAddress` + `getTransaction`, read 15 Nov 2026 ~11:10–11:40 AM MST; pump test on CoinGecko daily closes):

| Step | What happened (UTC) | Amount (ZBCN) |
|---|---|---:|
| 1 | Vaults → published hub [`9Sq2…`](https://solscan.io/account/9Sq2nZ481aiEkoDB9gavcfD6v7pr4LEcPnUdky4TEine): [`3J7n5U…`](https://solscan.io/account/3J7n5Usmei8BqgUHan5xuBiJkAx6M1AQQhGwbKiVdQ17) 500M (21 Aug); [`H8Hr96…`](https://solscan.io/account/H8Hr964ApEP3ie1rwRTT7wkSrgvUqJQb8oNAKspkDDfR) via [`FNuqKqgJ…`](https://solscan.io/account/FNuqKqgJLzJExhZQo1r8ZjQDQRp7hJX2j4bvE2hjcgtM) 318M (4 Oct) | 818M |
| 2 | Hub → Zebec streaming-program accounts ([`GXD2FnXi…`](https://solscan.io/account/GXD2FnXi718y9tPUd6CW1CW6khZ14DGtQc5cBpYkjm5J), owned by Zebec's streaming program [`zbcKGd…`](https://solscan.io/account/zbcKGdAmXfthXY3rEPBzexVByT2cqRqCZb9NwWdGQ2T)) → [`71LxiE4P…`](https://solscan.io/account/71LxiE4PvxdZxLmtGcoKAJEWKofPqYw5Wdn6PSpXHodV) the same minute: 500M (21 Aug), 35M + 318M (4 Oct) | 853M |
| 3 | [`71LxiE4P…`](https://solscan.io/account/71LxiE4PvxdZxLmtGcoKAJEWKofPqYw5Wdn6PSpXHodV) → [`EsDV3m3x…`](https://solscan.io/account/EsDV3m3xUZ7g8QKa1kFdbZT18nNz8ddGJRcTK84WDQ7k) (the wallet that funded vault [`3J7n5U…`](https://solscan.io/account/3J7n5Usmei8BqgUHan5xuBiJkAx6M1AQQhGwbKiVdQ17)): 204M (12 Sep), **333.3M (30 Sep, 5-day +23.2%)**, **62.5M (4 Oct, +21.0%)**, 85.1M (2 Nov), 43.4M (5 Nov) | 728.3M |
| 4 | [`EsDV3m3x…`](https://solscan.io/account/EsDV3m3xUZ7g8QKa1kFdbZT18nNz8ddGJRcTK84WDQ7k) → pairs of fresh wallets after 100- or 1,000-token test sends, then split into 5M–40M pieces within hours. Pump-day batches: **28.5M (22 Aug, +31.5%)**, **333.3M (30 Sep)**, **62.5M (4 Oct)** | 424.3M on pump days |

Where the traced pieces landed (1–3 hops after step 4; only part of the tree was followed):

| Destination | Traced amount | Dates (UTC) | What it is |
|---|---:|---|---|
| Orca Whirlpool + three Meteora DLMM pool vaults ([`FaoZEZ…`](https://solscan.io/account/FaoZEZFsRS2jJAzg5PXwNjDdA1hDAjDGAkDf4xRfY79w), [`6Mo8W6…`](https://solscan.io/account/6Mo8W6b67brHWokLNeXPdfwH7B1ir3xYCGd4EcBen6eM), [`5VXPSS…`](https://solscan.io/account/5VXPSSnSxa2bP9HPdHXt9pCXVyfwXwRN8HRE2pyoN88M), [`7U8DUK…`](https://solscan.io/account/7U8DUKAds4SKeKU9zWNdM6iVXrsLc7fx8VUY5sw2zjWz)) | **~50M** (across multiple swaps, sizes ~5–7M; one saved sale was 7.0M split across three pools) | 1 Oct, 03:40–14:43 (5-day **+23.0%**) | DEX sales [Tier A: tokens paid into pool vaults owned by the Orca and Meteora programs] |
| [`u6PJ8DtQuPFnfmwHbGFULQ4u4EgjDiyYKjVEsynXq2w`](https://solscan.io/account/u6PJ8DtQuPFnfmwHbGFULQ4u4EgjDiyYKjVEsynXq2w) | **51.0M** on pump days (+11.25M on 5 Oct) | 1 and 4 Oct | Exchange-scale wallet (63,203 SOL, 1,000 txs in 6 hours). It is where Arkham's "Gate Deposit (ACjqB)" sweeps every deposit, so very likely Gate's collection wallet [Gate label: one Tier B source + sweep pattern] |
| [`A77HErqtfN1hLLpvZ9pCtu66FEtM8BveoaKbbMoZ4RiR`](https://solscan.io/account/A77HErqtfN1hLLpvZ9pCtu66FEtM8BveoaKbbMoZ4RiR) | 25.0M | 30 Sep – 1 Oct | Exchange-scale wallet (9,088 SOL, 1,000 txs in under 3 days); label Not found |
| [`4GQeEya6ZTwvXre4Br6ZfDyfe2WQMkcDz2QbkJZazVqS`](https://solscan.io/account/4GQeEya6ZTwvXre4Br6ZfDyfe2WQMkcDz2QbkJZazVqS) | 30.0M | 1 Oct | High-activity wallet; label Not found |
| **Total traced on pump days** | **~156M ZBCN ≈ $0.41M** at ~$0.0026 | | Of 424.3M sent out on pump days |

- Who controls [`71LxiE4P…`](https://solscan.io/account/71LxiE4PvxdZxLmtGcoKAJEWKofPqYw5Wdn6PSpXHodV) and [`EsDV3m3x…`](https://solscan.io/account/EsDV3m3xUZ7g8QKa1kFdbZT18nNz8ddGJRcTK84WDQ7k) is not disclosed, and Arkham shows no entity for them. But both are funded from the published treasury hub and the Zebec-program vaults, and [`71LxiE4P…`](https://solscan.io/account/71LxiE4PvxdZxLmtGcoKAJEWKofPqYw5Wdn6PSpXHodV) tops the hub back up. Under this layout's rule ("funding a wallet that sells" on a pump day, without disclosure) that **fails Selling at gate level**. It would clear only if Zebec discloses these wallets as a disclosed market-maker or OTC programme.
- The fan-out pattern (test send, then pieces of 5–40M to wallets used once) is how OTC desks, market makers or exchange deposits are usually fed. Whether every piece was sold is Not found; the ~50M into DEX pools was.

### B. Published hub pays an Arkham-labelled Gate deposit address twice a month

| Date (UTC) | Hub → [`ACjqBWqMhcbDTbnWitdFohrJebHmSA7tmX23Awt7n54e`](https://solscan.io/account/ACjqBWqMhcbDTbnWitdFohrJebHmSA7tmX23Awt7n54e) | 5-day move |
|---|---:|---:|
| 2 Aug 2026 | 1,320,238 | +1.7% |
| 17 Aug | 1,586,306 | −3.5% |
| 2 Sep | 1,381,077 | −14.3% |
| 17 Sep | 1,445,000 | −4.3% |
| **1 Oct** | **964,346** | **+23.0% (pump day)** |
| 16 Oct | 1,110,445 | −2.7% |
| 1 Nov | 1,200,829 | −5.3% |
| **Total** | **9,008,241 (~$17k)** | |

- Arkham labels [`ACjqB…`](https://solscan.io/account/ACjqBWqMhcbDTbnWitdFohrJebHmSA7tmX23Awt7n54e) "Gate Deposit"; on-chain it forwards each receipt to [`u6PJ8DtQ…`](https://solscan.io/account/u6PJ8DtQuPFnfmwHbGFULQ4u4EgjDiyYKjVEsynXq2w) within hours ([Tier B] Arkham, read 15 Nov 2026 ~11:05 AM MST (signed-in account) · [Tier A] RPC). The same five or six wallets are paid on the 1st/2nd and 16th/17th of every month, so this looks like contributor pay in ZBCN, with one payee cashing out at Gate. Small, and on a schedule rather than timed to pumps; one payment fell on a pump day.

- Real Rails treasury badge (before this trace): **CAUTION**.

**What it means:** Yes, now. ZBCN from the published treasury cluster was split through fresh wallets and sold into DEX pools and sent to exchange-scale wallets on the 30 Sep – 4 Oct pump days (~156M traced, ~$0.41M), with no disclosure. The hub also pays an exchange deposit address twice a month (small). Score cut from 5 to 3, which trips the hard gate.

- **Disclosure quality (16 Nov 2026 rules): silence.** Zebec published the treasury wallets but not these sales. **Penalty applied (16 Nov 2026 rules):** a proven pump-day sale with no disclosure takes 2 points off the ordinary Selling score, floored at 0: **3 → 1**. The sales on 30 Sep – 3 Oct 2026 are still pump days on Gate prices (4 Oct is not). Pump days from Gate ZBCN_USDT UTC daily closes, re-run 16 Nov 2026 with scripts/pump_day_test.py (48 of 360 days); the body's earlier count used CoinGecko daily closes.

- **One-hop amendment (16 Nov 2026):** Still a **proven sale** under the amended rule. (b) holds: treasury-cluster ZBCN was sold into DEX pools on the pump days. Silence stands, so the penalty above is unchanged.

## 📊 Tokenomics & supply · 6/10 · ✅ PASS

| Item | Value | Source |
|---|---|---|
| Total supply | 99,998,768,429 (100B minus burns) | [Tier A] RPC |
| Mint / freeze authority | Revoked / revoked · classic SPL (no Token-2022 tax or hooks) | [Tier A] RPC |
| Unlocks | Final scheduled unlock Mar 2026 · no future unlock overhang | [Tier A] Zebec Q1 2026 report · exact date [Unverified] |
| Migration | ZBC → ZBCN 1:10, 10 Apr – 10 May 2024, no new supply | [Tier A] docs |
| Burns | Paused since ZIP-4; DAO may "evaluate" restarting by end-2026 | [Tier A] |

**What it means:** No printer and no unlock cliff left. The supply risk is concentration, not inflation.

## 💧 Liquidity & market · 7/10 · ✅ PASS

- CoinGecko 24h volume **$8.43M** on a $172.6M cap (~4.9% turnover). Listed on multiple CEXs; Nansen 7d exchange net flow −$613k.

**What it means:** Deep enough that a single seller cannot move it much.

## 🧑‍💻 Product & development · 5/10 · ❌ FAIL

- Live: Zebec cards (Mastercard), Enterprise Payroll (non-custodial; Solana, Stellar, Canton, Aleo, Algorand, Base), SuperApp (App Store v0.1.1 on 11 Jul 2026, promised mid-late March).
- Late / partial: eSIM in SuperApp, Enterprise Desktop 2.0, white-label employer app. Abandoned: ADP / UKG payroll integrations.
- GitHub `Zebec-protocol`: 16 repos, **0 pushed in the last 90 days** (last push 16 Sep 2026).

**What it means:** Products ship, often late. Public code is quiet.

## 🤝 Adoption & customers · 6/10 · ✅ PASS

| Partner claim | Status |
|---|---|
| Ripple: enterprise payroll on XRPL settled in RLUSD | Confirmed |
| Stripe via Privy wallets | Confirmed |
| Mastercard cards · Circle payroll case study · Nacha member | Confirmed |
| Visa partnership | False |
| "Zebec on Circle Arc with BlackRock/DTCC" | False |
| DTCC "banking takeover" | False |
| Stripe Tempo chain deal | Unverified |

**What it means:** A handful of real, confirmed integrations, surrounded by influencer claims that are false.

## 🛡️ Security & audits · 3/10 · ❌ FAIL

| Program | ID | Upgrade authority |
|---|---|---|
| Streaming | [`zbcKGdAmXfthXY3rEPBzexVByT2cqRqCZb9NwWdGQ2T`](https://solscan.io/account/zbcKGdAmXfthXY3rEPBzexVByT2cqRqCZb9NwWdGQ2T) | [`5aUDpuNNbAvme6hPi4o2vBbzHMrF7h3xB4kfKNMk6V8h`](https://solscan.io/account/5aUDpuNNbAvme6hPi4o2vBbzHMrF7h3xB4kfKNMk6V8h) (**single key**) |
| Custody / treasury | [`b6ZPysThkApNx2YDiGsPUiYPE7Ub1kTRdCWp7gBkzbr`](https://solscan.io/account/b6ZPysThkApNx2YDiGsPUiYPE7Ub1kTRdCWp7gBkzbr) | same single key |
| Staking | [`zSTKzGLiN6T6EVzhBiL6sjULXMahDavAS2p4R62afGv`](https://solscan.io/account/zSTKzGLiN6T6EVzhBiL6sjULXMahDavAS2p4R62afGv) | [`93aZawDHMCagDDPy8dbcJdx4Xd4WsYP5KWE6EScocDLN`](https://solscan.io/account/93aZawDHMCagDDPy8dbcJdx4Xd4WsYP5KWE6EScocDLN) |
| Vault | [`zVLTdc9GmsZ6zjS6bdSFWh7p3BdiPPyju9y82Cr7Vs3`](https://solscan.io/account/zVLTdc9GmsZ6zjS6bdSFWh7p3BdiPPyju9y82Cr7Vs3) | same [`93aZaw…`](https://solscan.io/account/93aZawDHMCagDDPy8dbcJdx4Xd4WsYP5KWE6EScocDLN) |

- No ZBCN hack on file (2025–2026). Governance: only two Realms proposals ever; the 2024 buyback vote passed with **one wallet casting 97.9%**.

**What it means:** One stolen key could rewrite the programs that move customer money.

## ⚖️ Regulatory · 3/10 · ❌ FAIL

- No issuer entity disclosed; no licence found on a register. Nacha membership confirmed. Movement Labs / MOVE press about Thapaliya: [Unverified]; no court filing naming him or Zebec found.

**What it means:** A payments company with no visible licensed entity behind the token.

## 📅 Catalysts & calendar · 4/10 · ❌ FAIL

| Date | Event |
|---|---|
| Q4 2026 | Next quarterly buyback report |
| By end-2026 | DAO may "evaluate" restarting burns |
| Open | Revised white paper ("in progress"; current v3.1, Mar 2025) |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None on file |
| Buybacks sold rather than held | 🟡 Cannot be ruled out (pooled exchange custody) |
| Treasury-funded wallets sell into pumps | 🔴 **Tripped** (30 Sep – 4 Oct 2026; Selling A): [`71LxiE4P…`](https://solscan.io/account/71LxiE4PvxdZxLmtGcoKAJEWKofPqYw5Wdn6PSpXHodV) → [`EsDV3m3x…`](https://solscan.io/account/EsDV3m3xUZ7g8QKa1kFdbZT18nNz8ddGJRcTK84WDQ7k) [tx: 333.3M, 30 Sep](https://solscan.io/tx/4HbiXD2wPnmWd8xz7KzoDuhfezbpikN1scNPQoXEgWUDf3v1ZwVK7vDF6SzBa5fVXBCsZ6rx9iXA9HmzPvXsz1m) · [tx: 62.5M, 4 Oct](https://solscan.io/tx/3frtonWRYHyLMmw46Bv7mei6R7eEDZLMeMc6Z4GKXpLQoJUFQqbCQ65wmSq9iboyoyqGxg9x8sx4xCRyaC1LFHPm) → DEX pool sales [tx: 1 Oct](https://solscan.io/tx/3NGf2C9JaZhkjrjzGc7KZkMgS5x3mEv8X9xStCmrJ5QHXQA4BCzrYDLQDAh83cwk2dWdmX5hHaENLnjLRuVrjA3p) [tx: 1 Oct](https://solscan.io/tx/3fxRyAcu5d196XgwZhUEem2FQ7NNMN9xtEoyvsS6TcoFSDXoRB1HBBKQq9A7VrCWSHggJVJYPFs3jXRZcsSHqiPc) |
| Treasury hub → exchange deposit | 🔴 **Tripped**, small (9.0M ZBCN to an Arkham-labelled Gate deposit, Aug–Nov 2026; Selling B): [Arkham: Gate Deposit](https://intel.arkm.com/explorer/address/ACjqBWqMhcbDTbnWitdFohrJebHmSA7tmX23Awt7n54e) · pump-day payment [tx: 1 Oct](https://solscan.io/tx/mTGdw8d3HVX46WbdZchqB3KxHPf7ZqQW4nCeKMcaN4s3MKuuSzwKooARg1awuSv1waRdjuT4p1sQRenUvHqZou2) |
| Founder/leadership change | 🟡 Founder dropped from team page (role unverified) |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| [`9Sq2…`](https://solscan.io/account/9Sq2nZ481aiEkoDB9gavcfD6v7pr4LEcPnUdky4TEine) | Zebec treasury hub | Zebec's own published wallet list + Solana RPC flows | high | yes (project publication) | Selling: funded the wallets that sold on 30 Sep – 3 Oct pump days |

## 📚 Sources

- [Tier A] Methodology update 16 Nov 2026: no new Arkham lookups; the attribution table uses evidence already cited in this report.
- [Tier A] Solana mainnet RPC: full token-account census 10 Oct 2026; balances 3 Nov 2026
- [Tier A] [docs.zebec.io](https://docs.zebec.io) · zebec.io/team · [Q1 2026 report](https://zebec.io/blog/q1-2026-report) · [ZIP-4](https://medium.com/zebec-protocol/zip-4-governance-proposal-redesignation-for-protocol-growth-83f62e3614cb)
- [Tier A] SEC EDGAR Form D, Shima Zebec SPV LLC (CIK 0001941922)
- [Tier A] CoinGecko `zebec-network`, 14 Nov 2026 9:08 AM MST
- [Tier A] Solana mainnet RPC (`api.mainnet-beta.solana.com`), every address and signature viewable on [Solscan](https://solscan.io) and linked inline and in the Evidence trail: ZBCN token accounts and parsed transactions for the hub [`9Sq2…`](https://solscan.io/account/9Sq2nZ481aiEkoDB9gavcfD6v7pr4LEcPnUdky4TEine) (all 95 successful transactions since 1 Aug 2026), [`71LxiE4P…`](https://solscan.io/account/71LxiE4PvxdZxLmtGcoKAJEWKofPqYw5Wdn6PSpXHodV), [`EsDV3m3x…`](https://solscan.io/account/EsDV3m3xUZ7g8QKa1kFdbZT18nNz8ddGJRcTK84WDQ7k), [`GXD2FnXi…`](https://solscan.io/account/GXD2FnXi718y9tPUd6CW1CW6khZ14DGtQc5cBpYkjm5J), [`FNuqKqgJ…`](https://solscan.io/account/FNuqKqgJLzJExhZQo1r8ZjQDQRp7hJX2j4bvE2hjcgtM), [`ACjqB…`](https://solscan.io/account/ACjqBWqMhcbDTbnWitdFohrJebHmSA7tmX23Awt7n54e) and 2–3 hops of fresh wallets; balances of the vaults and Uphold; 15 Nov 2026 ~11:10–11:40 AM MST
- [Tier B] Nansen pack 9 Nov 2026 (labels are third-party)
- [Tier B] Arkham, read 15 Nov 2026 ~11:05 AM MST (signed-in account) — [hub](https://intel.arkm.com/explorer/address/9Sq2nZ481aiEkoDB9gavcfD6v7pr4LEcPnUdky4TEine) · [ACjqB… Gate Deposit](https://intel.arkm.com/explorer/address/ACjqBWqMhcbDTbnWitdFohrJebHmSA7tmX23Awt7n54e) · [H8Hr96…](https://intel.arkm.com/explorer/address/H8Hr964ApEP3ie1rwRTT7wkSrgvUqJQb8oNAKspkDDfR) · [3J7n5U…](https://intel.arkm.com/explorer/address/3J7n5Usmei8BqgUHan5xuBiJkAx6M1AQQhGwbKiVdQ17) · [Uphold 5rhms6…](https://intel.arkm.com/explorer/address/5rhms6jZQaXnQc6wbicnrxDTkKqKi4iwfWW3612r5rHb) · [entity Zebec Network](https://intel.arkm.com/explorer/entity/zebec-network): hub [`9Sq2…`](https://solscan.io/account/9Sq2nZ481aiEkoDB9gavcfD6v7pr4LEcPnUdky4TEine) no entity (Phantom profile only); [`ACjqB…`](https://solscan.io/account/ACjqBWqMhcbDTbnWitdFohrJebHmSA7tmX23Awt7n54e) "Gate Deposit"; [`H8Hr96…`](https://solscan.io/account/H8Hr964ApEP3ie1rwRTT7wkSrgvUqJQb8oNAKspkDDfR) and [`3J7n5U…`](https://solscan.io/account/3J7n5Usmei8BqgUHan5xuBiJkAx6M1AQQhGwbKiVdQ17) no entity (tag Whale); [`5rhms6…`](https://solscan.io/account/5rhms6jZQaXnQc6wbicnrxDTkKqKi4iwfWW3612r5rHb) Uphold "Cold Wallet"; entity "Zebec Network" (1.1k addresses, $386k). Limits: relative ages only (dates above are from RPC); ~30-day exchange window, all-time is Enterprise-locked; first page of transfers read
- [Tier B] [BusinessWire, Nov 2021](https://www.businesswire.com/news/home/20211110005872/en/) · [The Block, Feb 2022](https://www.theblock.co/news/deals/2022-02-23-zebec-solana-protocol-funding-round-feb-135100) · [crypto.news Q3 buyback](https://crypto.news/zebec-network-zbcn-q3-buyback-payroll-revenue/)
- [Unverified] Self-reported card/payroll metrics; Thapaliya's current role; exact Mar 2026 unlock date; owners of [`71LxiE4P…`](https://solscan.io/account/71LxiE4PvxdZxLmtGcoKAJEWKofPqYw5Wdn6PSpXHodV), [`EsDV3m3x…`](https://solscan.io/account/EsDV3m3xUZ7g8QKa1kFdbZT18nNz8ddGJRcTK84WDQ7k) and the fresh wallets; Gate ownership of [`u6PJ8DtQ…`](https://solscan.io/account/u6PJ8DtQuPFnfmwHbGFULQ4u4EgjDiyYKjVEsynXq2w) (one label + sweep pattern); owners of [`A77HErqt…`](https://solscan.io/account/A77HErqtfN1hLLpvZ9pCtu66FEtM8BveoaKbbMoZ4RiR) and [`4GQeEya6…`](https://solscan.io/account/4GQeEya6ZTwvXre4Br6ZfDyfe2WQMkcDz2QbkJZazVqS)

## 🔗 Evidence trail

*Strongest findings first. Each link opens the primary record (block explorer) or the label source (Arkham) for the claim, so any number can be checked by hand.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| 🔴 Vault `3J7n5U…` → hub 500M (21 Aug 2026) | [tx `3waNh14q…`](https://solscan.io/tx/3waNh14q2e839J9HuVU9CUupqUQEw9y7fHUDGCHSHKjuKnkdE2DxRqyv2ZKdCdWyHosapJWJkeE7ycUXRig9y67V) · [`3J7n5Usm…`](https://solscan.io/account/3J7n5Usmei8BqgUHan5xuBiJkAx6M1AQQhGwbKiVdQ17) · [Arkham](https://intel.arkm.com/explorer/address/3J7n5Usmei8BqgUHan5xuBiJkAx6M1AQQhGwbKiVdQ17) | A | 15 Nov 2026 ~11:10–11:40 AM MST |
| 🔴 Vault `H8Hr96…` via `FNuqKqgJ…` → hub 318M (4 Oct) | [tx `5qZEqk5F…`](https://solscan.io/tx/5qZEqk5FnRfYa4Wv3LuAkQYnZvJX7d4uD8NR6bU9suDWn5spRuah4XKte6GsrARqst6xntRs5BgexXrgciMtdL6q) · [`FNuqKqgJ…`](https://solscan.io/account/FNuqKqgJLzJExhZQo1r8ZjQDQRp7hJX2j4bvE2hjcgtM) · [Arkham H8Hr96…](https://intel.arkm.com/explorer/address/H8Hr964ApEP3ie1rwRTT7wkSrgvUqJQb8oNAKspkDDfR) | A | 15 Nov 2026 ~11:10–11:40 AM MST |
| 🔴 Hub → Zebec streaming account `GXD2FnXi…` → `71LxiE4P…` same minute: 500M (21 Aug), 35M + 318M (4 Oct) | [tx: hub→GXD2 500M](https://solscan.io/tx/2PFXnM3qzmjNVJko4eazSLK5pi5t3A2Jt3RzjjAbXg39Pr7BYmDEcMT99hCwAsk1kfx5hA4FpmxdJT5FjGq2FgGi) [tx `GXD2→71Lx…`](https://solscan.io/tx/2jkwN4327xqbS4KhEecGq8pVm5PCfdannrzVS5DzdUKexLCgdYtkJgR4q5BLdU7ysPYiV8xCLZwHbJRXAkN7d4Q6) · [tx `35M…`](https://solscan.io/tx/42HjjYQnSkaWm8HD2MSy3c1sE8Ywh7pPcr8uWVsJfEcXdNqGoTMxfUx7DTePMbJi6j7Rb6JzihyPartfX6mCsZnH) [tx `3mxZyVR6…`](https://solscan.io/tx/3mxZyVR6tRp67QGARuUqdjYHqZitJgzHNH3qns5hTjRnGwWxoTRxt1LP5EBMBe2DnF5ZJdigWbxx2kaR7CxB7mYW) · [tx `318M…`](https://solscan.io/tx/yakoepseFx3q6TGrjwpUTiMQ49GHf3p9VNzaneyj5JFFFSb9Skf6wmzawgrryj29WtQZxQjVto1pPoX6Lj2EoqR) [tx `3FiT8DD6…`](https://solscan.io/tx/3FiT8DD6oXXzZf6BQLRuTA1s6usWWZHFacBzxWSbtupCni9rywjvhMyHZNqgq6bsqvwtp4GrBWHfc8zyy3DURVH3) · [`GXD2FnXi…`](https://solscan.io/account/GXD2FnXi718y9tPUd6CW1CW6khZ14DGtQc5cBpYkjm5J) | A | 15 Nov 2026 ~11:10–11:40 AM MST |
| 🔴 `71LxiE4P…` → `EsDV3m3x…` 333.3M on 30 Sep (5-day +23.2%), split to two fresh wallets in 4 min | [tx `4HbiXD2w…`](https://solscan.io/tx/4HbiXD2wPnmWd8xz7KzoDuhfezbpikN1scNPQoXEgWUDf3v1ZwVK7vDF6SzBa5fVXBCsZ6rx9iXA9HmzPvXsz1m) → [tx `166.7M→DoBTtiH3…`](https://solscan.io/tx/2RJaivxfxm31XLYTDNLmEWmeTTcDV89eTqfY1VSPntENmohaKLoe6zgofsraDerHL3tmFQK2Aqu8WvSMdJorx3PP) · [tx `166.6M→23c1Ryrg…`](https://solscan.io/tx/5fd5rpQuLv6K41qhBrdtKf3n8uirt4oZHB4AtPFdgraWCRFf85RqjpSzviU4t36p8RfmkJgd5gxyEwSrtfVEjSak) | A | 15 Nov 2026 ~11:10–11:40 AM MST |
| 🔴 `71LxiE4P…` → `EsDV3m3x…` 62.5M on 4 Oct (+21.0%), split 2 × 31.2M | [tx `3frtonWR…`](https://solscan.io/tx/3frtonWRYHyLMmw46Bv7mei6R7eEDZLMeMc6Z4GKXpLQoJUFQqbCQ65wmSq9iboyoyqGxg9x8sx4xCRyaC1LFHPm) → [tx `5JEak7LE…`](https://solscan.io/tx/5JEak7LEtBYFtffUdPGA5ZbiYQqVdL6GdzAH9GLhBJoWPmKPm2evHEMyHuMogP1HuGrxwYsfi7f9vvgDiJQtNGs1) · [tx `4PEr4Uba…`](https://solscan.io/tx/4PEr4Uba15DxKwPaG8TLy6ePhYM5Kj9Df1jLXJJZnz7VQEUP3FFRHXRWzKNT1NmoEDKYYX9XVmdWiqDknSEcRSWd) | A | 15 Nov 2026 ~11:10–11:40 AM MST |
| 🔴 1 Oct pump-day DEX sales into Orca/Meteora pool vaults | [tx `5LbxkaAi…`](https://solscan.io/tx/5LbxkaAieNfCLtEsab2nqPmTkoHrdgQJhgCVNjJ4tyvWHghTCmzkDukdhoBFXkFXyWnnk8iyEaJ7YZAGyVNvLiDb) · [tx `3NGf2C9J…`](https://solscan.io/tx/3NGf2C9JaZhkjrjzGc7KZkMgS5x3mEv8X9xStCmrJ5QHXQA4BCzrYDLQDAh83cwk2dWdmX5hHaENLnjLRuVrjA3p) · [tx `3fxRyAcu…`](https://solscan.io/tx/3fxRyAcu5d196XgwZhUEem2FQ7NNMN9xtEoyvsS6TcoFSDXoRB1HBBKQq9A7VrCWSHggJVJYPFs3jXRZcsSHqiPc) · vaults [`FaoZEZ…`](https://solscan.io/account/FaoZEZFsRS2jJAzg5PXwNjDdA1hDAjDGAkDf4xRfY79w) [`6Mo8W6…`](https://solscan.io/account/6Mo8W6b67brHWokLNeXPdfwH7B1ir3xYCGd4EcBen6eM) [`5VXPSS…`](https://solscan.io/account/5VXPSSnSxa2bP9HPdHXt9pCXVyfwXwRN8HRE2pyoN88M) [`7U8DUK…`](https://solscan.io/account/7U8DUKAds4SKeKU9zWNdM6iVXrsLc7fx8VUY5sw2zjWz). Three swap signatures are in the saved trace, including `5LbxkaAi…` from [`AzGcE5EN…`](https://solscan.io/account/AzGcE5EN6h7NDweVy19fmPDE1DtsQmu5C4xRwZxqyq5K) for 7.0M split across three pools (1.95M + 0.66M + 4.40M); other signatures behind the ~50M figure were not saved | A | 15 Nov 2026 ~11:10–11:40 AM MST |
| 🔴 Fresh wallets → exchange-scale `u6PJ8DtQ…` (pump days 30 Sep – 4 Oct) | [`u6PJ8DtQ…`](https://solscan.io/account/u6PJ8DtQuPFnfmwHbGFULQ4u4EgjDiyYKjVEsynXq2w) · [tx `3cRDohC9…`](https://solscan.io/tx/3cRDohC9hgGJTfvyPYwrTfLSA473zz5m9gy48jee1MaALFmwjzhBc2kwFSycktKjcfNhUEdqPxdaaESgNBkAgCc2) [tx `5CVfz817…`](https://solscan.io/tx/5CVfz817Pe2NhnZPABDwhDwPjX52jErcMBDNvPXFp9WZ9ycxyuPxHfEVG9SMHjNqnCZPuzjxnCdBJJGTZhu7XXB4) [tx `2WB6yHMJ…`](https://solscan.io/tx/2WB6yHMJmdfU3LZfjp8P6btViLSdEJuYCucWHWuyV5ta4Nm9W4hcWhXPKMvm3ZJSzQgjKwiZk3GBNeoWokqbn81W) [tx `42gcnbmB…`](https://solscan.io/tx/42gcnbmBgJne548byp48j39QvBphioim2RbdQfKB6UxSFmA9aUi1pGytG1ypxyC1fCafyPRqtyQ5jYSrxS9PzEF4) [tx `3JXfN5Hn…`](https://solscan.io/tx/3JXfN5Hns5SjL4LuBGAt2FmAmfKcZEeLzrYRudr9xxLU8YQtUBf6UMKJ9CWJgrEFgUDzkCaHLqanfhv6ASFmpite) [tx `4zWG8QYH…`](https://solscan.io/tx/4zWG8QYHAZwyR9ugZazxcDiPUqQq3x3T2JH9bWxZtCjWxpHD17yr8do84BLSRutHQqQksr8YZmup9DkvGEBKntjh) [tx `8mjdmevd…`](https://solscan.io/tx/8mjdmevdeofEvNpFJ3opg8bBPrTesVmf2LHofpKh4d3P7n2uYkUozDvqgH8qAhBdhgcqx3EACUXWZeq3HXqCpE3) [tx `WoXMXWm9…`](https://solscan.io/tx/WoXMXWm9NFoM41UnLUvDcV9ud3B6FUkHpM4uhCrYkBEP4L1vV2vB7jynTXZFCEzn1YBfqYSJr6tGXVonirAawQb) · 5 Oct [tx `ehnC5n5k…`](https://solscan.io/tx/ehnC5n5kRqEEqbvmdN9REXSdt91CR2rReRPu4NXWDYs7xRpu8frx5sMWCfnMYhBXxUn5BsKZmZL7m2MLVPzFaG3) | A flow / B label | 15 Nov 2026 ~11:10–11:40 AM MST |
| Fresh wallets → `A77HErqt…` 25M+ (30 Sep – 1 Oct) | [`A77HErqt…`](https://solscan.io/account/A77HErqtfN1hLLpvZ9pCtu66FEtM8BveoaKbbMoZ4RiR) · [tx `5YqJBeJs…`](https://solscan.io/tx/5YqJBeJsTyVjnVXZgvxZevr5ykbfTDsZzmJoHspTFrJRDeJ224ShGtVJfTnE9TDgASTZV53pNWcZAzqSzkgAMqXs) [tx `3n4eyTq6…`](https://solscan.io/tx/3n4eyTq6JZf1EtTJi7bbXrh1zyzvh4DEDTnhY8VojtfKjzy7KoW41HJMKp8sN47v5HG6AK74xUzm4Hx4BhXcJb8M) [tx `7jYvmked…`](https://solscan.io/tx/7jYvmkedMoo7g4Bi41pXJKUAK7ufgyAn6NjmVnGZRxscvZpDszvpZ2JQsRViLv9MFogCVrriJQced5ahp7zx5Hj) | A | 15 Nov 2026 ~11:10–11:40 AM MST |
| Fresh wallets → `4GQeEya6…` | [`4GQeEya6…`](https://solscan.io/account/4GQeEya6ZTwvXre4Br6ZfDyfe2WQMkcDz2QbkJZazVqS) · [tx `2f229bAa…`](https://solscan.io/tx/2f229bAaMmxfXY59NJ96P29avjo12FpFrbYUAVrz4y6U9DdEEGbzc6f1UFa6dvxvGVH1vXtQR5fLoqhd7hiZJghz) [tx `2nxRmp4e…`](https://solscan.io/tx/2nxRmp4e4oQYXkTDtkYnZA6RDnUR1yhXvYZVZWV5pbuH5HEXGjX8KUJPtr5jJ4Wv45x6HQajMXtErQ6euF75C8XD) | A | 15 Nov 2026 ~11:10–11:40 AM MST |
| Other `71LxiE4P…` → `EsDV3m3x…` feeds: 204M (12 Sep), 28.5M (22 Aug), 85.1M (2 Nov), 43.4M (5 Nov) | [tx `33c3mc7y…`](https://solscan.io/tx/33c3mc7yjaqaPZWVC8WEmQmDaFv4F9rNNhyZ6drmmnKDB21MqpmCgT7HEDzD9hqecTHVuu2iQtaPdwJLBcqfXPr2) · [tx `622rE4ES…`](https://solscan.io/tx/622rE4ESnB8uMsXbo6NpLgk1g9yTQjEVv4MfUzkCBAcZny8RTDrohFaSuT2A8GPxC2zYZFcja1oeETpHG9wqeZVk) · [tx `xDLq9FxN…`](https://solscan.io/tx/xDLq9FxNCc4QwPaohc7oht4x5EJXT5hawetrxXiB51RGvz818JBhin9J6EyyA6x8UpBjhxkW6b6YYLPdieNYMRz) · [tx `5u91aPk9…`](https://solscan.io/tx/5u91aPk9sFnjKmDXRTXkx6m6cAjGSrhgo6HU7BopvhgzUSiWPfYZYVmQRgJmy4PELkeFf9CaH2phLhWuC37MedhZ) | A | 15 Nov 2026 ~11:10–11:40 AM MST |
| 🔴 Hub → Arkham "Gate Deposit" `ACjqB…` 9.0M ZBCN (7 payments) | [Arkham label](https://intel.arkm.com/explorer/address/ACjqBWqMhcbDTbnWitdFohrJebHmSA7tmX23Awt7n54e) · [tx: 2 Aug](https://solscan.io/tx/3nXw3YEM5L1RVimMPVxYV7y2ZHAVbGEt5eiz4SSgTwL9DoeTKb8gQgA3BdSeD5i9JEMgf23X13yvYMrxLFZYtLeN) [tx: 17 Aug](https://solscan.io/tx/5P2iRfRoEyRB1cZscjUcGebA1PgfeZeN9ZwTfU9Ytf4yGZzNuGnrAAekYWWT5m77EQBadAS9hTwZLsXxegPcG8oT) [tx: 2 Sep](https://solscan.io/tx/yTBfJb954X22umjZYAPxECmZevwX6NNnJh6hTdP5VvdB44a59H7G5jQFiMsiHBtx2JRhopyqo8xQPe1dXLk6NrY) [tx: 17 Sep](https://solscan.io/tx/BmeJXLCVRLJy7JRsyaoQzMGnSh7h6B14iQdppsneLYHvxtSp3zivcawAKrEsmSpScXHhPnYZscb2wERsBBqWim7) **[tx: 1 Oct (pump)](https://solscan.io/tx/mTGdw8d3HVX46WbdZchqB3KxHPf7ZqQW4nCeKMcaN4s3MKuuSzwKooARg1awuSv1waRdjuT4p1sQRenUvHqZou2)** [tx: 16 Oct](https://solscan.io/tx/2KeAaBjPrVNmGpHD2xNBdAFLKWCGaT2FsybKy6CdanGSNec3r4KKJWCKtSeKjeYpSLysREUeUysytNow3wrzVWgL) [tx: 1 Nov](https://solscan.io/tx/2bffuJUQQxB1N9nnS3Wa19oZdefbTKZDg92oJp1hpjdeshHT8gwQa6oZB8PvPFnQdgo2WS2LZjAovezd6qUFX1AF) | A flow / B label | 15 Nov 2026 ~11:05–11:40 AM MST |
| Uphold holds 20.36B ZBCN (20.4%) incl. buyback inventory | [`5rhms6jZ…`](https://solscan.io/account/5rhms6jZQaXnQc6wbicnrxDTkKqKi4iwfWW3612r5rHb) · [Arkham: Uphold Cold Wallet](https://intel.arkm.com/explorer/address/5rhms6jZQaXnQc6wbicnrxDTkKqKi4iwfWW3612r5rHb) | A / B label | 15 Nov 2026 |
| Buyback wallet 108.26M ZBCN | [`EkXEg6de…`](https://solscan.io/account/EkXEg6de172aoLvr7w86YzQ2rf5oEFD3iUt8uQsLQuQW) | A | 3 Nov 2026 |
| Streaming + custody programs upgradeable by one plain key `5aUDpuNN…` | [`5aUDpuNN…`](https://solscan.io/account/5aUDpuNNbAvme6hPi4o2vBbzHMrF7h3xB4kfKNMk6V8h) · [`zbcKGd…` program](https://solscan.io/account/zbcKGdAmXfthXY3rEPBzexVByT2cqRqCZb9NwWdGQ2T) | A | 15 Nov 2026 |
| Arkham "Zebec Network" entity covers only small wallets ($386k) | [Arkham entity](https://intel.arkm.com/explorer/entity/zebec-network) | B | 15 Nov 2026 ~11:05 AM MST |

---

## 🔎 Open items and how to close them

| # | Open item | Exact path to close it | Cost / access |
|---|---|---|---|
| 1 | Who controls [`71LxiE4P…`](https://solscan.io/account/71LxiE4PvxdZxLmtGcoKAJEWKofPqYw5Wdn6PSpXHodV) and [`EsDV3m3x…`](https://solscan.io/account/EsDV3m3xUZ7g8QKa1kFdbZT18nNz8ddGJRcTK84WDQ7k), and is the Sep–Oct fan-out a disclosed market-maker or OTC programme? | Ask Zebec (no public treasury-wallet list beyond the hub and buyback wallet); Arkham entity pages for both (not read this pass) | Request to team · Arkham account (have) |
| 2 | Where the rest of the 424.3M pump-day fan-out went (only ~156M traced) | Follow the remaining fresh wallets ([`Adayxh…`](https://solscan.io/account/AdayxhsD2ZpgbmFks1ZJdi55pnoPQWp5ryKWGN6RxmtF), `dc8Qsw…`, [`66L1Yn…`](https://solscan.io/account/66L1YnNYaWxYp1Pi9kjL3ULSeqZc4LFiSwsV88UE1arW), [`AzGcE5…`](https://solscan.io/account/AzGcE5EN6h7NDweVy19fmPDE1DtsQmu5C4xRwZxqyq5K), [`5ZF2VQ…`](https://solscan.io/account/5ZF2VQck23LeuzLSJSWaNRZcrnZUJ6szAobE8ivVvBgd), `877yAidM…` and others) with `getSignaturesForAddress` + `getTransaction` until each piece reaches a pool vault or a labelled exchange wallet | Free, script; slow on public RPC |
| 3 | Confirm [`u6PJ8DtQ…`](https://solscan.io/account/u6PJ8DtQuPFnfmwHbGFULQ4u4EgjDiyYKjVEsynXq2w) is Gate and label [`A77HErqt…`](https://solscan.io/account/A77HErqtfN1hLLpvZ9pCtu66FEtM8BveoaKbbMoZ4RiR), [`4GQeEya6…`](https://solscan.io/account/4GQeEya6ZTwvXre4Br6ZfDyfe2WQMkcDz2QbkJZazVqS) | Arkham or Solscan entity pages; ask Gate | Arkham account (have) |
| 4 | Is the 1st/16th payee list contributor pay? | Ask Zebec; compare with any published compensation policy | Request to team |
| 5 | Token issuer entity | Zebec legal notices / terms; BVI, Cayman or Delaware registry search for "Zebec" | Free to paid |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
