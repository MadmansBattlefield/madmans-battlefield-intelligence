---
ticker: PUNDIX
name: Pundi X
chain: ethereum
contract: "0x0fd10b9899882a6f2fcb5c371e17e70fdee00c38"
overall_score: 3.4
overall_verdict: FAIL
section_scores:
  revenue: 2
  foundation_team: 4
  insider_holdings: 4
  selling_behavior: 4
  tokenomics_supply: 5
  liquidity_market: 3
  product_development: 3
  adoption_customers: 2
  security_audits: 5
  regulatory: 5
  catalysts: 3
gates_failed: [revenue]
red_lines:
  hack_exploit: "none found"
  mint_path_live: "not proven: single 258.5M mint on 8 Mar 2021, no mints since"
  team_wallet_to_exchange_during_pump: "not proven: the pump-day deposits came from Upbit hot wallets (exchange-to-exchange flow); no identified team wallet moved PUNDIX in the last year"
  one_hop_sale_status: none_found
  entity_concentration: "Upbit (exchange custody) holds 127.3M (49.3%); two unlabelled Safes hold 18.6M (7.2%)"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "No fee or revenue data; nothing reaches holders."
pump_day_price_source: "Gate PUNDIX_USDT UTC daily closes, re-run 16 Nov 2026 with scripts/pump_day_test.py (15 of 360 days); the body's earlier count used CoinGecko daily closes"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions:
  - address: "0x1dca35ea1aedfbbf6a7be6c5ef6b017433aa3b5a"
    label: "Upbit: Hot Wallet"
    confidence: high
    independent_corroboration: true
    basis: "Etherscan + Arkham"
price_usd: 0.07492
price_source: "CoinGecko, 16 Nov 2026 ~9:15 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### PUNDIX · Overall grade **3.4 / 10 · ❌ FAIL**

**Summary:** Pundi X began as a crypto point-of-sale company. PUNDIX replaced NPXS at 1,000:1 in March 2021, and the project has since moved toward AI data on its own chain. The ERC-20 supply is fixed at 258.4M and fully circulating. Half of it (49.3%) sits in one wallet that Arkham labels **Upbit**, so it is exchange custody, not a project treasury. No team wallet has been identified, so team holdings and selling are not proven. No revenue reaches the token, and the revenue gate fails.

**🚨 Top warning:** no revenue, and the team's own holdings are unknown. **Correction:** the 49.3% holder [0x2bc8…2960](https://etherscan.io/address/0x2bc8e0130319b206aace6f41e28fd0cb3c2a2960) and its funder 0xe0e0 are labelled **Upbit** by Arkham, and the "funded sellers" [0x1dca…3b5a](https://etherscan.io/address/0x1dca35ea1aedfbbf6a7be6c5ef6b017433aa3b5a) and [0xce07…80c4](https://etherscan.io/address/0xce07eb2831c5bd838343f739d6315623c35680c4) are **Upbit hot wallets**. The 11.9M PUNDIX they sent to Binance, Gate and Bithumb on pump days is Upbit moving inventory between exchanges, not insider selling. The two largest non-exchange holders are unlabelled 2-signature Safes (12.0M and 6.6M) that moved no PUNDIX in the last year. Every link is in the 🔗 Evidence trail below.

**Sections passed: 0 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 2/10 | ❌ FAIL (hard gate) |
| 🏛️ Foundation & team | 4/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 4/10 | ❌ FAIL |
| 📉 Selling behavior | 4/10 | ❌ FAIL (not proven) |
| 📊 Tokenomics & supply | 5/10 | ❌ FAIL |
| 💧 Liquidity & market | 3/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 3/10 | ❌ FAIL |
| 🤝 Adoption & customers | 2/10 | ❌ FAIL |
| 🛡️ Security & audits | 5/10 | ❌ FAIL |
| ⚖️ Regulatory | 5/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 3/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 PUNDIX · Pundi X · 3.4 / 10 · ❌ FAIL

> **One line:** Fixed, fully circulating supply, half of it in Upbit custody, with no revenue and no identifiable team wallets.

| 📊 Market (CoinGecko, 16 Nov 2026 ~9:15 AM MST) | 🔗 On-chain ([Etherscan](https://etherscan.io/token/0x0fd10b9899882a6f2fcb5c371e17e70fdee00c38), 16 Nov 2026 ~9:30 AM MST) |
|---|---|
| **Price** $0.07492 | **Supply** 258,386,541 PUNDIX (one mint, 8 Mar 2021) |
| **24h / 7d / 30d** ⚪ +0.9% / 🔴 −18.6% / 🔴 −25.1% | **0x2bc8 (Upbit, exchange)** 127.3M (49.3%) |
| **Market cap** $19.4M · **FDV** $19.4M | **Two 2-signature Safes** 12.0M and 6.6M |
| **24h volume** $0.60M (HTX, Binance $0.18M, BTCC, Toobit, Upbit, MEXC) | **Upbit hot wallets to other exchanges, last year** ~102M (0x1dca 57.7M, 0xce07 44.1M) |
| **ATH** $10.07 (30 Mar 2021) · now −99.3% | |
| **Pump days** 16 in the last year (largest +23.4% on 21 Aug 2026) | |

---

## 💰 Revenue — Does it make money? · 2/10 · ❌ FAIL (hard gate)

- No fee or revenue data on DefiLlama or from the project. **2 → hard-gate FAIL.**

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** No fee or revenue data; nothing reaches holders.

## 🏛️ Foundation & team — Who is in charge? · 4/10 · ❌ FAIL

- Pundi X Labs, described by role only. The project has pivoted from point-of-sale hardware to AI data on its own chain.

## 🪙 Foundation / team holdings — How many coins do they hold? · 4/10 · ❌ FAIL

- [0x2bc8](https://etherscan.io/address/0x2bc8e0130319b206aace6f41e28fd0cb3c2a2960) received 113.6M from 0xe0e0 on 21 Feb 2023 ([tx](https://etherscan.io/tx/0x6fa9a3b7c8370969dd5cc6b31e87fd79a584d46286e1aa9146252b4c93fa8e17)). 0xe0e0 had been funded by the 2021 mint wallet ([tx](https://etherscan.io/tx/0x6d51f4909e9eb3805ebc98b9ebebb2cabfe3833ca5e9d4b7815bbd81b5b4b6ed)). It holds 127.3M (49.3%).
- **Correction (Arkham, [Tier B] Arkham, read 16 Nov 2026 (signed-in account)):** [0x2bc8](https://intel.arkm.com/explorer/address/0x2bc8e0130319b206aace6f41e28fd0cb3c2a2960) and [0xe0e0](https://intel.arkm.com/explorer/address/0xe0e0fa0202f42c8bd7154a4cc3dd298b37eaca51) are both labelled **Upbit** (centralized exchange), and [0x5ae1](https://intel.arkm.com/explorer/address/0x5ae1b41d1598ae6c3ad716ecf14f55cf301c3bd0) is **Pundi X: SwapToken**, the NPXS→PUNDIX swap contract. So the "issuer line" is Upbit converting its customers' NPXS through the swap contract: the 49.3% is exchange custody, not a project holding.
- The largest non-exchange holders are two 2-signature Safes, [0x21f7](https://intel.arkm.com/explorer/address/0x21f7cfa4fc40fb9f1a68e9e7eaa92375dd7e163e) (12.0M) and [0x86E0](https://intel.arkm.com/explorer/address/0x86e0c334b7a90a0b0927b5da54ef0393303e7c6a) (6.6M). Arkham gives neither a project label; both are active in Aave and use Binance deposits for ETH and USDT. Whose they are is [Unverified].
- **Re-score:** no identified team or treasury holding, so concentration can't be pinned on insiders, but the team's holdings are not published either. Not proven → **4** (was 2).

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL (not proven)

| Wallet (Arkham label) | Funded by | To exchanges (last year) | On pump days | ≈ USD on pump days |
|---|---|---:|---:|---:|
| [0x1dca…3b5a](https://etherscan.io/address/0x1dca35ea1aedfbbf6a7be6c5ef6b017433aa3b5a) (**Upbit: Hot Wallet**) | 0x2bc8 (Upbit), 30 Nov 2025 ([tx](https://etherscan.io/tx/0x5b5af1ccc10d4f3e3fb99414b43c248d6a212555801c5f2ba634aaa3f8b2a6a1)) | 57.7M | 5.36M (117 tx) | $548k |
| [0xce07…80c4](https://etherscan.io/address/0xce07eb2831c5bd838343f739d6315623c35680c4) (**Upbit: Hot Wallet**) | 0x1dca (Upbit), 30 Nov 2025 ([tx](https://etherscan.io/tx/0x3a8df4d8f4e0d12d744d86adae2d2b1538f381ce2cb162d36863f02684852e46)) | 44.1M | 6.58M (146 tx) | $673k |

- Pump-day deposits by venue: Binance 6.56M, Gate 4.36M, Bithumb 1.01M. Example: 100,000 PUNDIX to a Binance deposit on 15 Sep 2026 (+22.4%) ([tx](https://etherscan.io/tx/0x14f94b125ab9380cb570a28e87354e51a104254a4f6ccdff7bf920fff09ab7b4)). All linked transactions returned status 1.
- **Correction:** Arkham labels both senders **Upbit hot wallets**, fed by Upbit deposit addresses. These are exchange-to-exchange transfers (Upbit to Binance, Gate and Bithumb), not team sales. The selling gate no longer fails.
- The two unlabelled Safes moved no PUNDIX in the last 365 days (Etherscan). 0x86E0's older outflows (Nov 2023–May 2025) went to one unlabelled wallet and fall outside the window.
- No team wallet is identified, so the pump-day test can't be run on insiders → **not proven, 4** (was 3).

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from Gate PUNDIX_USDT UTC daily closes, re-run 16 Nov 2026 with scripts/pump_day_test.py (15 of 360 days); the body's earlier count used CoinGecko daily closes.

## 📊 Tokenomics & supply · 5/10 · ❌ FAIL

- Fixed 258.4M, fully circulating since 2021, with no mints since.

## 💧 Liquidity & market · 3/10 · ❌ FAIL

- About $0.6M a day. Volume is split across HTX, Binance and Korean venues.

## 🧑‍💻 Product & development · 3/10 · ❌ FAIL

- The point-of-sale hardware business has faded. The new AI-data chain has no independent usage data.

## 🤝 Adoption & customers · 2/10 · ❌ FAIL

- No paying users found.

## 🛡️ Security & audits · 5/10 · ❌ FAIL

- No exploit found. The ERC-20 is a 2021 contract.

## ⚖️ Regulatory · 5/10 · ❌ FAIL

- No enforcement found.

## 📅 Catalysts & calendar · 3/10 · ❌ FAIL

- No dated catalysts. The chain migration and AI pivot are undated.

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | ⚪ Not proven: the 11.9M on pump days came from Upbit hot wallets (exchange flow) |
| Live mint path | 🟢 None seen since 2021 |
| Entity concentration | 🟠 49.3% in Upbit custody; 7.2% in two unlabelled Safes |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| [0x1dca…3b5a](https://etherscan.io/address/0x1dca35ea1aedfbbf6a7be6c5ef6b017433aa3b5a) | Upbit: Hot Wallet | Etherscan + Arkham | high | yes | None: exchange-to-exchange flow |

## 📚 Sources

- [Tier A] Methodology update 16 Nov 2026: no new Arkham lookups; the attribution table uses evidence already cited in this report.
- [Tier A] Etherscan token, wallet and transaction pages, with exchange deposit labels; receipts checked 16 Nov 2026
- [Tier A] CoinGecko `pundi-x-2`; pump days from Binance PUNDIXUSDT daily closes
- [Tier B] Arkham, read 16 Nov 2026 (signed-in account): Upbit on 0x2bc8 and 0xe0e0; Upbit: Hot Wallet on 0x1dca and 0xce07; Pundi X: SwapToken on 0x5ae1; no project label on Safes 0x21f7 and 0x86E0

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| 258.5M minted to one wallet | [tx 0x1471…](https://etherscan.io/tx/0x147164987258b9dd8da76023720f19c84c03e9cd662d4d250a23706e4e350f41) | A | 16 Nov 2026 |
| 113.6M from Upbit 0xe0e0 to Upbit 0x2bc8 | [tx 0x6fa9…](https://etherscan.io/tx/0x6fa9a3b7c8370969dd5cc6b31e87fd79a584d46286e1aa9146252b4c93fa8e17) | A | 16 Nov 2026 |
| Pump-day Upbit hot wallet → Binance deposit example | [tx 0x14f9…](https://etherscan.io/tx/0x14f94b125ab9380cb570a28e87354e51a104254a4f6ccdff7bf920fff09ab7b4), [tx 0xa185…](https://etherscan.io/tx/0xa185c4053c796f2b4d82691a5af4bfb1da6257a9a903eb9ab70eb90387143107) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Where are the team and treasury wallets?** | Arkham (16 Nov 2026) shows 0x2bc8 is Upbit and finds no Pundi X wallet besides the swap contract. Ask Pundi X Labs to publish its treasury addresses, including on Pundi AIFX chain | Free |
| 2 | **Who owns Safes 0x21f7 and 0x86E0** | Read their signers and trace the 2026 funder `0x6f1d09fe…` | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.

- Research only. Not investment advice.
