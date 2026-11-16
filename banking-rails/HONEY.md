---
ticker: HONEY
name: Hivemapper
chain: solana
contract: "4vMsoUT2BWatFweudnQM1xedRLfJgJ7hswhcpz4xgBTy"
overall_score: 3.1
overall_verdict: FAIL
section_scores:
  revenue: 2
  foundation_team: 3
  insider_holdings: 3
  selling_behavior: 5
  tokenomics_supply: 3
  liquidity_market: 2
  product_development: 4
  adoption_customers: 2
  security_audits: 4
  regulatory: 5
  catalysts: 2
gates_failed: [revenue]
red_lines:
  hack_exploit: none found
  mint_path_live: "yes: the SPL mint authority is a plain System-owned wallet (single key), and supply grew ~6.8M HONEY from 16 Oct to 16 Nov 2026; the 10B cap is policy (MIPs), not code"
  team_wallet_to_exchange_during_pump: "not tested (holder list not retrievable from free Solana RPCs)"
  treasury_in_single_key_wallets: "yes for the mint authority (single key); the freeze authority is an SPL multisig"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "The one revenue loop the token had has stopped."
pump_day_price_source: "Gate HONEY/USDT daily closes"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions: []
price_usd: 0.00129722
price_source: "CoinGecko, 16 Nov 2026 8:20 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### HONEY · Overall grade **3.1 / 10 · ❌ FAIL**

**Summary:** Hivemapper is a dashcam mapping network on Solana. HONEY was meant to capture value because map customers burn it to buy Map Credits. In **Jul 2026, Bee Maps (the operating company) said it would drop HONEY**: from Aug 2026, app rewards are paid in **USDC**, HONEY rewards are no longer supported in the app, and Bee Maps **"terminated our services agreement with the Hivemapper Foundation"**. Burn revenue on DefiLlama fell from ~$80k a month in late 2025 to **$0 in Oct–Nov 2026**. 55% of supply was allocated to investors, employees and the company. The price is down **99.7% from ATH and 85% in a year**. Revenue trips the hard gate.

**🚨 Top warning:** the business has walked away from the token. Bee Maps' own [blog (16 Jul 2026)](https://beemaps.com/blog/get-paid-in-usdc-to-map-your-city) moves rewards to USDC "funded directly by Bee Maps" and ends its Foundation services agreement. [DefiLlama](https://api.llama.fi/summary/fees/hivemapper?dataType=dailyRevenue) shows burn revenue at $0 since October. Meanwhile, HONEY can still be minted by a [single-key mint authority](https://solscan.io/account/7VhQVr8M2Dpdwp4QzzQB7EpvANtMMjv7gwpBHCrV3U2A).

**Sections passed: 0 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 2/10 | ❌ FAIL |
| 🏛️ Foundation & team | 3/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 3/10 | ❌ FAIL |
| 📉 Selling behavior | 5/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 3/10 | ❌ FAIL |
| 💧 Liquidity & market | 2/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 4/10 | ❌ FAIL |
| 🤝 Adoption & customers | 2/10 | ❌ FAIL |
| 🛡️ Security & audits | 4/10 | ❌ FAIL |
| ⚖️ Regulatory | 5/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 2/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 HONEY · Hivemapper · 3.1 / 10 · ❌ FAIL

> **One line:** The mapping business lives on in USDC, while its token has lost its rewards role, its burn demand and its company backer.

| 📊 Market (CoinGecko, 16 Nov 2026 8:20 AM MST) | 🔗 On-chain (Solana, 16 Nov 2026) |
|---|---|
| **Price** $0.00129722 | **Supply** 6,566,442,080 HONEY (RPC `getTokenSupply`) of a 10B policy cap |
| **24h / 7d / 30d** 🔴 −5.1% / −20.9% / −42.6% · 1y −85.3% | **Supply on 16 Oct 2026** 6,559,630,308 (Foundation site), so +6.8M in a month |
| **Market cap** $8.52M · **FDV** $8.52M | **Mint authority** [`7VhQ…3U2A`](https://solscan.io/account/7VhQVr8M2Dpdwp4QzzQB7EpvANtMMjv7gwpBHCrV3U2A) System-owned wallet (single key) |
| **24h volume** $80k (Coinbase, Orca, Kraken) | **Freeze authority** [`Bg58…TBhT`](https://solscan.io/account/Bg588m44EMWAvvgm2yFtgMztUBPN5FTvVGwnTNrvTBhT) SPL multisig account |
| **ATH** $0.3763 (12 Dec 2023) · now −99.7% | **Mint** [`4vMs…xgBTy`](https://solscan.io/token/4vMsoUT2BWatFweudnQM1xedRLfJgJ7hswhcpz4xgBTy) |

---

## 💰 Revenue — Does it make money? · 2/10 · ❌ FAIL

| Metric | Value | Source |
|---|---:|---|
| Burn revenue, last 12 months | **$315k** (fees $421k) | [Tier A] [DefiLlama revenue](https://api.llama.fi/summary/fees/hivemapper?dataType=dailyRevenue) |
| Monthly trend | Nov 2025 $81k · Dec $82k · Jan 2026 $36k · Apr $4.7k · Jun $2.8k · Aug $328 · Sep $38k · **Oct $0 · Nov $0** | [Tier A] same (daily chart) |
| Burn design | Map Credits cost $0.0075; 75% of the HONEY spent is burned and 25% re-minted to contributors | [Tier A] [Foundation HONEY page](https://hivemapperfoundation.com/honey) |
| Main customer / operator | Bee Maps now pays contributors in USDC and has ended its Foundation services agreement | [Tier A] [Bee Maps blog](https://beemaps.com/blog/get-paid-in-usdc-to-map-your-city) |

**What it means:** The one revenue loop the token had has stopped. **2, which trips the Revenue gate.**

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** The one revenue loop the token had has stopped.

## 🏛️ Foundation & team — Who is in charge? · 3/10 · ❌ FAIL

| Item | Finding | Source |
|---|---|---|
| Structure | The Hivemapper Foundation sets protocol rules through Map Improvement Proposals. Bee Maps (formerly Hivemapper Inc.) runs the app and hardware | [Tier A] [Foundation](https://hivemapperfoundation.com/honey) |
| Split | Bee Maps "terminated our services agreement with the Hivemapper Foundation" (Jul 2026) | [Tier A] [Bee Maps blog](https://beemaps.com/blog/get-paid-in-usdc-to-map-your-city) |
| Disclosure | No Foundation funding, runway or wallet list published | — |

## 🪙 Foundation / team holdings — How many coins do they hold? · 3/10 · ❌ FAIL

| Allocation | HONEY | Share |
|---|---:|---:|
| Contributors (rewards) | 4.0B | 40% |
| Investors | 2.0B | 20% |
| Employees | 2.0B | 20% |
| Hivemapper Inc. (R&D) | 1.5B | 15% |
| Hivemapper Foundation (growth) | 0.5B | 5% |

*Source: [Tier A] [Foundation HONEY page](https://hivemapperfoundation.com/honey).*

- **55% went to investors, employees and the company.** Current wallets and vesting status were **not found**: free Solana RPCs refused `getTokenLargestAccounts`.

## 📉 Selling behavior — Do insiders sell into pumps? · 5/10 · ❌ FAIL

*Gate HONEY/USDT daily closes (UTC): 50 of the last 365 days were pump days.*

- **Not tested.** Without a holder list, insider wallets could not be identified or traced. Not proven clean, so **5**.
- **Arkham ([Tier B] Arkham, read 16 Nov 2026 (signed-in account)):** the [mint authority](https://intel.arkm.com/explorer/address/7VhQVr8M2Dpdwp4QzzQB7EpvANtMMjv7gwpBHCrV3U2A) is unlabelled and holds almost no HONEY (772). Its recent transfers are many 600–3.8k HONEY sends to individual wallets, a weekly reward pattern; Solana RPC shows 1,000+ such transactions on 12 Nov 2026. The [freeze multisig](https://intel.arkm.com/explorer/address/Bg588m44EMWAvvgm2yFtgMztUBPN5FTvVGwnTNrvTBhT) shows no transfers (last activity Sep 2023 per RPC). The [mint](https://intel.arkm.com/explorer/address/4vMsoUT2BWatFweudnQM1xedRLfJgJ7hswhcpz4xgBTy) is labelled **Hivemapper: HONEY**, but Arkham does not list its top holders, so insider wallets stay [Unverified].

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from Gate HONEY/USDT daily closes.

## 📊 Tokenomics & supply · 3/10 · ❌ FAIL

- 6.57B of the 10B cap is issued, so up to 52% more can come. Weekly contributor minting is tied to "Global Map Progress", plus up to 500k a week of consumption re-mints ([Foundation](https://hivemapperfoundation.com/honey)).
- Supply still grew ~6.8M from 16 Oct to 16 Nov 2026, while burns were $0.
- **The mint authority is a single-key wallet**: a System-owned account (RPC `getAccountInfo`) whose address is on the ed25519 curve, so it is a real keypair, not a program-derived address. The cap is a governance rule, not enforced by the token program.

## 💧 Liquidity & market · 2/10 · ❌ FAIL

- $80k of 24h volume on an $8.5M cap; rank #1250; mainly Coinbase, Orca and Kraken.
- −99.7% from ATH, −85% in a year, −43% in 30 days.

## 🧑‍💻 Product & development · 4/10 · ❌ FAIL

- The mapping product (Bee dashcam, Bee Maps data) carries on, but now on USDC. HONEY's protocol rules sit with the Foundation, with no announced new use.

## 🤝 Adoption & customers · 2/10 · ❌ FAIL

- Zero Map Credit burns recorded in Oct–Nov 2026 (DefiLlama). Customer demand for the map, if any, no longer touches HONEY.

## 🛡️ Security & audits · 4/10 · ❌ FAIL

- No exploit found. But a single key controls minting of the token.

## ⚖️ Regulatory · 5/10 · ❌ FAIL

- No enforcement action found.

## 📅 Catalysts & calendar · 2/10 · ❌ FAIL

| Date | Event |
|---|---|
| TBA | Any Foundation MIP that gives HONEY a new role; none announced |
| Ongoing | Weekly contributor mints |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | 🟡 Not tested |
| Live mint path | 🔴 Yes, through a single-key mint authority |
| Treasury in single-key wallets | 🔴 Mint authority is single-key |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| Mint authority (single key) | Hivemapper issuer | Solana RPC + Arkham | medium | no | None: insiders not identified; Selling 5 as published |

## 📚 Sources

- [Tier A] Methodology update 16 Nov 2026: no new Arkham lookups; the attribution table uses evidence already cited in this report.
- [Tier A] Solana RPC `getTokenSupply` and `getAccountInfo` (mint, mint authority, freeze authority), read 16 Nov 2026 ~9:20 AM MST
- [Tier A] DefiLlama `hivemapper` fees, revenue and holders revenue (daily chart)
- [Tier A] [Bee Maps blog, 16 Jul 2026](https://beemaps.com/blog/get-paid-in-usdc-to-map-your-city) · [Hivemapper Foundation HONEY page](https://hivemapperfoundation.com/honey)
- [Tier A] CoinGecko `hivemapper` (16 Nov 2026 8:20 AM MST); Gate HONEY/USDT daily candles
- [Tier B] Arkham, read 16 Nov 2026 (signed-in account): mint label, mint-authority and freeze-multisig activity (links in Selling)
- [Tier A] Solana RPC `getSignaturesForAddress` for the mint authority and freeze multisig
- [Unverified] Holder list, insider vesting status, insider sales

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| USDC replaces HONEY rewards; Foundation agreement terminated | [Bee Maps blog](https://beemaps.com/blog/get-paid-in-usdc-to-map-your-city) | A | 16 Nov 2026 |
| Allocation 40/20/20/15/5; burn-and-mint rules | [Foundation](https://hivemapperfoundation.com/honey) | A | 16 Nov 2026 |
| Burn revenue $0 in Oct–Nov 2026 | [DefiLlama](https://api.llama.fi/summary/fees/hivemapper?dataType=dailyRevenue) | A | 16 Nov 2026 |
| Mint authority is a System-owned (single-key) account | [mint](https://solscan.io/token/4vMsoUT2BWatFweudnQM1xedRLfJgJ7hswhcpz4xgBTy) · [authority](https://solscan.io/account/7VhQVr8M2Dpdwp4QzzQB7EpvANtMMjv7gwpBHCrV3U2A) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Who holds the mint authority and freeze multisig keys** | Arkham (16 Nov 2026) labels neither. Ask the Hivemapper Foundation or Bee Maps [Unverified] | Free |
| 2 | **Top holders and insider vesting** | Run `getTokenLargestAccounts` on a keyed Solana RPC (Helius free tier) and match the wallets to the allocation buckets | Free API key |
| 3 | **Insider sales into pumps** | Trace insider wallets to exchange deposits on the 50 pump days | Free API key |
| 4 | **What the Foundation plans for HONEY** | Watch the MIP list and Foundation announcements | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
