---
ticker: RLC
name: iExec RLC
chain: ethereum
contract: "0x607f4c5bb672230e8672085532f7e901544a7375"
overall_score: 4.3
overall_verdict: FAIL
section_scores:
  revenue: 2
  foundation_team: 5
  insider_holdings: 5
  selling_behavior: 3
  tokenomics_supply: 8
  liquidity_market: 4
  product_development: 6
  adoption_customers: 3
  security_audits: 6
  regulatory: 6
  catalysts: 5
gates_failed: [revenue, selling_behavior]
red_lines:
  hack_exploit: "none found"
  mint_path_live: "no: fixed 87M supply, no mint function"
  team_wallet_to_exchange_during_pump: "yes: a 2-signature Safe funded by the Arkham-labelled iExec Team wallet sent 651,000 RLC to a Binance deposit address on 9-10 Oct 2026, during a +183.9% pump; no disclosure found"
  entity_concentration: "two Safes hold 18.25M RLC (21.0%); not on the project's published address list"
price_usd: 0.3376
price_source: "CoinGecko, 16 Nov 2026 ~9:00 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### RLC · Overall grade **4.3 / 10 · ❌ FAIL**

**Summary:** iExec has run a confidential-computing (TEE) marketplace since 2017. RLC pays for tasks and is staked as collateral. Supply is fixed at 87M with nothing left to unlock, which is the token's strength. The protocol publishes no fees or revenue, and its buyback "from protocol revenue" is still a plan tied to a new product that was on testnet, so the revenue gate fails. The selling gate also fails: during the unexplained **+184% spike of 9 Oct 2026**, a Safe linked to the project's original distribution wallets deposited RLC to Binance.

**🚨 Top warning:** pump-day exchange deposits from a project-linked Safe. Safe [0xc0e3…0afb](https://etherscan.io/address/0xc0e364408bcb86dad77dfa0db043c536d9b50afb) holds 10.5M RLC (12.1%). On **9 Oct 2026**, when RLC closed 183.9% above five days earlier, it sent **151,000 RLC** to a Binance deposit address ([tx](https://etherscan.io/tx/0x723e1d3dcf4c86acde1df6f385cedf6ef1221f87680ed363819df02efe5a106a)). It sent another **500,000 RLC** the next day (+32.3%) ([tx](https://etherscan.io/tx/0xd9194f6de2860fde0fa01c8cb4212d2277981d133bfa55bdf76aa9137a7fb559)), about **$637k** in total. The Safe was funded in 2025 by wallets that received their RLC in the April 2017 token distribution, plus withdrawals from Binance. The project hasn't published these addresses, so ownership is [Unverified]. Every link is in the 🔗 Evidence trail below.

**Sections passed: 4 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 2/10 | ❌ FAIL (hard gate) |
| 🏛️ Foundation & team | 5/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 5/10 | ❌ FAIL |
| 📉 Selling behavior | 3/10 | ❌ FAIL (hard gate) |
| 📊 Tokenomics & supply | 8/10 | ✅ PASS |
| 💧 Liquidity & market | 4/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 6/10 | ✅ PASS |
| 🤝 Adoption & customers | 3/10 | ❌ FAIL |
| 🛡️ Security & audits | 6/10 | ✅ PASS |
| ⚖️ Regulatory | 6/10 | ✅ PASS |
| 📅 Catalysts & calendar | 5/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 RLC · iExec RLC · 4.3 / 10 · ❌ FAIL

> **One line:** Clean fixed supply, but no revenue, and a project-linked Safe selling into an unexplained spike.

| 📊 Market (CoinGecko, 16 Nov 2026 ~9:00 AM MST) | 🔗 On-chain ([Etherscan](https://etherscan.io/token/0x607f4c5bb672230e8672085532f7e901544a7375), 16 Nov 2026 ~9:10 AM MST) |
|---|---|
| **Price** $0.3376 | **Supply** 86,999,785 RLC (no mint; ~215 burned) |
| **24h / 7d / 30d** 🔴 −1.4% / −19.7% / −56.6% | **Circulating** 87.0M (100%) |
| **Market cap** $29.4M · **FDV** $29.4M | **Safe 0xc0e3 (2 signatures)** 10.50M (12.1%) |
| **24h volume** $2.60M (BloFin $0.43M, BtcTurk $0.34M, Binance $0.32M, Pionex $0.25M, WhiteBIT $0.21M) | **Safe 0xa59b (2 signatures)** 7.75M (8.9%) |
| **ATH** $15.51 (10 May 2021) · now −97.8% | **Unlocks** none pending (docs) |
| **Pump days** 24 in the last year (largest +183.9% on 9 Oct 2026) | |

---

## 💰 Revenue — Does it make money? · 2/10 · ❌ FAIL (hard gate)

- Task payments go to app, data and worker providers, not to the protocol ([RLC docs](https://docs.iex.ec/get-started/overview/rlc)). DefiLlama has no fee record. Buybacks funded from revenue are proposed for the new confidential-DeFi product but not live. **2 → hard-gate FAIL.**

## 🏛️ Foundation & team — Who is in charge? · 5/10 · ❌ FAIL

- A company-led project since 2017 that describes itself as self-funded, with no VC rounds (docs). Leaders are described by role only. Treasury addresses are not all published.

## 🪙 Foundation / team holdings — How many coins do they hold? · 5/10 · ❌ FAIL

| Safe | RLC | % | Funding |
|---|---:|---:|---|
| [0xc0e3…0afb](https://etherscan.io/address/0xc0e364408bcb86dad77dfa0db043c536d9b50afb) | 10,495,721 | 12.1% | 6.80M from [0xd653…3298](https://intel.arkm.com/explorer/address/0xd65380d773208a6aa49472bf55186b855b393298), the Arkham-labelled **iExec: Team** wallet (got 15M from the distribution source in Apr 2017); 1.82M withdrawn from Binance in Jun 2025 |
| [0xa59b…8d10](https://etherscan.io/address/0xa59b56a167138ab567b44bb0f438c4c1f9748d10) | 7,753,295 | 8.9% | 4.88M from 0x24f6…5d48 (got 6M from the same source in Apr 2017); 2.45M withdrawn from Binance in Dec 2025 |

- Both are 2-signature Safes. 0xc0e3 was first funded in Jun 2025, and 0xa59b in Sep 2025. They are not on the project's important-addresses page, and Arkham ([Tier B] Arkham, read 16 Nov 2026 (signed-in account)) labels both only as Gnosis Safes. But [0xc0e3](https://intel.arkm.com/explorer/address/0xc0e364408bcb86dad77dfa0db043c536d9b50afb) was **funded by the Arkham-labelled iExec Team wallet** (2.799M, 2M and 2M RLC), and [0xa59b](https://intel.arkm.com/explorer/address/0xa59b56a167138ab567b44bb0f438c4c1f9748d10) shares a funder (`0x24f6…5d48`) with it. 0xc0e3 also received RLC from Keyrock, a market maker, and from a wallet Arkham labels with an individual's name (not given here). Which signers control the Safes is still [Unverified].

## 📉 Selling behavior — Do insiders sell into pumps? · 3/10 · ❌ FAIL (hard gate)

| Date | From | To | RLC | Close | ≈ USD | Pump? | Tx |
|---|---|---|---:|---:|---:|---|---|
| 26 Aug 2025 | 0xc0e3 | Binance Deposit 0x38e9 | 2,454,395 | $1.031 | n/a: same amount withdrawn to Safe 0xa59b on 22 Dec 2025 (round trip) | No | [0x9dae…](https://etherscan.io/tx/0x9daefc62db6b90d7273effc91607251774936f3dd564dde72d6d577729a1d231) |
| 4 Aug 2026 | 0xa59b | Binance Deposit 0x57c4 | 500,000 | $0.2593 | $130k | No | [0x961f…](https://etherscan.io/tx/0x961f11295cf4635b4894c6e35128ab85e2fb6cc657ec24dc951bb4a32ba8ffa0) |
| 9 Oct 2026 | 0xc0e3 | Binance Deposit 0x4035 | 151,000 | $1.0346 | $156k | **Yes, +183.9%** | [0x723e…](https://etherscan.io/tx/0x723e1d3dcf4c86acde1df6f385cedf6ef1221f87680ed363819df02efe5a106a), [0x6098…](https://etherscan.io/tx/0x6098348b05edc8772f13d04054ecc9f2a47c6fa01ef32b4029109dd51dbe4501) |
| 10 Oct 2026 | 0xc0e3 | Binance Deposit 0x4035 | 500,000 | $0.9624 | $481k | **Yes, +32.3%** | [0xd919…](https://etherscan.io/tx/0xd9194f6de2860fde0fa01c8cb4212d2277981d133bfa55bdf76aa9137a7fb559) |

- The deposit addresses carry Binance labels on Etherscan and Arkham, and forwarded straight to Binance's hot wallet. The 4 Aug 2026 deposit from 0xa59b was not on a pump day (Gate close −10.8% vs five days earlier; tx status 1 at 13:47 UTC). All linked transactions returned status 1 (success). No RLC came back to either Safe after the Oct 2026 deposits (checked 16 Nov 2026). I found no disclosure of them.

## 📊 Tokenomics & supply · 8/10 · ✅ PASS

- Fixed 87M supply, fully circulating, with no mint function and no pending unlocks.

## 💧 Liquidity & market · 4/10 · ❌ FAIL

- $2.6M of 24h volume spread across mid-tier venues. Price swung from about $0.27 to $1.03 and back within three months.

## 🧑‍💻 Product & development · 6/10 · ✅ PASS

- The TEE compute marketplace has been live since 2017. The new confidential-DeFi product (Nox) was still on testnet as of 16 Nov 2026.

## 🤝 Adoption & customers · 3/10 · ❌ FAIL

- No independent usage or fee data (DefiLlama has none). Only the project's own claims [Unverified].

## 🛡️ Security & audits · 6/10 · ✅ PASS

- No exploit found. The 2017 token contract has no mint function.

## ⚖️ Regulatory · 6/10 · ✅ PASS

- No enforcement found.

## 📅 Catalysts & calendar · 5/10 · ❌ FAIL

- The confidential-DeFi mainnet and a revenue-funded buyback are promised for "later in 2026", with no date.

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | 🔴 Yes: 651k RLC to Binance, 9–10 Oct 2026, from a Safe funded by the Arkham-labelled iExec Team wallet |
| Live mint path | 🟢 None |
| Entity concentration | 🟠 21% in two unpublished Safes |

## 📚 Sources

- [Tier A] Etherscan token, Safe and transaction pages, with Binance deposit labels. Receipts were checked through the Etherscan API on 16 Nov 2026
- [Tier A] [RLC docs](https://docs.iex.ec/get-started/overview/rlc); buyback program announced Mar 2025 (40% development / 30% treasury / 30% liquidity) [Unverified: single source]
- [Tier A] CoinGecko `iexec-rlc`; pump days from Binance RLCUSDT daily closes
- [Tier B] Arkham, read 16 Nov 2026 (signed-in account): iExec: Team label on 0xd653; Gnosis Safe labels on 0xc0e3 and 0xa59b; Binance Deposit labels; Keyrock as a counterparty; the 2017 Crowdsale contract `0xec33…0200`

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| 151k RLC → Binance on +183.9% day | [tx 0x723e…](https://etherscan.io/tx/0x723e1d3dcf4c86acde1df6f385cedf6ef1221f87680ed363819df02efe5a106a), [deposit address](https://etherscan.io/address/0x4035d72223ae3ef849c50ee6e6d56935dd8c71be) | A | 16 Nov 2026 |
| 500k RLC → Binance on +32.3% day | [tx 0xd919…](https://etherscan.io/tx/0xd9194f6de2860fde0fa01c8cb4212d2277981d133bfa55bdf76aa9137a7fb559) | A | 16 Nov 2026 |
| Safe funded from an Apr 2017 distribution wallet | [0xd653…3298](https://etherscan.io/address/0xd65380d773208a6aa49472bf55186b855b393298) | A | 16 Nov 2026 |
| Fixed supply, no unlocks | [RLC docs](https://docs.iex.ec/get-started/overview/rlc) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Who signs the two Safes** | Arkham (16 Nov 2026) ties 0xc0e3 to the iExec Team wallet by funding, not by label. Ask iExec to confirm the Safes and their signers [Unverified] | Free |
| 2 | **Whether the Oct deposits were disclosed (buyback liquidity?)** | Check iExec posts from Oct 2026 | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.

- Research only. Not investment advice.
