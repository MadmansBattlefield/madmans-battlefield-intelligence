---
ticker: ZEN
name: Horizen
chain: base
contract: "0xf43eb8de897fbc7f2502483b2bef7bb9ea179229"
overall_score: 3.7
overall_verdict: FAIL
section_scores:
  revenue: 1
  foundation_team: 5
  insider_holdings: 5
  selling_behavior: 4
  tokenomics_supply: 5
  liquidity_market: 5
  product_development: 3
  adoption_customers: 2
  security_audits: 5
  regulatory: 5
  catalysts: 5
gates_failed: [revenue]
red_lines:
  hack_exploit: "none found"
  mint_path_live: "no: all 21,000,000 ZEN already minted on Base; unvested Foundation/DAO tokens release monthly to mid-2029"
  team_wallet_to_exchange_during_pump: "not proven: Base wallet tracing was not available without a paid key; the Foundation discloses that it uses idle ZEN to 'support ZEN capital markets'"
  one_hop_sale_status: none_found
  entity_concentration: "Foundation (2M) + DAO (~3M) allocations ≈ 24% of max supply, vesting over 48 months from Jul 2025"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "No fee record; DAO yield on treasury liquidity is treasury income, not a holder mechanism."
pump_day_price_source: "MEXC ZENUSDT UTC daily closes, re-run 16 Nov 2026 with scripts/pump_day_test.py (45 of 360 days); the body's earlier count used CoinGecko daily closes"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions: []
price_usd: 4.09
price_source: "CoinGecko, 16 Nov 2026 ~8:40 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### ZEN · Overall grade **3.7 / 10 · ❌ FAIL**

**Summary:** Horizen started as a proof-of-work fork of Zcash with no premine. In Jul 2025 it moved ZEN to Base as an ERC20, adding Foundation and DAO allocations, and launched its own L3 chain. **The L3 was shut down on 5 Nov 2026**, and the DAO is now returning stranded balances on Base. No product currently earns fees, so the revenue gate fails. A three-year roadmap (a compliant privacy pool and confidential compute) has not yet been voted on.

**🚨 Top warning:** the product chain is gone. Horizen's own post says "Horizen L3 decommissioning was completed on Nov 5". Funds left on it are being returned by the DAO "after funds are made recoverable" ([Horizen blog](https://blog.horizen.io/changes-for-horizen)). The token now has no live chain of its own. The Foundation also says it uses idle ZEN "to support ZEN capital markets" ([Blockworks filing](https://blockworks.com/token-transparency/filing/horizen/8a6c87ba-3995-4cfb-a3d0-2daef84cd1b4)), so it may be selling into the market, but those flows were not traced. Every link is in the 🔗 Evidence trail below.

**Sections passed: 0 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 1/10 | ❌ FAIL (hard gate) |
| 🏛️ Foundation & team | 5/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 5/10 | ❌ FAIL |
| 📉 Selling behavior | 4/10 | ❌ FAIL (not proven) |
| 📊 Tokenomics & supply | 5/10 | ❌ FAIL |
| 💧 Liquidity & market | 5/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 3/10 | ❌ FAIL |
| 🤝 Adoption & customers | 2/10 | ❌ FAIL |
| 🛡️ Security & audits | 5/10 | ❌ FAIL |
| ⚖️ Regulatory | 5/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 5/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 ZEN · Horizen · 3.7 / 10 · ❌ FAIL

> **One line:** A fair-launch coin that has lost its chain twice (PoW, then the L3) and now earns nothing.

| 📊 Market (CoinGecko, 16 Nov 2026 ~8:40 AM MST) | 🔗 On-chain (Base RPC `totalSupply`, 16 Nov 2026 ~8:55 AM MST) |
|---|---|
| **Price** $4.09 | **Total supply on Base** 21,000,000 ZEN (all minted) |
| **24h / 7d / 30d** 🔴 −0.5% / −18.9% / −31.7% | **Circulating** 18.48M (CoinGecko) |
| **Market cap** $75.6M · **FDV** $85.9M | **Foundation** 2M total: 500k at migration, rest monthly over 48 months |
| **24h volume** $4.76M (HTX $0.82M, Binance $0.68M, WhiteBIT $1.03M, Hotcoin, Aerodrome) | **DAO** ~3M total: 750k at migration, rest monthly over 48 months |
| **ATH** $165.92 (7 May 2021) · now −97.5% | **Horizen L3** shut down 5 Nov 2026 |
| **Pump days** 47 in the last year (largest +50.3% on 23 Aug 2026) | |

---

## 💰 Revenue — Does it make money? · 1/10 · ❌ FAIL (hard gate)

- No fee or revenue record exists on DefiLlama, and the L3, the only chain that could earn fees, is shut down. The DAO earns yield on treasury liquidity positions, but that is treasury income, not protocol revenue. **1 → hard-gate FAIL.**

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** No fee record; DAO yield on treasury liquidity is treasury income, not a holder mechanism.

## 🏛️ Foundation & team — Who is in charge? · 5/10 · ❌ FAIL

- Horizen Foundation plus a DAO with a Special Council. Disclosure is good (a token transparency filing), but the team's main product has just been shut down.

## 🪙 Foundation / team holdings — How many coins do they hold? · 5/10 · ❌ FAIL

- Per zenIP 42407: the Foundation gets 2M ZEN and the DAO about 3M, each with 25% at the Jul 2025 migration and the rest monthly over 48 months. The filing says no core team members are paid in these tokens. There was no founder or ICO allocation at the 2017 launch.

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL (not proven)

- The Foundation and DAO wallets are on Base. I couldn't trace them: Base explorer APIs need a paid key or blocked automated reads. The Foundation openly says it deploys idle ZEN "to support ZEN capital markets", and the DAO runs automated LP strategies. Both would sell into rallies by design. Arkham ([Tier B] Arkham, read 16 Nov 2026 (signed-in account)) shows [`0xf43e…9229`](https://intel.arkm.com/explorer/address/0xf43eb8de897fbc7f2502483b2bef7bb9ea179229) is the **ZenToken contract itself** (692 ZEN of stray deposits), not a Foundation or DAO wallet, so those wallets are still not identified. **Not proven → 4.**

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from MEXC ZENUSDT UTC daily closes, re-run 16 Nov 2026 with scripts/pump_day_test.py (45 of 360 days); the body's earlier count used CoinGecko daily closes.

## 📊 Tokenomics & supply · 5/10 · ❌ FAIL

- Hard-capped at 21M and fully minted. About 2.5M ZEN (12%) is still to vest through mid-2029, which works out to roughly 0.6%–0.7% of supply a year.

## 💧 Liquidity & market · 5/10 · ❌ FAIL

- $4.76M of 24h volume (6.3% of market cap), with no single venue above $1.1M.

## 🧑‍💻 Product & development · 3/10 · ❌ FAIL

- The L3 has been decommissioned. ZEN staking is to be redeployed on Base, and the roadmap is still a proposal.

## 🤝 Adoption & customers · 2/10 · ❌ FAIL

- No live product usage to measure.

## 🛡️ Security & audits · 5/10 · ❌ FAIL

- No exploit found. Users who missed the bridge deadline have to rely on a DAO-run recovery and redistribution of their funds.

## ⚖️ Regulatory · 5/10 · ❌ FAIL

- Privacy positioning ("compliant privacy pool"). No enforcement found.

## 📅 Catalysts & calendar · 5/10 · ❌ FAIL

| Date | Event |
|---|---|
| From ~15 Nov 2026 | DAO returns L3 balances on Base |
| Not dated | ZEN staking relaunch on Base; three-year roadmap vote |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | ⚪ Not proven (disclosed market support) |
| Live mint path | 🟢 None (fully minted) |
| Entity concentration | 🟡 ~24% of max supply, vesting |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| Foundation and DAO wallets on Base | Horizen Foundation / DAO | Project statements | medium | no | Selling stays 4 (not traced) |

## 📚 Sources

- [Tier A] Methodology update 16 Nov 2026: no new Arkham lookups; the attribution table uses evidence already cited in this report.
- [Tier A] [Horizen blog: Changes for Horizen](https://blog.horizen.io/changes-for-horizen) (L3 shutdown and recovery)
- [Tier A] [Horizen blog: ZEN's move to Base](https://blog.horizen.io/get-ready-for-zen-s-big-move-to-base) (contract, supply changes)
- [Tier B] [Blockworks token transparency filing](https://blockworks.com/token-transparency/filing/horizen/8a6c87ba-3995-4cfb-a3d0-2daef84cd1b4) (vesting, market support)
- [Tier A] Base public RPC `totalSupply` for the ZEN contract (21,000,000)
- [Tier A] CoinGecko `zencash`; pump days from Binance ZENUSDT daily closes
- Not reached: Base wallet histories (paid key required). Arkham (Arkham, read 16 Nov 2026 (signed-in account)) was run only on the Base token contract, which it labels Horizen (ZEN); no Foundation or DAO wallet was identified

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| L3 decommissioned 5 Nov 2026 | [Horizen blog](https://blog.horizen.io/changes-for-horizen) | A | 16 Nov 2026 |
| ZEN on Base, 21M supply | [BaseScan token](https://basescan.org/token/0xf43eb8de897fbc7f2502483b2bef7bb9ea179229), [migration post](https://blog.horizen.io/get-ready-for-zen-s-big-move-to-base) | A | 16 Nov 2026 |
| Foundation supports ZEN capital markets | [Blockworks filing](https://blockworks.com/token-transparency/filing/horizen/8a6c87ba-3995-4cfb-a3d0-2daef84cd1b4) | B | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Foundation and DAO wallet flows on pump days** | Get the treasury addresses from the project's transparency page, and trace them on BaseScan with a key, or in Arkham (Base is supported) | Paid key / free account |
| 2 | **Roadmap vote** | Watch the Horizen DAO forum | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.

- Research only. Not investment advice.
