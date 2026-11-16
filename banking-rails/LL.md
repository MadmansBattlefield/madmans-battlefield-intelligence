---
ticker: LL
name: LightLink
chain: ethereum
contract: "0x0921799cb1d702148131024d18fcde022129dc73"
overall_score: 3.7
overall_verdict: FAIL
section_scores:
  revenue: 2
  foundation_team: 5
  insider_holdings: 4
  selling_behavior: 4
  tokenomics_supply: 4
  liquidity_market: 3
  product_development: 5
  adoption_customers: 3
  security_audits: 5
  regulatory: 5
  catalysts: 4
gates_failed: [revenue]
red_lines:
  hack_exploit: "none found in this pass"
  team_wallet_to_exchange_during_pump: "none found: top Safes sent no LL to exchanges in the past year"
  one_hop_sale_status: none_found
  wash_volume: "24h volume about 1.85x market cap, almost all on KuCoin"
price_usd: 0.00071231
price_source: "CoinGecko `lightlink`, 16 Nov 2026 ~3:00 PM MST"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "Enterprise fees buy LL into the Strategic Reserve (a treasury). Burning is only an option for a future DAO; nothing is burned or paid to holders today."
pump_day_price_source: "Gate LL_USDT UTC daily closes"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions:
  - address: "0x8c6ee4264e84b299e2c66aa5b284043a3d80ca8e"
    label: "Unlabelled Safe (32.8%), likely ecosystem or treasury"
    confidence: low
    independent_corroboration: false
    basis: "Ethplorer top holders + Etherscan contract name"
  - address: "0x63105ee97bfb22dfe23033b3b14a4f8fed121ee9"
    label: "PredicateProxy (31.2%), bridge-type contract"
    confidence: low
    independent_corroboration: false
    basis: "Etherscan contract name"
  - address: "0x58edf78281334335effa23101bbe3371b6a36a51"
    label: "KuCoin 20 (4.8%)"
    confidence: medium
    independent_corroboration: false
    basis: "Etherscan name tag"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### LL · Overall grade **3.7 / 10 · ❌ FAIL**

**Summary:** LightLink is an Ethereum layer-2 with a gasless "Enterprise Mode": apps pay a fixed monthly fee so their users transact for free. Since Oct 2025 LightLink says it converts enterprise fees into LL on the open market for a Strategic Reserve, a treasury that a future DAO may burn or spend. The reserve is not paid to holders and no fee total is published. CoinGecko's ~$108k of daily volume is about 1.85× its $58k market cap, almost all on KuCoin, which looks inflated. No team-labelled exchange flow was found on the 4 pump days. The Revenue gate fails.

**🚨 Top warning:** **Reported volume is about twice the market cap (~$108k a day vs $58k, ~98% on one venue, KuCoin) and is likely inflated.** CoinGecko also counts only ~82M of 1B LL as circulating, so the cap figure itself may be understated. The CEO's Jan 2026 note says Bybit had held "a sizeable allocation" of LL that was sold on the open market, and Bybit delisted LL.

**Sections passed: 0 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 2/10 | ❌ FAIL (hard gate) |
| 🏛️ Foundation & team | 5/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 4/10 | ❌ FAIL |
| 📉 Selling behavior | 4/10 | ❌ FAIL (not proven) |
| 📊 Tokenomics & supply | 4/10 | ❌ FAIL |
| 💧 Liquidity & market | 3/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 5/10 | ❌ FAIL |
| 🤝 Adoption & customers | 3/10 | ❌ FAIL |
| 🛡️ Security & audits | 5/10 | ❌ FAIL |
| ⚖️ Regulatory | 5/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 4/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 LL · LightLink · 3.7 / 10 · ❌ FAIL

> **One line:** A gasless L2 whose fees buy LL into a treasury, not to holders, on volume that looks inflated.

| 📊 Market (CoinGecko `lightlink`, 16 Nov 2026 ~3:00 PM MST) | 🔗 Chain |
|---|---|
| **Price** $0.000712 | **Supply** ~82M circulating (CoinGecko) / 1B max |
| **7d / 30d / 1y** 🔴 −3.1% / 🔴 −38.8% / 🔴 −92.2% | **Ethereum ERC-20** `0x0921…dc73` (also on Base and LightLink) |
| **Market cap** $58.2k · **FDV** $712k | **Holders** 4,885 (Ethplorer) |
| **24h volume** $108k (top venues: KuCoin $106k, Gate $2.15k, Uniswap V4 (Ethereum) $1) | **Top holders** Safe [`0x8c6e…ca8e`](https://etherscan.io/address/0x8c6ee4264e84b299e2c66aa5b284043a3d80ca8e) 32.8%, bridge-type proxy [`0x6310…1ee9`](https://etherscan.io/address/0x63105ee97bfb22dfe23033b3b14a4f8fed121ee9) 31.2% |
| **ATH** $0.162 (2024-04-24) |  |
| **Pump days** 4 of 360 days (Gate LL_USDT UTC daily closes); latest 2026-11-09, 2026-11-11 |  |

---

## 💰 Revenue — Does it make money? · 2/10 · ❌ FAIL (hard gate)

- Enterprise Mode plans are priced from free up to $5,000 a month and more ([pricing](https://lightlink.io/enterprise-mode)), but LightLink publishes no fee total and DefiLlama has no record.
- Since 31 Oct 2025 enterprise fees are used to buy LL for the [Strategic Reserve](https://lightlink.io/blog/lightlink-strategic-reserve), to fund grants, listings and liquidity. That is a treasury buy, not a holder payout.

**What it means:** Some revenue exists but none reaches holders. **2 → hard-gate FAIL.**

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** Enterprise fees buy LL into the Strategic Reserve (a treasury). Burning is only an option for a future DAO; nothing is burned or paid to holders today.

## 🏛️ Foundation & team — Who is in charge? · 5/10 · ❌ FAIL

- Built by Pellar Technology, with a named CEO and public [blog](https://lightlink.io/blog/lightlink-network-update). Code at [github.com/pellartech](https://github.com/pellartech).

## 🪙 Foundation / team holdings — How many coins do they hold? · 4/10 · ❌ FAIL

- Published allocation ([token page](https://lightlink.io/token)): team 14%, seed VCs 14%, advisors 5%, ecosystem fund 40%, staking reserve 10%, market making 5%.
- Two Safes hold 32.8% ([`0x8c6e…ca8e`](https://etherscan.io/address/0x8c6ee4264e84b299e2c66aa5b284043a3d80ca8e)) and 6.7% ([`0x1723…b331`](https://etherscan.io/address/0x172363249a18177623514434865611d8902ab331)) of the Ethereum supply. They are unlabelled, so they are likely, but not proven, ecosystem or treasury wallets [Unverified]. Not proven → **4**.

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL (not proven)

- Pump test: Gate LL_USDT found 4 pump days in 360 (11 Oct, 8, 9 and 11 Nov 2026).
- The top Safes made only internal moves in the past year: [`0x8c6e…ca8e`](https://etherscan.io/address/0x8c6ee4264e84b299e2c66aa5b284043a3d80ca8e) sent 11.5M LL to another Safe and 9.7M LL to an EOA that passed it on to one unlabelled address on 27 Nov 2025 (not a pump day). None of these reached an exchange-labelled address.
- The CEO's [6 Jan 2026 note](https://lightlink.io/blog/lightlink-network-update) says Bybit's "sizeable allocation" of LL was sold on the open market. That is an exchange's allocation, not a proven team sale. No Arkham pass was run.

**What it means:** No team sale proven → **4**.

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from Gate LL_USDT UTC daily closes.

## 📊 Tokenomics & supply · 4/10 · ❌ FAIL

- 1B max. CoinGecko counts ~82M circulating, while the token page's own $10M market-cap headline implies far more; the circulating figure is unclear. Team and VC vesting (15- and 12-month cliffs, then 18 months) from the Apr 2024 launch should be complete or nearly so.

## 💧 Liquidity & market · 3/10 · ❌ FAIL

- ~$108k a day: KuCoin LL/USDT ~$106k, Gate ~$2k, Uniswap ~$1. That is ~1.85× the CoinGecko market cap and ~15% of FDV a day on one venue, so it is **likely inflated**. Bybit delisted LL in Jan 2026.

## 🧑‍💻 Product & development · 5/10 · ❌ FAIL

- The L2 is live, with Enterprise Mode, an LL OFT on Ethereum, Base and LightLink, and Stella Wallet [Tier A, self-described].

## 🤝 Adoption & customers · 3/10 · ❌ FAIL

- No enterprise customer count or fee total is published.

## 🛡️ Security & audits · 5/10 · ❌ FAIL

- No exploit found in this pass.

## ⚖️ Regulatory · 5/10 · ❌ FAIL

- No enforcement found.

## 📅 Catalysts & calendar · 4/10 · ❌ FAIL

- DAO launch with control of the Strategic Reserve; possible burns if voted.

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | ⚪ None found: top Safes sent no LL to exchanges in the past year |
| Volume quality | 🔴 24h volume ~1.85× market cap, ~98% on KuCoin |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. No Arkham pass was run for this report, so every attribution that rests on an unlabelled wallet is low confidence. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| [`0x8c6e…ca8e`](https://etherscan.io/address/0x8c6ee4264e84b299e2c66aa5b284043a3d80ca8e) | Unlabelled Safe (32.8%), likely ecosystem or treasury | Ethplorer top holders + Etherscan contract name | low | no | none |
| [`0x6310…1ee9`](https://etherscan.io/address/0x63105ee97bfb22dfe23033b3b14a4f8fed121ee9) | PredicateProxy (31.2%), bridge-type contract | Etherscan contract name | low | no | none |
| [`0x58ed…6a51`](https://etherscan.io/address/0x58edf78281334335effa23101bbe3371b6a36a51) | KuCoin 20 (4.8%) | Etherscan name tag | medium | no | none |

## 📚 Sources

- [Tier A] [CoinGecko `lightlink`](https://www.coingecko.com/en/coins/lightlink): price, supply, venues and description, read 16 Nov 2026
- [Tier A] Gate LL_USDT UTC daily closes via `scripts/pump_day_test.py` (4 pump days of 360); Binance returned HTTP 451, so the hierarchy fell through to this venue
- [Tier A] Token contract and [holders](https://etherscan.io/token/0x0921799cb1d702148131024d18fcde022129dc73#balances) on the chain explorer; top holders from the Ethplorer API; contract or EOA status from Etherscan v2 `eth_getCode`

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Market data and venues | [CoinGecko `lightlink`](https://www.coingecko.com/en/coins/lightlink) | A | 16 Nov 2026 |
| Token contract and holders | [contract](https://etherscan.io/token/0x0921799cb1d702148131024d18fcde022129dc73) · [holders](https://etherscan.io/token/0x0921799cb1d702148131024d18fcde022129dc73#balances) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Safe ownership** | Ask LightLink to label the 32.8% and 6.7% Safes, or run Arkham on them | Arkham |
| 2 | **Enterprise fee total** | Ask for monthly Enterprise Mode revenue and Strategic Reserve purchases on-chain | Free |
| 3 | **KuCoin volume** | Compare KuCoin order-book depth with reported volume | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior. Under the 16 Nov 2026 one-hop amendment, a transfer to an exchange counts as a sale only with a team-attributed exchange account, evidence of a sale, or no plausible published reason.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.

- Research only. Not investment advice.
