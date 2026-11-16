---
ticker: TFUEL
name: Theta Fuel
chain: theta
contract: "native gas token of the Theta blockchain"
overall_score: 4.0
overall_verdict: FAIL
section_scores:
  revenue: 2
  foundation_team: 5
  insider_holdings: 4
  selling_behavior: 4
  tokenomics_supply: 3
  liquidity_market: 5
  product_development: 6
  adoption_customers: 3
  security_audits: 6
  regulatory: 6
  catalysts: 4
gates_failed: [revenue]
red_lines:
  hack_exploit: "none found"
  mint_path_live: "yes by design: protocol-set annual TFUEL issuance to stakers and edge nodes (supply 5.0B at genesis, 7.53B now)"
  team_wallet_to_exchange_during_pump: "not proven: no TFUEL account is publicly attributed to the developer company"
  entity_concentration: "largest account holds 935.9M (12.4%), unlabelled"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "Customer revenue is converted into TFUEL to pay node operators, not holders, and no total is published."
pump_day_price_source: "Gate TFUEL_USDT UTC daily closes, re-run 16 Nov 2026 with scripts/pump_day_test.py (12 of 360 days); the body's earlier count used the daily closes cited in the body"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions: []
price_usd: 0.006976
price_source: "CoinGecko, 16 Nov 2026 ~8:40 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### TFUEL · Overall grade **4.0 / 10 · ❌ FAIL**

**Summary:** TFUEL is the gas and payment token of the Theta blockchain. It pays network fees and pays node operators on Theta EdgeCloud, a GPU compute service. Supply grows every year by protocol design, from 5.0B at genesis to **7.53B today (+51%)**. All gas fees and at least 25% of edge-network payments are burned, but no burn totals, EdgeCloud revenue or paid-job counts are published. That fails the revenue gate. Three quarters of trading volume is on one Korean exchange.

**🚨 Top warning:** issuance keeps running with no proven demand. TFUEL supply is **7,532,022,689** ([Theta explorer API](https://explorer-api.thetatoken.org/api/supply/tfuel)) and keeps rising each year. The project describes EdgeCloud revenue being converted into TFUEL for operators, but no revenue or burn figures are published to show that demand offsets new supply. The largest account (**935.9M, 12.4%**) is unlabelled. Every link is in the 🔗 Evidence trail below.

**Sections passed: 3 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 2/10 | ❌ FAIL (hard gate) |
| 🏛️ Foundation & team | 5/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 4/10 | ❌ FAIL |
| 📉 Selling behavior | 4/10 | ❌ FAIL (not proven) |
| 📊 Tokenomics & supply | 3/10 | ❌ FAIL |
| 💧 Liquidity & market | 5/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 6/10 | ✅ PASS |
| 🤝 Adoption & customers | 3/10 | ❌ FAIL |
| 🛡️ Security & audits | 6/10 | ✅ PASS |
| ⚖️ Regulatory | 6/10 | ✅ PASS |
| 📅 Catalysts & calendar | 4/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 TFUEL · Theta Fuel · 4.0 / 10 · ❌ FAIL

> **One line:** An inflationary gas token whose GPU-cloud demand story has no published numbers behind it.

| 📊 Market (CoinGecko, 16 Nov 2026 ~8:40 AM MST) | 🔗 On-chain ([Theta explorer API](https://explorer-api.thetatoken.org/api/supply/tfuel), 16 Nov 2026 ~8:45 AM MST) |
|---|---|
| **Price** $0.006976 | **Supply** 7,532,022,689 TFUEL (all circulating) |
| **24h / 7d / 30d** 🟢 +3.8% / 🔴 −7.8% / −22.0% | **Genesis supply** 5.0B (2019) |
| **Market cap** $52.5M · **FDV** $52.5M | **Largest account** 935.9M (12.4%), unlabelled |
| **24h volume** $7.0M (Upbit $5.27M, Binance $0.77M, Pionex $0.39M, Bithumb $0.34M) | **Binance-held addresses** 300.0M + 257.9M |
| **ATH** $0.6816 (8 Jun 2021) · now −99.0% | **Burn** 100% of gas and ≥25% of edge payments (totals not published) |
| **Pump days** 11 in the last year (largest +22.9% on 23 Aug 2026) | |

---

## 💰 Revenue — Does it make money? · 2/10 · ❌ FAIL (hard gate)

- DefiLlama has no fee or revenue record. The project says EdgeCloud customers pay in fiat or stablecoins and the revenue is converted into TFUEL to pay node operators ([Theta blog](https://blog.thetatoken.org/why-edgecloud-drives-tfuel-and-theta-value/)). It publishes no revenue, job counts or burn totals. **2 → hard-gate FAIL.**

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** Customer revenue is converted into TFUEL to pay node operators, not holders, and no total is published.

## 🏛️ Foundation & team — Who is in charge? · 5/10 · ❌ FAIL

- Theta Labs, a US company, develops the chain. The validator set includes enterprise validators. Leaders are described by role only, and no audited accounts are public.

## 🪙 Foundation / team holdings — How many coins do they hold? · 4/10 · ❌ FAIL

| Account | TFUEL | % | Label |
|---|---:|---:|---|
| [0xffcf…61d9](https://explorer.thetatoken.org/account/0xffcf02555c27325db5a406d96689246f6d4661d9) | 935.9M | 12.4% | None |
| 0xf977…acec | 300.0M | 4.0% | Same address as Binance's labelled cold wallet on Ethereum |
| 0x5a52…efcb | 257.9M | 3.4% | Same address as a Binance cold wallet on Ethereum |
| [0xd551…d9f8](https://explorer.thetatoken.org/account/0xd551fd014d98edf6362c0c4e141dd7331888d9f8) | 233.4M | 3.1% | None; 82k+ transactions (likely an operational wallet) |

- The developer company's TFUEL holdings are not disclosed.

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL (not proven)

- No TFUEL account is publicly attributed to Theta Labs, so pump-day flows (11 in the last year) could not be checked. **Not proven → 4.**

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from Gate TFUEL_USDT UTC daily closes, re-run 16 Nov 2026 with scripts/pump_day_test.py (12 of 360 days); the body's earlier count used the daily closes cited in the body.

## 📊 Tokenomics & supply · 3/10 · ❌ FAIL

- Supply is uncapped by design, with protocol-set annual issuance plus edge-node rewards, offset by burns. Supply has grown 51% since genesis.

## 💧 Liquidity & market · 5/10 · ❌ FAIL

- $7.0M of 24h volume (13% of market cap), but 75% of it is on Upbit's KRW pair.

## 🧑‍💻 Product & development · 6/10 · ✅ PASS

- The chain runs (roughly one block every 7 seconds, Tier B). EdgeCloud is live, and paying in TFUEL is supported ([billing post](https://blog.thetatoken.org/tfuel-billing-support-now-live-on-edgecloud-integrating-edgecloud-with-the-theta-token-economy/)).

## 🤝 Adoption & customers · 3/10 · ❌ FAIL

- [Unverified] One secondary analysis counts about 25,000 non-automatic transactions in 14 days of early November 2026, and finds no on-chain count of EdgeCloud jobs.

## 🛡️ Security & audits · 6/10 · ✅ PASS

- No exploit found. Validators plus a guardian-node layer; about 32% of THETA is staked (Tier B).

## ⚖️ Regulatory · 6/10 · ✅ PASS

- No enforcement found.

## 📅 Catalysts & calendar · 4/10 · ❌ FAIL

- No dated catalysts.

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | ⚪ Not proven |
| Live mint path | 🟠 Yes, by design (annual issuance) |
| Entity concentration | 🟠 12.4% in one unlabelled account |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| Theta Labs TFUEL accounts | Not attributed | — | low | no | Selling stays 4 |

## 📚 Sources

- [Tier A] Methodology update 16 Nov 2026: no new Arkham lookups; the attribution table uses evidence already cited in this report.
- [Tier A] Theta explorer API: [supply](https://explorer-api.thetatoken.org/api/supply/tfuel) and the top-accounts endpoint, 16 Nov 2026
- [Tier A] [Theta blog on EdgeCloud and TFUEL](https://blog.thetatoken.org/why-edgecloud-drives-tfuel-and-theta-value/), [TFUEL billing post](https://blog.thetatoken.org/tfuel-billing-support-now-live-on-edgecloud-integrating-edgecloud-with-the-theta-token-economy/)
- [Tier A] CoinGecko `theta-fuel`; pump days from Binance TFUELUSDT daily closes
- [Tier B] [Blockworks token transparency filing](https://blockworks.com/token-transparency/filing/theta-network) (genesis supply, burn rule)
- [Tier B] Secondary analysis of explorer activity, early Nov 2026 ([Unverified], single source)
- Arkham does not cover the Theta chain (16 Nov 2026), so no Theta wallets could be looked up

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Supply 7,532,022,689 | [explorer API](https://explorer-api.thetatoken.org/api/supply/tfuel) | A | 16 Nov 2026 |
| Largest account 935.9M | [0xffcf…61d9](https://explorer.thetatoken.org/account/0xffcf02555c27325db5a406d96689246f6d4661d9) | A | 16 Nov 2026 |
| Revenue converted to TFUEL (no figures) | [Theta blog](https://blog.thetatoken.org/why-edgecloud-drives-tfuel-and-theta-value/) | A | 16 Nov 2026 |
| Genesis 5B; ≥25% edge-payment burn | [Blockworks filing](https://blockworks.com/token-transparency/filing/theta-network) | B | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Who owns 0xffcf…61d9 and 0xd551…d9f8** | Arkham does not cover Theta; check Theta Explorer labels or ask Theta Labs | Free |
| 2 | **Burn totals and EdgeCloud revenue** | Ask the project for its burn address totals and revenue figures | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.

- Research only. Not investment advice.
