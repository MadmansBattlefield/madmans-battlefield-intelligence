---
ticker: TLOS
name: Telos
chain: telos
contract: "native (Telos, an Antelope/EOSIO chain with Telos EVM); ERC20 0x193f4a4a6ea24102f49b931deeeb931f6e32405d"
overall_score: 3.0
overall_verdict: FAIL
section_scores:
  revenue: 1
  foundation_team: 3
  insider_holdings: 4
  selling_behavior: 3
  tokenomics_supply: 4
  liquidity_market: 3
  product_development: 4
  adoption_customers: 2
  security_audits: 5
  regulatory: 4
  catalysts: 3
gates_failed: [revenue, selling_behavior]
red_lines:
  hack_exploit: "none found in the review window"
  mint_path_live: "yes: token contract max supply 1B vs 467.6M issued; issuance is controlled by the eosio system account"
  team_wallet_to_exchange_during_pump: "yes: the Foundation-funded expenses account telosliquidi sent 500k TLOS to Bitget (13 Jan 2026, +14.4%) and 200k to Bitrue (7 May 2026, +70.7%)"
  treasury_in_single_key_wallet: "the Foundation account tf can be moved by any one of three controlling accounts (threshold 1)"
price_usd: 0.01266
price_source: "CoinGecko, 16 Nov 2026 7:56 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### TLOS · Overall grade **3.0 / 10 · ❌ FAIL**

**Summary:** Telos is an EOSIO/Antelope chain with a Telos EVM layer. It earns almost nothing (**$3.5k of fees in a year**, $2.0M of DeFi TVL) and the price is **−99.1% from its 2022 high**. The Telos Foundation pays its costs from a "Liquidity & Expenses" account, `telosliquidi`, which payroll memos tie to the Foundation. That account regularly sends TLOS to exchange deposit accounts, including **two deposits on pump days in the last year**: 500k TLOS to Bitget on 13 Jan 2026 (+14.4%) and 200k to Bitrue on 7 May 2026, the day of the year's biggest spike (+70.7%). Revenue and Selling both trip the hard gates.

**🚨 Top warning:** Foundation money goes to exchanges on pump days. The Foundation account [`tf`](https://explorer.telos.net/account/tf) funds [`telosliquidi`](https://explorer.telos.net/account/telosliquidi) (e.g. [3,684,700 TLOS "Ops and Expenses" on 14 Oct 2026](https://explorer.telos.net/transaction/95b535bc836005960ba43fcdff034610395e81c54d028149f91ee024d39a5e03)). `telosliquidi` sent [500,000 TLOS to Bitget's deposit account](https://explorer.telos.net/transaction/eba91c28a92878746c4cad2d4bb99172f9c79e697ed45ffb0f6790937ba42168) on 13 Jan 2026 and [200,000 TLOS to Bitrue](https://explorer.telos.net/transaction/2aac473efa757cc186e47af4632666195440ddd4864ba270e9e75b9801aaa155) on 7 May 2026. Between Aug and Oct 2025 it also made 10 deposits to HTX, KuCoin, MEXC, Gate, ProBit and Bitget. The dollar amounts are small (~$15k on the two pump days), but no sale was announced. Every link is in the 🔗 Evidence trail below.

**Sections passed: 0 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 1/10 | ❌ FAIL (hard gate) |
| 🏛️ Foundation & team | 3/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 4/10 | ❌ FAIL |
| 📉 Selling behavior | 3/10 | ❌ FAIL (hard gate) |
| 📊 Tokenomics & supply | 4/10 | ❌ FAIL |
| 💧 Liquidity & market | 3/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 4/10 | ❌ FAIL |
| 🤝 Adoption & customers | 2/10 | ❌ FAIL |
| 🛡️ Security & audits | 5/10 | ❌ FAIL |
| ⚖️ Regulatory | 4/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 3/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 TLOS · Telos · 3.0 / 10 · ❌ FAIL

> **One line:** A tiny-fee chain whose Foundation expense account feeds exchange deposits, including on pump days.

| 📊 Market (CoinGecko, 16 Nov 2026 7:56 AM MST) | 🔗 On-chain ([Telos API](https://mainnet.telos.net/v1/chain/get_info), 16 Nov 2026 ~8:00 AM MST) |
|---|---|
| **Price** $0.01266 | **Head block** 499,629,433 |
| **24h / 7d / 30d** 🔴 −1.4% / −10.7% / −25.2% · 1y −64.5% | **Supply** 467,563,681 of a 1,000,000,000 contract max |
| **Market cap** $5.73M · **FDV** $5.92M | **Telos EVM (`eosio.evm`)** 214.1M TLOS · **REX** 141.9M |
| **24h volume** $307k (KuCoin, MEXC, KoinBX, HTX, Gate) | **Fees** $3,511 in 12 months · $262 in 30 days (DefiLlama) |
| **ATH** $1.43 (7 Feb 2022) · now −99.1% | **DeFi TVL** $2.01M (DefiLlama) |
| **Pump days, last 365 days** 48 (CoinGecko daily closes; largest +70.7% on 7 May 2026) | **Foundation-linked accounts** ~49M TLOS (10.6%) |

---

## 💰 Revenue — Does it make money? · 1/10 · ❌ FAIL (hard gate)

| Metric | Value | Source |
|---|---:|---|
| Chain fees, last 12 months | **$3,511** (30 days: $262) | [Tier A] [DefiLlama `telos` fees](https://api.llama.fi/summary/fees/telos?dataType=dailyFees) |
| Revenue to holders | **$0** | No fee capture |

**What it means:** **1 → hard-gate FAIL.**

## 🏛️ Foundation & team — Who is in charge? · 3/10 · ❌ FAIL

- The Telos Foundation (`tf`) runs ecosystem spending. Its `active` permission is held by three accounts with a **threshold of 1**, so any one of them can move funds ([`tf` permissions](https://explorer.telos.net/account/tf)). Payroll is paid from `telosliquidi` with memos such as "L&E Payroll" and "June Salary".
- The `exrsrv.tf` economic reserve is controlled by the `eosio` system account and pays REX, EVM and grant accounts daily.

## 🪙 Foundation / team holdings — How many coins do they hold? · 4/10 · ❌ FAIL

| Account | TLOS | Role |
|---|---:|---|
| [`ptlosmigrate`](https://explorer.telos.net/account/ptlosmigrate) | 13.52M | pTLOS migration contract top-up |
| [`tedp4holding`](https://explorer.telos.net/account/tedp4holding) | 10.00M | TEDP holding |
| [`treasury.tcd`](https://explorer.telos.net/account/treasury.tcd) | 6.78M | Core-developer treasury (3-of-4 multisig) |
| [`exrsrv.tf`](https://explorer.telos.net/account/exrsrv.tf) | 5.67M | Economic reserve (system-controlled) |
| [`ignitegrants`](https://explorer.telos.net/account/ignitegrants) | 5.23M | Grants (4-of-6 multisig) |
| [`tlosfuelfund`](https://explorer.telos.net/account/tlosfuelfund) | 4.56M | Fuel fund |
| [`tffundsvault`](https://explorer.telos.net/account/tffundsvault) | 3.68M | Foundation vault (2-of-2), funded 12 Nov 2026 |

- About **49.4M TLOS (10.6% of supply)** sits in Foundation or governance accounts, read from the [top-holder list](https://mainnet.telos.net/v2/state/get_top_holders?contract=eosio.token&symbol=TLOS&limit=15). Holdings on the EVM side (214M in `eosio.evm`) were not attributed.

## 📉 Selling behavior — Do insiders sell into pumps? · 3/10 · ❌ FAIL (hard gate)

| Date (UTC day / MST time) | Flow | TLOS | Evidence |
|---|---|---:|---|
| 13 Jan 2026 (12 Jan 5:15 PM MST) · pump +14.4% | `telosliquidi` → `bitgetdetlos` (Bitget deposit, memo) | 500,000 (~$11.3k) | [tx](https://explorer.telos.net/transaction/eba91c28a92878746c4cad2d4bb99172f9c79e697ed45ffb0f6790937ba42168) |
| 7 May 2026 8:17 AM MST · pump +70.7% | `telosliquidi` → `bitruewallet` (Bitrue deposit, memo) | 200,000 (~$3.7k) | [tx](https://explorer.telos.net/transaction/2aac473efa757cc186e47af4632666195440ddd4864ba270e9e75b9801aaa155) |
| 12 Jan 2026 (pump +10.8%) | `eosio.evm` → `telosliquidi` withdrawal just before the Bitget deposit | 1,400,000 | [tx](https://explorer.telos.net/transaction/66d9fa72feeabcbf91e5112cf1929a9478a036cea64daa25f5bfc2ad72d79b63) |
| 14 Oct 2026 8:53 AM MST · pump +11.1% | `tf` → `telosliquidi` "Ops and Expenses" | 3,684,700 | [tx](https://explorer.telos.net/transaction/95b535bc836005960ba43fcdff034610395e81c54d028149f91ee024d39a5e03) (moved on to `tffundsvault` on 12 Nov) |

- Earlier, Aug–Oct 2025, `telosliquidi` made 10 more memo-tagged deposits (50k–200k each, 830k in total) to HTX, KuCoin, MEXC, Gate, ProBit and Bitget accounts, e.g. [200k to HTX on 24 Sep 2025](https://explorer.telos.net/transaction/d11a7214d919d04f4eb8e4d613dda6d55f9d77d1671fd85b187fb84811bcee97).
- Some coins came back (264k from Bitrue in Aug 2026, 500k from MEXC on 14 Nov 2026), consistent with an operating account that sells to pay costs and sometimes withdraws. No sale was announced.
- **Score 3:** a Foundation-funded account deposited to exchanges on two pump days in the window, without disclosure. The amounts are small.

## 📊 Tokenomics & supply · 4/10 · ❌ FAIL

- 467.6M issued against a **1B maximum** on the token contract ([currency stats](https://mainnet.telos.net/v1/chain/get_currency_stats)), so more than half the cap can still be issued by the `eosio` system account under governance. The economic reserve pays REX, EVM and grant rewards every day.

## 💧 Liquidity & market · 3/10 · ❌ FAIL

- $307k of 24h volume (5.4% of cap) spread over mid-tier exchanges. Small in absolute terms; the 48 pump days show a thin book.

## 🧑‍💻 Product & development · 4/10 · ❌ FAIL

- Telos EVM is live and holds most of the supply. Little measurable product traction.

## 🤝 Adoption & customers · 2/10 · ❌ FAIL

- $2.0M of DeFi TVL and $262 of monthly fees.

## 🛡️ Security & audits · 5/10 · ❌ FAIL

- No exploit found. The Foundation account's 1-of-3 control is a key-person risk.

## ⚖️ Regulatory · 4/10 · ❌ FAIL

- No enforcement found. Foundation spending is not reported in audited accounts.

## 📅 Catalysts & calendar · 3/10 · ❌ FAIL

| Date | Event |
|---|---|
| None dated | No scheduled upgrade or unlock found |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | 🔴 Yes: 500k to Bitget (13 Jan 2026), 200k to Bitrue (7 May 2026) |
| Live mint path | 🟡 Up to 1B on the token contract, system-controlled |
| Foundation account control | 🔴 1-of-3 |

## 📚 Sources

- [Tier A] Telos chain API (`get_info`, `get_currency_stats`, `get_currency_balance`, `get_account`) and Hyperion history (`get_actions` for the Foundation, reserve, grant and expense accounts; `get_transaction` for each linked tx, all `executed: true`); `get_top_holders`; read 16 Nov 2026 ~7:58–8:40 AM MST
- [Tier A] DefiLlama `telos` fees and chain TVL; CoinGecko `telos` (16 Nov 2026 7:56 AM MST) and 365-day closes for pump days
- Exchange ownership of `bitgetdetlos`, `bitruewallet`, `htxtlosmjuxn`, `kucoin4telos`, `mexcmexctlos`, `gateioiotlos`, `probitandtls` is inferred from the account names and numeric deposit memos [Tier B]
- [Tier B] Arkham, network list read 16 Nov 2026 ~7:35 AM MST (signed-in account): **Telos (native or EVM) is not supported.** Arkham's network selector lists only Ethereum, Polygon, BNB Chain, Optimism, Avalanche, Arbitrum, Base, Bitcoin, Tron, Flare, Solana, Dogecoin, Zcash, HyperEVM, Hypercore, Robinhood Chain. No Arkham labels were available for this report

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Supply 467.6M of 1B max | [currency stats](https://mainnet.telos.net/v1/chain/get_currency_stats) | A | 16 Nov 2026 |
| Fees $3.5k / 12 months | [DefiLlama](https://api.llama.fi/summary/fees/telos?dataType=dailyFees) | A | 16 Nov 2026 |
| `tf` → `telosliquidi` 3.68M | [tx](https://explorer.telos.net/transaction/95b535bc836005960ba43fcdff034610395e81c54d028149f91ee024d39a5e03) | A | 16 Nov 2026 |
| Pump-day exchange deposits | [Bitget 13 Jan](https://explorer.telos.net/transaction/eba91c28a92878746c4cad2d4bb99172f9c79e697ed45ffb0f6790937ba42168) · [Bitrue 7 May](https://explorer.telos.net/transaction/2aac473efa757cc186e47af4632666195440ddd4864ba270e9e75b9801aaa155) | A | 16 Nov 2026 |
| Earlier exchange deposits | [HTX 24 Sep 2025](https://explorer.telos.net/transaction/d11a7214d919d04f4eb8e4d613dda6d55f9d77d1671fd85b187fb84811bcee97) · [account history](https://explorer.telos.net/account/telosliquidi) | A | 16 Nov 2026 |
| Foundation-linked balances | [top holders](https://mainnet.telos.net/v2/state/get_top_holders?contract=eosio.token&symbol=TLOS&limit=15) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Whether the exchange deposits were sales or market-making** | Ask the Telos Foundation for its L&E account reports | Free |
| 2 | **Foundation holdings on Telos EVM** | Check the EVM addresses linked to `telosliquidi` withdrawals on the Telos EVM explorer (Arkham does not cover Telos) | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.

- Research only. Not investment advice.
