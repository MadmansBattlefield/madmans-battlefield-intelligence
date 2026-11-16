---
ticker: ICP
name: Internet Computer
chain: internet-computer
contract: "ICP ledger canister ryjl3-tyaaa-aaaaa-aaaba-cai"
overall_score: 4.3
overall_verdict: FAIL
section_scores:
  revenue: 2
  foundation_team: 5
  insider_holdings: 3
  selling_behavior: 4
  tokenomics_supply: 3
  liquidity_market: 6
  product_development: 8
  adoption_customers: 4
  security_audits: 6
  regulatory: 6
  catalysts: 5
gates_failed: [revenue]
red_lines:
  hack_exploit: "none found (liveness incidents only: subnet x4jtx stall 29 Oct 2026; ckBTC minter attack, no funds lost)"
  treasury_to_exchange_during_pump: "not proven (2021 genesis 'Treasury' 125013e9… deposited ~6.6M ICP into Coinbase deposit accounts on listing day 10 May 2021 and 15 Jun 2021; neither day is pump-testable / a pump day)"
  undisclosed_treasury_to_exchange_flow: "yes, 2021 (Arkham: 8.3M ICP Treasury -> exchanges; on-chain match verified; DFINITY publishes no wallet list)"
  treasury_descendant_pump_day_flow: "yes, to a distribution hub (11 Jun 2025 +22.6%: 1.4M ICP from Treasury-funded ecedd9b3… into hub 62dd3978…; 19 Nov 2024 +14.7%: 400k from 317aa76c…; hub owner [Unverified])"
  uncapped_inflation: "yes (supply ~469M at genesis -> 558.97M; voting rewards ~53k ICP/day vs ~$5k/day burned)"
price_usd: 2.22
price_source: "CoinGecko, 16 Nov 2026 5:26 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### ICP · Overall grade **4.3 / 10 · ❌ FAIL**

**Summary:** The Internet Computer is real, heavily built technology (42 subnets, 1.17M canisters, daily commits to `dfinity/ic`), but the token earns almost nothing: about **$1.9M a year** of cycles is burned while governance mints about **53,000 ICP a day** (~$43M a year). The genesis "Treasury" account that Arkham ties to DFINITY received **107,024,038 ICP** (≈ 22.8% of genesis) and put millions straight into Coinbase deposit accounts in 2021, and wallets it funded still feed a distribution hub, including on 2024–25 pump days. Revenue trips the hard gate.

**🚨 Top warning (red line):** The genesis account [`125013e9…8817`](https://dashboard.internetcomputer.org/account/125013e95bd5e008bd6d26f86f5ddda2b16c382372b3067672505c1f11418817) got the single largest genesis mint, **107,024,038 ICP** ([mint, block 9500](https://dashboard.internetcomputer.org/transaction/b7e3055193e55fa95dba3e11dddbad0c2e3649ea7a8be872c84cbe4ee571b1b9)). Arkham's June 2021 report calls it the **DFINITY "Treasury"** and says it deposited **8.3M ICP (~$2B) to exchanges**, with no vesting and no public wallet list ([Arkham report](https://info.arkm.com/researches/reports/icp-report); [Tier B]). The ledger matches Arkham's timestamps exactly: on listing day it sent ~1.94M to seven Coinbase deposit accounts ([12:02 UTC, 25k](https://dashboard.internetcomputer.org/transaction/81c712a5051f6af9c05ff47551f67cfb24cb19735d2040ed0220bb3764476e8d) · [13:06, 749,999](https://dashboard.internetcomputer.org/transaction/34040256783d27b234b4e31f0894ed9eb3189441056535f38353a3139d6909f9) · [16:10, 626,515](https://dashboard.internetcomputer.org/transaction/1af38109dc92ceee979e4c5acb8b5bf309717f2d22a14fdc999a445d5dcaff91)), and on 15 Jun 2021 it sent **4.7M** to deposit account [`54562ee0…6f65`](https://dashboard.internetcomputer.org/account/54562ee0de6b2bd80167593e8a73c52046584211092963bfb4f9d8521acd6f65) ([2M](https://dashboard.internetcomputer.org/transaction/6eca62a26d5ccb8a153e11e6fdb7eddfcbd25a708f82903d7274a75136283e49) · [2.7M](https://dashboard.internetcomputer.org/transaction/713844f34f7627ee3bcfc7be4a1fd24d24a48ad531db83704e776b6cd414367b)), which **swept both lots to high-volume hub accounts within one minute** ([sweep 1](https://dashboard.internetcomputer.org/transaction/fcc083f9ae00167fa6dc698c1bc68c4cdc7672dc818f67af26739920d9f03c99) · [sweep 2](https://dashboard.internetcomputer.org/transaction/e4588c4ac459b49e0d37f2e0be8be6d01e9a1800e22ae4d1d81f30175b09aa40)). A California appeals court opinion (30 Jan 2026) separately confirms DFINITY lent ICP to market makers Wintermute (702,000 ICP), GSR and Amber at launch. **Second warning:** Treasury-funded wallets moved **1.4M ICP into hub [`62dd3978…93f0`](https://dashboard.internetcomputer.org/account/62dd39780d34f2dc21eb680f99962659a6a0c2ccd9c68ec365962ae0eaf293f0) on the 11 Jun 2025 pump day (+22.6%)** ([first 50k](https://dashboard.internetcomputer.org/transaction/c08b7163df41fe68ae541176d3cc5fd3ca1264c03807ffd0e1fac921b8441163)); the hub's owner is [Unverified]. Every transfer is in the 🔗 Evidence trail below.

**Sections passed: 4 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 2/10 | ❌ FAIL |
| 🏛️ Foundation & team | 5/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 3/10 | ❌ FAIL |
| 📉 Selling behavior | 4/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 3/10 | ❌ FAIL |
| 💧 Liquidity & market | 6/10 | ✅ PASS |
| 🧑‍💻 Product & development | 8/10 | ✅ PASS |
| 🤝 Adoption & customers | 4/10 | ❌ FAIL |
| 🛡️ Security & audits | 6/10 | ✅ PASS |
| ⚖️ Regulatory | 6/10 | ✅ PASS |
| 📅 Catalysts & calendar | 5/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 ICP · Internet Computer · 4.3 / 10 · ❌ FAIL

> **One line:** Serious, actively shipped technology with almost no token revenue: ~$1.9M a year of cycles burned against ~19M ICP a year of new voting rewards, plus a 2021 genesis Treasury (107M ICP, Arkham: DFINITY) that sent millions straight into Coinbase deposit accounts and whose descendants still move coins on pump days.

| 📊 Market (CoinGecko, 16 Nov 2026 5:26 AM MST) | 🔗 On-chain (ICP ledger / NNS, 16 Nov 2026) |
|---|---|
| **Price** $2.22 | **Ledger** canister `ryjl3-tyaaa-aaaaa-aaaba-cai` ([IC dashboard](https://dashboard.internetcomputer.org/canister/ryjl3-tyaaa-aaaaa-aaaba-cai)) |
| **24h / 7d / 30d** 🔴 −2.4% / −5.9% / −25.8% · 1y −58.1% | **Total supply** 558,966,880 ICP (ledger API) · NNS `governance_total_supply_icp` 558,959,895 |
| **Market cap** $1.240B · **FDV** $1.240B (no max supply) | **Staked in neurons** 287.06M ICP (51.4%) · of which seed 71.41M, early contributors 12.62M |
| **24h volume** $33.3M | **Burned all-time** 3.01M ICP (`icp_burned_total`) |
| **ATH** $700.65 (10 May 2021) · now −99.7% | **Voting rewards** 53,104 ICP in the latest daily round · est. 1-yr reward rate 3.32% |
| **Pump days, last 365** 41 (cluster 13–17 Jan, 5–10 May, 5–9 Sep, 20–22 Sep 2026) | **Genesis Treasury** [`125013e9…8817`](https://dashboard.internetcomputer.org/account/125013e95bd5e008bd6d26f86f5ddda2b16c382372b3067672505c1f11418817): 107,024,038 in, 5.31 left, last tx 27 Jul 2021 |

---

## 💰 Revenue — Does it make money? · 2/10 · ❌ FAIL

| Metric | Value | Source |
|---|---:|---|
| Chain fees (cycles burned for compute/storage), 30d | **$167,664** | [Tier A] [DefiLlama fees, ICP chain](https://defillama.com/chain/ICP) (16 Nov 2026) |
| Chain fees, 1 year | **$1.93M** | same |
| Cycle burn rate, 15 Nov 2026 | 45.06B cycles/s ≈ 3,893 XDR/day ≈ **~$5.3k/day** | [Tier A] [IC API daily-stats](https://ic-api.internetcomputer.org/api/v3/daily-stats) (1T cycles = 1 XDR by protocol design) |
| ICP burned as ledger fees, all-time | 3,914 ICP (`icp_burned_fees`) | [Tier A] same |
| New ICP from voting rewards, latest daily round | **53,104 ICP (~$118k/day, ~$43M/yr)** | [Tier A] [IC API daily-stats](https://ic-api.internetcomputer.org/api/v3/daily-stats) `governance_latest_reward_round_total_available_e8s` |
| Revenue paid to holders | **None.** "ICP holders receive no dividend, no revenue share, and no treasury claim" | [Tier B] [Blockworks Token Transparency filing](https://blockworks.com/token-transparency/filing/internet-computer) |
| dApp revenue on ICP (30d) | ICPSwap $8.7k, WaterNeuron $2.4k, Liquidium $651 | [Tier A] [DefiLlama](https://defillama.com/chain/ICP) |

**What it means:** The only token "revenue" is the burn when developers pay for cycles: about $1.9M a year on a $1.24B network. Governance mints roughly 20× that in new ICP each year as voting rewards, before node-provider rewards. So burn does not offset dilution and nothing flows to an unstaked holder. Score **2**, which **trips the Revenue gate**.

## 🏛️ Foundation & team — Who is in charge? · 5/10 · ❌ FAIL

| Item | Finding | Source |
|---|---|---|
| Lead entity | **DFINITY Stiftung** (DFINITY Foundation), Swiss not-for-profit foundation, incorporated Oct 2016. Founder and chief scientist Dominic Williams | [Tier B] [Blockworks filing](https://blockworks.com/token-transparency/filing/internet-computer) · [DFINITY](https://dfinity.org/investors) |
| US affiliate | Dfinity USA Research LLC (named defendant in US class actions) | [Tier A] [N.D. Cal. complaint 3:21-cv-06118](https://storage.courtlistener.com/recap/gov.uscourts.cand.383070/gov.uscourts.cand.383070.1.0.pdf) |
| Powers | Foundation says it has "no veto, no pause power, and no unilateral spending power over the NNS"; it votes like any neuron and is a registered node provider | [Tier B] Blockworks filing |
| Funding | "Funds itself from its genesis endowment and from the node provider rewards"; it "divests that allocation over time" | [Tier B] Blockworks filing · [Tier A] [DFINITY governance post, Jun 2021](https://medium.com/dfinity/the-community-led-governance-of-the-internet-computer-b863cd2975ba) |
| Published financials | No audited accounts or treasury report found this pass | Not found |
| Published wallet list | **None.** DFINITY does not publish its ledger accounts or neuron IDs (only known neuron 27) | [Tier A] [IC API neuron 27](https://ic-api.internetcomputer.org/api/v3/neurons/27) |

**What it means:** A known foundation and founder with a long research record. But no audited accounts, no treasury report and no wallet list, so outsiders cannot see what the largest holder does with its coins.

## 🪙 Foundation / team holdings — How many coins do they hold? · 3/10 · ❌ FAIL

| Bucket | ICP | Notes |
|---|---:|---|
| Planned genesis share: "Foundation Endowment, Team and Partnership" | **52.93%** of genesis | [Tier A] [DFINITY presale post, 4 Apr 2018](https://medium.com/dfinity/announcing-the-dfinity-presale-fundraise-and-public-airdrop-cdea19892ef6) |
| Allocation per US class-action complaint | Foundation "nearly 25%", team 18%, advisors 2.4%, Internet Computer Association 4% | [Tier A as a filing / allegation only] [complaint](https://storage.courtlistener.com/recap/gov.uscourts.cand.383070/gov.uscourts.cand.383070.1.0.pdf) |
| Genesis "Treasury" [`125013e9…8817`](https://dashboard.internetcomputer.org/account/125013e95bd5e008bd6d26f86f5ddda2b16c382372b3067672505c1f11418817) | **107,024,038** at genesis (≈ 22.8% of ~469M) | Largest single genesis mint ([block 9500](https://dashboard.internetcomputer.org/transaction/b7e3055193e55fa95dba3e11dddbad0c2e3649ea7a8be872c84cbe4ee571b1b9)); Arkham: "the key address we believe belongs to Dfinity" [Tier B]. Emptied by 27 Jul 2021 (5.31 ICP left) |
| Treasury → [`52757335…c99f`](https://dashboard.internetcomputer.org/account/52757335752ff4029c423aaf2b820462c165ef38d77df9dde49745536e47c99f) | 50,271,451.72 | 11 Jun 2021 ([tx](https://dashboard.internetcomputer.org/transaction/6069d81f330bc7bbab74d5dfde125e3ff179c19531f6d0b165d95f110d0a65de)); split into 2M accounts on 30 Jun 2021, e.g. [→ `ecedd9b3…`](https://dashboard.internetcomputer.org/transaction/ed46ff948c922def3d191c37dc4a0fb9d49893e218eeb2105e8c8073ef39d367) |
| Treasury → ten 1M accounts | 10,000,000 | 30 Jun 2021, e.g. [→ `b9367b1c…`](https://dashboard.internetcomputer.org/transaction/36678e7d67b233616fd8d4eb2331ed7eb3a5929aa30702b0f59fdb610aa0e7aa), [→ `317aa76c…`](https://dashboard.internetcomputer.org/transaction/2daba69b6e49d258dd9bdac73a256758ca5f3d82d107b992f38734f798ec07d3) |
| What DFINITY holds today | **Not disclosed.** Staked neurons are not ledger accounts, and DFINITY publishes neither | Not found |

**What it means:** DFINITY's own 2018 plan gave the foundation, team and partners over half of genesis, and the biggest single genesis account (107M) was emptied within 11 weeks into exchanges, market makers and sub-wallets. Arkham said the foundation's tokens had no vesting, while seed donors got a 4-year neuron schedule. Today's holdings are invisible. Score **3**.

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL

**A. 2021: Treasury straight into exchange deposit accounts (Arkham's "Treasury")**

| Day (UTC) | Route | ICP | Close / 5-day change (Coinbase ICP-USD) | Pump? |
|---|---|---:|---:|---|
| 10 May 2021 (listing) | Treasury → 7 deposit accounts Arkham calls Coinbase: [`7b8c0a10…`](https://dashboard.internetcomputer.org/account/7b8c0a103851d344b09f278fd52533b16a887f7d3a8cd0c20f999fbfbf262056) 25k+75k ([tx](https://dashboard.internetcomputer.org/transaction/81c712a5051f6af9c05ff47551f67cfb24cb19735d2040ed0220bb3764476e8d)) · `0032a91f…` 25k · `cb749bf3…` 120k+80k · [`05ad4746…`](https://dashboard.internetcomputer.org/account/05ad474665f1eec0714c1a4ec941c3a395c703e14bb43100bd946d80b87828af) 749,999 ([tx](https://dashboard.internetcomputer.org/transaction/34040256783d27b234b4e31f0894ed9eb3189441056535f38353a3139d6909f9)) · `27d17170…` 200k · `00504a7e…` 40k · [`000a1f04…`](https://dashboard.internetcomputer.org/account/000a1f0436e925af8ae9ca45786f0ae85bd66f357fb0d19c9d3320e180710cf1) 626,515 ([tx](https://dashboard.internetcomputer.org/transaction/1af38109dc92ceee979e4c5acb8b5bf309717f2d22a14fdc999a445d5dcaff91)) | **1,941,514** | $426.98 / n/a (first day) | Not testable |
| 15 Jun 2021 | Treasury → deposit [`54562ee0…`](https://dashboard.internetcomputer.org/account/54562ee0de6b2bd80167593e8a73c52046584211092963bfb4f9d8521acd6f65) ([2M](https://dashboard.internetcomputer.org/transaction/6eca62a26d5ccb8a153e11e6fdb7eddfcbd25a708f82903d7274a75136283e49) · [2.7M](https://dashboard.internetcomputer.org/transaction/713844f34f7627ee3bcfc7be4a1fd24d24a48ad531db83704e776b6cd414367b)), swept within 1 minute to hubs [`a6ed987d…`](https://dashboard.internetcomputer.org/account/a6ed987d89796f921c8a49d275ec7c9aa04e75a8fc8cd2dbaa5da799f0215ab0) (31,211 txs) and [`660b1680…`](https://dashboard.internetcomputer.org/account/660b1680dafeedaa68c1f1f4cf8af42ed1dfb8564646efe935a2b9a48528b605) (26,781 txs) | **4,700,000** | $60.40 / −9.2% | No |

- The listing-day times and sizes match Arkham's published list line for line (25k at 12:02 to "address 1", 750k at 13:06, 627k at 16:10, etc.). Arkham's totals: **Treasury 8.3M ICP to exchanges; another 10.7M from 34 Treasury-linked "suspected insiders"** ([report](https://info.arkm.com/researches/reports/icp-report)). Arkham's labels are [Tier B]; the transfers themselves are [Tier A] ledger reads.
- **Court record:** the California Court of Appeal (Ocampo v. Dfinity Stiftung, A173226, 30 Jan 2026) describes DFINITY's **"loan" of 702,000 ICP to Wintermute** for market making, plus GSR and Amber agreements and a Coinbase Custody account ([opinion text](https://gno.law/c/10781904/ocampo-v-stiftung-ca13) · [Leagle](https://www.leagle.com/decision/incaco20260130026)). So part of the listing-day flow was liquidity provision. DFINITY's own June 2021 post says the foundation "did NOT sell ICP tokens from its endowment at or soon after Genesis launch" ([post](https://medium.com/dfinity/the-community-led-governance-of-the-internet-computer-b863cd2975ba)); the 15 Jun 4.7M deposit is not explained there.
- Pump days in 2021: on **24 May 2021 (+20.5%)** the Treasury sent 2.5M to [`55f4f3e3…`](https://dashboard.internetcomputer.org/account/55f4f3e37d7792a15dcfe9447d33a004a6d23bbb2bc9990a168cca15e3291861) ([tx](https://dashboard.internetcomputer.org/transaction/2f70c7783a75ed822ab3f6b6ab12fd1eb790fdad2fb9f83c7f9bf41da0821650)), which paid it out in 250k and smaller lots (not proven to be exchanges). On **30 Jun 2021 (+60.1%)** the Treasury and `52757335…` split ~62M into 1M and 2M sub-accounts (internal moves).

**B. Treasury descendants into hub `62dd3978…` (2024–2025)**

| Day (UTC) | From (Treasury-funded) | ICP | 5-day change (Coinbase) | Pump? |
|---|---|---:|---:|---|
| 19 Nov 2024 | [`317aa76c…`](https://dashboard.internetcomputer.org/account/317aa76cbee675c0cd55bcb9e966822c115a2ac16bc47a34ee6d0252000cfbfb) 8 × 50k ([first](https://dashboard.internetcomputer.org/transaction/0e21927eab78485e71136edaf725be940c4863b2982ddcfd5583161daf28013a)) | 400,000 | +14.7% | 🔴 Yes |
| 3 Feb 2025 | `52757335…` ([e.g.](https://dashboard.internetcomputer.org/transaction/fa96e36b4044fc2a33330f2cda8b274b6848b831c039f80db6de47be7765d4e1)), `b9367b1c…`, `b4d32ac4…`, `e6e28ecb…`, `406cc369…` | ~3.4M | −10.9% | No |
| 11 Jun 2025 | [`ecedd9b3…`](https://dashboard.internetcomputer.org/account/ecedd9b3595d88667b78315da6af8e0de29164ef718f96930e0459017d5d8a04) 28 × 50k ([first](https://dashboard.internetcomputer.org/transaction/c08b7163df41fe68ae541176d3cc5fd3ca1264c03807ffd0e1fac921b8441163)) | 1,399,998 | +22.6% | 🔴 Yes |

- In total **~7.04M ICP in 145 transfers** went from Treasury-funded accounts into [`62dd3978…93f0`](https://dashboard.internetcomputer.org/account/62dd39780d34f2dc21eb680f99962659a6a0c2ccd9c68ec365962ae0eaf293f0) between Nov 2024 and Jun 2025. The hub has 10,898 transactions, 1,180 senders and 746 recipients, and it pays out fixed-size amounts (e.g. 2,665.25 and 1,594.73 ICP) to hundreds of accounts within minutes. That looks like a **payroll / grant-distribution account**, not an exchange deposit. Owner [Unverified].
- **Last 12 months (from 16 Nov 2025):** across the 85 accounts that received ≥ 50k ICP straight from the Treasury or `52757335…`, the only large direct move was 989,411 ICP from [`ea48b23b…`](https://dashboard.internetcomputer.org/account/ea48b23b9893a92ab26e63a36a0da680e5abba580bcf30acfc94e1f19764a076) to fresh [`fa831ac5…`](https://dashboard.internetcomputer.org/account/fa831ac580bbca15e7ff0547198093d4cf9b6a80323959f3294749b537ae3c26) on 10 Dec 2025 ([tx](https://dashboard.internetcomputer.org/transaction/7776d6c548cd51d94ce7cf8362c52ddbc3e7046d8076add81d2dafe47e2fc965)), not a pump day; it is still held. No direct Treasury-branch deposit into an exchange account was found on a 2025–26 pump day.

**What it means:** The 2021 record is bad: the biggest genesis account (Arkham: DFINITY) put ~6.6M ICP straight into Coinbase deposit accounts within five weeks of launch, with no wallet disclosure and despite DFINITY saying the endowment did not sell. But neither big deposit day was a measurable pump day, and part of the flow was market-maker liquidity confirmed in court. Recent pump-day moves go into a distribution hub, not an exchange. Score **4**: not the gate, but a fail.

## 📊 Tokenomics & supply · 3/10 · ❌ FAIL

- **No supply cap.** Genesis minted "close to 470 million" ICP ([Blockworks](https://blockworks.com/token-transparency/filing/internet-computer)); supply today is **558.97M**, about **+19%** in 5.5 years, after 3.01M burned ([IC API](https://ic-api.internetcomputer.org/api/v3/daily-stats)).
- **Two mint streams:** neuron voting rewards (latest daily round 53,104 ICP) and node-provider rewards (paid monthly; not measured this pass).
- **Lock-up:** 287.06M ICP (51.4%) sits in neurons. 71.41M is still in seed neurons and 12.62M in early-contributor neurons, of which about 1.52M seed ICP is dissolving with under 6 months left ([IC API governance metrics](https://ic-api.internetcomputer.org/api/v3/governance-metrics)).
- **Deflation needs ~20× more cycle burn** than today to offset voting rewards alone.

## 💧 Liquidity & market · 6/10 · ✅ PASS

- $33.3M 24h volume on a $1.24B cap (≈ 2.7% turnover). Listed on Coinbase, Binance and other majors.
- Down 58% in a year and 99.7% from the 2021 high. 41 pump days in the last 365, mostly short squeezes (peak +54.5% on 8 May 2026).
- DeFi depth on-chain is thin: ICP chain TVL ~$7.4M ([DefiLlama](https://defillama.com/chain/ICP)).

## 🧑‍💻 Product & development · 8/10 · ✅ PASS

- `dfinity/ic` last commit 16 Nov 2026 3:50 AM MST (public, open source). The network runs 42 subnets, 2,878 nodes from 102 node providers, 1.17M canisters and ~9,100 transactions a second on average ([IC API daily-stats](https://ic-api.internetcomputer.org/api/v3/daily-stats)).
- Chain-key assets are live: ckBTC supply 226.6 BTC, ckETH 527.0 ETH (same source).

## 🤝 Adoption & customers · 4/10 · ❌ FAIL

- 3.34M Internet Identity users, but only **2,837 daily logins** and **4,164 unique ledger accounts a day** (15 Nov 2026).
- Paid usage is small: ~$1.9M a year of cycles. Named enterprise customers confirmed by both sides were not found this pass.

## 🛡️ Security & audits · 6/10 · ✅ PASS

- No protocol-level theft found. Recent incidents were liveness only: subnet `x4jtx` stalled during an upgrade on 29 Oct 2026 and was recovered via [NNS proposal 144648](https://internetcomputer.news/governance/nns/proposals/144648) in ~1h; a 2026 attack on the ckBTC minter led to an NNS upgrade with ~1h downtime and no funds lost ([report](https://theswop.app/news/attack-on-ckbtc-infrastructure-on-icp), [Unverified] single outlet).
- An open researcher write-up describes an ingress-pool quota flaw that lets one sender purge HTTP ingress on a replica (DoS, no fund loss) ([NullRabbit](https://nullrabbit.ai/research/ic-ingress-pool-quota-miskey-purge), [Unverified]).
- The NNS can upgrade any system canister, including the ledger. That is governance-controlled, not a single key, but most voting power follows a few neurons.

## ⚖️ Regulatory · 6/10 · ✅ PASS

- **Valenti v. Dfinity USA Research** (N.D. Cal. 3:21-cv-06118, securities class action): dismissed 9 Apr 2025 after plaintiffs declined to amend; appeal to the Ninth Circuit filed 7 May 2025, pending ([docket](https://www.drdocket.com/case/valenti-v-dfinity-usa-research-llc-cand-2021)).
- **Ocampo v. Dfinity Stiftung** (state court): summary judgment for DFINITY, **affirmed 30 Jan 2026** ([opinion](https://gno.law/c/10781904/ocampo-v-stiftung-ca13)).
- No SEC or other regulator action against ICP found.

## 📅 Catalysts & calendar · 5/10 · ❌ FAIL

| Date | Event |
|---|---|
| Pending | Ninth Circuit appeal in Valenti v. Dfinity |
| Ongoing | Seed/early-contributor neurons keep dissolving (~1.52M seed ICP with under 6 months left) |
| Ongoing | Monthly node-provider rewards and daily voting rewards (new supply) |
| Any time | NNS upgrades; DFINITY product launches (no dated token-relevant milestone found) |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None with fund loss found; liveness incidents only |
| Treasury → exchange during a pump | 🟡 Not proven: 2021 Treasury deposits were on listing day (not testable) and 15 Jun 2021 (−9.2%). [15 Jun 2M](https://dashboard.internetcomputer.org/transaction/6eca62a26d5ccb8a153e11e6fdb7eddfcbd25a708f82903d7274a75136283e49) · [sweep](https://dashboard.internetcomputer.org/transaction/fcc083f9ae00167fa6dc698c1bc68c4cdc7672dc818f67af26739920d9f03c99) |
| Undisclosed treasury → exchange flow | 🔴 Yes (2021): ~6.6M verified on the ledger into Coinbase deposit accounts; 8.3M per Arkham. [Treasury account](https://dashboard.internetcomputer.org/account/125013e95bd5e008bd6d26f86f5ddda2b16c382372b3067672505c1f11418817) |
| Treasury-branch pump-day flow | 🟡 19 Nov 2024 and 11 Jun 2025 into distribution hub `62dd3978…` (owner [Unverified]). [11 Jun 2025](https://dashboard.internetcomputer.org/transaction/c08b7163df41fe68ae541176d3cc5fd3ca1264c03807ffd0e1fac921b8441163) |
| Uncapped inflation | 🔴 Yes: ~469M → 558.97M; voting rewards ≈ 20× cycle burn |

## 📚 Sources

- [Tier A] ICP ledger API (`ledger-api.internetcomputer.org`): genesis mints, full history of the Treasury, `52757335…`, `54562ee0…`, `62dd3978…` and the 85 accounts the Treasury branch funded with ≥ 50k ICP; read 16 Nov 2026 MST
- [Tier A] IC API (`ic-api.internetcomputer.org`): `daily-stats` (15 Nov 2026), `governance-metrics`, neuron 27, cycle burn rate; read 16 Nov 2026 MST
- [Tier A] [IC dashboard](https://dashboard.internetcomputer.org) account and transaction pages (links throughout)
- [Tier A] DefiLlama ICP chain fees and revenue, 16 Nov 2026
- [Tier A] CoinGecko `internet-computer` price and 365-day closes (16 Nov 2026 5:26 AM MST); Coinbase Exchange ICP-USD daily candles for 2021 and 2024–25 pump tests
- [Tier A] [DFINITY presale post (2018)](https://medium.com/dfinity/announcing-the-dfinity-presale-fundraise-and-public-airdrop-cdea19892ef6) · [DFINITY governance post (Jun 2021)](https://medium.com/dfinity/the-community-led-governance-of-the-internet-computer-b863cd2975ba) · [seed access post](https://medium.com/dfinity/how-to-access-seed-and-airdrop-icp-tokens-and-participate-in-the-internet-computer-network-e6cd663a0c3c)
- [Tier A] Court records: [N.D. Cal. complaint](https://storage.courtlistener.com/recap/gov.uscourts.cand.383070/gov.uscourts.cand.383070.1.0.pdf) (allegations) · [Valenti docket](https://www.drdocket.com/case/valenti-v-dfinity-usa-research-llc-cand-2021) · [Ocampo opinion](https://gno.law/c/10781904/ocampo-v-stiftung-ca13) · [Leagle copy](https://www.leagle.com/decision/incaco20260130026)
- [Tier B] [Arkham ICP report, 28 Jun 2021](https://info.arkm.com/researches/reports/icp-report) (Treasury and Coinbase deposit attribution)
- [Tier B] [Blockworks Token Transparency filing (14 Aug 2026)](https://blockworks.com/token-transparency/filing/internet-computer)
- [Tier B] [ICN proposal 144648](https://internetcomputer.news/governance/nns/proposals/144648) · [PulsAPI status](https://www.pulsapi.com/services/internetcomputer) · [The Swop](https://theswop.app/news/attack-on-ckbtc-infrastructure-on-icp) · [NullRabbit](https://nullrabbit.ai/research/ic-ingress-pool-quota-miskey-purge)
- [Unverified] that the Treasury account is DFINITY's (one Tier B source plus size match); owner of hub `62dd3978…`; Coinbase ownership of the hub accounts `a6ed987d…`/`660b1680…`; current DFINITY holdings; node-provider mint totals

## 🔗 Evidence trail

*Every link below opens the primary record (IC dashboard, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Treasury got the largest genesis mint, 107,024,038 ICP | [mint block 9500](https://dashboard.internetcomputer.org/transaction/b7e3055193e55fa95dba3e11dddbad0c2e3649ea7a8be872c84cbe4ee571b1b9) · [account](https://dashboard.internetcomputer.org/account/125013e95bd5e008bd6d26f86f5ddda2b16c382372b3067672505c1f11418817) | A | 16 Nov 2026 |
| Arkham attributes the account to DFINITY and counts 8.3M to exchanges | [Arkham report](https://info.arkm.com/researches/reports/icp-report) | B | 16 Nov 2026 |
| Listing day: ~1.94M to seven Coinbase deposit accounts (times match Arkham) | [12:02 25k](https://dashboard.internetcomputer.org/transaction/81c712a5051f6af9c05ff47551f67cfb24cb19735d2040ed0220bb3764476e8d) · [13:06 749,999](https://dashboard.internetcomputer.org/transaction/34040256783d27b234b4e31f0894ed9eb3189441056535f38353a3139d6909f9) · [16:10 626,515](https://dashboard.internetcomputer.org/transaction/1af38109dc92ceee979e4c5acb8b5bf309717f2d22a14fdc999a445d5dcaff91) | A chain + B label | 16 Nov 2026 |
| 15 Jun 2021: 4.7M into deposit `54562ee0…`, swept in 1 minute | [2M in](https://dashboard.internetcomputer.org/transaction/6eca62a26d5ccb8a153e11e6fdb7eddfcbd25a708f82903d7274a75136283e49) · [sweep](https://dashboard.internetcomputer.org/transaction/fcc083f9ae00167fa6dc698c1bc68c4cdc7672dc818f67af26739920d9f03c99) · [2.7M in](https://dashboard.internetcomputer.org/transaction/713844f34f7627ee3bcfc7be4a1fd24d24a48ad531db83704e776b6cd414367b) · [sweep](https://dashboard.internetcomputer.org/transaction/e4588c4ac459b49e0d37f2e0be8be6d01e9a1800e22ae4d1d81f30175b09aa40) | A | 16 Nov 2026 |
| Treasury → `52757335…` 50.27M; split into 2M accounts | [50.27M](https://dashboard.internetcomputer.org/transaction/6069d81f330bc7bbab74d5dfde125e3ff179c19531f6d0b165d95f110d0a65de) · [2M → ecedd9b3](https://dashboard.internetcomputer.org/transaction/ed46ff948c922def3d191c37dc4a0fb9d49893e218eeb2105e8c8073ef39d367) | A | 16 Nov 2026 |
| 24 May 2021 pump day: Treasury → `55f4f3e3…` 2.5M | [tx](https://dashboard.internetcomputer.org/transaction/2f70c7783a75ed822ab3f6b6ab12fd1eb790fdad2fb9f83c7f9bf41da0821650) | A | 16 Nov 2026 |
| 19 Nov 2024 and 11 Jun 2025 pump days: Treasury-funded wallets → hub `62dd3978…` | [317aa76c funded](https://dashboard.internetcomputer.org/transaction/2daba69b6e49d258dd9bdac73a256758ca5f3d82d107b992f38734f798ec07d3) · [19 Nov 2024](https://dashboard.internetcomputer.org/transaction/0e21927eab78485e71136edaf725be940c4863b2982ddcfd5583161daf28013a) · [11 Jun 2025](https://dashboard.internetcomputer.org/transaction/c08b7163df41fe68ae541176d3cc5fd3ca1264c03807ffd0e1fac921b8441163) · [hub](https://dashboard.internetcomputer.org/account/62dd39780d34f2dc21eb680f99962659a6a0c2ccd9c68ec365962ae0eaf293f0) | A chain · owner [Unverified] | 16 Nov 2026 |
| 10 Dec 2025: 989,411 from Treasury-funded `ea48b23b…` to fresh wallet | [funding 2021](https://dashboard.internetcomputer.org/transaction/2a7e13d93220273bf1ed11730a586143b18727dfa5ae0711ac54a4cce8b3265c) · [tx](https://dashboard.internetcomputer.org/transaction/7776d6c548cd51d94ce7cf8362c52ddbc3e7046d8076add81d2dafe47e2fc965) | A | 16 Nov 2026 |
| DFINITY lent 702,000 ICP to Wintermute; GSR, Amber and Coinbase Custody agreements | [Ocampo opinion](https://gno.law/c/10781904/ocampo-v-stiftung-ca13) | A (court) | 16 Nov 2026 |
| Supply 558.97M, staked 287.06M, burned 3.01M, voting rewards 53,104/day, burn 45.06B cycles/s | [daily-stats](https://ic-api.internetcomputer.org/api/v3/daily-stats) · [governance-metrics](https://ic-api.internetcomputer.org/api/v3/governance-metrics) | A | 16 Nov 2026 |
| Chain fees $167,664 (30d), $1.93M (1y) | [DefiLlama ICP](https://defillama.com/chain/ICP) | A | 16 Nov 2026 |
| Genesis plan: 52.93% foundation, team and partners | [DFINITY 2018 post](https://medium.com/dfinity/announcing-the-dfinity-presale-fundraise-and-public-airdrop-cdea19892ef6) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Labels for the unlabelled ICP accounts** (the maintainer's `arkham/icp_addresses.csv` list: Treasury, `52757335…`, hub `62dd3978…`, the Coinbase deposit/hub accounts, top holders) | **Not covered by Arkham's explorer:** Arkham does not support ICP address pages (checked 16 Nov 2026); its 2021 published ICP report above is the only Arkham source. Use the ICP dashboard's known-account names, or ask DFINITY to publish its wallet list | Free |
| 2 | **Who runs hub `62dd3978…`?** | Ask DFINITY whether it is its grant/payroll distributor; check whether its recipients deposit to exchanges | Free |
| 3 | **What does DFINITY hold now?** | Ask DFINITY for its neuron IDs and ledger accounts; watch for a treasury report | Free |
| 4 | **Why the 4.7M Coinbase deposit on 15 Jun 2021?** | Compare with DFINITY's statement that the endowment did not sell; read the Coinbase Custody terms in the Ocampo record | Free |
| 5 | **Node-provider mint per month** | Sum node-provider reward mints from the ledger for the last 12 months | Free |
| 6 | **Ninth Circuit appeal (Valenti)** | Watch the docket | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
