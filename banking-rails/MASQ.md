---
ticker: MASQ
name: MASQ
chain: ethereum
contract: "0x06f3c323f0238c72bf35011071f2b5b7f43a054c"
overall_score: 2.7
overall_verdict: FAIL
section_scores:
  revenue: 1
  foundation_team: 3
  insider_holdings: 4
  selling_behavior: 4
  tokenomics_supply: 6
  liquidity_market: 0
  product_development: 3
  adoption_customers: 1
  security_audits: 4
  regulatory: 4
  catalysts: 3
gates_failed: [revenue]
red_lines:
  hack_exploit: "none found"
  mint_path_live: "no: 40M minted once in the constructor; no mint function; 2.45M burned by the deployer"
  team_wallet_to_exchange_during_pump: "not proven in the last 365 days on Ethereum; team-funded wallets made ProBit deposits from 2021 to May 2025; Base and Polygon flows not traced"
  one_hop_sale_status: none_found
  treasury_selling: "historical: team-funded wallets sent ~1.3M MASQ to ProBit deposit addresses (2021–2025)"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "Nothing shows money flowing to the token."
pump_day_price_source: "the daily closes cited in the body"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions: []
price_usd: 0.004996
price_source: "CoinGecko, 16 Nov 2026 7:33 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### MASQ · Overall grade **2.7 / 10 · ❌ FAIL**

**Summary:** MASQ is the token of a privacy browser and mesh-VPN project that merged its products with the Timpi search project in Mar 2026; Timpi became the "trusted custodian" of MASQ Network. The token is a fixed-supply ERC20 (no mint), which is the one thing that passes. Everything else is near zero: **$26 of trading in 24 hours**, a **$172k market cap**, **−99.3% from the Dec 2023 high**, and no measurable revenue. The project says subscription revenue funds buybacks, but no buyback was found on-chain. Revenue trips the hard gate.

**🚨 Top warning:** there is effectively **no market**. CoinGecko shows **$26.48 of 24h volume** (Uniswap V3 on Base $165 and Ethereum $26 in its venue list), so any sale moves the price. About **47% of supply sits in the Base and Polygon bridges**, where most holders now are, and team-funded wallets have a history of sending coins to ProBit deposit addresses (latest found: [72,139 MASQ on 21 May 2025](https://etherscan.io/tx/0x21ff8d3654e62a81dfa05c21d285c62305264ffc46976d3ef5098812b63f1ceb)). Every link is in the 🔗 Evidence trail below.

**Sections passed: 1 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 1/10 | ❌ FAIL (hard gate) |
| 🏛️ Foundation & team | 3/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 4/10 | ❌ FAIL |
| 📉 Selling behavior | 4/10 | ❌ FAIL (not proven) |
| 📊 Tokenomics & supply | 6/10 | ✅ PASS |
| 💧 Liquidity & market | 0/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 3/10 | ❌ FAIL |
| 🤝 Adoption & customers | 1/10 | ❌ FAIL |
| 🛡️ Security & audits | 4/10 | ❌ FAIL |
| ⚖️ Regulatory | 4/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 3/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 MASQ · MASQ · 2.7 / 10 · ❌ FAIL

> **One line:** A fixed-supply token with no revenue, no volume and a project now run under another project's custody.

| 📊 Market (CoinGecko, 16 Nov 2026 7:33 AM MST) | 🔗 On-chain ([Etherscan](https://etherscan.io/token/0x06f3c323f0238c72bf35011071f2b5b7f43a054c), 16 Nov 2026 ~8:00 AM MST) |
|---|---|
| **Price** $0.004996 | **Minted** 40,000,000 once at deploy (3 Nov 2020); 2,447,981 burned by the deployer |
| **30d / 1y** 🔴 −32.3% / −70.3% | **Base bridge** [`0x3154…2C35`](https://etherscan.io/address/0x3154cf16ccdb4c6d922629664174b904d80f2c35) 12.55M (33%) |
| **Market cap** $171.8k · **FDV** $187.3k | **Polygon bridge** [`0x40ec…bbDf`](https://etherscan.io/address/0x40ec5b33f54e0e8a33a975908c5ba1c14e5bbbdf) 5.08M (14%) |
| **24h volume** $26.48 | **Chains** Ethereum, Base, Polygon |
| **ATH** $0.7364 (3 Dec 2023) · now −99.3% | **Circulating** 34.38M of 37.5M max (CoinGecko) |
| **Pump days, last 365 days** 28 (CoinGecko daily closes; largest +37.9% on 10 Feb 2026) | **DefiLlama** not listed |

---

## 💰 Revenue — Does it make money? · 1/10 · ❌ FAIL (hard gate)

| Metric | Value | Source |
|---|---:|---|
| Protocol fees / revenue | **Not found** (no DefiLlama listing; no fee contract) | — |
| Buybacks from subscription revenue | Claimed; **no buyback found on-chain** | [Tier A] [MASQ blog, 10 Apr 2026](https://www.masqbrowser.com/blog/masq-joins-forces-with-timpi) (claim) |

**What it means:** Nothing shows money flowing to the token. **1 → hard-gate FAIL.**

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** Nothing shows money flowing to the token.

## 🏛️ Foundation & team — Who is in charge? · 3/10 · ❌ FAIL

- On 25 Mar 2026 MASQ and Timpi announced a product-ecosystem merger: MASQ becomes the consumer brand, Timpi the search-index layer, and "Timpi becomes a trusted custodian of MASQ Network" ([MASQ blog](https://www.masqbrowser.com/blog/masq-joins-forces-with-timpi), [release](https://chainwire.org/2026/03/25/timpi-and-masq-network-merge-product-ecosystems-to-launch-the-first-fully-decentralised-stack-that-is-ethical/)). No legal entity, accounts or team-wallet disclosure were found.

## 🪙 Foundation / team holdings — How many coins do they hold? · 4/10 · ❌ FAIL

- The deployer ([`0x88d5…0189`](https://etherscan.io/address/0x88d58af211ea329f49a1306f7e55dff009c70189), Etherscan-labelled "MASQ Networks: Deployer 1") sent **21M** to [`0xad5e…33a6`](https://etherscan.io/address/0xad5e3fab1e3e2636057ab30923bf6976377f33a6) (e.g. [5.5M on 4 Nov 2020](https://etherscan.io/tx/0x84e803c1369da3f97f848b0d4e3fa4c6d0d4bde4a36bc6dd2e82f383d51e5002)), 9M to [`0xab84…1fC7`](https://etherscan.io/address/0xab8476186c0b8b1d1d8209d7c55893dacfbe1fc7), 5M and 4.45M to two more wallets.
- `0xad5e` is now empty: it passed 8.37M to [`0xa868…9304`](https://etherscan.io/address/0xa868a4cfd702211b68cc0dbc795863c92c609304) and 5.16M to [`0x27d9…788d`](https://etherscan.io/address/0x27d9a2ac83b493f88ce9b4532edcf74e95b9788d), which bridged ~10M to Polygon and 1.5M to Base ([e.g. 701k](https://etherscan.io/tx/0x91fe250effebfe41ba8baa1ce87e6f18e5f2a8a5dfa609c98ea700ff663f9703)).
- Team-funded wallets still visible on Ethereum: `0xab84…` (789k) and [`0x2f89…E8c7`](https://etherscan.io/address/0x2f8932b7e5a828d17f63aed5f93be26c8bcfe8c7) (707k on Ethereum, ~1.18M more on Base; [funded by `0xad5e` on 14 Apr 2025](https://etherscan.io/tx/0xa0ac3dc679e39f6b1ee50e54a2dd20876d5ae5a012296657b0d5c30341d1bb38)). A smart wallet [`0x5a46…4Ce9`](https://etherscan.io/address/0x5a4660d8006bdaff1a32538f53843e654ec54ce9) received [1.69M on 15 Nov 2025](https://etherscan.io/tx/0x87f5c955400542bc8487afaacd3b43a496e1f6705a8124d3c5928416d46b0355); its owner is [Unverified].
- **Total team holdings: Not found.** At least ~2.7M (7%) is traceable to team funding, and the 47% sitting on Base and Polygon could not be attributed.

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL (not proven)

- Tracing from the deployer (4 hops, transfers ≥ 50k) found **20 deposits to ProBit addresses** from team-funded wallets between Apr 2021 and May 2025, e.g. [168,759 MASQ on 28 Jul 2022](https://etherscan.io/tx/0x7cd60b42c546f9e26ef854c7e68f1d85d00fe60ad2e56e09952545a6a75e6b34) and [72,139 on 21 May 2025](https://etherscan.io/tx/0x21ff8d3654e62a81dfa05c21d285c62305264ffc46976d3ef5098812b63f1ceb).
- **None fell in the last 365 days** on Ethereum, and none on the 28 pump days. Most supply and trading has moved to Base, where the public explorer API blocked automated reads (HTTP 403) and the Etherscan free tier does not cover Base; that route was not forced. Selling there is **not proven**, so this scores 4.

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from the daily closes cited in the body.

## 📊 Tokenomics & supply · 6/10 · ✅ PASS

- 40M minted once in the constructor ([creation tx](https://etherscan.io/tx/0x020304bbc863a0373aea633942056ab04da4afaad18322b62b5183d21a3b8655)); the contract has burn but **no mint function**. The deployer burned 2.45M ([e.g. 1.45M](https://etherscan.io/tx/0xf8d63c63440f00c964b37e9660549099b16c6c4bbc56f75f89d23b08b32a24ea)). No inflation.

## 💧 Liquidity & market · 0/10 · ❌ FAIL

- $26.48 of 24h volume. Effectively untradeable at any size.

## 🧑‍💻 Product & development · 3/10 · ❌ FAIL

- A browser, extension and dVPN node software exist; the 2026 roadmap is integrating Timpi search. The blog's last product post is from Apr 2026.

## 🤝 Adoption & customers · 1/10 · ❌ FAIL

- No usage metrics are published; market activity shows almost no demand.

## 🛡️ Security & audits · 4/10 · ❌ FAIL

- Simple OpenZeppelin-style ERC20 with no mint; no exploit found. No recent audit of the node software found.

## ⚖️ Regulatory · 4/10 · ❌ FAIL

- No entity disclosure; no enforcement found.

## 📅 Catalysts & calendar · 3/10 · ❌ FAIL

| Date | Event |
|---|---|
| Not dated | MASQ Browser with native Timpi Search (public beta) |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | ⚪ Not proven in the window (historical ProBit deposits) |
| Live mint path | 🟢 None |
| Treasury selling | 🟡 Historical team-funded deposits to ProBit, 2021–2025 |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| Team-funded wallets → ProBit (2021 – May 2025) | Deployer-funded (4 hops) | Etherscan | medium | no | None: no pump-day deposit proven in the last 365 days; Selling stays 4 |

## 📚 Sources

- [Tier A] Methodology update 16 Nov 2026: no new Arkham lookups; the attribution table uses evidence already cited in this report.
- [Tier A] Etherscan v2 API `tokentx` for the deployer and 90 traced wallets, contract creation, receipt status of every linked tx (all succeeded); Etherscan top-holder page and labels; read 16 Nov 2026 ~7:55–8:20 AM MST
- [Tier A] [MASQ blog, 10 Apr 2026](https://www.masqbrowser.com/blog/masq-joins-forces-with-timpi); [Tier B] [merger release, 25 Mar 2026](https://chainwire.org/2026/03/25/timpi-and-masq-network-merge-product-ecosystems-to-launch-the-first-fully-decentralised-stack-that-is-ethical/)
- [Tier A] CoinGecko `masq` (16 Nov 2026 7:33 AM MST) and 365-day closes for pump days
- Not covered: Base and Polygon wallet flows (Base explorer API returned 403; Etherscan free tier excludes Base). **Arkham was not run for MASQ's wallets.** Arkham supports Ethereum, Base and Polygon, so this is an open item (see Open items), not a coverage gap

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| 40M minted once, no mint function | [token](https://etherscan.io/token/0x06f3c323f0238c72bf35011071f2b5b7f43a054c) · [creation](https://etherscan.io/tx/0x020304bbc863a0373aea633942056ab04da4afaad18322b62b5183d21a3b8655) | A | 16 Nov 2026 |
| 33% in Base bridge, 14% in Polygon bridge | [Base bridge](https://etherscan.io/address/0x3154cf16ccdb4c6d922629664174b904d80f2c35) · [Polygon](https://etherscan.io/address/0x40ec5b33f54e0e8a33a975908c5ba1c14e5bbbdf) | A | 16 Nov 2026 |
| Deployer → `0xad5e` | [5.5M](https://etherscan.io/tx/0x84e803c1369da3f97f848b0d4e3fa4c6d0d4bde4a36bc6dd2e82f383d51e5002) | A | 16 Nov 2026 |
| Team-funded ProBit deposits | [28 Jul 2022](https://etherscan.io/tx/0x7cd60b42c546f9e26ef854c7e68f1d85d00fe60ad2e56e09952545a6a75e6b34) · [21 May 2025](https://etherscan.io/tx/0x21ff8d3654e62a81dfa05c21d285c62305264ffc46976d3ef5098812b63f1ceb) | A | 16 Nov 2026 |
| Team wallet → Base bridge | [701k](https://etherscan.io/tx/0x91fe250effebfe41ba8baa1ce87e6f18e5f2a8a5dfa609c98ea700ff663f9703) | A | 16 Nov 2026 |
| Timpi custody / merger | [MASQ blog](https://www.masqbrowser.com/blog/masq-joins-forces-with-timpi) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Base and Polygon flows of team-funded wallets** | Look up the team-funded wallets linked in this report on Basescan/Polygonscan by hand, or with a paid Etherscan plan | Free by hand |
| 2 | **Arkham pass not yet run: owner of the 1.69M smart wallet, the top Base holder and the team-funded Ethereum wallets** | Look up the Ethereum wallets named in this report on Arkham (supported), then the Base/Polygon ones | Free (Arkham login) |
| 3 | **Buybacks** | Ask the team for buyback transaction hashes | Free |
| 4 | **Pump-day test on exchange prices.** No Gate, MEXC, KuCoin or Kraken USDT series with a full year was returned on 16 Nov 2026 (Binance blocks this region) | Re-run scripts/pump_day_test.py on the first exchange in the price-source order that lists the token | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.

- Research only. Not investment advice.
