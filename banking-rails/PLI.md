---
ticker: PLI
name: Plugin
chain: xdc-network
contract: "xdcff7412ea7c8445c46a8254dfb557ac1e48094391"
overall_score: 2.8
overall_verdict: FAIL
section_scores:
  revenue: 1
  foundation_team: 4
  insider_holdings: 3
  selling_behavior: 4
  tokenomics_supply: 3
  liquidity_market: 2
  product_development: 4
  adoption_customers: 2
  security_audits: 4
  regulatory: 5
  catalysts: 2
gates_failed: [revenue]
red_lines:
  hack_exploit: "none found in this pass"
  team_wallet_to_exchange_during_pump: "not tested: no Gate, MEXC, KuCoin or Kraken series; insider wallets unpublished"
  one_hop_sale_status: none_found
price_usd: 0.00180969
price_source: "CoinGecko `plugin`, 16 Nov 2026 ~3:00 PM MST"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "Oracle fees go to the node operator serving the request; staking rewards are paid in PLI from allocations, not from fees. Nothing is burned or shared with holders."
pump_day_price_source: "not run (no Gate, MEXC, KuCoin or Kraken USDT series)"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions: []
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### PLI · Overall grade **2.8 / 10 · ❌ FAIL**

**Summary:** Plugin is an oracle network on the XDC chain. Data consumers pay node operators small PLI fees per request, and validators earn staking rewards of 3.5% a month (about 42% a year) since 1 Jun 2026. Those rewards are paid in PLI, not funded by fees, so they dilute holders. No fee or revenue record on DefiLlama and none published by the project was found. The Revenue gate fails.

**🚨 Top warning:** **Staking rewards of ~42% a year are paid in PLI, not from revenue.** Founders and promoters hold 18% and the foundation 30% under the published allocation; their wallets are not published.

**Sections passed: 0 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 1/10 | ❌ FAIL (hard gate) |
| 🏛️ Foundation & team | 4/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 3/10 | ❌ FAIL |
| 📉 Selling behavior | 4/10 | ❌ FAIL (not proven) |
| 📊 Tokenomics & supply | 3/10 | ❌ FAIL |
| 💧 Liquidity & market | 2/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 4/10 | ❌ FAIL |
| 🤝 Adoption & customers | 2/10 | ❌ FAIL |
| 🛡️ Security & audits | 4/10 | ❌ FAIL |
| ⚖️ Regulatory | 5/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 2/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 PLI · Plugin · 2.8 / 10 · ❌ FAIL

> **One line:** An XDC oracle whose high staking yield is token issuance, not revenue.

| 📊 Market (CoinGecko `plugin`, 16 Nov 2026 ~3:00 PM MST) | 🔗 Chain |
|---|---|
| **Price** $0.00181 | **Supply** 500M, all counted as circulating |
| **7d / 30d / 1y** 🟢 +4.1% / 🔴 −37.7% / 🔴 −80.1% | **XDC token** `xdcff74…4391` |
| **Market cap** $905k · **FDV** $905k | **Holders** not read (no XDC indexer used) |
| **24h volume** $13.3k (top venues: Bitrue $12.4k, XSwap Protocol V3 $505, XSwap $423) |  |
| **ATH** $0.972 (2021-11-10) |  |
| **Pump days** not tested: no Gate, MEXC or KuCoin USDT series |  |

---

## 💰 Revenue — Does it make money? · 1/10 · ❌ FAIL (hard gate)

- No fee or revenue record on DefiLlama and none published by the project was found.
- Per the [docs](https://docs.plugin.global/plugin-data-feeds-platform/benefits), consumers pay ~0.01–0.1 PLI per request to the node operator. Validator rewards are 3.5% a month on stake ([rewards](https://docs.plugin.global/plugin-2.0-validators/job-setup/rewards-information)).

**What it means:** Fees pay operators for a service; nothing reaches holders. **1 → hard-gate FAIL.**

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** Oracle fees go to the node operator serving the request; staking rewards are paid in PLI from allocations, not from fees. Nothing is burned or shared with holders.

## 🏛️ Foundation & team — Who is in charge? · 4/10 · ❌ FAIL

- Plugin ([site](https://goplugin.co/)); code at [github.com/goplugin](https://github.com/goplugin).

## 🪙 Foundation / team holdings — How many coins do they hold? · 3/10 · ❌ FAIL

- Published allocation ([Tokenomics.com](https://app.tokenomics.com/tokenomics/plugin), Tier B): founders and promoters 18%, core team 2%, foundation 30%, community 50%. Wallets not published, so the holding cannot be checked. **3**.

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL (not proven)

- The only CEX market is Bitrue, outside the Gate → MEXC → KuCoin → Kraken hierarchy, so the pump test was not run. No insider wallet is published. No Arkham pass was run.

**What it means:** Not proven → **4**.

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from not run (no Gate, MEXC, KuCoin or Kraken USDT series).

## 📊 Tokenomics & supply · 3/10 · ❌ FAIL

- 500M fixed supply, but 3.5% a month validator rewards come out of the allocations, so float rises steadily.

## 💧 Liquidity & market · 2/10 · ❌ FAIL

- ~$13k a day: Bitrue ~$12k and XSwap ~$0.9k.

## 🧑‍💻 Product & development · 4/10 · ❌ FAIL

- Data-feed and validator platforms are live per the docs; GitHub activity was not measured.

## 🤝 Adoption & customers · 2/10 · ❌ FAIL

- No count of paying data-feed consumers was found.

## 🛡️ Security & audits · 4/10 · ❌ FAIL

- No exploit found; no audit located.

## ⚖️ Regulatory · 5/10 · ❌ FAIL

- No enforcement found.

## 📅 Catalysts & calendar · 2/10 · ❌ FAIL

- None verified.

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | ⚪ Not tested: no exchange series in the hierarchy; wallets unpublished |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. No Arkham pass was run for this report, so every attribution that rests on an unlabelled wallet is low confidence. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| — | — | — | — | — | — |

## 📚 Sources

- [Tier A] [CoinGecko `plugin`](https://www.coingecko.com/en/coins/plugin): price, supply, venues and description, read 16 Nov 2026
- [Tier A] `scripts/pump_day_test.py`: no Gate, MEXC, KuCoin or Kraken USDT series returned on 16 Nov 2026

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Market data and venues | [CoinGecko `plugin`](https://www.coingecko.com/en/coins/plugin) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Insider wallets** | Ask Plugin for the founder, team and foundation wallets on XDC | Free |
| 2 | **Holder list** | Read the XDC explorer holder list for the PLI token | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior. Under the 16 Nov 2026 one-hop amendment, a transfer to an exchange counts as a sale only with a team-attributed exchange account, evidence of a sale, or no plausible published reason.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.

- Research only. Not investment advice.
