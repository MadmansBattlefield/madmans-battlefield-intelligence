---
ticker: ROSE
name: Oasis Network
chain: oasis (native consensus layer) · Sapphire / Emerald ParaTimes · bsc (bridged)
contract: "native coin; BSC 0xf00600ebc7633462bc4f9c61ea2ce99f5aaebd4a"
overall_score: 3.8
overall_verdict: FAIL
section_scores:
  revenue: 1
  foundation_team: 6
  insider_holdings: 4
  selling_behavior: 5
  tokenomics_supply: 5
  liquidity_market: 3
  product_development: 6
  adoption_customers: 2
  security_audits: 6
  regulatory: 5
  catalysts: 4
gates_failed: [revenue]
red_lines:
  hack_exploit: none found
  mint_path_live: "no; 10B cap fixed, staking rewards paid from a pre-funded common pool (497.6M ROSE left)"
  team_wallet_to_exchange_during_pump: "none found at 2 hops; suspected foundation wallets sent 108M ROSE on pump day 4 Sep 2026 to a non-exchange holder; attribution is community-sourced [Unverified]"
  one_hop_sale_status: none_found
  unlock_overhang: "896M ROSE still scheduled for Foundation, Community and Strategic buckets through Nov 2030 (≈56M per quarter, ≈ $258K at today's price)"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "No measurable revenue and no holder mechanism; staking rewards come from a pre-funded pool."
pump_day_price_source: "Gate ROSE_USDT UTC daily closes, re-run 16 Nov 2026 with scripts/pump_day_test.py (44 of 360 days); the body's earlier count used CoinGecko daily closes"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions: []
price_usd: 0.00461242
price_source: "CoinGecko, 16 Nov 2026 ~5:08 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### ROSE · Overall grade **3.8 / 10 · ❌ FAIL**

**Summary:** Oasis is a privacy-focused layer 1 with confidential-compute ParaTimes (Sapphire). After a **76% fall in a year** it is a **$37.5M market cap**. **DefiLlama tracks no fees**, and the two ParaTimes lock only **$0.39M** between them. **$1.39M trades a day**, and no exchange's ROSE pair does more than $0.31M. **896M ROSE** (≈ 9% of the cap) is still scheduled to unlock to the Foundation, Community and Strategic buckets through Nov 2030. No foundation-linked flow into a known exchange wallet was found, but the Foundation publishes no wallet list.

**🚨 Top warning:** the token earns nothing measurable while supply keeps arriving. **≈56M ROSE unlocks every quarter until Nov 2030** ([Oasis docs schedule](https://docs.oasis.io/general/oasis-network/token-metrics-and-distribution/)). That is ≈ $258K a quarter at today's price, small against $1.39M of daily volume, but it is steady supply with no revenue behind it. The Foundation also publishes no wallet list. On pump day **4 Sep 2026** (+10% or more over 5 days), two suspected Foundation delegation wallets moved [74M](https://explorer.oasis.io/mainnet/consensus/tx/05259778065e41fac40d1394526d1366dd5125e27e838d3c14aaf2370b910df2) and [34M](https://explorer.oasis.io/mainnet/consensus/tx/625eb0117dac533eab7212cb56a1c0597d52c5faa0351d9b648bee157eca35a7) ROSE to [`oasis1qqxc…ksal`](https://explorer.oasis.io/mainnet/consensus/address/oasis1qqxc9fnn8fftwfexrn98k52s9lvwu33d3c2pksal). That wallet has **never sent to a known exchange wallet**, so this is not a proven sale. Who owns either side is [Unverified]. All links are in the 🔗 Evidence trail.

**Sections passed: 3 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 1/10 | ❌ FAIL |
| 🏛️ Foundation & team | 6/10 | ✅ PASS |
| 🪙 Foundation / team holdings | 4/10 | ❌ FAIL |
| 📉 Selling behavior | 5/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 5/10 | ❌ FAIL |
| 💧 Liquidity & market | 3/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 6/10 | ✅ PASS |
| 🤝 Adoption & customers | 2/10 | ❌ FAIL |
| 🛡️ Security & audits | 6/10 | ✅ PASS |
| ⚖️ Regulatory | 5/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 4/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---

# 🪪 ROSE · Oasis Network · 3.8 / 10 · ❌ FAIL

> **One line:** Real privacy tech with almost no paid usage: no tracked fees, $0.39M in DeFi, thin volume, and 896M ROSE still to unlock over four years.

| 📊 Market (CoinGecko, 16 Nov 2026 ~5:08 AM MST) | 🔗 On-chain (Oasis Nexus, 16 Nov 2026) |
|---|---|
| **Price** $0.00461242 | **Native coin**, 10,000,000,000 cap (fixed) |
| **7d / 30d / 1y** 🔴 −15.4% / −41.1% / −76.2% | **Common pool** (staking rewards) [`oasis1qrmu…5zm`](https://explorer.oasis.io/mainnet/consensus/address/oasis1qrmufhkkyyf79s5za2r8yga9gnk4t446dcy3a5zm) 497.6M |
| **Market cap** $37.51M · **FDV** $46.17M | **Largest holder** [`oasis1qpg2…h70p`](https://explorer.oasis.io/mainnet/consensus/address/oasis1qpg2xuz46g53737343r20yxeddhlvc2ldqsjh70p) 1,655.2M; sent 1.0B to a new account today (community tag "Big Binance") |
| **24h volume** $1.39M | **Sapphire TVL** $0.20M · **Emerald TVL** $0.19M (DefiLlama) |
| **Circulating** 8.125B of 10B | **Unscheduled unlocks left** 896M (Foundation 400M · Community 296M · Strategic 200M) |
| **ATH** $0.5973 (14 Jan 2022) · now −99.2% | **Pump days** 43 of the last 365 |

---

## 💰 Revenue — Does it make money? · 1/10 · ❌ FAIL

| Metric | Value | Source |
|---|---:|---|
| Chain fees / revenue | **Not tracked** by DefiLlama (Oasis, Sapphire, Emerald all "not found") | [Tier A] DefiLlama fees API, 16 Nov 2026 |
| DeFi TVL (both EVM ParaTimes) | $0.39M | [Tier A] DefiLlama chains |
| Token value capture | Fees, staking and delegation only. No buyback or burn | [Tier A] [Oasis docs](https://docs.oasis.io/general/oasis-network/token-metrics-and-distribution/) |

**What it means:** There is no measurable revenue and no mechanism that returns value to holders. That is **1**, which **trips the Revenue gate**.

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** No measurable revenue and no holder mechanism; staking rewards come from a pre-funded pool.

## 🏛️ Foundation & team — Who is in charge? · 6/10 · ✅ PASS

- The **Oasis Foundation** runs the network and its grants. The protocol came out of Oasis Labs (academic founders, public team). The project raised **"over $45 million from backers" between 2018 and 2020** [Tier A docs].
- The Foundation stakes undistributed tokens across validators [Tier A docs]. It publishes **no wallet list**, so foundation wallets can only be inferred.

## 🪙 Foundation / team holdings — How many coins do they hold? · 4/10 · ❌ FAIL

| Bucket | ROSE | Share of 10B | Status (docs schedule) |
|---|---:|---:|---|
| Backers | 2,300,000,000 | 23.0% | Fully released |
| Core contributors | 2,000,000,000 | 20.0% | Fully released |
| Foundation endowment | 1,000,000,000 | 10.0% | **400M still scheduled** |
| Community & ecosystem | 1,850,000,000 | 18.5% | **296M still scheduled** |
| Strategic partners & reserve | 500,000,000 | 5.0% | **200M still scheduled** |
| Staking rewards | 2,350,000,000 | 23.5% | 497.6M left in the common pool |

*Source: [Tier A] Oasis docs [release-schedule CSV](https://docs.oasis.io/general/oasis-network/token-metrics-and-distribution/) (months 0–120).*

- Suspected foundation delegation wallets hold large stakes: [`oasis1qprt…3fcg`](https://explorer.oasis.io/mainnet/consensus/address/oasis1qprtzrg97jk0wxnqkhxwyzy5qys47r7alvfl3fcg) **649.8M staked** and [`oasis1qqja…c6zr`](https://explorer.oasis.io/mainnet/consensus/address/oasis1qqjak3gnnnxkc8rm9e6vu3rwt3hm3shq0y47c6zr) **442.7M staked** [Tier A balances]. They are linked to the Foundation only by a community tracker [Tier B, one source → Unverified].

**What it means:** Insiders started with **53.5%** (backers + contributors + Foundation + strategic). Another 896M is still to come, and the largest live stakes look like Foundation wallets but are not disclosed. That is **4**.

## 📉 Selling behavior — Do insiders sell into pumps? · 5/10 · ❌ FAIL

**Method:** the three biggest outflow receivers of the two suspected foundation wallets were tested against 12 community-tagged exchange wallets (Binance, Coinbase, Bybit, KuCoin, MEXC, Bitrue). The tags come from [this tracker](https://gardentools.jamie-oconnell.com/wallets.html) [Tier B, one source]. The test also checked pump days (CoinGecko closes, 43 in 365).

| Day (UTC) | From → to | ROSE | Pump? | Exchange? |
|---|---|---:|---|---|
| 4 Sep 2026 | `oasis1qprt…3fcg` → [`oasis1qqxc…ksal`](https://explorer.oasis.io/mainnet/consensus/address/oasis1qqxc9fnn8fftwfexrn98k52s9lvwu33d3c2pksal) ([tx](https://explorer.oasis.io/mainnet/consensus/tx/05259778065e41fac40d1394526d1366dd5125e27e838d3c14aaf2370b910df2)) | 74,000,000 | **Yes** | No |
| 4 Sep 2026 | `oasis1qqja…c6zr` → `oasis1qqxc…ksal` ([tx](https://explorer.oasis.io/mainnet/consensus/tx/625eb0117dac533eab7212cb56a1c0597d52c5faa0351d9b648bee157eca35a7)) | 34,000,000 | **Yes** | No |

- `oasis1qqxc…ksal` has received **667.9M** in total from those two wallets. Its outflows went mainly to `oasis1qrd3…gcfc` (268.4M, has never signed a transaction) and `oasis1qq6p…futg` (255.0M). **None of it went to a tagged exchange wallet** across its 753 loaded transfer events [Tier A].
- The other two big receivers, `oasis1qp2w…dslh` (460.1M) and `oasis1qzpu…nekw` (190.0M), also sent **nothing to tagged exchange wallets** [Tier A].
- Today, 16 Nov 2026 (01:09 UTC), the largest holder `oasis1qpg2…h70p` (1,655.2M) moved [1.0B ROSE](https://explorer.oasis.io/mainnet/consensus/tx/f890a1c34d92dc7f27aa2f2ea78fed40f07d14610636ba0a03edc75b0a8d6f8c) to a new account. It swaps lots of 15–60M with Binance's hot wallet `oasis1qzwf…urdgu` (nonce 174,897), so this looks like exchange custody, not a team move [Tier A pattern + Tier B tag].

**What it means:** No sale into a pump by a foundation wallet was found at 2 hops. But the Foundation's wallets aren't disclosed, and large pump-day moves were found whose purpose is unknown. That is **5**: not a gate fail, not proven clean.

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from Gate ROSE_USDT UTC daily closes, re-run 16 Nov 2026 with scripts/pump_day_test.py (44 of 360 days); the body's earlier count used CoinGecko daily closes.

## 📊 Tokenomics & supply · 5/10 · ❌ FAIL

- 10B fixed cap; 81% circulating. Staking rewards come from a pre-funded pool, so there is no new minting [Tier A docs].
- **≈56M ROSE every quarter** (Strategic 12.5M + Community 18.5M + Foundation 25M) until month 120 (≈ Nov 2030). That is 896M, about 11% of today's circulating supply.

## 💧 Liquidity & market · 3/10 · ❌ FAIL

- **$1.39M** in 24h volume (3.7% of market cap). The top pairs are Binance ROSE/USDT $0.31M, WhiteBIT $0.26M, Coinstore $0.19M and BTCC $0.15M [Tier A CoinGecko tickers]. That is thin: no single venue trades more than $0.31M a day (order books not read).
- 43 pump days in a year on a falling chart (−99.2% from ATH).

## 🧑‍💻 Product & development · 6/10 · ✅ PASS

- Mainnet since Nov 2020. **Sapphire** is a confidential EVM, and ROFL offers off-chain TEE compute [Tier A docs]. Development is ongoing under the public `oasisprotocol` GitHub org; repo activity was not measured this pass.

## 🤝 Adoption & customers · 2/10 · ❌ FAIL

- **$0.39M in DeFi TVL** across Sapphire and Emerald (DefiLlama). Paying users or enterprise customers were not evidenced from primary sources.

## 🛡️ Security & audits · 6/10 · ✅ PASS

- No protocol hack found. The consensus layer is a Tendermint-style BFT chain with ~120 validators, and slashing covers double-signing [Tier A docs].
- TEE-based privacy brings hardware trust assumptions. ParaTime audits were not read this pass.

## ⚖️ Regulatory · 5/10 · ❌ FAIL

- No enforcement action found. No MiCA white-paper check was done this pass. Not proven.

## 📅 Catalysts & calendar · 4/10 · ❌ FAIL

| Date | Event |
|---|---|
| Quarterly to ≈ Nov 2030 | ≈56M ROSE scheduled unlocks (Foundation, Community, Strategic) |
| Every epoch | Staking rewards from the common pool (~2.6% a year) |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Live mint path | 🟢 None (fixed cap, pre-funded rewards) |
| Team wallet → exchange during a pump | 🟢 None found at 2 hops · 🟡 108M pump-day move to a non-exchange holder; foundation wallets undisclosed |
| Unlock overhang vs liquidity | 🟡 896M left, ≈56M (≈ $258K) per quarter, against $1.39M a day of volume |
| Revenue | 🔴 None tracked |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| Suspected foundation wallets (108M on a pump day) | Not confirmed | Chain trace only | low | no | None: cannot move Selling; stays 5 |

## 📚 Sources

- [Tier A] Methodology update 16 Nov 2026: no new Arkham lookups; the attribution table uses evidence already cited in this report.
- [Tier A] Oasis Nexus API (`/consensus/accounts`, `/consensus/accounts/{addr}`, `/consensus/events?type=staking.transfer`), 16 Nov 2026 MST
- [Tier A] [Oasis docs: token metrics and distribution](https://docs.oasis.io/general/oasis-network/token-metrics-and-distribution/), with release-schedule and reward-schedule CSVs
- [Tier A] DefiLlama fees API and chain TVL; CoinGecko `oasis-network` market data, tickers and 365-day closes
- [Tier B] Community exchange and foundation wallet tags: [Garden Tools wallet map](https://gardentools.jamie-oconnell.com/wallets.html) (single source, self-described as speculative)
- [Unverified] Foundation wallet identities; owners of `oasis1qqxc…`, `oasis1qrd3…`, `oasis1qq6p…`, `oasis1qp2w…`

## 🔗 Evidence trail

*Every link below opens the primary record for the claim.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Allocation and 120-month release schedule | [Oasis docs](https://docs.oasis.io/general/oasis-network/token-metrics-and-distribution/) | A | 16 Nov 2026 |
| No tracked fees; $0.39M TVL | [DefiLlama API](https://api.llama.fi/summary/fees/oasis-sapphire?dataType=dailyFees) · [chains](https://defillama.com/chains) | A | 16 Nov 2026 |
| Suspected foundation stakes 649.8M and 442.7M | [`oasis1qprt…`](https://explorer.oasis.io/mainnet/consensus/address/oasis1qprtzrg97jk0wxnqkhxwyzy5qys47r7alvfl3fcg) · [`oasis1qqja…`](https://explorer.oasis.io/mainnet/consensus/address/oasis1qqjak3gnnnxkc8rm9e6vu3rwt3hm3shq0y47c6zr) | A balance · B attribution | 16 Nov 2026 |
| 108M moved on pump day 4 Sep 2026 | [74M](https://explorer.oasis.io/mainnet/consensus/tx/05259778065e41fac40d1394526d1366dd5125e27e838d3c14aaf2370b910df2) · [34M](https://explorer.oasis.io/mainnet/consensus/tx/625eb0117dac533eab7212cb56a1c0597d52c5faa0351d9b648bee157eca35a7) | A | 16 Nov 2026 |
| Receiver never paid a tagged exchange wallet | [`oasis1qqxc…`](https://explorer.oasis.io/mainnet/consensus/address/oasis1qqxc9fnn8fftwfexrn98k52s9lvwu33d3c2pksal) | A chain + B tags | 16 Nov 2026 |
| Largest holder is exchange custody | [`oasis1qpg2…`](https://explorer.oasis.io/mainnet/consensus/address/oasis1qpg2xuz46g53737343r20yxeddhlvc2ldqsjh70p) · [1.0B move](https://explorer.oasis.io/mainnet/consensus/tx/f890a1c34d92dc7f27aa2f2ea78fed40f07d14610636ba0a03edc75b0a8d6f8c) · [Binance hot](https://explorer.oasis.io/mainnet/consensus/address/oasis1qzwfdgpt3p6dd2mk6207qhf9qrxuvfn9eunurdgu) | A pattern + B tag | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Wallet labels for 10 Oasis wallets** (the maintainer's `arkham/rose_addresses.csv` list: suspected foundation wallets, pump-day receiver `oasis1qqxc…` and its two big recipients) | **Not covered by Arkham:** Arkham does not support Oasis (checked 16 Nov 2026). Use Oasis Explorer / Oasisscan tags, or ask the Oasis Foundation to publish its wallets | Free |
| 2 | **Which wallets are the Foundation's?** | Ask the Oasis Foundation to publish its endowment, community and strategic wallet addresses; check them against the schedule CSV | Free |
| 3 | **Exchange deposit addresses** | Oasis exchanges use per-user deposit accounts. Run a 3rd hop from `oasis1qrd3…` and `oasis1qq6p…` to see whether funds sweep into the tagged hot wallets | Free (Nexus) |
| 4 | **Second source for exchange tags** | Confirm the Binance / Coinbase / Bybit tags with a withdrawal test or the exchanges' published proof-of-reserves addresses (Arkham does not cover Oasis) | Free / small |
| 5 | **Fee revenue** | Sum consensus and Sapphire gas fees from Nexus per epoch for 12 months | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
