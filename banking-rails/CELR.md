---
ticker: CELR
name: Celer Network
chain: ethereum
contract: "0x4f9254c83eb525f9fcf346490bbb3ed28a81c667"
overall_score: 4.0
overall_verdict: FAIL
section_scores:
  revenue: 2
  foundation_team: 5
  insider_holdings: 4
  selling_behavior: 5
  tokenomics_supply: 7
  liquidity_market: 4
  product_development: 5
  adoption_customers: 3
  security_audits: 4
  regulatory: 5
  catalysts: 3
gates_failed: [revenue]
red_lines:
  hack_exploit: "none in the token; see Security"
  mint_path_live: "no (no mint function; fixed 10B)"
  pause_power: "yes: token owner 0xb22dc759f194f5d00f1981bf47ab5c3572562c96 (deployer EOA) can pause all transfers"
  team_wallet_to_exchange_during_pump: "none found; pump-day flows traced to exchange-cycling wallets"
  one_hop_sale_status: none_found
  treasury_in_single_key_wallets: "yes: mining-rewards reserve 0xa6045362e295db86da338da6b2a9f439add951b2 (1.63B CELR, 16.3%) is a plain EOA, labelled Celer Network: Treasury by Arkham"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "SGN fees go to validators and delegators in undisclosed amounts and no fee series is published, so revenue reaching holders is not shown."
pump_day_price_source: "Binance CELRUSDT UTC daily closes (Gate cross-check)"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions:
  - address: "0xa6045362e295db86da338da6b2a9f439add951b2"
    label: "Celer Network: Treasury (Team Wallet)"
    confidence: high
    independent_corroboration: true
    basis: "Arkham + 2.5B genesis transfer"
  - address: "0xb22dc759f194f5d00f1981bf47ab5c3572562c96"
    label: "Celer Network: Deployer"
    confidence: high
    independent_corroboration: true
    basis: "Arkham + RPC owner()"
  - address: "0x8a4b4c2acadeaa7206df96f00052e41d74a015ce"
    label: "Celer Network: Staking (verified)"
    confidence: high
    independent_corroboration: true
    basis: "Arkham + Etherscan"
  - address: "0x0f69be25aaeeb9478fa4c9666b69bbe8bfefd107"
    label: "Coinbase Deposit; Coinbase Hot Wallet"
    confidence: medium
    independent_corroboration: false
    basis: "Arkham"
  - address: "0xa9d1e08c7793af67e9d92fe308d5697fb81d3e43"
    label: "Coinbase Deposit; Coinbase Hot Wallet"
    confidence: medium
    independent_corroboration: false
    basis: "Arkham"
  - address: "0x758720487c5efd0947a98d81040233e2fb1d1509"
    label: "Bitvavo: Coinbase Prime Custody"
    confidence: medium
    independent_corroboration: false
    basis: "Arkham"
price_usd: 0.0019601
price_source: "CoinGecko, 16 Nov 2026 9:56 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### CELR · Overall grade **4.0 / 10 · ❌ FAIL**

**Summary:** Celer runs cBridge and the State Guardian Network (SGN), a Tendermint chain where CELR is staked to secure cross-chain messages. Supply is fixed at **10B CELR** with no mint function, and 91.6% is unlocked [Tier B]. Fee data is not tracked: DefiLlama lists cBridge only as a bridge, with **$10.75M TVL** and no fees series [Tier A]. Two control points stand out. The token owner is still the [deployer EOA](https://etherscan.io/address/0xb22dc759f194f5d00f1981bf47ab5c3572562c96), and the contract's `pause()` lets that one key **freeze every CELR transfer**. The 2.5B mining-rewards allocation sent at genesis still sits in plain EOA [0xa604…51b2](https://etherscan.io/address/0xa6045362e295db86da338da6b2a9f439add951b2) (**1.63B, 16.3%**). No team selling into pumps was found.

**🚨 Top warning:** A single key ([0xb22d…2c96](https://etherscan.io/address/0xb22dc759f194f5d00f1981bf47ab5c3572562c96)) can pause CELR transfers network-wide. A 1.63B CELR reserve sits in an EOA with no multisig. Fee revenue is not measurable. Price is −60.6% in a year and −99% from ATH.

**Sections passed: 1 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 2/10 | ❌ FAIL |
| 🏛️ Foundation & team | 5/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 4/10 | ❌ FAIL |
| 📉 Selling behavior | 5/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 7/10 | ✅ PASS |
| 💧 Liquidity & market | 4/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 5/10 | ❌ FAIL |
| 🤝 Adoption & customers | 3/10 | ❌ FAIL |
| 🛡️ Security & audits | 4/10 | ❌ FAIL |
| ⚖️ Regulatory | 5/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 3/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 CELR · Celer Network · 4.0 / 10 · ❌ FAIL

> **One line:** Fixed supply and no pump-timed insider dumping, but single-key control and no measurable fees.

| 📊 Market (CoinGecko, 16 Nov 2026 9:56 AM MST) | 🔗 On-chain (Blockscout / RPC, 16 Nov 2026) |
|---|---|
| **Price** $0.00196 · 7d / 30d −12.4% / −25.2% · 1y −60.6% | **Supply** 10,000,000,000 (fixed) · 24,578 holders |
| **Market cap** $15.5M · rank #894 · circ 7.92B | **SGN staking contract** [0x8a4b…15ce](https://etherscan.io/address/0x8a4b4c2acadeaa7206df96f00052e41d74a015ce): 18.15% |
| **24h volume** $1.28M: Binance $0.24M, BitDelta, BTCC, Pionex, BVOX | **Mining-rewards EOA** [0xa604…51b2](https://etherscan.io/address/0xa6045362e295db86da338da6b2a9f439add951b2): 16.32% |
| **Pump days** 26 in 365 (Binance CELR/USDT daily closes) | **Token owner** deployer EOA [0xb22d…2c96](https://etherscan.io/address/0xb22dc759f194f5d00f1981bf47ab5c3572562c96) (can `pause`) |

---

## 💰 Revenue — Does it make money? · 2/10 · ❌ FAIL

| Metric | Value | Source |
|---|---:|---|
| cBridge TVL | $10.75M | [Tier A] api.llama.fi/protocols |
| cBridge / SGN fees | Not tracked | [Tier A] DefiLlama "fees not found" |
| Fee share to stakers | SGN fees paid to validators and delegators (amount undisclosed) | [Tier A] [celer.network/technology](https://celer.network/technology/) |

**What it means:** revenue can't be measured. **2 (hard gate).**

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** SGN fees go to validators and delegators in undisclosed amounts and no fee series is published, so revenue reaching holders is not shown.

## 🏛️ Foundation & team — Who is in charge? · 5/10 · ❌ FAIL

- Celer has shipped cBridge since 2021, plus AgentPay (a state-channel payments network for AI agents, 2026) ([blog](https://blog.celer.network/category/news/), Tier A).

## 🪙 Foundation / team holdings — How many coins do they hold? · 4/10 · ❌ FAIL

| Holder | % supply | Note |
|---|---:|---|
| [0x8a4b…15ce](https://etherscan.io/address/0x8a4b4c2acadeaa7206df96f00052e41d74a015ce) SGN Staking | 18.15% | owner [0xf380…6575](https://etherscan.io/address/0xf380166f8490f24af32bf47d1aa217fba62b6575) (contract) |
| [0xa604…51b2](https://etherscan.io/address/0xa6045362e295db86da338da6b2a9f439add951b2) | 16.32% | received 2.5B from the deployer on 24 Mar 2019 ([0xcdfb0389…](https://etherscan.io/tx/0xcdfb038903f4d47f15b53f9211e698bb4fb477909713da40ea95096cbad4b76d)), matching the 25% mining-rewards allocation; plain EOA |
| Binance cold wallet | 13.13% | exchange |
| Unlabeled EOAs ([0x884a…4E9b](https://etherscan.io/address/0x884aD5933693D8575C37247774C9c1148a1C4E9b), [0x0fcb…Ab0C](https://etherscan.io/address/0x0fcb193c75cecae31d592B9CA0AE11C96a5bAb0C)) | 9.04% | low or no 365-day outflow |

- Team, foundation and investor tranches finished vesting years ago [Tier B, tokenomics.com]. The remaining scheduled unlock is ~25M CELR a month to Nov 2027.

## 📉 Selling behavior — Do insiders sell into pumps? · 5/10 · ❌ FAIL

*Binance CELR/USDT daily closes (UTC): 26 pump days in the last 365.*

| Wallet | Pump-day transfers | What it is |
|---|---|---|
| [0xa604…51b2](https://etherscan.io/address/0xa6045362e295db86da338da6b2a9f439add951b2) mining-rewards EOA | none; 15M out in 365 days (e.g. 10M on 4 Sep 2026) | reserve |
| [0x0f69…d107](https://etherscan.io/address/0x0f69be25aaeeb9478fa4c9666b69bbe8bfefd107) (3.64%) | 38.6M on 8 May ([0x1a804950…](https://etherscan.io/tx/0x1a804950bde18fc6b28df5bbc09035e2f3ffff2d12543d9d1a4d6e82ed9bb7e0)), 31.4M and 38.3M on 21/23 Sep ([0xd8f20e7a…](https://etherscan.io/tx/0xd8f20e7a6c89af9cbbb7eacae008436614c8c0f0e62d3830fa7ec908522444d9), [0xa4c595f7…](https://etherscan.io/tx/0xa4c595f78c38b9c14b783ddf6c641ceae031c5d57a4cfc39494713373be30f4a)) → [0xa9d1…3e43](https://etherscan.io/address/0xa9d1e08c7793af67e9d92fe308d5697fb81d3e43) | two-way: received 754M from and sent 393M to [0xa9d1…3e43](https://etherscan.io/address/0xa9d1e08c7793af67e9d92fe308d5697fb81d3e43), **Coinbase Hot Wallet** per Arkham; 0x0f69 itself is a **Coinbase Deposit** wallet, so these are exchange-internal moves |
| [0x1c87…8e30](https://etherscan.io/address/0x1c875c7c66243bb9de381c01f1dbe82cf0b98e30) → [0x7587…1509](https://etherscan.io/address/0x758720487c5efd0947a98d81040233e2fb1d1509) → Bitvavo | 78.4M withdrawn from Bitvavo 20 Sep, 20M back to Bitvavo Hot 3 [0xab78…e1bc](https://etherscan.io/address/0xab782bc7d4a2b306825de5a7730034f8f63ee1bc) on 21 Sep ([0xeedd525e…](https://etherscan.io/tx/0xeedd525e03ecc051b1e8aa6e8aec32dc8b2fb98feb3bf0d24000408d0d567ab5)) | Arkham labels 0x7587 **Bitvavo: Coinbase Prime Custody**: exchange custody, not a project wallet. 21 Sep was a pump day (+61.5% on Gate closes), but the move is internal to Bitvavo |

- **Arkham (16 Nov 2026):** [0xa604…51b2](https://intel.arkm.com/explorer/address/0xa6045362e295db86da338da6b2a9f439add951b2) is labelled **Celer Network: Treasury** (Team Wallet tag), high confidence alongside the 2.5B genesis transfer. Its 21 transfers go only to Celer's Farming Rewards and StakingReward contracts (e.g. 10M two months ago, the 4 Sep 2026 transfer above) or an unlabelled wallet four years ago; none to an exchange. [0x0f69…d107](https://intel.arkm.com/explorer/address/0x0f69be25aaeeb9478fa4c9666b69bbe8bfefd107) is a **Coinbase Deposit** wallet, [0xa9d1…3e43](https://intel.arkm.com/explorer/address/0xa9d1e08c7793af67e9d92fe308d5697fb81d3e43) is **Coinbase: Hot Wallet**, and [0x7587…1509](https://intel.arkm.com/explorer/address/0x758720487c5efd0947a98d81040233e2fb1d1509) is **Bitvavo: Coinbase Prime Custody**. The deployer [0xb22d…2c96](https://intel.arkm.com/explorer/address/0xb22dc759f194f5d00f1981bf47ab5c3572562c96) (Celer Network: Deployer) last sent CELR to Binance deposits five to six years ago. [Tier B] Arkham, read 16 Nov 2026 (signed-in account).

**What it means:** pump-day flows are exchange-internal or trading wallets, not insiders. **5**.

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from Binance CELRUSDT UTC daily closes (Gate cross-check).

## 📊 Tokenomics & supply · 7/10 · ✅ PASS

- Fixed 10B. The token ABI has no `mint` (verified source: `pause`, `unpause`, whitelist, `openTransfer`). **7**.

## 💧 Liquidity & market · 4/10 · ❌ FAIL

- $1.28M of 24h volume on a $15.5M cap, spread thinly across venues; Binance is the largest at $0.24M.

## 🧑‍💻 Product & development · 5/10 · ❌ FAIL

- cBridge keeps adding chains and tokens (Base, Unichain, Redbelly 2025; the CMC20 index token). AgentPay launched in 2026.

## 🤝 Adoption & customers · 3/10 · ❌ FAIL

- cBridge TVL is only $10.75M. Bridge market share has been lost to newer intent-based bridges.

## 🛡️ Security & audits · 4/10 · ❌ FAIL

- Token: owner [0xb22d…2c96](https://etherscan.io/address/0xb22dc759f194f5d00f1981bf47ab5c3572562c96) (EOA) can `pause()` all transfers; currently not paused [Tier A, RPC].
- An Aug 2022 cBridge front-end DNS hijack drained user approvals [Unverified, not re-sourced this run]. **4**.

## ⚖️ Regulatory · 5/10 · ❌ FAIL

- No enforcement found.

## 📅 Catalysts & calendar · 3/10 · ❌ FAIL

| Date | Event |
|---|---|
| 27th of each month | ~25M CELR unlock [Tier B] |
| Nov 2027 | Final unlock |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟡 2022 front-end DNS hijack [Unverified] |
| Team wallet → exchange during a pump | 🟢 None found |
| Live mint path | 🟢 None (fixed supply) |
| Single-key controls | 🔴 Deployer EOA can pause transfers; 1.63B reserve in an EOA |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| [0xa604…51b2](https://intel.arkm.com/explorer/address/0xa6045362e295db86da338da6b2a9f439add951b2) | Celer Network: Treasury (Team Wallet) | Arkham + 2.5B genesis transfer | high | yes (on-chain) | Holdings: confirms team reserve; no exchange sends |
| [0xb22d…2c96](https://intel.arkm.com/explorer/address/0xb22dc759f194f5d00f1981bf47ab5c3572562c96) | Celer Network: Deployer | Arkham + RPC owner() | high | yes | None |
| [0x8a4b…15ce](https://intel.arkm.com/explorer/address/0x8a4b4c2acadeaa7206df96f00052e41d74a015ce) | Celer Network: Staking (verified) | Arkham + Etherscan | high | yes | None |
| [0x0f69…d107](https://intel.arkm.com/explorer/address/0x0f69be25aaeeb9478fa4c9666b69bbe8bfefd107), [0xa9d1…3e43](https://intel.arkm.com/explorer/address/0xa9d1e08c7793af67e9d92fe308d5697fb81d3e43) | Coinbase Deposit; Coinbase Hot Wallet | Arkham | medium | no | Removes candidates: exchange-internal |
| [0x7587…1509](https://intel.arkm.com/explorer/address/0x758720487c5efd0947a98d81040233e2fb1d1509) | Bitvavo: Coinbase Prime Custody | Arkham | medium | no | Removes a candidate: exchange custody |

## 📚 Sources

- [Tier B] Arkham, read 16 Nov 2026 (signed-in account): the Treasury, deployer, staking contract and the Coinbase and Bitvavo wallets; dates from Etherscan
- [Tier A] Etherscan v2 token transfers; Blockscout holders, verified ABI and address metadata; Ethereum RPC `owner()`, `paused()`
- [Tier A] Etherscan labels (Celer Network: Deployer; Binance; Bitvavo Hot 3)
- [Tier A] [Celer technology page](https://celer.network/technology/) · [Celer blog](https://blog.celer.network/category/news/) · DefiLlama protocols and fees
- [Tier B] [tokenomics.com CELR unlocks](https://app.tokenomics.com/tokenomics/celer-network/unlocks)
- [Tier A] CoinGecko `celer-network` (16 Nov 2026 9:56 AM MST); Binance CELRUSDT daily klines (cross-checked with Gate: 26 pump days on both)

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| 2.5B mining allocation to an EOA at genesis | [0xcdfb0389…](https://etherscan.io/tx/0xcdfb038903f4d47f15b53f9211e698bb4fb477909713da40ea95096cbad4b76d) | A | 16 Nov 2026 |
| Deployer EOA owns the pausable token | [0xb22d…2c96](https://etherscan.io/address/0xb22dc759f194f5d00f1981bf47ab5c3572562c96) | A | 16 Nov 2026 |
| Pump-day flow to Bitvavo from a cycling wallet | [0xeedd525e…](https://etherscan.io/tx/0xeedd525e03ecc051b1e8aa6e8aec32dc8b2fb98feb3bf0d24000408d0d567ab5) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Who signs for the Treasury EOA** | Arkham (16 Nov 2026) confirms the Celer Network: Treasury label; ask Celer about key custody | Free |
| 2 | **Identity of the omnibus contract** | Closed 16 Nov 2026: Arkham labels [0xa9d1…3e43](https://intel.arkm.com/explorer/address/0xa9d1e08c7793af67e9d92fe308d5697fb81d3e43) Coinbase: Hot Wallet | Done |
| 3 | **SGN fee income** | SGN chain explorer / validator reward data | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
