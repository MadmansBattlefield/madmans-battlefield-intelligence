---
ticker: HASH
name: Provenance Blockchain
chain: provenance
contract: "native (Provenance Blockchain, denom nhash)"
overall_score: 3.8
overall_verdict: FAIL
section_scores:
  revenue: 3
  foundation_team: 5
  insider_holdings: 2
  selling_behavior: 4
  tokenomics_supply: 5
  liquidity_market: 1
  product_development: 7
  adoption_customers: 5
  security_audits: 4
  regulatory: 5
  catalysts: 5
gates_failed: [revenue]
red_lines:
  hack_exploit: "user-wallet compromise via a Web3auth/Keplr vulnerability; governance froze 18 affected accounts on 11 Nov 2026 (prop 118)"
  mint_path_live: "governance-controlled: nhash is a marker; supply changes need a passed proposal (prop 106 burned 5B in May 2026)"
  team_wallet_to_exchange_during_pump: "not proven: the largest group-controlled accounts made no sends on pump days found; most trading is on Figure Markets, which is not traceable on-chain from outside"
  account_freeze_power: "yes: the sanction module lets governance freeze any account (used in prop 118)"
price_usd: 0.006448
price_source: "CoinGecko, 16 Nov 2026 7:41 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### HASH · Overall grade **3.8 / 10 · ❌ FAIL**

**Summary:** Provenance is the Cosmos-based chain that Figure (Nasdaq: FIGR) uses for its loans and tokenized assets. Real activity runs on it: chain fees were **$3.51M in the last 12 months** and TVL is ~$139M. But DefiLlama's protocol **revenue has been $0 since 7 Apr 2026**, and fees go to validators rather than to a value-capture mechanism, so the revenue gate fails. The bigger problems are **control and liquidity**: Figure says it holds about **25%** of HASH and has run the Foundation since Jan 2026, the **top 3 accounts hold 50.5%** of supply, and the coin trades only **~$2.5k a day** against a $389M market cap.

**🚨 Top warning:** the price is close to untradeable. CoinGecko shows **$2,468 of 24h volume**, $2,198 of it on Figure Markets (Figure's own venue), for a coin valued at $388.6M ($612M fully diluted). Anyone trying to sell even 0.01% of the cap would move the price. On top of that, governance froze 18 user accounts on 11 Nov 2026 after a wallet vulnerability ([prop 118](https://explorer.provenance.io/proposal/118)), which shows the chain can freeze any account by vote. Every link is in the 🔗 Evidence trail below.

**Sections passed: 1 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 3/10 | ❌ FAIL (hard gate) |
| 🏛️ Foundation & team | 5/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 2/10 | ❌ FAIL |
| 📉 Selling behavior | 4/10 | ❌ FAIL (not proven) |
| 📊 Tokenomics & supply | 5/10 | ❌ FAIL |
| 💧 Liquidity & market | 1/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 7/10 | ✅ PASS |
| 🤝 Adoption & customers | 5/10 | ❌ FAIL |
| 🛡️ Security & audits | 4/10 | ❌ FAIL |
| ⚖️ Regulatory | 5/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 5/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 HASH · Provenance Blockchain · 3.8 / 10 · ❌ FAIL

> **One line:** A real RWA chain with real fees, but Figure-controlled supply, no protocol revenue since April, and almost no market.

| 📊 Market (CoinGecko, 16 Nov 2026 7:41 AM MST) | 🔗 On-chain ([Provenance explorer](https://explorer.provenance.io/), 16 Nov 2026 ~7:50 AM MST) |
|---|---|
| **Price** $0.006448 | **Max / current supply** 95B / 94.98B HASH |
| **24h / 7d / 30d** 🟢 +1.3% / +5.1% / +3.8% · 1y −78.7% | **Circulation** 60.27B · **Bonded (staked)** 15.34B |
| **Market cap** $388.6M · **FDV** $612.5M | **Holders** 11,959 accounts · top 3 = 50.5%, top 10 = 71.1% |
| **24h volume** $2,468 (Figure Markets $2,198, Osmosis $271) | **Fees (12 months)** $3.51M · 30 days $483k (DefiLlama) |
| **ATH** $0.0601 (14 Sep 2025) · now −89.3% | **Protocol revenue** $302k in 12 months, **$0 since 7 Apr 2026** |
| **Pump days, last 365 days** 36 (CoinGecko daily closes; largest +53.6% on 9 Dec 2025) | **TVL** ~$139M (DefiLlama) |

---

## 💰 Revenue — Does it make money? · 3/10 · ❌ FAIL (hard gate)

| Metric | Value | Source |
|---|---:|---|
| Chain fees, last 12 months | **$3,511,414** (30 days: $483,279) | [Tier A] [DefiLlama `provenance` fees](https://api.llama.fi/summary/fees/provenance?dataType=dailyFees) |
| Protocol revenue, last 12 months | **$302,027**, last non-zero day **7 Apr 2026**; 30 days: **$0** | [Tier A] [DefiLlama revenue](https://api.llama.fi/summary/fees/provenance?dataType=dailyRevenue) |

**What it means:** Fees are real but small next to a $389M cap (~110× fees), they are paid to validators and delegators, and the revenue line DefiLlama tracks stopped in April. Figure's Jan 2026 release promised "a revised tokenomics model that introduces network fees", which has not shown up in revenue yet. **3 → hard-gate FAIL.**

## 🏛️ Foundation & team — Who is in charge? · 5/10 · ❌ FAIL

- On 14 Jan 2026 holders passed [prop 98](https://explorer.provenance.io/proposal/98), "Figure to Steward the Provenance Foundation". Figure now runs the Foundation day to day; the Foundation's director stays on ([Figure release, 21 Jan 2026](https://investors.figure.com/news-releases/news-release-details/figure-technology-solutions-announces-community-approved-update), [proposal page](https://docs.provenance.io/2df23393565480c28ba0d2e197059e32)).
- Figure is a Nasdaq-listed company, so its disclosures are audited. But the chain's operator is also its largest holder and its main user.

## 🪙 Foundation / team holdings — How many coins do they hold? · 2/10 · ❌ FAIL

| Account | HASH | % of 95B | What it is |
|---|---:|---:|---|
| [`pb15yfx…6af7z`](https://explorer.provenance.io/accounts/pb15yfx2r9sxjzgrcdghvt8me9vvt540w4kg25mehwlcjm4jq2m2hmsh6af7z) | 17.57B | 18.5% | x/group policy account (multi-member); owner [Unverified] |
| [`bonded_tokens_pool`](https://explorer.provenance.io/accounts/pb1fl48vsnmsdzcv85q5d2q4z5ajdha8yu3u4z25t) | 15.74B | 16.6% | Staking module (all delegated HASH) |
| [`pb1a0esk…4t5dq`](https://explorer.provenance.io/accounts/pb1a0eskr8037ucvqwfjm6ktnr3fngazz9r7nxxx2kfll08vvuz82kqg4t5dq) | 14.67B | 15.4% | Continuous vesting account: 14.64B vesting 22 Jun 2025 → 22 May 2029 |
| [`pb16s9hm…machf`](https://explorer.provenance.io/accounts/pb16s9hm7ylx7hwc50lx46j84cjda38yqm2m36dtqshcguc25avd96skmachf) | 4.93B | 5.2% | Group account carrying Figure KYC and Figure Markets attributes |
| [`pb1e2fhl…9r4aq`](https://explorer.provenance.io/accounts/pb1e2fhljv44saqmewp6j6ra0y94e8vzfs9a9r4aq) | 4.50B | 4.7% | Creates vesting accounts for others (distributor) |

- Figure states it holds **roughly 25% of outstanding HASH** ([release](https://investors.figure.com/news-releases/news-release-details/figure-technology-solutions-announces-community-approved-update)). Which of the accounts above are Figure's or the Foundation's is not published [Unverified].
- The top 3 accounts hold 50.5% and the top 10 hold 71.1% of supply, read from the explorer's full holder list (11,959 accounts).

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL (not proven)

- The largest group account `pb15yfx…` made its last bank send on 9 Jan 2026; its recent transactions are group proposals and votes. `pb16s9hm…` last sent on 14–22 May 2026, not on a pump day. No large insider send was found on the 36 pump days.
- Most HASH trading happens inside **Figure Markets**, Figure's own exchange, where order flow is not visible on-chain. Insider selling there **cannot be traced** from outside, so the rule scores this 4 (not proven).

## 📊 Tokenomics & supply · 5/10 · ❌ FAIL

- Max supply is now **95B** after [prop 106](https://explorer.provenance.io/proposal/106) burned **5B HASH** (passed 1 May 2026), matching Figure's pledge to burn up to ~5% of total supply.
- Non-retail holdings above 100K are locked and vest over 48 months from May 2025 (the large vesting accounts end 22 May 2029), so a steady unlock continues for 2.5 more years.
- Supply is a governance-controlled marker: any change needs a passed proposal. [Prop 110](https://explorer.provenance.io/proposal/110) raised the marker module's per-marker ceiling for vault shares (no effect on HASH supply).

## 💧 Liquidity & market · 1/10 · ❌ FAIL

- **$2,468 of 24h volume** against a $388.6M cap (0.0006% a day). 89% of it is on Figure Markets. There is no meaningful exit liquidity at the quoted price.

## 🧑‍💻 Product & development · 7/10 · ✅ PASS

- An active chain with frequent governance upgrades (vault shares, CosmWasm upload restrictions in prop 115) and a production user in Figure's lending and marketplace business.

## 🤝 Adoption & customers · 5/10 · ❌ FAIL

- ~$139M of TVL and $3.5M of yearly fees show real use, but almost all of it comes from one company, Figure. Third-party adoption is limited.

## 🛡️ Security & audits · 4/10 · ❌ FAIL

- [Prop 118](https://explorer.provenance.io/proposal/118) (passed 11 Nov 2026) froze **18 accounts "affected by a recent Web3auth/Keplr vulnerability"** that still had funds at risk; funds are to be returned to owners later. It was a wallet-side compromise, not a chain exploit, but it shows (a) user funds were at risk and (b) governance can freeze any account through the sanction module.

## ⚖️ Regulatory · 5/10 · ❌ FAIL

- The operator is an SEC-reporting public company. HASH itself has no registration, and the freeze power plus Figure's control make it look more like a permissioned corporate chain than a decentralized one.

## 📅 Catalysts & calendar · 5/10 · ❌ FAIL

| Date | Event |
|---|---|
| Not dated | Revised tokenomics with network fees (Figure commitment, Jan 2026) |
| Not dated | Return of frozen funds to the 18 affected accounts |
| Monthly to 22 May 2029 | Continuous vesting unlocks of locked holdings |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟡 Wallet-side vulnerability; 18 accounts frozen by governance |
| Team wallet → exchange during a pump | ⚪ Not proven (Figure Markets flow not visible) |
| Live mint path | 🟡 Governance-controlled marker supply |
| Account freeze power | 🔴 Yes (sanction module, used Nov 2026) |

## 📚 Sources

- [Tier A] Provenance LCD `api.provenance.io`: `cosmos/gov/v1/proposals` (106, 110, 115, 118), `cosmos/auth/v1beta1/accounts` (account types and vesting terms); read 16 Nov 2026 ~7:40–7:55 AM MST
- [Tier A] Provenance explorer API: `utility_token/stats` (supply, circulation, bonded, burned), the full `nhash` holder list (11,959 accounts), and account transaction lists; read 16 Nov 2026 ~7:45–7:55 AM MST
- [Tier A] [Figure release, 21 Jan 2026](https://investors.figure.com/news-releases/news-release-details/figure-technology-solutions-announces-community-approved-update); [prop 98 proposal page](https://docs.provenance.io/2df23393565480c28ba0d2e197059e32)
- [Tier A] DefiLlama `provenance` fees and revenue; CoinGecko `hash-2` (16 Nov 2026 7:41 AM MST) and 365-day closes for pump days
- [Tier B] Arkham, network list read 16 Nov 2026 ~7:35 AM MST (signed-in account): **Provenance is not supported.** Arkham's network selector lists only Ethereum, Polygon, BNB Chain, Optimism, Avalanche, Arbitrum, Base, Bitcoin, Tron, Flare, Solana, Dogecoin, Zcash, HyperEVM, Hypercore, Robinhood Chain. No Arkham labels were available for this report

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Supply 94.98B, circulation 60.27B, bonded 15.34B | [stats API](https://service-explorer.provenance.io/api/v3/utility_token/stats) | A | 16 Nov 2026 |
| Fees $3.51M / revenue $0 since Apr | [fees](https://api.llama.fi/summary/fees/provenance?dataType=dailyFees) · [revenue](https://api.llama.fi/summary/fees/provenance?dataType=dailyRevenue) | A | 16 Nov 2026 |
| Figure holds ~25%, runs the Foundation | [Figure release](https://investors.figure.com/news-releases/news-release-details/figure-technology-solutions-announces-community-approved-update) · [prop 98](https://explorer.provenance.io/proposal/98) | A | 16 Nov 2026 |
| 5B burn | [prop 106](https://explorer.provenance.io/proposal/106) · [LCD](https://api.provenance.io/cosmos/gov/v1/proposals/106) | A | 16 Nov 2026 |
| 18 accounts frozen | [prop 118](https://explorer.provenance.io/proposal/118) · [LCD](https://api.provenance.io/cosmos/gov/v1/proposals/118) | A | 16 Nov 2026 |
| Largest holders and vesting terms | [group account](https://explorer.provenance.io/accounts/pb15yfx2r9sxjzgrcdghvt8me9vvt540w4kg25mehwlcjm4jq2m2hmsh6af7z) · [vesting account](https://api.provenance.io/cosmos/auth/v1beta1/accounts/pb1a0eskr8037ucvqwfjm6ktnr3fngazz9r7nxxx2kfll08vvuz82kqg4t5dq) · [holder list](https://service-explorer.provenance.io/api/v3/assets/nhash/holders?count=50&page=1) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Which large accounts belong to Figure or the Foundation** | Match the group accounts linked in this report against group membership (`cosmos/group/v1/group_policy_info`) and Figure's filings | Free |
| 2 | **Insider selling on Figure Markets** | Not visible on-chain; ask Figure/Foundation for disclosed sales or check Figure's 10-Q digital-asset notes | Free |
| 3 | **When network-fee tokenomics go live** | Watch governance proposals | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.

- Research only. Not investment advice.
