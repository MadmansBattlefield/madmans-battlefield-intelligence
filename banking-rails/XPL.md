---
ticker: XPL
name: Plasma
chain: plasma
contract: "native (Plasma chain, chain id 9745)"
overall_score: 3.6
overall_verdict: FAIL
section_scores:
  revenue: 2
  foundation_team: 5
  insider_holdings: 3
  selling_behavior: 0
  tokenomics_supply: 3
  liquidity_market: 6
  product_development: 6
  adoption_customers: 6
  security_audits: 6
  regulatory: 5
  catalysts: 3
gates_failed: [revenue, selling_behavior]
red_lines:
  hack_exploit: "none found"
  mint_path_live: "planned: 5% validator inflation (falling to 3%) once external validators and delegation go live"
  team_wallet_to_exchange_during_pump: "yes: a wallet funded by the Ecosystem Treasury (genesis 50M + 250M on 21 Aug 2026, itself a +35.7% day) sent 284.5M XPL (~$58M) to Binance, Bybit, Bitget, Gate and one unlabeled deposit; 202M of it in 18 transfers on pump days (Aug-Sep 2026); an investor-allocation recipient sent 23.9M XPL to a Bybit deposit on the cliff day (25 Sep 2026, +28.5%)"
  treasury_selling: "Ecosystem Treasury has paid out 960M XPL; docs allow use for 'liquidity needs' and 'exchange integrations', but the sales themselves were not disclosed"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "USD₮ transfers are free by design and the small fee income does not reach holders."
pump_day_price_source: "Gate XPL_USDT UTC daily closes, re-run 16 Nov 2026 with scripts/pump_day_test.py (76 of 360 days); the body's earlier count used the daily closes cited in the body"
pump_day_disclosure_quality: silence
pump_day_undisclosed_penalty_applied: true
dual_review: not_run
attributions: []
price_usd: 0.04311
price_source: "CoinGecko, 16 Nov 2026 6:58 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### XPL · Overall grade **3.6 / 10 · ❌ FAIL**

**Summary:** Plasma is a stablecoin-focused layer-1 with zero-fee USD₮ transfers. It holds **$405M of TVL**, real usage, and XPL trades $31.5M a day. But the chain earns almost nothing (**$104k of revenue in 12 months**, which is burned base fees), and XPL is −97% from its September 2025 high and −82% in a year. Insiders own 50% of supply. The team/investor one-year cliff opened on **25 Sep 2026** (1.67B XPL), and monthly unlocks follow until 2028. On-chain, an Ecosystem-allocation wallet has been **dumping into centralized exchanges on pump days**. Both hard gates fail.

**🚨 Top warning:** The [Plasma: Ecosystem Treasury `0xF97B…8558`](https://plasmascan.to/address/0xF97Ba376d3Ecb36C4472B1D3c5aaF2D158c28558) sent [**250M XPL on 21 Aug 2026**](https://plasmascan.to/tx/0x97a102ad1a4a5f3e70a316df1cbd5c7c2390e44b589f10d2914a82aa55fbe62a) (a +35.7% day) to [`0x9374…970f`](https://plasmascan.to/address/0x9374437baf4550929a5967d77d4ff979b88c970f). That wallet had also received [50M at genesis](https://plasmascan.to/tx/0xc84c15cdd1dd20aad28e363d28867b750d60d1bdd41c486a95ccdf0bfadb908c) from the same system allocation. It has sent **284.5M XPL (~$58M at the day's price) to exchange deposit addresses** (Binance 133.9M, Bybit 68.4M, Bitget 34.5M, Gate 2.5M and one unlabeled deposit 45.3M). **202M of that went in on pump days**, e.g. [13.9M to Bybit on 23 Aug 2026 (+33.9%)](https://plasmascan.to/tx/0x4ea492de18804eb934a890edb2fdc225de0311af79dd64fc99aca9eb44e6c64f) and [30M to Binance on 26 Sep 2026 (+13.8%)](https://plasmascan.to/tx/0x376b215074e9c9796f44a3eeba128905977b2129af61687229de5a1880d4f724). Every link is in the 🔗 Evidence trail below.

**Sections passed: 4 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 2/10 | ❌ FAIL (hard gate) |
| 🏛️ Foundation & team | 5/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 3/10 | ❌ FAIL |
| 📉 Selling behavior | 0/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 3/10 | ❌ FAIL |
| 💧 Liquidity & market | 6/10 | ✅ PASS |
| 🧑‍💻 Product & development | 6/10 | ✅ PASS |
| 🤝 Adoption & customers | 6/10 | ✅ PASS |
| 🛡️ Security & audits | 6/10 | ✅ PASS |
| ⚖️ Regulatory | 5/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 3/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 XPL · Plasma · 3.6 / 10 · ❌ FAIL

> **One line:** A stablecoin chain with real TVL and a token with almost no revenue, half of supply with insiders, and an ecosystem wallet that sold $58M into exchanges, much of it on spike days.

| 📊 Market (CoinGecko, 16 Nov 2026 6:58 AM MST) | 🔗 On-chain (Plasma, 16 Nov 2026) |
|---|---|
| **Price** $0.0431 | **Token** native XPL (chain id 9745); wrapped [WXPL](https://plasmascan.to/address/0x6100E367285b01F48D07953803A2d8dCA5D19873) |
| **24h / 7d / 30d** 🔴 −2.9% / −19.7% / −46.5% · 1y −81.7% | **Supply** 10.0B at launch; CoinGecko circulating 4.76B (47.6%) |
| **Market cap** $205.2M · **FDV** $431.0M | **Ecosystem Treasury** [`0xF97B…8558`](https://plasmascan.to/address/0xF97Ba376d3Ecb36C4472B1D3c5aaF2D158c28558) 2.15B XPL |
| **24h volume** $31.5M (Binance $7.5M, LBank $5.9M, Upbit, Bybit) | **Team** [`0xCf54…7b25`](https://plasmascan.to/address/0xCf54CB695A70f466fD5a271F85A7e268C2c97b25) 1.03B · **Investor** [`0xA4E2…74a4`](https://plasmascan.to/address/0xA4E25178BBc0409944df09aaebE110ce858374a4) 0.19B |
| **ATH** $1.68 (27 Sep 2025) · now −97.4% | **Unattributed** [`0x0E7B…E2A97A`](https://plasmascan.to/address/0x0E7B99b9B6B8D33FfC2A6aDbe54a3746e4E2A97A) 555.6M from the Investor wallet (27 Jan 2026), untouched |
| **Pump days, last 365 days** 76 (Binance XPLUSDT closes) | **TVL** $404.9M (DefiLlama) |

*Wallet names ("Plasma: Ecosystem Treasury", "Team", "Investor") are Plasmascan (Etherscan) public labels. They match genesis funding from the system allocation addresses `0x…a11b001/2/4`.*

---

## 💰 Revenue — Does it make money? · 2/10 · ❌ FAIL (hard gate)

| Metric | Value | Source |
|---|---:|---|
| Chain fees = revenue, last 12 months | **$103,801** (30 days: $5,046) | [Tier A] [DefiLlama, `plasma`](https://api.llama.fi/summary/fees/plasma?dataType=dailyRevenue) |
| To holders | Same $103.8k, as burned base fees (EIP-1559) | [Tier A] [DefiLlama holders revenue](https://api.llama.fi/summary/fees/plasma?dataType=dailyHoldersRevenue) · [tokenomics docs](https://www.plasma.to/docs/get-started/xpl/tokenomics) |

**What it means:** The main product, USD₮ transfers, is free by design, so $405M of TVL earns about $100k a year. **2 → hard-gate FAIL.**

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** USD₮ transfers are free by design and the small fee income does not reach holders.

## 🏛️ Foundation & team — Who is in charge? · 5/10 · ❌ FAIL

- Plasma is a company-run chain with a 25% investor allocation ([docs](https://www.plasma.to/docs/get-started/xpl/tokenomics)). Validators are still run by the team; external validators and delegation are "planned".
- No on-chain governance; the treasury, team and investor wallets are company-controlled.

## 🪙 Foundation / team holdings — How many coins do they hold? · 3/10 · ❌ FAIL

| Allocation (docs) | XPL | On-chain now |
|---|---:|---|
| Ecosystem & Growth | 4.0B (40%); 800M unlocked at launch, then 88.9M a month to Sep 2028 | Treasury received 3.11B so far; paid out 960M; holds **2.15B** |
| Team | 2.5B (25%); one-third after the 1-year cliff (25 Sep 2026), rest monthly to Sep 2028 | Paid out **1.47B on 24–25 Sep 2026** to 60+ wallets (e.g. [`0x36dc…1568`](https://plasmascan.to/address/0x36dcBE087D9dC15415d13c3B1b0d17E3A2E31568) 300M); holds **1.03B** |
| Investors | 2.5B (25%), same schedule | Paid out **2.32B**, including 555.6M, 191.7M and 71.6M **before** the cliff (Jan–May 2026); holds **0.19B** |
| Public sale | 1.0B (10%) | Non-US unlocked at launch; US buyers on 28 Jul 2026 |

**What it means:** Insiders hold or recently received most of the supply. Investor-wallet tokens moved before the cliff to unlabeled wallets, and those wallets' lock status is unknown. **3.**

## 📉 Selling behavior — Do insiders sell into pumps? · 0/10 · ❌ FAIL

Exchange identification: Plasmascan labels the hot wallets (Binance, Bybit Wallet 129, Bybit Hot Wallet 1, Gate, Bitget 6 via Etherscan). Each deposit below swept to one of them.

| Seller | Source of funds | To exchanges | On pump days | Example |
|---|---|---:|---:|---|
| [`0x9374…970f`](https://plasmascan.to/address/0x9374437baf4550929a5967d77d4ff979b88c970f) | Ecosystem Treasury (250M) + genesis ecosystem allocation (50M) | **284.5M XPL** (~$58.4M): Binance 133.9M, Bybit 68.4M, unlabeled 45.3M, Bitget 34.5M, Gate 2.5M | **202.0M in 18 tx** (21 Aug, 23 Aug, 3 Sep, 26 Sep 2026) | [Binance 11.3M, 23 Aug (+33.9%)](https://plasmascan.to/tx/0xa025f5ba47d414507444c9f8a0d67ee93c2fdc1faa14aec2f0706b22d1e8b8d9) · [Binance 17.0M, 3 Sep (+11.1%)](https://plasmascan.to/tx/0x020d90da5e17eac75b9232ec556d49d4d51786561b2aa2134408be028a653da7) |
| [`0x3729…6dcd`](https://plasmascan.to/address/0x37295d829e9a8c562343d2e9377530732eb46dcd) | [71.6M from the Investor wallet](https://plasmascan.to/tx/0x668298f06974047a832d30175f8744b678b13dc737a25ccc876d7213031de95c) (5 Mar 2026) | 25.8M to a Bybit deposit | **23.9M on 25 Sep 2026 (+28.5%)**, the cliff day | [tx](https://plasmascan.to/tx/0xde089fb10759be934343b260ac4789ec36a683f3d37c6174c64affddb3453bf1) |

- The docs allow ecosystem XPL for "liquidity needs" and "exchange integrations", so some exchange flow is expected. But the size and timing (selling into four separate spikes right after a 250M top-up), and the lack of any sale disclosure, meet the hard-gate rule.
- Team-cliff recipients (24–25 Sep 2026): none of the wallets that got 5M+ XPL sent it to a labeled exchange (directly or via a deposit address) up to 16 Nov 2026. They are still unlocking monthly.

**What it means:** A treasury-funded wallet sold ~$58M into exchanges, most of it on pump days. **1.**

- **Disclosure quality (16 Nov 2026 rules): silence.** Treasury "operations" are mentioned, but the sales themselves were not disclosed. **Penalty applied (16 Nov 2026 rules):** a proven pump-day sale with no disclosure fails Selling (ordinary score at most 3) and then loses 2 points, floored at 0: **1 → 0**. Pump days from Gate XPL_USDT UTC daily closes, re-run 16 Nov 2026 with scripts/pump_day_test.py (76 of 360 days); the body's earlier count used the daily closes cited in the body.

## 📊 Tokenomics & supply · 3/10 · ❌ FAIL

- 10B at launch, plus planned **5% annual inflation** (falling 0.5% a year to 3%) once external validators go live. Base fees are burned.
- Unlocks: ecosystem ~88.9M a month and team + investors ~139M a month until Sep 2028, after the 1.67B cliff on 25 Sep 2026 ([docs](https://www.plasma.to/docs/get-started/xpl/tokenomics)).

## 💧 Liquidity & market · 6/10 · ✅ PASS

- $31.5M of 24h volume on a $205M cap. Binance, Upbit and Bybit are among the venues (CoinGecko, 16 Nov 2026 6:58 AM MST). Price −46.5% in 30 days.

## 🧑‍💻 Product & development · 6/10 · ✅ PASS

- Mainnet beta since 25 Sep 2025, with zero-fee USD₮ transfers and an EVM. Large DeFi deployments; the [LayerZero OFT adapter](https://plasmascan.to/address/0x405FBc9004D857903bfD6b3357792D71a50726b0) holds 262M XPL.

## 🤝 Adoption & customers · 6/10 · ✅ PASS

- TVL **$404.9M** (DefiLlama, 16 Nov 2026). Stablecoin transfers are the main use; fees are near zero by design.

## 🛡️ Security & audits · 6/10 · ✅ PASS

- No exploit of the chain or token found. Validators are still permissioned (team-run), which is a centralization risk.

## ⚖️ Regulatory · 5/10 · ❌ FAIL

- The public sale included US purchasers under a 12-month lock. The chain is built around USD₮, so issuer and stablecoin regulation are direct dependencies. No enforcement action found.

## 📅 Catalysts & calendar · 3/10 · ❌ FAIL

| Date | Event |
|---|---|
| Monthly to Sep 2028 | Team, investor and ecosystem unlocks (~228M XPL a month) |
| TBD | External validators + 5% inflation switch-on |
| Past | 25 Sep 2026 cliff (1.67B) |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | 🔴 Ecosystem-funded wallet → Binance/Bybit/Bitget on pump days ([23 Aug 2026](https://plasmascan.to/tx/0x4ea492de18804eb934a890edb2fdc225de0311af79dd64fc99aca9eb44e6c64f)); investor recipient → Bybit on the cliff day ([tx](https://plasmascan.to/tx/0xde089fb10759be934343b260ac4789ec36a683f3d37c6174c64affddb3453bf1)) |
| Live mint path | 🟡 5% validator inflation planned |
| Treasury selling | 🔴 ~284.5M XPL from an ecosystem wallet to exchanges |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| Ecosystem Treasury-funded wallet | Plasma Ecosystem Treasury (genesis 50M + 250M top-up) | Etherscan funding | high | yes (on-chain) | Selling: 284.5M XPL to Binance, Bybit, Bitget and Gate, 202M on Aug–Sep 2026 pump days |

## 📚 Sources

- [Tier A] Methodology update 16 Nov 2026: no new Arkham lookups; the attribution table uses evidence already cited in this report.
- [Tier A] Plasma chain via Etherscan API v2 (chain 9745): native and internal transfers of the Ecosystem Treasury, Team, Investor, 80 first-hop recipients and 56 second-hop addresses; receipts (status 1) for every linked tx, 16 Nov 2026 ~7:00–7:30 AM MST
- [Tier A] Plasmascan public labels and top-accounts page (16 Nov 2026); Etherscan Ethereum labels for Binance/Bitget deposits on the same addresses
- [Tier B] Arkham, read 16 Nov 2026 ~7:35 AM MST (signed-in account): **Plasma is not supported.** The network selector lists only Ethereum, Polygon, BNB Chain, Optimism, Avalanche, Arbitrum, Base, Bitcoin, Tron, Flare, Solana, Dogecoin, Zcash, HyperEVM, Hypercore, Robinhood Chain. The first address looked up, `0xF97B…8558`, showed no assets and no transfers ([Arkham](https://intel.arkm.com/explorer/address/0xF97Ba376d3Ecb36C4472B1D3c5aaF2D158c28558)). No Arkham labels were available for this report
- [Tier A] [Plasma docs: tokenomics](https://www.plasma.to/docs/get-started/xpl/tokenomics); DefiLlama `plasma` fees, revenue and TVL; CoinGecko `plasma` (16 Nov 2026 6:58 AM MST); Binance XPLUSDT daily closes
- [Unverified] who controls `0x9374…`, `0x3729…` and `0x0E7B…`; whether ecosystem sales were market-making under an agreement. Arkham does not support Plasma (checked 16 Nov 2026)

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Allocation and unlock schedule | [tokenomics docs](https://www.plasma.to/docs/get-started/xpl/tokenomics) | A | 16 Nov 2026 |
| Treasury → `0x9374…` 250M on a +35.7% day; genesis 50M | [250M](https://plasmascan.to/tx/0x97a102ad1a4a5f3e70a316df1cbd5c7c2390e44b589f10d2914a82aa55fbe62a) · [genesis](https://plasmascan.to/tx/0xc84c15cdd1dd20aad28e363d28867b750d60d1bdd41c486a95ccdf0bfadb908c) | A | 16 Nov 2026 |
| `0x9374…` → exchanges on pump days | [Bybit 23 Aug](https://plasmascan.to/tx/0x4ea492de18804eb934a890edb2fdc225de0311af79dd64fc99aca9eb44e6c64f) · [Binance 23 Aug](https://plasmascan.to/tx/0xa025f5ba47d414507444c9f8a0d67ee93c2fdc1faa14aec2f0706b22d1e8b8d9) · [Binance 3 Sep](https://plasmascan.to/tx/0x020d90da5e17eac75b9232ec556d49d4d51786561b2aa2134408be028a653da7) · [Binance 26 Sep](https://plasmascan.to/tx/0x376b215074e9c9796f44a3eeba128905977b2129af61687229de5a1880d4f724) | A chain · identity [Unverified] | 16 Nov 2026 |
| Investor recipient → Bybit on cliff day | [funding](https://plasmascan.to/tx/0x668298f06974047a832d30175f8744b678b13dc737a25ccc876d7213031de95c) · [deposit](https://plasmascan.to/tx/0xde089fb10759be934343b260ac4789ec36a683f3d37c6174c64affddb3453bf1) | A | 16 Nov 2026 |
| Revenue $103.8k / 12 months | [DefiLlama](https://api.llama.fi/summary/fees/plasma?dataType=dailyRevenue) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Who controls `0x9374…970f`, and is it a disclosed market maker?** | Arkham does not cover Plasma. Ask Plasma for market-making disclosures; check the same address on Ethereum (Arkham-supported) for a label | Free |
| 2 | **Is the 555.6M in `0x0E7B…` still locked?** | Check for a custody label or a lock contract; follow any outflow | Free |
| 3 | **Team-cliff recipients' selling after Nov 2026** | Re-run the second-hop exchange check monthly | Free |
| 4 | **Where the unlabeled deposit `0x16ef…` sweeps to (`0xe8fe…`)** | Identify the hot wallet on Plasmascan (Arkham does not cover Plasma) | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.

- Research only. Not investment advice.
