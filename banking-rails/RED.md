---
ticker: RED
name: RedStone
chain: ethereum
contract: "0xc43c6bfeda065fe2c4c11765bf838789bd0bb5de"
overall_score: 4.3
overall_verdict: FAIL
section_scores:
  revenue: 2
  foundation_team: 6
  insider_holdings: 4
  selling_behavior: 4
  tokenomics_supply: 4
  liquidity_market: 4
  product_development: 7
  adoption_customers: 5
  security_audits: 6
  regulatory: 6
  catalysts: 4
gates_failed: [revenue]
red_lines:
  hack_exploit: "none found"
  mint_path_live: "1B cap; minted in tranches (597M on Ethereum so far), rest on Base/bridged"
  team_wallet_to_exchange_during_pump: "not proven for team: a vesting beneficiary sent 1.67M RED to Binance on a +70.9% day (6 Apr 2026); whether it is team or investor is unknown"
  entity_concentration: "four vesting contracts 164M, a 3-signature Safe 45M, airdrop contracts 56M"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "Oracle income goes to the company; DefiLlama lists $61.8 of fees in a year."
pump_day_price_source: "Gate RED_USDT UTC daily closes, re-run 16 Nov 2026 with scripts/pump_day_test.py (43 of 360 days); the body's earlier count used CoinGecko daily closes"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions: []
price_usd: 0.1081
price_source: "CoinGecko, 16 Nov 2026 ~9:15 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### RED · Overall grade **4.3 / 10 · ❌ FAIL**

**Summary:** RedStone is a working oracle network: price feeds used by DeFi lending protocols on many chains. That makes its product the strongest part of the report. But the RED token earns nothing: DefiLlama shows $62 of fees over a whole year, and no oracle revenue reaches holders, so the revenue gate fails. RED is down 88% from its March 2025 listing high. People paid out by its vesting contracts have been sending their RED straight to exchanges, including on a pump day.

**🚨 Top warning:** vesting payouts go straight to exchanges. Wallet [0x1955…042b](https://etherscan.io/address/0x19555bdfb024076136efbb3b00ed6169fa5c042b) collected **11.84M RED** from the RedStone vesting contract [0xa77e…1b2e](https://etherscan.io/address/0xa77e9c5861892b82e9a360f71aed9f81c6d51b2e) and sent all of it to Binance and Bybit deposit addresses. That includes **1.67M RED (~$308k) on 6 Apr 2026**, when RED closed 70.9% above five days earlier ([tx](https://etherscan.io/tx/0xfac81c9bfa60e5d116c40da7a9fe608f9f2ae23a50bbc4cfaaa870729df91120)). Arkham leaves 0x1955 unlabelled, so whether this beneficiary is team or an investor is not public. Every link is in the 🔗 Evidence trail below.

**Sections passed: 4 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 2/10 | ❌ FAIL (hard gate) |
| 🏛️ Foundation & team | 6/10 | ✅ PASS |
| 🪙 Foundation / team holdings | 4/10 | ❌ FAIL |
| 📉 Selling behavior | 4/10 | ❌ FAIL (not proven) |
| 📊 Tokenomics & supply | 4/10 | ❌ FAIL |
| 💧 Liquidity & market | 4/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 7/10 | ✅ PASS |
| 🤝 Adoption & customers | 5/10 | ❌ FAIL |
| 🛡️ Security & audits | 6/10 | ✅ PASS |
| ⚖️ Regulatory | 6/10 | ✅ PASS |
| 📅 Catalysts & calendar | 4/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 RED · RedStone · 4.3 / 10 · ❌ FAIL

> **One line:** A real oracle business whose token captures no revenue, while vesting payouts flow straight to exchanges.

| 📊 Market (CoinGecko, 16 Nov 2026 ~9:15 AM MST) | 🔗 On-chain ([Etherscan](https://etherscan.io/token/0xc43c6bfeda065fe2c4c11765bf838789bd0bb5de), 16 Nov 2026 ~9:20 AM MST) |
|---|---|
| **Price** $0.1081 | **Ethereum supply** 597,000,000 RED (cap 1B) |
| **24h / 7d / 30d** 🔴 −3.8% / 🔴 −31.1% / 🔴 −22.5% | **4 TokenVestingManager contracts** 164.3M |
| **Market cap** $62.5M · **FDV** $108.1M | **3-signature Safe 0xba54** 45.0M |
| **24h volume** $1.27M (CoinUp $0.24M, Binance $0.21M, Bybit $0.13M, WhiteBIT, Upbit, Toobit) | **Airdrop contracts** 42.3M + 13.7M |
| **Circulating** 577.6M (57.8%) | **Vesting funder 0x70da** received 317M at mint (9 Apr 2025) |
| **ATH** $0.9325 (6 Mar 2025) · now −88.4% | |
| **Pump days** 42 in the last year (largest +94.3% on 7 Apr 2026) | |

---

## 💰 Revenue — Does it make money? · 2/10 · ❌ FAIL (hard gate)

- DefiLlama lists $61.8 of fees over the last year. Oracle service income goes to the company, not to RED holders, and no figures are published. **2 → hard-gate FAIL.**

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** Oracle income goes to the company; DefiLlama lists $61.8 of fees in a year.

## 🏛️ Foundation & team — Who is in charge? · 6/10 · ✅ PASS

- An established oracle company, described by role only. The vesting and treasury contracts are verified on Etherscan.

## 🪙 Foundation / team holdings — How many coins do they hold? · 4/10 · ❌ FAIL

- Four `TokenVestingManager` contracts were funded by 0x70da, which received a 317M mint on 9 Apr 2025. They hold 164.3M: [0xb286](https://etherscan.io/address/0xb286aaa8ff1a4d2075a3ac1dfa9e695fd5d3a654) 59.5M, [0xa77e](https://etherscan.io/address/0xa77e9c5861892b82e9a360f71aed9f81c6d51b2e) 49.6M, [0xf39e](https://etherscan.io/address/0xf39e316c74d7f975a94729395c12b06c91892dec) 35.0M and [0xf0f3](https://etherscan.io/address/0xf0f3445d002e29a230cd444e6273a3abfa0d4c4e) 20.2M. A 3-signature Safe, [0xba54](https://etherscan.io/address/0xba544abd1b34c4a337e3f3cbe2a390e061031ff7), holds 45M.

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL (not proven)

| Date | From | To | RED | Close | ≈ USD | Pump? | Tx |
|---|---|---|---:|---:|---:|---|---|
| 25 Feb 2025 | Mint recipient 0xcc6b | Binance deposit | 39,999,990 | — | — | Pre-listing (4% = Launchpool size) | [0xeaad…](https://etherscan.io/tx/0xeaada4a4948d9ee080e7a2d561ff4b424e4ebf4d2ae9df99ef4f2378122dbf66) |
| 6 Apr 2026 | Beneficiary 0x1955 (from vesting 0xa77e) | Binance deposit | 1,673,289 | $0.1839 | $308k | **Yes, +70.9%** | [0xfac8…](https://etherscan.io/tx/0xfac81c9bfa60e5d116c40da7a9fe608f9f2ae23a50bbc4cfaaa870729df91120) |
| 13 Jun 2026 | 0x1955 | Binance deposit | 3,586,252 | $0.0918 | $329k | No | [0x65c1…](https://etherscan.io/tx/0x65c1c309d4a51a255cff3191ac8e2803f3a6200b90a9ff3381a31e63992b0c60) |
| 24 Aug 2026 | Beneficiary of vesting 0xf0f3 | Coinbase Prime (custody) | 2,073,430 | $0.115 | $238k | Yes, +19.8% (custody, not a sale) | [0x4321…](https://etherscan.io/tx/0x432138562906c805479cc4fe85306ed38557f6e49f0601e5f96920da182db684) |
| 26 Aug 2026 | 0x1955 | Binance deposit | 3,928,060 | $0.110 | $432k | No | [0x1f6a…](https://etherscan.io/tx/0x1f6a8ba092a8773a0ac69bfb13efbc099af7969fdeaac175e981bfb7e910f7de) |
| 30 Sep 2026 | Vesting 0xa77e (claim) | Binance deposit | 1,091,065 | $0.1765 | $193k | No | [0xf4a7…](https://etherscan.io/tx/0xf4a7cf7cccf1e1d186259ee778847a7a758785302bbd8de09dfafcd2752bcd7b) |
| 15 Oct 2026 | 0x1955 | Bybit deposit | 1,964,219 | $0.1548 | $304k | No | [0xf71a…](https://etherscan.io/tx/0xf71a57d0037190f264dee0b0e4c4fc489b27b18561f1fcbb746c1dbefa95709d) |

- Method: a 3-hop trace from the vesting funder 0x70da, the Safe 0xba54 and mint recipient 0xcc6b (60 wallets; transfers of 1M+ RED). All linked transactions returned status 1. The Safe and 0x70da themselves sent nothing to exchanges.
- **Arkham ([Tier B] Arkham, read 16 Nov 2026 (signed-in account)):** [0x1955](https://intel.arkm.com/explorer/address/0x19555bdfb024076136efbb3b00ed6169fa5c042b) is unlabelled (not team, investor or market maker). It is paid by [TokenVestingManager 0xa77e](https://intel.arkm.com/explorer/address/0xa77e9c5861892b82e9a360f71aed9f81c6d51b2e) and forwards the same amounts to Bybit and Binance deposits. The Safes [0x70da](https://intel.arkm.com/explorer/address/0x70da99aedda98cdd5aac73c136df4fbc3899d69f), [0xba54](https://intel.arkm.com/explorer/address/0xba544abd1b34c4a337e3f3cbe2a390e061031ff7) (dormant) and [0xcc6b](https://intel.arkm.com/explorer/address/0xcc6b3cc29b7047b70c64a243a52f74db618b9087) carry no RedStone label.
- Vesting contract [0xf39e](https://intel.arkm.com/explorer/address/0xf39e316c74d7f975a94729395c12b06c91892dec) pays **Amber Group**, a market maker: 1.06M RED in five payouts from Apr to Oct 2026, including [147,788 RED on 7 Apr 2026](https://etherscan.io/tx/0xc8e259ba6f7d8871a2fc35e5fd725fe3c0a3cfb95d23088a306ed66ad2147360) (Gate close +95.6%, a pump day) and [181,185 RED on 24 Oct 2026](https://etherscan.io/tx/0xb1c1f837e8c6d64b5e515efad8e7da77b9b2be0561986389d36b3e16f8ae84e7). That is a vesting release to a market maker, not a team sale.
- One pump-day exchange deposit came from a vesting beneficiary that remains unattributed after the Arkham pass. **Selling stays not proven → 4.** If 0x1955 is shown to be a team wallet, the score becomes 3 and the selling gate fails (overall 4.1).

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from Gate RED_USDT UTC daily closes, re-run 16 Nov 2026 with scripts/pump_day_test.py (43 of 360 days); the body's earlier count used CoinGecko daily closes.

## 📊 Tokenomics & supply · 4/10 · ❌ FAIL

- 57.8% circulating, with vesting continuing from four contracts. The cap is 1B.

## 💧 Liquidity & market · 4/10 · ❌ FAIL

- $1.27M of 24h volume against a $62M market cap, spread across mid-tier venues.

## 🧑‍💻 Product & development · 7/10 · ✅ PASS

- Live pull and push oracle feeds across many EVM and non-EVM chains, with active development.

## 🤝 Adoption & customers · 5/10 · ❌ FAIL

- Oracle integrations with lending and RWA protocols (company claims). No paid-usage figures to check.

## 🛡️ Security & audits · 6/10 · ✅ PASS

- No exploit of RedStone feeds found. The token, vesting and Safe contracts are verified.

## ⚖️ Regulatory · 6/10 · ✅ PASS

- No enforcement found.

## 📅 Catalysts & calendar · 4/10 · ❌ FAIL

- Monthly vesting from four contracts continues, with no published end date.

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | ⚪ Not proven (vesting beneficiary, unlabelled on Arkham) |
| Live mint path | 🟠 Tranche mints up to the 1B cap |
| Entity concentration | 🟠 ~265M in vesting, Safe and airdrop contracts |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| Vesting beneficiary → Binance (6 Apr, +70.9% day) | Vesting beneficiary (team or investor unknown) | Etherscan | low | no | None: not proven as a team sale; Selling stays 4 |

## 📚 Sources

- [Tier A] Methodology update 16 Nov 2026: no new Arkham lookups; the attribution table uses evidence already cited in this report.
- [Tier A] Etherscan token, contract source names, Safe threshold and transactions; receipts checked 16 Nov 2026
- [Tier A] DefiLlama `redstone` fees; CoinGecko `redstone-oracles`; pump days from Binance REDUSDT daily closes
- [Tier B] Binance Launchpool listing coverage (Feb 2025)
- [Tier B] Arkham, read 16 Nov 2026 (signed-in account): TokenVestingManager labels on 0xa77e, 0xb286, 0xf39e and 0xf0f3; Amber Group as a 0xf39e payee; Bybit and Binance Deposit labels; 0x1955 and the Safes unlabelled

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Pump-day deposit, 1.67M RED | [tx 0xfac8…](https://etherscan.io/tx/0xfac81c9bfa60e5d116c40da7a9fe608f9f2ae23a50bbc4cfaaa870729df91120) | A | 16 Nov 2026 |
| Beneficiary funded by vesting 0xa77e | [0x1955…](https://etherscan.io/address/0x19555bdfb024076136efbb3b00ed6169fa5c042b) | A | 16 Nov 2026 |
| Vesting contracts and Safe holdings | [holders](https://etherscan.io/token/0xc43c6bfeda065fe2c4c11765bf838789bd0bb5de#balances) | A | 16 Nov 2026 |
| Fees $61.8 / year | [DefiLlama](https://defillama.com/protocol/redstone) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Is 0x1955 a team or investor beneficiary?** | Arkham (16 Nov 2026) leaves it unlabelled. Read the beneficiary schedule on vesting contract 0xa77e, or ask RedStone | Free |
| 2 | **Who signs Safe 0xba54** | Read the owners on the Safe app | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.

- Research only. Not investment advice.
