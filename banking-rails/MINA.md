---
ticker: MINA
name: Mina Protocol
chain: mina
contract: "native"
overall_score: 4.0
overall_verdict: FAIL
section_scores:
  revenue: 1
  foundation_team: 5
  insider_holdings: 5
  selling_behavior: 5
  tokenomics_supply: 5
  liquidity_market: 4
  product_development: 6
  adoption_customers: 2
  security_audits: 6
  regulatory: 5
  catalysts: 4
gates_failed: [revenue]
red_lines:
  hack_exploit: "none found"
  mint_path_live: "yes, protocol coinbase (no cap; ~3% a year observed, 7% long-run target)"
  team_wallet_to_exchange_during_pump: "not testable (foundation holds via custodians; no published wallets)"
  treasury_in_single_key_wallets: "unknown (custodied)"
methodology_2026_11_16:
  revenue_reaches_holders: "no"
  disclosure_quality: not_applicable
  pump_day_undisclosed_penalty_applied: false
  pump_day_price_source: "Gate MINA_USDT UTC daily closes"
  dual_review: not_run
price_usd: 0.04621846
price_source: "CoinGecko, 16 Nov 2026 9:11 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### MINA · Overall grade **4.0 / 10 · ❌ FAIL**

**Summary:** Mina is a succinct-blockchain layer 1 built around zk-proofs and zkApps. The Mesa upgrade went live in Sep 2026 (90-second slots, halved coinbase). Usage is thin. A full day of mainnet (290 blocks, 16 Nov 2026) carried **563 user transactions, zero zkApp transactions and 17.3 MINA (~$0.80) of fees**. DefiLlama tracks no Mina fees or TVL. Supply has no cap: **1,310,246,125 MINA** on-chain, with coinbase issuance running at about 3% a year. Disclosure is unusually good: the Mina Foundation publishes quarterly balances, 24.33M MINA treasury and 52.21M MINA grants at 31 Mar 2026 ([Q1 2026 report](https://www.minafoundation.com/reports/q1-2026-transparency-report)). Revenue trips the hard gate.

**🚨 Top warning:** No fee economy. Validators are paid almost entirely from new issuance; ~104,400 MINA were minted in the sample day against 17.3 MINA of fees. The foundation has handed its operations to the developer company o1Labs, and the planned 55M-MINA Decentralized Treasury has no guaranteed size or date [Tier A]. The price is −64% in a year and −99.5% from ATH.

**Sections passed: 2 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 1/10 | ❌ FAIL |
| 🏛️ Foundation & team | 5/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 5/10 | ❌ FAIL |
| 📉 Selling behavior | 5/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 5/10 | ❌ FAIL |
| 💧 Liquidity & market | 4/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 6/10 | ✅ PASS |
| 🤝 Adoption & customers | 2/10 | ❌ FAIL |
| 🛡️ Security & audits | 6/10 | ✅ PASS |
| ⚖️ Regulatory | 5/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 4/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 MINA · Mina Protocol · 4.0 / 10 · ❌ FAIL

> **One line:** Serious zk engineering and good disclosure, but essentially no on-chain demand.

| 📊 Market (CoinGecko, 16 Nov 2026 9:11 AM MST) | 🔗 On-chain (Mina GraphQL, 16 Nov 2026) |
|---|---|
| **Price** $0.0462 · 24h / 7d / 30d 🔴 +1.6% / −12.2% / −38.8% · 1y −63.9% | **Total currency** 1,310,246,125 MINA · no cap |
| **Market cap** $59.8M · rank #360 | **Height** 572,954 · last 290 blocks span 23.3 h |
| **24h volume** $2.91M: HTX $0.71M, WhiteBIT $0.41M, LBank $0.38M, OKX $0.23M, Binance $0.21M | **Last day** 563 user tx, 0 zkApp tx, 17.3 MINA fees |
| **ATH** $9.09 (31 May 2021) · now −99.5% | **Coinbase** 104,400 MINA/day ≈ 3.0% a year |

---

## 💰 Revenue — Does it make money? · 1/10 · ❌ FAIL

| Metric | Value | Source |
|---|---:|---|
| Fees, last 290 blocks (23.3 h) | 17.33 MINA (~$0.80) | [Tier A] Mina GraphQL `bestChain` (api.minascan.io) |
| User / zkApp transactions | 563 / 0 | same |
| DefiLlama fees / TVL | Not listed | [Tier A] api.llama.fi |

**What it means:** no revenue. **1 (hard gate).**

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** Validators are paid from new issuance; fees are tiny and there is no fee burn, buyback or fee share, so revenue does not reach holders.

## 🏛️ Foundation & team — Who is in charge? · 5/10 · ❌ FAIL

- Mina Foundation (Swiss) transferred engineering, marketing, grants and delegation to o1Labs, a US Delaware company; the scaled-down foundation now works only on the Decentralized Treasury ([Q1 2026 report](https://www.minafoundation.com/reports/q1-2026-transparency-report), Tier A; [Blockworks filing](https://blockworks.com/token-transparency/filing/mina-protocol), Tier B).
- The quarterly transparency reports are a plus.

## 🪙 Foundation / team holdings — How many coins do they hold? · 5/10 · ❌ FAIL

| Holder | MINA | Source |
|---|---:|---|
| Mina Foundation treasury | 24,330,000 | [Tier A] [Q1 2026 report](https://www.minafoundation.com/reports/q1-2026-transparency-report) (31 Mar 2026) |
| Mina Foundation grants | 52,210,000 | same |
| o1Labs, early backers | Not disclosed | — |

- All genesis, backer and contributor allocations are fully unlocked [Tier B, Blockworks filing].
- Foundation MINA (76.5M) is ~5.8% of supply. The foundation also held $18.2M of USD and stablecoins.

## 📉 Selling behavior — Do insiders sell into pumps? · 5/10 · ❌ FAIL

*Gate MINA/USDT daily closes (UTC): 44 pump days in the last 365.*

- Foundation MINA is held with custodians and no wallets are published, so a pump-day test is not possible.
- The foundation reports **buying** MINA with fiat through non-US service providers, capped at 2% of daily volume. In Q1 2026 it booked $4.37M of OTC proceeds (including the sale of its 65 BTC) and a 3M-MINA "Proceeds Liquidity Program" line [Tier A].

**What it means:** untestable; disclosed flows lean toward buying. **5**.

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from Gate MINA_USDT UTC daily closes.

## 📊 Tokenomics & supply · 5/10 · ❌ FAIL

- No cap. The original design targets 12% inflation falling to 7% ([economics white paper](https://minaprotocol.com/wp-content/uploads/economicsWhitepaper.pdf), Tier A).
- Observed coinbase is ~3.0% of supply a year, because only ~31% of slots produced blocks in the sample and Mesa halved the coinbase ([Mesa docs](https://docs.minaprotocol.com/network-upgrades/mesa), Tier A).

## 💧 Liquidity & market · 4/10 · ❌ FAIL

- $2.91M of 24h volume on a $59.8M cap (4.9%), spread across HTX, WhiteBIT, LBank, OKX and Binance.
- −99.5% from ATH.

## 🧑‍💻 Product & development · 6/10 · ✅ PASS

- Mesa hard fork live (Sep 2026); next upgrade being scoped ([o1Labs blog](https://minaprotocol.com/blog/welcome-to-mesa), Tier A). The Decentralized Treasury passed zkSecurity and Trail of Bits audits [Tier A].

## 🤝 Adoption & customers · 2/10 · ❌ FAIL

- 563 user transactions and no zkApp transactions in a full day. Almost no live application usage.

## 🛡️ Security & audits · 6/10 · ✅ PASS

- No chain exploit found. Treasury contracts audited by two firms (Q1 2026 report).

## ⚖️ Regulatory · 5/10 · ❌ FAIL

- The Swiss foundation is engaging with its supervisory authority over the treasury allocation; o1Labs is a US company. No enforcement found.

## 📅 Catalysts & calendar · 4/10 · ❌ FAIL

| Date | Event |
|---|---|
| Unscheduled | Decentralized Treasury launch (target 55M MINA) |
| Unscheduled | Post-Mesa upgrade |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | 🟡 Not testable |
| Live mint path | 🟡 Protocol issuance ~3% a year, no cap |
| Treasury in single-key wallets | 🟡 Unknown (custodied) |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| No foundation addresses published | — | Arkham does not cover the Mina chain | — | — | None |

## 📚 Sources

- [Tier B] Arkham, read 16 Nov 2026 (signed-in account): no Mina-chain coverage and no published foundation addresses, so nothing to attribute
- [Tier A] Mina GraphQL `bestChain` at api.minascan.io (290 blocks), latest block 16 Nov 2026 9:04 AM MST
- [Tier A] [Mina Foundation Q1 2026 report](https://www.minafoundation.com/reports/q1-2026-transparency-report) · [Mesa docs](https://docs.minaprotocol.com/network-upgrades/mesa) · [Welcome to Mesa](https://minaprotocol.com/blog/welcome-to-mesa) · [economics white paper](https://minaprotocol.com/wp-content/uploads/economicsWhitepaper.pdf)
- [Tier B] [Blockworks token transparency filing](https://blockworks.com/token-transparency/filing/mina-protocol)
- [Tier A] CoinGecko `mina-protocol` (16 Nov 2026 9:11 AM MST); DefiLlama; Gate MINA/USDT daily candles

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Foundation MINA balances | [Q1 2026 report](https://www.minafoundation.com/reports/q1-2026-transparency-report) | A | 16 Nov 2026 |
| Mesa halved slot time and coinbase | [docs](https://docs.minaprotocol.com/network-upgrades/mesa) | A | 16 Nov 2026 |
| Near-zero fees and zkApp usage | Mina GraphQL `bestChain(maxLength:290)` (no per-claim explorer link) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Foundation custody addresses** | The foundation publishes no wallet addresses, and Arkham does not cover the Mina chain (16 Nov 2026). Ask the Mina Foundation to publish them | Free |
| 2 | **Foundation and o1Labs wallets** | Ask for custody addresses, or look up the largest Mina accounts on Minascan | Free |
| 3 | **30-day fee income** | Repeat the GraphQL fee sum over 30 days | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
