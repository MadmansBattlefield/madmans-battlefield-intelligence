---
ticker: LINK
name: Chainlink
chain: ethereum
contract: "0x514910771AF9Ca656af840dff83E8264EcF986CA"
overall_score: 7.1
overall_verdict: PASS
section_scores:
  revenue: 8
  foundation_team: 6
  insider_holdings: 4
  selling_behavior: 5
  tokenomics_supply: 6
  liquidity_market: 10
  product_development: 9
  adoption_customers: 8
  security_audits: 8
  regulatory: 8
  catalysts: 6
gates_failed: []
red_lines:
  one_hop_sale_status: none_found
  hack_exploit: none
  treasury_to_exchange_during_pump: not_found
  undisclosed_treasury_to_exchange_flow: recurring_quarterly
methodology_effective: 2026-11-16
revenue_reaches_holders: "yes"
revenue_mechanism: "Payment Abstraction converts on-chain and off-chain service revenue into LINK automatically through Chainlink Automation and a DEX, and deposits it in the on-chain Chainlink Reserve (431,900 LINK bought in 30 days) ([Chainlink](https://chain.link/blog/chainlink-reserve-strategic-link-reserve), [Payment Abstraction](https://chain.link/blog/payment-abstraction-svr-fee-conversion)). That is an automatic, executed buyback paid from revenue, so the test is yes. Caveat: the bought LINK is held in a timelocked reserve, not burned or paid out."
pump_day_price_source: "CoinGecko LINK daily closes, re-run 17 Nov 2026 with scripts/pump_day_test.py (25 of 360 days); midnight stamps labelled as the close of the prior UTC day; partial current-day tick dropped"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions:
  - address: "0x9b1c1752b6b6eaf62a8c491a8681b32c1f7ecde9"
    label: "Binance Deposit (Arkham) forwarding to Binance 14"
    confidence: high
    independent_corroboration: true
    basis: "Arkham + Etherscan tag + forwarding pattern"
price_usd: 9.19
price_source: "CoinGecko, 14 Nov 2026 9:08 AM MST"
last_updated: 2026-11-17
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### LINK · Overall grade **7.1 / 10 · ✅ PASS**

**Summary:** A real, fee-earning oracle network with clean token code, but its non-circulating treasury sends roughly 9–19M LINK to Binance a few times a year (58.85M in the last 12 months) without a formal announcement. None of those sends fell on a pump day.

**🚨 Top warning:** Chainlink's non-circulating treasury Safes keep feeding one **Binance deposit address** [`0x9b1c…cde9`](https://etherscan.io/address/0x9B1c1752B6B6eAF62a8c491A8681B32C1F7ecDE9): **58.85M LINK in the last 12 months** (253.8M since Aug 2022), with no formal announcement. Latest batch 9 Oct 2026, incl. 3.4M from Safe #17 ([in](https://etherscan.io/tx/0x2f03bf93b7c50c740a6a9ebdcb2182ae112ea3c14474559e189afa8aaed40836) → [Binance 14](https://etherscan.io/tx/0x595cc8d1b1156210b6ecdf9fe34adc45857091fa6894b3d2c876bd3aee4bdb8e)). Not pump-timed. Check: [deposit address on Etherscan](https://etherscan.io/address/0x9B1c1752B6B6eAF62a8c491A8681B32C1F7ecDE9) · [Arkham “Binance Deposit”](https://intel.arkm.com/explorer/address/0x9B1c1752B6B6eAF62a8c491A8681B32C1F7ecDE9) · [Safe #17 on Arkham (“Chainlink: Non-Circulating Supply”)](https://intel.arkm.com/explorer/address/0xa42d0a18b834f52e41beddeaa2940165db3da9a3).

**Sections passed: 8 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 8/10 | ✅ PASS |
| 🏛️ Foundation & team | 6/10 | ✅ PASS |
| 🪙 Foundation / team holdings | 4/10 | ❌ FAIL |
| 📉 Selling behavior | 5/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 6/10 | ✅ PASS |
| 💧 Liquidity & market | 10/10 | ✅ PASS |
| 🧑‍💻 Product & development | 9/10 | ✅ PASS |
| 🤝 Adoption & customers | 8/10 | ✅ PASS |
| 🛡️ Security & audits | 8/10 | ✅ PASS |
| ⚖️ Regulatory | 8/10 | ✅ PASS |
| 📅 Catalysts & calendar | 6/10 | ✅ PASS |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 LINK · Chainlink · 7.1 / 10 · ✅ PASS

> **One line:** A real, fee-earning oracle network with clean token code, but its non-circulating treasury sends roughly 9–19M LINK to Binance a few times a year (58.85M in the last 12 months) without a formal announcement. None of those sends fell on a pump day.

| 📊 Market (CoinGecko, 14 Nov 2026 9:08 AM MST) | 🔗 On-chain (Ethereum, 10 Oct / 3 Nov 2026) |
|---|---|
| **Price** $9.19 | **Token** [`0x5149…86CA`](https://etherscan.io/address/0x514910771AF9Ca656af840dff83E8264EcF986CA) "LinkToken" ERC-677, Solidity 0.4.16 |
| **24h / 7d / 30d** 🔴 −7.4% / −15.1% / −24.9% | **Supply** 1,000,000,000 fixed · no owner, mint, pause, blacklist, upgrade |
| **Market cap** $7.05B · **FDV** $9.19B | **Circulating (CoinGecko)** 766.85M → ~233.15M non-circulating |
| **24h volume** $246.3M | **Holders** ~1,007,408 (Blockscout, 10 Oct) |
| **ATH** $52.70 (9 May 2021) · now −83% | **Community staking pool** [`0xBc10…DB5e`](https://etherscan.io/address/0xBc10f2E862ED4502144c7d632a3459F49DFCDB5e) 40,875,544 (4.09%) |

---

## 💰 Revenue — Does it make money? · 8/10 · ✅ PASS

| Metric | Value | Source |
|---|---:|---|
| 30-day fees | $5,516,481 | [Tier A] DefiLlama `chainlink-requests`, `chainlink-staking` (pulled 13 Nov 2026) |
| 30-day revenue | $5,340,836 | [Tier A] DefiLlama |
| All-time fees | $82,853,166 | [Tier A] DefiLlama |
| All-time revenue | $75,513,614 | [Tier A] DefiLlama |
| Chainlink Reserve buys | 431,900 LINK in 30 days, funded by service revenue | [Tier A] treasury pass |
| Reserve size | >6M LINK (28 Sep 2026) | [Unverified] news only; contract balance not read |

**What it means:** Yes, it makes money, and some of it is used to buy LINK. Annualised revenue is ~$65M on a $7B cap.

- **Reaches holders (binary test, 16 Nov 2026 rules): Yes.** Payment Abstraction converts on-chain and off-chain service revenue into LINK automatically through Chainlink Automation and a DEX, and deposits it in the on-chain Chainlink Reserve (431,900 LINK bought in 30 days) ([Chainlink](https://chain.link/blog/chainlink-reserve-strategic-link-reserve), [Payment Abstraction](https://chain.link/blog/payment-abstraction-svr-fee-conversion)). That is an automatic, executed buyback paid from revenue, so the test is yes. Caveat: the bought LINK is held in a timelocked reserve, not burned or paid out.

## 🏛️ Foundation & team — Who is in charge? · 6/10 · ✅ PASS

| Item | Finding | Source |
|---|---|---|
| Sergey Nazarov | Co-founder; CEO of Chainlink Labs. Verified commits | [Tier A] GitHub `smartcontractkit` |
| Steve Ellis | Co-founder; CTO (commonly stated). Commits verified by name | [Tier A] commits · title [Unverified] |
| Chainlink Foundation | Entity, directors and jurisdiction **not checked** this pass | [Unverified] |
| Non-circulating Safes | Known on-chain ("Noncirculating Supply" Safe multisigs, e.g. #17 [`0xa42d0a18…9a3`](https://etherscan.io/address/0xa42d0a18b834f52e41beddeaa2940165db3da9a3) · [Arkham](https://intel.arkm.com/explorer/address/0xa42d0a18b834f52e41beddeaa2940165db3da9a3)), **no official address list**. Arkham files `0xa42d…` as **"Chainlink: Non-Circulating Supply"** inside its "Chainlink" entity (5.5K addresses, ~$3.19B, 286.6M LINK). Etherscan + Arkham = two Tier B labels, so these Safes are **verified Chainlink treasury** | [Tier A] chain · labels Etherscan · [Tier B] Arkham, read 15 Nov 2026 ~11:00 AM MST (signed-in account) |

**What it means:** The builders are known and active. The treasury Safes are now confirmed as Chainlink's by two label sources, but which legal entity (Labs or Foundation) controls them is still an open question.

## 🪙 Foundation / team holdings — How many coins do they hold? · 4/10 · ❌ FAIL

| Bucket | LINK | % of supply | Notes |
|---|---:|---:|---|
| Non-circulating (1B − CoinGecko circulating) | ~233,150,030 | ~23.3% | Held in Safe multisigs; not vested on-chain |
| Arkham "Chainlink" entity (all labelled addresses) | 286.6M LINK (~$2.64B), plus ~$285M in syrupUSDC/USDT and other tokens | ~28.7% | One Tier B source; likely includes contracts beyond the treasury Safes (e.g. Reserve, staking-related), so it is not a clean treasury figure [Unverified] |
| Community staking pool | 40,875,544 | 4.09% | User stake, not treasury |
| Release to Binance | 58.85M in the last 12 months (9.2M–18.4M per batch) | ~5.9% a year | Discretionary |

**What it means:** About a quarter of supply is in treasury Safes that can move at any time; there is no on-chain lock.

## 📉 Selling behavior — Do insiders sell into pumps? · 5/10 · ❌ FAIL

| Window (UTC) | Route | Amount to Binance 14 | LINK 5-day change before send | Pump? |
|---|---|---:|---:|---|
| 9 Oct 2026 19:43–21:13 | Noncirculating Safes → [`0x9b1c1752…cde9`](https://etherscan.io/address/0x9B1c1752B6B6eAF62a8c491A8681B32C1F7ecDE9) ([Arkham](https://intel.arkm.com/explorer/address/0x9B1c1752B6B6eAF62a8c491A8681B32C1F7ecDE9); forwards in minutes) → Binance 14 [`0x28c6c062…1d60`](https://etherscan.io/address/0x28C6c06298d514Db089934071355E5743bf21d60). Txs: [3.4M in](https://etherscan.io/tx/0x2f03bf93b7c50c740a6a9ebdcb2182ae112ea3c14474559e189afa8aaed40836) · [3.4M → Binance](https://etherscan.io/tx/0x595cc8d1b1156210b6ecdf9fe34adc45857091fa6894b3d2c876bd3aee4bdb8e) · [4.5M → Binance](https://etherscan.io/tx/0x1d0f1263c828d4ff2a147c05ef27b96f6527a2a7f032e8cf1e02a4e82e459c4e) · [2.73M → Binance](https://etherscan.io/tx/0x3a38babee890d50904ad004c9b8dbe2002aa73b6bc791006f6358f276207a812) | **16,875,000** (+1,874,999 to Safe `0xd50f074e`) | −10.3% | ❌ No |
| 19 Jun 2026 19:17–21:13 | same route (5 Safes). Txs: [8.375M → Binance](https://etherscan.io/tx/0xef13c7c8b91afbed0995167813e98646cc99995eb3506215dd1420850550399e) · [4.0M → Binance](https://etherscan.io/tx/0x5fd73e5a2ef1303670ed15f91ca9bdc774470892f1eced9059901c938f9c04d5) | **18,375,000** (+2,624,999 to `0xd50f…`) | −2.9% | ❌ No |
| 3 Apr 2026 19:35–22:52 | same route (3 Safes). Txs: [9.775M → Binance](https://etherscan.io/tx/0x4dc3376c4d43e39db54ec36e2d34e18e522b0783e1231173b62f5302151fd89d) · [2.5M → Binance](https://etherscan.io/tx/0xd2b4c2c4a9e2208fda54e57fef07de1c59cf92b12d389439a0088951dd9e31e3) | **14,375,000** (+4,624,999 to `0xd50f…`) | +2.9% | ❌ No |
| 19 Dec 2025 20:11–20:30 | same route (2 Safes). Txs: [5.225M → Binance](https://etherscan.io/tx/0xd3916e84214f649df558feaeaf5a919eb974f0083e8d5645fd93b5a2c3729771) · [4.0M → Binance](https://etherscan.io/tx/0x3bd07fec96f7092c3c0b27a88e57e12c5f8fe0f39d7e2be933955adee8bb9972) | **9,225,000** (+2,024,999 to `0xd50f…`) | −5.7% | ❌ No |

- Example tx: [tx `0x2f03bf93b7c50c740a6a9ebdcb2182ae112ea3c14474559e189afa8aaed40836`](https://etherscan.io/tx/0x2f03bf93b7c50c740a6a9ebdcb2182ae112ea3c14474559e189afa8aaed40836) (3,399,999 from Safe #17 on 9 Oct, forwarded as [tx `0x595cc8d1b115…`](https://etherscan.io/tx/0x595cc8d1b1156210b6ecdf9fe34adc45857091fa6894b3d2c876bd3aee4bdb8e) seven minutes later).
- **Full history, now read in full (15 Nov):** `0x9b1c…` has forwarded **253.8M LINK to Binance 14 in 62 transfers since 26 Aug 2022** (first: [tx `0x540c7288…`](https://etherscan.io/tx/0x540c72883f4cb0e14042c450e6e9297108893655493f4e10120625311aa40a2c); full list on [Etherscan](https://etherscan.io/address/0x9B1c1752B6B6eAF62a8c491A8681B32C1F7ecDE9)), usually within minutes of arriving (at most a few hours), and has never sent LINK anywhere else. The last 12 months are the four rows above: **58.85M**.
- **Labels, now verified:** Arkham labels `0x9b1c…` "Binance Deposit" and `0x28c6…` "Binance: Hot Wallet"; Etherscan tags `0x28c6…` "Binance 14". Two independent Tier B labels plus the [Tier A] forwarding pattern confirm a **Binance deposit address** credited to one Binance account ([Tier B] Arkham, read 15 Nov 2026 ~11:00 AM MST (signed-in account)).
- **[`0xd50f074e…`](https://etherscan.io/address/0xd50f074ec5c7997ce1daacb513ec194c480878af) (the Safe that gets a slice of each batch; [Arkham](https://intel.arkm.com/explorer/address/0xd50f074ec5c7997ce1daacb513ec194c480878af)):** Arkham shows no entity. On-chain it receives only from the non-circulating Safes and pays 499,999 or 607,499 LINK every few weeks to Safe [`0x7a28b8cf…`](https://etherscan.io/address/0x7a28b8cfeb73b45626f521de928d0dd2d25c14a3) (since Nov 2022). No exchange sends. That looks like an operating budget; purpose [Unverified].
- Pump test (re-run 17 Nov 2026, CoinGecko daily closes with the midnight-stamp convention): **25 of 360 days** were pump days, 16 Nov 2025 – 16 Nov 2026. Last pump day 29 Sep 2026 (+10.5%); peak 21 Aug 2026 (+27.8%). **None** of the four batches fell on a pump day (also none on the following day). Corrected 5-day moves: 19 Dec 2025 −5.7%, 3 Apr 2026 +2.9%, 19 Jun 2026 −2.9%, 9 Oct 2026 −10.3%.
- **Correction (15 Nov):** the October batch was **16,875,000** to Binance (plus 1,874,999 to `0xd50f…`, 18.75M in all), not 15.875M as this page said before. The press figure of 16.875M was right. The June and April rows were partial before; full totals are above. Whether Binance sold the LINK cannot be seen on-chain.

**What it means:** Not pump-timed, and the cadence is regular (four batches in 12 months, all on calm or falling days). Arkham now confirms the treasury and the Binance deposit. But it is still undisclosed treasury-to-exchange flow, about 59M LINK a year, so it does not pass (score unchanged at 5).

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from CoinGecko LINK daily closes, re-run 17 Nov 2026 with the midnight-stamp convention (25 of 360 days).

## 📊 Tokenomics & supply · 6/10 · ✅ PASS

- Fixed 1B, ERC-677, not upgradeable, no tax. Matches white paper v2.0 (15 Apr 2021).
- No burn claimed. Unlock pressure: 58.85M to Binance in the last 12 months (~7.7% of circulating a year), in batches of 9–19M.

## 💧 Liquidity & market · 10/10 · ✅ PASS

- $246.3M 24h volume; deep on every major CEX and DEX.

## 🧑‍💻 Product & development · 9/10 · ✅ PASS

- Live: Data Feeds, Data Streams, CCIP (GA 24 Apr 2024), Automation, VRF, Functions; Staking v0.2 (Nov 2023).
- GitHub `smartcontractkit`: 100 repos listed, **93 pushed in last 90 days**, last push 3 Nov 2026.

## 🤝 Adoption & customers · 8/10 · ✅ PASS

- Confirmed: Swift + UBS Asset Management pilot bridging tokenized assets to payment systems (Nov 2024).
- Partly: "Chainlink is Swift's contingency plan." Unverified: Chainlink + RedStone with Plume.

## 🛡️ Security & audits · 8/10 · ✅ PASS

- No LINK-token or Chainlink protocol hack on file (2025–2026). Remaining risk lives in oracle configs, CCIP lanes, staking and Reserve contracts.

## ⚖️ Regulatory · 8/10 · ✅ PASS

- **US:** SEC Release 33-11412 (issued 17 Mar 2026, effective 23 Mar 2026, joined by the CFTC) names **Chainlink (LINK)** as an example of a **digital commodity**, which is not a security ([Tier A] [govinfo](https://www.govinfo.gov/content/pkg/FR-2026-03-23/html/2026-05635.htm)). Peers named in the same list are scored 8 on this section.
- **Correction, 17 Nov 2026:** Regulatory **5 → 8** after this release was applied. Overall **6.9 → 7.1**. Still PASS.

## 📅 Catalysts & calendar · 6/10 · ✅ PASS

| Date | Event |
|---|---|
| ~Dec 2026 – Jan 2027 | Next treasury release window (last four: 19 Dec 2025, 3 Apr, 19 Jun, 9 Oct 2026) |
| Ongoing | Reserve buys from service revenue |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None |
| Treasury → exchange during a pump | 🟢 Not found (sends were off-pump) |
| Undisclosed treasury → exchange flow | 🟡 Recurring: 4 batches, 58.85M LINK in 12 months (Binance deposit confirmed by Arkham + Etherscan): [deposit address](https://etherscan.io/address/0x9B1c1752B6B6eAF62a8c491A8681B32C1F7ecDE9) · [Arkham label](https://intel.arkm.com/explorer/address/0x9B1c1752B6B6eAF62a8c491A8681B32C1F7ecDE9) · [9 Oct example](https://etherscan.io/tx/0x595cc8d1b1156210b6ecdf9fe34adc45857091fa6894b3d2c876bd3aee4bdb8e) |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| [0x9b1c…cde9](https://etherscan.io/address/0x9B1c1752B6B6eAF62a8c491A8681B32C1F7ecDE9) | Binance Deposit (Arkham) forwarding to Binance 14 | Arkham + Etherscan tag + forwarding pattern | high | yes | Selling: treasury batches to Binance, none on pump days |
| Chainlink non-circulating treasury Safes | Chainlink treasury | Arkham entity + supply disclosures | high | yes | Holdings: ~25% in liquid Safes |

## 📚 Sources

- [Tier A] Methodology update 16 Nov 2026: no new Arkham lookups; the attribution table uses evidence already cited in this report.
- [Tier A] Ethereum RPC and Blockscout; `eth_getLogs` Transfer trace, Oct 2026
- [Tier A] Etherscan v2 API `tokentx` (LINK) for `0x9b1c…`, `0xa42d…` and `0xd50f…`, full history, read 15 Nov 2026 ~11:20 AM MST
- [Tier B] Arkham, read 15 Nov 2026 ~11:00 AM MST (signed-in account): "Chainlink" entity; `0xa42d…` "Chainlink: Non-Circulating Supply"; `0x9b1c…` "Binance Deposit"; `0x28c6…` "Binance: Hot Wallet"; `0xd50f…` (no entity). Arkham shows relative ages only; dates above come from on-chain reads where amounts match. All-time exchange totals are Enterprise-locked
- [Tier B] Etherscan name tags "Binance 14" ([`0x28c6…`](https://etherscan.io/address/0x28C6c06298d514Db089934071355E5743bf21d60)) and "Noncirculating Supply Safe" ([`0xa42d…`](https://etherscan.io/address/0xa42d0a18b834f52e41beddeaa2940165db3da9a3))
- [Tier A] Explorer pages used (Etherscan): [`0x9b1c…`](https://etherscan.io/address/0x9B1c1752B6B6eAF62a8c491A8681B32C1F7ecDE9) · [`0xa42d…`](https://etherscan.io/address/0xa42d0a18b834f52e41beddeaa2940165db3da9a3) · [`0xd50f…`](https://etherscan.io/address/0xd50f074ec5c7997ce1daacb513ec194c480878af) · [`0x7a28…`](https://etherscan.io/address/0x7a28b8cfeb73b45626f521de928d0dd2d25c14a3) · [`Binance 14`](https://etherscan.io/address/0x28C6c06298d514Db089934071355E5743bf21d60) · token [`0x5149…`](https://etherscan.io/address/0x514910771AF9Ca656af840dff83E8264EcF986CA)
- [Tier B] Arkham address pages used: [0xa42d…](https://intel.arkm.com/explorer/address/0xa42d0a18b834f52e41beddeaa2940165db3da9a3) · [0x9b1c…](https://intel.arkm.com/explorer/address/0x9B1c1752B6B6eAF62a8c491A8681B32C1F7ecDE9) · [0x28c6…](https://intel.arkm.com/explorer/address/0x28C6c06298d514Db089934071355E5743bf21d60) · [0xd50f…](https://intel.arkm.com/explorer/address/0xd50f074ec5c7997ce1daacb513ec194c480878af)
- [Tier A] [docs.chain.link](https://docs.chain.link) · [white paper v2](https://research.chain.link/whitepaper-v2.pdf)
- [Tier A] DefiLlama fees/revenue, pulled 13 Nov 2026 4:22 AM MST
- [Tier A] CoinGecko `chainlink` price and 365-day daily closes, 14 Nov 2026
- [Tier A] GitHub `smartcontractkit`
- [Tier B] [PR Newswire, CCIP GA](https://www.prnewswire.com/news-releases/chainlink-announces-general-availability-for-ccip-302126061.html)
- [Unverified] Reserve balance >6M LINK; Foundation entity and signers; Steve Ellis title; purpose of `0xd50f…` → `0x7a28b8cf…` payments; Arkham's 286.6M entity total

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer) or the label source (Arkham) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| **Treasury → Binance deposit pattern:** non-circulating Safes → `0x9b1c…cde9` → Binance 14; 58.85M LINK in 12 months, 253.8M since Aug 2022 | [Etherscan (full history)](https://etherscan.io/address/0x9B1c1752B6B6eAF62a8c491A8681B32C1F7ecDE9) · [Arkham “Binance Deposit”](https://intel.arkm.com/explorer/address/0x9B1c1752B6B6eAF62a8c491A8681B32C1F7ecDE9) · [Binance 14 tag](https://etherscan.io/address/0x28C6c06298d514Db089934071355E5743bf21d60) · [Arkham “Binance: Hot Wallet”](https://intel.arkm.com/explorer/address/0x28C6c06298d514Db089934071355E5743bf21d60) | A pattern + 2× B | 15 Nov 2026 ~11:20 AM MST |
| 9 Oct 2026 batch: 16.875M to Binance (incl. 3,399,999 from Safe #17) | [3.4M in](https://etherscan.io/tx/0x2f03bf93b7c50c740a6a9ebdcb2182ae112ea3c14474559e189afa8aaed40836) · [3.4M → Binance](https://etherscan.io/tx/0x595cc8d1b1156210b6ecdf9fe34adc45857091fa6894b3d2c876bd3aee4bdb8e) · [4.5M → Binance](https://etherscan.io/tx/0x1d0f1263c828d4ff2a147c05ef27b96f6527a2a7f032e8cf1e02a4e82e459c4e) · [2.73M → Binance](https://etherscan.io/tx/0x3a38babee890d50904ad004c9b8dbe2002aa73b6bc791006f6358f276207a812) | A | 15 Nov 2026 |
| 19 Jun 2026 batch: 18.375M to Binance | [8.375M → Binance](https://etherscan.io/tx/0xef13c7c8b91afbed0995167813e98646cc99995eb3506215dd1420850550399e) · [4.0M → Binance](https://etherscan.io/tx/0x5fd73e5a2ef1303670ed15f91ca9bdc774470892f1eced9059901c938f9c04d5) | A | 15 Nov 2026 |
| 3 Apr 2026 batch: 14.375M to Binance | [9.775M → Binance](https://etherscan.io/tx/0x4dc3376c4d43e39db54ec36e2d34e18e522b0783e1231173b62f5302151fd89d) · [2.5M → Binance](https://etherscan.io/tx/0xd2b4c2c4a9e2208fda54e57fef07de1c59cf92b12d389439a0088951dd9e31e3) | A | 15 Nov 2026 |
| 19 Dec 2025 batch: 9.225M to Binance | [5.225M → Binance](https://etherscan.io/tx/0xd3916e84214f649df558feaeaf5a919eb974f0083e8d5645fd93b5a2c3729771) · [4.0M → Binance](https://etherscan.io/tx/0x3bd07fec96f7092c3c0b27a88e57e12c5f8fe0f39d7e2be933955adee8bb9972) | A | 15 Nov 2026 |
| Safe #17 `0xa42d…` is Chainlink treasury ("Chainlink: Non-Circulating Supply" + Etherscan tag) | [Etherscan](https://etherscan.io/address/0xa42d0a18b834f52e41beddeaa2940165db3da9a3) · [Arkham](https://intel.arkm.com/explorer/address/0xa42d0a18b834f52e41beddeaa2940165db3da9a3) | 2× B | 15 Nov 2026 |
| `0xd50f…` gets a slice of each batch and pays `0x7a28…` (no exchange sends) | [0xd50f… Etherscan](https://etherscan.io/address/0xd50f074ec5c7997ce1daacb513ec194c480878af) · [Arkham](https://intel.arkm.com/explorer/address/0xd50f074ec5c7997ce1daacb513ec194c480878af) · [0x7a28… Etherscan](https://etherscan.io/address/0x7a28b8cfeb73b45626f521de928d0dd2d25c14a3) | A | 15 Nov 2026 |
| Community staking pool 40,875,544 LINK | [Etherscan](https://etherscan.io/address/0xBc10f2E862ED4502144c7d632a3459F49DFCDB5e) | A | 10 Oct 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Did Chainlink disclose the 58.85M sent to Binance?** | Search Chainlink blog / X / transparency posts for the Dec 2025, Apr, Jun and Oct 2026 batches; ask Chainlink Labs what the Binance account is used for (node-operator rewards, OTC, sales) | Free |
| 2 | **Full list of non-circulating Safes and their balances** | Enumerate Etherscan "Noncirculating Supply Safe" tags and Arkham's "Chainlink: Non-Circulating Supply" addresses; sum `balanceOf` | Free (Arkham login) |
| 3 | **What `0xd50f…` → `0x7a28b8cf…` pays for** | Trace `0x7a28b8cf…` onward flows; ask Chainlink | Free |
| 4 | **Reserve balance (>6M LINK claimed)** | Read the Chainlink Reserve contract `balanceOf` | Free |
| 5 | **Regulatory status** | Look for licences / filings for Chainlink Labs and the Foundation | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
