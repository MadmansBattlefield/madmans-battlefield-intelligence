---
ticker: XVG
name: Verge
chain: verge
contract: "native coin (no contract)"
overall_score: 4.1
overall_verdict: FAIL
section_scores:
  revenue: 1
  foundation_team: 3
  insider_holdings: 9
  selling_behavior: 7
  tokenomics_supply: 8
  liquidity_market: 3
  product_development: 3
  adoption_customers: 2
  security_audits: 2
  regulatory: 6
  catalysts: 3
gates_failed: [revenue]
red_lines:
  hack_exploit: "yes, outside the 1-year window: timewarp attacks Apr and May 2018; 560,000-block reorg (~200 days) on 15 Feb 2021"
  mint_path_live: "no beyond PoW issuance; supply ~16.52B, essentially fully mined"
  team_wallet_to_exchange_during_pump: "not applicable: no premine or ICO (2014 launch as DogecoinDark)"
  entity_concentration: "none known (no team allocation)"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "Fees go to miners; nothing accrues to holders."
pump_day_price_source: "MEXC XVGUSDT UTC daily closes, re-run 16 Nov 2026 with scripts/pump_day_test.py (39 of 360 days); the body's earlier count used not applicable (no insider wallets)"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions: []
price_usd: 0.001721
price_source: "CoinGecko, 16 Nov 2026 ~9:35 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### XVG · Overall grade **4.1 / 10 · ❌ FAIL**

**Summary:** Verge is a 2014 proof-of-work privacy-payments coin, first launched as DogecoinDark. It had no premine or ICO, so there are no insider wallets that could sell, and supply is essentially fully mined. Those sections pass. But it earns nothing, and its chain has been attacked three times: it suffered timewarp attacks twice in 2018 and lost about 200 days of history in a 2021 reorg. Volume is only $0.43M a day. The revenue gate fails.

**🚨 Top warning:** the chain's security record. In February 2021 an attacker rewrote **more than 560,000 blocks (about 200 days)** of Verge history. The fix was a checkpoint that the developers pushed out, which shows the chain relies on them to decide which history is valid ([CoinDesk](https://www.coindesk.com/markets/2021/02/15/pornhub-payment-option-verge-suffers-massive-blockchain-reorganization), [Coin Metrics researcher write-up](https://1ucas.me/research/verge)). It still uses five-algorithm proof-of-work, and a proof-of-stake switch is only in testnet [Tier B, one source]. Every link is in the 🔗 Evidence trail below.

**Sections passed: 4 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 1/10 | ❌ FAIL (hard gate) |
| 🏛️ Foundation & team | 3/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 9/10 | ✅ PASS |
| 📉 Selling behavior | 7/10 | ✅ PASS |
| 📊 Tokenomics & supply | 8/10 | ✅ PASS |
| 💧 Liquidity & market | 3/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 3/10 | ❌ FAIL |
| 🤝 Adoption & customers | 2/10 | ❌ FAIL |
| 🛡️ Security & audits | 2/10 | ❌ FAIL |
| ⚖️ Regulatory | 6/10 | ✅ PASS |
| 📅 Catalysts & calendar | 3/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 XVG · Verge · 4.1 / 10 · ❌ FAIL

> **One line:** No insiders and no inflation, but no revenue and a chain that has been rewritten three times.

| 📊 Market (CoinGecko, 16 Nov 2026 ~9:35 AM MST) | 🔗 Chain (project docs) |
|---|---|
| **Price** $0.001721 | **Supply** ~16.52B XVG (essentially fully mined) |
| **24h / 7d / 30d** ⚪ −0.4% / 🔴 −16.0% / 🔴 −32.3% | **Consensus** PoW, 5 algorithms, ~30-second blocks |
| **Market cap** $28.4M · **FDV** $28.5M | **Team / treasury** none (no premine, no ICO) |
| **24h volume** $0.43M (Binance $75k, Bitvavo $73k, Biconomy, MEXC, WEEX) | |
| **ATH** $0.2619 (23 Dec 2017) · now −99.3% | |
| **Pump days** 41 in the last year (Binance XVGUSDT; largest +33.0% on 23 Aug 2026) | |

---

## 💰 Revenue — Does it make money? · 1/10 · ❌ FAIL (hard gate)

- Proof-of-work with no protocol treasury. Fees go to miners. **1 → hard-gate FAIL.**

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** Fees go to miners; nothing accrues to holders.

## 🏛️ Foundation & team — Who is in charge? · 3/10 · ❌ FAIL

- Volunteer developers with no company. Funding comes from donations ([FAQ](https://vergecurrency.com/faq)).

## 🪙 Foundation / team holdings — How many coins do they hold? · 9/10 · ✅ PASS

- No premine or ICO: the team buys coins on the open market ([FAQ](https://vergecurrency.com/faq)).

## 📉 Selling behavior — Do insiders sell into pumps? · 7/10 · ✅ PASS

- With no team, foundation or treasury wallets, the insider pump-day test doesn't apply. This follows the BCH, XMR and ETC reports.
- One past exception: Fortune reported in 2018 that 18M XVG left a community crowdfunding wallet without explanation [Unverified: one secondary source], outside the window.

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from MEXC XVGUSDT UTC daily closes, re-run 16 Nov 2026 with scripts/pump_day_test.py (39 of 360 days); the body's earlier count used not applicable (no insider wallets).

## 📊 Tokenomics & supply · 8/10 · ✅ PASS

- Supply is essentially fully mined, so there's no meaningful inflation.

## 💧 Liquidity & market · 3/10 · ❌ FAIL

- $0.43M a day spread over small venues. Upbit delisted XVG in May 2020.

## 🧑‍💻 Product & development · 3/10 · ❌ FAIL

- Wallet and Secure Messaging work continues, with proof of stake in testnet [Tier B, one source].

## 🤝 Adoption & customers · 2/10 · ❌ FAIL

- Payment adoption claims are old (2018). No current usage data.

## 🛡️ Security & audits · 2/10 · ❌ FAIL

- Timewarp attacks in Apr and May 2018 and a 560,000-block reorg in Feb 2021 ([CoinDesk](https://www.coindesk.com/markets/2021/02/15/pornhub-payment-option-verge-suffers-massive-blockchain-reorganization)). Five-algorithm proof-of-work remains hard to secure.

## ⚖️ Regulatory · 6/10 · ✅ PASS

- No issuer and no sale, and no enforcement found. Privacy branding has contributed to exchange delistings.

## 📅 Catalysts & calendar · 3/10 · ❌ FAIL

- None dated. The proof-of-stake move is undated.

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🔴 Three chain attacks (2018 ×2, 2021), outside the 1-year window |
| Team wallet → exchange during a pump | 🟢 Not applicable (no team wallets) |
| Live mint path | 🟢 Essentially fully mined |
| Entity concentration | 🟢 None known |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| No team, foundation or treasury wallets | — | — | high | n/a | None: insider test does not apply |

## 📚 Sources

- [Tier A] Methodology update 16 Nov 2026: no new Arkham lookups; the attribution table uses evidence already cited in this report.
- [Tier A] [Verge FAQ](https://vergecurrency.com/faq) (no premine, no ICO)
- [Tier B] [CoinDesk, 15 Feb 2021](https://www.coindesk.com/markets/2021/02/15/pornhub-payment-option-verge-suffers-massive-blockchain-reorganization), [Coin Metrics researcher write-up](https://1ucas.me/research/verge), [PriFi profile](https://prifi.info/protocols/verge/)
- [Tier A] CoinGecko `verge`; pump days from Binance XVGUSDT daily closes
- Arkham was not run for this report (no team wallets)

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| No premine, no ICO | [FAQ](https://vergecurrency.com/faq) | A | 16 Nov 2026 |
| 560,000-block reorg, Feb 2021 | [CoinDesk](https://www.coindesk.com/markets/2021/02/15/pornhub-payment-option-verge-suffers-massive-blockchain-reorganization), [write-up](https://1ucas.me/research/verge) | B+B | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Current hashrate per algorithm and attack cost** | Read a public mining-pool stats page | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.

- Research only. Not investment advice.
