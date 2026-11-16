---
ticker: DOT
name: Polkadot
chain: polkadot
contract: "native (Polkadot Asset Hub balances)"
overall_score: 4.9
overall_verdict: FAIL
section_scores:
  revenue: 2
  foundation_team: 7
  insider_holdings: 5
  selling_behavior: 4
  tokenomics_supply: 5
  liquidity_market: 7
  product_development: 7
  adoption_customers: 4
  security_audits: 6
  regulatory: 7
  catalysts: 5
gates_failed: [revenue]
red_lines:
  hack_exploit: none
  mint_path_live: "protocol issuance only (~56M DOT/yr after 14 Mar 2026, hard cap 2.1B set by Ref 1710); no admin mint key"
  team_wallet_to_exchange_during_pump: "not proven (W3F-linked multisig-proxied account 13FzGL… and two other W3F-linked wallets sent 33.1M DOT (29.4M from 13FzGL…) into deposit-style account 14mr97…, which forwards to an unidentified high-throughput service; 4.0M of it on 14 pump days, 2023-2026; service and owner [Unverified])"
  treasury_selling: "disclosed (OpenGov Refs 457/1104/1501/1729 swap treasury DOT for USDT/USDC through Hydration DCA; Ref 1729 = 2.64M DOT)"
  chain_stalls_2026: "4 partial stalls (parachains 23 Mar, People chain 22 Apr, Asset Hub ~30 min 12 Jun, staking election 30 Jun - 3 Jul); no funds lost"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "Fees are tiny and none is paid to holders; staking rewards come from issuance."
pump_day_price_source: "Gate DOT_USDT UTC daily closes, re-run 16 Nov 2026 with scripts/pump_day_test.py (29 of 360 days); the body's earlier count used CoinGecko daily closes"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions: []
price_usd: 0.7286
price_source: "CoinGecko, 16 Nov 2026 5:10 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### DOT · Overall grade **4.9 / 10 · ❌ FAIL**

**Summary:** Polkadot is a real, actively built network: a large open-source codebase, a public foundation (Web3 Foundation) and builder (Parity), a US spot ETF, and a new hard cap of 2.1B DOT. But the token earns almost nothing from usage: DefiLlama counts **$3,868 of Polkadot fees in a whole year**, and fees, coretime and slashes now flow into a protocol pool, not to holders. Staking rewards are new issuance (~56M DOT a year). Price is down 98.7% from its high. On-chain, **Web3 Foundation-linked wallets, led by one multisig-controlled account,** have sent **33.1M DOT into one deposit-style account** that feeds an unidentified high-throughput service, **4.0M of it on pump days**. Whether that was a sale is not proven.

**🚨 Top warning:** The 2-of-3 multisig-controlled account [`13FzGL…BtVZbXu`](https://assethub-polkadot.subscan.io/account/13FzGLWoueKvUqFePiJgvFYWhH5KckHGtVBXvAX7SBtVZbXu), which swaps DOT both ways with Web3 Foundation's registered sub-identity [`12RYJb…VFSfJr8Y`](https://people-polkadot.subscan.io/account/12RYJb5gG4hfoWPK3owEYtmWoko8G6zwYpvDYTyXFVSfJr8Y) and paid the ["W3F Governance Team"](https://people-polkadot.subscan.io/account/14mmwp83EuacfrQTCCPUgRPJEeXuS52Psz95GDZEodj37imd) identity, sent **29.4M DOT** into [`14mr97…U78xoq4`](https://assethub-polkadot.subscan.io/account/14mr97Z7TR26zrEqH4yS2PuUx3xEKjMRzrM2FvBpbU78xoq4); with two other W3F-linked wallets the total into that account is **33.1M DOT in 346 transfers (Feb 2023 – Nov 2026)**. `14mr97…` takes ~99% of its inflow from W3F-linked wallets and passes everything on to [`12xKCG…kjrWPi3ff`](https://assethub-polkadot.subscan.io/account/12xKCGbw56Bq8V4tdHT7QUabaWeUh8d935t81mPkjrWPi3ff), a hub with 1,400+ unique senders. **4.02M DOT went in on pump days**, e.g. [1.275M on 21 Dec 2023 (+18.7%)](https://polkadot.subscan.io/extrinsic/18692262-332) and [100k on 8 Sep 2026 (+40.2%)](https://assethub-polkadot.subscan.io/extrinsic/20401730-2). Who runs that service (exchange, custodian, OTC desk) is **[Unverified]**, so this is a 🟡 flag, not a proven pump-day sale. Every link is in the 🔗 Evidence trail below.

**Sections passed: 5 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 2/10 | ❌ FAIL |
| 🏛️ Foundation & team | 7/10 | ✅ PASS |
| 🪙 Foundation / team holdings | 5/10 | ❌ FAIL |
| 📉 Selling behavior | 4/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 5/10 | ❌ FAIL |
| 💧 Liquidity & market | 7/10 | ✅ PASS |
| 🧑‍💻 Product & development | 7/10 | ✅ PASS |
| 🤝 Adoption & customers | 4/10 | ❌ FAIL |
| 🛡️ Security & audits | 6/10 | ✅ PASS |
| ⚖️ Regulatory | 7/10 | ✅ PASS |
| 📅 Catalysts & calendar | 5/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 DOT · Polkadot · 4.9 / 10 · ❌ FAIL

> **One line:** Polkadot is a real, actively built network with a public foundation, a US ETF and a new 2.1B hard cap. But the token earns almost nothing from usage (DefiLlama: $3,868 of fees in a year), staking rewards are new issuance, and Web3 Foundation-linked wallets (mainly one multisig account) have fed 33.1M DOT into an unidentified service, 4.0M of it on pump days.

| 📊 Market (CoinGecko, 16 Nov 2026 5:10 AM MST) | 🔗 On-chain (Polkadot Asset Hub, 16 Nov 2026) |
|---|---|
| **Price** $0.7286 | **Token** native DOT; balances live on Asset Hub since the 2025 migration |
| **24h / 7d / 30d** 🔴 −1.3% / −15.4% / −36.6% · 1y −74.2% | **`Balances.TotalIssuance`** 1,712,374,781 DOT (Asset Hub RPC, block ~23,206,696) |
| **Market cap** $1.248B · **FDV** $1.248B | **Hard cap** 2,100,000,000 DOT (Ref 1710) |
| **24h volume** $58.8M | **Treasury** [`13UVJyLn…JhFsTB`](https://assethub-polkadot.subscan.io/account/13UVJyLnbVp9RBZYFwFGyDvVd1y27Tt8tkntv6Q7JVPhFsTB) 21,456,795 DOT |
| **ATH** $54.98 (4 Nov 2021) · now −98.7% | **Dynamic Allocation Pool** [`13UVJyLk…iunZq1`](https://assethub-polkadot.subscan.io/account/13UVJyLkAxdQn6zM3GrLGvrFgN9jWneRX2NGvf3u92iunZq1) 7,374,992 DOT |
| **Pump days, last ~360 days** 29 (Binance DOT/USDT closes) | **W3F-linked cluster found** ~67.9M DOT across 15 accounts, most of it staked (see Holdings) |

---

## 💰 Revenue — Does it make money? · 2/10 · ❌ FAIL

| Metric | Value | Source |
|---|---:|---|
| Polkadot fees, last 365 days | **$3,868** (30 days: $66.94; ≈ $0/day since 18 Oct 2026) | [Tier A] [DefiLlama fees API, `polkadot`](https://api.llama.fi/summary/fees/polkadot?dataType=dailyFees), read 16 Nov 2026 |
| Polkadot "revenue" (burn) | **$0** (365 days and all-time per DefiLlama's method "Revenue: burned coins") | [Tier A] [DefiLlama, dailyRevenue](https://api.llama.fi/summary/fees/polkadot?dataType=dailyRevenue) |
| Where fees, coretime sales and slashes go now | Into the **Dynamic Allocation Pool (DAP)**, a protocol account governance allocates to validators, nominators, the treasury and a reserve. Treasury burns stopped with runtime 2.1.0/2.1.1 (Mar 2026) | [Tier A] [Parity blog, 2 Mar 2026](https://www.parity.io/blog/refining-polkadots-economic-architecture-issuance-DOT-DAP-and-network-adjustments) · [Polkadot forum: Changes in March 2026](https://forum.polkadot.network/t/changes-on-polkadot-in-march-2026/17101) |
| DAP balance | **7,374,991.87 DOT** in [`13UVJyLk…iunZq1`](https://assethub-polkadot.subscan.io/account/13UVJyLkAxdQn6zM3GrLGvrFgN9jWneRX2NGvf3u92iunZq1) (`modl` + `dap/buff`) | [Tier A] Asset Hub RPC `System.Account`, 16 Nov 2026 ~5:40 AM MST |
| Staking yield source | New issuance (~56M DOT/yr), not fees | [Tier A] [fellows runtimes issue #985](https://github.com/polkadot-fellows/runtimes/issues/985) |
| Asset Hub (Polkadot Hub) fees | Not tracked by DefiLlama; not measured this pass | [Unverified] |

**What it means:** DefiLlama tracks only relay-chain fees, and most activity moved to Asset Hub in late 2025, so the true fee number is somewhat higher than $3,868. But nothing found suggests real usage fees large enough to matter against a $1.25B market cap, and none of it is paid to holders: it sits in a protocol pool that governance spends. Stakers are paid with new DOT. **2, which trips the Revenue gate.**

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** Fees are tiny and none is paid to holders; staking rewards come from issuance.

## 🏛️ Foundation & team — Who is in charge? · 7/10 · ✅ PASS

| Item | Finding | Source |
|---|---|---|
| Foundation | **Web 3 Technologies Foundation (W3F)**, Switzerland. Registered on-chain identity [`14JezN…uC9m`](https://people-polkadot.subscan.io/account/14JezNxa4Fqzsf7ef9prYrNy71Cd1Ff3cZizFrntwviVuC9m) ("W3F", web3.foundation, with 4 sub-identities) and a second "Web3 Foundation" identity [`12Ysqh…Q2AD7`](https://people-polkadot.subscan.io/account/12Ysqhvb4EiqgEpjXG9EK1hQbVFXxKF7JQYCvdQ4TQKg6AD7) | [Tier A] People-chain `Identity.IdentityOf` / `SuperOf`, read 16 Nov 2026 |
| Core developer | **Parity Technologies** (UK Ltd and GmbH both hold on-chain identities, e.g. [`1C6E7T…AkCpmPk`](https://people-polkadot.subscan.io/account/1C6E7TL9hQkTqfPdZFjmdLkFiijMqriwosxozZLeAkCpmPk)) | [Tier A] People chain |
| Who decides | **OpenGov**: DOT-weighted on-chain referenda (189 in the last 12 months per the official developer site); a Technical Fellowship can whitelist urgent fixes | [Tier A] [developers.polkadot.com/platform](https://developers.polkadot.com/platform/) |
| Token sales disclosed | Oct 2017 presale (50% of the initial 10M DOT, $145M); Jul 2019 private sale (500k old DOT = 50M today); Jul 2020 private sale ($47M) | [Tier B] [Blockworks Token Transparency](https://blockworks.com/token-transparency/filing/polkadot), citing the 21Shares S-1/A |
| Runway statements | W3F's CEO said the foundation has "over five years of financial runway without selling DOT" (2024) | [Tier B] [CryptoSlate](https://cryptoslate.com/web3-foundation-parity-technologies-dismiss-polkadot-treasury-depletion-fears/) |

**What it means:** Named organisations, public on-chain identities, an on-chain treasury with quarterly reports, and real governance. What's missing: W3F does not publish its wallet list or current DOT balance.

## 🪙 Foundation / team holdings — How many coins do they hold? · 5/10 · ❌ FAIL

| Bucket | DOT | Notes |
|---|---:|---|
| On-chain Treasury (`py/trsry`) | **21,456,795** (1.25%) | [account](https://assethub-polkadot.subscan.io/account/13UVJyLnbVp9RBZYFwFGyDvVd1y27Tt8tkntv6Q7JVPhFsTB). Governed by OpenGov, not a company. The 2025-Q4 Treasury Report put the treasury at 32M DOT incl. stables/aDOT ([forum](https://forum.polkadot.network/t/2025-q4-polkadot-treasury-report/16847)) |
| Dynamic Allocation Pool | **7,374,992** (0.43%) | [account](https://assethub-polkadot.subscan.io/account/13UVJyLkAxdQn6zM3GrLGvrFgN9jWneRX2NGvf3u92iunZq1) |
| W3F sub-identity [`12RYJb…VFSfJr8Y`](https://assethub-polkadot.subscan.io/account/12RYJb5gG4hfoWPK3owEYtmWoko8G6zwYpvDYTyXFVSfJr8Y) | **7,920,162** (7.92M frozen/staked) | On-chain sub-identity of W3F's `14JezN…` (Tier A). Received [5.5M on 29 Aug 2025](https://polkadot.subscan.io/extrinsic/27532965-4) and [508k on 20 Jan 2025](https://polkadot.subscan.io/extrinsic/24369973-2) from W3F-cluster accounts |
| Other W3F-linked accounts (funding ties to `12RYJb…`) | **~60.0M** across 14 accounts | e.g. [`1GVe7p…GgzBB`](https://assethub-polkadot.subscan.io/account/1GVe7pAK2Pc4TVGuPBYbEU82VmaiQhKjFTzECpX7GGXgzBB) 9.24M · [`13Xo4x…UsBhQ`](https://assethub-polkadot.subscan.io/account/13Xo4xYdMRQQoWD7TA9yCDHG1BXqQFvnjeGvU6LHhRhUsBhQ) 8.85M · [`15j4dg…vDCK`](https://assethub-polkadot.subscan.io/account/15j4dg5GzsL1bw2U2AWgeyAk6QTxq43V7ZPbXdAmbVLjvDCK) 7.92M · [`16GMHo…274B`](https://assethub-polkadot.subscan.io/account/16GMHo9HZv8CcJy4WLoMaU9qusgzx2wxKDLbXStEBvt5274B) 7.92M · [`14Ns6k…fPDJ`](https://assethub-polkadot.subscan.io/account/14Ns6kKbCoka3MS4Hn6b7oRw9fFejG8RH5rq5j63cWUfpPDJ) 6.60M · `12x2Jz…` 5.00M · [`13FzGL…`](https://assethub-polkadot.subscan.io/account/13FzGLWoueKvUqFePiJgvFYWhH5KckHGtVBXvAX7SBtVZbXu) 4.74M. Owner [Unverified] (no label source read) |
| **Total found in the W3F-linked cluster** | **~67.9M (≈ 4.0% of issuance)** | Most of it staked in 7.92M lots. W3F's full holdings are **not disclosed** |

**What it means:** The treasury and DAP are protocol accounts that sell only by public vote. The foundation side is the gap: W3F has never published its wallets or balance. The cluster traced here holds ~68M DOT (~4%), but genesis-era distributor `15j4dg…` alone sent 162M DOT out since 2020, so W3F-linked supply is likely larger than what was found. Score **5**: moderate concentration, mostly staked, not disclosed.

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL

**A. W3F-linked multisig account → deposit-style account 14mr97… → unidentified service.** [`13FzGL…`](https://assethub-polkadot.subscan.io/account/13FzGLWoueKvUqFePiJgvFYWhH5KckHGtVBXvAX7SBtVZbXu) is controlled through a **2-of-3 multisig acting as proxy** (raw call: [`multisig.asMulti → proxy.proxy(real = 13FzGL…) → utility.batch`](https://polkadot-api.statescan.io/extrinsics/18692262-332)). It is tied to W3F on-chain: it got [255,000 DOT from W3F sub-identity `12RYJb…` on 23 Aug 2026](https://assethub-polkadot.subscan.io/extrinsic/19802011-2), sent [570,000 back on 1 Oct 2026](https://assethub-polkadot.subscan.io/extrinsic/21296206-3), and paid [100 DOT to the "W3F Governance Team" identity](https://assethub-polkadot.subscan.io/extrinsic/10434763-2). Owner: W3F-linked by Tier A chain ties; no label source confirms it.

From Feb 2023 to Nov 2026, **33,114,401 DOT arrived in 346 transfers** at [`14mr97…`](https://assethub-polkadot.subscan.io/account/14mr97Z7TR26zrEqH4yS2PuUx3xEKjMRzrM2FvBpbU78xoq4) (2023: 16.8M · 2024: 7.4M · 2025: 3.6M · 2026: 5.3M; **5.97M in the last 12 months**): **29.4M from `13FzGL…` itself**, 2.74M from `1c7yPS…` and 0.41M from `12imiR…` (both funded inside the W3F cluster), and ~0.3M from others. `14mr97…` forwarded everything to [`12xKCG…`](https://assethub-polkadot.subscan.io/account/12xKCGbw56Bq8V4tdHT7QUabaWeUh8d935t81mPkjrWPi3ff) (1,400+ unique senders) and [`145UYr…`](https://polkadot.subscan.io/account/145UYrCgKd6u7h8NsSM5Cde3sx26hkPczLLTbuRa5XAqh3bX), which both pay into [`15G8FG…`](https://assethub-polkadot.subscan.io/account/15G8FGwh2bk2XSAUjKJSZuHT1rdsbxLNr9CwED4mp6aZnZ8F) (~97M DOT throughput, 570+ payees). That is a **deposit-address pattern at a service**, but no label source names it. Pump-day deposits (Binance DOT/USDT closes):

| Day (UTC) | DOT into `14mr97…` | Close / 5-day change | Pump? |
|---|---:|---:|---|
| 3 Jul 2023 | [319,090](https://polkadot.subscan.io/extrinsic/16235250-2) | $5.43 / +11.3% | 🟡 Yes |
| 23 Oct 2023 | [223,200](https://polkadot.subscan.io/extrinsic/17849741-4) | $4.36 / +19.2% | 🟡 Yes |
| 11 Dec 2023 | [576,450](https://polkadot.subscan.io/extrinsic/18550388-2) | $6.71 / +11.0% | 🟡 Yes |
| 21 Dec 2023 | [1,275,000](https://polkadot.subscan.io/extrinsic/18692262-332) | $8.42 / +18.7% | 🟡 Yes |
| 4 Mar 2024 | [109,248](https://polkadot.subscan.io/extrinsic/19753126-4) | $9.86 / +18.2% | 🟡 Yes |
| 22 Apr 2024 | [329,280](https://polkadot.subscan.io/extrinsic/20455871-2) | $7.47 / +13.4% | 🟡 Yes |
| 23 Aug 2024 | [84,000](https://polkadot.subscan.io/extrinsic/22214638-2) | $4.89 / +11.4% | 🟡 Yes |
| 27 Sep 2024 | [153,600](https://polkadot.subscan.io/extrinsic/22719245-2) | $4.88 / +13.2% | 🟡 Yes |
| 6 Dec 2024 | [278,513](https://polkadot.subscan.io/extrinsic/23724311-3) | $10.67 / +14.9% | 🟡 Yes |
| 5 Jan 2026 | [189,555](https://assethub-polkadot.subscan.io/extrinsic/11102372-5) | $2.21 / +23.4% | 🟡 Yes |
| 27 Feb 2026 | [100,000](https://assethub-polkadot.subscan.io/extrinsic/12718518-2) | $1.60 / +21.8% | 🟡 Yes |
| 21 Aug 2026 | [103,626](https://assethub-polkadot.subscan.io/extrinsic/19714570-2) | $0.94 / +23.8% | 🟡 Yes |
| 8 Sep 2026 | [100,000](https://assethub-polkadot.subscan.io/extrinsic/20401730-2) | $1.25 / +40.2% | 🟡 Yes |
| 18 Sep 2026 | [122,760](https://assethub-polkadot.subscan.io/extrinsic/20793857-3) | $1.13 / +13.5% | 🟡 Yes |

- **Pump-day total into `14mr97…`: 4,016,425 DOT** (the 14 lots above plus smaller ones). After the 8 Sep 2026 deposit, `14mr97…` passed 20,494 DOT to `12xKCG…` two hours later and 40,988 the next day: a drip pattern consistent with an OTC desk or market maker selling, or a custodian rebalancing. Not provable from chain data.

**B. Direct exchange-pattern routing found (small, not on pump days).** `13FzGL…` sent 16,857 DOT on 19 Jan 2024 ([extrinsic](https://polkadot.subscan.io/extrinsic/19109283-2)) and 19,110 DOT on 29 Jan 2024 ([extrinsic](https://polkadot.subscan.io/extrinsic/19253141-2)) to deposit-style `13u6rd3F…`, which forwarded both to [`1qnJN7…t8GT7`](https://assethub-polkadot.subscan.io/account/1qnJN7FViy3HZaxZK9tGAA71zxHSBeUweirKqCaox4t8GT7), a hot wallet with **2.4M+ transfers** (an exchange by pattern; which one is [Unverified]). Neither day was a pump day. Other "hub" hits were XCM sends to the Bifrost (para 2030) and Hydration (para 2034) sovereign accounts, which are DeFi, not exchanges.

**C. Largest pump-day move checked and cleared.** On 3 Jan 2025 (+12.9%), genesis-era W3F-cluster account `15j4dg…` moved **6,827,024 DOT** to `15SBQ3…` ([1](https://polkadot.subscan.io/extrinsic/24126120-2) · [2](https://polkadot.subscan.io/extrinsic/24126469-3) · [3](https://polkadot.subscan.io/extrinsic/24127019-3)). It was split the same day into two 2M accounts and one 2.95M account, all of which are still staking or came back. **Internal, not a sale.**

**D. Treasury selling (disclosed).** OpenGov voted to sell treasury DOT for USDT/USDC in small DCA trades on Hydration: Refs 457, 1104, 1501 and **1729 (2,640,000 DOT, Aug 2025)**. These are public votes, so they are not a red line. [Ref 1729](https://polkadot.subsquare.io/referenda/1729) · [Ref 1104](https://polkadot.subsquare.io/referenda/1104) · [Ref 1953 fix](https://polkadot.polkassembly.io/referenda/1953).

**What it means:** No W3F or Parity wallet was caught paying an exchange on a pump day. But W3F-linked wallets, mainly one multisig account, have fed 33M DOT into one service, 4M of it on pump days, and the service is unnamed. W3F has said it doesn't need to sell DOT, yet these flows are not disclosed. **4**: a fail, but not the hard gate, because neither the owner nor the sale is proven.

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from Gate DOT_USDT UTC daily closes, re-run 16 Nov 2026 with scripts/pump_day_test.py (29 of 360 days); the body's earlier count used CoinGecko daily closes.

## 📊 Tokenomics & supply · 5/10 · ❌ FAIL

- **Supply now:** `Balances.TotalIssuance` on Asset Hub = **1,712,374,781 DOT** (Tier A RPC). `InactiveIssuance` 28.8M.
- **Hard cap 2.1B** from Wish-for-Change **Ref 1710** (passed Sep 2025, 81% aye). From **14 Mar 2026**, issuance dropped from ~120M to **~56M DOT/yr** (13.14% of the remaining gap to the cap per year, reset every two years; the cap is reached ~2160). [fellows #985](https://github.com/polkadot-fellows/runtimes/issues/985) · [Parity](https://www.parity.io/blog/refining-polkadots-economic-architecture-issuance-DOT-DAP-and-network-adjustments)
- **Still ~3.3% inflation a year** against near-zero fee demand. Treasury burns were switched off in Mar 2026 (surplus now goes to the DAP).
- **No admin mint key.** New DOT comes only from the runtime's issuance curve, which OpenGov can change by referendum (as it just did).
- ~908M DOT (≈ 53%) staked per the official developer site ([source](https://developers.polkadot.com/platform/)).

## 💧 Liquidity & market · 7/10 · ✅ PASS

- $58.8M 24h volume on a $1.25B cap (≈ 4.7% turnover). Listed widely: KuCoin $13.3M, BitDelta $10.4M, CoinW, Azbit, Binance $2.0M, OKX, WhiteBIT (CoinGecko tickers, 16 Nov 2026 5:10 AM MST). Also a US spot ETF (21Shares TDOT).
- 29 pump days in the last ~360 days, clustered in Aug–Sep 2026. Long downtrend: −74% in a year, −98.7% from ATH.

## 🧑‍💻 Product & development · 7/10 · ✅ PASS

- `paritytech/polkadot-sdk`: pushed 16 Nov 2026, **100+ commits since 18 Aug 2026** (API cap hit); `polkadot-fellows/runtimes`: 48 commits in the same window. [Tier A] GitHub API
- **Polkadot Hub smart contracts** (EVM-compatible REVM and native PVM) live since 27 Jan 2026 ([forum](https://forum.polkadot.network/t/release-of-smart-contracts-on-polkadot/16848)). **dotUSD**, a protocol-owned stablecoin, approved by Ref 1944 (Oct 2026) ([PCF](https://pcf.network/news/dotusd-approved/)).
- **JAM** (the next protocol) has no mainnet date; Gray Paper v1.0 is still the audit target ([forum: The Road to JAM](https://forum.polkadot.network/t/the-road-to-jam/18621)).

## 🤝 Adoption & customers · 4/10 · ❌ FAIL

- 37 active parachains (Parity postmortem, Mar 2026) ([forum](https://forum.polkadot.network/t/partial-polkadot-parachains-stall-on-runtime-upgrade-2-1-1-postmortem/17387)).
- The US ETF holds about **$8.2M** in net assets (21Shares product page) ([21shares](https://www.21shares.com/en-us/products-us/tdot)); Grayscale withdrew its DOT ETF in Aug 2026 ([CoinDesk](https://www.coindesk.com/business/2026/08/10/grayscale-quietly-drops-cardano-polkadot-and-hedera-etf-plans)).
- No named enterprise or bank customer paying in DOT was found. Fee data (above) says paid usage is tiny.

## 🛡️ Security & audits · 6/10 · ✅ PASS

- **No exploit of the relay chain or the protocol treasury found.**
- **2026 incidents (all postmortems are public, no funds lost):**
  - 23 Mar: 5 of 37 parachains stalled after runtime 2.1.1 ([postmortem](https://forum.polkadot.network/t/partial-polkadot-parachains-stall-on-runtime-upgrade-2-1-1-postmortem/17387)).
  - 22 Apr: People chain halted for 23 minutes ([postmortem](https://forum.polkadot.network/t/polkadot-people-chain-stall-degradation-postmortem/17729)).
  - 12 Jun: Asset Hub stopped producing blocks for ~30 minutes after runtime 2.3 (no formal postmortem found) ([forum](https://forum.polkadot.network/t/a-request-for-clarity-before-jam-the-people-who-funded-this-deserve-a-straight-answer/17969/2)).
  - 30 Jun – 3 Jul: the staking election froze after Refs 1890/1909; fixed by Ref 1914 ([postmortem](https://forum.polkadot.network/t/2026-06-30-staking-election-stall-postmortem/18077)).
- Four stalls in one year is a real cost to reliability, but each was disclosed and fixed quickly.

## ⚖️ Regulatory · 7/10 · ✅ PASS

- **21Shares Polkadot Staking ETF (TDOT)**: SEC registration effective 4 Mar 2026, trading on Nasdaq since 6 Mar 2026 ([Nasdaq circular](https://www.nasdaqtrader.com/content/newsalerts/2026/InfoCircular/TDOT_Circular_NQ.pdf) · [21shares](https://www.21shares.com/en-us/products-us/tdot)).
- No enforcement action against DOT, W3F or Parity was found this pass.

## 📅 Catalysts & calendar · 5/10 · ❌ FAIL

| Date | Event |
|---|---|
| Ongoing | DAP budgets set by OpenGov (validators, nominators, treasury, reserve) |
| Ongoing | dotUSD phase 2 (DOT-backed vaults) |
| No date | JAM mainnet hard fork |
| 14 Mar 2028 | Next step-down in issuance under Ref 1710 |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found on the relay chain or treasury |
| Team wallet → exchange during a pump | 🟡 **Not proven:** W3F-linked wallets (mainly `13FzGL…`) sent 4.02M DOT into deposit-style `14mr97…` on pump days (33.1M in total). The receiving service is unidentified. [21 Dec 2023](https://polkadot.subscan.io/extrinsic/18692262-332) · [8 Sep 2026](https://assethub-polkadot.subscan.io/extrinsic/20401730-2) · [`14mr97…`](https://assethub-polkadot.subscan.io/account/14mr97Z7TR26zrEqH4yS2PuUx3xEKjMRzrM2FvBpbU78xoq4) |
| Live mint path | 🟢 No admin key; issuance is protocol-set (~56M/yr) and capped at 2.1B |
| Treasury selling | 🟡 Disclosed DCA sales of treasury DOT (e.g. [Ref 1729](https://polkadot.subsquare.io/referenda/1729), 2.64M DOT) |
| Chain stalls | 🟡 Four partial stalls in 2026, all fixed; no funds lost |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| W3F-linked multisig-proxied account `13FzGL…` | Web3 Foundation (linked, not confirmed) | Subscan proxy links | low | no | None: the owner and the sale are not proven; Selling stays 4 |

## 📚 Sources

- [Tier A] Methodology update 16 Nov 2026: no new Arkham lookups; the attribution table uses evidence already cited in this report.
- [Tier A] Polkadot Asset Hub RPC (`polkadot-asset-hub-rpc.polkadot.io`): `Balances.TotalIssuance`, `InactiveIssuance`, `System.Account` for the treasury, DAP and the 15 W3F-linked accounts, 16 Nov 2026 ~5:10–6:00 AM MST
- [Tier A] Polkadot People-chain RPC: full `Identity.IdentityOf` (3,084 entries) and `SuperOf` (919) scan, 16 Nov 2026
- [Tier A] Statescan indexer APIs (relay `polkadot-api.statescan.io`, Asset Hub `ahp-api.statescan.io`): full transfer histories for the W3F-linked accounts, `14mr97…`, `12xKCG…`, `145UYr…`, `15G8FG…`, `15SBQ3…`; extrinsic decode of [18692262-332](https://polkadot-api.statescan.io/extrinsics/18692262-332)
- [Tier A] DefiLlama fees API (`polkadot`), 16 Nov 2026
- [Tier A] Official: [Parity blog (2 Mar 2026)](https://www.parity.io/blog/refining-polkadots-economic-architecture-issuance-DOT-DAP-and-network-adjustments) · [Polkadot forum, March 2026 changes](https://forum.polkadot.network/t/changes-on-polkadot-in-march-2026/17101) · [fellows runtimes #985](https://github.com/polkadot-fellows/runtimes/issues/985) · [developers.polkadot.com](https://developers.polkadot.com/platform/) · [2025-Q4 Treasury Report](https://forum.polkadot.network/t/2025-q4-polkadot-treasury-report/16847) · 2026 postmortems linked above
- [Tier A] OpenGov referenda: [1729](https://polkadot.subsquare.io/referenda/1729) · [1104](https://polkadot.subsquare.io/referenda/1104) · [1953](https://polkadot.polkassembly.io/referenda/1953) · [dotUSD Ref 1944 (PCF)](https://pcf.network/news/dotusd-approved/)
- [Tier A] [Nasdaq TDOT circular](https://www.nasdaqtrader.com/content/newsalerts/2026/InfoCircular/TDOT_Circular_NQ.pdf) · [21shares TDOT page](https://www.21shares.com/en-us/products-us/tdot)
- [Tier B] [Blockworks Token Transparency](https://blockworks.com/token-transparency/filing/polkadot) · [CryptoSlate](https://cryptoslate.com/web3-foundation-parity-technologies-dismiss-polkadot-treasury-depletion-fears/) · [CoinDesk (Grayscale withdrawal)](https://www.coindesk.com/business/2026/08/10/grayscale-quietly-drops-cardano-polkadot-and-hedera-etf-plans)
- [Tier A] CoinGecko `polkadot` market data and tickers (16 Nov 2026 5:10 AM MST); Binance DOT/USDT daily closes (from 18 Aug 2020)
- [Tier A] GitHub API: `paritytech/polkadot-sdk`, `polkadot-fellows/runtimes`
- [Unverified] who runs `14mr97…`/`12xKCG…`/`15G8FG…`; which exchange runs `1qnJN7…`; W3F ownership of every cluster account except the registered sub-identity `12RYJb…`; W3F's total DOT; Asset Hub fee totals. **Not covered by Arkham:** Arkham does not support Polkadot (checked 16 Nov 2026)

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| `12RYJb…` is a registered sub-identity of W3F's "W3F / Web 3 Technologies Foundation" identity | [W3F identity `14JezN…`](https://people-polkadot.subscan.io/account/14JezNxa4Fqzsf7ef9prYrNy71Cd1Ff3cZizFrntwviVuC9m) · [`12RYJb…`](https://people-polkadot.subscan.io/account/12RYJb5gG4hfoWPK3owEYtmWoko8G6zwYpvDYTyXFVSfJr8Y) | A (on-chain identity) | 16 Nov 2026 |
| `13FzGL…` ties to W3F: 255k in from `12RYJb…`, 570k back, 100 DOT to "W3F Governance Team" | [255k in](https://assethub-polkadot.subscan.io/extrinsic/19802011-2) · [570k back](https://assethub-polkadot.subscan.io/extrinsic/21296206-3) · [100 DOT](https://assethub-polkadot.subscan.io/extrinsic/10434763-2) · [W3F Gov Team identity](https://people-polkadot.subscan.io/account/14mmwp83EuacfrQTCCPUgRPJEeXuS52Psz95GDZEodj37imd) | A chain · owner [Unverified] | 16 Nov 2026 |
| `13FzGL…` is run through a 2-of-3 multisig proxy | [raw decoded call](https://polkadot-api.statescan.io/extrinsics/18692262-332) | A | 16 Nov 2026 |
| 33.1M DOT into `14mr97…`, 4.02M on pump days; `14mr97…` forwards to `12xKCG…`/`145UYr…` → `15G8FG…` | [`14mr97…`](https://assethub-polkadot.subscan.io/account/14mr97Z7TR26zrEqH4yS2PuUx3xEKjMRzrM2FvBpbU78xoq4) · [21 Dec 2023](https://polkadot.subscan.io/extrinsic/18692262-332) · [5 Jan 2026](https://assethub-polkadot.subscan.io/extrinsic/11102372-5) · [8 Sep 2026](https://assethub-polkadot.subscan.io/extrinsic/20401730-2) · [`12xKCG…`](https://assethub-polkadot.subscan.io/account/12xKCGbw56Bq8V4tdHT7QUabaWeUh8d935t81mPkjrWPi3ff) · [`15G8FG…`](https://assethub-polkadot.subscan.io/account/15G8FGwh2bk2XSAUjKJSZuHT1rdsbxLNr9CwED4mp6aZnZ8F) | A chain · service [Unverified] | 16 Nov 2026 |
| 35,967 DOT routed to exchange-pattern hot wallet `1qnJN7…` (Jan 2024, not pump days) | [19 Jan](https://polkadot.subscan.io/extrinsic/19109283-2) · [29 Jan](https://polkadot.subscan.io/extrinsic/19253141-2) · [`1qnJN7…`](https://assethub-polkadot.subscan.io/account/1qnJN7FViy3HZaxZK9tGAA71zxHSBeUweirKqCaox4t8GT7) | A chain · exchange name [Unverified] | 16 Nov 2026 |
| 6.83M DOT on the 3 Jan 2025 pump day was internal (re-staked) | [1](https://polkadot.subscan.io/extrinsic/24126120-2) · [2](https://polkadot.subscan.io/extrinsic/24126469-3) · [3](https://polkadot.subscan.io/extrinsic/24127019-3) · [`15SBQ3…`](https://assethub-polkadot.subscan.io/account/15SBQ3sdJZ7jEbpMABwr6hF7ZPjZuaPBAuN29tpPdCovjTDE) | A | 16 Nov 2026 |
| Treasury 21.46M DOT; DAP 7.37M DOT; total issuance 1.712B | [Treasury](https://assethub-polkadot.subscan.io/account/13UVJyLnbVp9RBZYFwFGyDvVd1y27Tt8tkntv6Q7JVPhFsTB) · [DAP](https://assethub-polkadot.subscan.io/account/13UVJyLkAxdQn6zM3GrLGvrFgN9jWneRX2NGvf3u92iunZq1) | A (RPC) | 16 Nov 2026 ~5:40 AM MST |
| Fees $3,868 in 365 days; $0 burned | [DefiLlama fees](https://api.llama.fi/summary/fees/polkadot?dataType=dailyFees) · [revenue](https://api.llama.fi/summary/fees/polkadot?dataType=dailyRevenue) | A | 16 Nov 2026 |
| 2.1B cap, ~56M/yr issuance from 14 Mar 2026, DAP replaces burns | [fellows #985](https://github.com/polkadot-fellows/runtimes/issues/985) · [Parity blog](https://www.parity.io/blog/refining-polkadots-economic-architecture-issuance-DOT-DAP-and-network-adjustments) | A | 16 Nov 2026 |
| Treasury DCA sales of DOT (disclosed) | [Ref 1729](https://polkadot.subsquare.io/referenda/1729) · [Ref 1104](https://polkadot.subsquare.io/referenda/1104) | A | 16 Nov 2026 |
| US spot ETF live since 6 Mar 2026 | [Nasdaq circular](https://www.nasdaqtrader.com/content/newsalerts/2026/InfoCircular/TDOT_Circular_NQ.pdf) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Who runs `14mr97…` → `12xKCG…`/`145UYr…` → `15G8FG…`?** (exchange, custodian, OTC desk or market maker) | Not covered by Arkham (no Polkadot support, checked 16 Nov 2026). Use Subscan's account labels and identity registry; ask W3F or the exchanges | Free |
| 2 | **Is `13FzGL…` Web3 Foundation's?** | Subscan label check (Arkham does not cover Polkadot); ask W3F; check the identities of the 3 multisig signers | Free |
| 3 | **Which exchange is `1qnJN7…`?** | Subscan label (Arkham does not cover Polkadot) | Free |
| 4 | **W3F's total DOT and wallet list** | Ask W3F; trace the rest of `15j4dg…`'s 162M DOT of 2020–2023 outflows | Free |
| 5 | **Asset Hub fee totals** | Subscan API (needs a key) or Parity data dashboards | Free/key |
| 6 | **Were the pump-day deposits sales?** | Ask W3F what the `14mr97…` account is for | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
