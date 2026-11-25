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

---

## Research update 24 Nov 2026 (MST): Super App launch dates, self-reported volume, and Q3 buyback — reported only, unscored

This section adds primary-source findings from a 24 Nov 2026 desk review of official Zebec docs and posts, plus Unverified leads from a same-day public livestream ([YouTube, Crypto Millie, “Zebec a NEW distribution channel,” id QMyED-T_Wfc](https://www.youtube.com/watch?v=QMyED-T_Wfc)). It does not change the score, badge, formula, or the `revenue_reaches_holders` result (still no). Company volume figures below are **Unverified**, unaudited throughput, not revenue.

### Super App launch dates (official)

- Desktop Super App: Zebec’s [Q1 2026 report](https://zebec.io/blog/q1-2026-report) says the desktop Super App launched in late February 2026.
- Mobile Super App: official blog [“Meet the Zebec SuperApp (Mobile),” 17 Jul 2026](https://zebec.io/blog/meet-the-zebec-superapp-mobile). This report already records App Store version 0.1.1 dated 11 Jul 2026.
- Product docs: [Web SuperApp](https://docs.zebec.io/zebec-application-suite/web-superapp); [cards](https://docs.zebec.io/zebec-product-information/cards).

### Self-reported volume — Unverified, unaudited throughput, not revenue

None of the figures in this table is a published revenue number. They are company usage or volume claims. They have not been audited in a filing reviewed for this update, and they are labelled **Unverified**.

| Claim | Source | Status |
|---|---|---|
| $49M monthly payroll; $65.1M card volume described as “rolling 4-week annualized” (the label is ambiguous and is not treated as revenue) | [Q1 2026 report](https://zebec.io/blog/q1-2026-report) | Unverified throughput, not revenue |
| $72.3M card volume / $55M monthly payroll / 271 clients (September recap) | Already recorded in this report | Unverified throughput, not revenue |
| $500M annual payroll network and more than 50,000 monthly active users; USX to roll out on payroll infrastructure and the Super App | Official blog [“Zebec Introduces ‘Earn on Pay’ Capability with Solstice’s USX,” 13 Aug 2026](https://zebec.io/blog/zebec-introduces-earn-on-pay-capability-with-solstices-usx). Product docs still described the USX / Solstice integration as coming soon as of this pass ([USX / Solstice](https://docs.zebec.io/zebec-product-information/yield/usx-solstice)). | Company claim; Unverified as current audited usage or revenue |
| PayBridge “more than $300 million in annual payroll volume”; PayBridge and School Payroll Services together said to have added 12,000 users | Official blogs [Fintech Fusion](https://zebec.io/blog/fintech-fusion-the-role-of-m-a-in-zebecs-vision) and [Transformative Acquisitions](https://zebec.io/blog/zebecs-transformative-acquisitions-building-the-one-stop-payments-infrastructure-for-global-finance) | Historical acquisition/volume claims, not Super App revenue; Unverified as current figures |

### The only revenue-linked dollar figure on file

The only dollar figure in official Zebec materials that is tied to a token-holder mechanism remains the Q3 2026 buyback: **40,536,539 ZBCN, about $100,000**, announced on Zebec’s official X account on 21 Oct 2026. This report already records that those tokens are held in the buyback wallet [`EkXEg6de172aoLvr7w86YzQ2rf5oEFD3iUt8uQsLQuQW`](https://solscan.io/account/EkXEg6de172aoLvr7w86YzQ2rf5oEFD3iUt8uQsLQuQW) (108.26M as of 3 Nov 2026), held at Uphold, and that burns remain about 1.23M all-time, with **0 burned from the buyback wallet**. See [Inside the ZBCN buyback program](https://zebec.io/blog/inside-the-zbcn-buyback-program) (ZIP-4 paused burns).

No published company, Super App, or protocol revenue figure was found on 24 Nov 2026. DefiLlama had no Zebec fees or revenue adapter when checked on 24 Nov 2026.

### Marketing claims vs what is on file

Official marketing and docs include “fully deflationary” language and claims that Super App fees automatically convert into ZBCN ([tokenomics](https://docs.zebec.io/zebec-protocol/tokenomics); [How ZBCN powers the Zebec SuperApp](https://zebec.io/blog/how-zbcn-powers-the-zebec-superapp)). Those claims conflict with the current on-file facts: ZIP-4 paused burns, and buyback inventory is held, not burned. This is a documentation conflict, not a score change.

### Official payroll-chain wording — discrepancy to reconcile, list not changed

This report’s Product section still lists Enterprise Payroll as live on Solana, Stellar, Canton, Aleo, Algorand, and Base, and separately marks Ripple / XRPL payroll as Confirmed. Official docs as of 24 Nov 2026, [Supported chains and assets](https://docs.zebec.io/zebec-application-suite/enterprise-payroll/supported-chains-and-assets), also say: “Solana, Stellar, XRP Ledger, and Canton are supported for both payroll and card products. All other chains are currently supported for card products only; payroll support is coming soon.” The same docs page lists additional chains in a table. **This is a discrepancy to reconcile. The listed chains in this report were not silently changed.**

### Livestream leads — Unverified

A 24 Nov 2026 public livestream (YouTube id `QMyED-T_Wfc`, Crypto Millie; released about 11:12 AM MST; duration 1:03:11) discussed Zebec distribution and showed on-screen posts attributed to CEO Simon Babakhani. YouTube is a lead source, not a primary official publication. The following remain **Unverified leads** until Zebec publishes them:

- Meetings with WisdomTree “this week” (on-screen post; no official Zebec blog confirmation found on 24 Nov 2026).
- A Midnight (NIGHT) partnership or hookup (livestream discussion; no official Zebec or Midnight confirmation found on 24 Nov 2026).
- “Payro Finance” as a named lending partner (the name appears in secondary coverage; no confirmed product page on zebec.io was found in this pass).
- Automatic conversion of Super App fees into ZBCN (repeated on the stream; conflicts with paused burns and held buyback inventory, as above).

A Stripe Tempo “chain deal” remains Unverified as a Zebec partnership, as already noted in this report. Official Tempo docs themselves state there is no native or separate gas token and that fees are paid in USD TIP-20 stablecoins ([Tempo network fees](https://tempo.xyz/developers/docs/network/fees); [pay fees in any stablecoin](https://developers.tempo.xyz/docs/guide/payments/pay-fees-in-any-stablecoin); [Stripe Tempo overview](https://docs.stripe.com/stablecoins/ecosystem/tempo)). That is a fact about Tempo, not a confirmation of a Zebec deal.

### Rails vs tokens — value-accrual context (opinion flagged)

A 24 Nov 2026 desk comparison of payments and TradFi rails with a public-token value-accrual path. **Opinion, clearly labelled:** large firms can use a settlement rail without issuing or sharing cash flow with a public token. When a project does have a public token, holder accrual is a documented mechanism, not a partnership headline. Evidence (not a score change):

| Rail or project | Official facts | Public-token value accrual |
|---|---|---|
| Tempo (Stripe + Paradigm) | Official docs: no native gas token; USD stablecoin fees. Design partners named on [Paradigm’s 4 Sep 2025 post](https://www.paradigm.xyz/writing/tempo-payments-first-blockchain). A reported $500M raise at a $5B valuation (Fortune, 17 Oct 2025, anonymous sources) is **Unverified** at the official Tempo / Stripe level. | No public Tempo token is documented in official docs. |
| HSBC–Uber on Canton (see the CC 24 Nov 2026 update) | Official 30 Oct 2026 joint release: tokenized deposits, Franklin Templeton Benji money-market fund, Tradeweb, Fireblocks, delivery-versus-payment, and a weekend partial redemption. Size not disclosed. | The official release does not state a CC fee or payout. Whether CC was burned is **Unverified**. |
| Zebec Super App / ZBCN | Official launch dates and self-reported volume as above. | The only official revenue-linked dollar figure is the about $100k Q3 buyback, held not burned. `revenue_reaches_holders` remains no. |
| ONDO (context only) | This desk’s ONDO report already records product fees and a token with no cash-flow claim. | Token earns nothing; no change in this update. |
| PLUME (context only) | This desk’s PLUME report already records small chain fees and vault fees to users and curators. | No burn; no change in this update. |

**Opinion (flagged):** a working payments or treasury rail is not the same thing as a token-holder claim on its fees. The HSBC–Uber pilot and Tempo’s official no-token fee design are examples of rails that can run without a documented payout to a public token. Zebec has a public token and a documented buyback, but the buyback is small, held rather than burned, and company volume claims are not published revenue.

## Treasury advisory 24 Nov 2026 (MST): a treasury-funded wallet network sends ZBCN to exchanges and DEX pools — reported only; the Real Rails treasury badge stays CAUTION

**Advisory: more investigation is needed.** This section reports evidence and a labelled hypothesis. It does not change the v3 score, the Selling gate result, the Real Rails treasury badge (still **CAUTION**), the formula or `revenue_reaches_holders`. Approved for publication by Madman on 24 Nov 2026.

**How labels are used (process rule P12).** Labels marked **Nansen-labeled** come from a single third-party labeler and are treated as leads, not primary sources. Every balance and transfer amount below was checked against a direct read of the public Solana mainnet RPC (`getTokenAccountsByOwner`, `getSignaturesForAddress`, `getTransaction`). Where a Nansen figure did not match the chain, it was discarded. "On-chain" means read straight from the chain. Times are MST.

### Research done

- 16 Nov 2026: on-chain trace of the published treasury hub [`9Sq2nZ48…`](https://solscan.io/account/9Sq2nZ481aiEkoDB9gavcfD6v7pr4LEcPnUdky4TEine) (see Selling A above).
- 24 Nov 2026, early morning MST: Nansen counterparty and label pulls (May 24 to Nov 24 2026) for the hub and its hop wallets, each cross-checked on-chain.
- 24 Nov 2026, about 3:30–4:40 PM MST: a free on-chain trace (H-22) of every ZBCN batch that [`71LxiE4P…`](https://solscan.io/account/71LxiE4PvxdZxLmtGcoKAJEWKofPqYw5Wdn6PSpXHodV) sent to [`EsDV3m3x…`](https://solscan.io/account/EsDV3m3xUZ7g8QKa1kFdbZT18nNz8ddGJRcTK84WDQ7k) from June to November 2026. All 19 recipient wallets were followed hop by hop, up to six hops, until the tokens reached a DEX pool account or a labeled exchange wallet. No paid data was used for this step. Exchange labels for the endpoints are Nansen labels that were already on file.

### Evidence trail

1. **Newest hub movement (on-chain).**
   - 19 Nov, 6:54 PM: the hub sent 10,553,119.34 ZBCN to [`D9sdqZtS…`](https://solscan.io/account/D9sdqZtSGfYV1gs6jCpQ7Ax3SnP6rxDChjm7qQYkpHVz) ([tx `2GJMgyizcG…`](https://solscan.io/tx/2GJMgyizcG4aUzgC9mevCfxek1ezPBXktw5W9mzfbq6eJjhHnjvQdSqXZJ2s8w8CzrC4FEGdxrXEiWnTohKgjqYA)).
   - 19 Nov, 8:06–8:08 PM: that wallet passed it to [`AoJhYbSr…`](https://solscan.io/account/AoJhYbSrNgKj1KkCiYpAnahqQveBVcCsZj79S8gz9Aw4).
   - 19 Nov, 8:10 PM: [`AoJhYbSr…`](https://solscan.io/account/AoJhYbSrNgKj1KkCiYpAnahqQveBVcCsZj79S8gz9Aw4) sent 10,553,119.42 ZBCN to [`3V11R3pE…`](https://solscan.io/account/3V11R3pEGSt5XeRaoLDcCdkAB8zVSaKRCm8y3uKBgnsr) ([tx `bxABE4ErR2…`](https://solscan.io/tx/bxABE4ErR2A1CDDkDZmE7u4CBfU1NUQ6B3wyJTpUWN1DqNwujC6ZoddU4gGzcYZmr7uFRsjQMnDvHmZaFSiCiQd)). The receiving wallet is **Nansen-labeled "BloFin"** (an exchange), and its ZBCN balance rose from 14.72M to 25.27M.
   - Hub to exchange took about 76 minutes. [`D9sdqZtS…`](https://solscan.io/account/D9sdqZtSGfYV1gs6jCpQ7Ax3SnP6rxDChjm7qQYkpHVz) was first funded in Apr 2024 by [`8mUKxVLf…`](https://solscan.io/account/8mUKxVLfHWBppvetbCDdQzmuSZRaaPyceN5AsNe8guTc), an earlier hub hop that emptied into DEX pools on 16 Nov. It also received 25.14M ZBCN from the hub between May and Nov and sold about 11M into Orca and Meteora pools.
2. **20 Nov, 8:56 AM (on-chain):** the hub sent 1,266,155.65 ZBCN to [`G9ZnxaE6…`](https://solscan.io/account/G9ZnxaE6t4d8pV6A5Fh5NMMDMfr3Rk5ne17XPCkzZFLR), which is **Nansen-labeled "ZBCN Distributor"**. That wallet swapped the tokens in the Orca SOL-ZBCN pool and sent SOL, USDC and USDT to a **Nansen-labeled MEXC deposit** address. It also traded with a wallet **Nansen-labeled "Wintermute"** (a market maker).
3. **15 Nov hop wallets** (Nansen counterparties, cross-checked with the 16 Nov on-chain trace):
   - [`ACjqBWqM…`](https://solscan.io/account/ACjqBWqMhcbDTbnWitdFohrJebHmSA7tmX23Awt7n54e): 14.48M ZBCN to **Nansen-labeled Gate**.
   - [`AqUuUe11…`](https://solscan.io/account/AqUuUe114vG8Q7UCQumkJLXPthZT44HQaU5MScinD1wk): 4.77M ZBCN to a deposit address, plus USDC to **Nansen-labeled Binance and Bybit** deposit addresses.
   - [`F9wCYEae…`](https://solscan.io/account/F9wCYEaem2CXEBjtmp8hAp7FEQD1KT6pDF6oaFLBLZDt): ZBCN into Orca and Meteora pools, plus USDC to a **Nansen-labeled Coinbase** deposit address.
   - [`3uWEqNcN…`](https://solscan.io/account/3uWEqNcNgUY8FpjPsH43Xq4prcyKAXhamo1amgy1trUw) and [`4h9huCdn…`](https://solscan.io/account/4h9huCdnPHHeUyFxBcEYRoYCr8cR9wnaPfHiv46T2VX7): 3.52M and 15.38M ZBCN to [`8N6eosfr…`](https://solscan.io/account/8N6eosfr2nzv5AwWpmwBfHBafyuvCNWr5T3ocjQbhDzc), which is **Nansen-labeled "KuCoin: Deposit"**.
   - [`2RBTh513…`](https://solscan.io/account/2RBTh513YHgaDg1WbqQNUbF3R8CQrMtuD72BREM1oitY): received 23,916,149 ZBCN (on-chain). It sells into Meteora and Orca pools (routed through OKX DEX and Jupiter, per Nansen) and held 11.66M on 24 Nov.
   - [`9acGHNrd…`](https://solscan.io/account/9acGHNrdibvN4tsqWhS5uQDeU2dzvXCr23TYKWYoAj2j) still holds all 5,586,647.50 ZBCN it received on 8 Nov.
4. **Stablecoin side.**
   - On 24 May 2026, 8:37 AM, the hub made the first deposit into [`EKC8EXTc…`](https://solscan.io/account/EKC8EXTc5AfVWk7RdfCgSy1nXAuFwxvMBuKohyrk1343) (0.25 SOL, [tx `5VdNmWXiCw…`](https://solscan.io/tx/5VdNmWXiCw9hi4J3PtSU1xGUqoY5Kk42t8i49x68gTqV1AAdodcN3UGKBvXPgbx2E78Dn7P8oSZTDTrpEdJy27nu)). That wallet sends USDC to the hop wallets and to **Nansen-labeled** MEXC, Bybit and Kraken deposit addresses. It also receives from **Nansen-labeled** Bybit and MEXC hot wallets.
   - A second feeder, [`27ems4HF…`](https://solscan.io/account/27ems4HFoKuFnHz2oLTcGfayL2rox22xw6A7jKUwRV3u), was first funded by a **Nansen-labeled** MEXC wallet. It funds the hop wallets and moves stablecoins with [`DEXUMunp…`](https://solscan.io/account/DEXUMunpdMfySXahhQ89VVhV6ZWgCr1E6X7oJoaFVt2u) (first funded by a **Nansen-labeled** Binance wallet) and [`A1gEhBYV…`](https://solscan.io/account/A1gEhBYV6N6VbEESUJVBB8de7MZwYfr2LVWmxxbRubNc).
   - **On-chain:** [`EsDV3m3x…`](https://solscan.io/account/EsDV3m3xUZ7g8QKa1kFdbZT18nNz8ddGJRcTK84WDQ7k) sent 642,135.63 USDC and 26,757.04 USDT (about $669K) to [`27ems4HF…`](https://solscan.io/account/27ems4HFoKuFnHz2oLTcGfayL2rox22xw6A7jKUwRV3u) between 4 Jun and 5 Nov 2026. Most of it went in roughly monthly lots of about $90K–$100K, often after a small test send.
5. **No Nansen label** exists for [`9acGHNrd…`](https://solscan.io/account/9acGHNrdibvN4tsqWhS5uQDeU2dzvXCr23TYKWYoAj2j), [`2RBTh513…`](https://solscan.io/account/2RBTh513YHgaDg1WbqQNUbF3R8CQrMtuD72BREM1oitY), [`ACjqBWqM…`](https://solscan.io/account/ACjqBWqMhcbDTbnWitdFohrJebHmSA7tmX23Awt7n54e), [`EKC8EXTc…`](https://solscan.io/account/EKC8EXTc5AfVWk7RdfCgSy1nXAuFwxvMBuKohyrk1343), [`27ems4HF…`](https://solscan.io/account/27ems4HFoKuFnHz2oLTcGfayL2rox22xw6A7jKUwRV3u), [`D9sdqZtS…`](https://solscan.io/account/D9sdqZtSGfYV1gs6jCpQ7Ax3SnP6rxDChjm7qQYkpHVz) or [`4h9huCdn…`](https://solscan.io/account/4h9huCdnPHHeUyFxBcEYRoYCr8cR9wnaPfHiv46T2VX7).
6. **Upstream reserve (on-chain).**
   - [`3J7n5Usm…`](https://solscan.io/account/3J7n5Usmei8BqgUHan5xuBiJkAx6M1AQQhGwbKiVdQ17) sent 500,000,000 ZBCN to the hub on 21 Aug 2026, 9:10 AM ([tx `3waNh14q2e…`](https://solscan.io/tx/3waNh14q2e839J9HuVU9CUupqUQEw9y7fHUDGCHSHKjuKnkdE2DxRqyv2ZKdCdWyHosapJWJkeE7ycUXRig9y67V)). It holds 5,500,000,100 ZBCN (5.50% of supply).
   - It received 7B ZBCN from [`EsDV3m3x…`](https://solscan.io/account/EsDV3m3xUZ7g8QKa1kFdbZT18nNz8ddGJRcTK84WDQ7k) and sent 1B back on 26 Apr 2026, 8:54 PM ([tx `NrDf71uT1A…`](https://solscan.io/tx/NrDf71uT1AVttCaxUQgQRAuyRksc8R8b2Jo1hCUoh5SDe21SLyNe5stccak3J8nuof5pcR6AckctS3d9KQVuyno)).
   - [`H8Hr964A…`](https://solscan.io/account/H8Hr964ApEP3ie1rwRTT7wkSrgvUqJQb8oNAKspkDDfR) holds 7,000,217,587 ZBCN (7.00%). Its only outflow in 12 months was 318M on 3 Oct 2026 ([tx `bKKdrJV7kB…`](https://solscan.io/tx/bKKdrJV7kBSTozJiVJGCoHTLp27JSsA1ex1mCY7ytPfmUgNquLeH5mWGpLKZsT3zoNkQ8Tx3BJUWhXs8NBXFbhU)).
7. **Address poisoning.** Many zero-value lookalike addresses interact with these wallets. That is spam, not treasury activity.
8. **The ~1.02B ZBCN from [`71LxiE4P…`](https://solscan.io/account/71LxiE4PvxdZxLmtGcoKAJEWKofPqYw5Wdn6PSpXHodV) (H-22, on-chain).**
   - **Source.** [`71LxiE4P…`](https://solscan.io/account/71LxiE4PvxdZxLmtGcoKAJEWKofPqYw5Wdn6PSpXHodV) is a plain wallet. It received 25.11B ZBCN from [`GXD2FnXi…`](https://solscan.io/account/GXD2FnXi718y9tPUd6CW1CW6khZ14DGtQc5cBpYkjm5J), an account owned by Zebec's streaming program [`zbcKGdAm…`](https://solscan.io/account/zbcKGdAmXfthXY3rEPBzexVByT2cqRqCZb9NwWdGQ2T) (**Nansen-labeled** "Zebec Network: ZBCN Distributor"). The stream paid about 1B a month from Feb 2025 until 16 Mar 2026 (last regular payment 965M, [tx `4CR5FnfiCT…`](https://solscan.io/tx/4CR5FnfiCTcRPDhC2eQDgoFvevAQK4MSHauUrcrNgQDc5xqtGc64XyfWSfx3Q3MGyV8YTQZDxUQgEEycfgjaG1ja)). After that it only relayed hub and vault tokens: 500M on 21 Aug 2026 and 353M on 3 Oct 2026. The wallet still holds **243,300,463.61 ZBCN** (24 Nov, 3:36 PM).
   - **Vesting check.** This report's tokenomics already records the last scheduled unlock as March 2026, with all 100B released. The stream's end date matches that schedule. The ~1.02B moved from June to November 2026 is therefore **not a new scheduled unlock**. It is already-unlocked inventory being released.
   - **Batches to [`EsDV3m3x…`](https://solscan.io/account/EsDV3m3xUZ7g8QKa1kFdbZT18nNz8ddGJRcTK84WDQ7k).** Between 20 Jun and 23 Nov 2026 there were 11 batches totalling 1,023,600,000 ZBCN, for example 333.3M on 29 Sep, 10:11 PM ([tx `4HbiXD2wPn…`](https://solscan.io/tx/4HbiXD2wPnmWd8xz7KzoDuhfezbpikN1scNPQoXEgWUDf3v1ZwVK7vDF6SzBa5fVXBCsZ6rx9iXA9HmzPvXsz1m)) and 204M on 11 Sep, 9:24 PM ([tx `33c3mc7yja…`](https://solscan.io/tx/33c3mc7yjaqaPZWVC8WEmQmDaFv4F9rNNhyZ6drmmnKDB21MqpmCgT7HEDzD9hqecTHVuu2iQtaPdwJLBcqfXPr2)).
   - **Pattern.** Every batch starts with a 10–1,000 ZBCN test send. Within minutes the batch is split between one or two fresh wallets, which forward it through single-use hop wallets. All 19 recipients now hold 0 ZBCN.

   | Recipient | ZBCN from [`EsDV3m3x…`](https://solscan.io/account/EsDV3m3xUZ7g8QKa1kFdbZT18nNz8ddGJRcTK84WDQ7k) (MST) | Where it ended (pro rata through hops) |
   |---|---|---|
   | [`DoBTtiH3…`](https://solscan.io/account/DoBTtiH3q4WC1R4h1bywhELzxWEYXqep6FzmJgvH65tR) | 166,650,000 on 29 Sep, 10:15 PM ([tx `2RJaivxfxm…`](https://solscan.io/tx/2RJaivxfxm31XLYTDNLmEWmeTTcDV89eTqfY1VSPntENmohaKLoe6zgofsraDerHL3tmFQK2Aqu8WvSMdJorx3PP)) | 105.0M to the **Nansen-labeled** OKX hot wallet [`C68a6RCG…`](https://solscan.io/account/C68a6RCGLiPskbPYtAcsCjhG8tfTWYcoB4JjCrXFdqyo), e.g. 18M on 30 Sep, 2:36 AM ([tx `7PpVMjTKaA…`](https://solscan.io/tx/7PpVMjTKaA37ZXYTcyiMTcr5VMoeWpws63qZEPsJM8NywJkdAYLc1BkJyUM9sqTMFQULHckWSeb7e6SrvE8yPbm)); 31.7M to the **Nansen-labeled** Bitget hot wallet [`A77HErqt…`](https://solscan.io/account/A77HErqtfN1hLLpvZ9pCtu66FEtM8BveoaKbbMoZ4RiR); 30M passed to [`23c1Ryrg…`](https://solscan.io/account/23c1Ryrg4yxJytMGEebDTqNTeyrd5yZ1kNXkMbxpGTWT) |
   | [`23c1Ryrg…`](https://solscan.io/account/23c1Ryrg4yxJytMGEebDTqNTeyrd5yZ1kNXkMbxpGTWT) | 166,649,800 on 29 Sep, 10:15 PM ([tx `5fd5rpQuLv…`](https://solscan.io/tx/5fd5rpQuLv6K41qhBrdtKf3n8uirt4oZHB4AtPFdgraWCRFf85RqjpSzviU4t36p8RfmkJgd5gxyEwSrtfVEjSak)) | 69.7M to the **Nansen-labeled** Gate wallet [`u6PJ8DtQ…`](https://solscan.io/account/u6PJ8DtQuPFnfmwHbGFULQ4u4EgjDiyYKjVEsynXq2w); 56.3M sold into the Orca and Meteora pools, e.g. 30 Sep, 10:28 PM ([tx `3NGf2C9JaZ…`](https://solscan.io/tx/3NGf2C9JaZhkjrjzGc7KZkMgS5x3mEv8X9xStCmrJ5QHXQA4BCzrYDLQDAh83cwk2dWdmX5hHaENLnjLRuVrjA3p)); 30M to OKX; 30M to the **Nansen-labeled** "Trading Bot" [`4GQeEya6…`](https://solscan.io/account/4GQeEya6ZTwvXre4Br6ZfDyfe2WQMkcDz2QbkJZazVqS); 10M to Bitget |
   | [`DU7Nxvum…`](https://solscan.io/account/DU7NxvumXU8RYmzWadPHeMbNVcC8sx9mhsEfGu5Ye73E) | 102,000,000 on 11 Sep, 9:26 PM ([tx `5XK8AkqeMA…`](https://solscan.io/tx/5XK8AkqeMAht1X8B1kfQHzk9B5RvHr5ip5hQdebobmSdunGBJ9oqLYMyjUuiisA4ZzPhJCBtuNKYikPG21Qh9fY6)) | All 102M to Bitget, e.g. 21M on 12 Sep, 10:14 AM ([tx `2iL6FEDq2W…`](https://solscan.io/tx/2iL6FEDq2WArFopzRh6pycNCBn8xRKpU7QPEBaAW1NzvHAzoJjWFPwvWXHRqLfHdm6tkk3XeCB4PCYuTfxsciBcZ)) |
   | [`DP5U1C6T…`](https://solscan.io/account/DP5U1C6TdwbdcQVwXPFCopFL3y3zba2PWB68jsCqrU3S) | 101,998,000 on 11 Sep, 9:27 PM ([tx `5VwmwYNRST…`](https://solscan.io/tx/5VwmwYNRST5tPzNw14oXPH1M1xfqwqu2GcUrFrXrG1YjkpBomVtJVhoUh9cAGxtLoBAKbREC7bhaUQHBmMK9bL6g)) | All 102M to Bitget, e.g. 20M on 20 Sep, 8:38 AM ([tx `4n9DEy3Mfb…`](https://solscan.io/tx/4n9DEy3MfbtFtLzBfyG48UCFBLgFdeUkhKyRYK3aauAYpu7UoPBbPrzATwSt61HHCsjeuC9gHyn7i8US7xMxvwBz)) |
   | [`AHrdAPnn…`](https://solscan.io/account/AHrdAPnnPbUW2MeYiddAwmd8J4zmzNbcKiYzYfK3kqaY) | 85,099,900 on 2 Nov, 12:45 AM ([tx `4KxbKdzgs5…`](https://solscan.io/tx/4KxbKdzgs5jJhEZYvMSr7bZiersWKqRng99PaibGFNRth5Tz8VDEZ3o4NjQLNLLpu1BHhqyCbBNck5Q6tXSdErQ2)) | All 85.1M sold into the Orca and Meteora pools between 2 and 4 Nov, e.g. 15.1M on 2 Nov, 2:49 AM ([tx `3SaA42ZECp…`](https://solscan.io/tx/3SaA42ZECpDdN19wDx6TB5JXeShCestZtifXECEs3s6GuCUJ9Yhq94nJqGJv5hZWn7ZdESb3cW3NKmD3Ckv4UBbV)) |
   | [`7qeeXnwu…`](https://solscan.io/account/7qeeXnwuddtTQrqWmk1VrMeSQ4NSsDCVjMsdjfKGifvv) | 75,754,320 on 15 Jun, 8:41 AM ([tx `5K3hsNDfXD…`](https://solscan.io/tx/5K3hsNDfXD8b5pohRApfzmRJw5Vyaz5xhcuqLz3DkwPbAQHyzMxjT7jXa1guxdPkfetRmYteZckMgUPUDRYXV31V)) | All 75.75M to Bitget, e.g. 13.75M on 15 Jun, 7:12 PM ([tx `3yT8Dy8qev…`](https://solscan.io/tx/3yT8Dy8qevVSap73tuqnQg695eqiNcjPqCVgKjCcR8q3vs4FUr74g5hmBcN976M7rejeQs68Get1tqBbwMD9hrbv)) |
   | [`4cbBMqgi…`](https://solscan.io/account/4cbBMqgin3JftR1U7HbgBmkLrke8hWq8gMu48xU5w99r) | 75,750,000 on 15 Jun, 8:40 AM ([tx `4SgB4JwN23…`](https://solscan.io/tx/4SgB4JwN23DCB7krmdLiEU6NXYDzNcYgHxV3AqLqa8mczQeotQu2xqgWHbfXoQ5p9heWC2rHFXUGbM84evYsXF5t)) | All 75.75M to Bitget, e.g. 13.0M on 16 Jun, 8:13 PM ([tx `3msvgkaGTP…`](https://solscan.io/tx/3msvgkaGTPU5KUgAXdnoP3GGbHr7zb52yejU69k2A8o2f1iPAYjUuR8dzwtaZHzkWsATpSMQfSVt5Pcs3Vvfe7y)) |

   - **The 15 Jun pair.** [`7qeeXnwu…`](https://solscan.io/account/7qeeXnwuddtTQrqWmk1VrMeSQ4NSsDCVjMsdjfKGifvv) and [`4cbBMqgi…`](https://solscan.io/account/4cbBMqgin3JftR1U7HbgBmkLrke8hWq8gMu48xU5w99r) were paid from [`EsDV3m3x…`](https://solscan.io/account/EsDV3m3xUZ7g8QKa1kFdbZT18nNz8ddGJRcTK84WDQ7k)'s May inventory (242.1M from [`71LxiE4P…`](https://solscan.io/account/71LxiE4PvxdZxLmtGcoKAJEWKofPqYw5Wdn6PSpXHodV) on 19 and 21 May), not from the June–November batches.
   - **Totals.** The 19 recipients received 1,175.1M ZBCN in all. About 607.5M reached the **Nansen-labeled** Bitget hot wallet [`A77HErqt…`](https://solscan.io/account/A77HErqtfN1hLLpvZ9pCtu66FEtM8BveoaKbbMoZ4RiR), 135.0M the **Nansen-labeled** OKX hot wallet [`C68a6RCG…`](https://solscan.io/account/C68a6RCGLiPskbPYtAcsCjhG8tfTWYcoB4JjCrXFdqyo), and 106.9M the **Nansen-labeled** Gate wallet [`u6PJ8DtQ…`](https://solscan.io/account/u6PJ8DtQuPFnfmwHbGFULQ4u4EgjDiyYKjVEsynXq2w). About 285.5M was sold directly into the ZBCN pools: Orca [`FaoZEZFs…`](https://solscan.io/account/FaoZEZFsRS2jJAzg5PXwNjDdA1hDAjDGAkDf4xRfY79w) and Meteora [`6Mo8W6b6…`](https://solscan.io/account/6Mo8W6b67brHWokLNeXPdfwH7B1ir3xYCGd4EcBen6eM), [`5VXPSSnS…`](https://solscan.io/account/5VXPSSnSxa2bP9HPdHXt9pCXVyfwXwRN8HRE2pyoN88M) and [`7U8DUKAd…`](https://solscan.io/account/7U8DUKAds4SKeKU9zWNdM6iVXrsLc7fx8VUY5sw2zjWz), all owned by the Orca Whirlpool and Meteora DLMM programs (on-chain). Another 40.3M went to the "Trading Bot" wallet.
   - **On-chain checks.** The three exchange wallets each show at least 300 recent signatures (Bitget 22,200 SOL, Gate 100,725 SOL), which is exchange scale. A pool deposit is a swap. For example, on 23 Nov 2026, 8:20 PM, a hop wallet sold 17,000,000 ZBCN into the Orca and Meteora pools through Jupiter and received about 414.8 SOL ([tx `4r772XxDvr…`](https://solscan.io/tx/4r772XxDvrikD3fRr7bGunw3HY3kEUnUv1v1V3SyDYbNVnytNvKb5zhc5cBe7aWJnF1cFx91bbc89vZBLZg2GNpb)).
   - **Newest batches.**
     - 22 Nov, 6:30 PM: 68M ZBCN went from [`71LxiE4P…`](https://solscan.io/account/71LxiE4PvxdZxLmtGcoKAJEWKofPqYw5Wdn6PSpXHodV) to [`EsDV3m3x…`](https://solscan.io/account/EsDV3m3xUZ7g8QKa1kFdbZT18nNz8ddGJRcTK84WDQ7k) ([tx `2NQtA9MB4S…`](https://solscan.io/tx/2NQtA9MB4SBC4iqJfvdPCATPjU5huYryPVFXxwQ3cvYbftjKzaiENqXpYSwzNbbFrgqGdKaSF1uBabimwLqcCn5Z)). It was sold into the pools between 6:51 PM and 10:44 PM, for example [tx `2VfhnHqbdL…`](https://solscan.io/tx/2VfhnHqbdLPWBb5bQbVMRicKznmXvj8uS7rxQPWCpGDUdjsZXpa5pZndCjyaHEdxCyP5PXd5LTQEyPJCzFC3dN7N) and [tx `62QmT9zhGR…`](https://solscan.io/tx/62QmT9zhGRRB2gSiiuEH7DrvVsc8pjA4cgB2ZQSJ5ypU8zXcGNePk21YAPTEqgmpENoK51T15YZYHbRYzB4xH6a4).
     - 23 Nov, 8:09 PM: another 17M took the same route ([tx `JNwu2q5KYg…`](https://solscan.io/tx/JNwu2q5KYgfoYUWAobWSZX39oFRWaKjFMxcpgX9utA5rMD6RjH8oYgUguNKaHAY7wGfYRDmxqvGaD3jGSqzAt65)) and was sold 11 minutes later.
   - **Approximation note.** A few reused hop wallets also carried older, unrelated flows, so the per-endpoint splits are approximate. The totals reconcile.

### Hypothesis (labeled, Unverified)

**Assumed purpose:** [`71LxiE4P…`](https://solscan.io/account/71LxiE4PvxdZxLmtGcoKAJEWKofPqYw5Wdn6PSpXHodV) is likely a Zebec-side unlock and distribution wallet: Zebec's own streaming program funded it, and it tops up the published hub. [`EsDV3m3x…`](https://solscan.io/account/EsDV3m3xUZ7g8QKa1kFdbZT18nNz8ddGJRcTK84WDQ7k) likely runs a selling or liquidity programme for it, as does the hub's hop-wallet network. Each one-hop or multi-hop route ends at exchange hot wallets or deposit addresses (Bitget, OKX, Gate, BloFin, KuCoin, Binance) or in DEX pools within hours. A treasury-funded wallet cycles stablecoins between exchanges and the hop wallets.

- **Alternatives:** (a) a market maker or OTC desk paid in ZBCN by Zebec, selling or making markets on its own account (the "ZBCN Distributor" and Wintermute links would fit this); (b) OTC buyers' own wallets; (c) exchange deposits that are custody or OTC settlement rather than sales.
- **Not proven:** who signs for [`71LxiE4P…`](https://solscan.io/account/71LxiE4PvxdZxLmtGcoKAJEWKofPqYw5Wdn6PSpXHodV) or [`EsDV3m3x…`](https://solscan.io/account/EsDV3m3xUZ7g8QKa1kFdbZT18nNz8ddGJRcTK84WDQ7k). No public Zebec disclosure names either wallet.

### Advisory and next steps

**More investigation is needed.** This advisory does not change the badge or score.

- **Would clear it:** Zebec names [`71LxiE4P…`](https://solscan.io/account/71LxiE4PvxdZxLmtGcoKAJEWKofPqYw5Wdn6PSpXHodV), [`EsDV3m3x…`](https://solscan.io/account/EsDV3m3xUZ7g8QKa1kFdbZT18nNz8ddGJRcTK84WDQ7k), the hop wallets and [`EKC8EXTc…`](https://solscan.io/account/EKC8EXTc5AfVWk7RdfCgSy1nXAuFwxvMBuKohyrk1343) as disclosed market-making, OTC or custody arrangements.
- **Would escalate it:** proof of sale into a pump window by a confirmed Zebec wallet, or a repeated pattern that meets the Option B FAIL bar.
- **Open items:**
  - Ask Zebec who controls [`71LxiE4P…`](https://solscan.io/account/71LxiE4PvxdZxLmtGcoKAJEWKofPqYw5Wdn6PSpXHodV) and [`EsDV3m3x…`](https://solscan.io/account/EsDV3m3xUZ7g8QKa1kFdbZT18nNz8ddGJRcTK84WDQ7k).
  - Read the creator and terms of the stream account [`GXD2FnXi…`](https://solscan.io/account/GXD2FnXi718y9tPUd6CW1CW6khZ14DGtQc5cBpYkjm5J).
  - Trace the onward flow of the "Trading Bot" wallet [`4GQeEya6…`](https://solscan.io/account/4GQeEya6ZTwvXre4Br6ZfDyfe2WQMkcDz2QbkJZazVqS) (40.3M).
- **Monitoring:** these wallets are on the desk's monthly treasury watch: the hub hop and feeder wallets, [`3J7n5Usm…`](https://solscan.io/account/3J7n5Usmei8BqgUHan5xuBiJkAx6M1AQQhGwbKiVdQ17), [`EsDV3m3x…`](https://solscan.io/account/EsDV3m3xUZ7g8QKa1kFdbZT18nNz8ddGJRcTK84WDQ7k) and [`H8Hr964A…`](https://solscan.io/account/H8Hr964ApEP3ie1rwRTT7wkSrgvUqJQb8oNAKspkDDfR). [`71LxiE4P…`](https://solscan.io/account/71LxiE4PvxdZxLmtGcoKAJEWKofPqYw5Wdn6PSpXHodV) (243.3M ZBCN still held) is proposed for the watch.

## Nansen-month findings, 24 Nov 2026 (MST) — reported only, unscored

This appendix publishes findings from the desk's 24 Nov 2026 holder and treasury research. It does not change the v3 score, badge, gates, formula or `revenue_reaches_holders`. Labels marked **Nansen-labeled** come from one third-party labeler and are treated as leads. Under process rule P12, every Nansen balance or holder figure used here was checked against a direct on-chain read before use, and mismatches were discarded. Hypotheses are labelled **Unverified**. Times are MST.

### P12 recheck of earlier Nansen figures (24 Nov 2026)
- Every Nansen number in the treasury advisory above was re-read on-chain with free Solana RPC (token-balance deltas, 24 May to 24 Nov 2026), and all of them matched:
  - `ACjqBWqM…` → Gate: 14,475,374 ZBCN.
  - `AqUuUe11…`: 4,773,751 ZBCN, plus 41,163 USDC and 2,211 USDT to a Binance-labeled deposit and 10,000 USDC to a Bybit-labeled deposit.
  - `3uWEqNcN…` and `4h9huCdn…` → KuCoin deposit: 3,523,512 and 15,380,168 ZBCN.
  - `9acGHN…` holds 5,586,647.50 ZBCN.
  - `D9sdqZtS…`: 25,140,906 ZBCN in; about 11.02M out to Orca and Meteora.
  - `2RBTh513…`: 23,916,149 ZBCN in.
  - `EsDV3m3x…` → `27ems4HF…`: 642,135.63 USDC and 26,757.04 USDT.
- One wording fix: Nansen names aggregator routers (OKX DEX, Jupiter) for `2RBTh513…`'s sales, but the chain shows the tokens ending in the Meteora and Orca pools (and 5.86M to Meteora pool account `7U8DUKAd…`). No data fix was needed.

### Holder mix (top 100 holders)
- Exchange share of the top 100 holders: **21.53%** of supply in Nansen-labeled exchange and DEX-pool wallets (Nansen holders pass, 24 Nov 2026).
- Issuer and other named holders: No issuer-labeled wallet in the top 10 (Nansen project-labeled share 0.22%). The two unlabeled holders with 7.00% and 5.50% (H8Hr964A and 3J7n5Usm) are covered in the advisory above.
- Checked on-chain: Solana token-account reads (`getTokenAccountsByOwner`, `getTokenSupply`, public mainnet RPC), 24 Nov 2026, about 4:35 AM MST; every figure matched. The exchange share itself is Nansen's top-100 sum and was checked on-chain only through its largest wallets.
- Unscored: this line has no effect on the score, badge or ranking. Labels are Nansen's (a third-party labeler) and are leads, not confirmed ownership.
