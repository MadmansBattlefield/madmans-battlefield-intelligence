---
ticker: CARDS
name: Collector Crypt
chain: solana
contract: "CARDSccUMFKoPRZxt5vt3ksUbxEFEcnZ3H2pd3dKxYjp"
overall_score: 4.7
overall_verdict: FAIL
section_scores:
  revenue: 5
  foundation_team: 5
  insider_holdings: 3
  selling_behavior: 4
  tokenomics_supply: 4
  liquidity_market: 5
  product_development: 6
  adoption_customers: 7
  security_audits: 5
  regulatory: 4
  catalysts: 4
gates_failed: []
red_lines:
  hack_exploit: none
  mint_path_live: "no (mintAuthority and freezeAuthority are null, read 16 Nov 2026)"
  team_wallet_to_exchange_during_pump: "not proven (no treasury CARDS reached a labelled exchange on a pump day in the wallets traced)"
  one_hop_sale_status: none_found
  treasury_to_exchange: "yes, not a pump day (treasury multisig -> fresh relay 4JTA… -> Coinbase deposit -> Coinbase hot wallet, 7,000,000 CARDS, 6 Nov 2026; no disclosure found)"
  treasury_to_market_maker: "yes, undisclosed: 60M CARDS from treasury-funded cards.sol (redFW…) went 8Qvd… -> 2asR… -> Fireblocks custody 6rQG…, which sends 0.4–2M lots to GSR Markets custody (Arkham, Tier B); pump-day timing not tested"
  treasury_pump_day_outflows: "14 Jun 2026 (9.5M via a multisig signer to a reward-claim vault) and 5 Oct 2026 (1.25M to unlabelled DFEstp…, onward owner [Unverified])"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "Company-run buybacks are discretionary and tiny relative to its revenue (~$1 to holders per $225 kept); nothing is automatic or obligated. Holders have no live claim on revenue; the score describes the business, not holder accrual."
pump_day_price_source: "CoinGecko daily closes"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions: []
price_usd: 0.1496
price_source: "CoinGecko, 16 Nov 2026 5:08 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### CARDS · Overall grade **4.7 / 10 · ❌ FAIL**

**Summary:** Collector Crypt runs a real, busy business: gacha packs backed by graded trading cards, with **$106.2M of revenue (net of pack buybacks) in the last 12 months** on DefiLlama. But the token gets very little of it: only **$471K** went to CARDS buy-and-burn in the same 12 months (about 0.4%). The company's own Squads multisig treasury still holds **54.8% of supply**, unlocked, and team, advisor and seed tokens are unlocking about **44.8M CARDS a month until Jul 2027**. The mint can't create new tokens, which is good. But on 6 Nov 2026 the treasury sent **7M CARDS to Coinbase** through a fresh wallet, with no announcement found, and an Arkham pass shows a 60M-CARDS branch paid out of the company ops wallet ends at a custody wallet that feeds **GSR Markets**, a market maker.

**🚨 Top warning:** the published treasury wallet [`3PnV…F1QB`](https://solscan.io/account/3PnVBrb4wPLFLW38oaYR7dA6HSfKpawxHGESPj5kF1QB) (named on [collectorcrypt.com/tokenomics](https://collectorcrypt.com/tokenomics)) sent **7,000,000 CARDS (≈ $1.7M at that day's close)** to a fresh wallet [`4JTA…Ajnq`](https://solscan.io/account/4JTAa4ZbKKQuVef229Y54S26JXNzdb6GknpAYDL7Ajnq) (Arkham: first funder is the Squads vault "CARDS Treasury", [Arkham](https://intel.arkm.com/explorer/address/4JTAa4ZbKKQuVef229Y54S26JXNzdb6GknpAYDL7Ajnq)): a 100 test on [3 Nov](https://solscan.io/tx/5fFNVhxw2egpdDQNd5AA6KvJNGhJuoXCzfKYSVMkGUAHqS2hMeqTkvesU8wfczL3HRgNp9mqrPsijwiWhwEcHcpk), then [6,999,900 on 4 Nov](https://solscan.io/tx/5t6a4JZ1gsUJ9bEXWfiveGLeXgGG6d3TDXtv2CXt4bDij33qL64sBT3wKRBKkSLqnip8QX8bCVKw92Jo8tpPXK4g). On 6 Nov 2026 that wallet [paid all 7M into Coinbase deposit `E1t8…82U1` (Nansen and Arkham labels)](https://solscan.io/tx/2cr5JGxAfU87jMoqKMqRwqNCNPEZsvgwT1k8JNR2C8rvj1ivTukUdeq9LaGBkRnVyT5hpX2bajD6kW4ZM2KFx1vM), and [4 minutes later it was swept to "Coinbase: Hot Wallet" `H8sM…3WjS`](https://solscan.io/tx/5EY3dWwb9ojw7wR6cUhWLWfSwfGdDDip1YWXumyceDdJ2bRHJmKjrCc7kwqBxMZh4rthkFQtiZJ4Be7STqDfGueT). That day was **not** a pump day (+5.8% over 5 days). Holding 54.8% of supply in one unlocked multisig is the bigger structural risk. Every link is repeated in the 🔗 Evidence trail below.

**Sections passed: 2 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 5/10 | ❌ FAIL |
| 🏛️ Foundation & team | 5/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 3/10 | ❌ FAIL |
| 📉 Selling behavior | 4/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 4/10 | ❌ FAIL |
| 💧 Liquidity & market | 5/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 6/10 | ✅ PASS |
| 🤝 Adoption & customers | 7/10 | ✅ PASS |
| 🛡️ Security & audits | 5/10 | ❌ FAIL |
| ⚖️ Regulatory | 4/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 4/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

> **Arkham pass, 16 Nov 2026:** no score change. Arkham confirms the 6 Nov relay and the escrows are funded by the Squads "CARDS Treasury" vault and that `E1t8…` is a Coinbase deposit. New: the 60M branch paid out of `cards.sol` ends at Fireblocks custody `6rQG…`, which sends CARDS to **GSR Markets** custody, so it reads as market-maker inventory. Selling stays at 4: an undisclosed market-maker route is a yellow flag, but no pump-day sale was proven.

---


# 🪪 CARDS · Collector Crypt · 4.7 / 10 · ❌ FAIL

> **One line:** A real gacha-pack business with about $106M a year in net revenue, but the token is an afterthought: about 0.4% of revenue goes to buy-and-burn, the company multisig holds 54.8% of supply, about 403M CARDS are still to unlock by Jul 2027, and 7M treasury CARDS went to Coinbase on 6 Nov 2026 without an announcement.

| 📊 Market (CoinGecko, 16 Nov 2026 5:08 AM MST) | 🔗 On-chain (Solana, 16 Nov 2026) |
|---|---|
| **Price** $0.1496 | **Mint** [`CARDS…xYjp`](https://solscan.io/token/CARDSccUMFKoPRZxt5vt3ksUbxEFEcnZ3H2pd3dKxYjp), SPL Token, 6 decimals |
| **24h / 7d / 30d** 🔴 −12.4% / −27.7% / −48.7% · 1y +129.8% | **Supply** 1,972,174,887.42 (2.0B minted, ~27.8M burned) |
| **Market cap** $133.3M · **FDV** $295.2M | **mintAuthority / freezeAuthority** null / null ✅ |
| **24h volume** $4.66M | **Treasury** [`3PnV…F1QB`](https://solscan.io/account/3PnVBrb4wPLFLW38oaYR7dA6HSfKpawxHGESPj5kF1QB) (Squads vault) 1,081,261,037 CARDS (54.8%) |
| **ATH** $0.3825 (21 Oct 2026) · now −60.9% | **Main pool** Raydium CLMM CARDS/USDC [`Hnhp…23tD`](https://solscan.io/account/HnhpJPJgBG2KwniMTNW8cVBHvk1hFog3RC3kjnyc23tD) |
| **Circulating** 890.9M (CoinGecko) · 500.2M (company definition) | **Buyback wallet** [`3nGN…9Kq`](https://solscan.io/account/3nGNwiz1qevPjhEoQi1dLj16oTkjmbevTnpV9piWY7Kq) 100,527 CARDS |

---

## 💰 Revenue — Does it make money? · 5/10 · ❌ FAIL

| Metric | Value | Source |
|---|---:|---|
| Revenue, last 12 months (pack sales + royalties **net of pack buybacks**, plus treasury LP fees) | **$106.24M** (30d $12.67M, all-time $124.36M) | [Tier A] [DefiLlama fees/revenue API](https://api.llama.fi/summary/fees/collector-crypt?dataType=dailyRevenue), read 16 Nov 2026 |
| Monthly revenue trend | Oct 2026 $18.84M (record) · Sep $12.53M · Jun $16.12M · Jan $4.42M | [Tier A] same |
| Paid to CARDS holders (buy-and-burn), 12 months | **$471K** (30d $360K) ≈ 0.44% of revenue | [Tier A] [DefiLlama holders revenue](https://api.llama.fi/summary/fees/collector-crypt?dataType=dailyHoldersRevenue) |
| Burns listed by the company | 22,485,689.90 (29 Aug 2026) · 3,055,864.00 (1 Oct) · 1,981,942.69 (3 Nov) · total 27,824,510.82 | [Tier A] [collectorcrypt.com/tokenomics](https://collectorcrypt.com/tokenomics) · on-chain supply 1,972,174,887.42 agrees to ~0.6K |
| Holder rights | None by contract. Buybacks are discretionary ("LP fees and buybacks (if any)") | [Tier A] tokenomics page |

**What it means:** The business is real and growing, and it earns more than most tokens on this list. The token gets almost none of it: holders received about **$1 for every $225** the company kept, and nothing obliges the company to keep buying. That is better than a token with no business (QNT scored 4 for an optional, unmeasured sink), so **5**, but well short of a pass.

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** Company-run buybacks are discretionary and tiny relative to its revenue (~$1 to holders per $225 kept); nothing is automatic or obligated. Holders have no live claim on revenue; the score describes the business, not holder accrual.

## 🏛️ Foundation & team — Who is in charge? · 5/10 · ❌ FAIL

| Item | Finding | Source |
|---|---|---|
| Operator | Collector Crypt, which publishes the token mint, the treasury and the buyback wallet | [Tier A] [tokenomics page](https://collectorcrypt.com/tokenomics) |
| Treasury control | `3PnV…` is a **Squads multisig vault**: every treasury move runs through `VaultTransactionExecute` (program `SQDS4ep6…`). Executors seen: `Gxms…`, `By8Z…`, `HWPR…`, `C4mK…`, `3C7J…` | [Tier A] e.g. [Streamflow create tx](https://solscan.io/tx/5ucuMxxQJsFdJKUAbymzte9khTXe6aZHtHRxBXvnZHpW9DmThZ7h3wAN36EZuEjqMKD5EJ2xin5xm5TofYpLi2hb) |
| `cards.sol` | The SNS name `cards.sol` resolves to the treasury `3PnV…` (SNS resolver, read 16 Nov 2026). Nansen also tags `redFW…` as "cards.sol"; that wallet created the Aug 2026 vesting streams | [Tier A] SNS · [Tier B] Nansen |
| Legal entity, cap table, audited accounts | **Not found** this pass | — |

**What it means:** The company names its key wallets and runs the treasury through a multisig, which is better than most small caps. But no legal entity, filings or multisig threshold was confirmed, so it is not proven.

## 🪙 Foundation / team holdings — How many coins do they hold? · 3/10 · ❌ FAIL

| Bucket | CARDS | Notes |
|---|---:|---|
| Treasury multisig [`3PnV…`](https://solscan.io/account/3PnVBrb4wPLFLW38oaYR7dA6HSfKpawxHGESPj5kF1QB) | **1,081,261,037 (54.8%)** | Unlocked. Company page: "Foundation 770.03M" + "Community 290.00M" (rewards), all company-held [Tier A] |
| Streamflow escrows (team / advisors / seed) | ~403.23M by the company's count; Vestream counts 346.79M on Streamflow | Self-owned escrow token accounts, e.g. [`96cJ…`](https://solscan.io/account/96cJVtxcPYeJ5doebfV3RqJMB1xg1d1tRAAiDAsZ2do4) 82.66M, [`4xkD…`](https://solscan.io/account/4xkDss3j27G9JNqDnyhrzFkwfsQHFfi5FC31UfnHxog7) / [`Av47…`](https://solscan.io/account/Av47AL9pfDcUN9m4iLfdbeyZWbmhFWHJSPeEse5MzyZz) / [`EEae…`](https://solscan.io/account/EEaezt3okKxvrxVNxyhsZyLcYotYokievV6MA2B572ea) 64.29M each [Tier A] · [Tier B] [Vestream](https://www.vestream.io/token/101/CARDSccUMFKoPRZxt5vt3ksUbxEFEcnZ3H2pd3dKxYjp) |
| Treasury LP positions in the Raydium pool | net ~19.0M CARDS + ~$583K USDC put in (Aug 2025 – Oct 2026) | [Tier A] 97 open/close/collect transactions read |
| Company-defined circulating | 500.2M (25.0%) | [Tier A] tokenomics page |

**What it means:** By the company's own numbers, about **75% of supply is company-held or still vesting**. The 54.8% in the treasury is unlocked and can move with a multisig vote. Disclosure is good (it is all named), but the concentration is extreme, so **3**.

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL

All 349 transactions on the treasury's CARDS account (29 Aug 2025 – 16 Nov 2026) were read and every outflow of 1M or more was followed. Pump days were taken from CoinGecko daily closes (122 pump days in the last 365; closes before 17 Nov 2025 were not available on the free API).

**A. Treasury → exchange (not on a pump day)**

| Day (UTC) | Route | CARDS | 5-day change | Pump? |
|---|---|---:|---:|---|
| 3–4 Nov 2026 | Treasury → fresh [`4JTA…`](https://solscan.io/account/4JTAa4ZbKKQuVef229Y54S26JXNzdb6GknpAYDL7Ajnq) ([100 test](https://solscan.io/tx/5fFNVhxw2egpdDQNd5AA6KvJNGhJuoXCzfKYSVMkGUAHqS2hMeqTkvesU8wfczL3HRgNp9mqrPsijwiWhwEcHcpk) · [6,999,900](https://solscan.io/tx/5t6a4JZ1gsUJ9bEXWfiveGLeXgGG6d3TDXtv2CXt4bDij33qL64sBT3wKRBKkSLqnip8QX8bCVKw92Jo8tpPXK4g)) | 7,000,000 | — | No |
| 6 Nov 2026 | `4JTA…` → Coinbase deposit [`E1t8…`](https://solscan.io/account/E1t8AdPqfFAkzdaTNivZ9jHBqDUfhZnCMd4o1H6h82U1) ([tx](https://solscan.io/tx/2cr5JGxAfU87jMoqKMqRwqNCNPEZsvgwT1k8JNR2C8rvj1ivTukUdeq9LaGBkRnVyT5hpX2bajD6kW4ZM2KFx1vM)) → "Coinbase: Hot Wallet" [`H8sM…`](https://solscan.io/account/H8sMJSCQxfKiFTCfDR3DUMLPwcRbM61LGFJ8N4dK3WjS) in 4 min ([tx](https://solscan.io/tx/5EY3dWwb9ojw7wR6cUhWLWfSwfGdDDip1YWXumyceDdJ2bRHJmKjrCc7kwqBxMZh4rthkFQtiZJ4Be7STqDfGueT)) | 7,000,000 | $0.2422 / +5.8% | No |

Labels: Nansen tags `E1t8…` "Coinbase / CEX" and `H8sM…` "Coinbase: Hot Wallet" ([Tier B] Nansen, read 16 Nov 2026); Arkham also labels `E1t8…` "Coinbase Deposit" and names the relay `4JTA…`'s first funder as the Squads vault "CARDS Treasury" `3PnVB` ([Tier B] Arkham, read 16 Nov 2026 ~6:35–6:40 AM MST (signed-in account), [4JTA… on Arkham](https://intel.arkm.com/explorer/address/4JTAa4ZbKKQuVef229Y54S26JXNzdb6GknpAYDL7Ajnq)). Two Tier B sources now agree on the Coinbase label. The deposit-then-sweep pattern is [Tier A]. Whether it was a sale, an OTC transfer or exchange inventory is **not visible** [Unverified]. No disclosure was found.

**B. Treasury outflows on pump days**

| Day | Route | CARDS | 5-day change | What happened next |
|---|---|---:|---:|---|
| 14 Jun 2026 | Treasury → multisig executor [`HWPR…`](https://solscan.io/account/HWPRgtDGpBm8mByTGS57BWCsijMo53qPPSbskWDukfTc) ([tx](https://solscan.io/tx/3Sdu3Ck5b72dC6XuTvutTDcKRWK8pKy8NGqF2w7gsDBJXkxSiv9HVHjGJcSvR8DYTV69FhYxZ73LfWfoZBmamrmw)) → [`3CRv…`](https://solscan.io/account/3CRvVY8NJcgEFwoFTay4ykiRDwFKwNuMxw8wNt5qDZjP) 14.64M ([tx](https://solscan.io/tx/2Ai4KmLuESdfhMvzAuyhcR6bRwQwzwqkkzMRygbWZg7CafDprzZcCb9CvTm78Ga1Wd3Bw2AZwvbWzyfWPfBhkhR7)) | 9,503,000 | +41.6% | `3CRv…`'s token account pays out small amounts to many users through a claim program (`gdrpGjV…`); leftovers returned to `HWPR…`. Same pattern on 9 Dec 2025 ([15M](https://solscan.io/tx/Ci17ZhvVFwC9UQ2BkkRzFK4rUxvw4qinVjEMLjepHckRL7yLimsCx253pfL4hBwmyW4VJ7VFwUj1LmUKxGHCa7m)), 9 Mar 2026 ([14M](https://solscan.io/tx/2ELuYQnd3P94aosCyvEsyKPqCxtByax2gi4iRhBSeiyFNiNiHm9wxFjocsXr9y4cxBi34BorV2riX337JnLsTsF5)) and 7 Sep 2026. Reads as the published quarterly community rewards, **not an exchange sale** |
| 28 Sep 2026 | Treasury cancelled old Streamflow streams ([cancel tx](https://solscan.io/tx/TDDxQ1unB7ogA6J1NdmYWEPFQDdfKBtsjSPmj5t25MEcUtcb9JGQwCdugt18maFWZgBdrny5xpjrU9hQxeDjuTZ)) and re-created them ([create tx](https://solscan.io/tx/5ucuMxxQJsFdJKUAbymzte9khTXe6aZHtHRxBXvnZHpW9DmThZ7h3wAN36EZuEjqMKD5EJ2xin5xm5TofYpLi2hb)) | ~400M re-locked | +32.0% | Coins stayed in escrows. No exchange flow |
| 5 Oct 2026 | Treasury → [`DFEs…`](https://solscan.io/account/DFEstpYN3fsz93AC9v2ujzPPngPgodqH2xxopuyfSsAE) ([tx](https://solscan.io/tx/3RhbQ2bdrP9LL6FdPDpNRb77KReUyuduZXALYH58fmYiNHsWAWKMaEQK7VmTPdP566UHraNYxbf1aZuEPs8sD1Ez)) | 1,250,000 | +36.3% | Forwarded via `Ersg…` / `HmmY…` to unlabelled "High Balance" `6UJ9…`. Arkham: `DFEs…` was first funded by a Magic Eden escrow and moves USDC to a Kraken deposit [Arkham](https://intel.arkm.com/explorer/address/DFEstpYN3fsz93AC9v2ujzPPngPgodqH2xxopuyfSsAE); `6UJ9…` is unlabelled and passed 1.082M on to `9oGT…` [Arkham](https://intel.arkm.com/explorer/address/6UJ9q432L57njSHPYGaQ7CqW5CTxrcDMpU3z9gpdH4SF). Owner [Unverified] |

**C. Wallets paid by company wallets that sold on the DEX.** `cards.sol` (`redFW…`) paid [`7AMz…`](https://solscan.io/account/7AMzq99oGa6ittsSWueJbu2yUmamxPmNqd8Dm2Ai5i8j) 1,187,500 CARDS a month (9.5M total; two payments fell on pump days, [27 May](https://solscan.io/tx/4RiNjZdo9Lprh24vMwZqWSxoWt2Vi2ZNsomF4N7xoqKTe4sYetT61UYcUdHDZn9s1UEajaRMWEutk8mt8mTwbF8A) and [15 Aug 2026](https://solscan.io/tx/5aFrYvFs6LLYjK28MdWfvARy7A2zii1xzm4wvTyD6V9mEnrJUFhQBVLzXLMpDp3LEcPN7TuHZWCb914PH22dmT2f)). Arkham labels `7AMz…` a **Fireblocks Custody** wallet; it also sent 100K CARDS to a KuCoin deposit [Arkham](https://intel.arkm.com/explorer/address/7AMzq99oGa6ittsSWueJbu2yUmamxPmNqd8Dm2Ai5i8j). It forwarded 5.94M to [`4ZKi…`](https://solscan.io/account/4ZKiZi8Mh3jkkvjZY918PRSBeAeu6zSU5Q4fdPUJ2GL9), which sold ~5.58M into the Raydium pool ([Tier B] Nansen counterparties; Arkham shows the inflows about four months ago, i.e. around Jul 2026, but only relative dates [Arkham](https://intel.arkm.com/explorer/address/4ZKiZi8Mh3jkkvjZY918PRSBeAeu6zSU5Q4fdPUJ2GL9)). That looks like a contractor or advisor selling their pay; the sale days were not pump-tested this pass.

**C2. A 60M branch from `cards.sol` ends with a market maker.** `cards.sol` (`redFW…`, which Arkham shows receiving 79.2M from the "CARDS Treasury" vault [Arkham](https://intel.arkm.com/explorer/address/redFWCNFJDg86S3CAbuGGjAr9hQCimcr7xz7v3oEpuj)) paid 60M to [`8Qvd…`](https://solscan.io/account/8QvdxiBP43edFfXCoRV1saVZAJ6iddzqH2Ys99fdKwyq), which passed it in 4.75M lots to [`2asR…`](https://solscan.io/account/2asR4HQHhZrMHq4vGykzSHhRqhMZq9Q6C6Wb3JKgjg55) [Arkham](https://intel.arkm.com/explorer/address/2asR4HQHhZrMHq4vGykzSHhRqhMZq9Q6C6Wb3JKgjg55), which sent ~57M on to [`6rQG…`](https://solscan.io/account/6rQG31K3k9ZSDPV53hApWLoFagBbH6BnjcMk4vQbD37o). Arkham labels `6rQG…` **Fireblocks Custody** and shows it sending CARDS in 0.4–2M lots to **GSR Markets: Fireblocks Custody** [Arkham](https://intel.arkm.com/explorer/address/6rQG31K3k9ZSDPV53hApWLoFagBbH6BnjcMk4vQbD37o) ([Tier B] Arkham, read 16 Nov 2026 ~6:35–6:40 AM MST (signed-in account)). So treasury-sourced CARDS reached a market maker without any announcement found. Who owns `6rQG…` is not named [Unverified].

**C3. Other treasury-funded wallets (Arkham).** [`HX4q…`](https://solscan.io/account/HX4qRBbEVp7xo6AdKc5mS4y9CoL5Sbku8HtDKmQqZYMg) was first funded by the "CARDS Treasury" vault and forwards CARDS within hours to unlabelled `8AaqB4…` in 100–200K lots [Arkham](https://intel.arkm.com/explorer/address/HX4qRBbEVp7xo6AdKc5mS4y9CoL5Sbku8HtDKmQqZYMg). [`BAxT…`](https://solscan.io/account/BAxTk97HsaJqbnbFmTiQTaL4KSRvJ8Y65ArZCsP6vA5M) (10M from the treasury in Jun 2026, 7.76M returned) carries the Phantom profile "CCRaffle", which fits a Collector Crypt raffle wallet [Arkham](https://intel.arkm.com/explorer/address/BAxTk97HsaJqbnbFmTiQTaL4KSRvJ8Y65ArZCsP6vA5M). The multisig executor `HWPR…` shows only a Pump.fun profile, no team name [Arkham](https://intel.arkm.com/explorer/address/HWPRgtDGpBm8mByTGS57BWCsijMo53qPPSbskWDukfTc).

**D. Treasury liquidity management.** The treasury runs concentrated-liquidity positions in its own pool ([launch position, 29 Aug 2025: 40M CARDS + $786K USDC](https://solscan.io/tx/38cPjsTVp1G587ZsH5KsrKa4WrT2YiLd44gXpRAMtd22RqUBQfPRbhE6ePwwpR7NXnVK3urvKbaBhfcTZMEe12eL); [closed 5 Sep 2025 for 142K CARDS + $4.45M USDC](https://solscan.io/tx/LmLV9w1daYCPHGQF91xpaqNZw7Fhp6RLnAayGD6EzALjkq1EbJDLSmibkU7PUeSd1Jd7zL1ubVftMHSoRnQg6xt)). So about 40M CARDS were sold to buyers through the range in the first week. Across all 97 position transactions, the net flow is still *into* the pool (−19.0M CARDS, −$583K USDC). A treasury-funded bot [`CcM9…`](https://solscan.io/account/CcM9FGcjo7hS1ZoiCXxM6cUVfiGrDV3qMDYGCbdmmSWj) (20.7M from the treasury in 2025) swaps both ways in the pool all day (3,000 transactions in 6 days, Nov 2026). Arkham shows a Phantom profile "CollectorTrex" on it but no market-maker or buyback label [Arkham](https://intel.arkm.com/explorer/address/CcM9FGcjo7hS1ZoiCXxM6cUVfiGrDV3qMDYGCbdmmSWj).

**What it means:** No treasury CARDS were traced into a labelled exchange **on a pump day**, so the hard rule is not tripped. But the treasury sent 7M to Coinbase without notice, sold heavily through its LP range at launch, runs a trading bot in its own pool, and (per Arkham) about 57M from a treasury-paid branch went toward GSR Markets' custody. Holders can't tell market-making from selling. That puts it at **4** (unchanged after Arkham): not proven bad on pumps, and not clean.

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from CoinGecko daily closes.

## 📊 Tokenomics & supply · 4/10 · ❌ FAIL

- **Fixed supply, and code agrees:** `mintAuthority` and `freezeAuthority` are both null [Tier A, RPC `getAccountInfo`, 16 Nov 2026]. Supply 1,972,174,887.42 after ~27.8M burned.
- **Unlocks:** Team 297.80M, Advisors 61.09M, Seed 44.34M are still vesting: **~44.8M a month** (2.2% of supply) through **29 Jul 2027**, next on **29 Nov 2026** [Tier A, company page]. At the current burn pace (~$0.36M in 30 days ≈ 2M CARDS) unlocks run about **20× faster** than burns.
- **Original allocation (TGE 29 Aug 2025):** Foundation 36.8%, Community 17.5%, Team 19.5%, Pre-seed 8.2%, Advisors 4.4%, Seed 3.7%, Launch pool 5%, Airdrop 2.5%, LP 2.5%. The Foundation share has **grown** to 38.5% (LP fees and buybacks land there).

## 💧 Liquidity & market · 5/10 · ❌ FAIL

- $4.66M of volume in 24h on a $133M cap (≈ 3.5% turnover). The main venue is the treasury-seeded Raydium CLMM pool; Coinbase hot-wallet flows exist.
- Very volatile: **122 of the last 365 days were pump days**. The price is down 61% from the 21 Oct 2026 ATH and −48.7% in 30 days.

## 🧑‍💻 Product & development · 6/10 · ✅ PASS

- Live gacha packs on Solana, Base and Robinhood Chain plus a fiat/card rail, a marketplace with royalties, and integration with Jupiter Gacha (DefiLlama methodology) [Tier A].
- No public code repository was checked this pass, so dev activity is not measured.

## 🤝 Adoption & customers · 7/10 · ✅ PASS

- About **$106M of net revenue in 12 months**, with Oct 2026 the best month so far ($18.8M) [Tier A DefiLlama]. Users pay real money for packs, so demand is not just token farming.
- Reward claim vaults paid thousands of users (thousands of transactions per vault) [Tier A].

## 🛡️ Security & audits · 5/10 · ❌ FAIL

- ✅ No mint or freeze authority. ✅ The treasury is a Squads multisig, not a single key. ✅ Vesting uses Streamflow, not custom code.
- ❌ The multisig threshold and signers are not published [Unverified]. No audit of Collector Crypt's own programs was found. No hack found.

## ⚖️ Regulatory · 4/10 · ❌ FAIL

- Paid random packs (gacha) with buyback of prizes may fall under gambling or loot-box rules in some places. No licence or legal opinion was found this pass. Not proven either way.

## 📅 Catalysts & calendar · 4/10 · ❌ FAIL

| Date | Event |
|---|---|
| 29 Nov 2026 | Monthly unlock ~44.8M CARDS (Team 33.09M, Advisors 6.79M, Seed 4.93M) and the next tokenomics-page update |
| Monthly to 29 Jul 2027 | Same unlock each month |
| Any time | Treasury multisig can move its 1.08B CARDS |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Live mint path | 🟢 No: mint and freeze authorities are null |
| Team wallet → exchange during a pump | 🟢 Not found in the wallets traced |
| Treasury → exchange (any day) | 🔴 **Yes:** 7,000,000 CARDS to Coinbase on 6 Nov 2026 via fresh `4JTA…`. [→ deposit](https://solscan.io/tx/2cr5JGxAfU87jMoqKMqRwqNCNPEZsvgwT1k8JNR2C8rvj1ivTukUdeq9LaGBkRnVyT5hpX2bajD6kW4ZM2KFx1vM) · [→ hot wallet](https://solscan.io/tx/5EY3dWwb9ojw7wR6cUhWLWfSwfGdDDip1YWXumyceDdJ2bRHJmKjrCc7kwqBxMZh4rthkFQtiZJ4Be7STqDfGueT) |
| Treasury → market maker | 🟡 ~57M via `cards.sol` → `8Qvd…` → `2asR…` → Fireblocks `6rQG…` → **GSR Markets** custody; no disclosure found. [Arkham](https://intel.arkm.com/explorer/address/6rQG31K3k9ZSDPV53hApWLoFagBbH6BnjcMk4vQbD37o) |
| Treasury moves on pump days | 🟡 14 Jun 2026 9.5M (to rewards); 5 Oct 2026 1.25M to unlabelled `DFEs…`. [tx](https://solscan.io/tx/3RhbQ2bdrP9LL6FdPDpNRb77KReUyuduZXALYH58fmYiNHsWAWKMaEQK7VmTPdP566UHraNYxbf1aZuEPs8sD1Ez) |
| Supply concentration | 🔴 54.8% in one unlocked treasury multisig |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| Treasury → Coinbase (7M) and GSR-bound branch (~57M) | Collector Crypt treasury; GSR per Arkham | Solana RPC + Arkham | medium | no | Selling: none proven on a pump day; stays 4 |

## 📚 Sources

- [Tier A] Methodology update 16 Nov 2026: no new Arkham lookups; the attribution table uses evidence already cited in this report.
- [Tier A] Solana RPC (mainnet-beta, publicnode): `getAccountInfo` for the mint, `getTokenSupply`, full signature history and parsed transactions for the treasury token account `DgiH…` (349 tx), `5iVa…` (cards.sol, 188 tx), `HWPR…`, `4JTA…`, `E1t8…`, read 16 Nov 2026 MST
- [Tier A] [collectorcrypt.com/tokenomics](https://collectorcrypt.com/tokenomics): allocation, unlocks, treasury and buyback addresses, burn list (last updated 3 Nov 2026)
- [Tier A] SNS resolver: `cards.sol` → `3PnV…`
- [Tier A] DefiLlama `collector-crypt` fees, revenue and holders revenue, 16 Nov 2026
- [Tier A] CoinGecko `collector-crypt` price, market data and 365-day closes, 16 Nov 2026 5:08 AM MST
- [Tier B] Nansen API, read 16 Nov 2026 ~5:20–5:50 AM MST: labels for `E1t8…` (Coinbase), `H8sM…` (Coinbase: Hot Wallet), `Hnhp…` (Raydium pool), `redFW…` (cards.sol); counterparty totals for 16 wallets; top-30 holders
- [Tier B] Arkham, read 16 Nov 2026 ~6:35–6:40 AM MST (signed-in account): "CARDS Treasury" vault as first funder of [4JTA…](https://intel.arkm.com/explorer/address/4JTAa4ZbKKQuVef229Y54S26JXNzdb6GknpAYDL7Ajnq), [HX4q…](https://intel.arkm.com/explorer/address/HX4qRBbEVp7xo6AdKc5mS4y9CoL5Sbku8HtDKmQqZYMg) and the escrow [96cJ…](https://intel.arkm.com/explorer/address/96cJVtxcPYeJ5doebfV3RqJMB1xg1d1tRAAiDAsZ2do4); Fireblocks Custody on [7AMz…](https://intel.arkm.com/explorer/address/7AMzq99oGa6ittsSWueJbu2yUmamxPmNqd8Dm2Ai5i8j) and [6rQG…](https://intel.arkm.com/explorer/address/6rQG31K3k9ZSDPV53hApWLoFagBbH6BnjcMk4vQbD37o) (the latter sending to GSR Markets custody); Coinbase Deposit on `E1t8…`; no owner label on [redFW…](https://intel.arkm.com/explorer/address/redFWCNFJDg86S3CAbuGGjAr9hQCimcr7xz7v3oEpuj), [CcM9…](https://intel.arkm.com/explorer/address/CcM9FGcjo7hS1ZoiCXxM6cUVfiGrDV3qMDYGCbdmmSWj), [8Qvd…](https://intel.arkm.com/explorer/address/8QvdxiBP43edFfXCoRV1saVZAJ6iddzqH2Ys99fdKwyq), [2asR…](https://intel.arkm.com/explorer/address/2asR4HQHhZrMHq4vGykzSHhRqhMZq9Q6C6Wb3JKgjg55), [DFEs…](https://intel.arkm.com/explorer/address/DFEstpYN3fsz93AC9v2ujzPPngPgodqH2xxopuyfSsAE), [6UJ9…](https://intel.arkm.com/explorer/address/6UJ9q432L57njSHPYGaQ7CqW5CTxrcDMpU3z9gpdH4SF), [BAxT…](https://intel.arkm.com/explorer/address/BAxTk97HsaJqbnbFmTiQTaL4KSRvJ8Y65ArZCsP6vA5M). Arkham's token filter is Enterprise-only, so counterparties come from the default first page and dates are relative.
- [Tier B] [Vestream](https://www.vestream.io/token/101/CARDSccUMFKoPRZxt5vt3ksUbxEFEcnZ3H2pd3dKxYjp) (346.79M locked on Streamflow) · [Streamflow case study](https://streamflow.finance/case-studies/collector-crypt)
- [Unverified] purpose of the 7M Coinbase transfer and the GSR route; multisig threshold; owners of `DFEs…`, `6UJ9…`, `CcM9…`, `7AMz…`/`4ZKi…`, `8Qvd…`/`2asR…`/`6rQG…` (custodian known, owner not); legal entity

## 🔗 Evidence trail

*Every link below opens the primary record for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Mint and freeze authority revoked; supply 1,972,174,887 | [mint](https://solscan.io/token/CARDSccUMFKoPRZxt5vt3ksUbxEFEcnZ3H2pd3dKxYjp) | A | 16 Nov 2026 |
| Treasury, buyback wallet and allocations are the company's | [tokenomics page](https://collectorcrypt.com/tokenomics) · [treasury](https://solscan.io/account/3PnVBrb4wPLFLW38oaYR7dA6HSfKpawxHGESPj5kF1QB) · [buyback](https://solscan.io/account/3nGNwiz1qevPjhEoQi1dLj16oTkjmbevTnpV9piWY7Kq) | A | 16 Nov 2026 |
| Treasury → 4JTA → Coinbase deposit → Coinbase hot wallet, 7M, 3–6 Nov 2026 | [test](https://solscan.io/tx/5fFNVhxw2egpdDQNd5AA6KvJNGhJuoXCzfKYSVMkGUAHqS2hMeqTkvesU8wfczL3HRgNp9mqrPsijwiWhwEcHcpk) · [6,999,900](https://solscan.io/tx/5t6a4JZ1gsUJ9bEXWfiveGLeXgGG6d3TDXtv2CXt4bDij33qL64sBT3wKRBKkSLqnip8QX8bCVKw92Jo8tpPXK4g) · [→ E1t8](https://solscan.io/tx/2cr5JGxAfU87jMoqKMqRwqNCNPEZsvgwT1k8JNR2C8rvj1ivTukUdeq9LaGBkRnVyT5hpX2bajD6kW4ZM2KFx1vM) · [→ H8sM](https://solscan.io/tx/5EY3dWwb9ojw7wR6cUhWLWfSwfGdDDip1YWXumyceDdJ2bRHJmKjrCc7kwqBxMZh4rthkFQtiZJ4Be7STqDfGueT) | A chain + B label (Nansen) | 16 Nov 2026 |
| 14 Jun 2026 pump day: 9.5M treasury → HWPR → reward vault | [→ HWPR](https://solscan.io/tx/3Sdu3Ck5b72dC6XuTvutTDcKRWK8pKy8NGqF2w7gsDBJXkxSiv9HVHjGJcSvR8DYTV69FhYxZ73LfWfoZBmamrmw) · [→ 3CRv](https://solscan.io/tx/2Ai4KmLuESdfhMvzAuyhcR6bRwQwzwqkkzMRygbWZg7CafDprzZcCb9CvTm78Ga1Wd3Bw2AZwvbWzyfWPfBhkhR7) | A | 16 Nov 2026 |
| 28 Sep 2026: Streamflow streams cancelled and re-created by the multisig | [cancel](https://solscan.io/tx/TDDxQ1unB7ogA6J1NdmYWEPFQDdfKBtsjSPmj5t25MEcUtcb9JGQwCdugt18maFWZgBdrny5xpjrU9hQxeDjuTZ) · [create](https://solscan.io/tx/5ucuMxxQJsFdJKUAbymzte9khTXe6aZHtHRxBXvnZHpW9DmThZ7h3wAN36EZuEjqMKD5EJ2xin5xm5TofYpLi2hb) | A | 16 Nov 2026 |
| 5 Oct 2026 pump day: 1.25M treasury → DFEs | [tx](https://solscan.io/tx/3RhbQ2bdrP9LL6FdPDpNRb77KReUyuduZXALYH58fmYiNHsWAWKMaEQK7VmTPdP566UHraNYxbf1aZuEPs8sD1Ez) | A · owner [Unverified] | 16 Nov 2026 |
| Launch LP: 40M CARDS sold through the range in a week | [open](https://solscan.io/tx/38cPjsTVp1G587ZsH5KsrKa4WrT2YiLd44gXpRAMtd22RqUBQfPRbhE6ePwwpR7NXnVK3urvKbaBhfcTZMEe12eL) · [close](https://solscan.io/tx/LmLV9w1daYCPHGQF91xpaqNZw7Fhp6RLnAayGD6EzALjkq1EbJDLSmibkU7PUeSd1Jd7zL1ubVftMHSoRnQg6xt) | A | 16 Nov 2026 |
| Monthly 1.1875M payments from cards.sol to 7AMz (incl. pump days) | [27 May](https://solscan.io/tx/4RiNjZdo9Lprh24vMwZqWSxoWt2Vi2ZNsomF4N7xoqKTe4sYetT61UYcUdHDZn9s1UEajaRMWEutk8mt8mTwbF8A) · [15 Aug](https://solscan.io/tx/5aFrYvFs6LLYjK28MdWfvARy7A2zii1xzm4wvTyD6V9mEnrJUFhQBVLzXLMpDp3LEcPN7TuHZWCb914PH22dmT2f) | A | 16 Nov 2026 |
| Relay `4JTA…` and `HX4q…` first-funded by the "CARDS Treasury" vault; `E1t8…` is a Coinbase deposit | [Arkham 4JTA…](https://intel.arkm.com/explorer/address/4JTAa4ZbKKQuVef229Y54S26JXNzdb6GknpAYDL7Ajnq) · [Arkham HX4q…](https://intel.arkm.com/explorer/address/HX4qRBbEVp7xo6AdKc5mS4y9CoL5Sbku8HtDKmQqZYMg) | B (Arkham) + A chain | 16 Nov 2026 ~6:35 AM MST |
| 60M `cards.sol` branch ends at Fireblocks custody that sends to GSR Markets | [`8Qvd…`](https://solscan.io/account/8QvdxiBP43edFfXCoRV1saVZAJ6iddzqH2Ys99fdKwyq) · [Arkham 2asR…](https://intel.arkm.com/explorer/address/2asR4HQHhZrMHq4vGykzSHhRqhMZq9Q6C6Wb3JKgjg55) · [Arkham 6rQG…](https://intel.arkm.com/explorer/address/6rQG31K3k9ZSDPV53hApWLoFagBbH6BnjcMk4vQbD37o) | A chain + B (Arkham) | 16 Nov 2026 ~6:38 AM MST |
| `7AMz…` is Fireblocks custody | [Arkham 7AMz…](https://intel.arkm.com/explorer/address/7AMzq99oGa6ittsSWueJbu2yUmamxPmNqd8Dm2Ai5i8j) | B | 16 Nov 2026 ~6:37 AM MST |
| Revenue $106.24M 12m; holders $471K | [revenue](https://api.llama.fi/summary/fees/collector-crypt?dataType=dailyRevenue) · [holders](https://api.llama.fi/summary/fees/collector-crypt?dataType=dailyHoldersRevenue) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | ~~Arkham pass on 14 unlabelled wallets~~ **Done 16 Nov 2026** (the maintainer's `arkham/cards_addresses.csv` list): treasury funding of the relay and escrows confirmed; `7AMz…` and `6rQG…` are Fireblocks custody, and `6rQG…` feeds GSR Markets. Still unnamed: `redFW…`, `CcM9…`, `HWPR…`, `8Qvd…`, `2asR…`, `DFEs…`, `6UJ9…`, `HX4q…`, escrow recipients | Re-check with Arkham Enterprise's token filter for exact dates and full CARDS history | Arkham Enterprise |
| 1b | **Is GSR Collector Crypt's market maker, and was the 60M disclosed?** | Ask Collector Crypt; look for a market-maker agreement or announcement | Free |
| 2 | **Why did 7M treasury CARDS go to Coinbase on 6 Nov 2026?** | Ask Collector Crypt; check the tokenomics update due after the 29 Nov unlock for a drop in "Foundation" | Free |
| 3 | **Did `4ZKi…` sell on pump days?** | Read its token account history and match sale days to the pump list | Free |
| 4 | **Multisig threshold and signers** | Read the Squads multisig account for vault `3PnV…` | Free |
| 5 | **Pump test for Aug–Nov 2025** | Pull exchange daily closes for 29 Aug – 16 Nov 2025 and re-test treasury moves in that window | Free |
| 6 | **Legal entity and gacha licensing** | Find the operating company and any gaming or consumer-protection licence | Free |
| 7 | **Pump-day test on exchange prices.** Gate CARDS_USDT returned only 42 days on 16 Nov 2026, too short for a 365-day test | Re-run scripts/pump_day_test.py on a venue with full history, or once Gate has a year of data | Free |
| 8 | **Pump-day test on exchange prices.** The test used CoinGecko daily closes and no Gate, MEXC, KuCoin or Kraken USDT series was returned on 16 Nov 2026 (Binance blocks this region) | Re-run scripts/pump_day_test.py on the first exchange in the price-source order that lists the token | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
