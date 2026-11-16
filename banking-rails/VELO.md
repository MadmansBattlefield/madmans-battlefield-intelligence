---
ticker: VELO
name: Velo
chain: stellar
contract: "VELO-GDM4RQUQQUVSKQA7S6EM7XBZP3FCGH4Q7CL6TABQ7B2BEJ5ERARM2M5M (Stellar); BSC 0xf486ad071f3bee968384d2e39e2d8af0fcf6fd46"
overall_score: 3.6
overall_verdict: FAIL
section_scores:
  revenue: 1
  foundation_team: 5
  insider_holdings: 3
  selling_behavior: 4
  tokenomics_supply: 4
  liquidity_market: 4
  product_development: 5
  adoption_customers: 3
  security_audits: 6
  regulatory: 5
  catalysts: 4
gates_failed: [revenue]
red_lines:
  hack_exploit: "none found"
  mint_path_live: "no: Stellar issuer locked (master weight 0, thresholds 0), so no further issuance"
  team_wallet_to_exchange_during_pump: "not proven: no Stellar account is publicly attributed to Velo Labs (the labelled directory sits behind a payment wall)"
  entity_concentration: "top 10 Stellar accounts hold 49.3%; ~6.4B (27%) not counted as circulating"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "About $1.5k of fees in a year and no buyback, burn or fee share."
pump_day_price_source: "Gate VELO_USDT UTC daily closes, re-run 16 Nov 2026 with scripts/pump_day_test.py (50 of 360 days); the body's earlier count used no pump-day test in the body"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions: []
price_usd: 0.003042
price_source: "CoinGecko, 16 Nov 2026 ~8:40 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### VELO · Overall grade **3.6 / 10 · ❌ FAIL**

**Summary:** VELO is the utility token of Velo Labs, a payments company in Thailand. It is issued on Stellar, with a bridged BSC copy. Issuance is permanently closed because the Stellar issuer account is locked, which is the token's one structural positive. The token earns essentially nothing: DefiLlama tracks **$1,468 of fees over the past year ($81 in the last 30 days)** for the Velo Finance protocol. Ownership is opaque: the top 10 accounts hold 49.3% of supply, and none of them carries a public label. The revenue gate fails.

**🚨 Top warning:** concentration with no attribution. Two multisig accounts (a 2-of-4 holding **2.49B, 10.4%**, and a 4-of-6 holding **1.57B, 6.6%**) plus eight single-key accounts hold **49.3% of all VELO**. CoinGecko counts about **6.4B VELO (27%) as not circulating**. Which of these belong to Velo Labs is not disclosed on-chain. Promised staking and "Treasury as a Service" are still undated, and the project's Q3 2026 white-label partner had not been announced by Q3's end. Every link is in the 🔗 Evidence trail below.

**Sections passed: 1 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 1/10 | ❌ FAIL (hard gate) |
| 🏛️ Foundation & team | 5/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 3/10 | ❌ FAIL |
| 📉 Selling behavior | 4/10 | ❌ FAIL (not proven) |
| 📊 Tokenomics & supply | 4/10 | ❌ FAIL |
| 💧 Liquidity & market | 4/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 5/10 | ❌ FAIL |
| 🤝 Adoption & customers | 3/10 | ❌ FAIL |
| 🛡️ Security & audits | 6/10 | ✅ PASS |
| ⚖️ Regulatory | 5/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 4/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 VELO · Velo · 3.6 / 10 · ❌ FAIL

> **One line:** Supply is capped, but the token earns about $1.5k a year and half of it sits in unlabelled accounts.

| 📊 Market (CoinGecko, 16 Nov 2026 ~8:40 AM MST) | 🔗 On-chain ([Stellar Horizon](https://horizon.stellar.org/assets?asset_code=VELO&asset_issuer=GDM4RQUQQUVSKQA7S6EM7XBZP3FCGH4Q7CL6TABQ7B2BEJ5ERARM2M5M), 16 Nov 2026 ~8:50 AM MST) |
|---|---|
| **Price** $0.003042 | **Issued on Stellar** 23,949,595,872 VELO |
| **24h / 7d / 30d** 🟢 +0.7% / 🔴 −10.6% / −26.4% | **Holders** 43,124 trustlines |
| **Market cap** $53.4M · **FDV** $73.0M | **Circulating** 17.56B (CoinGecko) |
| **24h volume** $2.5M (Bybit $0.72M, KuCoin $0.37M, PointPay, Kraken, PancakeSwap, Gate) | **Top 10 accounts** 49.3% · top 2 multisigs 17.0% |
| **ATH** $2.29 (8 Mar 2021) · now −99.87% | **Issuer** locked (master weight 0) |
| **Pump days** 50 in the last year (largest +30.8% on 2 Oct 2026) | **In AMM pools / Soroban** 36.1M / 13.9M |

---

## 💰 Revenue — Does it make money? · 1/10 · ❌ FAIL (hard gate)

- DefiLlama's `velo-finance` record shows $1,468 of fees over 12 months and $81 over 30 days, with TVL of about $56k. There is no buyback, burn or fee share to VELO. **1 → hard-gate FAIL.**

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** About $1.5k of fees in a year and no buyback, burn or fee share.

## 🏛️ Foundation & team — Who is in charge? · 5/10 · ❌ FAIL

- Velo Labs is a company founded in 2018. A conglomerate backer is reported by one secondary source only ([Unverified]). The [official site](https://www.velo.org/) describes the payments, card and tokenized-treasury products. No audited accounts were found.

## 🪙 Foundation / team holdings — How many coins do they hold? · 3/10 · ❌ FAIL

| Stellar account | VELO | % | Control |
|---|---:|---:|---|
| [GCUAZ…HBTB](https://horizon.stellar.org/accounts/GCUAZB7ELECT4IVTNXYIDL4BVTJCNBAMX7MZLV4SOQ52Y6XOFVMOHBTB) | 2.49B | 10.4% | 2-of-4 multisig |
| [GDDHS…FLBK](https://horizon.stellar.org/accounts/GDDHS46N6OV6BE5BKYHYST6SOE5656G4RKKEVTEO6W4RCSVNWW26FLBK) | 1.57B | 6.6% | 4-of-6 multisig, no VELO payments in recent history |
| [GDQQO…DBWSU](https://horizon.stellar.org/accounts/GDQQOTRFDRZVBOFEJAEBN775RF5XE4AR35LZ4BGMDH4JB7KI7WEDBWSU) | 1.41B | 5.9% | Single key |
| [GCKPJ…CZTVJ](https://horizon.stellar.org/accounts/GCKPJE7UD6F57HZMAAGALCSKZCJPFO2MMAHMBBKWZPEPE6MFA7MCZTVJ) | 1.36B | 5.7% | Single key; active today |
| [GBMPX…GFQK7](https://horizon.stellar.org/accounts/GBMPXKDUX366F4S4DDEBRZGWJH4U3FFQMBQI22QRCE7P2PYON5DGFQK7) | 1.27B | 5.3% | Single key |

- None of these accounts sets a home domain, and labels could not be read (see 📉 below). Several are likely exchange hot wallets. Not proven either way, so the score is capped at 3.

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL (not proven)

- No Stellar account is publicly attributed to Velo Labs. The labelled account directory (stellar.expert) answered with HTTP 402 (payment required), so it was not used. With no team wallets identified, pump-day flows cannot be checked. **Not proven → 4.**

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from Gate VELO_USDT UTC daily closes, re-run 16 Nov 2026 with scripts/pump_day_test.py (50 of 360 days); the body's earlier count used no pump-day test in the body.

## 📊 Tokenomics & supply · 4/10 · ❌ FAIL

- Hard-capped at about 23.95B on Stellar, because the issuer is locked. CoinGecko counts 17.56B as circulating, leaving about 6.4B (27%) outside the float and able to enter the market.

## 💧 Liquidity & market · 4/10 · ❌ FAIL

- $2.5M of 24h volume (4.7% of market cap), with no venue above $0.75M.

## 🧑‍💻 Product & development · 5/10 · ❌ FAIL

- [Unverified] A card launched with a partner in Aug 2026, and a Binance.US listing followed in Jul 2026 (secondary sources only). The official site lists products marked "Coming in 2026".

## 🤝 Adoption & customers · 3/10 · ❌ FAIL

- No public usage numbers. DefiLlama TVL is about $56k.

## 🛡️ Security & audits · 6/10 · ✅ PASS

- The issuer is locked, with no clawback or revocation flags, so tokens cannot be minted, frozen or seized ([issuer account](https://horizon.stellar.org/accounts/GDM4RQUQQUVSKQA7S6EM7XBZP3FCGH4Q7CL6TABQ7B2BEJ5ERARM2M5M)). No exploit found. The BSC copy depends on a bridge.

## ⚖️ Regulatory · 5/10 · ❌ FAIL

- A payments and remittance focus in Southeast Asia brings licensing exposure. No enforcement found.

## 📅 Catalysts & calendar · 4/10 · ❌ FAIL

- VELO staking and Treasury-as-a-Service are promised for "Q4 2026 – 2027", with no date.

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | ⚪ Not proven (no attributed wallets) |
| Live mint path | 🟢 None (issuer locked) |
| Entity concentration | 🟠 49.3% in the top 10 unlabelled accounts |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| No Stellar account publicly attributed to Velo Labs | — | — | low | no | None: Selling not proven (4) |

## 📚 Sources

- [Tier A] Methodology update 16 Nov 2026: no new Arkham lookups; the attribution table uses evidence already cited in this report.
- [Tier A] Stellar Horizon: the asset record, the issuer account and a full crawl of holder accounts (43,124), 16 Nov 2026
- [Tier A] CoinGecko `velo`; pump days from CoinGecko 365-day closes
- [Tier A] DefiLlama `velo-finance` fees and TVL
- [Tier A] [velo.org](https://www.velo.org/)
- [Tier B] Secondary news on the card, the Binance.US listing and the roadmap (single sources, [Unverified])
- Not reached: stellar.expert account labels (HTTP 402). Arkham does not cover Stellar (16 Nov 2026); the BNB Chain copy of VELO was not looked up

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Issuer locked, no further mint | [issuer account](https://horizon.stellar.org/accounts/GDM4RQUQQUVSKQA7S6EM7XBZP3FCGH4Q7CL6TABQ7B2BEJ5ERARM2M5M) | A | 16 Nov 2026 |
| 23.95B issued, 43,124 holders | [asset record](https://horizon.stellar.org/assets?asset_code=VELO&asset_issuer=GDM4RQUQQUVSKQA7S6EM7XBZP3FCGH4Q7CL6TABQ7B2BEJ5ERARM2M5M) | A | 16 Nov 2026 |
| Largest holder 2.49B, 2-of-4 multisig | [GCUAZ…HBTB](https://horizon.stellar.org/accounts/GCUAZB7ELECT4IVTNXYIDL4BVTJCNBAMX7MZLV4SOQ52Y6XOFVMOHBTB) | A | 16 Nov 2026 |
| Fees $1,468 a year | [DefiLlama](https://defillama.com/protocol/velo-finance) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Which top accounts are Velo Labs vs exchanges** | Look up the top accounts named in this report on stellar.expert in a signed-in browser, or ask Velo Labs | Paid API / free UI |
| 2 | **Where the ~6.4B non-circulating VELO sits** | Ask CoinGecko or Velo for the excluded-address list | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.

- Research only. Not investment advice.
