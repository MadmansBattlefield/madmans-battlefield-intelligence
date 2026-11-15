---
ticker: JASMY
name: JasmyCoin
chain: ethereum
contract: "0x7420B4b9a0110cdC71fB720908340C03F9Bc03EC"
overall_score: 2.8
overall_verdict: FAIL
section_scores:
  revenue: 1
  foundation_team: 3
  insider_holdings: 3
  selling_behavior: 2
  tokenomics_supply: 7
  liquidity_market: 5
  product_development: 2
  adoption_customers: 1
  security_audits: 5
  regulatory: 3
  catalysts: 2
gates_failed: [revenue, selling_behavior]
red_lines:
  admin_or_mint: none (plain ERC-20)
  deployer_exchange_deposits: "yes (~1.99B to Gate.io, 2023 – Jan 2025)"
  pump_day_exchange_deposit_linked_to_issuer: "unverified (29 Sep 2026)"
price_usd: 0.003214
price_source: "CoinGecko, 14 Nov 2026 12:12 PM MST"
last_updated: 2026-11-14
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### JASMY · Overall grade **2.8 / 10 · ❌ FAIL**

**Summary:** A plain, fully minted 50B ERC-20 with no admin keys, but no revenue, no verifiable product usage and no disclosed issuer. The deployer wallet has fed about 2B JASMY into a Gate.io deposit address over the years, and JASMY is no longer listed on Upbit.

**Sections passed: 1 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 1/10 | ❌ FAIL |
| 🏛️ Foundation & team | 3/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 3/10 | ❌ FAIL |
| 📉 Selling behavior | 2/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 7/10 | ✅ PASS |
| 💧 Liquidity & market | 5/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 2/10 | ❌ FAIL |
| 🤝 Adoption & customers | 1/10 | ❌ FAIL |
| 🛡️ Security & audits | 5/10 | ❌ FAIL |
| ⚖️ Regulatory | 3/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 2/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 JASMY · JasmyCoin · 2.8 / 10 · ❌ FAIL

> **One line:** A plain, fully minted 50B ERC-20 with no admin keys, but no revenue, no verifiable product usage and no disclosed issuer. The deployer wallet has fed about 2B JASMY into a Gate.io deposit address over the years, and JASMY is no longer listed on Upbit.

| 📊 Market (CoinGecko + DexScreener, 14 Nov 2026 ~12:12 PM MST) | 🔗 On-chain (Ethereum RPC + Blockscout, 14 Nov 2026) |
|---|---|
| **Price** $0.003214 | **Token** `0x7420…03EC` "JasmyCoin" · Solidity 0.5.15 · verified |
| **24h / 7d / 30d** 🔴 −6.1% / −12.5% / −32.1% | **Supply** 50,000,000,000, all minted 26 Dec 2019 to the deployer |
| **Market cap** $159.0M · **FDV** $160.8M | **Functions** approve / transfer / transferFrom / allowance only. **No owner, mint, pause or blacklist** |
| **24h volume** $6.79M | **Deployer** `0xf4a5…7BE9` holds 555,000,322 (1.11%) |
| **ATH** $4.79 (15 Feb 2021) · now −99.93% | **Holders** 102,120 |
| **Circulating (CoinGecko)** 49.44B | **Top 4 wallets** ~3.54–3.60B each, funded by Coinbase |

---

## 💰 Revenue — Does it make money? · 1/10 · ❌ FAIL

| Metric | Value | Source |
|---|---|---|
| Protocol fees or revenue | **None found** (no DefiLlama listing) | [Tier A] DefiLlama (absence) |
| Value accrual to the token | **None.** The contract has no fee, burn or buyback logic | [Tier A] verified source |
| Company revenue | Jasmy Corp is private; no figures | Not found |

**What it means:** Nothing ties token value to any business income.

## 🏛️ Foundation & team — Who is in charge? · 3/10 · ❌ FAIL

| Item | Finding | Source |
|---|---|---|
| Issuer | Jasmy Corporation (Japan) per public materials. The entity and its link to the token were **not verified** from a registry | [Unverified] |
| On-chain control | None. The token has no owner or admin | [Tier A] verified source |
| Deployer | `0xf4a5b232DF2De4dd6ad613ba17C3113CEf707BE9` (Blockscout "Jasmy Deployer") | [Tier A] |
| MultiSigWallet | `0xB0D8Cf2436Ee7a1303dcDA2342611d256EFA5C3a` holds 1.296B with active in/out to `0x28f2E788…`. **Owner unknown** | [Tier A] balance · owner [Unverified] |

**What it means:** No primary document links a named, accountable issuer to the token wallets.

## 🪙 Foundation / team holdings — How many coins do they hold? · 3/10 · ❌ FAIL

| Wallet | Label | 14 Nov 2026 | % supply | Notes |
|---|---|---:|---:|---|
| `0xf4a5…7BE9` | Jasmy Deployer | 555,000,322 | 1.11% | Has sent out 49.445B in total |
| `0xB0D8…5C3a` | MultiSigWallet, owner unknown | 1,296,095,740 | 2.59% | Active |
| `0x10287883…` | Received 4,999,999,999 from the deployer on 8 Oct 2020 | — | — | Role [Unverified] |
| 4 EOAs | ~3.54–3.60B each (~28.7% total), funded by Coinbase Hot Wallet `0xA9D1e08C…` in Oct and Dec 2025 | ~14.3B | ~28.7% | Likely Coinbase custody, **not insiders** [Unverified] |
| Exchanges | Binance 8 1.94B, Binance 28 1.63B, plus Crypto.com, eToro, Revolut, Coinbase, MEXC, Kraken, BtcTurk | — | — | [Tier A] Blockscout labels |

**What it means:** The known insider balance today is small (~1–4%), but where the deployer's 5B of 2020 went is unknown, so the full insider stake is unclear.

## 📉 Selling behavior — Do insiders sell into pumps? · 2/10 · ❌ FAIL

**Pump test:** 38 of 360 days had a ≥10% 5-day rise (CoinGecko). The runs were 22–28 Aug and 21 Sep–2 Oct 2026.

| Date | Flow | Source |
|---|---|---|
| 2023 – 16 Jan 2025 | The deployer sent many tranches to `0xa2A3d0d99EC9f3dBd73F36b600A05C89ddF3390f`, which forwards within ~1 hour to **Gate.io Hot Wallet** `0x0D0707963952f2fBA59dD06f2b425ace40b492Fe` (a Gate deposit pattern). **~1.99B in total.** Examples: 26 Jun 2023 770M · 1 Aug 2023 140M · 27 Sep 2024 95.1M · **16 Jan 2025 50M** (last deployer send, tx `0x2f3ba2a6f73d…`) | [Tier A] Blockscout transfers |
| **29 Sep 2026** (5-day **+21.8% 🔴 pump**) | `0x722E6c8ef971338BdB46D4e7924E392D6f2a5b50` (a contract wallet that received 249,999,000 from Binance 14 on 16 Sep 2026 and still holds 150M) sent 43.5M (tx `0x816c67ec404493b8…`) and 50M (tx `0xc20fe5c8ae95660e…`) to the **same** Gate deposit address `0xa2A3…`. They were forwarded to Gate at 05:31 UTC (tx `0x0d8b7e86…`) and 07:30 UTC (tx `0x8840f8f6…`), i.e. 10:31 PM MST on 28 Sep and 12:30 AM MST on 29 Sep | [Tier A] transfers · link to Jasmy **[Unverified]** (shared-deposit-address heuristic) |

**What it means:** The deployer has a long record of undisclosed exchange deposits. On a 2026 pump day, a wallet using the same deposit address sold 93.5M. That shared address is a strong hint, but it is not proof of an issuer link.

## 📊 Tokenomics & supply · 7/10 · ✅ PASS

| Item | Value | Source |
|---|---|---|
| Max / total | 50,000,000,000, all minted at deploy (26 Dec 2019) | [Tier A] |
| Mint / burn functions | None | [Tier A] verified source |
| Circulating | 49.44B (98.9%) | [Tier B] CoinGecko |
| Unlock schedule | No vesting contract. Unlocks are whatever wallets choose to move | [Tier A] |

**What it means:** No new supply can ever be created, and almost all of it already circulates. The risk is distribution, not inflation.

## 💧 Liquidity & market · 5/10 · ❌ FAIL

| Venue | 24h volume (approx.) | Source |
|---|---:|---|
| HTX | $1.42M | [Tier B] CoinGecko tickers |
| Binance | $880k | [Tier B] |
| Coinbase | $610k | [Tier B] |
| BloFin, WhiteBIT, Poloniex | smaller | [Tier B] |
| Upbit | **No JASMY market** | [Tier A] Upbit market API (delisting date [Unverified]) |
| DEX total | **~$70.6k** liquidity (Uniswap JASMY/WETH $37k) | [Tier A] DexScreener API |

**What it means:** Still on Binance and Coinbase, but volume is thin for a $159M cap, and on-chain depth is negligible.

## 🧑‍💻 Product & development · 2/10 · ❌ FAIL

- No on-chain product contract or usage metric tied to the token was found (Not found).
- IoT and data-sovereignty product claims are marketing only ([Unverified]).

**What it means:** Nothing on-chain shows a product using the token.

## 🤝 Adoption & customers · 1/10 · ❌ FAIL

- No named customer, filing or usage dashboard was verified (Not found).
- About 28.7% of supply in Coinbase-funded custody wallets reflects exchange custody, not product adoption.

**What it means:** No verifiable adoption.

## 🛡️ Security & audits · 5/10 · ❌ FAIL

| Item | Finding | Source |
|---|---|---|
| Contract | Minimal ERC-20, no admin. Nobody can freeze, mint or upgrade | [Tier A] |
| Compiler | Solidity 0.5.15 (old, but a simple surface) | [Tier A] |
| Audit | Not found | Not found |
| Hacks | None found for JASMY | [Tier B] |

**What it means:** The code risk is low because there is almost no code. With no audit on file, it cannot score higher.

## ⚖️ Regulatory · 3/10 · ❌ FAIL

- Upbit: no JASMY market today ([Tier A] Upbit API). Date and reason of removal [Unverified]; earlier notes said 14 Sep 2026.
- BITPOINT / SBI VC notices (28 Oct 2026, earlier notes): **[Unverified]**. Neither venue appears in CoinGecko's ticker list.
- No MiCA white paper or other filing found (Not found).

**What it means:** It has lost at least one major regulated venue, and no compliance documents exist.

## 📅 Catalysts & calendar · 2/10 · ❌ FAIL

| Date | Event | Source |
|---|---|---|
| — | No scheduled unlock (fully minted) | [Tier A] |
| — | No confirmed product, listing or governance event | Not found |
| Watch | Further Japanese exchange actions (BITPOINT / SBI VC) | [Unverified] |

**What it means:** No positive catalysts are visible. The only known risk events are delistings.

## 🚩 Red lines status

| Red line | Status | Evidence |
|---|---|---|
| Admin key, mint or pause | 🟢 None | Verified source |
| Deployer exchange deposits | 🔴 Yes | ~1.99B to Gate via `0xa2A3…`, last 16 Jan 2025 |
| Pump-day exchange deposit tied to the issuer | 🟡 Possible, unproven | 29 Sep 2026, 93.5M via the same Gate deposit address |
| Delisted from a major venue | 🔴 Yes (Upbit) | Upbit market API |

## 📚 Sources

- [Tier A] Ethereum RPC and eth.blockscout.com: verified source, holders, labels and transfers for the deployer, `0xa2A3…`, `0x722E…` and the MultiSigWallet, 14 Nov 2026
- [Tier A] Upbit public market API (no JASMY market)
- [Tier A] DexScreener tokens API · DefiLlama (no listing)
- [Tier B] CoinGecko markets, tickers and daily closes, 14 Nov 2026
- [Unverified] Issuer entity; Upbit delisting date; BITPOINT / SBI VC notices; owner of the MultiSigWallet; Jasmy link to `0x722E…`; role of `0x10287883…`

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
