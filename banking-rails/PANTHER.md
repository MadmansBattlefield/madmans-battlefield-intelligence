---
ticker: PANTHER
name: Panther Protocol
chain: ethereum
contract: "0x909e34d3f6124c324ac83dcca84b74398a6fa173"
overall_score: 3.4
overall_verdict: FAIL
section_scores:
  revenue: 1
  foundation_team: 5
  insider_holdings: 4
  selling_behavior: 4
  tokenomics_supply: 3
  liquidity_market: 3
  product_development: 6
  adoption_customers: 2
  security_audits: 5
  regulatory: 4
  catalysts: 4
gates_failed: [revenue]
red_lines:
  hack_exploit: "none found in this pass"
  team_wallet_to_exchange_during_pump: "none found: DAO Safe flows on pump days went to the Polygon and Base bridges"
  one_hop_sale_status: none_found
  supply_inflation: "38.2M PANTHER minted to a Safe in Aug and Nov 2026"
price_usd: 0.00133526
price_source: "CoinGecko `panther`, 16 Nov 2026 ~3:00 PM MST"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "No burn, buyback or fee share to holders was found; PANTHER is used for governance and protocol rewards."
pump_day_price_source: "MEXC PANTHERUSDT UTC daily closes"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions:
  - address: "0x505796f5bc290269d2522cf19135ad7aa60dfd77"
    label: "Protocol/DAO Safe (receives mints)"
    confidence: medium
    independent_corroboration: false
    basis: "Etherscan token transfers from the zero address"
  - address: "0x18709e89bd403f470088abdacebe86cc60dda12e"
    label: "Huobi: Recovery"
    confidence: medium
    independent_corroboration: false
    basis: "Etherscan name tag"
  - address: "0x9642b23ed1e01df1092b92641051881a322f5d4e"
    label: "MEXC 16"
    confidence: medium
    independent_corroboration: false
    basis: "Etherscan name tag"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### PANTHER · Overall grade **3.4 / 10 · ❌ FAIL**

**Summary:** Panther is a zero-knowledge privacy protocol for DeFi, run by Panther DAO. Its token was renamed from ZKP to PANTHER in Dec 2025 with no contract change, and mainnet went live on Polygon on 7 May 2026. No fee or revenue record on DefiLlama and none published by the project was found. No mechanism pays holders. A DAO Safe receives newly minted PANTHER and moved it to the Polygon and Base bridges, including on a pump day, which is a bridge flow, not a sale. The Revenue gate fails.

**🚨 Top warning:** **New supply is still being minted:** a Safe received 5.1M PANTHER minted on 21 Aug 2026 and 33.1M on 5 Nov 2026, with 468M of 1B max now issued. About 14% of supply sits in an address Etherscan tags "Huobi: Recovery".

**Sections passed: 1 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 1/10 | ❌ FAIL (hard gate) |
| 🏛️ Foundation & team | 5/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 4/10 | ❌ FAIL |
| 📉 Selling behavior | 4/10 | ❌ FAIL (not proven) |
| 📊 Tokenomics & supply | 3/10 | ❌ FAIL |
| 💧 Liquidity & market | 3/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 6/10 | ✅ PASS |
| 🤝 Adoption & customers | 2/10 | ❌ FAIL |
| 🛡️ Security & audits | 5/10 | ❌ FAIL |
| ⚖️ Regulatory | 4/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 4/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 PANTHER · Panther Protocol · 3.4 / 10 · ❌ FAIL

> **One line:** A live DeFi privacy protocol with no holder revenue and ongoing token minting.

| 📊 Market (CoinGecko `panther`, 16 Nov 2026 ~3:00 PM MST) | 🔗 Chain |
|---|---|
| **Price** $0.00134 | **Supply** 468M issued / 1B max |
| **7d / 30d / 1y** 🔴 −33.0% / 🔴 −48.6% / 🔴 −91.3% | **Ethereum ERC-20** `0x909e…a173` (also Polygon, Base) |
| **Market cap** $624k · **FDV** $624k | **Holders** 4,478 (Ethplorer) |
| **24h volume** $60k (top venues: MEXC $53.1k, LBank $6.78k, Uniswap V3 (Base) $46) | **Top holders** Polygon bridge 29.4%, "Huobi: Recovery" [`0x1870…a12e`](https://etherscan.io/address/0x18709e89bd403f470088abdacebe86cc60dda12e) 14.1% |
| **ATH** $0.439 (2022-03-04) |  |
| **Pump days** 43 of 360 days (MEXC PANTHERUSDT UTC daily closes); latest 2026-09-18, 2026-09-19 |  |

---

## 💰 Revenue — Does it make money? · 1/10 · ❌ FAIL (hard gate)

- No fee or revenue record on DefiLlama and none published by the project was found.
- Mainnet launched on Polygon on [7 May 2026](https://blog.pantherprotocol.io/programmable-privacy-is-live-panther-protocol-deploys-on-polygon/).

**What it means:** Nothing reaches holders. **1 → hard-gate FAIL.**

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** No burn, buyback or fee share to holders was found; PANTHER is used for governance and protocol rewards.

## 🏛️ Foundation & team — Who is in charge? · 5/10 · ❌ FAIL

- Panther Protocol Foundation (non-profit) funds development; the protocol is governed by Panther DAO via [Snapshot](https://snapshot.box/#/s:pantherprotocol.eth).

## 🪙 Foundation / team holdings — How many coins do they hold? · 4/10 · ❌ FAIL

- Safe [`0x5057…fd77`](https://etherscan.io/address/0x505796f5bc290269d2522cf19135ad7aa60dfd77) (3.9%) receives new mints from the zero address, so it is protocol- or DAO-controlled [Tier A on-chain]. Team and investor wallets are not published.
- [`0x1870…a12e`](https://etherscan.io/address/0x18709e89bd403f470088abdacebe86cc60dda12e) (14.1%) is tagged "Huobi: Recovery" by Etherscan; [`0x9642…5d4e`](https://etherscan.io/address/0x9642b23ed1e01df1092b92641051881a322f5d4e) (5.3%) is MEXC 16. Not proven → **4**.

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL (not proven)

- Pump test: MEXC PANTHERUSDT found 43 pump days in 360.
- On pump day 21 Aug 2026 the minting Safe sent 5.12M PANTHER to [`0xe1b5…5768`](https://etherscan.io/address/0xe1b583de9cb37196031b771686734a31ec365768), which sent it the same day to the Base bridge. On 31 Jan 2026 (a pump day) the Safe sent 18.5M to the Polygon bridge. On 5 Nov 2026 it sent 9M to the Polygon bridge and 5.8M to two unlabelled addresses. Bridge transfers are not sales under the one-hop rule, and none reached an exchange-labelled address. No Arkham pass was run.

**What it means:** No team sale proven → **4**.

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from MEXC PANTHERUSDT UTC daily closes.

## 📊 Tokenomics & supply · 3/10 · ❌ FAIL

- 1B max; 468M issued. 38.2M were minted to the DAO Safe in Aug and Nov 2026, so issuance continues.

## 💧 Liquidity & market · 3/10 · ❌ FAIL

- ~$60k a day, mostly MEXC (~$53k) and LBank (~$7k); DEX pools are tiny.

## 🧑‍💻 Product & development · 6/10 · ✅ PASS

- Mainnet live on Polygon with zSwap routing through Quickswap, Uniswap and Curve; Ethereum deployment approved by PIP-41 and parameters under vote (PIP-43, Nov 2026) [Tier A].

## 🤝 Adoption & customers · 2/10 · ❌ FAIL

- No usage or TVL figure was found.

## 🛡️ Security & audits · 5/10 · ❌ FAIL

- No exploit found; the launch post notes limited governance-controlled upgrade and emergency mechanisms.

## ⚖️ Regulatory · 4/10 · ❌ FAIL

- Privacy protocols face regulatory risk; access uses third-party zero-knowledge compliance credentials.

## 📅 Catalysts & calendar · 4/10 · ❌ FAIL

- Ethereum mainnet deployment; possible Base deployment funded by a DAO grant.

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | ⚪ None found: DAO Safe flows on pump days went to bridges |
| Supply inflation | 🟡 New PANTHER minted Aug and Nov 2026 |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. No Arkham pass was run for this report, so every attribution that rests on an unlabelled wallet is low confidence. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| [`0x5057…fd77`](https://etherscan.io/address/0x505796f5bc290269d2522cf19135ad7aa60dfd77) | Protocol/DAO Safe (receives mints) | Etherscan token transfers from the zero address | medium | no | none |
| [`0x1870…a12e`](https://etherscan.io/address/0x18709e89bd403f470088abdacebe86cc60dda12e) | Huobi: Recovery | Etherscan name tag | medium | no | none |
| [`0x9642…5d4e`](https://etherscan.io/address/0x9642b23ed1e01df1092b92641051881a322f5d4e) | MEXC 16 | Etherscan name tag | medium | no | none |

## 📚 Sources

- [Tier A] [CoinGecko `panther`](https://www.coingecko.com/en/coins/panther): price, supply, venues and description, read 16 Nov 2026
- [Tier A] MEXC PANTHERUSDT UTC daily closes via `scripts/pump_day_test.py` (43 pump days of 360); Binance returned HTTP 451, so the hierarchy fell through to this venue
- [Tier A] Token contract and [holders](https://etherscan.io/token/0x909e34d3f6124c324ac83dcca84b74398a6fa173#balances) on the chain explorer; top holders from the Ethplorer API; contract or EOA status from Etherscan v2 `eth_getCode`

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Market data and venues | [CoinGecko `panther`](https://www.coingecko.com/en/coins/panther) | A | 16 Nov 2026 |
| Token contract and holders | [contract](https://etherscan.io/token/0x909e34d3f6124c324ac83dcca84b74398a6fa173) · [holders](https://etherscan.io/token/0x909e34d3f6124c324ac83dcca84b74398a6fa173#balances) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Huobi: Recovery holding** | Confirm what the 14.1% "Huobi: Recovery" address is and whether those tokens can move | Arkham |
| 2 | **Mint schedule** | Find the governance rule behind the Aug and Nov 2026 mints | Free |
| 3 | **Recipients of 5 Nov 2026 transfers** | Trace `0x1240…59d3` and `0x09e4…97cb` | Arkham |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior. Under the 16 Nov 2026 one-hop amendment, a transfer to an exchange counts as a sale only with a team-attributed exchange account, evidence of a sale, or no plausible published reason.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.

- Research only. Not investment advice.
