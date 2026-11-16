---
ticker: DUSK
name: Dusk
chain: dusk (native) / ethereum (ERC20)
contract: "0x940a2db1b7008b6c776d4faaca729d6d4a4aa551"
overall_score: 4.0
overall_verdict: FAIL
section_scores:
  revenue: 1
  foundation_team: 6
  insider_holdings: 5
  selling_behavior: 5
  tokenomics_supply: 4
  liquidity_market: 4
  product_development: 6
  adoption_customers: 2
  security_audits: 6
  regulatory: 5
  catalysts: 4
gates_failed: [revenue]
red_lines:
  hack_exploit: "none found"
  mint_path_live: "yes, protocol emission (~62.6M DUSK a year, ~10% of supply) to stakers and a 10% development fund"
  team_wallet_to_exchange_during_pump: "not testable on the native chain; largest ERC20 EOAs are Binance / Bitvavo withdrawals, not team"
  treasury_in_single_key_wallets: "unknown (development-fund wallet not published)"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "No revenue to speak of; staking is paid by emission."
pump_day_price_source: "Gate DUSK/USDT daily closes"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions: []
price_usd: 0.062035
price_source: "CoinGecko, 16 Nov 2026 8:34 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### DUSK · Overall grade **4.0 / 10 · ❌ FAIL**

**Summary:** Dusk is a privacy-focused layer 1 for regulated assets; its mainnet has been live since Jan 2025. DUSK pays gas and staking. **There is essentially no fee revenue.** A 2,000-block sample of mainnet (16 Nov 2026) held **68 transactions in 5.6 hours** (~290 a day), and DefiLlama tracks no fees or TVL. Supply grows by protocol emission of 19.86 DUSK a block, about 62.6M a year or **~10% of current supply**, with 10% of every block reward going to a development fund. Engineering is active (Rusk 1.7.3 security release, DuskEVM testnet). The initial allocation finished vesting in 2022. Revenue trips the hard gate.

**🚨 Top warning:** Usage is close to nil while issuance runs at about 10% a year. Live supply is 614,751,130 DUSK ([supply.dusk.network](https://supply.dusk.network)), up from 500M at genesis, and every new token is paid to stakers or the development fund rather than earned from fees. The price is −46.7% over 30 days, and Binance restricted DUSK trading for users in Brazil on 27 Oct 2026 [Tier B].

**Sections passed: 3 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 1/10 | ❌ FAIL |
| 🏛️ Foundation & team | 6/10 | ✅ PASS |
| 🪙 Foundation / team holdings | 5/10 | ❌ FAIL |
| 📉 Selling behavior | 5/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 4/10 | ❌ FAIL |
| 💧 Liquidity & market | 4/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 6/10 | ✅ PASS |
| 🤝 Adoption & customers | 2/10 | ❌ FAIL |
| 🛡️ Security & audits | 6/10 | ✅ PASS |
| ⚖️ Regulatory | 5/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 4/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 DUSK · Dusk · 4.0 / 10 · ❌ FAIL

> **One line:** Real engineering and a live mainnet, but no fee income and a 10%-a-year emission schedule paying for security.

| 📊 Market (CoinGecko, 16 Nov 2026 8:34 AM MST) | 🔗 On-chain (16 Nov 2026) |
|---|---|
| **Price** $0.0620 · 24h / 7d / 30d 🔴 −1.7% / −13.5% / −46.7% · 1y +6.7% | **Native supply** 614,751,130 DUSK (supply.dusk.network); max 1B |
| **Market cap** $38.1M · rank #488 | **Mainnet height** 5,778,972 (Dusk node GraphQL) |
| **24h volume** $2.49M: HTX $0.95M, BloFin $0.60M, Binance $0.20M | **ERC20** [`0x940a…a551`](https://etherscan.io/address/0x940a2db1b7008b6c776d4faaca729d6d4a4aa551): 500M issued; [`0x36B8…084F`](https://etherscan.io/address/0x36B8e0B938c0172c20e14cc32E7f0e51dCf1084F) migration 115.2M · [`0xE75D…C339`](https://etherscan.io/address/0xE75Df3C68906f6AdbE17e87d4e22509Fde24C339) burner 50.0M |
| **ATH** $1.09 (29 Dec 2021) · now −94.3% | **ERC20 holders** 20,176 (Blockscout) |

---

## 💰 Revenue — Does it make money? · 1/10 · ❌ FAIL

| Metric | Value | Source |
|---|---:|---|
| Mainnet activity | 68 transactions in 2,000 blocks (5.6 h) ≈ 290 a day | [Tier A] Dusk node GraphQL `blocks`, heights 5,776,972–5,778,971 |
| Gas used in sample | 1.045B gas ≈ 1 DUSK of fees at the 1-LUX minimum gas price | [Tier A] same; price assumption [inference] |
| DefiLlama fees / TVL | Not listed | [Tier A] api.llama.fi |

- All fees go to block producers and committees with the block reward; nothing accrues to holders except through staking.

**What it means:** no revenue to speak of. **1 (hard gate).**

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** No revenue to speak of; staking is paid by emission.

## 🏛️ Foundation & team — Who is in charge? · 6/10 · ✅ PASS

- A long-running team (project since 2018) shipping regular public releases: Rusk 1.7.3 (5 Nov 2026), Web Wallet 2.0.0, block explorer 1.7.x ([Dusk developer update, 2–9 Nov 2026](https://docs.dusk.network/updates/developer/2026-11-02-to-2026-11-09/), Tier A).
- The development fund receives 10% of every block reward (~6.3M DUSK a year) ([tokenomics](https://docs.dusk.network/learn/tokenomics/), Tier A). Its wallet is not published.

## 🪙 Foundation / team holdings — How many coins do they hold? · 5/10 · ❌ FAIL

| Initial allocation | DUSK | Vested |
|---|---:|---|
| Token sale | 250M (50%) | — |
| Development | 90.5M (18.1%) | Fully by Apr 2022 |
| Exchange | 59M (11.8%) | Fully by Apr 2022 |
| Marketing | 36.5M (7.3%) | Fully by Apr 2022 |
| Team / Advisors | 32M / 32M (6.4% each) | Fully by Apr 2022 |

*Source: [Tier A] [Dusk tokenomics docs](https://docs.dusk.network/learn/tokenomics/).*

- On Ethereum, the largest non-contract holders ([`0xed73…E10a`](https://etherscan.io/address/0xed731C285683bEDF3B6C640C7714642747a1E10a) 39.2M, [`0xAf3d…36b8`](https://etherscan.io/address/0xAf3db0b61a3db3Ce0BAdD127499A5B337f7936b8) 29.5M, [`0x26c9…6486`](https://etherscan.io/address/0x26c971A130376299C2B6EF136AFfB93E46126486) 28.0M) were all filled from Binance hot wallets in 2026 (Arkham: "DUSK Whale" tags, Binance Hot Wallet senders). They look like whales or custody wallets, not team.
- Arkham ([Tier B] Arkham, read 16 Nov 2026 (signed-in account)) labels [0x36B8](https://intel.arkm.com/explorer/address/0x36B8e0B938c0172c20e14cc32E7f0e51dCf1084F) DUSKMigration and [0x8787](https://intel.arkm.com/explorer/address/0x8787BbE53920B33411F7C9A91Ac321AF1ea1aa2d) DuskMainnetOnramp (106.1M). The on-ramp's largest inflows were 10M DUSK from Dusk Network and 50M from Efficient Frontier, a market maker, moving tokens to the native chain.
- Native-chain balances (shielded and public Moonlight accounts) could not be ranked. The team's and development fund's current holdings are **Not found**.

## 📉 Selling behavior — Do insiders sell into pumps? · 5/10 · ❌ FAIL

*Gate DUSK/USDT daily closes (UTC): **68 pump days** in the last 365, an extremely volatile market.*

- No team wallet is identifiable, so a direct test isn't possible.
- The only pump-day outflow among the top ERC20 EOAs was [1.6M DUSK to Bitvavo on 19 Oct 2026](https://etherscan.io/tx/0x5f82c54ca00e78e7b40fbbf1ac61131d9eba9a07c7165ac1b9b3c516cc5592b1), from [`0xb0A3…4411`](https://etherscan.io/address/0xb0A3A2B60E969AFD26561429Aa4c1444C57E4411). **Correction:** Arkham labels `0xb0A3…4411` itself a **Bitvavo Cold Wallet** (centralized exchange), so this was Bitvavo moving its own inventory, not an insider sale.

**What it means:** no evidence either way. **5**.

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from Gate DUSK/USDT daily closes.

## 📊 Tokenomics & supply · 4/10 · ❌ FAIL

- 500M at genesis, plus 500M emitted over 36 years (geometric decay, halving every 4 years). Years 0–4 emit 250.48M (19.8574 DUSK per block) [Tier A docs].
- 114.75M emitted so far (614.75M live, which matches 5.78M blocks × 19.86). That is ~62.6M a year, ~10% of current supply.
- 10% of rewards go to the development fund; undistributed generator credits are burned (small).

## 💧 Liquidity & market · 4/10 · ❌ FAIL

- $2.49M of 24h volume on a $38M cap. The top venue is HTX; Binance spot is only $0.2M.
- Binance restricted DUSK in Brazil on 27 Oct 2026 [Tier B, CoinMarketCap news].

## 🧑‍💻 Product & development · 6/10 · ✅ PASS

- Mainnet live; DuskEVM on testnet since 10 Aug 2026; Boreas upgrade on 12 May 2026 [Tier B]. Active public repos and weekly developer updates [Tier A].

## 🤝 Adoption & customers · 2/10 · ❌ FAIL

- ~290 transactions a day, no DefiLlama TVL, and the NPEX securities dApp not yet deployed [Tier B]. Institutional use is not visible on-chain.

## 🛡️ Security & audits · 6/10 · ✅ PASS

- No exploit found. The 1.7.3 security update shipped on 5 Nov 2026. The ERC20 migration and on-ramp contracts hold 221M DUSK.

## ⚖️ Regulatory · 5/10 · ❌ FAIL

- Positioned for EU-regulated assets (MiCA / DLT Pilot), with no enforcement found. Exchange-level restrictions (Binance Brazil) are a mild negative.

## 📅 Catalysts & calendar · 4/10 · ❌ FAIL

| Date | Event |
|---|---|
| Unscheduled | DuskEVM mainnet |
| Unscheduled | NPEX regulated-securities dApp |
| ~Jan 2029 | First emission halving (year 4) |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | 🟡 Not testable (no published team wallets) |
| Live mint path | 🔴 Protocol emission ~10% a year |
| Treasury in single-key wallets | 🟡 Unknown |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| Largest ERC20 EOAs | Exchanges | Etherscan labels | medium | no | None |

## 📚 Sources

- [Tier A] Methodology update 16 Nov 2026: no new Arkham lookups; the attribution table uses evidence already cited in this report.
- [Tier A] Dusk node GraphQL (`nodes.dusk.network`) block sample, read 16 Nov 2026 ~10:45 AM MST; [supply.dusk.network](https://supply.dusk.network)
- [Tier A] [Dusk tokenomics](https://docs.dusk.network/learn/tokenomics/) · [developer update 2–9 Nov 2026](https://docs.dusk.network/updates/developer/2026-11-02-to-2026-11-09/)
- [Tier A] Blockscout / Etherscan v2 for the ERC20 holders and transfers
- [Tier B] [CoinMarketCap DUSK news](https://coinmarketcap.com/cmc-ai/dusk/latest-updates/)
- [Tier B] Arkham, read 16 Nov 2026 (signed-in account): DUSKMigration and DuskMainnetOnramp contracts; Bitvavo Cold Wallet on 0xb0A3; DUSK Whale tags on the Binance-funded holders. Arkham does not cover the native Dusk chain
- [Tier A] CoinGecko `dusk-network` (16 Nov 2026 8:34 AM MST); Gate DUSK/USDT daily candles

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Live supply 614.75M | [supply.dusk.network](https://supply.dusk.network) | A | 16 Nov 2026 |
| Emission schedule; 10% dev fund | [docs](https://docs.dusk.network/learn/tokenomics/) | A | 16 Nov 2026 |
| Pump-day 1.6M Bitvavo cold → Bitvavo (exchange-internal) | [tx](https://etherscan.io/tx/0x5f82c54ca00e78e7b40fbbf1ac61131d9eba9a07c7165ac1b9b3c516cc5592b1) | A | 16 Nov 2026 |
| Migration contract 115.2M | [contract](https://etherscan.io/address/0x36B8e0B938c0172c20e14cc32E7f0e51dCf1084F) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Native-chain team and fund wallets** | Arkham does not cover the Dusk chain. Ask Dusk to publish its native team and fund addresses | Free |
| 2 | **Development-fund wallet** | Ask Dusk for the Moonlight address that receives the 10% share, then track its outflows | Free |
| 3 | **Real fee income** | Sum `gasSpent × gasPrice` over 30 days via the node GraphQL | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
