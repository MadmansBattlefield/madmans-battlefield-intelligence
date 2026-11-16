---
ticker: XNO
name: Nano
chain: nano
contract: "native coin (no contract)"
overall_score: 4.9
overall_verdict: FAIL
section_scores:
  revenue: 1
  foundation_team: 4
  insider_holdings: 8
  selling_behavior: 6
  tokenomics_supply: 9
  liquidity_market: 4
  product_development: 6
  adoption_customers: 4
  security_audits: 6
  regulatory: 7
  catalysts: 4
gates_failed: [revenue]
red_lines:
  hack_exploit: "none at protocol level found in the last year"
  mint_path_live: "no: fixed 133,248,297 XNO, fully distributed"
  team_wallet_to_exchange_during_pump: "no in the last year: the 2019 developer-fund accounts are empty; their last moves (Oct-Nov 2023) went to a high-traffic account that looks like an exchange hot wallet [Unverified]"
  one_hop_sale_status: none_found
  entity_concentration: "none known: developer-fund accounts hold ~10 XNO"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "Nano charges no fees, so there is no burn, buyback, staking yield or fee share, and nothing reaches holders."
pump_day_price_source: "Binance XNOUSDT UTC daily closes"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions: []
price_usd: 0.284071
price_source: "CoinGecko, 16 Nov 2026 ~9:45 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### XNO · Overall grade **4.9 / 10 · ❌ FAIL**

**Summary:** Nano is a feeless block-lattice payments coin. Almost all of its 133M fixed supply was given away through a free faucet from 2015 to 2017. There was no ICO and no venture round. The foundation's 7M XNO developer fund is now essentially spent: the published fund accounts hold about 10 XNO. So no insider supply remains to sell, and supply can't grow. But the network collects no fees at all, development depends on a small foundation with a finite budget, and trading volume is under $0.5M a day. The revenue gate fails.

**🚨 Top warning:** **no revenue and a finite budget**. Nano charges no fees and has no treasury income, mining or staking rewards. Its development depends on a nearly spent developer fund and a small group of contributors led by one dominant core developer ([Digital Gold Foundation CFV report](https://www.digitalgoldfoundation.org/reports/xno), [nano.org 2026 round-up](https://nano.org/blog/nano-ecosystem-round-up-of-2026-so-far)). Every link is in the 🔗 Evidence trail below.

**Sections passed: 6 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 1/10 | ❌ FAIL (hard gate) |
| 🏛️ Foundation & team | 4/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 8/10 | ✅ PASS |
| 📉 Selling behavior | 6/10 | ✅ PASS |
| 📊 Tokenomics & supply | 9/10 | ✅ PASS |
| 💧 Liquidity & market | 4/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 6/10 | ✅ PASS |
| 🤝 Adoption & customers | 4/10 | ❌ FAIL |
| 🛡️ Security & audits | 6/10 | ✅ PASS |
| ⚖️ Regulatory | 7/10 | ✅ PASS |
| 📅 Catalysts & calendar | 4/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 XNO · Nano · 4.9 / 10 · ❌ FAIL

> **One line:** A fair-distributed, fixed-supply, feeless coin with no insiders left to sell, but no revenue either.

| 📊 Market (CoinGecko, 16 Nov 2026 ~9:45 AM MST) | 🔗 Chain (Nano public node RPC) |
|---|---|
| **Price** $0.2841 | **Supply** 133,248,297 XNO, fixed and fully distributed |
| **24h / 7d / 30d** 🔴 −6.4% / 🔴 −14.0% / 🔴 −14.3% | **Fees** none (ever) |
| **Market cap** $37.9M · **FDV** $37.9M | **Developer fund** 31 published accounts hold ~10 XNO in total |
| **24h volume** $0.48M (Binance $260k, Kraken USD $87k, Kraken EUR, Bit2Me, KuCoin, Gate) | **Consensus** Open Representative Voting |
| **ATH** $33.69 (1 Jan 2018) · now −99.2% | |
| **Pump days** 17 in the last year (Binance XNOUSDT; largest +48.3% on 20 Jul 2026) | |

---

## 💰 Revenue — Does it make money? · 1/10 · ❌ FAIL (hard gate)

- Nano charges no fees, so there's no protocol revenue, treasury income or holder value capture. "Not a single network fee has been paid" ([nano.org](https://nano.org/blog/nano-ecosystem-round-up-of-2026-so-far)). **1 → hard-gate FAIL.**

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** Nano charges no fees, so there is no burn, buyback, staking yield or fee share, and nothing reaches holders.

## 🏛️ Foundation & team — Who is in charge? · 4/10 · ❌ FAIL

- The Nano Foundation and a small group of contributors work on a finite fund, and one core developer does most of the work ([CFV report](https://www.digitalgoldfoundation.org/reports/xno)). V28.2 is live and V29 is in progress ([nano.org](https://nano.org/blog/nano-ecosystem-round-up-of-2026-so-far)).

## 🪙 Foundation / team holdings — How many coins do they hold? · 8/10 · ✅ PASS

- 126.2M XNO went out through the faucet and 7M went to the developer fund. No ICO, VC or private sale ([CFV report](https://www.digitalgoldfoundation.org/reports/xno)). I checked all 31 developer-fund accounts listed in 2019 ([foundation announcement](https://blog.nano.org/announcement-changes-to-nano-foundation-development-fund-account-43f8f340a841)) on a public node: together they hold about 10 XNO.

## 📉 Selling behavior — Do insiders sell into pumps? · 6/10 · ✅ PASS

- None of the fund accounts moved anything in the last year. In Oct–Nov 2023, the last 50,000-XNO lots moved through single-use accounts into `nano_3cpz…xsaaf`. That account behaves like an exchange hot wallet [Unverified], and in Sep–Oct 2025 it forwarded 2.26M XNO to another high-traffic account. All of this is outside the one-year window. No insider supply is left to test → **6** (in line with ETC).

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from Binance XNOUSDT UTC daily closes.

## 📊 Tokenomics & supply · 9/10 · ✅ PASS

- Fixed 133.2M supply with no issuance.

## 💧 Liquidity & market · 4/10 · ❌ FAIL

- $0.48M a day on Binance and Kraken. Thin, but on major venues.

## 🧑‍💻 Product & development · 6/10 · ✅ PASS

- Instant, feeless payments that work; node V28.2; x402 agent-payment tooling launched in 2026 ([nano.org](https://nano.org/blog/nano-ecosystem-round-up-of-2026-so-far)).

## 🤝 Adoption & customers · 4/10 · ❌ FAIL

- Activity is real but hard to measure because transactions are free (the CFV report estimates $1.2B a year) [Unverified: one source].

## 🛡️ Security & audits · 6/10 · ✅ PASS

- No protocol exploit found in the last year. Feeless design has made it a spam target before [Unverified].

## ⚖️ Regulatory · 7/10 · ✅ PASS

- No ICO and faucet distribution, so issuer-sale risk is low.

## 📅 Catalysts & calendar · 4/10 · ❌ FAIL

- V29 node release and x402 integrations.

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found in the last year |
| Team wallet → exchange during a pump | 🟢 None in the last year (fund empty) |
| Live mint path | 🟢 None (fixed supply) |
| Entity concentration | 🟢 None known |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| `nano_3cpz…xsaaf` | Unlabelled; behaves like an exchange hot wallet [Unverified] | Public node history | low | no | None (outside the window) |

## 📚 Sources

- [Tier B] Arkham, read 16 Nov 2026 (signed-in account): not used: Arkham does not cover the Nano chain, so the developer-fund trail rests on the public node
- [Tier A] [Nano Foundation dev-fund announcement (2019 account list)](https://blog.nano.org/announcement-changes-to-nano-foundation-development-fund-account-43f8f340a841), [nano.org 2026 round-up](https://nano.org/blog/nano-ecosystem-round-up-of-2026-so-far)
- [Tier A] Nano public node RPC (`account_balance`, `account_history`) for all 31 listed accounts
- [Tier B] [Digital Gold Foundation CFV report, Mar 2026](https://www.digitalgoldfoundation.org/reports/xno)
- [Tier A] CoinGecko `nano` (market, venues); pump days from Binance XNOUSDT daily closes

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Dev-fund accounts hold ~10 XNO | Nano RPC on the 31 accounts in the [2019 list](https://blog.nano.org/announcement-changes-to-nano-foundation-development-fund-account-43f8f340a841) | A | 16 Nov 2026 |
| Fixed supply, no fees | [nano.org](https://nano.org/blog/nano-ecosystem-round-up-of-2026-so-far), [CFV](https://www.digitalgoldfoundation.org/reports/xno) | A+B | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Who owns `nano_3cpz…xsaaf`** (2023 dev-fund sink) | Known-account lists (nanolooker was down); Arkham does not cover the Nano chain (16 Nov 2026) | Free |
| 2 | **Current developer fund (community-run) balance** | Ask the fund operator | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.

- Research only. Not investment advice.
