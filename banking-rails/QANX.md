---
ticker: QANX
name: QANplatform
chain: ethereum
contract: "0xaaa9214f675316182eaa21c85f0ca99160cc3aaa (Ethereum and BNB Chain)"
overall_score: 3.6
overall_verdict: FAIL
section_scores:
  revenue: 1
  foundation_team: 5
  insider_holdings: 4
  selling_behavior: 4
  tokenomics_supply: 5
  liquidity_market: 3
  product_development: 4
  adoption_customers: 3
  security_audits: 6
  regulatory: 5
  catalysts: 5
gates_failed: [revenue]
red_lines:
  hack_exploit: "none found"
  mint_path_live: "no: 3.333B minted once in Feb 2023; 1.233B burned Dec 2023"
  team_wallet_to_exchange_during_pump: "not proven: no exchange deposits of 1M QANX or more from the top Ethereum holders in the window; team wallets aren't identified, and the BNB Chain side isn't traced"
  one_hop_sale_status: none_found
  entity_concentration: "1.1B (52% of the 2.1B live supply) sits in the Etherscan-labelled QANX Bridge Allocation wallet, untouched since Dec 2023"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "There is no mainnet and no fee stream, so revenue does not reach holders."
pump_day_price_source: "Gate QANX-USDT UTC daily closes"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions:
  - address: "0x3e9d2bfec755a2787431dd56534226255f33a32a"
    label: "QANplatform: Bridge Allocation"
    confidence: high
    independent_corroboration: true
    basis: "Arkham + token-contract funding"
  - address: "0xce99e79466b3b3353be8b141e89c30ce3e022930"
    label: "Gate Deposit"
    confidence: high
    independent_corroboration: true
    basis: "Arkham + Etherscan forward to Gate hot wallet"
  - address: "0xd7f35d78d592609c384f4423da6a512f5e904cd8"
    label: "Unlabelled claimers (generic tags)"
    confidence: low
    independent_corroboration: false
    basis: "Arkham"
  - address: "0x0ea0f3a77e097294a54c9e15758ef760bb600ce4"
    label: "Unlabelled claimers (generic tags)"
    confidence: low
    independent_corroboration: false
    basis: "Arkham"
  - address: "0x15dc45098e220a61c307303f16bec8d67dc88d36"
    label: "Unlabelled claimers (generic tags)"
    confidence: low
    independent_corroboration: false
    basis: "Arkham"
  - address: "0x12fa63b263e0e5e2410fb975f024eb3997422092"
    label: "Unlabelled claimers (generic tags)"
    confidence: low
    independent_corroboration: false
    basis: "Arkham"
price_usd: 0.00786508
price_source: "CoinGecko, 16 Nov 2026 ~11:35 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### QANX · Overall grade **3.6 / 10 · ❌ FAIL**

**Summary:** QANplatform is building a quantum-resistant, Ethereum-compatible layer 1. Its mainnet still isn't live: the team has promised it "this year" since July 2026, and the final audit hasn't started. The QANX token pays nothing to holders. In December 2023, 1.233B QANX was burned and 1.1B was moved to a wallet Etherscan labels as the QANX Bridge Allocation. That wallet hasn't moved since and holds 52% of the live supply. The revenue gate fails.

**🚨 Top warning:** **half the live supply waits for a mainnet that hasn't launched.** On 14 Dec 2023, the token contract sent **1,100,000,000 QANX** to `0x3e9d…a32a`, which Etherscan labels "QANplatform: QANX Bridge Allocation" ([tx](https://etherscan.io/tx/0xda6c51690ac459f4cf2d1529c82e99f1bd49e5bb3f4c72b99951b1235cd9dfdc), status 1). It hasn't moved since. That's 52% of the 2.1B live supply. Mainnet has been promised for 2026, but on 23 Oct 2026 the final audit hadn't started ([Crypto Quantum Tracker](https://cryptoquantum.info/chain/qanx), [QAN Medium](https://medium.com/qanplatform/september-milestones-xlink-goes-on-chain-and-deterministic-qvm-metering-takes-shape-b70a92f7c686)). Every link is in the 🔗 Evidence trail below.

**Sections passed: 1 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 1/10 | ❌ FAIL (hard gate) |
| 🏛️ Foundation & team | 5/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 4/10 | ❌ FAIL |
| 📉 Selling behavior | 4/10 | ❌ FAIL (not proven) |
| 📊 Tokenomics & supply | 5/10 | ❌ FAIL |
| 💧 Liquidity & market | 3/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 4/10 | ❌ FAIL |
| 🤝 Adoption & customers | 3/10 | ❌ FAIL |
| 🛡️ Security & audits | 6/10 | ✅ PASS |
| ⚖️ Regulatory | 5/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 5/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 QANX · QANplatform · 3.6 / 10 · ❌ FAIL

> **One line:** A pre-mainnet quantum-safe chain token with no revenue and half its supply parked for a bridge.

| 📊 Market (CoinGecko, 16 Nov 2026 ~11:35 AM MST) | 🔗 Chain (Etherscan) |
|---|---|
| **Price** $0.00787 | **Supply** 2.1B live (3.333B minted, 1.233B burned) |
| **24h / 7d / 30d** 🔴 −3.0% / 🔴 −12.7% / 🔴 −30.7% | **Bridge Allocation** 1.1B, idle since Dec 2023 |
| **Market cap** $13.4M · **FDV** $16.5M | **Token contract** still holds 132.4M for claims |
| **24h volume** ~$0.10M (Uniswap v3 $43k, Gate $35k, PancakeSwap $27k) | **Gate deposit** `0xc882…f071` 79.3M |
| **ATH** $0.2034 (27 Nov 2021) · now −96.1% | |
| **Pump days** 24 in the last year (Gate QANX-USDT; largest +52.1% on 5 Jul 2026) | |

---

## 💰 Revenue — Does it make money? · 1/10 · ❌ FAIL (hard gate)

- No mainnet, so no fees. Nothing accrues to QANX. **1 → hard-gate FAIL.**

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** There is no mainnet and no fee stream, so revenue does not reach holders.

## 🏛️ Foundation & team — Who is in charge? · 5/10 · ❌ FAIL

- A company publishing its leadership, with Hacken audits of its VM (Jul 2025) and cross-signer (Nov 2025). Mainnet deadlines have repeatedly slipped.

## 🪙 Foundation / team holdings — How many coins do they hold? · 4/10 · ❌ FAIL

- Allocation: reserve 24.4%, liquidity 15%, marketing 15.6%, team 10%, advisors 10%, staking 10% ([Tokenomics.com](https://app.tokenomics.com/tokenomics/qanplatform)). All vesting is finished. The 1.1B Bridge Allocation is the only large identified project wallet.
- **Arkham (16 Nov 2026)** labels [0x3e9d…a32a](https://intel.arkm.com/explorer/address/0x3e9d2bfec755a2787431dd56534226255f33a32a) **QANplatform: Bridge Allocation**. It holds 2.2B QANX, 1.1B on Ethereum and 1.1B on BNB Chain, each received from the token contract about two years ago, with no transfers since (Dormant tag). On BNB Chain it is the largest holder (33%). The next Ethereum holders [0xd7f3…4cd8](https://intel.arkm.com/explorer/address/0xd7f35d78d592609c384f4423da6a512f5e904cd8) (18.3M), [0x0ea0…0ce4](https://intel.arkm.com/explorer/address/0x0ea0f3a77e097294a54c9e15758ef760bb600ce4) (12.6M), [0x15dc…8d36](https://intel.arkm.com/explorer/address/0x15dc45098e220a61c307303f16bec8d67dc88d36) and [0x12fa…2092](https://intel.arkm.com/explorer/address/0x12fa63b263e0e5e2410fb975f024eb3997422092) (10.1M each) are unlabelled claimers with only generic Whale or first-funder tags, so they can't be classed as team. [Tier B] Arkham, read 16 Nov 2026 (signed-in account).

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL (not proven)

- I traced the Bridge Allocation and the top ten unlabelled Ethereum holders two hops out, for transfers of 1M QANX or more. No exchange deposits at all. Team and reserve tokens were claimed through the token contract into 1,741 addresses, so team wallets aren't identified, and the BNB Chain side isn't traced.
- **Arkham (16 Nov 2026):** [0xce99…2930](https://intel.arkm.com/explorer/address/0xce99e79466b3b3353be8b141e89c30ce3e022930) is a labelled **Gate Deposit**. It received 79,433,495 QANX straight from the token contract on 19 Mar 2023 ([tx](https://etherscan.io/tx/0x80e4e9ef5ead8b08514d4c0f84cf0322afad8fb18e976dda4d783ba51cca7993)) and forwarded all of it to Gate's hot wallet the same day ([tx](https://etherscan.io/tx/0x77b25cf0a5ec767bdca0aa4d17a0bd71620e8d9ecfb56ec0499b65615ff83172)). That is a contract claim paid directly to an exchange account more than three years ago, outside the one-year window, and the claimant is not identified. On BNB Chain, Arkham shows only small Gate deposits forwarding to the Gate hot wallet (50K and less), none tied to a pump day. [Tier B] Arkham, read 16 Nov 2026 (signed-in account).
- No labelled QANplatform wallet sent to an exchange in the window, and no pump-day deposit is established. **Not proven → 4.**

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from Gate QANX-USDT UTC daily closes.

## 📊 Tokenomics & supply · 5/10 · ❌ FAIL

- 1.233B burned in Dec 2023 ([tx](https://etherscan.io/tx/0x3cc2f6fd1637ffed7c4b7d77e9db29ffd48ed10454789213e98129cbf2b5beed), [tx](https://etherscan.io/tx/0x4ea6d624382696d18f81ab783d63a1302ec784d9bae37abdf9c854b67f152c0a)). No more minting. The bridge reserve could reach the market at mainnet.

## 💧 Liquidity & market · 3/10 · ❌ FAIL

- About $0.10M a day across Uniswap, Gate and PancakeSwap.

## 🧑‍💻 Product & development · 4/10 · ❌ FAIL

- Testnet only. The execution client was rebased onto Ethereum code in 2026.

## 🤝 Adoption & customers · 3/10 · ❌ FAIL

- One third-party bank pilot runs on a private QAN deployment, not the public chain.

## 🛡️ Security & audits · 6/10 · ✅ PASS

- No exploit found. Hacken audits.

## ⚖️ Regulatory · 5/10 · ❌ FAIL

- No enforcement found.

## 📅 Catalysts & calendar · 5/10 · ❌ FAIL

- Mainnet launch promised for 2026.

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | ⚪ Not proven: no deposits found; team wallets unidentified |
| Live mint path | 🟢 No |
| Entity concentration | 🔴 1.1B (52%) in the Bridge Allocation wallet |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| [0x3e9d…a32a](https://intel.arkm.com/explorer/address/0x3e9d2bfec755a2787431dd56534226255f33a32a) | QANplatform: Bridge Allocation | Arkham + token-contract funding | high | yes (on-chain allocation) | Holdings: project reserve, dormant |
| [0xce99…2930](https://intel.arkm.com/explorer/address/0xce99e79466b3b3353be8b141e89c30ce3e022930) | Gate Deposit | Arkham + Etherscan forward to Gate hot wallet | high | yes | None (2023, outside window) |
| [0xd7f3…4cd8](https://intel.arkm.com/explorer/address/0xd7f35d78d592609c384f4423da6a512f5e904cd8), [0x0ea0…0ce4](https://intel.arkm.com/explorer/address/0x0ea0f3a77e097294a54c9e15758ef760bb600ce4), [0x15dc…8d36](https://intel.arkm.com/explorer/address/0x15dc45098e220a61c307303f16bec8d67dc88d36), [0x12fa…2092](https://intel.arkm.com/explorer/address/0x12fa63b263e0e5e2410fb975f024eb3997422092) | Unlabelled claimers (generic tags) | Arkham | low | no | None |

## 📚 Sources

- [Tier B] Arkham, read 16 Nov 2026 (signed-in account): the Bridge Allocation, the top unlabelled claimers, the Gate deposit and the BNB Chain token page; dates from Etherscan
- [Tier A] [QANplatform company page](https://learn.qanplatform.com/about-us/company), [QAN September milestones](https://medium.com/qanplatform/september-milestones-xlink-goes-on-chain-and-deterministic-qvm-metering-takes-shape-b70a92f7c686), [CTO open letter, Jul 2026](https://medium.com/qanplatform/open-letter-from-qanplatforms-co-founder-and-cto-reinforcing-mainnet-launch-this-year-2394d1bc510d)
- [Tier B] [Tokenomics.com QANX](https://app.tokenomics.com/tokenomics/qanplatform), [Crypto Quantum Tracker](https://cryptoquantum.info/chain/qanx)
- [Tier A] Etherscan holders, labels and transfers for `0xaaa9…3aaa`
- [Tier A] CoinGecko `qanplatform` (market, venues); pump days from Gate QANX-USDT daily closes

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| 1.1B → QANX Bridge Allocation, 14 Dec 2023 | [tx](https://etherscan.io/tx/0xda6c51690ac459f4cf2d1529c82e99f1bd49e5bb3f4c72b99951b1235cd9dfdc) | A | 16 Nov 2026 |
| 1.133B burned, Dec 2023 | [tx](https://etherscan.io/tx/0x3cc2f6fd1637ffed7c4b7d77e9db29ffd48ed10454789213e98129cbf2b5beed) | A | 16 Nov 2026 |
| 100.45M burned, Dec 2023 | [tx](https://etherscan.io/tx/0x4ea6d624382696d18f81ab783d63a1302ec784d9bae37abdf9c854b67f152c0a) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Identify team and reserve claim wallets** among the 1,741 claimers | Not published; Arkham (16 Nov 2026) labels only the Bridge Allocation and exchange wallets. Ask QANplatform | Free |
| 2 | **BNB Chain side** | BscScan API needs a paid tier | Arkham |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.

- Research only. Not investment advice.
