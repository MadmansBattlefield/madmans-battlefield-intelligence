---
ticker: POLYX
name: Polymesh
chain: polymesh
contract: "native (Polymesh mainnet balances; SS58 prefix 12)"
overall_score: 3.0
overall_verdict: FAIL
section_scores:
  revenue: 1
  foundation_team: 4
  insider_holdings: 3
  selling_behavior: 0
  tokenomics_supply: 4
  liquidity_market: 4
  product_development: 6
  adoption_customers: 2
  security_audits: 6
  regulatory: 6
  catalysts: 4
gates_failed: [revenue, selling_behavior]
red_lines:
  hack_exploit: none found
  mint_path_live: "no max supply; staking issuance up to 140M POLYX/yr (docs); supply grew 1.2187B -> 1.3398B (+9.9%) in the last 12 months"
  team_wallet_to_exchange_during_pump: "YES by pattern: Polymesh Association-listed and genesis-identity wallets (plus 2HXnHMiy..., funded by Association wallets) sent 187.3M POLYX in 139 transfers into memo-deposit address 2F8aakk..., 32.9M of it on pump days (34 transfers), 59.3M in the last 12 months; exchange name [Unverified]"
  treasury_selling: "not disclosed; Association assets incl. POLYX sold to Polymath (Jun 2025), Polymath acquired by Nasdaq-listed TruGolf (Oct 2026)"
  fee_capture: "fees go to block-producing operators, not holders; 4,780 POLYX of fees in 365 days"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "The chain earns almost nothing and fees go to block producers; Polymath's SaaS revenue belongs to a company."
pump_day_price_source: "Gate POLYX_USDT UTC daily closes, re-run 16 Nov 2026 with scripts/pump_day_test.py (33 of 360 days); the body's earlier count used the daily closes cited in the body"
pump_day_disclosure_quality: silence
pump_day_undisclosed_penalty_applied: true
dual_review: not_run
attributions: []
price_usd: 0.02545
price_source: "CoinGecko, 16 Nov 2026 5:10 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### POLYX · Overall grade **3.0 / 10 · ❌ FAIL**

**Summary:** Polymesh is a purpose-built chain for regulated securities with identity and compliance built into the base layer, and it keeps shipping (runtime 8.1.3 on 11 Nov 2026 gave every asset an EVM address). But almost nobody uses it: in the last 12 months the whole network paid **4,780 POLYX (~$120) in fees**, created **28 assets** and settled **129 instructions**, and the fees go to node operators, not holders. Supply grew **9.9%** in a year with no cap. The Polymesh Association sold its assets, including its POLYX, to Polymath in June 2025, and Polymath was bought by Nasdaq golf-simulator company TruGolf in October 2026. On-chain, **Association and genesis-identity wallets have sent 187.3M POLYX (14% of supply) into one memo-style exchange deposit address, 32.9M of it on pump days and 59.3M in the last 12 months.**

**🚨 Top warning:** The Polymesh Association lists [`2FEWmT…fBvLh`](https://polymesh.subscan.io/account/2FEWmTkH9czpKJSnnFxJhMaKHaM6H7k57PDSqJgqifwfBvLh), [`2DbjUi…JWePw6Y`](https://polymesh.subscan.io/account/2DbjUiD2vUgPaWyFgmNnbWXGBRS8QxG5yy71Vhd35WJePw6Y) and five other addresses as its own in its [official circulating-supply page](https://raw.githubusercontent.com/PolymeshAssociation/PolymeshAssociation.github.io/main/circulating-supply/index.html). Those wallets, the genesis identity #1 wallets ([`2FTmkf…yom4q`](https://polymesh.subscan.io/account/2FTmkfcG6qxGWZ3MY5L9ctNyeJ6rauRfMEtknKTjXz1yom4q), [`2CjgV6…6sBUGVX`](https://polymesh.subscan.io/account/2CjgV6Mp6HwdhwWYPZFaZYGhDe74EhyYEGrqoaHoR6sBUGVX)) and [`2HXnHM…HCup`](https://polymesh.subscan.io/account/2HXnHMiy3nSCd12kJHaWpVirdqNDRnSSAQef8Mm76QrRHCup) (funded with 52.5M POLYX by Association wallets in 2026) sent **187.3M POLYX in 139 transfers (Sep 2022 – Oct 2026)** into [`2F8aak…6wo4`](https://polymesh.subscan.io/account/2F8aakkWMbuLqFD1Zc2q3Bss88TTbeazX2MEoCfeUMqk6wo4). That address has taken deposits from 479 senders with 1,691 different numeric memos since mid-2024 and sweeps everything to [`2CoSRa…roua`](https://polymesh.subscan.io/account/2CoSRaWBjmxEWikG1FbzXe63G9DGayCpUnnVPkJu5V14roua): an exchange deposit pattern. **32.9M went in on pump days**, e.g. [3M on 24 Oct 2023 (+71.8%)](https://polymesh.subscan.io/block/10341720), [4M on 25 Mar 2024 (+74.9%)](https://polymesh.subscan.io/block/12545731) and [2M on 15 Sep 2026 (+11.2%)](https://polymesh.subscan.io/extrinsic/25546196-1). The exchange's name is **[Unverified]**, and no sale disclosure was found. Every link is in the 🔗 Evidence trail below.

**Sections passed: 3 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 1/10 | ❌ FAIL |
| 🏛️ Foundation & team | 4/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 3/10 | ❌ FAIL |
| 📉 Selling behavior | 0/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 4/10 | ❌ FAIL |
| 💧 Liquidity & market | 4/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 6/10 | ✅ PASS |
| 🤝 Adoption & customers | 2/10 | ❌ FAIL |
| 🛡️ Security & audits | 6/10 | ✅ PASS |
| ⚖️ Regulatory | 6/10 | ✅ PASS |
| 📅 Catalysts & calendar | 4/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 POLYX · Polymesh · 3.0 / 10 · ❌ FAIL

> **One line:** A well-engineered securities chain that almost nobody pays to use (~$120 of fees in a year, all to operators), with ~10% yearly inflation, and whose foundation-side wallets have fed 187M POLYX into one exchange-style deposit address, 33M of it on pump days.

| 📊 Market (CoinGecko, 16 Nov 2026 5:10 AM MST) | 🔗 On-chain (Polymesh mainnet, 16 Nov 2026) |
|---|---|
| **Price** $0.02545 | **Token** native POLYX (6 decimals), runtime spec 8001030 |
| **24h / 7d / 30d** 🔴 −2.8% / −15.2% / −29.6% · 1y −64.3% | **`Balances.TotalIssuance`** 1,339,757,233 POLYX (block ~26,425,941) |
| **Market cap** $34.1M · **FDV** $34.1M (no max supply) | **12 months ago** 1,218,729,136 POLYX (block 21,184,603) → **+9.9%** |
| **24h volume** $472k (Binance $281k, Upbit $151k) | **Association-listed wallets** 191.7M POLYX (14.3%) · genesis identity #1 62.7M (4.7%) |
| **ATH** $0.7488 (31 Mar 2024) · now −96.6% | **Largest single wallet** [`2DzB6L…FUkb`](https://polymesh.subscan.io/account/2DzB6Lg4WdUWXC6Pt95L3aqisDVS92M6MuCvfAkbVBQLFUkb) 511.4M (38.2%), owner [Unverified] |
| **Pump days, last ~360 days** 32 (Binance POLYX/USDT closes) | **Accounts holding POLYX** 7,602 (full `System.Account` scan) |

---

## 💰 Revenue — Does it make money? · 1/10 · ❌ FAIL

| Metric | Value | Source |
|---|---:|---|
| Network fees paid, last 365 days | **4,779.69 POLYX** (~$122 at today's price) in 43,901 fee payments | [Tier A] Polymesh middleware indexer (`mainnet-graphql.polymesh.network`), `TransactionFeePaid` sum since 16 Nov 2025, read 16 Nov 2026 |
| Network fees, all-time (since Oct 2021) | 33,833.84 POLYX | [Tier A] same indexer |
| Where fees go | "Both transaction and protocol fees are paid to the operator that produces a block" | [Tier A] [Polymesh docs: Network Fees](https://developers.polymesh.network/polyx/fees/) |
| Only protocol fee | 25 POLYX to register a ticker | [Tier A] [Polymesh docs: Network Fees](https://developers.polymesh.network/polyx/fees/) |
| Fees to holders / buyback / burn | **None** | [Tier A] docs above; no burn mechanism found |
| On-chain treasury (`pm/trsry`) | **0 POLYX** in [`2EvQQs…LroV`](https://polymesh.subscan.io/account/2EvQQsqdCSiHGUXeTqp5F1i76GFBheTUG7rLdRXk3qAcLroV) | [Tier A] RPC `System.Account` |
| Company revenue (not token revenue) | Polymath had **$4.2M of revenue in 2025** and $21M of assets | [Tier A] [TruGolf 8-K Ex. 99.1, 18 Aug 2026](https://www.sec.gov/Archives/edgar/data/1857086/000149315226038904/ex99-1.htm) |

**What it means:** The chain earns almost nothing, and what it earns goes to block producers. Polymath's $4.2M of SaaS revenue belongs to a company (now inside TruGolf), not to POLYX holders. **1, which trips the Revenue gate.**

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** The chain earns almost nothing and fees go to block producers; Polymath's SaaS revenue belongs to a company.

## 🏛️ Foundation & team — Who is in charge? · 4/10 · ❌ FAIL

| Item | Finding | Source |
|---|---|---|
| Original steward | **Polymesh Association** (Switzerland), on-chain genesis identity `0x04…` (16 accounts); its addresses are listed on its own supply page | [Tier A] [Association supply page source](https://raw.githubusercontent.com/PolymeshAssociation/PolymeshAssociation.github.io/main/circulating-supply/index.html) · indexer identity `0x04…` |
| Genesis roles | Chain spec: identity 1 = "[Polymesh] GenesisCouncil (1 of 3) + UpgradeCommittee + TechnicalCommittee"; 2, 3 = council; 4 = operators; 5 = sudo | [Tier A] [`mainnet_runtime.rs`](https://github.com/PolymeshAssociation/Polymesh/blob/develop/src/chain_spec/mainnet_runtime.rs) |
| June 2025 | **Polymath bought "certain assets … of Polymesh Switzerland, including POLYX tokens held by Polymesh Switzerland"** into Polymesh Labs Ltd (Cayman subsidiary) | [Tier B] [AnalytixInsight release, 27 Jun 2025](https://www.newsfilecorp.com/release/257215/AnalytixInsight-Inc.-Provides-Update-to-Reverse-Takeover-Transaction-with-Polymath-Research-Inc.) (TSXV issuer's own release) |
| October 2026 | **TruGolf Holdings (NASDAQ: TRUG)**, a golf-simulator company, closed its acquisition of Polymath; Polymath is now a wholly owned subsidiary | [Tier A] [Polymath announcement, 9 Oct 2026](https://www.polymath.network/articles/trugolf-completes-acquisition-of-polymath) · [TruGolf 8-K, 18 Aug 2026](https://www.sec.gov/Archives/edgar/data/1857086/000149315226038904/ex99-1.htm) |
| Paid in POLYX | TruGolf's new CFO/COO gets **$25,000 a year of her salary in POLYX** | [Tier A] [TruGolf 8-K Ex. 10.4, 9 Oct 2026](https://www.sec.gov/Archives/edgar/data/1857086/000149315226046435/ex10-4.htm) |
| Who decides upgrades | On-chain PIPs, a Governing Council and committees seeded at genesis | [Tier A] [Polymesh docs: Governance](https://developers.polymesh.network/governance/) |

**What it means:** The token's steward went from a Swiss non-profit to a for-profit Cayman subsidiary to a small Nasdaq company that needs cash (it raised $2.95M from preferred warrants the day before closing). The people are public and the filings are real, but holders now depend on a company whose interests are its shareholders', not POLYX holders'. **4.**

## 🪙 Foundation / team holdings — How many coins do they hold? · 3/10 · ❌ FAIL

| Bucket | POLYX | Notes |
|---|---:|---|
| Association-listed addresses (7 wallets + treasury + rewards pots) | **191.7M (14.3%)** | Listed in the [supply page](https://raw.githubusercontent.com/PolymeshAssociation/PolymeshAssociation.github.io/main/circulating-supply/index.html); largest: [`2FT35T…yHMa`](https://polymesh.subscan.io/account/2FT35TKtSvjrKPhwzSbHE2aqWnEYiMubrjxj9pZUQDM9yHMa) 59.5M · [`2HexZQ…7HMq`](https://polymesh.subscan.io/account/2HexZQdNn9KziSkEek6E1Y68gUdP69JFs8szQQyUvYBX7HMq) 59.5M · [`2DbjUi…JWePw6Y`](https://polymesh.subscan.io/account/2DbjUiD2vUgPaWyFgmNnbWXGBRS8QxG5yy71Vhd35WJePw6Y) 59.3M · [`2F5eK4…jbkK`](https://polymesh.subscan.io/account/2F5eK4mfXfMRYmfYAsvqnakTDVn7CciBKtmY3b5yA5vJbjkK) 5.66M. Treasury and rewards pots hold 0 |
| Genesis identity #1 (`0x01…`, 11 accounts) | **62.7M (4.7%)** | e.g. [`2FTmkf…yom4q`](https://polymesh.subscan.io/account/2FTmkfcG6qxGWZ3MY5L9ctNyeJ6rauRfMEtknKTjXz1yom4q) 28.4M · [`2FoTUs…5f2`](https://polymesh.subscan.io/account/2FoTUsfoAUSw3yVfwuq6NzWegD1ak1nxTsgjFtU5VtR9C5f2) 16.4M · [`2EcsMG…sbZN`](https://polymesh.subscan.io/account/2EcsMGNDthpDiDRcngm3JUFQE2TaitjDSLtX8HV86tfQbsZN) 16.4M. Polymesh's own council seat per the chain spec; current owner after the 2025 asset sale [Unverified] |
| [`2HXnHM…HCup`](https://polymesh.subscan.io/account/2HXnHMiy3nSCd12kJHaWpVirdqNDRnSSAQef8Mm76QrRHCup) (identity created 21 Jul 2025) | **7.0M** | Funded with 52.5M POLYX by Association wallets in 2026; owner (likely Polymesh Labs) [Unverified] |
| **Total foundation-side found** | **~261M (≈ 19.5%)** | Ownership now sits with Polymath / TruGolf per the asset sale; no current wallet list from them |
| Largest wallet: [`2DzB6L…FUkb`](https://polymesh.subscan.io/account/2DzB6Lg4WdUWXC6Pt95L3aqisDVS92M6MuCvfAkbVBQLFUkb) | 511.4M (38.2%) | Single-account identity; 1.02B in / 732M out, mostly from two feeder accounts. Looks like custodial cold storage. Owner [Unverified]; Arkham does not cover Polymesh |

**What it means:** About a fifth of supply sits with the foundation side, now controlled by a company, and that side has been steadily moving coins to an exchange-style address (see Selling). One unlabeled wallet holds 38%. **3.**

## 📉 Selling behavior — Do insiders sell into pumps? · 0/10 · ❌ FAIL

**Deposit address.** [`2F8aak…6wo4`](https://polymesh.subscan.io/account/2F8aakkWMbuLqFD1Zc2q3Bss88TTbeazX2MEoCfeUMqk6wo4) (identity `0x45fd73…`, created Sep 2022) received deposits from **479 senders with 1,691 different numeric memos** since June 2024 (the memo pattern exchanges use to credit users) and swept them to [`2CoSRa…roua`](https://polymesh.subscan.io/account/2CoSRaWBjmxEWikG1FbzXe63G9DGayCpUnnVPkJu5V14roua) in 13,000+ transfers. It holds only ~80k POLYX. That is an exchange deposit pattern; which exchange is **[Unverified]**.

**What went in from foundation-side wallets (indexer, de-duplicated):**

| Sender group | POLYX into `2F8aak…` | Transfers |
|---|---:|---:|
| Genesis identity #1 (`2FTmkf…`, `2CjgV6…` and others) | 98,492,103 | 62 |
| Association-listed wallets (`2FEWmT…` and others) | 42,342,684 | 47 |
| `2HXnHM…` (funded by Association wallets) | 46,499,995 | 30 |
| **Total, Sep 2022 – Oct 2026** | **187,334,782 (≈ $29.2M at each day's close)** | **139** |

By year: 2022 7.5M · 2023 49.4M · 2024 40.1M · 2025 31.1M · **2026 59.3M** (Aug–Oct 2026 alone ≈ 45M, around the TruGolf deal). Another 4.0M went from `2HXnHM…` to a second memo address [`2EJz9E…uaeyy`](https://polymesh.subscan.io/account/2EJz9EwEQ31jmKSQwQXH4uudNDbnJU1hK7cYU7jQiaKYaeuy) on 1 Nov 2026.

**Pump-day deposits (Binance POLYX/USDT closes), lots of 1M+:**

| Day (UTC) | POLYX into `2F8aak…` | From | Close / 5-day change |
|---|---:|---|---:|
| 20 Oct 2023 | [1,500,000](https://polymesh.subscan.io/block/10286711) | `2FTmkf…` | $0.194 / +61.3% |
| 24 Oct 2023 | [2,000,000](https://polymesh.subscan.io/block/10339984) + [3,000,000](https://polymesh.subscan.io/block/10341720) + [3,000,000](https://polymesh.subscan.io/block/10345143) | `2FTmkf…` | $0.257 / +71.8% |
| 4 Mar 2024 | [1,000,000](https://polymesh.subscan.io/block/12241401) | `2FTmkf…` | $0.240 / +23.8% |
| 13 Mar 2024 | [5,000,000](https://polymesh.subscan.io/block/12370209) | `2FEWmT…` (Association) | $0.281 / +12.1% |
| 25 Mar 2024 | [2,000,000](https://polymesh.subscan.io/block/12543282) + [2,000,000](https://polymesh.subscan.io/block/12545329) + [4,000,000](https://polymesh.subscan.io/block/12545731) | `2FTmkf…`, `2FEWmT…` | $0.597 / +74.9% |
| 26 Mar 2024 | [1,000,000](https://polymesh.subscan.io/block/12555513) | `2FTmkf…` | $0.580 / +42.2% |
| 22 Nov 2024 | [1,698,000](https://polymesh.subscan.io/extrinsic/16017779-1) | `2FTmkf…` | $0.337 / +18.9% |
| 12 Feb 2025 | [1,700,000](https://polymesh.subscan.io/extrinsic/17200135-1) | `2CjgV6…` | $0.191 / +13.3% |
| 12 Sep 2025 | [1,900,000](https://polymesh.subscan.io/extrinsic/20250342-1) | `2CjgV6…` | $0.141 / +10.5% |
| 15 Sep 2026 | [2,000,000](https://polymesh.subscan.io/extrinsic/25546196-1) | `2HXnHM…` | $0.0386 / +11.2% |
| 22 Sep 2026 | [1,000,000](https://polymesh.subscan.io/extrinsic/25648436-1) | `2HXnHM…` | $0.0439 / +15.8% |

- **Pump-day total: 32,877,835 POLYX in 34 transfers.** The 2023–2024 lots were sent without an extrinsic of their own (executed inside the block, e.g. by a multisig), so the links point at the block; the sender, receiver and amount come from the Polymesh indexer.
- **Last 12 months: 59.3M POLYX** (≈ 4.4% of supply) went into this one deposit address.
- No sale disclosure, unlock schedule or treasury report from the Association, Polymath or TruGolf was found.

**What it means:** Wallets the Association itself lists, plus its genesis council identity, have paid an exchange-style deposit address for four years, including big lots on the strongest pump days (+72% and +75%). The exchange is not named, so it stays "by pattern", but the senders are Tier A. **2, which trips the Selling gate.**

- **Disclosure quality (16 Nov 2026 rules): silence.** No disclosure was found. The receiving address is proven to be an exchange deposit by its on-chain memo pattern, not by a label. **Penalty applied (16 Nov 2026 rules):** a proven pump-day sale with no disclosure fails Selling (ordinary score at most 3) and then loses 2 points, floored at 0: **2 → 0**. Pump days from Gate POLYX_USDT UTC daily closes, re-run 16 Nov 2026 with scripts/pump_day_test.py (33 of 360 days); the body's earlier count used the daily closes cited in the body.

## 📊 Tokenomics & supply · 4/10 · ❌ FAIL

- **No max supply.** New POLYX is minted each era for operators and stakers, "capped at a maximum of 140 million POLYX per year" ([docs](https://developers.polymesh.network/polyx/tokenomics/)). POLY on Ethereum can also be upgraded 1:1 through a one-way bridge ([blog](https://polymesh.network/blog/understanding-polyx-tokenomics)).
- **Supply grew 121.0M (+9.9%) in 12 months** (1,218,729,136 → 1,339,757,233; Tier A RPC at blocks 21,184,603 and 26,425,941).
- Staking rewards are the only yield, paid in new coins.

## 💧 Liquidity & market · 4/10 · ❌ FAIL

- $472k 24h volume on a $34.1M cap. Binance POLYX/USDT $281k and Upbit POLYX/KRW $151k are ~92% of it; then Pionex, BitKan, Gate, Crypto.com (CoinGecko tickers, 16 Nov 2026 5:10 AM MST).
- −96.6% from the Mar 2024 high, −64% in a year. 32 pump days in the last ~360 days.

## 🧑‍💻 Product & development · 6/10 · ✅ PASS

- **Polymesh 8.1.3** live on mainnet (11 Nov 2026): every asset gets an EVM address, issuers can freeze single holders ([blog](https://polymesh.network/blog/polymesh-8-1-3-mainnet-upgrade)).
- Confidential assets on a new DevNet; AlphaPoint integration ([blog index](https://polymesh.network/blog)).
- Identity, compliance and settlement are native to the chain ([docs](https://developers.polymesh.network/)).

## 🤝 Adoption & customers · 2/10 · ❌ FAIL

| Last 12 months (indexer, from block 21,184,603) | Count |
|---|---:|
| New assets created | **28** |
| Settlement instructions | **129** (91 executed) |
| Asset transfers | **186** |
| Signed extrinsics | 43,799 |
| New identities | 205 (8,366 all-time) |

- All-time: 560 assets; the most-transferred asset ever is an NFT collection with 670 transfers.
- Polymath claims "$132 million in tokenized assets for more than 65 active issuers" as of 31 Dec 2025 ([Polymath](https://www.polymath.network/articles/trugolf-completes-acquisition-of-polymath)); company-stated and **[Unverified]** on-chain.

## 🛡️ Security & audits · 6/10 · ✅ PASS

- No exploit of the chain or its bridge found this pass ([Unverified] absence; no incident page read).
- Permissioned operators (licensed institutions); Polymath states SOC 2 Type 1 compliance ([Polymath](https://www.polymath.network/articles/trugolf-completes-acquisition-of-polymath)).

## ⚖️ Regulatory · 6/10 · ✅ PASS

- Built for regulated securities; every account needs a verified identity (CDD) to hold POLYX.
- The steward is now a subsidiary of an SEC-reporting Nasdaq company, so POLYX facts may show up in its filings (one already does: salary paid in POLYX).
- No enforcement action against POLYX, Polymath or the Association was found this pass.

## 📅 Catalysts & calendar · 4/10 · ❌ FAIL

| Date | Event |
|---|---|
| Ongoing | TruGolf integration of Polymath; possible POLYX disclosures in TruGolf 10-Q/10-K |
| Q1 2027 | TruGolf Links equipment-leasing program funded by tokenized securities (target) |
| Ongoing | EVM-addressed assets (8.1.3), confidential assets DevNet |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | 🔴 **Yes, by pattern:** Association-listed and genesis wallets sent 32.9M POLYX into memo-deposit `2F8aak…` on pump days (187.3M in total). [24 Oct 2023](https://polymesh.subscan.io/block/10341720) · [25 Mar 2024](https://polymesh.subscan.io/block/12545731) · [15 Sep 2026](https://polymesh.subscan.io/extrinsic/25546196-1) · [`2F8aak…`](https://polymesh.subscan.io/account/2F8aakkWMbuLqFD1Zc2q3Bss88TTbeazX2MEoCfeUMqk6wo4). Exchange name [Unverified] |
| Live mint path | 🟡 No admin mint key, but uncapped staking issuance (+9.9% in 12 months) |
| Treasury selling | 🔴 Not disclosed; Association POLYX sold to Polymath (2025) |
| Fee capture | 🔴 Fees go to operators; ~4,780 POLYX in a year |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| Association-listed and genesis-identity wallets | Polymesh Association | The Association's own wallet list (Tier A) | high | yes | Selling: 32.9M POLYX on pump days into memo-deposit address `2F8aak…` |
| `2F8aak…6wo4` | Exchange memo-deposit address (exchange not named) | 479 senders, 1,691 numeric memos (on-chain pattern) | high | yes (on-chain pattern) | Selling: on-chain proof that it is an exchange deposit |

## 📚 Sources

- [Tier A] Methodology update 16 Nov 2026: no new Arkham lookups; the attribution table uses evidence already cited in this report.
- [Tier A] Polymesh mainnet RPC (`mainnet-rpc.polymesh.network`): `Balances.TotalIssuance` at blocks 21,184,603 and 26,425,941; full `System.Account` scan (7,602 accounts, sum = issuance), 16 Nov 2026 ~5:40 AM MST
- [Tier A] Polymesh middleware indexer (`mainnet-graphql.polymesh.network`): identities `0x01…`–`0x05…`, account→identity links, `polyxTransactions` for all genesis-identity accounts, `2HXnHM…`, `2F8aak…`; fee, asset, instruction and extrinsic counts, 16 Nov 2026
- [Tier A] Polymesh Association [circulating-supply page source](https://raw.githubusercontent.com/PolymeshAssociation/PolymeshAssociation.github.io/main/circulating-supply/index.html) (address list)
- [Tier A] Polymesh docs: [fees](https://developers.polymesh.network/polyx/fees/) · [tokenomics](https://developers.polymesh.network/polyx/tokenomics/) · [governance](https://developers.polymesh.network/governance/) · [chain spec](https://github.com/PolymeshAssociation/Polymesh/blob/develop/src/chain_spec/mainnet_runtime.rs) · [8.1.3 blog](https://polymesh.network/blog/polymesh-8-1-3-mainnet-upgrade) · [tokenomics blog (2022)](https://polymesh.network/blog/understanding-polyx-tokenomics)
- [Tier A] SEC: [TruGolf 8-K Ex. 99.1 (18 Aug 2026)](https://www.sec.gov/Archives/edgar/data/1857086/000149315226038904/ex99-1.htm) · [8-K Ex. 10.4 (9 Oct 2026)](https://www.sec.gov/Archives/edgar/data/1857086/000149315226046435/ex10-4.htm); [Polymath closing announcement](https://www.polymath.network/articles/trugolf-completes-acquisition-of-polymath)
- [Tier B] [AnalytixInsight release on the Polymesh asset purchase (27 Jun 2025)](https://www.newsfilecorp.com/release/257215/AnalytixInsight-Inc.-Provides-Update-to-Reverse-Takeover-Transaction-with-Polymath-Research-Inc.)
- [Tier A] CoinGecko `polymesh` market data and tickers (16 Nov 2026 5:10 AM MST); Binance POLYX/USDT daily closes (from 17 Oct 2022)
- [Unverified] which exchange runs `2F8aak…`/`2CoSRa…`; who owns `2DzB6L…` and `2HXnHM…`; who controls the genesis identity #1 accounts after the 2025 sale; Polymesh Labs' full wallet list. **Not covered by Arkham:** Arkham does not support Polymesh (checked 16 Nov 2026)

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Association lists 7 wallets + treasury/rewards pots as its own | [supply page source](https://raw.githubusercontent.com/PolymeshAssociation/PolymeshAssociation.github.io/main/circulating-supply/index.html) · [`2FEWmT…`](https://polymesh.subscan.io/account/2FEWmTkH9czpKJSnnFxJhMaKHaM6H7k57PDSqJgqifwfBvLh) · [`2DbjUi…`](https://polymesh.subscan.io/account/2DbjUiD2vUgPaWyFgmNnbWXGBRS8QxG5yy71Vhd35WJePw6Y) | A | 16 Nov 2026 |
| Identity 1 = Polymesh genesis council seat | [chain spec](https://github.com/PolymeshAssociation/Polymesh/blob/develop/src/chain_spec/mainnet_runtime.rs) · [`2FTmkf…`](https://polymesh.subscan.io/account/2FTmkfcG6qxGWZ3MY5L9ctNyeJ6rauRfMEtknKTjXz1yom4q) | A · current owner [Unverified] | 16 Nov 2026 |
| 187.3M POLYX in 139 transfers into `2F8aak…`; 32.9M on pump days; 59.3M in last 12 months | [`2F8aak…`](https://polymesh.subscan.io/account/2F8aakkWMbuLqFD1Zc2q3Bss88TTbeazX2MEoCfeUMqk6wo4) · [24 Oct 2023](https://polymesh.subscan.io/block/10341720) · [25 Mar 2024](https://polymesh.subscan.io/block/12545731) · [22 Nov 2024](https://polymesh.subscan.io/extrinsic/16017779-1) · [12 Sep 2025](https://polymesh.subscan.io/extrinsic/20250342-1) · [15 Sep 2026](https://polymesh.subscan.io/extrinsic/25546196-1) | A chain · exchange [Unverified] | 16 Nov 2026 |
| `2F8aak…` is a memo deposit address sweeping to `2CoSRa…` | [`2F8aak…`](https://polymesh.subscan.io/account/2F8aakkWMbuLqFD1Zc2q3Bss88TTbeazX2MEoCfeUMqk6wo4) · [`2CoSRa…`](https://polymesh.subscan.io/account/2CoSRaWBjmxEWikG1FbzXe63G9DGayCpUnnVPkJu5V14roua) | A chain · name [Unverified] | 16 Nov 2026 |
| `2HXnHM…` got 52.5M from Association wallets in 2026 and sent 46.5M to `2F8aak…` | [`2HXnHM…`](https://polymesh.subscan.io/account/2HXnHMiy3nSCd12kJHaWpVirdqNDRnSSAQef8Mm76QrRHCup) · [26 Oct 2026](https://polymesh.subscan.io/extrinsic/26128344-1) | A chain · owner [Unverified] | 16 Nov 2026 |
| Fees 4,779.69 POLYX in 365 days; fees go to operators | indexer `TransactionFeePaid` sum · [docs](https://developers.polymesh.network/polyx/fees/) | A | 16 Nov 2026 |
| Supply +9.9% in 12 months; no max | RPC `TotalIssuance` at two blocks · [docs](https://developers.polymesh.network/polyx/tokenomics/) | A | 16 Nov 2026 |
| Polymath bought Association assets incl. POLYX (Jun 2025) | [AnalytixInsight release](https://www.newsfilecorp.com/release/257215/AnalytixInsight-Inc.-Provides-Update-to-Reverse-Takeover-Transaction-with-Polymath-Research-Inc.) | B | 16 Nov 2026 |
| TruGolf acquired Polymath; $4.2M revenue 2025; salary paid in POLYX | [8-K Ex. 99.1](https://www.sec.gov/Archives/edgar/data/1857086/000149315226038904/ex99-1.htm) · [8-K Ex. 10.4](https://www.sec.gov/Archives/edgar/data/1857086/000149315226046435/ex10-4.htm) · [Polymath](https://www.polymath.network/articles/trugolf-completes-acquisition-of-polymath) | A | 16 Nov 2026 |
| 28 new assets, 129 instructions, 186 asset transfers in 12 months | indexer counts from block 21,184,603 | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Which exchange runs `2F8aak…` / `2CoSRa…`?** And who owns `2DzB6L…` (38% of supply) and `2HXnHM…`? | Not covered by Arkham (no Polymesh support, checked 16 Nov 2026). Use Subscan labels and Polymesh identity (CDD) records; the numeric 9-digit memos also hint at the exchange's tag format | Free |
| 2 | **Who controls the genesis identity #1 and Association wallets after the 2025 sale?** | Read TruGolf's next 10-Q/10-K for digital-asset holdings; ask Polymath | Free |
| 3 | **Were the deposits sales, and were they disclosed?** | TruGolf / Polymath financial statements (digital-asset sales line) | Free |
| 4 | **Pre-runtime-v8 lots that have no extrinsic ID** | Confirm the block events on Subscan (`polymesh.subscan.io/block/…`, Events tab) | Free |
| 5 | **Exploit history** | Check Polymesh incident disclosures and rekt.news | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.

- Research only. Not investment advice.
