---
ticker: IOST
name: IOST
chain: bsc + IOST L1
contract: "0xaf48b7e315a52518cfbf7d96c455d9dfad94cb48"
overall_score: 3.1
overall_verdict: FAIL
section_scores:
  revenue: 1
  foundation_team: 4
  insider_holdings: 3
  selling_behavior: 4
  tokenomics_supply: 2
  liquidity_market: 4
  product_development: 4
  adoption_customers: 2
  security_audits: 5
  regulatory: 5
  catalysts: 3
gates_failed: [revenue]
red_lines:
  hack_exploit: "none found"
  mint_path_live: "yes, BSC owner mint up to a 90B cap, separate from the L1 90B cap"
  mint_owner: "0x6ab479c813daa50914fc96c837e2f08a8203ab70 (3-of-4 Safe)"
  team_wallet_to_exchange_during_pump: "not tested (BSC transfer history not reachable with free tools)"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "L2 gas is paid in BNB, and no fee burn, automatic buyback or fee share is live, so revenue does not reach holders."
pump_day_price_source: "Gate IOST_USDT UTC daily closes"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions:
  - address: "0xaf48b7e315a52518cfbf7d96c455d9dfad94cb48"
    label: "IOST BEP-20 token"
    confidence: high
    independent_corroboration: true
    basis: "Arkham + BscScan verified source"
  - address: "0x6ab479c813daa50914fc96c837e2f08a8203ab70"
    label: "Safe (3-of-4), signer tags shown"
    confidence: high
    independent_corroboration: true
    basis: "Arkham + RPC owner()"
price_usd: 0.00056557
price_source: "CoinGecko, 16 Nov 2026 9:11 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### IOST · Overall grade **3.1 / 10 · ❌ FAIL**

**Summary:** IOST relaunched as "IOST 3.0" in Mar 2025: a BEP-20 token on BNB Chain plus an OP Stack Layer 2 whose gas is paid in **BNB, not IOST**. The project issued **21.32B new IOST** for the relaunch, roughly doubling the original float ([economic model](https://docs.iost.io/tokenomics/economic-model), Tier A). Two ledgers now coexist: **32.74B** on the original L1 (api.iost.io) and **22.37B** on the [BSC contract](https://bscscan.com/address/0xaf48b7e315a52518cfbf7d96c455d9dfad94cb48), read by RPC. Each has its own 90B cap. The BSC owner, a [3-of-4 Safe](https://bscscan.com/address/0x6ab479c813daa50914fc96c837e2f08a8203ab70), can call `mint` up to that cap. No fee revenue reaches the token, so Revenue trips the hard gate.

**🚨 Top warning:** Supply is controlled by a multisig: the BSC owner can mint up to 90B regardless of the L1 supply. A further ~12.4B IOST is reported still vesting from one revocable contract through 2030, about 444M every 30 days [Unverified, single Tier B]. Price is −70% in a year and −99.6% from ATH.

**Sections passed: 0 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 1/10 | ❌ FAIL |
| 🏛️ Foundation & team | 4/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 3/10 | ❌ FAIL |
| 📉 Selling behavior | 4/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 2/10 | ❌ FAIL |
| 💧 Liquidity & market | 4/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 4/10 | ❌ FAIL |
| 🤝 Adoption & customers | 2/10 | ❌ FAIL |
| 🛡️ Security & audits | 5/10 | ❌ FAIL |
| ⚖️ Regulatory | 5/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 3/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 IOST · IOST · 3.1 / 10 · ❌ FAIL

> **One line:** A rebranded L1 with a doubled supply, a multisig mint key and an L2 that runs on BNB gas.

| 📊 Market (CoinGecko, 16 Nov 2026 9:11 AM MST) | 🔗 On-chain (RPC / IOST API, 16 Nov 2026) |
|---|---|
| **Price** $0.000566 · 1y −69.9% | **BSC supply** 22,373,793,636 · cap 90B · owner [3-of-4 Safe](https://bscscan.com/address/0x6ab479c813daa50914fc96c837e2f08a8203ab70) |
| **Market cap** $20.7M · rank #738 · circ 36.69B of 90B max | **L1 supply** 32,739,771,023 · cap 90B · head block 481,058,784 |
| **24h volume** $2.31M: HTX $0.78M, LBank, Binance $0.23M, WhiteBIT, Pionex | **Pump days** 32 in 365 (Gate IOST/USDT) |
| **ATH** $0.1298 (2018) · now −99.6% | |

---

## 💰 Revenue — Does it make money? · 1/10 · ❌ FAIL

| Metric | Value | Source |
|---|---:|---|
| L2 gas token | BNB, not IOST | [Tier B] iost.asia 3.0 explainer; [Tier A] docs.iost.io |
| DefiLlama fees / chain TVL | Not listed | [Tier A] api.llama.fi |
| 2025 buyback | $3M announced Jul 2025; no on-chain proof found | [Unverified] |

**What it means:** no protocol revenue accrues to IOST. **1 (hard gate).**

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** L2 gas is paid in BNB, and no fee burn, automatic buyback or fee share is live, so revenue does not reach holders.

## 🏛️ Foundation & team — Who is in charge? · 4/10 · ❌ FAIL

- The IOST Foundation runs the project. A $21M strategic round led by DWF Labs (Jun 2025) is [Unverified] (one Tier B source).
- Sep 2026: 70M legacy ERC-20 IOST burned ([Medium](https://medium.com/iost/the-iost-foundation-completes-70-million-token-burn-c2966786331e), Tier A).

## 🪙 Foundation / team holdings — How many coins do they hold? · 3/10 · ❌ FAIL

| Bucket (of the 21.32B relaunch issuance) | Share | Vesting | Source |
|---|---:|---|---|
| PayPIN node rewards | 60% | 60 months | [Tier A] docs |
| Airdrops and stakedrops | 20% | 48 months | same |
| PayFi incentives / dev grants / Nexus DAO | 8% / 5% / 4% | 36–48 months | same |
| Team | 3% | 12-month lock, 36-month release | same |

- One vesting contract reportedly holds all ten schedules: 7.9B released and 12.39B still unvested as of mid-Oct 2026, revocable by a 3-of-4 multisig [Unverified].
- A free holder list for BSC was not reachable, so concentration is unmeasured.

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL

*Gate IOST/USDT daily closes (UTC): 32 pump days in the last 365.*

- Not tested. BscScan's API is paid-only for BSC and public RPCs cap log ranges, so the vesting and beneficiary flows could not be pulled.
- About 444M IOST a month of reported vesting [Unverified] is a steady supply overhang.

**What it means:** unknown, with heavy scheduled supply. **4**.

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from Gate IOST_USDT UTC daily closes.

## 📊 Tokenomics & supply · 2/10 · ❌ FAIL

- BSC `mint(address,uint256)` is owner-only, capped at 90B (`cap()` read by RPC); owner [0x6ab479c813daa50914fc96c837e2f08a8203ab70](https://bscscan.com/address/0x6ab479c813daa50914fc96c837e2f08a8203ab70) is a Safe with threshold 3 and 4 owners.
- The L1 has a separate 90B cap and 32.74B supply. A one-way bridge moves L1 coins to BSC, so the two supplies overlap and the real float is unclear.
- The relaunch doubled supply. **2**.

## 💧 Liquidity & market · 4/10 · ❌ FAIL

- $2.31M of 24h volume on a $20.7M cap (11%); HTX is the largest venue.

## 🧑‍💻 Product & development · 4/10 · ❌ FAIL

- L1 still runs (go-iost v4.0.0 node upgrade, Oct 2026). The OP Stack L2 (chain ID 182) is live but reported nearly empty [Tier B].

## 🤝 Adoption & customers · 2/10 · ❌ FAIL

- No DefiLlama listing for either chain. The Signet identity ring app (Nov 2025) shows no measurable on-chain use.

## 🛡️ Security & audits · 5/10 · ❌ FAIL

- No exploit found. Mint and vesting powers sit with 3-of-4 multisigs.

## ⚖️ Regulatory · 5/10 · ❌ FAIL

- No enforcement found.

## 📅 Catalysts & calendar · 3/10 · ❌ FAIL

| Date | Event |
|---|---|
| Every 30 days | ~444M IOST vesting tranche [Unverified] |
| Early Mar 2027 | Year-two node-reward tranche ends [Unverified] |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | 🟡 Not tested |
| Live mint path | 🔴 Owner mint to 90B on BSC (3-of-4 Safe) |
| Revocable vesting by multisig | 🟡 Reported [Unverified] |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| [0xaf48…cb48](https://intel.arkm.com/explorer/address/0xaf48b7e315a52518cfbf7d96c455d9dfad94cb48) | IOST BEP-20 token | Arkham + BscScan verified source | high | yes | None; March 2025 mint not visible on Arkham |
| [0x6ab4…ab70](https://intel.arkm.com/explorer/address/0x6ab479c813daa50914fc96c837e2f08a8203ab70) | Safe (3-of-4), signer tags shown | Arkham + RPC `owner()` | high | yes (on-chain) | None (mint path) |

## 📚 Sources

- [Tier B] Arkham, read 16 Nov 2026 (signed-in account): the BSC token contract and its owner Safe; neither page shows the March 2025 mint
- [Tier A] BSC RPC reads of `totalSupply()`, `cap()`, `owner()`, `getThreshold()`, `getOwners()`; verified source (ABI) of the token
- [Tier A] api.iost.io `getTokenInfo/iost` and `getChainInfo`
- [Tier A] [IOST economic model](https://docs.iost.io/tokenomics/economic-model) · [70M burn](https://medium.com/iost/the-iost-foundation-completes-70-million-token-burn-c2966786331e)
- [Tier B] [iost.asia 3.0 explainer](https://iost.asia/en/iost-3-0) · [Phemex vesting analysis](https://phemex.com/blogs/iost-price-prediction-2026-2030)
- [Tier A] CoinGecko `iostoken` (16 Nov 2026 9:11 AM MST); Gate IOST/USDT daily candles

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Owner mint up to 90B | [token](https://bscscan.com/address/0xaf48b7e315a52518cfbf7d96c455d9dfad94cb48) | A | 16 Nov 2026 |
| Owner is a 3-of-4 Safe | [Safe](https://bscscan.com/address/0x6ab479c813daa50914fc96c837e2f08a8203ab70) | A | 16 Nov 2026 |
| 21.32B relaunch issuance | [docs](https://docs.iost.io/tokenomics/economic-model) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Arkham attribution of the IOST wallets** | Done 16 Nov 2026: Arkham shows the BSC token and the owner Safe but not the March 2025 mint or its destination. Ask IOST to publish the vesting contract and beneficiaries | Free |
| 2 | **Vesting contract and beneficiaries** | A BscScan API plan or a BSC Arkham trace of the March 2025 mint destination | API plan |
| 3 | **Holder concentration on BSC** | BscScan token holders page | Free (manual) |
| 4 | **$3M buyback proof** | Ask IOST for the buyback wallet | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
