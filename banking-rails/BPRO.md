---
ticker: BPRO
name: Money On Chain BPRO
chain: rootstock
contract: "0x440cd83c160de5c96ddb20246815ea44c7abbca8"
overall_score: 3.8
overall_verdict: FAIL
section_scores:
  revenue: 3
  foundation_team: 5
  insider_holdings: 4
  selling_behavior: 4
  tokenomics_supply: 5
  liquidity_market: 1
  product_development: 6
  adoption_customers: 3
  security_audits: 5
  regulatory: 5
  catalysts: 3
gates_failed: [revenue]
red_lines:
  hack_exploit: "none found in this pass"
  team_wallet_to_exchange_during_pump: "not tested: no exchange series; no team allocation of BPRO"
  one_hop_sale_status: none_found
price_usd: 93676
price_source: "Blockscout BPRO exchange rate, 16 Nov 2026"
methodology_effective: 2026-11-16
revenue_reaches_holders: "yes"
revenue_mechanism: "Per Money On Chain, 20% of protocol fees are added to BPRO's technical price automatically in the protocol contracts."
pump_day_price_source: "not run (no Gate, MEXC, KuCoin or Kraken USDT series)"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions:
  - address: "0xd07d569322a93a47b62d71203e21f0aff8246099"
    label: "Unlabelled EOA (34.7%)"
    confidence: low
    independent_corroboration: false
    basis: "Blockscout holders"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### BPRO · Overall grade **3.8 / 10 · ❌ FAIL**

**Summary:** BPRO is Money On Chain's leveraged-bitcoin reserve token on Rootstock, minted and redeemed against rBTC. Money On Chain says 20% of protocol fees go into BPRO's technical price, so the holder test is yes. But no fee total is published and DefiLlama has no record, so the amount is unmeasured. About 185 BPRO exist (~$17M at Blockscout's ~$93.7k price); one unlabelled EOA holds ~35%. The Revenue gate fails.

**🚨 Top warning:** **A leveraged BTC position, not a savings product:** BPRO can fall more than bitcoin, and one unlabelled wallet holds ~35% of supply.

**Sections passed: 1 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 3/10 | ❌ FAIL (hard gate) |
| 🏛️ Foundation & team | 5/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 4/10 | ❌ FAIL |
| 📉 Selling behavior | 4/10 | ❌ FAIL (not proven) |
| 📊 Tokenomics & supply | 5/10 | ❌ FAIL |
| 💧 Liquidity & market | 1/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 6/10 | ✅ PASS |
| 🤝 Adoption & customers | 3/10 | ❌ FAIL |
| 🛡️ Security & audits | 5/10 | ❌ FAIL |
| ⚖️ Regulatory | 5/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 3/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 BPRO · Money On Chain BPRO · 3.8 / 10 · ❌ FAIL

> **One line:** A fee-sharing leveraged-BTC reserve token with unmeasured fees and concentrated holders.

---

## 💰 Revenue — Does it make money? · 3/10 · ❌ FAIL (hard gate)

- 20% of protocol fees accrue to BPRO's technical price ([Money On Chain](https://moneyonchain.com/bpro-token/)). Mint and redeem fees are 0.20–0.25%. No fee total is published, so the size is unknown.

**What it means:** The mechanism is real but unmeasured: **3 → hard-gate FAIL.**

- **Reaches holders (binary test, 16 Nov 2026 rules): Yes.** Per Money On Chain, 20% of protocol fees are added to BPRO's technical price automatically in the protocol contracts.

## 🏛️ Foundation & team — Who is in charge? · 5/10 · ❌ FAIL

- Money On Chain ([site](https://moneyonchain.com/)); governed with the MOC token.

## 🪙 Foundation / team holdings — How many coins do they hold? · 4/10 · ❌ FAIL

- [`0xd07d…6099`](https://rootstock.blockscout.com/address/0xd07d569322a93a47b62d71203e21f0aff8246099) 34.7% (EOA) is unlabelled. BPRO is minted against rBTC, so there is no team allocation. Not proven → **4**.

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL (not proven)

- BPRO has no team allocation and no exchange series.
- No exchange-labelled deposit from a disclosed team or treasury wallet on a pump day was found in this pass. No Arkham pass was run.

**What it means:** Not proven → **4**.

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from not run (no Gate, MEXC, KuCoin or Kraken USDT series).

## 📊 Tokenomics & supply · 5/10 · ❌ FAIL

- Supply floats with mints and redemptions against rBTC.

## 💧 Liquidity & market · 1/10 · ❌ FAIL

- No exchange volume; mint and redeem through the protocol.

## 🧑‍💻 Product & development · 6/10 · ✅ PASS

- Live since 2019 on Rootstock.

## 🤝 Adoption & customers · 3/10 · ❌ FAIL

- ~$17M of BPRO outstanding; 1,609 holders.

## 🛡️ Security & audits · 5/10 · ❌ FAIL

- No exploit found in this pass.

## ⚖️ Regulatory · 5/10 · ❌ FAIL

- No enforcement found.

## 📅 Catalysts & calendar · 3/10 · ❌ FAIL

- None verified.

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | ⚪ Not tested: no exchange series; no team allocation of BPRO |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. No Arkham pass was run for this report, so every attribution that rests on an unlabelled wallet is low confidence. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| `0xd07d569322a93a47b62d71203e21f0aff8246099` | Unlabelled EOA (34.7%) | Blockscout holders | low | no | None: cannot move Holdings or Selling |

## 📚 Sources

- [Tier A] [Money On Chain: BPRO](https://moneyonchain.com/bpro-token/): fee share, contracts, read 16 Nov 2026
- [Tier A] [Money On Chain protocol FAQ](https://moneyonchain.com/protocol-faq/)
- [Tier A] [Blockscout BPRO token](https://rootstock.blockscout.com/token/0x440cd83c160de5c96ddb20246815ea44c7abbca8): supply, holders, price, read 16 Nov 2026

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Fee share to BPRO | [moneyonchain.com/bpro-token](https://moneyonchain.com/bpro-token/) | A | 16 Nov 2026 |
| Supply and holders | [Blockscout](https://rootstock.blockscout.com/token/0x440cd83c160de5c96ddb20246815ea44c7abbca8/holders) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Fee totals** | Sum protocol fee events from the Money On Chain contracts on Rootstock | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior. Under the 16 Nov 2026 one-hop amendment, a transfer to an exchange counts as a sale only with a team-attributed exchange account, evidence of a sale, or no plausible published reason.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.

- Research only. Not investment advice.
