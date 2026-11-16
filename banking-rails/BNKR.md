---
ticker: BNKR
name: Bankr (BankrCoin)
not_to_be_confused_with: "BANKROLL, BNKRW or other Bankr-launched tokens"
chain: base
contract: "0x22af33fe49fd1fa80c7149773dde5890d3c76f3b"
other_contracts:
  robinhood_chain: "0x178e54df3d091ee4d0b2534742ef9e3692b76526"
overall_score: 5.6
overall_verdict: FAIL
section_scores:
  revenue: 6
  foundation_team: 3
  insider_holdings: 7
  selling_behavior: 6
  tokenomics_supply: 8
  liquidity_market: 5
  product_development: 7
  adoption_customers: 5
  security_audits: 5
  regulatory: 3
  catalysts: 5
gates_failed: []
red_lines:
  monthly_revenue_below_250k: tripped
  buyback_safe_sells_bnkr: none_found_partial_scan
  hack_exploit: none_found
methodology_effective: 2026-11-16
revenue_reaches_holders: "yes"
revenue_mechanism: "Every Doppler launch trade pays a coded 0.2375% BNKR buyback fee, and BNKR is paid to stakers through BnkrStakingV3 ($190k in 30 days, executed on-chain). Revenue stays 6. Close call: the move from the buyback Safe into the staking stream is a Safe transaction, not a contract call."
pump_day_price_source: "Gate BNKR_USDT UTC daily closes, re-run 16 Nov 2026 with scripts/pump_day_test.py (66 of 360 days); the body's earlier count used CoinGecko daily closes"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions: []
price_usd: 0.00023038
price_source: "CoinGecko bankercoin-2, 15 Nov 2026 6:47 AM MST"
chain_read_block: 57802826
last_updated: 2026-11-15
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### BNKR · Overall grade **5.6 / 10 · ❌ FAIL**

**Summary:** A real business with clean token code: Bankr has earned about $17M in 12 months from token launches and trading, and since late September it has paid part of that to BNKR stakers. But revenue has fallen about 90% from its peak, the team is pseudonymous with no company filing found, and buy-side depth is thin.

**🚨 Top warning:** Revenue has fallen ~90% from its peak (last 30 days $237,790, under this series' $250k/month line), the team is pseudonymous with **no legal entity found**, and the buyback Safe [`0x0424…9b13`](https://basescan.org/address/0x042455f9990098e11592be1fbd72e6dc68419b13) needs only **2 of 2** keys with no delay. Positive: Arkham shows **no exchange deposits** from the buyback Safe or the 4% holder [`0x301f…fb28`](https://basescan.org/address/0x301f742573c76ee107cb8e263f2d5c009ecbfb28). Check: [buyback Safe on Arkham](https://intel.arkm.com/explorer/address/0x042455f9990098e11592be1fbd72e6dc68419b13) · [treasury Safe on Arkham](https://intel.arkm.com/explorer/address/0x5f8DA8F88eC81e27f2E22fCB9CA5D926c595E508) · [buyback Safe on Basescan](https://basescan.org/address/0x042455f9990098e11592be1fbd72e6dc68419b13).

**Sections passed: 5 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 6/10 | ✅ PASS |
| 🏛️ Foundation & team | 3/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 7/10 | ✅ PASS |
| 📉 Selling behavior | 6/10 | ✅ PASS |
| 📊 Tokenomics & supply | 8/10 | ✅ PASS |
| 💧 Liquidity & market | 5/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 7/10 | ✅ PASS |
| 🤝 Adoption & customers | 5/10 | ❌ FAIL |
| 🛡️ Security & audits | 5/10 | ❌ FAIL |
| ⚖️ Regulatory | 3/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 5/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 BNKR · Bankr · 5.6 / 10 · ❌ FAIL

> **One line:** A real business with clean token code: Bankr has earned about $17M in 12 months from token launches and trading, and since late September it has paid part of that to BNKR stakers. But revenue has fallen about 90% from its peak, the team is pseudonymous with no company filing found, and buy-side depth is thin.

| 📊 Market (CoinGecko, 15 Nov 2026 6:47 AM MST) | 🔗 On-chain (Base RPC, block 57,802,826) |
|---|---|
| **Price** $0.00023038 | **Contract** [`0x22aF33FE…3c76F3b`](https://basescan.org/address/0x22af33fe49fd1fa80c7149773dde5890d3c76f3b) · ERC-20 · 18 decimals |
| **24h / 7d / 30d / 1y** 🔴 −5.8% / −9.4% / −23.0% / −29.1% | **Supply** 100,000,000,000 (fixed) |
| **Market cap = FDV** $23.04M · rank #709 | **Genesis** 3 Dec 2024 04:44 UTC: 100% minted and sent straight into the Uniswap v3 pool |
| **24h volume** $2.23M | **Burned (0xdEaD)** 3.463B (**3.46%**), up from 3.04% on 3 Nov |
| **ATH** $0.001201 (10 Feb 2026) · now **−81%** | **Staked** 26.83B (**26.8%**) in the staking contract |
| **Main pool** Uniswap v3 BNKR/WETH, $1.40M liquidity | **Owner / mint / proxy** none |

---

## 💰 Revenue — Does it make money? · 6/10 · ✅ PASS

**How Bankr earns** ([Tier A] [docs.bankr.bot](https://docs.bankr.bot/llms-full.txt)): agents and users launch tokens through Bankr. On a Doppler launch every trade pays **1.75% all-in**: 0.665% to the creator, 0.285% locked LP, **0.475% Bankr protocol fee**, **0.2375% BNKR buyback** (BNKR buybacks + protocol-owned BNKR liquidity). Bankr Club costs $20/month or $198/year (USDC, BNKR or other tokens). Index-token fees are split between creator, Bankr treasury and BNKR stakers (FeeSplitter `0x9a926c84…`, StakersSink `0x6822e370…`).

| Metric (DefiLlama `bankr`, to 14 Nov 2026) | Value | Source |
|---|---:|---|
| Fees, 12 months (creators + Bankr) | **$40,159,423** | [Tier A] DefiLlama |
| **Revenue to Bankr, 12 months** | **$16,958,504** | [Tier A] DefiLlama |
| Revenue, all-time | $17,249,427 | [Tier A] |
| Fees / revenue, last 30 days | $530,337 / **$237,790** | [Tier A] |
| Fees / revenue, last 7 days | $34,934 / $21,121 | [Tier A] |
| Revenue, last 24h | $647 | [Tier A] |
| **Holders revenue** (BNKR paid into the staking stream since 26 Sep 2026) | 30 days **$190,045** · all-time **$336,255** | [Tier A] DefiLlama (method: BnkrStakingV3 inflows) |
| Revenue by month | Jan $2.30M · **Feb $4.53M** · Mar $640k · Apr $443k · May $3.42M · Jun $1.08M · Jul $1.27M · Aug $781k · Sep $1.95M · **Oct $443k** · Nov 1–14 $56k | [Tier A] |
| Buyback Safe → staking | **184,822,635 BNKR** on 20 Sep 2026 | [Tier A] Base logs |
| Burn | [`0xdEaD`](https://basescan.org/address/0x000000000000000000000000000000000000dEaD) holds 3,463,062,021 BNKR (3.46%) vs 3.04% on 3 Nov 2026 | [Tier A] RPC |

**What it means:** Bankr is a real fee business and some cash now reaches holders: about $190k in the last 30 days went to stakers, roughly 10% a year on today's market cap if it held. But revenue is volatile and falling hard (Feb $4.5M vs Oct $443k), and most revenue stays with the company.

- **Reaches holders (binary test, 16 Nov 2026 rules): Yes.** Every Doppler launch trade pays a coded 0.2375% BNKR buyback fee, and BNKR is paid to stakers through BnkrStakingV3 ($190k in 30 days, executed on-chain). Revenue stays 6. Close call: the move from the buyback Safe into the staking stream is a Safe transaction, not a contract call.

## 🏛️ Foundation & team — Who is in charge? · 3/10 · ❌ FAIL

| Item | Finding | Source |
|---|---|---|
| Legal entity | **Not found.** No company name, registration number or address in the docs | [Tier A] docs (absence) |
| Founder | Pseudonymous `@0xDeployer` on X; legal name not published | [Unverified] |
| GitHub | `BankrBot` org, 8 repos; `skills` (1,215 stars) pushed 15 Nov 2026; others last pushed Oct 2025 – May 2026 | [Tier A] GitHub API |
| Deployer | Contract created by factory [`0x9b84fce5…c3e1`](https://basescan.org/address/0x9b84fce5dcd9a38d2d01d5d72373f6b6b067c3e1), tx sent from [`0x72469d86…288f`](https://basescan.org/address/0x72469d86a92f5a9e975fe371a66015e667ab288f) (3 Dec 2024) | [Tier A] Base RPC |
| Buyback Safe [`0x042455f9990098e11592be1fbd72e6dc68419b13`](https://basescan.org/address/0x042455f9990098e11592be1fbd72e6dc68419b13) ([Arkham](https://intel.arkm.com/explorer/address/0x042455f9990098e11592be1fbd72e6dc68419b13)) | Safe, **2 of 2** signers: [`0xdd51d97f…14c0`](https://basescan.org/address/0xdd51d97ff41c382c8da1c63190bc2e0f112214c0) and [`0xf60633d0…163e`](https://basescan.org/address/0xf60633d02690e2a15a54ab919925f3d038df163e). Arkham: "Gnosis Safe Proxy", tagged "BNKR Whale", no entity name | [Tier A] Safe `getThreshold` / `getOwners` · [Tier B] Arkham, read 15 Nov 2026 ~10:40 AM MST |
| Treasury Safe [`0x5f8DA8F88eC81e27f2E22fCB9CA5D926c595E508`](https://basescan.org/address/0x5f8DA8F88eC81e27f2E22fCB9CA5D926c595E508) ([Arkham](https://intel.arkm.com/explorer/address/0x5f8DA8F88eC81e27f2E22fCB9CA5D926c595E508)) | Full address now known (Arkham). Safe, **2 of 2** signers (`0x1746c924…d565`, `0x538c4f2a…a8eb`); holds 624,421 USDC and 250,548 BNKR. Arkham lists "@0xdeployer (0xdeployer.eth)" as a signer, but `0xdeployer.eth` resolves today to `0x7124cf2e…5960`, which is **not** one of the two owners, so the founder link is not confirmed | [Tier A] Base RPC owners/threshold/balances + ENS · [Tier B] Arkham, read 15 Nov 2026 ~10:40 AM MST · Bankr ownership [Unverified] (old-draft Dune listing + Arkham tag) |
| Fee wallet `0xF606…` | Very likely [`0xf60633d02690e2a15a54ab919925f3d038df163e`](https://basescan.org/address/0xf60633d02690e2a15a54ab919925f3d038df163e): same prefix, it is one of the two buyback-Safe signers, and it sent 118.57M BNKR into the buyback Safe on 4 Jul 2026 | [Tier A] `getOwners` + logs · identity as the Dune-listed fee wallet [Unverified] |
| Investors | Base Ecosystem Fund (Coinbase Ventures) investment | [Unverified] old draft; not re-checked |

**What it means:** You are trusting an anonymous team with no visible legal entity, and the buyback wallet needs only two keys with no delay.

## 🪙 Foundation / team holdings — How many coins do they hold? · 7/10 · ✅ PASS

**No team allocation at launch.** The genesis transaction [tx `0x661d7c8f…4662`](https://basescan.org/tx/0x661d7c8f088bb866b756bf17cf74ca43890c18260318deab861e37e8d7594662) minted all 100,000,000,000 BNKR and sent them straight into the Uniswap v3 pool [`0xAEC085E5…E703`](https://basescan.org/address/0xaec085e5a5ce8d96a7bdd3eb3a62445d4f6ce703) ([Tier A] Base RPC logs, block 23,205,873).

| Wallet | Role | BNKR | % of supply | Source |
|---|---|---:|---:|---|
| [`0x88470240FF0663Faefa68B1D7621b472DdD9584A`](https://basescan.org/address/0x88470240FF0663Faefa68B1D7621b472DdD9584A) | Staking contract (all stakers) | 26,834,326,560 | 26.83% | [Tier A] RPC + docs |
| [`0x1172a9b0…0caf`](https://basescan.org/address/0x1172a9b08573dec93cd53132875046f8e0770caf) | Coinbase-labelled wallet (Nansen label) | 4,030,026,389 | 4.03% | [Tier A] balance · label [Unverified] |
| [`0x301f7425…fb28`](https://basescan.org/address/0x301f742573c76ee107cb8e263f2d5c009ecbfb28) ([Arkham](https://intel.arkm.com/explorer/address/0x301f742573c76ee107cb8e263f2d5c009ecbfb28)) | Large holder, key-held account (230 txs on Base). Arkham: **no entity**, tagged "AERO Whale"; also holds ~3.63M AERO and SPX; trades through 0x and OKX DEX routers; **no exchange deposits** seen | 3,996,184,663 | 4.00% | [Tier A] balance · [Tier B] Arkham, read 15 Nov 2026 ~10:40 AM MST · owner Not found |
| `0x000…dEaD` | Burn | 3,463,062,021 | 3.46% | [Tier A] |
| [`0xAEC085E5…E703`](https://basescan.org/address/0xaec085e5a5ce8d96a7bdd3eb3a62445d4f6ce703) | Main Uniswap v3 pool | 3,166,566,673 | 3.17% | [Tier A] |
| [`0x40ebc1ac…50c6`](https://basescan.org/address/0x40ebc1ac8d4fedd2e144b75fe9c0420be82750c6) | Unlabeled | 905,304,642 | 0.91% | [Tier A] |
| [`0x042455f9…9b13`](https://basescan.org/address/0x042455f9990098e11592be1fbd72e6dc68419b13) | **Buyback Safe (company)** | **587,068,789** | **0.59%** | [Tier A] |
| [`0x019fD9AB…17b7`](https://basescan.org/address/0x019fD9ABC9CaEB476D7AFA68BB675518C6BE17b7) | Legacy staking vault (withdraw-only since 8 Apr 2026) | 461,723,790 | 0.46% | [Tier A] |
| Company fee Safe staking 3.29B | ChainWard study, Oct 2026 (secondary) | — | ~3.3% | [Unverified] |

**What it means:** Insiders started at zero. The company's known wallet holds about 0.6% liquid, plus a possible ~3.3% staked position that hasn't been confirmed. No unlocks hang over the supply.

## 📉 Selling behavior — Do insiders sell into pumps? · 6/10 · ✅ PASS

**Pump test:** CoinGecko daily closes, 16 Nov 2025 – 15 Nov 2026: **67 of 360 days** were pump days (biggest: +298% five-day move on 31 Jan 2026; clusters in Jan–Feb, mid-May, and 19–28 Sep 2026).

| Check | Finding | Source |
|---|---|---|
| Team allocation to sell | None exists (100% into the pool at genesis) | [Tier A] |
| Buyback Safe on pump days | Every BNKR transfer found was **inbound** (buys from the pool and from fee wallets: e.g. 23.26M + 1.39M from the pool and 118.57M from `0xf60633d0…` on 4 Jul 2026; 58.19M + 1.07M from the pool on 28 Sep). **Only outbound: 184.82M to the staking contract on 20 Sep 2026** | [Tier A] Base `eth_getLogs` |
| Coverage of that scan | **46 of 134** pump-day log windows returned; 88 hit the public RPC's rate limit | Partial |
| Fee wallet / treasury Safe selling | Old draft: the fee wallet held 0–10k BNKR at every monthly snapshot because fees are taken in ETH | [Unverified] |
| Exchange flows (Arkham, all time) | **Buyback Safe:** no exchange activity; only Uniswap v3 pool trades. **Treasury Safe:** tiny Coinbase/Binance flows (≈$47K deposited all-time, Coinbase $36K + Binance $11K; 33.75K USDC withdrawn from a Coinbase hot wallet ~1 day before the read). **`0x301f…` (4%):** no exchange activity | [Tier B] Arkham, read 15 Nov 2026 ~10:40 AM MST (one source) |

**What it means:** No sign of insiders dumping into pumps. The known company wallet buys BNKR and sends it to stakers, and Arkham shows no exchange deposits from it or from the 4% holder. Arkham can't show which way each Uniswap trade went on each pump day, so the scan gap remains and this stays a provisional pass (score unchanged).

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from Gate BNKR_USDT UTC daily closes, re-run 16 Nov 2026 with scripts/pump_day_test.py (66 of 360 days); the body's earlier count used CoinGecko daily closes.

## 📊 Tokenomics & supply · 8/10 · ✅ PASS

| Item | Value | Source |
|---|---|---|
| Total supply | 100,000,000,000, fixed | [Tier A] `totalSupply()` |
| Owner / mint / proxy / tax | None found in bytecode; no `owner()`, no EIP-1967 slot | [Tier A] old draft bytecode read; supply re-read today |
| Circulating | 100% (CoinGecko) | [Tier B] |
| Unlocks | None | [Tier A] genesis |
| Burned | 3.46% | [Tier A] |
| Robinhood Chain BNKR | Separate contract `0x178E54df…6526` | [Tier A] docs |

## 💧 Liquidity & market · 5/10 · ❌ FAIL

| Pool / venue (15 Nov 2026) | Liquidity | 24h volume | Source |
|---|---:|---:|---|
| Uniswap v3 BNKR/WETH `0xAEC085E5…` | **$1,401,580** (3.17B BNKR + 368.59 WETH ≈ $673k) | $239,758 | [Tier A] DexScreener |
| Aerodrome BNKR/WETH `0xCfddb369…` | $53,334 | $143,843 | [Tier A] |
| Aerodrome BNKR/WETH `0xCDD442e2…` | $46,429 | $138,312 | [Tier A] |
| All 30 DEX pairs | $1,644,514 | | [Tier A] |
| Coinbase Exchange BNKR/USD | | $596,656 | [Tier B] CoinGecko |
| Coinbase book within ±2% | **Bids $1,265** · asks $17,638 | | [Tier A] Coinbase public API, 6:54 AM MST |

**Estimated sell impact** against the WETH side of the main pool (~$673k), constant-product math. Concentrated v3 ranges can make this better or worse:

| Sell size | Estimated drop |
|---:|---:|
| $5,000 | −1.5% |
| $10,000 | −2.9% |
| $25,000 | −7.0% |
| $50,000 | −13.4% |
| $100,000 | −24.2% |

**What it means:** Fine for small trades, but the Coinbase book holds almost no bids near the price, and a $50k sale would move the main pool about 13%.

## 🧑‍💻 Product & development · 7/10 · ✅ PASS

- Live: agent wallets, token launching (Base, Robinhood Chain, Arbitrum, Arc), LLM gateway paid from fees, limit/stop orders, index tokens, staking ([Tier A] docs, ~960 KB llms-full.txt).
- Staking v3: weekly BNKR rewards streamed over 7 days, multiplier 1x → 2x over 365 days, 48-hour unstake cooldown; legacy vault closed 8 Apr 2026 ([Tier A] docs).
- GitHub `BankrBot/skills` pushed 15 Nov 2026 ([Tier A]).

## 🤝 Adoption & customers · 5/10 · ❌ FAIL

- Paying usage is real: $40.2M of fees in 12 months ([Tier A] DefiLlama). Most of it is memecoin and agent-token trading, which comes and goes with speculation.
- 30-day fees $530k vs Feb 2026's ~$11.3M monthly peak.
- Named partners: none confirmed by the other party this pass. "Gives every Facebook user a wallet" and "is a bank" were already marked False in the old draft.

## 🛡️ Security & audits · 5/10 · ❌ FAIL

| Item | Finding | Source |
|---|---|---|
| Token contract | No owner, no mint, no proxy | [Tier A] |
| Buyback Safe | 2 of 2, no time lock | [Tier A] |
| Audits of staking / index / launch contracts | Not found in docs this pass | Not found |
| Hacks | None found in primary sources this pass | Not found |
| Custody | Bankr "Trading" wallets are signed by Bankr for the user ("Bankr signs for you") | [Tier A] docs |

## ⚖️ Regulatory · 3/10 · ❌ FAIL

- No legal entity, licence or registration found.
- The product signs for users' trading wallets, runs token launches, and offers trading and staking — the kinds of services that can need licences depending on where users are.
- No enforcement or court record found (not exhaustively checked).

## 📅 Catalysts & calendar · 5/10 · ❌ FAIL

| Date | Event | Effect |
|---|---|---|
| Weekly | Staking reward batch | Buy pressure from fees |
| Ongoing | Fee schedule fixed per launch; new launches use the 1.75% hook schedule | Revenue tied to launch volume |
| None dated | No roadmap dates found | |

## 🚩 Red lines status

| Red line | Status | Evidence |
|---|---|---|
| Monthly revenue under $250k | 🔴 **Tripped** | Oct 2026 $442,850; last 30 days $237,790 |
| Buyback Safe sells BNKR | 🟢 None found (partial scan) | Only outbound was to staking ([Basescan](https://basescan.org/address/0x042455f9990098e11592be1fbd72e6dc68419b13) · [Arkham: no exchange activity](https://intel.arkm.com/explorer/address/0x042455f9990098e11592be1fbd72e6dc68419b13)) |
| Hack / exploit | 🟢 None found | |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| Bankr buyback Safe | Bankr company wallet | Base logs (funds the staking stream) | high | yes (on-chain) | Holdings and Selling: buys BNKR, no exchange deposits found |

## 📚 Sources

- [Tier A] Methodology update 16 Nov 2026: no new Arkham lookups; the attribution table uses evidence already cited in this report.
- [Tier A] Base RPC (`base-rpc.publicnode.com`, `base.drpc.org`, `mainnet.base.org`): `totalSupply`, `balanceOf`, Safe `getOwners`/`getThreshold`, genesis logs at block 23,205,873, pump-day `eth_getLogs` for the buyback Safe; 15 Nov 2026
- [Tier A] [Bankr docs llms-full.txt](https://docs.bankr.bot/llms-full.txt) (fees, staking, contracts)
- [Tier A] DefiLlama `bankr` fees, revenue and holders revenue API, to 14 Nov 2026
- [Tier A] DexScreener token-pairs API; Coinbase Exchange public order book, 15 Nov 2026 6:54 AM MST
- [Tier A] GitHub API `BankrBot`
- [Tier B] CoinGecko `bankercoin-2` market data and 365 daily closes, 15 Nov 2026 6:47 AM MST
- [Tier A] Base RPC `getOwners`/`getThreshold`/`balanceOf` for the buyback and treasury Safes and `0x301f…`; ENS `0xdeployer.eth` resolution on Ethereum; 15 Nov 2026 ~10:50 AM MST
- [Tier B] Arkham Intelligence, read 15 Nov 2026 ~10:40 AM MST (signed-in account): `0x301f…` (no entity, "AERO Whale"), buyback Safe ("Gnosis Safe Proxy", "BNKR Whale"), treasury Safe `0x5f8DA8F8…E508` (signer tag @0xdeployer); exchange-flow totals
- [Tier A] Explorer pages used (Basescan): token [`0x22aF…`](https://basescan.org/address/0x22af33fe49fd1fa80c7149773dde5890d3c76f3b) · buyback Safe [`0x0424…`](https://basescan.org/address/0x042455f9990098e11592be1fbd72e6dc68419b13) · treasury Safe [`0x5f8D…`](https://basescan.org/address/0x5f8DA8F88eC81e27f2E22fCB9CA5D926c595E508) · fee wallet [`0xf606…`](https://basescan.org/address/0xf60633d02690e2a15a54ab919925f3d038df163e) · staking [`0x8847…`](https://basescan.org/address/0x88470240FF0663Faefa68B1D7621b472DdD9584A) · [`0x301f…`](https://basescan.org/address/0x301f742573c76ee107cb8e263f2d5c009ecbfb28) · pool [`0xAEC0…`](https://basescan.org/address/0xaec085e5a5ce8d96a7bdd3eb3a62445d4f6ce703) · genesis [tx `0x661d…`](https://basescan.org/tx/0x661d7c8f088bb866b756bf17cf74ca43890c18260318deab861e37e8d7594662)
- [Tier B] Arkham address pages used: [buyback Safe](https://intel.arkm.com/explorer/address/0x042455f9990098e11592be1fbd72e6dc68419b13) · [treasury Safe](https://intel.arkm.com/explorer/address/0x5f8DA8F88eC81e27f2E22fCB9CA5D926c595E508) · [0x301f…](https://intel.arkm.com/explorer/address/0x301f742573c76ee107cb8e263f2d5c009ecbfb28)
- [Unverified] Founder identity; company entity; Base Ecosystem Fund investment; fee wallet = `0xf60633d0…`; Bankr ownership of the treasury Safe; ChainWard 3.29B staked figure; Nansen labels

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer) or the label source (Arkham) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| No team allocation: all 100B BNKR minted straight into the Uniswap v3 pool | [genesis tx](https://basescan.org/tx/0x661d7c8f088bb866b756bf17cf74ca43890c18260318deab861e37e8d7594662) · [pool](https://basescan.org/address/0xaec085e5a5ce8d96a7bdd3eb3a62445d4f6ce703) | A | 15 Nov 2026 |
| Buyback Safe (2 of 2) holds 587.07M BNKR; only outbound was 184.82M to staking (20 Sep 2026); Arkham: no exchange activity | [Basescan](https://basescan.org/address/0x042455f9990098e11592be1fbd72e6dc68419b13) · [Arkham](https://intel.arkm.com/explorer/address/0x042455f9990098e11592be1fbd72e6dc68419b13) | A + B | 15 Nov 2026 ~10:50 AM MST |
| Treasury Safe `0x5f8D…` (2 of 2): ~$47K to Coinbase/Binance all-time, 624,421 USDC | [Basescan](https://basescan.org/address/0x5f8DA8F88eC81e27f2E22fCB9CA5D926c595E508) · [Arkham](https://intel.arkm.com/explorer/address/0x5f8DA8F88eC81e27f2E22fCB9CA5D926c595E508) | A + B | 15 Nov 2026 |
| Fee wallet `0xf606…` sent 118.57M BNKR into the buyback Safe (4 Jul 2026) | [Basescan](https://basescan.org/address/0xf60633d02690e2a15a54ab919925f3d038df163e) | A (fee-wallet identity [Unverified]) | 15 Nov 2026 |
| 4% holder `0x301f…`: no entity, no exchange deposits | [Basescan](https://basescan.org/address/0x301f742573c76ee107cb8e263f2d5c009ecbfb28) · [Arkham](https://intel.arkm.com/explorer/address/0x301f742573c76ee107cb8e263f2d5c009ecbfb28) | A + B | 15 Nov 2026 |
| Staking contract holds 26.83B BNKR (26.83%); burn address 3.46B | [staking](https://basescan.org/address/0x88470240FF0663Faefa68B1D7621b472DdD9584A) · [0xdEaD](https://basescan.org/address/0x000000000000000000000000000000000000dEaD) | A | 15 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | How to close it | Access needed |
|---|---|---|---|
| 1 | Finish the pump-day scan for the buyback Safe `0x042455f9…9b13` (88 of 134 windows missing). *Narrowed 15 Nov:* Arkham shows no exchange deposits ever, only Uniswap v3 pool trades, so the remaining question is only the direction of pool trades on pump days | Re-run `eth_getLogs` on BNKR Transfer events with `from`/`to` = the Safe over the 67 pump days, 50,000-block windows, slower rate; or Basescan / Etherscan v2 `tokentx` for the address | Public RPC: free but rate-limited. **Etherscan v2 API key** (free tier) for a one-call answer |
| 2 | **Partly closed:** treasury Safe is `0x5f8DA8F88eC81e27f2E22fCB9CA5D926c595E508` (2 of 2; Arkham); fee wallet `0xF606…` is very likely buyback-Safe signer `0xf60633d02690e2a15a54ab919925f3d038df163e`. Still open: confirm both against Bankr's own list, plus Bankr's "three fee addresses" per chain | Bankr's Dune dashboard `dune.com/bankrofficial/bankr-metrics` (query SQL names the addresses); DefiLlama's `bankr` adapter source on GitHub (`DefiLlama/dimension-adapters`, `fees/bankr`) lists the fee addresses | Free (Dune account for SQL view) |
| 3 | Whether those fee wallets sold BNKR on pump days | After #2, run the same log scan on each address and check if receivers are DEX pools or CEX deposits | Free / Etherscan key |
| 4 | Owner of `0x301f742573c76ee107cb8e263f2d5c009ecbfb28` (4.0% of supply). *Narrowed 15 Nov:* Arkham has no entity (tag "AERO Whale") and shows no exchange activity, so it is not a known exchange or fund wallet | First funding tx on Basescan; Nansen label; ask Bankr whether it is a team, investor or market-maker wallet | Free / request · Nansen paid |
| 5 | Company entity and founder identity | Ask Bankr for its legal entity; then Delaware / Wyoming / Cayman / BVI registers; check Terms of Service on bankr.bot for the contracting entity | Request to team; some registers charge a fee |
| 6 | Base Ecosystem Fund / Coinbase Ventures investment | Coinbase Ventures portfolio page or Base blog post naming Bankr | Free |
| 7 | Audits of staking v3 (`0x88470240…`), index contracts and the Doppler hook | Ask Bankr; check Basescan "Contract" tab for audit links; search audit firms' public report lists | Free / request |
| 8 | ChainWard claim that the company fee Safe stakes 3.29B BNKR | Read the staking contract's per-account stake (staking ABI in the docs) for the fee Safe once its address is known (#2) | Free |
| 9 | Staking reward size per week | bankr.bot/stake page, or the staking contract's reward-rate getters | Free |
| 10 | Licensing for custodial trading wallets | Ask Bankr which jurisdiction and licence (if any) covers custodial wallets; check FinCEN MSB search and the EU ESMA CASP register | Free / request |
| 11 | Hacks or wallet incidents | Search Bankr's X account and docs changelog for incident posts; check rekt.news and DefiLlama hacks list | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
