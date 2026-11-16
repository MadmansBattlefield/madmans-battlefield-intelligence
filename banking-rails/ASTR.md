---
ticker: ASTR
name: Astar
chain: astar
contract: "0xf27441230eadeac85b764610325cc9a0d7859689"
overall_score: 3.8
overall_verdict: FAIL
section_scores:
  revenue: 1
  foundation_team: 4
  insider_holdings: 4
  selling_behavior: 5
  tokenomics_supply: 6
  liquidity_market: 4
  product_development: 5
  adoption_customers: 2
  security_audits: 6
  regulatory: 5
  catalysts: 4
gates_failed: [revenue]
red_lines:
  hack_exploit: none found
  mint_path_live: "yes, by design (Tokenomics 3.0: ~3% yearly inflation today, ceiling 5.5%, decaying toward a ~10B maximum)"
  team_wallet_to_exchange_during_pump: "not tested (Foundation wallets are not published; the Foundation says it does not sell ASTR to fund operations)"
  treasury_in_single_key_wallets: "unknown for the Foundation; the 304.5M ASTR on-chain treasury is a governance-controlled pallet account"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "Revenue rounds to zero; no material fee-funded burn, buyback or fee share is documented in this report."
pump_day_price_source: "Gate ASTR_USDT UTC daily closes, re-run 16 Nov 2026 with scripts/pump_day_test.py (30 of 360 days); the body's earlier count used Gate ASTR/USDT daily closes"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions: []
price_usd: 0.00443889
price_source: "CoinGecko, 16 Nov 2026 8:20 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### ASTR · Overall grade **3.8 / 10 · ❌ FAIL**

**Summary:** Astar is a Polkadot parachain with an EVM, run by the Astar Foundation. It cleaned up its token in Mar 2026 with **Tokenomics 3.0** (inflation now ~3%, ceiling cut to 5.5%, supply converging toward ~10B, and 80% of gas fees burned). But the chain is nearly unused: **$1.9k of fees and $689 of revenue in a year** and **$1.0M TVL** on DefiLlama. The Foundation is pivoting to "consumer finance from Japan" (AstarFi, not yet launched), while its own forum shows holders asking whether the founding company has moved on to Soneium. The price is down **98.9% from ATH and 67% in a year**. Revenue trips the hard gate.

**🚨 Top warning:** there is no business under the token yet. DefiLlama shows [$689 of revenue in 12 months](https://api.llama.fi/summary/fees/astar?dataType=dailyRevenue), against ~3% yearly new supply (~265M ASTR, ~$1.2M at today's price) paid to stakers. Burndrop, the promised supply-reduction event, has no date. The Foundation says it is "sequenced" behind products and partner confirmation ([forum, Jun 2026](https://forum.astar.network/t/state-of-burndrop/9514)).

**Sections passed: 2 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 1/10 | ❌ FAIL |
| 🏛️ Foundation & team | 4/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 4/10 | ❌ FAIL |
| 📉 Selling behavior | 5/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 6/10 | ✅ PASS |
| 💧 Liquidity & market | 4/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 5/10 | ❌ FAIL |
| 🤝 Adoption & customers | 2/10 | ❌ FAIL |
| 🛡️ Security & audits | 6/10 | ✅ PASS |
| ⚖️ Regulatory | 5/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 4/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 ASTR · Astar · 3.8 / 10 · ❌ FAIL

> **One line:** Tidy new tokenomics on top of a chain almost nobody pays to use; the turnaround rests on products that have not launched.

| 📊 Market (CoinGecko, 16 Nov 2026 8:20 AM MST) | 🔗 On-chain (Astar, 16 Nov 2026) |
|---|---|
| **Price** $0.00443889 | **Total issuance** 8,830,538,340 ASTR (Subscan API) |
| **24h / 7d / 30d** 🟢 +0.3% / 🔴 −12.8% / −27.4% · 1y −67.0% | **Locked** 3.11B · dApp-staking bonded 2.92B (33%) |
| **Market cap** $39.19M · **FDV** $39.20M | **On-chain treasury** [`YQnb…fXhd`](https://astar.subscan.io/account/YQnbw3oWxBnCUarnbePrjFcrSgVPP2jqTZYzWcccmN8fXhd) 304,497,672 ASTR (RPC `System.Account`) |
| **24h volume** $908k (Binance, HTX, WhiteBIT, Pionex) | **Chain TVL** $1.02M · fees 12 months $1,900 ([DefiLlama](https://api.llama.fi/summary/fees/astar?dataType=dailyFees)) |
| **ATH** $0.4216 (17 Jan 2022) · now −98.9% | **ERC20 on Ethereum** [`0xF274…9689`](https://etherscan.io/token/0xf27441230eadeac85b764610325cc9a0d7859689) only 13.97M, 729 holders |

---

## 💰 Revenue — Does it make money? · 1/10 · ❌ FAIL

| Metric | Value | Source |
|---|---:|---|
| Chain fees, last 12 months | **$1,900** ($83 in 30 days) | [Tier A] [DefiLlama fees](https://api.llama.fi/summary/fees/astar?dataType=dailyFees) |
| Revenue (burned fees), last 12 months | **$689** | [Tier A] [DefiLlama revenue](https://api.llama.fi/summary/fees/astar?dataType=dailyRevenue) |
| Fee burn | 80% of gas fees are burned, 20% go to collators | [Tier A] [Astar Tokenomics 3.0](https://astar.network/blog/tokenomics-3-0-233/) |
| Staker income | New issuance (~3% a year) | [Tier A] same |

**What it means:** Revenue rounds to zero. **1, which trips the Revenue gate.**

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** Revenue rounds to zero; no material fee-funded burn, buyback or fee share is documented in this report.

## 🏛️ Foundation & team — Who is in charge? · 4/10 · ❌ FAIL

| Item | Finding | Source |
|---|---|---|
| Structure | The Astar Foundation stewards the chain. Governance runs through the Main Council, Finance Committee, Community Council and Technical Committee. Startale (builder of Soneium) is described as a "contributor" and partner, not the decision-maker | [Tier A] Foundation post on the [Astar forum](https://forum.astar.network/t/state-of-burndrop/9514) |
| Strategy | 2026 pivot to consumer finance starting from Japan: AstarFi (V1 "in the coming months" as of Jun 2026) and ASTR cashback on a Japanese Visa card | [Tier A] same |
| Engineering | Holders point out that one developer maintains the public L1 repo; the Foundation says most work is on private product repos | [Tier A/B] same, [Unverified] |
| Community trust | Long forum threads complain of silence and of the founding team focusing on Soneium; the Foundation admits it was "too quiet, for too long" | [Tier A] same |

## 🪙 Foundation / team holdings — How many coins do they hold? · 4/10 · ❌ FAIL

| Holder | ASTR | Notes |
|---|---:|---|
| On-chain treasury pallet [`YQnb…fXhd`](https://astar.subscan.io/account/YQnbw3oWxBnCUarnbePrjFcrSgVPP2jqTZYzWcccmN8fXhd) | 304.5M (3.4%) | Gets 5% of emissions; spending needs governance [Tier A RPC + docs] |
| Astar Foundation | **Not found** | The Foundation says its treasury is held "across stablecoins, other assets, and ASTR" and gives no figures ("I won't put numbers on a forum") |
| ERC20 top holder [`0x747f…7A95`](https://etherscan.io/address/0x747f98a14e5ea2ca9c076f938a6c6f12eb377a95) | 7.5M ERC20 | Unlabelled on [Arkham](https://intel.arkm.com/explorer/address/0x747f98a14e5ea2ca9c076f938a6c6f12eb377a95); one inbound transfer of 7.5M from unlabelled `0x379c…` on 16 Jun 2026 ([tx](https://etherscan.io/tx/0xfab353089083a7789ae68dd7fd8745f5a2c2e1071e4c4a2041485b5136c02e0f)); no Foundation or bridge label |
| ERC20 holder [`0xDC9e…C1d4`](https://intel.arkm.com/explorer/address/0xdc9ea45ad25c7766a369707dcff8202b216cc1d4) | 0.85M ERC20 | Arkham: unlabelled, first funded by an individual-labelled ENS wallet; an active DeFi user, not a Foundation wallet |

**What it means:** The protocol treasury is transparent; the Foundation's own holdings are not. **4**.

## 📉 Selling behavior — Do insiders sell into pumps? · 5/10 · ❌ FAIL

*Gate ASTR/USDT daily closes (UTC): 30 of the last 365 days were pump days.*

- The Foundation stated in Jun 2026 that "our operating costs are not covered by selling ASTR" ([forum](https://forum.astar.network/t/state-of-burndrop/9514)) [Tier A claim, not checkable on-chain].
- No Foundation wallets are published, and the Subscan API needs a key, so **no Foundation transfers were pump-tested**.

**What it means:** Not proven clean, so **5**.

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from Gate ASTR_USDT UTC daily closes, re-run 16 Nov 2026 with scripts/pump_day_test.py (30 of 360 days); the body's earlier count used Gate ASTR/USDT daily closes.

## 📊 Tokenomics & supply · 6/10 · ✅ PASS

- **Tokenomics 3.0 (16 Mar 2026):** ceiling cut from 7% to 5.5%, actual ~3%, block emissions decay, and supply converges toward ~10B ([Astar blog](https://astar.network/blog/tokenomics-3-0-233/)).
- 8.83B issued today, so about 13% more supply can still come. 80% of gas fees are burned, but fees are tiny.
- Burndrop (burn ASTR for future Startale-ecosystem tokens) is opt-in and has no date.

## 💧 Liquidity & market · 4/10 · ❌ FAIL

- $908k of 24h volume on a $39.2M cap (2.3% turnover), on Binance, HTX and WhiteBIT.
- −98.9% from ATH, −67% in a year, −27% in 30 days.

## 🧑‍💻 Product & development · 5/10 · ❌ FAIL

- The L1 is in a "stability and hardening" phase (WASM smart contracts sunset, runtime 2204 moved to slot-based AURA). AstarFi was not live as of Jun 2026 ([forum](https://forum.astar.network/t/state-of-burndrop/9514)).

## 🤝 Adoption & customers · 2/10 · ❌ FAIL

- $1.02M TVL and $83 of fees in 30 days ([DefiLlama](https://api.llama.fi/v2/chains)). ASTR is one of three cashback assets on the bitbank–EPOS card (0.5% cashback) [Tier A Foundation post, single source].

## 🛡️ Security & audits · 6/10 · ✅ PASS

- No exploit of the Astar chain or the ASTR token found in this pass. It is secured as a Polkadot parachain.

## ⚖️ Regulatory · 5/10 · ❌ FAIL

- No enforcement action found. The consumer-finance pivot puts it under Japanese financial rules [Unverified].

## 📅 Catalysts & calendar · 4/10 · ❌ FAIL

| Date | Event |
|---|---|
| TBA | AstarFi V1 launch |
| TBA | Burndrop (needs partner confirmation of the eligible tokens) |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | 🟡 Not tested (wallets unpublished) |
| Live mint path | 🔴 ~3% yearly inflation, capped near 10B |
| Treasury in single-key wallets | 🟡 Foundation unknown; protocol treasury is a governed pallet |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| None found | — | — | low | no | Selling not proven |

## 📚 Sources

- [Tier A] Methodology update 16 Nov 2026: no new Arkham lookups; the attribution table uses evidence already cited in this report.
- [Tier A] Astar Substrate RPC `state_getStorage` for `System.Account` of the treasury pallet (`py/trsry`); Subscan token endpoint (total issuance, locked, bonded), read 16 Nov 2026 ~9:00 AM MST
- [Tier A] DefiLlama `astar` fees and revenue; DefiLlama chains TVL
- [Tier A] [Astar Tokenomics 3.0](https://astar.network/blog/tokenomics-3-0-233/) · [Astar forum "State of burndrop"](https://forum.astar.network/t/state-of-burndrop/9514)
- [Tier A] Blockscout ERC20 holders; CoinGecko `astar` (16 Nov 2026 8:20 AM MST); Gate ASTR/USDT daily candles
- [Tier B] Arkham, read 16 Nov 2026 (signed-in account): no entity label on the two ERC20 holders checked. Arkham does not cover Astar's Substrate or EVM chains, so the treasury pallet could not be looked up
- [Unverified] Foundation holdings and wallets; engineering headcount; AstarFi launch date

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| ~3% inflation, 5.5% ceiling, ~10B maximum, 80% fee burn | [Astar blog](https://astar.network/blog/tokenomics-3-0-233/) | A | 16 Nov 2026 |
| $1.9k fees, $689 revenue in 12 months | [fees](https://api.llama.fi/summary/fees/astar?dataType=dailyFees) · [revenue](https://api.llama.fi/summary/fees/astar?dataType=dailyRevenue) | A | 16 Nov 2026 |
| Treasury pallet 304.5M ASTR | [Subscan account](https://astar.subscan.io/account/YQnbw3oWxBnCUarnbePrjFcrSgVPP2jqTZYzWcccmN8fXhd) | A | 16 Nov 2026 |
| Foundation: no ASTR sales for operations; Burndrop sequenced; AstarFi pending | [forum thread](https://forum.astar.network/t/state-of-burndrop/9514) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Owner of the 7.5M ERC20 holder and its funder `0x379c…`** | Arkham (16 Nov 2026) shows no label. Ask Astar whether it is a Foundation or bridge wallet [Unverified] | Free |
| 2 | **Foundation wallets and exchange flows** | Ask the Foundation for its addresses; trace them with a Subscan API key and pump-test them | Free API key |
| 3 | **Foundation treasury size** | Ask the Finance Committee for a treasury report | Free |
| 4 | **AstarFi and Burndrop dates** | Watch the Astar forum and blog | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
