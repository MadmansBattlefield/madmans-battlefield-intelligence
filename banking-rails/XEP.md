---
ticker: XEP
name: Electra Protocol
chain: electra-protocol
contract: "native XEP on the Electra Protocol PoS chain; wrapped on BSC 0xb897d0a0f68800f8be7d69ffdd1c24b69f57bf3e and Solana 2HmJ717Smn26MRn4PzmbGf29Z5d2nU6Jqre7HyELNsX3"
overall_score: 3.1
overall_verdict: FAIL
section_scores:
  revenue: 1
  foundation_team: 4
  insider_holdings: 4
  selling_behavior: 4
  tokenomics_supply: 4
  liquidity_market: 2
  product_development: 3
  adoption_customers: 2
  security_audits: 5
  regulatory: 6
  catalysts: 3
gates_failed: [revenue]
red_lines:
  hack_exploit: "none found"
  mint_path_live: "yes; proof-of-stake rewards of up to 3% a year"
  team_wallet_to_exchange_during_pump: "not proven: no team wallets are disclosed, and the native explorer couldn't be read"
  one_hop_sale_status: none_found
  entity_concentration: "not found; native rich list unreachable"
price_usd: 9.133e-05
price_source: "CoinGecko, 16 Nov 2026 ~12:30 PM MST"
methodology_effective: 2026-11-16
revenue_reaches_holders: "unclear"
revenue_mechanism: "project says transaction fees are burned; not checked on-chain, and at XEP's fee level it rounds to zero"
pump_day_price_source: "MEXC XEP_USDT daily closes (UTC); Binance unavailable (451), Gate has no XEP pair (HTTP 400), MEXC is next in the hierarchy"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions:
  - address: "0xb897d0a0f68800f8be7d69ffdd1c24b69f57bf3e"
    label: "Electra Protocol (XEP), wrapped BSC token"
    confidence: high
    independent_corroboration: true
    basis: "Arkham explicit entity label on a verified BEP20 contract; matches the project-published wrapped contract"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### XEP · Overall grade **3.1 / 10 · ❌ FAIL**

**Summary:** Electra Protocol (XEP) is a small proof-of-stake payments coin, live since 2017 and on its own chain since 2021, with wrapped versions on BSC and Solana. It's run by a volunteer core team and the Electra Foundation. The project says fees are burned, but that couldn't be checked on-chain, and fees are tiny anyway. Trading is almost all on MEXC (~$55k a day). No team wallets are disclosed, so Selling is not proven. XEP is down 97.7% from its 2021 peak. The revenue gate fails.

**🚨 Top warning:** **nearly all trading is on one exchange, and nothing can be checked on-chain.** CoinGecko shows ~$54.8k of the ~$55k daily volume on MEXC, whose reported volumes look templated across small tokens. The native explorer couldn't be reached, so neither the claimed fee burn nor wallet concentration could be checked. Every link is in the 🔗 Evidence trail below.

**Sections passed: 1 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 1/10 | ❌ FAIL (hard gate) |
| 🏛️ Foundation & team | 4/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 4/10 | ❌ FAIL |
| 📉 Selling behavior | 4/10 | ❌ FAIL (not proven) |
| 📊 Tokenomics & supply | 4/10 | ❌ FAIL |
| 💧 Liquidity & market | 2/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 3/10 | ❌ FAIL |
| 🤝 Adoption & customers | 2/10 | ❌ FAIL |
| 🛡️ Security & audits | 5/10 | ❌ FAIL |
| ⚖️ Regulatory | 6/10 | ✅ PASS |
| 📅 Catalysts & calendar | 3/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 XEP · Electra Protocol · 3.1 / 10 · ❌ FAIL

> **One line:** A volunteer-run PoS payments coin with unverifiable burns and MEXC-only liquidity.

| 📊 Market (CoinGecko, 16 Nov 2026 ~12:30 PM MST) | 🔗 Chain |
|---|---|
| **Price** $0.0000913 | **Supply** 18.44B circulating / 29.5B total |
| **24h / 7d / 30d** 🟢 +0.1% / 🔴 −4.9% / 🔴 −27.3% | **Native PoS chain** since 1 Jan 2021 |
| **Market cap** $1.68M · **FDV** $2.69M | **Wrapped** BSC and Solana tokens |
| **24h volume** ~$54.8k (almost all MEXC) | **Rich list** not reachable |
| **ATH** $0.00397 (24 Mar 2021) · now −97.7% | |
| **Pump days** 45 in the last year (MEXC XEP_USDT; largest +33.6% on 14 Dec 2025) | |

---

## 💰 Revenue — Does it make money? · 1/10 · ❌ FAIL (hard gate)

- The project says all transaction fees are burned and staking pays up to 3% [Unverified: the native explorer couldn't be read]. Staking is new issuance, not revenue.

**What it means:** at XEP's fee level any burn rounds to zero; whether it is live couldn't be checked. **Holder test: unclear.** **1 → hard-gate FAIL.**

## 🏛️ Foundation & team — Who is in charge? · 4/10 · ❌ FAIL

- Run by a volunteer core team led by a global coordinator, with the Electra Foundation (set up in 2022) ([electraprotocol.com](https://www.electraprotocol.com)). Leaders are described by role only.

## 🪙 Foundation / team holdings — How many coins do they hold? · 4/10 · ❌ FAIL

- No team or foundation allocation or wallet is disclosed, and the native rich list was unreachable. Score 4.
- **Arkham (16 Nov 2026)** labels the wrapped BSC contract [0xb897…bf3e](https://intel.arkm.com/explorer/address/0xb897d0a0f68800f8be7d69ffdd1c24b69f57bf3e) **Electra Protocol (XEP)**, a verified contract deployed by an "Electra Protocol: Deployer" wallet. The page has no holder ranking and no exchange activity, so it identifies the token, not team wallets. [Tier B] Arkham, read 16 Nov 2026 (signed-in account).

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL (not proven)

- No disclosed team wallets, and the native chain couldn't be read. BscScan needs a paid key for the wrapped token. **Not proven → 4.**

## 📊 Tokenomics & supply · 4/10 · ❌ FAIL

- 29.5B total, 18.44B circulating, with PoS issuance of up to 3% a year. How the gap between total and circulating supply is held isn't disclosed.

## 💧 Liquidity & market · 2/10 · ❌ FAIL

- ~$55k a day, almost all on MEXC; MEXC's figures look templated across small tokens [Unverified].

## 🧑‍💻 Product & development · 3/10 · ❌ FAIL

- Roadmap (as of Nov 2026) lists smart contracts and validator nodes; a staking wallet shipped in Apr 2026 [Tier B, project site].

## 🤝 Adoption & customers · 2/10 · ❌ FAIL

- Little visible usage.

## 🛡️ Security & audits · 5/10 · ❌ FAIL

- No exploit found. A small PoS chain is exposed to stake-concentration risk.

## ⚖️ Regulatory · 6/10 · ✅ PASS

- No enforcement found.

## 📅 Catalysts & calendar · 3/10 · ❌ FAIL

- Smart contracts and validator nodes are on the roadmap, with no dates.

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | ⚪ Not proven: no disclosed team wallets |
| Live mint path | 🟡 PoS rewards up to 3% |
| Entity concentration | ⚪ Not found |

## 📚 Sources

- [Tier B] Arkham, read 16 Nov 2026 (signed-in account): Electra Protocol label on the wrapped BSC contract
- [Tier A] [Electra Protocol site](https://www.electraprotocol.com)
- [Tier A] CoinGecko `electra-protocol` (market, venues, contracts); pump days from MEXC XEP_USDT daily closes (UTC), per the price-source hierarchy (Gate has no pair)

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Wrapped BSC contract | [BscScan token](https://bscscan.com/token/0xb897d0a0f68800f8be7d69ffdd1c24b69f57bf3e) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Is the fee burn live, and who holds the supply?** | Read the native explorer's rich list and burn address | Free, once an explorer is reachable |
| 2 | **Wrapped-token holders on BSC** | BscScan holders page | Paid API key, or manual read |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.

- Research only. Not investment advice.
