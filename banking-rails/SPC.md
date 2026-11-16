---
ticker: SPC
name: SpaceChain
chain: ethereum
contract: "0x86ed939b500e121c0c5f493f399084db596dad20"
overall_score: 3.2
overall_verdict: FAIL
section_scores:
  revenue: 1
  foundation_team: 5
  insider_holdings: 3
  selling_behavior: 4
  tokenomics_supply: 4
  liquidity_market: 2
  product_development: 5
  adoption_customers: 2
  security_audits: 4
  regulatory: 5
  catalysts: 4
gates_failed: [revenue]
red_lines:
  hack_exploit: "none found in this pass"
  team_wallet_to_exchange_during_pump: "not tested: no exchange series; top holders sent nothing to exchanges in the past year"
  one_hop_sale_status: none_found
  entity_concentration: "one unlabelled proxy holds about 64% of supply"
price_usd: 0.00609034
price_source: "CoinGecko `spacechain-erc-20`, 16 Nov 2026 ~3:00 PM MST"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "Satellite and communications income stays with the company; no burn, buyback or fee share to SPC holders was found."
pump_day_price_source: "not run (no Gate, MEXC, KuCoin or Kraken USDT series)"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions:
  - address: "0x2d358d2ce3a22a91eaf638bb7d60062a096a005d"
    label: "Unlabelled proxy (63.9%)"
    confidence: low
    independent_corroboration: false
    basis: "Ethplorer top holders + Etherscan contract name"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### SPC · Overall grade **3.2 / 10 · ❌ FAIL**

**Summary:** SpaceChain builds satellite payloads and services for blockchain and secure communications. In Q3 2026 it delivered the KSA-1 CubeSat for launch integration and a satellite handset, "Tethys". SPC is an ERC-20 (migrated from a v1 contract) with no claim on the company's satellite income. One proxy contract holds ~64% of supply and made no transfers in the past year. The Revenue gate fails.

**🚨 Top warning:** **About 64% of SPC sits in one unlabelled proxy contract** (`0x2d35…005d`); who controls it is not published. Daily volume is only ~$10k, all on DEX pools.

**Sections passed: 0 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 1/10 | ❌ FAIL (hard gate) |
| 🏛️ Foundation & team | 5/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 3/10 | ❌ FAIL |
| 📉 Selling behavior | 4/10 | ❌ FAIL (not proven) |
| 📊 Tokenomics & supply | 4/10 | ❌ FAIL |
| 💧 Liquidity & market | 2/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 5/10 | ❌ FAIL |
| 🤝 Adoption & customers | 2/10 | ❌ FAIL |
| 🛡️ Security & audits | 4/10 | ❌ FAIL |
| ⚖️ Regulatory | 5/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 4/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 SPC · SpaceChain · 3.2 / 10 · ❌ FAIL

> **One line:** A satellite-tech company's token with no claim on its income and a dominant unlabelled holder.

| 📊 Market (CoinGecko `spacechain-erc-20`, 16 Nov 2026 ~3:00 PM MST) | 🔗 Chain |
|---|---|
| **Price** $0.00609 | **Supply** 604M (CoinGecko) |
| **7d / 30d / 1y** 🔴 −10.3% / 🔴 −33.9% / 🔴 −72.2% | **Ethereum ERC-20 v2** `0x86ed…ad20` |
| **Market cap** $3.68M · **FDV** $3.68M | **Holders** 2,589 (Ethplorer) |
| **24h volume** $10.1k (top venues: Sushiswap V3 (Ethereum) $5.07k, Curve (Ethereum) $4.99k, Sushiswap V3 (Ethereum) $7) | **Top holder** proxy [`0x2d35…005d`](https://etherscan.io/address/0x2d358d2ce3a22a91eaf638bb7d60062a096a005d) 63.9% |
| **ATH** $0.129 (2021-02-17) |  |
| **Pump days** not tested: no Gate, MEXC or KuCoin USDT series |  |

---

## 💰 Revenue — Does it make money? · 1/10 · ❌ FAIL (hard gate)

- No fee or revenue record on DefiLlama and none published by the project was found.
- Company income from missions such as KSA-1 with SpaceBelt KSA ([Q2 2026 report](https://medium.com/blogspacechain/spacechain-quarterly-report-april-june-2026-0dfa8acc0ca9)) does not flow to SPC.

**What it means:** Nothing reaches holders. **1 → hard-gate FAIL.**

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** Satellite and communications income stays with the company; no burn, buyback or fee share to SPC holders was found.

## 🏛️ Foundation & team — Who is in charge? · 5/10 · ❌ FAIL

- SpaceChain, with a named CEO and quarterly reports on [Medium](https://medium.com/blogspacechain).

## 🪙 Foundation / team holdings — How many coins do they hold? · 3/10 · ❌ FAIL

- Proxy [`0x2d35…005d`](https://etherscan.io/address/0x2d358d2ce3a22a91eaf638bb7d60062a096a005d) holds 63.9% and had no SPC transfers since Nov 2025. It is unlabelled; it may be a migration or treasury contract [Unverified]. **3**.

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL (not proven)

- SPC trades only on DEX pools (Sushiswap, Curve), so no Gate, MEXC, KuCoin or Kraken series exists and the pump test was not run.
- The top EOAs and the 63.9% proxy sent no SPC to an exchange-labelled address in the past year; one top EOA sold 5.2M SPC through MetaMask Swaps, but it is not team-attributed. No Arkham pass was run.

**What it means:** Not proven → **4**.

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from not run (no Gate, MEXC, KuCoin or Kraken USDT series).

## 📊 Tokenomics & supply · 4/10 · ❌ FAIL

- 604M supply (CoinGecko); the v1 → v2 migration's leftover and the proxy's role are not documented.

## 💧 Liquidity & market · 2/10 · ❌ FAIL

- ~$10k a day across Sushiswap V3 and Curve; no centralized exchange market.

## 🧑‍💻 Product & development · 5/10 · ❌ FAIL

- KSA-1 satellite delivered for launch integration and Tethys handset delivered in Q3 2026 [Tier B, self-reported].

## 🤝 Adoption & customers · 2/10 · ❌ FAIL

- One named mission partner (SpaceBelt KSA); no SPC usage figures.

## 🛡️ Security & audits · 4/10 · ❌ FAIL

- No exploit found.

## ⚖️ Regulatory · 5/10 · ❌ FAIL

- No enforcement found.

## 📅 Catalysts & calendar · 4/10 · ❌ FAIL

- KSA-1 launch (date not confirmed).

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | ⚪ Not tested: no exchange series; no team wallet sent SPC to an exchange in the past year |
| Entity concentration | 🔴 One proxy holds ~64% |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. No Arkham pass was run for this report, so every attribution that rests on an unlabelled wallet is low confidence. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| [`0x2d35…005d`](https://etherscan.io/address/0x2d358d2ce3a22a91eaf638bb7d60062a096a005d) | Unlabelled proxy (63.9%) | Ethplorer top holders + Etherscan contract name | low | no | none |

## 📚 Sources

- [Tier A] [CoinGecko `spacechain-erc-20`](https://www.coingecko.com/en/coins/spacechain-erc-20): price, supply, venues and description, read 16 Nov 2026
- [Tier A] `scripts/pump_day_test.py`: no Gate, MEXC, KuCoin or Kraken USDT series returned on 16 Nov 2026
- [Tier A] Token contract and [holders](https://etherscan.io/token/0x86ed939b500e121c0c5f493f399084db596dad20#balances) on the chain explorer; top holders from the Ethplorer API; contract or EOA status from Etherscan v2 `eth_getCode`

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Market data and venues | [CoinGecko `spacechain-erc-20`](https://www.coingecko.com/en/coins/spacechain-erc-20) | A | 16 Nov 2026 |
| Token contract and holders | [contract](https://etherscan.io/token/0x86ed939b500e121c0c5f493f399084db596dad20) · [holders](https://etherscan.io/token/0x86ed939b500e121c0c5f493f399084db596dad20#balances) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **63.9% proxy** | Ask SpaceChain what `0x2d35…005d` is and who controls it, or run Arkham | Arkham |
| 2 | **Token role** | Find any use of SPC in KSA-1 or Tethys services | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior. Under the 16 Nov 2026 one-hop amendment, a transfer to an exchange counts as a sale only with a team-attributed exchange account, evidence of a sale, or no plausible published reason.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.

- Research only. Not investment advice.
