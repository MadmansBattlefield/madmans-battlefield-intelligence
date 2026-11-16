---
ticker: SHARE
name: ShareX
chain: bsc
contract: "0x5fca51aff213bfbeab0b711b93c3374252fd6ac3"
overall_score: 3.3
overall_verdict: FAIL
section_scores:
  revenue: 2
  foundation_team: 4
  insider_holdings: 3
  selling_behavior: 4
  tokenomics_supply: 3
  liquidity_market: 3
  product_development: 4
  adoption_customers: 3
  security_audits: 5
  regulatory: 5
  catalysts: 3
gates_failed: [revenue]
red_lines:
  hack_exploit: "none found"
  mint_path_live: "not proven: 100M cap per docs; contract not read (BscScan wall)"
  team_wallet_to_exchange_during_pump: "not proven: BNB Chain transfers could not be read (BscScan API is paid; its pages sit behind a bot check)"
  entity_concentration: "82% of supply in project-controlled vesting pools (docs)"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "No fee or revenue data; nothing reaches holders."
pump_day_price_source: "the daily closes cited in the body"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions: []
price_usd: 2.64
price_source: "CoinGecko, 16 Nov 2026 ~9:15 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### SHARE · Overall grade **3.3 / 10 · ❌ FAIL**

**Summary:** ShareX is a DePIN project that links real-world shared-economy devices to a token on BNB Chain. It launched on Binance Alpha on 8 May 2026. Only 18% of the 100M supply circulates, so the $47M market cap sits under a **$264M FDV**. No fee or revenue data is published, so the revenue gate fails. I couldn't trace BNB Chain wallets with free tools, so selling is not proven.

**🚨 Top warning:** a 4× jump that held on thin volume, just as unlocks begin. SHARE went from **$0.64 on 7 Oct to $2.35 on 12 Oct 2026** (+267.7% over five days), and it has stayed between $2.6 and $2.7 since then on only ~$1M a day. The 6-month cliff on Mining, Ecosystem and Treasury (60% of supply) ended around 8 Nov 2026. Those pools now vest monthly ([tokenomics](https://docs.sharex.network/docs/share/tokenomics)). Every link is in the 🔗 Evidence trail below.

**Sections passed: 0 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 2/10 | ❌ FAIL (hard gate) |
| 🏛️ Foundation & team | 4/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 3/10 | ❌ FAIL |
| 📉 Selling behavior | 4/10 | ❌ FAIL (not proven) |
| 📊 Tokenomics & supply | 3/10 | ❌ FAIL |
| 💧 Liquidity & market | 3/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 4/10 | ❌ FAIL |
| 🤝 Adoption & customers | 3/10 | ❌ FAIL |
| 🛡️ Security & audits | 5/10 | ❌ FAIL |
| ⚖️ Regulatory | 5/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 3/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 SHARE · ShareX · 3.3 / 10 · ❌ FAIL

> **One line:** 18% float, a quadrupled price on ~$1M a day, and 60% of supply starting to vest.

| 📊 Market (CoinGecko, 16 Nov 2026 ~9:15 AM MST) | 🔗 Supply ([docs](https://docs.sharex.network/docs/share/tokenomics)) |
|---|---|
| **Price** $2.64 | **Total** 100,000,000 SHARE |
| **24h / 7d / 30d** ⚪ +0.4% / 🟢 +3.2% / 🟢 +7.4% | **Circulating** 17.95M (CoinGecko) |
| **Market cap** $47.4M · **FDV** $263.9M | **Team + investors** 20M (12-month cliff to May 2027) |
| **24h volume** $1.06M (PancakeSwap Infinity $0.43M, LBank $0.41M, MEXC $0.11M, KuCoin $0.10M) | **Mining + Ecosystem + Treasury** 60M (cliff ended ~8 Nov 2026; 96 months linear) |
| **ATH** $2.78 (27 Oct 2026) · now −5.2% | **Holders / transfers** not read (BscScan wall) |
| **Pump days** 40 since listing on 8 May 2026 (largest +267.7% on 12 Oct 2026) | |

---

## 💰 Revenue — Does it make money? · 2/10 · ❌ FAIL (hard gate)

- DefiLlama has no record for ShareX, and the project publishes no fee or revenue data. **2 → hard-gate FAIL.**

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** No fee or revenue data; nothing reaches holders.

## 🏛️ Foundation & team — Who is in charge? · 4/10 · ❌ FAIL

- Leaders are described by role only. The project launched through Binance Alpha ([ChainCatcher](https://www.chaincatcher.com/en/article/2263342)).

## 🪙 Foundation / team holdings — How many coins do they hold? · 3/10 · ❌ FAIL

- Docs allocate Mining 20%, Ecosystem 20%, Treasury & Reserve 20%, Community & Marketing 15%, Investors 10%, Team & Advisors 10% and Early Liquidity 5%. That puts 82% of supply in project-run pools.

**Top holders on BNB Chain** ([Arkham token page](https://intel.arkm.com/explorer/token/sharex-2), [Tier B] Arkham, read 16 Nov 2026 (signed-in account)):

| Holder | SHARE | % of 100M | Note |
|---|---:|---:|---|
| Vesting proxy `0x479…` | 76.67M | 76.7% | A vesting proxy contract [Unverified owner; Arkham's tag is a tentative exchange guess] |
| PancakeSwap V2 pool | 3.12M | 3.1% | DEX pool |
| Gnosis Safe `0xA6E…` | 3.00M | 3.0% | No project label |
| Gnosis Safe `0xEEa…` | 2.92M | 2.9% | No project label |
| `0x5437…BB3A3` | 2.25M | 2.3% | Unlabelled; also STBL's largest holder (28.2%) |

- About 77% of supply sits in one vesting proxy, which matches the docs' project-run pools, but its controller isn't labelled. The two Safes look like pool wallets [Unverified]. The same unlabelled `0x5437…BB3A3` appears in both SHARE and STBL, which points to a shared custodian, launch platform or market maker [Unverified].
- A second Arkham pass (16 Nov 2026) found no project treasury wallet. The token contract shows only small transfers, and the Binance Wallet proxy `0x73d8` (a Binance-run contract) holds no SHARE. **The treasury is still unseen.** Holdings stays **3**.

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL (not proven)

- BNB Chain transfers could not be read: Etherscan's free API doesn't cover BNB Chain, and BscScan pages return a bot check. Arkham's first page for the token shows only small transfers and nothing from 7–12 Oct 2026. **Not proven → 4** (unchanged after the second Arkham pass). The +267.7% move on 12 Oct 2026 is still the key window to check.

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from the daily closes cited in the body.

## 📊 Tokenomics & supply · 3/10 · ❌ FAIL

- 18% float, with a 6-month cliff and then 96 months for 60% of supply. Team and investors have a 12-month cliff, then 24 months.

## 💧 Liquidity & market · 3/10 · ❌ FAIL

- About $1M a day against a $47M cap. 41% of volume is on one PancakeSwap pool, and the price held flat after a fourfold jump.

## 🧑‍💻 Product & development · 4/10 · ❌ FAIL

- A DePIN device network and an RWA pitch (Tier B). No on-chain usage dashboard found.

## 🤝 Adoption & customers · 3/10 · ❌ FAIL

- No independent device or user counts found.

## 🛡️ Security & audits · 5/10 · ❌ FAIL

- No audit reviewed and no exploit found.

## ⚖️ Regulatory · 5/10 · ❌ FAIL

- No enforcement found.

## 📅 Catalysts & calendar · 3/10 · ❌ FAIL

- Monthly vesting of Mining, Ecosystem and Treasury from Nov 2026, then team and investors from May 2027.

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | ⚪ Not proven (BNB Chain not traceable with free tools) |
| Live mint path | ⚪ Not proven |
| Entity concentration | 🔴 82% in project pools |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| BNB Chain transfers | Not readable (BscScan wall) | — | low | no | Selling stays 4 |

## 📚 Sources

- [Tier A] Methodology update 16 Nov 2026: no new Arkham lookups; the attribution table uses evidence already cited in this report.
- [Tier A] [ShareX tokenomics docs](https://docs.sharex.network/docs/share/tokenomics)
- [Tier A] CoinGecko `sharex-2` (market, venues, daily prices since 8 May 2026 for pump days)
- [Tier B] [Tokenomics.com ShareX](https://app.tokenomics.com/tokenomics/sharex), [ChainCatcher listing note](https://www.chaincatcher.com/en/article/2263342), [OrangeX explainer](https://www.orangex.com/blog/articles/what-is-sharex-share-depin-rwa-token)
- [Tier B] Arkham, read 16 Nov 2026 (signed-in account): token label ShareX Token; top holders from the [Arkham token page](https://intel.arkm.com/explorer/token/sharex-2) (vesting proxy 0x479, PancakeSwap V2 pool, two Safes, unlabelled 0x5437)

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Allocation, cliffs, vesting | [docs](https://docs.sharex.network/docs/share/tokenomics) | A | 16 Nov 2026 |
| Price path $0.64 → $2.35 (7–12 Oct 2026) | [CoinGecko](https://www.coingecko.com/en/coins/sharex-2) | A | 16 Nov 2026 |
| Listing 8 May 2026 | [ChainCatcher](https://www.chaincatcher.com/en/article/2263342), [Tokenomics.com](https://app.tokenomics.com/tokenomics/sharex) | B+B | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Who controls vesting proxy 0x479 and the two Safes; exchange deposits around 12 Oct 2026** | Arkham (16 Nov 2026) gives no project label. Read the proxy's admin and the Safes' signers with a BNB Chain indexer | Free |
| 2 | **Who makes the market on PancakeSwap and LBank** | Arkham entity labels on the pool's LPs | Free account |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.

- Research only. Not investment advice.
