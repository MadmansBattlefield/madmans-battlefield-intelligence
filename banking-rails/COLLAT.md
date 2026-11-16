---
ticker: COLLAT
name: Collaterize
chain: solana
contract: "C7heQqfNzdMbUFQwcHkL9FvdwsFsDRBnfwZDDyWYCLTZ"
overall_score: 3.8
overall_verdict: FAIL
section_scores:
  revenue: 3
  foundation_team: 4
  insider_holdings: 4
  selling_behavior: 4
  tokenomics_supply: 6
  liquidity_market: 3
  product_development: 5
  adoption_customers: 3
  security_audits: 4
  regulatory: 4
  catalysts: 3
gates_failed: [revenue]
red_lines:
  hack_exploit: "none found in this pass"
  team_wallet_to_exchange_during_pump: "not tested: no Gate, MEXC, KuCoin or Kraken series; dev wallet unpublished"
  one_hop_sale_status: none_found
price_usd: 0.00055959
price_source: "CoinGecko `collaterize`, 16 Nov 2026 ~3:00 PM MST"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "Described: stakers get 80% of protocol trading fees in SOL, 3.75 of a 5% graduation fee buys back COLLAT, and vote-lockers share some fund fees. No distribution or buyback was verified on-chain, so the binary test is scored No until it is shown."
pump_day_price_source: "not run (no Gate, MEXC, KuCoin or Kraken USDT series)"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions: []
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### COLLAT · Overall grade **3.8 / 10 · ❌ FAIL**

**Summary:** Collaterize is a Solana real-world-asset launchpad and app. COLLAT launched on 30 Jan 2025 as a fair launch with the full ~1B supply circulating (10% held for development, vesting). The project describes stakers receiving 80% of protocol trading fees in SOL and buybacks from graduation fees, and vote-lockers sharing some fund fees. But no fee totals or on-chain distributions are published, so the holder test is unproven. Trading is ~$52k a day, almost all on KCEX. The Revenue gate fails.

**🚨 Top warning:** **The fee-share is described but not shown:** no fee totals, buyback transactions or staker payouts are published. About 97% of volume is on one small exchange (KCEX).

**Sections passed: 1 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 3/10 | ❌ FAIL (hard gate) |
| 🏛️ Foundation & team | 4/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 4/10 | ❌ FAIL |
| 📉 Selling behavior | 4/10 | ❌ FAIL (not proven) |
| 📊 Tokenomics & supply | 6/10 | ✅ PASS |
| 💧 Liquidity & market | 3/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 5/10 | ❌ FAIL |
| 🤝 Adoption & customers | 3/10 | ❌ FAIL |
| 🛡️ Security & audits | 4/10 | ❌ FAIL |
| ⚖️ Regulatory | 4/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 3/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 COLLAT · Collaterize · 3.8 / 10 · ❌ FAIL

> **One line:** A small Solana RWA launchpad promising fee-sharing it has not yet shown on-chain.

| 📊 Market (CoinGecko `collaterize`, 16 Nov 2026 ~3:00 PM MST) | 🔗 Chain |
|---|---|
| **Price** $0.00056 | **Supply** ~1B, fully circulating |
| **7d / 30d / 1y** 🔴 −18.8% / 🔴 −16.4% / 🔴 −91.8% | **Solana SPL** `C7heQq…YCLTZ` |
| **Market cap** $560k · **FDV** $560k | **Holders** ~12k (CoinMarketCap) [Tier B] |
| **24h volume** $51.7k (top venues: KCEX $50k, Raydium $1.77k) | **Holder list** not read (no Solana indexer key) |
| **ATH** $0.0897 (2025-05-25) |  |
| **Pump days** not tested: no Gate, MEXC or KuCoin USDT series |  |

---

## 💰 Revenue — Does it make money? · 3/10 · ❌ FAIL (hard gate)

- No fee or revenue record on DefiLlama and none published by the project was found.
- Fee design per [Solana Compass](https://solanacompass.com/projects/collaterize) [Tier B]: a 2% trading fee in SOL split issuer 1%, stakers 0.8%, protocol 0.2%; a 5% graduation fee, of which 3.75% buys back COLLAT. The [vote-locking guide](https://medium.com/@collaterize_gov/stake-collat-how-to-earn-and-track-step-by-step-guide-ed2e507dc1fd) (8 Oct 2026) says DTF fee rewards depend on each fund's settings.

**What it means:** A holder mechanism is described but not shown, and no fee volume is published. **3 → hard-gate FAIL.**

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** Described: stakers get 80% of protocol trading fees in SOL, 3.75 of a 5% graduation fee buys back COLLAT, and vote-lockers share some fund fees. No distribution or buyback was verified on-chain, so the binary test is scored No until it is shown.

## 🏛️ Foundation & team — Who is in charge? · 4/10 · ❌ FAIL

- Collaterize ([site](https://collaterize.com/)); the operating company and team were not verified in this pass [Unverified].

## 🪙 Foundation / team holdings — How many coins do they hold? · 4/10 · ❌ FAIL

- 10% of supply is described as a vesting development wallet; its address is not published. Not proven → **4**.

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL (not proven)

- No Gate, MEXC, KuCoin or Kraken series exists (main venue KCEX), so the pump test was not run. The development wallet is not published. No Arkham pass was run.

**What it means:** Not proven → **4**.

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from not run (no Gate, MEXC, KuCoin or Kraken USDT series).

## 📊 Tokenomics & supply · 6/10 · ✅ PASS

- ~1B supply, fully circulating since TGE; market cap equals FDV, so there is no unlock overhang beyond the 10% dev wallet's vesting.

## 💧 Liquidity & market · 3/10 · ❌ FAIL

- ~$52k a day: KCEX ~$50k and Raydium ~$1.8k. Concentrated on a single small exchange.

## 🧑‍💻 Product & development · 5/10 · ❌ FAIL

- Mobile app, bonding-curve launchpad and DTF funds are described as live [Tier B].

## 🤝 Adoption & customers · 3/10 · ❌ FAIL

- ~12k holders (CoinMarketCap); no launch or fee volume published.

## 🛡️ Security & audits · 4/10 · ❌ FAIL

- CertiK rating 3.1 shown on CoinMarketCap [Tier B]; no exploit found.

## ⚖️ Regulatory · 4/10 · ❌ FAIL

- Tokenized real-estate and fund offerings to retail may need securities licensing; none verified.

## 📅 Catalysts & calendar · 3/10 · ❌ FAIL

- More asset launches; publication of fee and buyback data.

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | ⚪ Not tested: no exchange series in the hierarchy; dev wallet unpublished |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. No Arkham pass was run for this report, so every attribution that rests on an unlabelled wallet is low confidence. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| — | — | — | — | — | — |

## 📚 Sources

- [Tier A] [CoinGecko `collaterize`](https://www.coingecko.com/en/coins/collaterize): price, supply, venues and description, read 16 Nov 2026
- [Tier A] `scripts/pump_day_test.py`: no Gate, MEXC, KuCoin or Kraken USDT series returned on 16 Nov 2026

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Market data and venues | [CoinGecko `collaterize`](https://www.coingecko.com/en/coins/collaterize) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Fee distributions** | Find the staker-payout and buyback transactions on Solscan | Free |
| 2 | **Dev wallet** | Ask Collaterize for the 10% development wallet address and vesting contract | Free |
| 3 | **Top holders** | Read the Solscan holder list | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior. Under the 16 Nov 2026 one-hop amendment, a transfer to an exchange counts as a sale only with a team-attributed exchange account, evidence of a sale, or no plausible published reason.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.

- Research only. Not investment advice.
