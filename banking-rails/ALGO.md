---
ticker: ALGO
name: Algorand
chain: algorand
contract: "native (no token contract)"
overall_score: 5.0
overall_verdict: FAIL
section_scores:
  revenue: 1
  foundation_team: 6
  insider_holdings: 6
  selling_behavior: 5
  tokenomics_supply: 7
  liquidity_market: 6
  product_development: 7
  adoption_customers: 4
  security_audits: 7
  regulatory: 8
  catalysts: 5
gates_failed: [revenue]
red_lines:
  one_hop_sale_status: proven
  hack_exploit: none
  foundation_sells_on_pump_days: tripped_disclosed_program
  structured_selling_status: paused_onchain_since_2026-08-24_not_announced
  foundation_share_of_online_stake_over_15pct: tripped
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "Staking rewards are paid from the Foundation treasury, not from fees; the planned revenue-funded buyback does not exist on-chain."
pump_day_price_source: "Gate ALGO_USDT UTC daily closes, re-run 16 Nov 2026 with scripts/pump_day_test.py (40 of 360 days); the body's earlier count used CoinGecko daily closes"
pump_day_disclosure_quality: formal_announcement
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions: []
price_usd: 0.080319
price_source: "CoinGecko algorand, 15 Nov 2026 6:45 AM MST"
chain_read_round: 66980074
last_updated: 2026-11-17
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### ALGO · Overall grade **5.0 / 10 · ❌ FAIL**

**Summary:** One of the most transparent foundations in crypto, with published wallets, quarterly reports and an SEC "digital commodity" listing. But the network earns almost nothing (about $6.5k of fees a year on DefiLlama), validators are paid from the Foundation's own stack, and the Foundation has sold steadily (about 103M ALGO left its selling wallets in the past year, some on pump days). Those sales stopped on-chain after 24 Aug 2026. Fails the revenue gate.

> ⚠️ **Top warning:** The Foundation's Fireblocks selling wallet [`44GWRTQG…`](https://allo.info/account/44GWRTQGSAYUJJCQ3GFINYKZXMBDVKCF75VMCXKORN7ZJ6BKPNG2RMGH7E) sent ALGO to unlabelled [`45KKMHBB…`](https://allo.info/account/45KKMHBBE5DDNPQNFAFNCOYLDIFKCKFLN4GZOOAEHLF6OR3CQSTELRCL6E) **on three pump days** — [3M on 1 Jun](https://allo.info/tx/MAZ5LSZ26DJI26HCYEUM63YWG4A4JLA7ETOHQJQ3IU6GUKA7GFFA), [5M on 5 Aug](https://allo.info/tx/QBXLVQ6UO4G3KTARLLMZNBP42C5CFHJNQCS3LEYX7XI3LWQCLZOQ), [3M on 24 Aug 2026](https://allo.info/tx/AZORFFIXMWMNWGGLD2GO6QAUYTI2J2UCSTJBTQ4UCSMFUBYZMOTQ) — and the Foundation controls **19.6% of online stake**. The selling program is disclosed; the final buyers are not.

**Sections passed: 7 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 1/10 | ❌ FAIL |
| 🏛️ Foundation & team | 6/10 | ✅ PASS |
| 🪙 Foundation / team holdings | 6/10 | ✅ PASS |
| 📉 Selling behavior | 5/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 7/10 | ✅ PASS |
| 💧 Liquidity & market | 6/10 | ✅ PASS |
| 🧑‍💻 Product & development | 7/10 | ✅ PASS |
| 🤝 Adoption & customers | 4/10 | ❌ FAIL |
| 🛡️ Security & audits | 7/10 | ✅ PASS |
| ⚖️ Regulatory | 8/10 | ✅ PASS |
| 📅 Catalysts & calendar | 5/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 ALGO · Algorand · 5.0 / 10 · ❌ FAIL

> **One line:** One of the most transparent foundations in crypto, with published wallets, quarterly reports and an SEC "digital commodity" listing. But the network earns almost nothing (about $6.5k of fees a year on DefiLlama), validators are paid from the Foundation's own stack, and the Foundation has sold steadily (about 103M ALGO left its selling wallets in the past year, some on pump days). Those sales stopped on-chain after 24 Aug 2026. Fails the revenue gate.

ℹ️ **Adapted for a layer-1.** "Revenue" = fees users pay and where they go. "Foundation" = the Algorand Foundation, which now operates as "Algorand" (it took over Algorand Technologies in Q1 2026). "Holdings / Selling" = the Foundation's published accounts and its structured-selling wallets, checked against pump days.

| 📊 Market (CoinGecko, 15 Nov 2026 6:45 AM MST) | 🔗 On-chain (AlgoNode algod + indexer, round 66,980,074) |
|---|---|
| **Price** $0.080319 | **Asset** native ALGO, no contract |
| **24h / 7d / 30d** 🔴 −2.2% / −15.0% / −32.2% | **Ledger total money** 9,820,111,709 ALGO (max 10,000,000,000) |
| **Market cap** $729.3M · **FDV** $729.3M | **Online (staking) stake** 2,001,416,970 ALGO |
| **24h volume** $51.5M | **Foundation published accounts, live** 878,853,131 ALGO (8.8% of max) |
| **ATH** $3.56 (20 Jun 2019) · now **−97.7%** | **Foundation stake online** 392,499,828 ALGO (**19.6%** of online stake) |
| **Circulating (CoinGecko)** 9.080B | **Fee Sink** [`Y76M3M…L226CA`](https://allo.info/account/Y76M3MSY6DKBRHBL7C3NNDXGS5IIMQVQVUAB6MP4XEMMGVF2QWNPL226CA) 11,584,063 ALGO |

---

## 💰 Revenue — Does it make money? · 1/10 · ❌ FAIL

| Metric | Value | Source |
|---|---:|---|
| 24h fees | $129 | [Tier A] DefiLlama `algorand` fees, 15 Nov 2026 |
| 30-day fees | $877 | [Tier A] DefiLlama |
| 12-month fees | **$6,470** | [Tier A] DefiLlama |
| All-time fees (DefiLlama coverage) | $15,652 | [Tier A] DefiLlama |
| Our cross-check | ~777,000 top-level tx/day × 0.001 ALGO minimum fee ≈ 777 ALGO/day ≈ **$62/day ≈ $23k/year at most** | [Tier A] block sample of 300 blocks, calculated |
| Where fees go | The **Fee Sink** account (Foundation-published). No burn | [Tier A] Foundation account page |
| What pays stakers | **20M ALGO per quarter** in validator rewards (Q1 and Q2 2026), funded by the Foundation; ≈ $1.6M a quarter at today's price | [Tier A] Q1 and Q2 2026 transparency reports |
| Plans | 6 Nov 2026: ideas to lift the supply cap, capture MEV or raise the minimum fee are "no longer being considered". New usage-based fees (e.g. for Falcon post-quantum transactions) "may still be introduced" | [Tier A] [Algorand Community Update](https://algorand.co/blog/algorand-community-update) |

**What it means:** Algorand is cheap to use by design, so the network earns almost nothing. Stakers are paid by the Foundation spending down its treasury, not by users. The new CEO's stated plan is to sell paid services and use that revenue to buy ALGO ([Unverified], one Tier B report). Nothing like that exists on-chain yet.

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** Staking rewards are paid from the Foundation treasury, not from fees; the planned revenue-funded buyback does not exist on-chain.

## 🏛️ Foundation & team — Who is in charge? · 6/10 · ✅ PASS

| Item | Finding | Source |
|---|---|---|
| Entity | Algorand Foundation. In Jan 2026 it **moved back to the US, with headquarters in Delaware**. It took over protocol development from Algorand Technologies in Q1 2026 and now publishes as "Algorand" | [Tier A] Q1 2026 transparency report |
| CEO | **William Herkelrath**, effective 31 Aug 2026, succeeding Staci Warden (announced 9 Sep 2026) | [Tier A] Algorand press release (PR Newswire) and algorand.co blog |
| CFO | Harpal Singh (signs the transparency reports) | [Tier A] Q2 2026 report |
| CTO | Bruno Martins was appointed in Mar 2026 (named in the Q1 2026 report) and **resigned around 9 Oct 2026**. No successor was named. Marketing and strategy chief Marc Vanlerberghe left around 14 Oct 2026 | [Tier A] Q1 2026 report (appointment); [Tier A] Martins' own X post, 9 Oct 2026 (resignation); [Tier B] contemporaneous news (Vanlerberghe) |
| Founder | Silvio Micali | [Unverified] not re-checked against a primary page this pass |
| Staff | **25% reduction in force** at the end of Q1 2026 | [Tier A] Q1 2026 report |
| Community bodies | 6 Nov 2026: **xGov grants paused** (effective 6 Dec), **forum closed**, Ecosystem Advisory Council ended, Technical Council sponsorship ended | [Tier A] Community Update |
| Reporting | Quarterly transparency reports since 2022; the latest posted is **Q2 2026**. Q3 2026 is not yet on the page as of 15 Nov | [Tier A] [transparency page](https://algorand.co/algorand-foundation/transparency) |
| Developer org | GitHub `algorand`; `go-algorand` last push 15 Nov 2026 | [Tier A] GitHub API |
| Senior departures | Reports of a third senior exit since August | [Unverified] one blog source |

**What it means:** Named leaders, a US home and real reporting. It is now more company-run and less community-run than a year ago.

## 🪙 Foundation / team holdings — How many coins do they hold? · 6/10 · ✅ PASS

| Item | ALGO | Source |
|---|---:|---|
| Foundation balance, 31 Dec 2025 | 1,134,532,000 | [Tier A] Q1 2026 report |
| Foundation balance, 31 Mar 2026 | 1,078,875,000 (−55.7M in the quarter) | [Tier A] Q1 2026 report |
| Foundation balance, **30 Jun 2026** | **1,036,000,000** | [Tier A] Q2 2026 report |
| **Live sum of all published accounts, 15 Nov 2026** (65 treasury + 2 market-operations + 10 governance/xGov) | **878,853,131** | [Tier A] algod account reads, round 66,980,074 |
| Of which: largest single account [`EWFYFTXIN7A4HIGZND3AK2QU3FPM4WZCDTCGO4Z3JFBIPKBKE3OOHQY62Q`](https://allo.info/account/EWFYFTXIN7A4HIGZND3AK2QU3FPM4WZCDTCGO4Z3JFBIPKBKE3OOHQY62Q) | 193,589,529 (offline) | [Tier A] |
| Of which: staking online | 392,499,828 | [Tier A] |
| Of which: selling wallet [`44GWRTQG…`](https://allo.info/account/44GWRTQGSAYUJJCQ3GFINYKZXMBDVKCF75VMCXKORN7ZJ6BKPNG2RMGH7E) (Fireblocks) | 3,641,609 | [Tier A] |
| Gap vs the 30 Jun report | **≈157M ALGO.** Q3 sales visible on-chain (~41.4M) plus ~1.5 quarters of staking rewards (~30M) explain about half | Calculated · rest [Unverified] |

**What it means:** The Foundation publishes its accounts, and the live total is checkable: about 879M ALGO (8.8% of max supply). It is a large stack, but it can be seen. About 86M ALGO of the drop since June is not yet explained, probably legacy or custodial accounts or Q3 spending the Q3 report will show.

## 📉 Selling behavior — Do insiders sell into pumps? · 5/10 · ❌ FAIL

**Pump test:** CoinGecko daily closes, 16 Nov 2025 – 15 Nov 2026: **39 of 360 days** were pump days (10.8%), including 5–7 Jan, 1–7 Apr (peak +52.1% on 4 Apr), 1 Jun, 4–7 Aug, 21–25 Aug and 21–30 Sep 2026. Last pump day 30 Sep 2026.

**The disclosed program** ([Tier A] Q1 and Q2 2026 reports): structured selling out of two published wallets, [`37VPAD3CK7CDHRE4U3J75IE4HLFN5ZWVKJ52YFNBX753NNDN6PUP2N7YKI`](https://allo.info/account/37VPAD3CK7CDHRE4U3J75IE4HLFN5ZWVKJ52YFNBX753NNDN6PUP2N7YKI) (BitGo) and [`44GWRTQGSAYUJJCQ3GFINYKZXMBDVKCF75VMCXKORN7ZJ6BKPNG2RMGH7E`](https://allo.info/account/44GWRTQGSAYUJJCQ3GFINYKZXMBDVKCF75VMCXKORN7ZJ6BKPNG2RMGH7E) (Fireblocks). Daily sales are capped by a fixed amount and a share of market volume. Sales **halt on a 10% drop in 24h** or below a price floor. **There is no rule against selling into a rise.** Reported sales: **24M ALGO in Q1 2026, 10.60M in Q2 2026.**

### A. Every outflow from the selling wallets, past 12 months ([Tier A] AlgoNode indexer)

| Period | From | To [`45KKMHBBE5DDNPQNFAFNCOYLDIFKCKFLN4GZOOAEHLF6OR3CQSTELRCL6E`](https://allo.info/account/45KKMHBBE5DDNPQNFAFNCOYLDIFKCKFLN4GZOOAEHLF6OR3CQSTELRCL6E) | Transfers |
|---|---|---:|---:|
| 24 Nov – 12 Dec 2025 | BitGo `37VPAD3C…` | 24,000,000 (6 × 4M) | 6 |
| 12 Jan – 23 Feb 2026 | Fireblocks [`44GWRTQG…`](https://allo.info/account/44GWRTQGSAYUJJCQ3GFINYKZXMBDVKCF75VMCXKORN7ZJ6BKPNG2RMGH7E) | 27,000,000 | 6 |
| 15 May – 29 Jun 2026 | Fireblocks | 10,647,668 (report: 10.60M sold in Q2 ✅) | 3 |
| 2 Jul – 24 Aug 2026 | Fireblocks | **41,358,391** (Q3, not yet in a published report) | 10 |
| **25 Aug – 15 Nov 2026** | both | **0** | 0 |

### B. Pump-day transfers

| Date (UTC) | Amount | 5-day move | Tx id |
|---|---:|---:|---|
| 1 Jun 2026 11:03 | 3,000,000 | +17.6% | [`MAZ5LSZ26DJI26HCYEUM63YWG4A4JLA7ETOHQJQ3IU6GUKA7GFFA`](https://allo.info/tx/MAZ5LSZ26DJI26HCYEUM63YWG4A4JLA7ETOHQJQ3IU6GUKA7GFFA) |
| 5 Aug 2026 08:48 | 10,000,000 **in** from Foundation account [`VAOTJJLJ…`](https://allo.info/account/VAOTJJLJP54QIKGCCFNJZVNHXXFZUZ3AAXCVGX5LRDQXQOUZRWBFBASUDQ) | +13.4% | [`6LQLL6ZMUAEKVK3BCC5XAOUUQUQOZZIWFJAOEVLHQJEZGTYV4EJQ`](https://allo.info/tx/6LQLL6ZMUAEKVK3BCC5XAOUUQUQOZZIWFJAOEVLHQJEZGTYV4EJQ) |
| 5 Aug 2026 09:53 | 5,000,000 out | +13.4% | [`QBXLVQ6UO4G3KTARLLMZNBP42C5CFHJNQCS3LEYX7XI3LWQCLZOQ`](https://allo.info/tx/QBXLVQ6UO4G3KTARLLMZNBP42C5CFHJNQCS3LEYX7XI3LWQCLZOQ) |
| 24 Aug 2026 14:32 | 3,000,000 | +20.6% | [`AZORFFIXMWMNWGGLD2GO6QAUYTI2J2UCSTJBTQ4UCSMFUBYZMOTQ`](https://allo.info/tx/AZORFFIXMWMNWGGLD2GO6QAUYTI2J2UCSTJBTQ4UCSMFUBYZMOTQ) |

- **3 of 25** selling-wallet transfers (12%) fell on pump days, against 10.8% of all days. That is what chance would give: the program sells on a schedule, not on rallies. It also does not stop for them.
- **Downstream:** [`45KKMHBB…`](https://allo.info/account/45KKMHBBE5DDNPQNFAFNCOYLDIFKCKFLN4GZOOAEHLF6OR3CQSTELRCL6E) (unlabelled; it is fed only by the selling wallets and two published treasury accounts, [`B223SVF4…`](https://allo.info/account/B223SVF452UWAMMLNIHIUAPHYPX5J3HLVJF6MNOHUJE2NWJBG7C66JILGE) and [`2TZAMEZZ…`](https://allo.info/account/2TZAMEZZDWFY37QV66HXWQIYWYJIZKE2KP3QNPI2QHHKSMKUZEICNMMUFU)) sent **112.9M ALGO** onward in the past year, mostly to [`DI6YXMONC7…`](https://allo.info/account/DI6YXMONC7PFVCRXHFP4UQCV5UXUFWO3Z2QURBV2K3SQLHILW3CROQ7UOI) (51.7M), [`S6VQ2RAB…`](https://allo.info/account/S6VQ2RABLUOAXZ2MUFQXKDYLPVIYDO4C72ZBY763CL534MCN5RLZASSEEI) (31.9M) and [`GSRT2TB2…`](https://allo.info/account/GSRT2TB2TADJ2YCE4A6O2ZH6TPFN3J2ACN5YOHT42MZKOO6LF4RFGAVSMQ) (19.6M). Those look like exchange or OTC deposit addresses ([Unverified]). **11.5M** of that went on pump days. It kept sending small amounts after the selling wallets stopped: 2.15M in Oct, 0.19M in Nov (latest 5 Nov 2026). It holds 311,735 ALGO now.
- **Did the program end?** On-chain, nothing has left either selling wallet since **24 Aug 2026**, a week before the new CEO started. **No announcement that structured selling ended was found** in Foundation sources. Status: paused on-chain, end [Unverified].

**What it means:** This is disclosed, rules-based selling, not a hidden dump, so it is not a hard-gate fail. But the Foundation was the steady seller for most of the year, including on some pump days, and Q3's ~41M ALGO of transfers is not yet covered by a report. 5/10.

- **Disclosure quality (16 Nov 2026 rules): formal announcement.** The Foundation publishes a rules-based selling program and reports its sales (Q3 2026 not yet reported), so no penalty applies; Selling stays 5. Pump days from Gate ALGO_USDT UTC daily closes, re-run 16 Nov 2026 with scripts/pump_day_test.py (40 of 360 days); the body's earlier count used CoinGecko daily closes.

## 📊 Tokenomics & supply · 7/10 · ✅ PASS

| Item | Value | Source |
|---|---|---|
| Max supply | 10,000,000,000 ALGO, protocol-fixed | [Tier A] |
| Ledger total money | 9,820,111,709 | [Tier A] algod `/v2/ledger/supply` |
| Circulating | 9.080B (CoinGecko); 9.06B at end-Sep per Blockworks | [Tier B] |
| Inflation | None beyond the cap; staking rewards are paid from existing ALGO | [Tier A] Community Update |
| Supply-cap lift | **Dropped** ("no longer being considered", 6 Nov 2026) | [Tier A] |
| Staking rewards | Committed through **January 2028** | [Tier A] Community Update |
| Burn | None | [Tier A] |
| Main overhang | Foundation's ~879M published stack (+ unreconciled ~157M gap) | [Tier A] / calculated |

## 💧 Liquidity & market · 6/10 · ✅ PASS

| Venue (CoinGecko tickers, 15 Nov 2026) | Pair | 24h volume | Bid depth to −2% |
|---|---|---:|---:|
| BitDelta | ALGO/USDT | $14.87M (29% of first 100 tickers) | n/a |
| Binance | ALGO/USDT | $2.91M | $172k |
| Kraken | ALGO/USD | $2.79M | $691k |
| Coinbase Exchange | ALGO/USD | $2.60M | $207k |
| Upbit | ALGO/KRW | $1.87M | $99k |
| Bybit | ALGO/USDT | $1.16M | $68k |
| OKX | ALGO/USDT | $1.10M | $95k |
| **Major-venue USD/stable pairs, total −2% depth** | | | **≈ $1.87M** |

- DeFi TVL on Algorand: **$25.5M** ([Tier A] DefiLlama).
- Biggest reported venue is a smaller exchange (BitDelta). On top-tier venues, real volume is a few million dollars a day each.

**What it means:** Listed everywhere that matters. Depth is modest: about $1.9M of bids within 2% across the majors, against a Foundation stack worth ~$70M.

## 🧑‍💻 Product & development · 7/10 · ✅ PASS

| Item | Detail | Source |
|---|---|---|
| Node | `go-algorand`: **98 commits in 13 weeks**; v5.0.5-stable (28 Oct 2026), v5.1.0-beta (6 Nov 2026) | [Tier A] GitHub API |
| Post-quantum | Algorand 5.0 made Falcon-1024 accounts native (late Aug 2026); PQ multisig planned by end-2026 | [Unverified] Blockworks Q3 report (one Tier B) |
| Block time | ~2.8 s (300-block sample) | [Tier A] calculated |
| Strategy shift | xGov grants paused; focus on selling post-quantum services to custodians, wallets and other networks | [Tier A] Community Update |

## 🤝 Adoption & customers · 4/10 · ❌ FAIL

| Item | Finding | Source |
|---|---|---|
| Activity | ≈ **777,000 top-level tx/day** (300-block sample) | [Tier A] calculated |
| Stablecoins on Algorand | **$120.7M** | [Tier A] DefiLlama stablecoins |
| DeFi TVL | $25.5M | [Tier A] DefiLlama |
| Online stake | 2.00B ALGO; community ~80% | [Tier A] / Q2 report |
| HesabPay | 1M+ users, ~$183M a month on Algorand | [Unverified] company claim via Blockworks |
| x402 agent payments | 1.04M settlements, $319k volume in Q3; fell sharply after early Sep | [Unverified] Blockworks |
| Flow Traders | Institutional ALGO liquidity partner | [Unverified] press release via old draft; not re-read |
| FIFA Collect | Moved **off** Algorand in May 2025 (old draft finding) | [Unverified] not re-read this pass |
| Ecosystem fees | Pact, Alpha Arcade and Haystack fees about halved to $17,500 in Q3 | [Unverified] Blockworks |

**What it means:** Lots of transactions and a growing stablecoin base, but little money moves through apps, and the strongest customer claims are self-reported.

## 🛡️ Security & audits · 7/10 · ✅ PASS

| Item | Finding | Source |
|---|---|---|
| Protocol hack | None found | [Tier A] absence |
| "14-hour mainnet outage, 9 Jun 2026" claim | **Not a chain halt.** Block timestamps run normally through the window (round 61,991,269 at 14:59:57 UTC → round 61,993,269 at 16:31:24 UTC, ~2.75 s blocks). The incident was on an RPC provider's status page | [Tier A] algod block reads |
| Same-day patch | go-algorand **v4.7.2-stable** (9 Jun 2026): "better bound checks to transaction evaluation code"; no protocol upgrade | [Tier A] GitHub release |
| Stake concentration | Foundation is **19.6%** of online stake | [Tier A] |
| Post-quantum | Falcon signatures supported | [Tier A] Community Update |

## ⚖️ Regulatory · 8/10 · ✅ PASS

| Item | Finding | Source |
|---|---|---|
| United States | SEC release **33-11412** (effective 23 Mar 2026) names **Algorand (ALGO)** a **digital commodity**, even though it had no CFTC futures contract | [Tier A] [sec.gov](https://www.sec.gov/files/rules/interp/2026/33-11412.pdf) |
| EU MiCA white paper | Crypto Risk Metrics GmbH via BaFin, 7 Apr 2026 (FFG K8S6W74KS), third-party filer | [Tier A] ESMA interim register |
| Foundation domicile | Delaware headquarters since Jan 2026 | [Tier A] Q1 report |
| Enforcement / court | None found | [Unverified] no docket search this pass |

## 📅 Catalysts & calendar · 5/10 · ❌ FAIL

| Date | Event | Effect |
|---|---|---|
| Any day now | Q3 2026 transparency report (Jul–Sep sales, ~41M ALGO of transfers seen on-chain) | Disclosure |
| 6 Dec 2026 | xGov grants paused | Less ecosystem funding |
| End 2026 | Native post-quantum multisig (planned) | Product |
| Open | Whether structured selling has formally ended | Removes a seller if yes |
| Through Jan 2028 | Foundation-funded staking rewards | Treasury spend continues |
| 8–9 Dec 2026 | FOMC meeting | Macro |

## 🚩 Red lines status

| Red line | Status | Evidence |
|---|---|---|
| Hack / exploit | 🟢 None | — |
| Foundation sells on pump days | 🔴 Tripped, under a **disclosed** program | [1 Jun](https://allo.info/tx/MAZ5LSZ26DJI26HCYEUM63YWG4A4JLA7ETOHQJQ3IU6GUKA7GFFA), [5 Aug](https://allo.info/tx/QBXLVQ6UO4G3KTARLLMZNBP42C5CFHJNQCS3LEYX7XI3LWQCLZOQ), [24 Aug](https://allo.info/tx/AZORFFIXMWMNWGGLD2GO6QAUYTI2J2UCSTJBTQ4UCSMFUBYZMOTQ) 2026 transfers from [`44GWRTQG…`](https://allo.info/account/44GWRTQGSAYUJJCQ3GFINYKZXMBDVKCF75VMCXKORN7ZJ6BKPNG2RMGH7E) to [`45KKMHBB…`](https://allo.info/account/45KKMHBBE5DDNPQNFAFNCOYLDIFKCKFLN4GZOOAEHLF6OR3CQSTELRCL6E) |
| Structured selling still running | 🟡 Paused on-chain since 24 Aug 2026; no announcement | Indexer |
| Foundation >15% of online stake | 🔴 Tripped (19.6%) | algod ([ledger supply](https://mainnet-api.algonode.cloud/v2/ledger/supply)) · [Foundation account list](https://algorand.co/algorand-foundation/transparency) |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| Algorand Foundation structured-selling wallets | Algorand Foundation | Foundation transparency reports + chain | high | yes (Foundation reports) | Selling: disclosed program sold on some pump days |

## 📚 Sources

- [Tier A] Methodology update 16 Nov 2026: no new Arkham lookups; the attribution table uses evidence already cited in this report.
- [Tier A] AlgoNode public algod ([`mainnet-api.algonode.cloud`](https://mainnet-api.algonode.cloud/v2/ledger/supply)) and indexer ([`mainnet-idx.algonode.cloud`](https://mainnet-idx.algonode.cloud/v2/accounts/45KKMHBBE5DDNPQNFAFNCOYLDIFKCKFLN4GZOOAEHLF6OR3CQSTELRCL6E/transactions?limit=100)); human-readable views on [Allo](https://allo.info) (every account and tx cited is linked inline and in the Evidence trail): ledger supply, all published Foundation accounts, selling-wallet and [`45KKMHBB…`](https://allo.info/account/45KKMHBBE5DDNPQNFAFNCOYLDIFKCKFLN4GZOOAEHLF6OR3CQSTELRCL6E) transaction histories, block samples; 15 Nov 2026 ~6:50 AM MST
- [Tier A] [Algorand Foundation transparency page and account list](https://algorand.co/algorand-foundation/transparency); Q1 2026 and Q2 2026 transparency reports (PDF)
- [Tier A] [Algorand Community Update, 6 Nov 2026](https://algorand.co/blog/algorand-community-update); CEO announcement (PR Newswire / algorand.co, 9 Sep 2026)
- [Tier A] Bruno Martins' X post, 9 Oct 2026, announcing his resignation as CTO; [Tier B] news coverage of that post and of Marc Vanlerberghe's departure around 14 Oct 2026
- [Tier A] DefiLlama fees, chain TVL, stablecoins; CoinGecko market data, tickers with depth and 365 daily closes (15 Nov 2026 6:45 AM MST)
- [Tier A] GitHub API `algorand/go-algorand` (activity, releases incl. v4.7.2-stable)
- [Tier A] SEC release 33-11412; ESMA interim MiCA register
- [Tier B] Blockworks "Algorand Token Holder Report Q3 2026" (13 Nov 2026); CoinDesk (CEO change)
- [Tier B] [Arkham](https://intel.arkm.com/explorer/address/45KKMHBBE5DDNPQNFAFNCOYLDIFKCKFLN4GZOOAEHLF6OR3CQSTELRCL6E), read 15 Nov 2026 ~11:05 AM MST (signed-in account): **Algorand is not supported** ([`45KKMHBB…`](https://allo.info/account/45KKMHBBE5DDNPQNFAFNCOYLDIFKCKFLN4GZOOAEHLF6OR3CQSTELRCL6E) returns "Something went wrong / Couldn't load portfolio"; [`DI6YXMONC7…`](https://allo.info/account/DI6YXMONC7PFVCRXHFP4UQCV5UXUFWO3Z2QURBV2K3SQLHILW3CROQ7UOI) and [`GSRT2TB2…`](https://allo.info/account/GSRT2TB2TADJ2YCE4A6O2ZH6TPFN3J2ACN5YOHT42MZKOO6LF4RFGAVSMQ) not opened for the same reason). Open item #3 stays open
- [Unverified] HesabPay and x402 figures; Flow Traders; FIFA migration; founder; the end of structured selling

## 🔗 Evidence trail

*Strongest findings first. Each link opens the primary record (block explorer) or the label source (Arkham) for the claim, so any number can be checked by hand.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| 🔴 Pump-day sale 1 Jun 2026: 3M ALGO selling wallet → `45KKMHBB…` (+17.6% 5-day) | [tx MAZ5LSZ2…](https://allo.info/tx/MAZ5LSZ26DJI26HCYEUM63YWG4A4JLA7ETOHQJQ3IU6GUKA7GFFA) · [`44GWRTQG…`](https://allo.info/account/44GWRTQGSAYUJJCQ3GFINYKZXMBDVKCF75VMCXKORN7ZJ6BKPNG2RMGH7E) | A | 15 Nov 2026 ~6:50 AM MST |
| 🔴 5 Aug 2026: 10M in from Foundation `VAOTJJLJ…`, 5M out an hour later (+13.4%) | [in: tx 6LQLL6ZM…](https://allo.info/tx/6LQLL6ZMUAEKVK3BCC5XAOUUQUQOZZIWFJAOEVLHQJEZGTYV4EJQ) · [out: tx QBXLVQ6U…](https://allo.info/tx/QBXLVQ6UO4G3KTARLLMZNBP42C5CFHJNQCS3LEYX7XI3LWQCLZOQ) · [`VAOTJJLJ…`](https://allo.info/account/VAOTJJLJP54QIKGCCFNJZVNHXXFZUZ3AAXCVGX5LRDQXQOUZRWBFBASUDQ) | A | 15 Nov 2026 ~6:50 AM MST |
| 🔴 24 Aug 2026: 3M ALGO (+20.6%), last sale on-chain | [tx AZORFFIX…](https://allo.info/tx/AZORFFIXMWMNWGGLD2GO6QAUYTI2J2UCSTJBTQ4UCSMFUBYZMOTQ) | A | 15 Nov 2026 ~6:50 AM MST |
| `45KKMHBB…` sent 112.9M ALGO onward (11.5M on pump days) | [Allo](https://allo.info/account/45KKMHBBE5DDNPQNFAFNCOYLDIFKCKFLN4GZOOAEHLF6OR3CQSTELRCL6E) · [indexer txs](https://mainnet-idx.algonode.cloud/v2/accounts/45KKMHBBE5DDNPQNFAFNCOYLDIFKCKFLN4GZOOAEHLF6OR3CQSTELRCL6E/transactions?limit=100) · [Arkham check (Algorand unsupported)](https://intel.arkm.com/explorer/address/45KKMHBBE5DDNPQNFAFNCOYLDIFKCKFLN4GZOOAEHLF6OR3CQSTELRCL6E) | A | 15 Nov 2026 ~6:50–11:05 AM MST |
| Main destinations: `DI6YXMONC7…` 51.7M · `S6VQ2RAB…` 31.9M · `GSRT2TB2…` 19.6M | [`DI6YXMONC7…`](https://allo.info/account/DI6YXMONC7PFVCRXHFP4UQCV5UXUFWO3Z2QURBV2K3SQLHILW3CROQ7UOI) · [`S6VQ2RAB…`](https://allo.info/account/S6VQ2RABLUOAXZ2MUFQXKDYLPVIYDO4C72ZBY763CL534MCN5RLZASSEEI) · [`GSRT2TB2…`](https://allo.info/account/GSRT2TB2TADJ2YCE4A6O2ZH6TPFN3J2ACN5YOHT42MZKOO6LF4RFGAVSMQ) | A flow / owner unverified | 15 Nov 2026 ~6:50 AM MST |
| `45KKMHBB…` also fed by treasury accounts | [`B223SVF4…`](https://allo.info/account/B223SVF452UWAMMLNIHIUAPHYPX5J3HLVJF6MNOHUJE2NWJBG7C66JILGE) · [`2TZAMEZZ…`](https://allo.info/account/2TZAMEZZDWFY37QV66HXWQIYWYJIZKE2KP3QNPI2QHHKSMKUZEICNMMUFU) | A | 15 Nov 2026 ~6:50 AM MST |
| Foundation 19.6% of online stake; 879M ALGO across published accounts | [Foundation transparency + account list](https://algorand.co/algorand-foundation/transparency) · [ledger supply](https://mainnet-api.algonode.cloud/v2/ledger/supply) | A | 15 Nov 2026 ~6:50 AM MST |
| Fee Sink 11.58M ALGO | [`Y76M3M…L226CA`](https://allo.info/account/Y76M3MSY6DKBRHBL7C3NNDXGS5IIMQVQVUAB6MP4XEMMGVF2QWNPL226CA) | A | 15 Nov 2026 ~6:50 AM MST |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Has structured selling ended?** | (a) Q3 2026 transparency report on [algorand.co/algorand-foundation/transparency](https://algorand.co/algorand-foundation/transparency), "Structured selling" section. (b) Email the CFO at the "ask the CFO" address printed in every report. (c) Keep watching `37VPAD3C…` and [`44GWRTQG…`](https://allo.info/account/44GWRTQGSAYUJJCQ3GFINYKZXMBDVKCF75VMCXKORN7ZJ6BKPNG2RMGH7E) on the AlgoNode indexer (`/v2/accounts/{addr}/transactions`) | Free |
| 2 | **~157M ALGO gap** between the 30 Jun report (1,036M) and today's published-account total (878.9M) | Compare the Q3 report's "Foundation holdings" line and reconciliation table with a live sum. Also sum the **legacy Foundation accounts** list linked on the transparency page, which this pass did not include | Free |
| 3 | **Who is [`45KKMHBB…`](https://allo.info/account/45KKMHBBE5DDNPQNFAFNCOYLDIFKCKFLN4GZOOAEHLF6OR3CQSTELRCL6E), and who are [`DI6YXMONC7…`](https://allo.info/account/DI6YXMONC7PFVCRXHFP4UQCV5UXUFWO3Z2QURBV2K3SQLHILW3CROQ7UOI), [`S6VQ2RAB…`](https://allo.info/account/S6VQ2RABLUOAXZ2MUFQXKDYLPVIYDO4C72ZBY763CL534MCN5RLZASSEEI), [`GSRT2TB2…`](https://allo.info/account/GSRT2TB2TADJ2YCE4A6O2ZH6TPFN3J2ACN5YOHT42MZKOO6LF4RFGAVSMQ)?** (where the sold ALGO goes) | **Arkham checked 15 Nov 2026: Algorand not supported, so Arkham cannot label these; stays open.** Ask the Foundation which custodian or OTC desk receives structured-selling transfers. Check Pera Explorer / Allo.info name tags. Nansen may label some Algorand exchange wallets (paid) | Free ask · Nansen paid |
| 4 | **Did Q1 sales match transfers?** (27M moved Jan–Feb vs 24M reported sold) | Q1 report reconciliation vs indexer. Ask the CFO whether the 3M difference was held over or sold in Q2 | Free |
| 5 | **CTO successor after Martins' 9 Oct 2026 resignation** | Foundation announcement or the next transparency report | Free |
| 5 | **Real fee revenue** (DefiLlama $6.5k/yr vs our ≤$23k/yr estimate) | Sum the `fee` field over all transactions for 30 days from the indexer (`/v2/transactions?min-round=…&max-round=…`, paginated), or run a Conduit / indexer export | Free but slow (~25M txs a month); a self-hosted indexer is faster |
| 6 | **Falcon-1024 / Algorand 5.0 dates and usage** | `go-algorand` v5.0.x release notes on GitHub, plus Algorand's own blog post on Algorand 5.0 | Free |
| 7 | **HesabPay volume, x402 settlements, Flow Traders** | HesabPay's own disclosures; GoPlausible x402 facilitator stats; Flow Traders press release on PR Newswire; on-chain, the USDC (ASA 31566704) transfer volume to known HesabPay accounts if published | Free; HesabPay volume may need a request |
| 8 | **Founder and team roles** | algorand.co team / leadership page; Delaware Division of Corporations entity search for the Foundation's US entity (officers are not listed there; the name and file number are) | Free |
| 9 | **Enforcement or court records** | PACER search for "Algorand Foundation" / "Algorand Inc." (paid, $0.10 a page); Singapore court records for the legacy entity | PACER small fee |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
