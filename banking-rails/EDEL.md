---
ticker: EDEL
name: Edel Finance
chain: base
contract_base: "0xFb31f85A8367210B2e4Ed2360D2dA9Dc2D2Ccc95"
overall_score: 2.5
overall_verdict: FAIL
section_scores:
  revenue: 1
  foundation_team: 4
  insider_holdings: 3
  selling_behavior: 3
  tokenomics_supply: 3
  liquidity_market: 4
  product_development: 3
  adoption_customers: 1
  security_audits: 1
  regulatory: 4
  catalysts: 2
gates_failed: [revenue, selling_behavior]
red_lines:
  hack_exploit: tripped_twice
  official_liquidity_pulled: tripped
  founder_or_director_exit: none_found
price_usd: 0.01082
price_source: "CoinGecko, 14 Nov 2026 9:08 AM MST"
last_updated: 2026-11-14
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### EDEL · Overall grade **2.5 / 10 · ❌ FAIL**

**Summary:** A renounced, fixed-supply Base token from a BVI company, with two security incidents in 2026, a lending product that was shut down, no revenue to the token, and 60% of supply taken by insiders in the launch transaction.

**Sections passed: 0 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 1/10 | ❌ FAIL |
| 🏛️ Foundation & team | 4/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 3/10 | ❌ FAIL |
| 📉 Selling behavior | 3/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 3/10 | ❌ FAIL |
| 💧 Liquidity & market | 4/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 3/10 | ❌ FAIL |
| 🤝 Adoption & customers | 1/10 | ❌ FAIL |
| 🛡️ Security & audits | 1/10 | ❌ FAIL |
| ⚖️ Regulatory | 4/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 2/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 EDEL · Edel Finance · 2.5 / 10 · ❌ FAIL

> **One line:** A renounced, fixed-supply Base token from a BVI company, with two security incidents in 2026, a lending product that was shut down, no revenue to the token, and 60% of supply taken by insiders in the launch transaction.

| 📊 Market (CoinGecko, 14 Nov 2026 9:08 AM MST) | 🔗 On-chain (Base RPC, 12–13 Nov 2026) |
|---|---|
| **Price** $0.01082 | **Canonical token** `0xFb31…Ccc95` (Base, 18 dp) |
| **24h / 7d / 30d** 🔴 −1.6% / −52.5% / −64.8% | **Supply** 1,000,000,000 fixed · owner `0x0` · levy 0 |
| **Market cap** $7.65M · **FDV** $10.82M | **Hedgey vesting** 293.66M (29.4%) |
| **24h volume** $708,941 | **Launch-tx insider take** 602.39M (60.24%) |
| **ATH** $0.1109 (19 Nov 2025) · now −90% | **New LP controlled by one wallet** ~98.6%, none locked |
| **Circulating (CoinGecko)** 706.66M | **Solana mint authority** still set |
| **Holders** 34,365 · top 10 = 48.96% (GeckoTerminal) | **Bridges** ETH, BNB, Solana, Robinhood Chain (LayerZero OFT) |

---

## 💰 Revenue — Does it make money? · 1/10 · ❌ FAIL

| Metric | Value | Source |
|---|---:|---|
| DefiLlama all-time fees | $47,728.86 | [Tier A] DefiLlama `edel` |
| DefiLlama all-time revenue | $4,771.47 | [Tier A] DefiLlama |
| 30-day fees / revenue | $0 / $0 | [Tier A] DefiLlama |
| TVL | ~$838 (borrowed 0) | [Tier A] DefiLlama |
| TVL before 30 Jun 2026 exploit | $632,753 → $952 a day later | [Tier A] DefiLlama |
| Markets (Canton perps) API | 13 markets, open interest 0, dust USDCx volume | [Tier A] Edel Markets API, 12 Nov |
| Token's claim on revenue | **None.** MiCAR paper: "does not grant any legally enforceable or contractual rights" | [Tier A] MiCAR white paper |

- Marketing says "share in protocol revenue." The legal filing says no. The filing wins.
- Official X, 10 Nov 2026: TVL $0, paused because "the economics don't justify the operation."

**What it means:** The business earned about $4.8k of revenue in its whole life, and none of it flows to the token.

## 🏛️ Foundation & team — Who is in charge? · 4/10 · ❌ FAIL

| Item | Finding | Source |
|---|---|---|
| Issuer | Titan Labs Limited, BVI company 2194169, LEI `529900E9GA8R99VOHV41` (ACTIVE) | [Tier A] MiCAR paper, GLEIF |
| Registered | 25 Nov 2025 (paper) · GLEIF creation 24 Nov 2025 | [Tier A] |
| Token launched | 12 Nov 2025, **13 days before** the company existed | [Tier A] Base launch tx |
| Terms of Service operator | "TITAN LIMITED", P.O. Box 3189 (paper/GLEIF use Titan Labs Limited, Box 3198) | [Tier A] docs.edel.finance/legal/terms |
| Directors (MiCAR) | Andrés Soltermann · James Sherborne | [Tier A] MiCAR A.12 / D.5 |
| CTO (site only) | Roman Fritschi, **not named** in the MiCAR filing | [Tier A] site · [Tier A] filing |
| Prior company | Grizzly Development AG (Zug): Fritschi board president, Soltermann board member. Bankruptcy opened 17 Jun 2025, discontinued for lack of assets 19 Sep 2025 | [Tier A] SHAB / Zefix |
| Sherborne | Director of Saxon Advisors Ltd (UK 11443641, Active) | [Tier A] Companies House |
| Head office | "No head office"; no published financial statements | [Tier A] MiCAR |
| Investors | "Titan Labs, private investors and/or ecosystem partners" — no rounds, prices or leads | [Unverified] |

**What it means:** Real, findable people and a real BVI shell, but the company was formed after the token, and two founders' last company went bankrupt with no assets.

## 🪙 Foundation / team holdings — How many coins do they hold? · 3/10 · ❌ FAIL

| Wallet / contract | EDEL | % of 1B | Locked? |
|---|---:|---:|---|
| Hedgey TokenVestingPlans `0x2CDE9919e81b20B4B33DD562a48a84b54C48F00C` | 293,656,323.85 | 29.37% | Vesting (mixed schedules) |
| · Team re-lock (26 Mar 2026) | 127,000,000 | 12.70% | 🔒 cliff 26 Mar 2027, end 25 Mar 2029 |
| · Reserves | 99,945,543 + 699,735 redeemable | ~10.06% | Vesting to 11 Nov 2028 |
| · Investors 4 | 28,167,986 + 197,214 redeemable | ~2.84% | Vesting to 11 Nov 2028 |
| · Investors 1–3 (50 plans) | 0 + 5,550,146 unclaimed | 0.56% | 🔓 fully vested 11 Feb 2026 |
| Cluster wallet `0x0c3eA09eD6798BFF724588e07EACA8278AD64E07` | 3,842,840 | 0.38% | 🔓 liquid |
| Same wallet: new-pool LP | 60,497.87 of 61,331.64 LP (~98.6%) | — | 🔓 none locked |
| OFT adapter owner (EOA) `0x9a1f4408252d524419c2d8ccb4845e47799c1376` | 980,461 | 0.10% | 🔓 |
| MiCAR "issuer retained" | 150,000,000 | 15% | Matches reserves lock |

Snapshot: Base block 56,602,263 (12 Nov 2026, 12:13 PM MST) and 13 Nov re-reads.

**What it means:** About 29% sits in vesting, and one wallet that the team uses controls almost all of the main pool's liquidity with no lock.

## 📉 Selling behavior — Do insiders sell into pumps? · 3/10 · ❌ FAIL

| Date (MST) | Event | Evidence | Verdict |
|---|---|---|---|
| 12 Nov 2025 10:00 AM | Deploy tx `0x66505d60…0e86e` swapped 5.622 ETH for **602,385,686 EDEL (60.24%)** behind a 50% levy that paid the deployer's own chosen wallet | [Tier A] Base receipt | Insider acquisition at launch |
| 12 Nov 2025 | 100 deployer-chosen levy wallets collected ~195M EDEL from outside buyers and **sold it into Uniswap V3 pool `0x97fcf528…3c06`** within ~1,100 blocks. All 100 hold 0 today | [Tier A] Base logs | Insider-linked dumping at launch (not a "pump window" under the 5-day test) |
| 12 Nov 2025 | Funder sent 53,799,721 EDEL to 63 unknown addresses | [Tier A] logs · destinations [Unverified] | Open |
| 12 Nov 2026 3:17–3:26 PM | Official Aerodrome LP lock expired 2:23 PM; `0x0c3e` withdrew 60,219.35 LP, took 162.48 WETH + 22.37M EDEL (~$656k), re-deposited into new pool `0xb01cc306…0a33` (created 28 Oct by `0x859bc5fe…`). **No sale in those five txs.** No announcement | [Tier A] five Base receipts | Liquidity pulled and re-parked under one wallet |
| 12 Nov 2026 8:31 AM | Team: "$300k worth of $EDEL tokens have been stolen and sold"; MEXC and BloFin blocked the rest | [Tier A] official X · steal txs [Unverified] | Second incident |

- Formal pump test (Real Rails v69): 97 windows of ≥10% over 5 daily closes since launch. **No two-label team → exchange deposit found.** Year-long Base routing only partly recovered.

**What it means:** No proven sale into a pump, but insider-chosen wallets dumped outside buyers' tax at launch and the official liquidity was pulled without a word. Treat as hostile until shown otherwise.

## 📊 Tokenomics & supply · 3/10 · ❌ FAIL

| Item | Value | Source |
|---|---|---|
| Total supply | 1,000,000,000 (Base canonical, fixed, no mint/pause/blacklist) | [Tier A] Sourcify + RPC |
| Bridged copies | ETH OFT 8.51M · BNB OFT 5.86M · Solana 27.99M · Robinhood Chain 55.11M | [Tier A] RPC |
| Base OFT adapter lockbox | 97.45M (balances to remotes within ~0.02%) | [Tier A] |
| Solana mint authority | **Still set** (`2zw5h8BMFA29tp1DN9m9itiL8QmkKazeEynGc6WFN9ra`) | [Tier A] Solana RPC |
| Official tokenomics post | Investors 15.8%, 10% TGE then 12-month linear | [Tier A] official X, 13 Nov 2025 |
| On-chain reality | Investors 1–3 vested in **3 months**, not 12. Percentages sum to 99.2% | [Tier A] Hedgey decode |
| Burns | No schedule; dead balance 67.76 EDEL | [Tier A] |
| Upcoming | Team cliff 26 Mar 2027; reserves + Investors 4 through Nov 2028 | [Tier A] |

**What it means:** The Base token is clean code. The schedule around it does not match what the team posted.

## 💧 Liquidity & market · 4/10 · ❌ FAIL

| Pool | Reserves | Indicative USD | Who controls LP |
|---|---|---:|---|
| New Aerodrome V2 WETH/EDEL `0xb01cc306…0a33` (12 Nov read) | 165.40 WETH + 22.74M EDEL | ~$667k | `0x0c3e` ~98.6%, unlocked |
| Old official pool `0x566bee…5A31` | 3.89 WETH + 532,605 EDEL | ~$15.7k | Locker balance 0 |

- 24h volume $708,941; price −52.5% over 7 days.

**What it means:** There is depth today, but the owner of almost all of it can withdraw at will.

## 🧑‍💻 Product & development · 3/10 · ❌ FAIL

- White paper: Aave V3-style lending for tokenized stocks/RWAs. **Officially sunset 11 Aug 2026** ("We sunset EVM lending as our vision expanded").
- Live: Canton instruments (SPYe, QQQe, NVDAe, SPCXe, EDELx) listed on Cantex; Markets API up and empty.
- GitHub `Edel-Finance`: 4 public repos; `edel-v3-core` is a retitled Aave V3 fork; `edel-ai-config` pushed 6 Nov 2026.

**What it means:** The flagship product is gone and the replacement has no users yet.

## 🤝 Adoption & customers · 1/10 · ❌ FAIL

- Confirmed: Cantex listing, Aerodrome pool, LayerZero OFTs.
- [Unverified] Anchorage, Flowdesk, DTCC working group, Ondo, Chainlink, a live Kraken listing — none confirmed by those parties.
- Self-reported volume, APY and user counts: [Unverified].

**What it means:** No paying customer you can point to.

## 🛡️ Security & audits · 1/10 · ❌ FAIL

| Incident | Date | Loss | Status |
|---|---|---|---|
| Lending price-feed exploit, tx `0xe2320086…2612` | 30 Jun 2026, 5:24 PM MST | ~$403k bad debt (official); 204,215.57 USDC net to attacker | Tranche 1 repaid 205,878.53 USDC (51%) to 238 wallets; tranche 2 **never created** |
| "$300k EDEL stolen and sold" | 12 Nov 2026 | ~$300k (official) | Post-mortem promised; steal txs not found on-chain |

- "Trust & Security" page lists **seven contract IDs that do not exist** (six empty EVM addresses, one invalid Solana key).
- The "full protocol audit" (Adevar) is a 3-day deployment-script review: 0 Fixed, 0 Acknowledged.

**What it means:** Two incidents in five months, half-paid restitution, and a fake contract list on a page titled "Built to Be Verified."

## ⚖️ Regulatory · 4/10 · ❌ FAIL

- MiCAR white paper **notified** 14 Jan 2026 (home state Ireland). A notification is not a licence or an approval.
- No licence found on any regulator register. No court records found.

**What it means:** Paperwork exists; no regulator has vetted anything.

## 📅 Catalysts & calendar · 2/10 · ❌ FAIL

| Date | Event |
|---|---|
| Pending | Post-mortem on the 12 Nov theft |
| Pending | Merkl restitution tranche 2 (promised for "next week" on 7 Jul 2026) |
| 26 Mar 2027 | Team re-lock cliff (127M) |
| Through 11 Nov 2028 | Reserves + Investors 4 vesting |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit on the protocol | 🔴 **Tripped twice** (30 Jun and 12 Nov 2026) |
| Official liquidity pulled or unlocked | 🔴 **Tripped** (12 Nov 2026) |
| Founder or director exit | 🟢 None found |

## 📚 Sources

- [Tier A] Base RPC reads and receipts (launch, Hedgey, UNCX, LP migration), 12–13 Nov 2026
- [Tier A] [MiCAR white paper](https://assets.edel.finance/docs/2026-01-14-White-paper-Edel-FFG-R2MQ3JKN7.xhtml) · [GLEIF](https://search.gleif.org/#/record/529900E9GA8R99VOHV41)
- [Tier A] [docs.edel.finance](https://docs.edel.finance) · [terms](https://docs.edel.finance/legal/terms)
- [Tier A] Official X @edeldotfinance (statuses 2072154468058022033, 2074732155201097928, 2087168780669538679, 2120902181104611616, 2120908165168422923, 1989009678702088366)
- [Tier A] DefiLlama `edel` fees/revenue/TVL · Merkl campaign API
- [Tier A] Swiss SHAB / Zefix; UK Companies House 11443641
- [Tier A] CoinGecko `edel`, 14 Nov 2026 9:08 AM MST
- [Tier B] DL News 27 Nov 2025 and Cointelegraph (Bubblemaps sniping claim; on-chain first-60-block count is 19.18%, not 30%)
- [Unverified] Investors; partner claims; 12 Nov theft txs; 63 TGE-day recipients

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
