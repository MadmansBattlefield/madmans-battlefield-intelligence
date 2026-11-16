---
ticker: KAVA
name: Kava
chain: kava
contract: "native (ukava); BEP20 0x9bafc8d4b487cebff201721702507a3e2c67ad79"
overall_score: 3.1
overall_verdict: FAIL
section_scores:
  revenue: 1
  foundation_team: 4
  insider_holdings: 4
  selling_behavior: 5
  tokenomics_supply: 6
  liquidity_market: 4
  product_development: 2
  adoption_customers: 2
  security_audits: 1
  regulatory: 5
  catalysts: 2
gates_failed: [revenue]
red_lines:
  hack_exploit: "yes: HARD Lend exploit on 14 Nov 2026, ~53.9M KAVA (~$3.76M) drained and mostly sold on BNB Chain"
  mint_path_live: "no (on-chain inflation is 0%; supply 1,082,846,850 KAVA)"
  team_wallet_to_exchange_during_pump: "not tested (Kava Labs wallets are not published)"
  treasury_in_single_key_wallets: "no for the on-chain treasury (community pool and kavadist are module accounts); Kava Labs wallets unknown"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "The chain's fee-earning apps are being switched off; nothing reaches holders."
pump_day_price_source: "Gate KAVA/USDT daily closes"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions: []
price_usd: 0.02976698
price_source: "CoinGecko, 16 Nov 2026 8:34 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### KAVA · Overall grade **3.1 / 10 · ❌ FAIL**

**Summary:** Kava is a Cosmos/EVM Layer 1 whose own DeFi apps (Mint, Lend, Swap) are being **wound down by governance** (proposal 222, passed Oct 2026). On **14 Nov 2026 an attacker drained ~53.9M KAVA from HARD Lend** through a dormant BUSD market, bridged most of it to BNB Chain and sold it. KAVA fell up to ~59% that day and is **−57.6% over 7 days**. Inflation is 0% and supply is fixed at 1.08B, but there is no revenue, only **11.7% of supply is staked**, and the core repo was last pushed in Jan 2026. Revenue trips the hard gate.

**🚨 Top warning:** a live exploit on a chain in wind-down. Kava's [incident report (16 Nov 2026)](https://medium.com/@Kava_Chain/hard-lend-security-incident-579888f8dd73) confirms ~53.9M KAVA taken. The HARD Lend module account now holds [1,987 KAVA](https://kava-rest.publicnode.com/cosmos/bank/v1beta1/balances/kava1a42xtwfzphuuu9mdp0es6633wu5mm8fhm789v3/by_denom?denom=ukava), against 55.33M before the attack ([The Block](https://www.theblock.co/news/defi/2026-11-14-kava-lend-loses-roughly-3-8-million-to-hack-sending-kava-token-down-nearly-40-440350)). Upbit, Bithumb and Coinone paused deposits and withdrawals, and Axelar paused its bridge ([TokenPost](https://www.tokenpost.com/news/technology/57418)).

**Sections passed: 1 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 1/10 | ❌ FAIL |
| 🏛️ Foundation & team | 4/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 4/10 | ❌ FAIL |
| 📉 Selling behavior | 5/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 6/10 | ✅ PASS |
| 💧 Liquidity & market | 4/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 2/10 | ❌ FAIL |
| 🤝 Adoption & customers | 2/10 | ❌ FAIL |
| 🛡️ Security & audits | 1/10 | ❌ FAIL |
| ⚖️ Regulatory | 5/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 2/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 KAVA · Kava · 3.1 / 10 · ❌ FAIL

> **One line:** A chain shutting down its own DeFi apps, just hit by a $3.8M lending exploit, with fixed supply as its only strength.

| 📊 Market (CoinGecko, 16 Nov 2026 8:34 AM MST) | 🔗 On-chain (Kava LCD, 16 Nov 2026) |
|---|---|
| **Price** $0.02976698 | **Supply** 1,082,846,850 KAVA ([LCD](https://kava-rest.publicnode.com/cosmos/bank/v1beta1/supply/by_denom?denom=ukava)) |
| **24h / 7d / 30d** 🔴 −17.9% / −56.6% / −57.6% · 1y −77.5% | **Inflation** 0% ([LCD](https://kava-rest.publicnode.com/cosmos/mint/v1beta1/inflation)) |
| **Market cap** $31.86M · **FDV** $31.86M | **Bonded** 126.7M (11.7%) ([LCD](https://kava-rest.publicnode.com/cosmos/staking/v1beta1/pool)) |
| **24h volume** $9.84M (Upbit, Binance, Pionex) | **Community pool** 7.32M KAVA · **kavadist module** 37.75M KAVA |
| **ATH** $9.12 (30 Aug 2021) · now −99.7% | **Chain TVL** $13.84M ([DefiLlama chains](https://api.llama.fi/v2/chains)) |

---

## 💰 Revenue — Does it make money? · 1/10 · ❌ FAIL

| Metric | Value | Source |
|---|---:|---|
| Protocol fees / revenue | **Not tracked** on DefiLlama (no `kava` fee adapter) | [Tier A] DefiLlama |
| Native apps | Mint, Lend and Swap are in a governance-run wind-down; incentives ended and new borrowing stopped | [Tier A] [Proposal 222](https://kava-rest.publicnode.com/cosmos/gov/v1/proposals/222) |

**What it means:** The chain's own fee-earning apps are being switched off. **1, which trips the Revenue gate.**

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** The chain's fee-earning apps are being switched off; nothing reaches holders.

## 🏛️ Foundation & team — Who is in charge? · 4/10 · ❌ FAIL

- Kava Labs leads development. Governance runs through on-chain proposals: 215 (Phase 1 debt caps, May 2026), 221 (rejected, Aug 2026), 222 (Phase 2 wind-down, passed Oct 2026), plus monthly "Kava Rise" payouts ([gov LCD](https://kava-rest.publicnode.com/cosmos/gov/v1/proposals?pagination.reverse=true)).
- The core `Kava-Labs/kava` repo was last pushed on 23 Jan 2026 (GitHub API) [Tier A].
- The incident report came out two days after the hack, with a plan to permanently disable HARD Lend lending [Tier A].

## 🪙 Foundation / team holdings — How many coins do they hold? · 4/10 · ❌ FAIL

| Holder | KAVA | Notes |
|---|---:|---|
| Community pool (distribution module) `kava1jv65…splc` | 7.32M | Governance-controlled [Tier A LCD] |
| `kavadist` module `kava1cj7n…f0w` | 37.75M | Reward-distribution module [Tier A LCD] |
| Kava Labs / team | **Not found** | No published wallet list |

## 📉 Selling behavior — Do insiders sell into pumps? · 5/10 · ❌ FAIL

*Gate KAVA/USDT daily closes (UTC): 29 of the last 365 days were pump days.*

- **Not tested.** Kava Labs wallets are not published, and Cosmos accounts need an indexer to trace. The 48.4M KAVA dumped on BNB Chain on 15 Nov 2026 was the **attacker**, not an insider [Tier B ×2].

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from Gate KAVA/USDT daily closes.

## 📊 Tokenomics & supply · 6/10 · ✅ PASS

- 0% inflation and a fixed 1.0828B supply (Tier A LCD). No unlocks found.
- Risk: only 11.7% is bonded, so the validator set is thinly secured for a Proof-of-Stake chain.

## 💧 Liquidity & market · 4/10 · ❌ FAIL

- $9.8M of 24h volume on a $31.9M cap, but Korean exchanges paused deposits and withdrawals after the hack.
- −99.7% from ATH; −57.6% in 30 days.

## 🧑‍💻 Product & development · 2/10 · ❌ FAIL

- The native DeFi suite is being retired (Phases 1–3), and the core repo has been quiet since Jan 2026.

## 🤝 Adoption & customers · 2/10 · ❌ FAIL

- $13.8M chain TVL; HARD Lend has been emptied of KAVA.

## 🛡️ Security & audits · 1/10 · ❌ FAIL

- **14 Nov 2026:** an accounting flaw in HARD Lend's dormant BUSD market inflated collateral ~243,000×. The attacker borrowed KAVA 127 times, drained ~53.9M net, bridged 49.2M to BNB Chain via LayerZero and sold ~48.4M for ~$2.09M. Kava says the chain was not compromised, no KAVA was minted, and part of the funds is frozen ([incident report](https://medium.com/@Kava_Chain/hard-lend-security-incident-579888f8dd73) · [The Block](https://www.theblock.co/news/defi/2026-11-14-kava-lend-loses-roughly-3-8-million-to-hack-sending-kava-token-down-nearly-40-440350) · [Crypto Briefing](https://cryptobriefing.com/kava-hard-lend-wind-down-exploit/)).

## ⚖️ Regulatory · 5/10 · ❌ FAIL

- No enforcement action found. Kava says it is working with law enforcement on recovery.

## 📅 Catalysts & calendar · 2/10 · ❌ FAIL

| Date | Event |
|---|---|
| Late Nov 2026 | 7-day vote to permanently disable HARD Lend lending and borrowing |
| TBA | Phase 3 of the Mint/Lend/Swap wind-down; recovery of frozen funds |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🔴 HARD Lend, 14 Nov 2026, ~53.9M KAVA |
| Team wallet → exchange during a pump | 🟡 Not tested |
| Live mint path | 🟢 0% inflation |
| Treasury in single-key wallets | 🟢 On-chain treasury is module accounts; 🟡 Kava Labs unknown |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| Kava Labs wallets | Not published | — | low | no | Selling stays 5 (not tested) |

## 📚 Sources

- [Tier A] Methodology update 16 Nov 2026: no new Arkham lookups; the attribution table uses evidence already cited in this report.
- [Tier A] Kava LCD (publicnode): supply, inflation, staking pool, community pool, module balances, governance proposals; read 16 Nov 2026 ~9:00 AM MST
- [Tier A] [Kava incident report](https://medium.com/@Kava_Chain/hard-lend-security-incident-579888f8dd73); GitHub API for `Kava-Labs/kava`
- [Tier B] [The Block](https://www.theblock.co/news/defi/2026-11-14-kava-lend-loses-roughly-3-8-million-to-hack-sending-kava-token-down-nearly-40-440350) · [Crypto Briefing](https://cryptobriefing.com/kava-hard-lend-wind-down-exploit/) · [TokenPost](https://www.tokenpost.com/news/technology/57418) · [Block Insider](https://blockinsider.com/article/kava-s-3-7m-exploit-kava-says-chain-s-security-is-uncompromised)
- [Tier A] CoinGecko `kava` (16 Nov 2026 8:34 AM MST); Gate KAVA/USDT daily candles; DefiLlama chains TVL
- Arkham does not cover the Kava chain (16 Nov 2026), so none of the Kava wallets could be looked up; the attacker's BNB Chain address was not looked up
- [Unverified] Kava Labs holdings and sales; source of staking rewards at 0% inflation

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| HARD Lend drained of ~53.9M KAVA | [incident report](https://medium.com/@Kava_Chain/hard-lend-security-incident-579888f8dd73) · [hard module balance](https://kava-rest.publicnode.com/cosmos/bank/v1beta1/balances/kava1a42xtwfzphuuu9mdp0es6633wu5mm8fhm789v3/by_denom?denom=ukava) | A | 16 Nov 2026 |
| Wind-down of Mint/Lend/Swap | [Proposal 222](https://kava-rest.publicnode.com/cosmos/gov/v1/proposals/222) | A | 16 Nov 2026 |
| 0% inflation; supply 1.0828B; 11.7% bonded | [inflation](https://kava-rest.publicnode.com/cosmos/mint/v1beta1/inflation) · [supply](https://kava-rest.publicnode.com/cosmos/bank/v1beta1/supply/by_denom?denom=ukava) · [pool](https://kava-rest.publicnode.com/cosmos/staking/v1beta1/pool) | A | 16 Nov 2026 |
| Community pool 7.32M KAVA | [community pool](https://kava-rest.publicnode.com/cosmos/distribution/v1beta1/community_pool) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Who controls the large Kava wallets** | Arkham does not cover Kava. Ask Kava Labs for its wallet list and check Mintscan labels; the attacker's BNB Chain address from the incident report can be looked up on Arkham | Free |
| 2 | **Kava Labs wallets and exchange flows** | Ask Kava Labs; trace with Mintscan and pump-test | Free |
| 3 | **What funds staking rewards at 0% inflation?** | Read `kavadist` params and payouts | Free |
| 4 | **Recovery outcome** | Follow Kava's post-mortem and the HARD Lend disable vote | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
