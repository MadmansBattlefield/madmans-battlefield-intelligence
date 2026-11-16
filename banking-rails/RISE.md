---
ticker: RISE
name: T-RIZE (RIZE token; listed here as T-RISE / Rise)
chain: base
contract: "0x9818b6c09f5ecc843060927e8587c427c7c93583"
overall_score: 3.8
overall_verdict: FAIL
section_scores:
  revenue: 2
  foundation_team: 6
  insider_holdings: 3
  selling_behavior: 4
  tokenomics_supply: 4
  liquidity_market: 3
  product_development: 5
  adoption_customers: 3
  security_audits: 6
  regulatory: 5
  catalysts: 5
gates_failed: [revenue]
red_lines:
  hack_exploit: "none found; the issuer's filing reports no token exploits"
  mint_path_live: "no; 5B fixed supply"
  team_wallet_to_exchange_during_pump: "not proven: the disclosed Operations2 wallet sent 2.6M RIZE to a MEXC deposit, but not on a pump day; 75M moved to unlabelled wallets that weren't traced"
  one_hop_sale_status: none_found
  entity_concentration: "deployer-created vesting contracts hold ~2.38B (48%); two unlabelled project-funded wallets hold 700M more"
price_usd: 0.00304956
price_source: "CoinGecko `rize`, 16 Nov 2026 ~1:30 PM MST"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "none; T-RIZE Group keeps its tokenization service revenue, and the filing says holders have no rights over fees, buybacks or treasury"
pump_day_price_source: "MEXC RIZEUSDT daily closes (UTC); Binance unavailable (451), Gate has no RIZE pair (HTTP 400), MEXC is next in the hierarchy"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions:
  - address: "0x9525df984b7062c7c0fb103bc745467396241e7b"
    label: "Governance allocation (VestingWallet)"
    confidence: high
    independent_corroboration: true
    basis: "Basescan: created by T-RIZE: Deployer; listed as the Governance wallet in the Blockworks token transparency filing"
  - address: "0x08f326ac9192d92584d33d1b2560c4460291643b"
    label: "Operations2 (Fireblocks MPC)"
    confidence: high
    independent_corroboration: true
    basis: "listed in the Blockworks filing; Basescan shows its transfers"
  - address: "0x0151988326ded907853c7b75641d6a7897959510"
    label: "Partnership & Growth (UnallocatedVesting)"
    confidence: high
    independent_corroboration: true
    basis: "listed in the Blockworks filing; created by T-RIZE: Deployer"
  - address: "0x7adc57d2ffd3521d4a68d83a8e40d32971472f87"
    label: "MEXC Dep"
    confidence: medium
    independent_corroboration: false
    basis: "Basescan name tag only"
  - address: "0xc7a60e8b130cce51b7f489fd8b7fcf25141430cc"
    label: "unlabelled 500M holder"
    confidence: low
    independent_corroboration: false
    basis: "gas funded by the same wallet that funded T-RIZE: Deployer; no label"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### RISE · Overall grade **3.8 / 10 · ❌ FAIL**

**Summary:** The repo lists this as "T-RISE / Rise", but the token is RIZE, from T-RIZE Group, a Montréal company that structures tokenized assets on the Canton Network. A Cayman foundation (CarbonZero) holds the token reserves. The company keeps its service revenue, and its own disclosure says holders have no rights over fees, buybacks or the treasury. Deployer-created vesting contracts hold ~48% of supply. A disclosed operations wallet sent 2.6M RIZE to MEXC, not on pump days, and larger moves to unlabelled wallets weren't traced. RIZE is down 97% from its Jul 2025 peak. The revenue gate fails.

**🚨 Top warning:** **about half the supply sits in project vesting contracts, and the operations wallet feeds MEXC.** The Basescan-tagged **T-RIZE: Deployer** created contracts holding ~2.38B RIZE, including the 1.5B Governance vesting wallet [`0x9525…1e7b`](https://basescan.org/address/0x9525df984b7062c7c0fb103bc745467396241e7b). The disclosed Operations2 wallet [`0x08f3…643b`](https://basescan.org/address/0x08f326ac9192d92584d33d1b2560c4460291643b) sent 2.6M RIZE to a Basescan-tagged MEXC deposit, e.g. [2.5M on 23 Oct 2026](https://basescan.org/tx/0xba8b6b0059d27a8c738f57d01c464732eec09728420153f5ae1942f5ae696d73). It also sent 75M to unlabelled wallets in Jun and Nov 2026. Every link is in the 🔗 Evidence trail below.

**Sections passed: 2 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 2/10 | ❌ FAIL (hard gate) |
| 🏛️ Foundation & team | 6/10 | ✅ PASS |
| 🪙 Foundation / team holdings | 3/10 | ❌ FAIL |
| 📉 Selling behavior | 4/10 | ❌ FAIL (not proven) |
| 📊 Tokenomics & supply | 4/10 | ❌ FAIL |
| 💧 Liquidity & market | 3/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 5/10 | ❌ FAIL |
| 🤝 Adoption & customers | 3/10 | ❌ FAIL |
| 🛡️ Security & audits | 6/10 | ✅ PASS |
| ⚖️ Regulatory | 5/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 5/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 RISE · T-RIZE (RIZE token; listed here as T-RISE / Rise) · 3.8 / 10 · ❌ FAIL

> **One line:** A real tokenization company whose utility token has no claim on revenue and a 48% vesting overhang.

| 📊 Market (CoinGecko, 16 Nov 2026 ~1:30 PM MST) | 🔗 Chain (Basescan) |
|---|---|
| **Price** $0.00305 | **Supply** 2.07B circulating / 5B |
| **24h / 7d / 30d** 🟢 +36.1% / 🔴 −10.4% / 🔴 −35.2% | **Governance vesting** 1.5B (30%) |
| **Market cap** $6.31M · **FDV** $15.2M | **Governance Bonding** 895M · **Unallocated vestings** 400M, 250M, 227M |
| **24h volume** ~$85.7k (Aerodrome ~$44.6k, MEXC $39.0k, PancakeSwap $2.1k) | **Unlabelled** 500M and 200M (project-funded) |
| **ATH** $0.0980 (21 Jul 2025) · now −96.9% | |
| **Pump days** 56 in the last year (MEXC RIZEUSDT; largest +212.6% on 24 Jun 2026) | |

---

## 💰 Revenue — Does it make money? · 2/10 · ❌ FAIL (hard gate)

- T-RIZE Group earns fees for structuring and tokenizing assets. The [Blockworks token transparency filing](https://blockworks.com/token-transparency/filing/rize) says holders have no rights over "treasury actions, fee-routing, rewards, buybacks", and no repurchases have happened. RIZE is a utility and access token.

**What it means:** the token has no claim on revenue. **Holder test: no.** **2 → hard-gate FAIL.**

## 🏛️ Foundation & team — Who is in charge? · 6/10 · ✅ PASS

- T-RIZE Group Corporation (Canada) is the developer. CarbonZero Foundation Company (Cayman) holds the token reserves. Key staff are named in the filing; described here by role. The company is a Canton Foundation member ([site](https://www.t-rize.io/)).

## 🪙 Foundation / team holdings — How many coins do they hold? · 3/10 · ❌ FAIL

- **Insider-controlled contracts** (created by the Basescan-tagged **T-RIZE: Deployer** [`0x1829…a885`](https://basescan.org/address/0x1829a3f35f4ef621f410e2c487499a8e933da885)): Governance vesting [`0x9525…1e7b`](https://basescan.org/address/0x9525df984b7062c7c0fb103bc745467396241e7b) **1.5B**; unallocated vestings [`0xad12…5f2d`](https://basescan.org/address/0xad12b1421d14130633700af043445115d16f5f2d) 400M and [`0x6d59…11eb`](https://basescan.org/address/0x6d596a1d2c317f39029ee7ccea3fe1d6460811eb) 250M; Partnership & Growth [`0x0151…9510`](https://basescan.org/address/0x0151988326ded907853c7b75641d6a7897959510) 227M. That is **~2.38B (48%)**.
- **Attribution confidence:** high. The creator tag is on-chain proof, and the issuer's filing lists the same wallets.
- [`0xc7a6…30cc`](https://basescan.org/address/0xc7a60e8b130cce51b7f489fd8b7fcf25141430cc) (500M) and [`0x5adf…f9f4`](https://basescan.org/address/0x5adfc1a01f03c81c027fb2f0f5e4bac04ca9f9f4) (200M) are unlabelled. Their gas came from [`0x978f…e3b8`](https://basescan.org/address/0x978fb0e41ea2b7e6c96427cbab9131df3976e3b8), which also funded the deployer. That is low confidence, so they don't move this score. Score 3.

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL (not proven)

- **Disclosed Operations2** [`0x08f3…643b`](https://basescan.org/address/0x08f326ac9192d92584d33d1b2560c4460291643b) → Basescan-tagged **MEXC Dep** [`0x7adc…2f87`](https://basescan.org/address/0x7adc57d2ffd3521d4a68d83a8e40d32971472f87): 2.5M on 23 Oct 2026 ([tx](https://basescan.org/tx/0xba8b6b0059d27a8c738f57d01c464732eec09728420153f5ae1942f5ae696d73)), 100k on 4 Sep ([tx](https://basescan.org/tx/0xb91b90f2929f4a39171d056fa0005a4f39d96d9661acb9f1b520c06bd1c864fb)) and 6k on 7 Jul ([tx](https://basescan.org/tx/0x9eb44d4268f1fa482f67be0650f7b03539006faba2cd7bf6319d0fb63d36ec44)). That's ~$11k in all, and not on a pump day. All three have status 1.
- Operations2 also sent **25M on 5 Jun 2026** ([tx](https://basescan.org/tx/0xf6659b925fc3ee77be0414695fbef9db72d3f2386c9ba6bb2c12b01a631862e3)) and **2 × 25M on 4 Nov 2026** ([tx 1](https://basescan.org/tx/0x57fab5be69dc493c47a8a980b761a2cf25f718be6a3320a2d752b51f76de470e), [tx 2](https://basescan.org/tx/0x4d08295aa467717b318cdf5a070ca6bc7ff0e610601049eb7993a7dd021be718)) to unlabelled wallets. Those weren't traced further: Basescan's API needs a paid key, and its per-wallet transfer pages were read one hop only.
- **Attribution confidence:** sender high (disclosed wallet); MEXC deposit medium (one tag). **Not proven → 4.** **Disclosure quality:** not applicable (no pump-day sale found). The filing says no market-maker or listing allocations exist.

## 📊 Tokenomics & supply · 4/10 · ❌ FAIL

- 5B fixed supply; 2.07B circulating. Governance (30%) vests over 36 months after a 12-month cliff, but the 1.5B wallet hasn't moved. Team (14%) has a 24-month cliff ending ~Apr 2027 ([filing](https://blockworks.com/token-transparency/filing/rize)).

## 💧 Liquidity & market · 3/10 · ❌ FAIL

- ~$86k a day, split between Aerodrome and MEXC. The foundation runs ~$50k of protocol-owned liquidity through Arrakis.

## 🧑‍💻 Product & development · 5/10 · ❌ FAIL

- Tokenization infrastructure on Canton, Chainlink CCIP integration (Oct 2026) and a structured private-credit programme of up to $500M ([CCIP news](https://www.t-rize.io/news/T-RIZE-Integrates-Chainlink-CCIP-on-Canton)).

## 🤝 Adoption & customers · 3/10 · ❌ FAIL

- Real institutional deals, but on-chain use of RIZE is mostly trading and bonding.

## 🛡️ Security & audits · 6/10 · ✅ PASS

- Verified contracts; the filing reports no exploits.

## ⚖️ Regulatory · 5/10 · ❌ FAIL

- Canadian company and Cayman foundation; no enforcement found.

## 📅 Catalysts & calendar · 5/10 · ❌ FAIL

- Team cliff ends ~Apr 2027; exchange listings (Kraken, Revolut, Bitpanda, MEXC).

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | ⚪ Not proven: MEXC deposits not on pump days; large moves untraced |
| Live mint path | 🟢 None |
| Entity concentration | 🔴 ~48% in deployer-created vesting contracts |

## 📚 Sources

- [Tier A] [Blockworks token transparency filing (issuer-submitted)](https://blockworks.com/token-transparency/filing/rize), [T-RIZE site](https://www.t-rize.io/)
- [Tier A] Basescan: holders, contract creators, address tags and transfers (linked above)
- [Tier A] CoinGecko `rize` (market, venues); pump days from MEXC RIZEUSDT daily closes (UTC), per the price-source hierarchy (Gate has no pair)

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Governance vesting 1.5B created by T-RIZE: Deployer | [`0x9525…1e7b`](https://basescan.org/address/0x9525df984b7062c7c0fb103bc745467396241e7b) | A | 16 Nov 2026 |
| Operations2 → MEXC deposit | [2.5M, 23 Oct 2026](https://basescan.org/tx/0xba8b6b0059d27a8c738f57d01c464732eec09728420153f5ae1942f5ae696d73) | A | 16 Nov 2026 |
| Operations2 → unlabelled 2 × 25M | [tx 1](https://basescan.org/tx/0x57fab5be69dc493c47a8a980b761a2cf25f718be6a3320a2d752b51f76de470e) · [tx 2](https://basescan.org/tx/0x4d08295aa467717b318cdf5a070ca6bc7ff0e610601049eb7993a7dd021be718) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Where the 75M from Operations2 went** | Trace the 5 Jun and 4 Nov recipients onward | Arkham (no lookup yet), or a paid Basescan key |
| 2 | **Who controls the 500M and 200M wallets** | Arkham entity view of [`0xc7a6…30cc`](https://basescan.org/address/0xc7a60e8b130cce51b7f489fd8b7fcf25141430cc) and [`0x5adf…f9f4`](https://basescan.org/address/0x5adfc1a01f03c81c027fb2f0f5e4bac04ca9f9f4) | Arkham |
| 3 | **Fix the repo ticker** | Rename RISE → RIZE in ALL-PROJECTS.md | Integrator |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.

- Research only. Not investment advice.
