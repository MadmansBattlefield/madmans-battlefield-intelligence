---
ticker: XRP
name: XRP
chain: xrp-ledger
contract: "native (XRP Ledger)"
overall_score: 5.1
overall_verdict: FAIL
section_scores:
  revenue: 2
  foundation_team: 6
  insider_holdings: 3
  selling_behavior: 4
  tokenomics_supply: 5
  liquidity_market: 10
  product_development: 7
  adoption_customers: 6
  security_audits: 7
  regulatory: 7
  catalysts: 5
gates_failed: [revenue]
red_lines:
  one_hop_sale_status: none_found
  hack_exploit: none
  ledger_halt: none_in_series
  ripple_ops_flow_on_pump_day: tripped_2_of_23
  ripple_sales_undisclosed: open
methodology_effective: 2026-11-16
revenue_reaches_holders: "yes"
revenue_mechanism: "Every transaction fee is burned automatically, but the amount is tiny (~$282k a year); Revenue stays 2."
pump_day_price_source: "Gate XRP_USDT UTC daily closes, re-run 16 Nov 2026 with scripts/pump_day_test.py (21 of 360 days); the body's earlier count used CoinGecko daily closes"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions: []
price_usd: 0.953837
price_source: "CoinGecko, 14 Nov 2026 12:12 PM MST"
chain_read_ledger: 108330736
last_updated: 2026-11-15
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### XRP · Overall grade **5.1 / 10 · ❌ FAIL**

**Summary:** A fast, cheap, long-running ledger, but the network collects only ~$282k a year in fees, Ripple still controls about a third of supply, and ~300M XRP a month leaves escrow into a Ripple chain of wallets whose final buyers are not disclosed.

**🚨 Top warning:** About **300M XRP a month** leaves Ripple's escrow into operational wallet [`rBg2…o91m`](https://xrpscan.com/account/rBg2FuZT91C52Nny68houguJ4vt5x1o91m), which sent **3.868B XRP to one wallet** [`rJqiMb…nE`](https://xrpscan.com/account/rJqiMb94hyz41SBTNr2AyPNW8AzELa8nE) in the last year, **2 of 23 sends on pump days** ([5 Jan 300M](https://xrpscan.com/tx/F2948835DAFF627ED8BFEC468BF705EC0D373806C2B6A0BC3BC96D02514804F8) · [6 Jul 150M](https://xrpscan.com/tx/F00C7180F72FB6A10D34F43E2D82363955DD0B4F08B7C73D7D3DA92A3900D80B)). The final buyers are not disclosed, and Arkham does not cover the XRP Ledger, so these wallets have no second label.

**Sections passed: 6 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 2/10 | ❌ FAIL |
| 🏛️ Foundation & team | 6/10 | ✅ PASS |
| 🪙 Foundation / team holdings | 3/10 | ❌ FAIL |
| 📉 Selling behavior | 4/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 5/10 | ❌ FAIL |
| 💧 Liquidity & market | 10/10 | ✅ PASS |
| 🧑‍💻 Product & development | 7/10 | ✅ PASS |
| 🤝 Adoption & customers | 6/10 | ✅ PASS |
| 🛡️ Security & audits | 7/10 | ✅ PASS |
| ⚖️ Regulatory | 7/10 | ✅ PASS |
| 📅 Catalysts & calendar | 5/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below. Overall fails the **Revenue gate** (2 ≤ 3).*

---


# 🪪 XRP · XRP · 5.1 / 10 · ❌ FAIL

> **One line:** A fast, cheap, long-running ledger, but the network collects only ~$282k a year in fees, Ripple still controls about a third of supply, and ~300M XRP a month leaves escrow into a Ripple chain of wallets whose final buyers are not disclosed.

ℹ️ **Adapted for a layer-1 with a dominant company.** "Revenue" = XRPL fees (all burned). Ripple's own business revenue does not flow to the token, so it is not counted. "Foundation" = Ripple Labs (largest holder and main developer) plus the XRPL Foundation. "Holdings / Selling" = Ripple escrow and operational wallets.

| 📊 Market (CoinGecko, 14 Nov 2026 12:12 PM MST) | 🔗 On-chain (XRPL, ledger 108,330,736) |
|---|---|
| **Price** $0.9538 | **Total coins** 99,985,552,195 (of 100B created) |
| **24h / 7d / 30d** 🔴 −6.8% / −17.8% / −28.8% | **Burned since genesis** 14,447,805 XRP |
| **Market cap** $60.63B · **FDV** $95.44B | **Circulating (CoinGecko)** 63.52B (63.5%) |
| **24h volume** $2.31B | **Base fee** 0.00001 XRP · **reserve** 1 XRP + 0.2 per object |
| **ATH** $3.65 (17 Jul 2025) · now −74% | **Server** rippled 3.4.1 |

---

## 💰 Revenue — Does it make money? · 2/10 · ❌ FAIL

| Metric | Value | Source |
|---|---:|---|
| 24h fees | $1,255 | [Tier A] DefiLlama `xrpl`, 14 Nov 2026 |
| 30-day fees | $43,003 | [Tier A] DefiLlama |
| 12-month fees | $282,342 | [Tier A] DefiLlama |
| All-time fees | $3,956,789 | [Tier A] DefiLlama |
| Where fees go | **100% burned** (no miners, no validator rewards) | [Tier A] XRPL docs |
| Lifetime burn | 14,447,805 XRP (0.014% of supply) | [Tier A] ledger `total_coins` |

**What it means:** XRP burns every fee, which is good design, but there is almost nothing to burn: ~$282k a year on a $60B asset. Ripple the company earns money from payments and custody; that does not flow to XRP holders.

- **Reaches holders (binary test, 16 Nov 2026 rules): Yes.** Every transaction fee is burned automatically, but the amount is tiny (~$282k a year); Revenue stays 2.

## 🏛️ Foundation & team — Who is in charge? · 6/10 · ✅ PASS

| Item | Finding | Source |
|---|---|---|
| Ripple Labs | US company; largest XRP holder; main contributor to rippled; CEO Brad Garlinghouse | [Tier A] ripple.com |
| XRPL Foundation / XRPLF | Maintains `XRPLF/rippled` — last push 13 Nov 2026, release 3.4.1 on 10 Oct 2026 | [Tier A] GitHub |
| Consensus | Federated: validators pick a Unique Node List; no protocol rewards to validators | [Tier A] XRPL docs |
| Ripple MiCA CASP authorization (Q3 2026) | Reported | [Unverified] one secondary summary |

**What it means:** The company is known and regulated, but one company dominates both development and supply.

## 🪙 Foundation / team holdings — How many coins do they hold? · 3/10 · ❌ FAIL

**Escrows read on-chain this pass (14 Nov 2026):**

| Ripple account | Escrow objects | XRP in escrow | Unlock dates | Spendable balance |
|---|---:|---:|---|---:|
| [`rB3WNZc45gxzW31zxfXdkx8HusAhoqscPn`](https://xrpscan.com/account/rB3WNZc45gxzW31zxfXdkx8HusAhoqscPn) | 12 | 4,000,000,000 | 1 Dec 2026 → 1 Jul 2027 | 500,000,235 |
| [`r9UUEXn3cx2seufBkDa8F86usfjWM6HiYp`](https://xrpscan.com/account/r9UUEXn3cx2seufBkDa8F86usfjWM6HiYp) | 12 | 4,000,000,000 | 1 Dec 2026 → 1 Jul 2027 | 500,000,220 |
| [`rU9qmGM4Y6WWDhiNzkwVKBwwatcoE7YL1T`](https://xrpscan.com/account/rU9qmGM4Y6WWDhiNzkwVKBwwatcoE7YL1T) | 5 | 1,600,000,000 | Apr → Jul 2029 | — |
| [`rNASJdZjY9dToHnNURi3HAUku3duPwbtD1`](https://xrpscan.com/account/rNASJdZjY9dToHnNURi3HAUku3duPwbtD1) | 5 | 1,500,000,000 | Apr → Jun 2029 | — |
| **Read this pass** | **34** | **11,100,000,000** | | |

| Bucket | XRP | % of supply | Source |
|---|---:|---:|---|
| All Ripple escrow (99 objects) | ~31.1B | ~31% | [Tier B] xrp-insights + Coinpaper (same tracker) — only 11.1B re-read here |
| Ripple operational wallets | ~5.1B | ~5% | [Unverified] Ripple Q3 2026 figure as relayed by secondary sites |
| Ripple total | ~36.8B | ~37% | [Unverified] |
| Founders (estimate) | ~4.6B | ~4.6% | [Unverified] |

**What it means:** Escrow is enforced by the ledger, so Ripple cannot take more than 1B a month out. Even so, a single company controls roughly a third of supply.

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL

**Pump test:** CoinGecko daily closes, 15 Nov 2025 – 14 Nov 2026: **20 of 361 days** were pump days. Last 26 Sep 2026 (+11.2%).

**Monthly escrow cycle (Tier A, on-chain):** on the 1st, 1B XRP is released (e.g. 1 Nov 2026 EscrowFinish [tx `3CB037A5…`](https://xrpscan.com/tx/3CB037A5F9BC193427592EDB87C49C1ABE499F80F5C049090141B4EDE539F948), [tx `33F693E7…`](https://xrpscan.com/tx/33F693E7C92AD6D7A127F55441C0B38A153E8F37092B7CE0235652FF326DE564)); the same day 700M is re-escrowed to 2029 (e.g. [tx `979F6504…`](https://xrpscan.com/tx/979F650441DDEC1516613AA054AF79B297EB59F92A42A384BB8B0CBCB9EB5B4C) 500M → [`rNASJd…`](https://xrpscan.com/account/rNASJdZjY9dToHnNURi3HAUku3duPwbtD1), re-locked by EscrowCreate [tx `71BB0841…`](https://xrpscan.com/tx/71BB08412E8A4746F1AA3E0737CDDADAB21DF7EF5B2F0CFB2FE95A09114A2E5F); [tx `D0F16959…`](https://xrpscan.com/tx/D0F16959C38F01F7C337596AC982F17319CFFA01EA1053F33EAA9C5DB3B54379) 200M → [`rU9qmG…`](https://xrpscan.com/account/rU9qmGM4Y6WWDhiNzkwVKBwwatcoE7YL1T)), and **300M** goes to operational wallet [`rBg2FuZT91C52Nny68houguJ4vt5x1o91m`](https://xrpscan.com/account/rBg2FuZT91C52Nny68houguJ4vt5x1o91m) ([tx `72755A8C…`](https://xrpscan.com/tx/72755A8CE0ECF4B947559906FC47C7AEC45880F29D9CFED83B73800C40296D1F)).

**Where that 300M/month went (rBg2… full scan, 15 Nov 2025 – 14 Nov 2026):**

| Item | Value |
|---|---:|
| Received | 3.600B XRP (12 monthly 300M lots) |
| Sent out | **3.868B XRP in 23 payments — all to one wallet, [`rJqiMb94hyz41SBTNr2AyPNW8AzELa8nE`](https://xrpscan.com/account/rJqiMb94hyz41SBTNr2AyPNW8AzELa8nE)** |
| Sent on pump days | **2 of 23: 5 Jan 2026 300M (5-day +11.8%, [tx `F2948835…`](https://xrpscan.com/tx/F2948835DAFF627ED8BFEC468BF705EC0D373806C2B6A0BC3BC96D02514804F8)) · 6 Jul 2026 150M (+11.4%, [tx `F00C7180…`](https://xrpscan.com/tx/F00C7180F72FB6A10D34F43E2D82363955DD0B4F08B7C73D7D3DA92A3900D80B))** |
| Latest sends | 2 Nov 2026 100M ([tx `60622733…`](https://xrpscan.com/tx/606227335E41D09DBC26768D74C3997DA8A0FAD08F19C5454F26A1EA13F1146F)) · 13 Nov 2026 200M ([tx `DFF5DA6F…`](https://xrpscan.com/tx/DFF5DA6F8CB8DF21063A8ABC2F1A7C529C09F67AA5CE2C67B208002F6E5D6849)) — not pump days |
| Balance now | 100,745,082 |

- `rJqiMb…` then paid out **1.014B XRP in 109 payments since 15 Aug 2026**, mostly to [`raRVLN1i5QFF6w8cwV3RovtTkjFj3qyNRf`](https://xrpscan.com/account/raRVLN1i5QFF6w8cwV3RovtTkjFj3qyNRf) (546M), [`rP4X2hTa7A7udDbE6wczXvPz7XZ63sKxv3`](https://xrpscan.com/account/rP4X2hTa7A7udDbE6wczXvPz7XZ63sKxv3) (320.8M) and [`rnU65s4J4ffJF5VtTEuHtEdWMKc1m9AR5J`](https://xrpscan.com/account/rnU65s4J4ffJF5VtTEuHtEdWMKc1m9AR5J) (99.9M). Balance now 251.8M. **Who those are (exchanges, OTC desks, customers) is not labeled** — [Unverified].
- Ripple's quarterly XRP sales figures: not found in a primary source this pass.
- **Arkham can't help here:** it does not cover the XRP Ledger. Its "Ripple" entity is Ethereum-only (mainly RLUSD; $136.66M of deposits in its window, ~80% Coinbase and ~19% OKX), so `rBg2…`, `rJqiMb…` and their downstream wallets **cannot be labelled or confirmed** from Arkham ([Tier B] Arkham, read 15 Nov 2026 ~11:00 AM MST (signed-in account)).

**What it means:** The release-and-distribute cycle is regular and mostly off-pump, but two large transfers landed on pump days and Ripple does not publish who the end buyers are. That is undisclosed insider distribution, so it fails — though not at the gate level.

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from Gate XRP_USDT UTC daily closes, re-run 16 Nov 2026 with scripts/pump_day_test.py (21 of 360 days); the body's earlier count used CoinGecko daily closes.

## 📊 Tokenomics & supply · 5/10 · ❌ FAIL

| Item | Value | Source |
|---|---|---|
| Max supply | 100B, all created at genesis; no minting possible | [Tier A] XRPL docs |
| Circulating | 63.52B (63.5%) | [Tier B] CoinGecko |
| Net new float | ~300M XRP/month (~3.6B/yr, ~5.7% of circulating) out of escrow | [Tier A] on-chain cycle |
| Re-escrow habit | 70% of each release re-locked for 12 straight months — voluntary, not code | [Tier A] chain · [Tier B] trackers |

## 💧 Liquidity & market · 10/10 · ✅ PASS

- $2.31B 24h volume; top-5 by market cap; global XRP ETPs took ~$355M net inflows in Q3 2026 [Unverified secondary summary].

## 🧑‍💻 Product & development · 7/10 · ✅ PASS

- rippled 3.4.1 live; native AMM/DEX; RLUSD stablecoin; Lending Protocol proposed (not live) [Tier A docs / GitHub].

## 🤝 Adoption & customers · 6/10 · ✅ PASS

- Ripple payments/custody customers exist, but on-ledger fee data (~$1.3k/day) shows modest paid usage. Evernorth treasury company expected to hold ~473M XRP [Unverified].

## 🛡️ Security & audits · 7/10 · ✅ PASS

- No ledger hack; no halt in this series. Brief past consensus stalls are known history. Kraken / Coinbase operational pauses are exchange issues, not ledger issues.

## ⚖️ Regulatory · 7/10 · ✅ PASS

- SEC v. Ripple litigation concluded in 2025 after both sides dropped appeals [Tier B]. Exchange and ETP listings in the US followed. Residual: Ripple's ongoing distribution is the main policy question.

## 📅 Catalysts & calendar · 5/10 · ❌ FAIL

| Date | Event | Effect |
|---|---|---|
| 1 Dec 2026 00:00 UTC | 1B XRP escrow release (4 objects, rB3WNZ… and r9UUEX…) | ~300M net new float if pattern holds |
| Monthly | Same cycle | Supply ↑ |
| TBD | XRPL Lending Protocol amendment | Product |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None |
| Ledger halt | 🟢 None in series |
| Ripple ops flow on a pump day | 🔴 Tripped 2 of 23 times ([5 Jan](https://xrpscan.com/tx/F2948835DAFF627ED8BFEC468BF705EC0D373806C2B6A0BC3BC96D02514804F8), [6 Jul 2026](https://xrpscan.com/tx/F00C7180F72FB6A10D34F43E2D82363955DD0B4F08B7C73D7D3DA92A3900D80B)) |
| Ripple end-buyer disclosure | 🟡 Open |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| Ripple operational accounts | Ripple | XRPL explorer + Ripple escrow reports | high | yes | Selling: two large transfers on pump days to undisclosed recipients, not proven exchange sales; stays 4 |

## 📚 Sources

- [Tier A] Methodology update 16 Nov 2026: no new Arkham lookups; the attribution table uses evidence already cited in this report.
- [Tier A] XRPL public API (`xrplcluster.com`): `ledger`, `server_info`, `account_info`, `account_objects` (escrow), `account_tx` for Ripple escrow owners, `rBg2…` and `rJqiMb…`; 14 Nov 2026 ~12:24 PM MST
- [Tier A] DefiLlama fees `xrpl`, 14 Nov 2026
- [Tier A] CoinGecko `ripple` price and 365-day daily closes, 14 Nov 2026 12:12 PM MST
- [Tier A] GitHub `XRPLF/rippled`
- [Tier B] [xrp-insights escrow tracker](https://xrp-insights.com/xrp-radar/escrow) · Coinpaper · CryptoTicker
- [Tier A] XRPScan account pages used: [`rB3WNZ…`](https://xrpscan.com/account/rB3WNZc45gxzW31zxfXdkx8HusAhoqscPn) · [`r9UUEX…`](https://xrpscan.com/account/r9UUEXn3cx2seufBkDa8F86usfjWM6HiYp) · [`rU9qmG…`](https://xrpscan.com/account/rU9qmGM4Y6WWDhiNzkwVKBwwatcoE7YL1T) · [`rNASJd…`](https://xrpscan.com/account/rNASJdZjY9dToHnNURi3HAUku3duPwbtD1) · [`rBg2…`](https://xrpscan.com/account/rBg2FuZT91C52Nny68houguJ4vt5x1o91m) · [`rJqiMb…`](https://xrpscan.com/account/rJqiMb94hyz41SBTNr2AyPNW8AzELa8nE) · [`raRVLN…`](https://xrpscan.com/account/raRVLN1i5QFF6w8cwV3RovtTkjFj3qyNRf) · [`rP4X2h…`](https://xrpscan.com/account/rP4X2hTa7A7udDbE6wczXvPz7XZ63sKxv3) · [`rnU65s…`](https://xrpscan.com/account/rnU65s4J4ffJF5VtTEuHtEdWMKc1m9AR5J) (full tx hashes re-read from `xrplcluster.com` `account_tx`, 15 Nov 2026 ~12:00 PM MST)
- [Tier B] Arkham, read 15 Nov 2026 ~11:00 AM MST (signed-in account): XRPL not supported; "Ripple" entity covers Ethereum (RLUSD) only. All-time exchange totals Enterprise-locked
- [Unverified] Ripple total / operational holdings; founders' holdings; MiCA authorization; ETP flows; Evernorth holdings; identities behind `rJqiMb…` downstream wallets

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer) or the label source (Arkham) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Monthly cycle: 1B XRP released from escrow on 1 Nov 2026 | [EscrowFinish 1](https://xrpscan.com/tx/3CB037A5F9BC193427592EDB87C49C1ABE499F80F5C049090141B4EDE539F948) · [EscrowFinish 2](https://xrpscan.com/tx/33F693E7C92AD6D7A127F55441C0B38A153E8F37092B7CE0235652FF326DE564) · [rB3WNZ…](https://xrpscan.com/account/rB3WNZc45gxzW31zxfXdkx8HusAhoqscPn) · [r9UUEX…](https://xrpscan.com/account/r9UUEXn3cx2seufBkDa8F86usfjWM6HiYp) | A | 15 Nov 2026 |
| 700M re-escrowed to 2029 the same day | [500M → rNASJd…](https://xrpscan.com/tx/979F650441DDEC1516613AA054AF79B297EB59F92A42A384BB8B0CBCB9EB5B4C) · [EscrowCreate 500M](https://xrpscan.com/tx/71BB08412E8A4746F1AA3E0737CDDADAB21DF7EF5B2F0CFB2FE95A09114A2E5F) · [200M → rU9qmG…](https://xrpscan.com/tx/D0F16959C38F01F7C337596AC982F17319CFFA01EA1053F33EAA9C5DB3B54379) | A | 15 Nov 2026 |
| **300M to operational wallet `rBg2…`** (1 Nov 2026) | [tx](https://xrpscan.com/tx/72755A8CE0ECF4B947559906FC47C7AEC45880F29D9CFED83B73800C40296D1F) · [rBg2… account](https://xrpscan.com/account/rBg2FuZT91C52Nny68houguJ4vt5x1o91m) | A | 15 Nov 2026 |
| **`rBg2…` sent 3.868B XRP in 23 payments, all to `rJqiMb…`**; 2 on pump days | [5 Jan 2026 300M (pump)](https://xrpscan.com/tx/F2948835DAFF627ED8BFEC468BF705EC0D373806C2B6A0BC3BC96D02514804F8) · [6 Jul 2026 150M (pump)](https://xrpscan.com/tx/F00C7180F72FB6A10D34F43E2D82363955DD0B4F08B7C73D7D3DA92A3900D80B) · [rJqiMb… account](https://xrpscan.com/account/rJqiMb94hyz41SBTNr2AyPNW8AzELa8nE) | A | 15 Nov 2026 |
| Latest sends `rBg2…` → `rJqiMb…` | [2 Nov 100M](https://xrpscan.com/tx/606227335E41D09DBC26768D74C3997DA8A0FAD08F19C5454F26A1EA13F1146F) · [13 Nov 200M](https://xrpscan.com/tx/DFF5DA6F8CB8DF21063A8ABC2F1A7C529C09F67AA5CE2C67B208002F6E5D6849) | A | 15 Nov 2026 |
| `rJqiMb…` paid out 1.014B XRP since 15 Aug 2026, mostly to three unlabeled accounts | [raRVLN…](https://xrpscan.com/account/raRVLN1i5QFF6w8cwV3RovtTkjFj3qyNRf) · [rP4X2h…](https://xrpscan.com/account/rP4X2hTa7A7udDbE6wczXvPz7XZ63sKxv3) · [rnU65s…](https://xrpscan.com/account/rnU65s4J4ffJF5VtTEuHtEdWMKc1m9AR5J) | A (owners [Unverified]) | 14 Nov 2026 |
| Arkham can't label XRPL wallets (no XRPL support) | Arkham entity read only; no address links possible | B | 15 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Who `rJqiMb…`'s downstream wallets are** (`raRVLN…`, `rP4X2h…`, `rnU65s…`) | XRPL-native label sources (XRPScan / Bithomp account names, exchange destination tags); check whether payments carry exchange destination tags | Free |
| 2 | **Confirm `rBg2…` and `rJqiMb…` are Ripple's** | Ripple's own disclosures or an XRPL explorer's verified account names (Arkham does not cover XRPL) | Free |
| 3 | **Ripple's quarterly XRP sales** | Ripple quarterly XRP Markets Reports, or filings if any | Free |
| 4 | **Ripple total / operational holdings** | Sum `account_info` for all escrow owners and known operational wallets | Free |
| 5 | **MiCA authorization; ETP flows** | ESMA register; ETP issuer holdings pages | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
