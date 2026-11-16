---
ticker: CRO
name: Cronos (Crypto.com)
chain: cronos-pos (native) + cronos evm + ethereum (ERC-20)
contract: "Native denom basecro on Cronos POS; ERC-20 0xa0b73e1ff0b80914ab6fe0444e65848c4c34450b on Ethereum"
overall_score: 3.7
overall_verdict: FAIL
section_scores:
  revenue: 2
  foundation_team: 5
  insider_holdings: 2
  selling_behavior: 4
  tokenomics_supply: 2
  liquidity_market: 4
  product_development: 6
  adoption_customers: 4
  security_audits: 6
  regulatory: 6
  catalysts: 4
gates_failed: [revenue]
red_lines:
  one_hop_sale_status: none_found
  hack_exploit: "none found at chain level (the Jan 2022 incident was at the Crypto.com exchange, not the chain)"
  treasury_to_exchange_during_pump: "no: 2.5B reserve-vested CRO (~$307M) went to a memo-based exchange hot wallet on 23 Sep 2025, 23 Feb, 30 Apr and 7-8 Oct 2026, none of them pump days"
  treasury_funded_wallet_to_exchange_during_pump: "no (same flows, all on down days)"
  unenforced_lockups: "no for the reserve itself (native PeriodicVestingAccount); yes after vesting: released CRO sits in plain accounts"
  mint_path_live: "yes: 70B burned CRO were re-minted in Mar 2025; validator inflation continues"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "Chain fees are a rounding error and the perks belong to the company, not the token."
pump_day_price_source: "KuCoin CRO-USDT daily closes"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions: []
price_usd: 0.04283
price_source: "CoinGecko, 16 Nov 2026 6:51 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### CRO · Overall grade **3.7 / 10 · ❌ FAIL**

**Summary:** CRO is the token of Crypto.com's Cronos chains. The company behind it is large and heavily licensed (MiCA CASP, US broker-dealer, two US CRO ETF filings pending), and the chain code is active. The token is a different story. In March 2025 a governance vote **re-minted the 70B CRO burned in 2021** into a Crypto.com-run "Strategic Reserve", which releases **1.167B CRO a month until ~2030**. Issuer-controlled accounts now hold about two-thirds of all CRO. The chain earns ~$136k a year in fees and holders get none of it. The price is −62.6% over a year. No pump-day selling was found, but 2.5B reserve CRO (~$307M) has already been moved to an exchange hot wallet without per-transfer disclosure. Revenue fails its gate.

**🚨 Top warning:** The re-minted reserve, PeriodicVestingAccount [`cro198pr…l7f4h`](https://cronos-pos.org/explorer/account/cro198pra975lcj526974r80fflr6retphnl3l7f4h) (original vesting 70,000,000,000 CRO, start 18 Mar 2025, 60 monthly periods), has released a net **22.17B CRO** so far and still holds 47.83B. The released coins go to three successive "unlock" accounts ([`cro1jejj…`](https://cronos-pos.org/explorer/account/cro1jejjqrmtmjm22hskcuqxwnfszpnhawpvl02gqe), [`cro1dkg7…`](https://cronos-pos.org/explorer/account/cro1dkg74ac85n65drd8zcerzaedrl83pth63rcq45), [`cro1h9ql…`](https://cronos-pos.org/explorer/account/cro1h9ql6gjr9zlu3t8zvjs47hzeylexhjjm9w9e2v)), which hold 19.6B between them. **2.5B has gone on to [`cro1w2kv…`](https://cronos-pos.org/explorer/account/cro1w2kvwrzp23aq54n3amwav4yy4a9ahq2kz2wtmj)**, a memo-based exchange hot wallet (980k+ transactions, deposits require a memo; very likely Crypto.com's own [Tier B]). That was 1.0B on 23 Sep 2025 via a one-day relay (≈ $205M; [relay in](https://cronos-pos.org/explorer/tx/61D7E742600578BB0EBCF413531A234F265CBAD4F97D868C653310F015375C49), [to exchange](https://cronos-pos.org/explorer/tx/8966AD09274BEB68506C7134EC2EB3588E178C232263DD4B9C6D27CC35988563)), then 500M each on 23 Feb, 30 Apr and 7–8 Oct 2026 via relay [`cro150mq…`](https://cronos-pos.org/explorer/account/cro150mqfrdg4nukqrnmglst84jamqkmmru5cpddus) ([Feb](https://cronos-pos.org/explorer/tx/2529A12142156C90DD0571DE4B805C8D32B5F499B17AA0C20DA960DF875F1C67), [Apr](https://cronos-pos.org/explorer/tx/A781A209D12D07F5F6E21AFC5C0FF4D85A6F11A99B05B1B95EB98709F14B3E71), [Oct](https://cronos-pos.org/explorer/tx/7FD4B525FE8C031B01112AF68E5167014666FB6D206CD6CFBC55E682919A434F)). **None of these days was a pump day** (5-day changes −13.3%, −5.0%, −2.2%, −9.3%), so the Selling gate holds. But the reserve was sold to voters as ETF seeding and US/AI ecosystem funding, and these exchange moves have no matching announcement. **Second warning:** supply. 70B coins came back from the dead, and 1.167B more vest every ~30.4 days (≈ $50M a month at today's price, about 2.2% of the float each month) until ~Mar 2030. Every transfer is in the 🔗 Evidence trail below.

**Sections passed: 3 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 2/10 | ❌ FAIL |
| 🏛️ Foundation & team | 5/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 2/10 | ❌ FAIL |
| 📉 Selling behavior | 4/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 2/10 | ❌ FAIL |
| 💧 Liquidity & market | 4/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 6/10 | ✅ PASS |
| 🤝 Adoption & customers | 4/10 | ❌ FAIL |
| 🛡️ Security & audits | 6/10 | ✅ PASS |
| ⚖️ Regulatory | 6/10 | ✅ PASS |
| 📅 Catalysts & calendar | 4/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 CRO · Cronos · 3.7 / 10 · ❌ FAIL

> **One line:** A licensed exchange's house token whose 2021 burn was reversed, now vesting a re-minted 70B back to its issuer.

**Identity:** CRO = Cronos (formerly Crypto.org Coin), cronos.org, issued by the Crypto.com group. CoinGecko `crypto-com-chain`, symbol CRO. Native coin of Cronos POS (`basecro`, 8 decimals) and Cronos EVM; ERC-20 [`0xa0b7…450b`](https://etherscan.io/token/0xa0b73e1ff0b80914ab6fe0444e65848c4c34450b) on Ethereum. Not to be confused with other "CRO" tickers. Matches the pipeline row (CRO, Cronos).

| 📊 Market (CoinGecko, 16 Nov 2026 6:51 AM MST) | 🔗 On-chain (Cronos POS REST, 16 Nov 2026) |
|---|---|
| **Price** $0.04283 | **Total supply** 99.04B (max 100B) after the 2025 re-mint |
| **24h / 7d / 30d / 1y** 🔴 −3.1% / −11.7% / −25.4% / −62.6% | **Reserve account** 47.83B still vesting |
| **Market cap** $2.22B · **FDV** $4.24B | **Released reserve CRO still in unlock accounts** 19.6B |
| **24h volume** $5.48M (CoinUp.io, Crypto.com Exchange, OKX, Upbit) | **Holders' revenue** $0 (DefiLlama) |
| **ATH** $0.8915 (23 Nov 2021) · now −95.2% | **Reserve → exchange hot wallet** 2.5B (~$307M) |
| **Pump days, last 365** 20 (KuCoin closes; CoinGecko 22) | **Circulating** 51.95B (52%) |

---

## 💰 Revenue — Does it make money? · 2/10 · ❌ FAIL

| Metric | Value | Source |
|---|---:|---|
| Cronos chain fees, 30d / 1y | $13,639 / $135,897 | [Tier A] [DefiLlama Cronos](https://defillama.com/chain/cronos) (16 Nov 2026) |
| Revenue to CRO holders | **$0** | same |
| What holders get | Staking rewards paid from inflation; Crypto.com app and card perks (off-chain, at the company's discretion) | [Tier A] [cronos.org](https://cronos.org/) |

**What it means:** The chain's fees are a rounding error against a $2.2B market cap, and the perks belong to the company, not the token. Score **2**, which **trips the Revenue gate**.

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** Chain fees are a rounding error and the perks belong to the company, not the token.

## 🏛️ Foundation & team — Who is in charge? · 5/10 · ❌ FAIL

| Item | Finding | Source |
|---|---|---|
| Issuer | Crypto.com group (Foris DAX entities); Cronos Labs runs the chains | [Tier A] [Crypto.com licences](https://crypto.com/en/licenses) |
| Re-mint governance | Proposal #29 on Cronos POS, voting 3–17 Mar 2025; reserve "subject to a 5-year lockup", "not intended to be delegated" | [Tier A] [proposal discussion](https://github.com/crypto-org-chain/chain-main/discussions/1124) · [Cronos blog](https://blog.cronos.com/p/the-new-golden-age-for-cronos) |
| Reserve address | Not named in the proposal ("cro1…"); identified on-chain as account #0, a PeriodicVestingAccount with 70B original vesting | [Tier A] REST `auth/accounts` |
| Use of funds | "Seeding the $CRO ETF", US initiatives, AI grants. No per-transfer reporting found | [Tier A] proposal |

**What it means:** A heavily regulated company, but the token's biggest decisions are made and executed by the issuer with little on-chain reporting. Score **5**.

## 🪙 Foundation / team holdings — How many coins do they hold? · 2/10 · ❌ FAIL

| Account | Type | CRO now | Note |
|---|---|---:|---|
| Strategic Reserve [`cro198pr…`](https://cronos-pos.org/explorer/account/cro198pra975lcj526974r80fflr6retphnl3l7f4h) | PeriodicVestingAccount (#0) | 47,833,333,334 | Not delegated; 80 sends so far |
| Unlock account 1 [`cro1jejj…`](https://cronos-pos.org/explorer/account/cro1jejjqrmtmjm22hskcuqxwnfszpnhawpvl02gqe) | Plain account | 5,833,333,332 | Took Jun–Aug 2025 releases (6.33B) |
| Unlock account 2 [`cro1dkg7…`](https://cronos-pos.org/explorer/account/cro1dkg74ac85n65drd8zcerzaedrl83pth63rcq45) | Plain account | ~0 | Took Sep 2025 – Jan 2026 (5.83B); passed 4.83B to account 3 on 13 Feb 2026 ([tx](https://cronos-pos.org/explorer/tx/4896AAC621B8F481B2305861DC2F8031D188376361B63C8F39D16D944F4DD653)) and 1.0B toward the exchange |
| Unlock account 3 [`cro1h9ql…`](https://cronos-pos.org/explorer/account/cro1h9ql6gjr9zlu3t8zvjs47hzeylexhjjm9w9e2v) | Plain account | 13,783,333,315 | Takes releases since Feb 2026, latest 21 Oct 2026 ([tx](https://cronos-pos.org/explorer/tx/B8B16FBE40C62749D3D4B58D7B3691912F183EB696EAED86E45BFC9DEC5C0FA6)) |

- Issuer-controlled on Cronos POS alone: **67.45B CRO, about 68% of total supply**, before counting Crypto.com's exchange and Ethereum cold wallets.

**What it means:** One company controls most of the supply, and once released the coins sit in ordinary accounts. Score **2**.

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL

Pump test uses KuCoin CRO-USDT daily closes (from Oct 2020). Transfers are Tier A (Cronos POS REST `cosmos/tx/v1beta1/txs`). The exchange label is Tier B (memo-style deposits, 980k+ txs).

| Day (UTC) | Route | CRO | 5-day change | Pump? |
|---|---|---:|---:|---|
| 23 Sep 2025 | Unlock 2 → relay [`cro1v274…`](https://cronos-pos.org/explorer/account/cro1v274vlzm6l6y3lf9w4ggdu4m2nmkc0d9r72ljj) ([tx](https://cronos-pos.org/explorer/tx/61D7E742600578BB0EBCF413531A234F265CBAD4F97D868C653310F015375C49)) → exchange hot wallet in 5 × 200M within ~20 minutes ([tx](https://cronos-pos.org/explorer/tx/8966AD09274BEB68506C7134EC2EB3588E178C232263DD4B9C6D27CC35988563)) | 1,000,000,000 | −13.3% | No |
| 20 → 23 Feb 2026 | Unlock 3 → relay `cro150mq` ([tx](https://cronos-pos.org/explorer/tx/265C292F9AF0E288712563050B7ACC0DD998BA2C5AD05DEDA69E5DC8F9C67756)) → exchange ([tx](https://cronos-pos.org/explorer/tx/2529A12142156C90DD0571DE4B805C8D32B5F499B17AA0C20DA960DF875F1C67)) | 500,000,000 | −5.0% | No |
| 30 Apr 2026 | Same route, same day ([tx](https://cronos-pos.org/explorer/tx/A781A209D12D07F5F6E21AFC5C0FF4D85A6F11A99B05B1B95EB98709F14B3E71)) | 500,000,000 | −2.2% | No |
| 13 Sep → 7–8 Oct 2026 | Same route ([in](https://cronos-pos.org/explorer/tx/94412C8BB74055F4F10FE56FE0773A613677BE4067C0611A2CF47A44997836FA), [out](https://cronos-pos.org/explorer/tx/7FD4B525FE8C031B01112AF68E5167014666FB6D206CD6CFBC55E682919A434F)) | 500,000,000 | −5.3%, −9.3% | No |

- 2.5B CRO ≈ **$307M** at each day's close. All on down days, but none matches a public announcement found this pass.
- 50M went from unlock 3 to [`cro1zgd7…`](https://cronos-pos.org/explorer/account/cro1zgd7xapjg5lv3fjp9gf70lt9utejr5xqe7dywf) and on to [`cro1ag7q…`](https://cronos-pos.org/explorer/account/cro1ag7qj65w7882kkn8nl7hnfvfqlemxwamd5g2pr) (4.2B CRO, claims "tier rewards" all day: a Crypto.com rewards account [Unverified]).
- Ethereum ERC-20 and Cronos EVM flows were not traced this pass. Arkham ([Tier B] Arkham, read 16 Nov 2026 (signed-in account)) labels the ERC-20 contract [`0xa0b7…`](https://intel.arkm.com/explorer/address/0xa0b73e1ff0b80914ab6fe0444e65848c4c34450b) **Crypto.com: Cronos Token (CRO)**. It is the token contract, not a cold wallet, and shows only small stray deposits. Arkham does not support Cronos POS, so the reserve's destination `cro1w2kv…` cannot be checked there. It stays *likely* a Crypto.com exchange hot wallet [Unverified].

**What it means:** No pump-day pattern, so the gate holds. But very large issuer transfers to an exchange wallet with no disclosure keep this a fail. Score **4**.

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from KuCoin CRO-USDT daily closes.

## 📊 Tokenomics & supply · 2/10 · ❌ FAIL

- 2021: 70B CRO burned. 2025: the same 70B re-minted to the reserve, "bringing the total supply back to 100 Billion" ([Cronos blog](https://blog.cronos.com/p/the-new-golden-age-for-cronos), Tier A).
- Vesting: 60 periods of 1,166,666,666.67 CRO, each ~30.4 days, start 18 Mar 2025, end ~17 Mar 2030 (read from the account itself, Tier A). Plus validator inflation.
- FDV is 1.9× the market cap.

## 💧 Liquidity & market · 4/10 · ❌ FAIL

- CoinGecko shows only $5.48M of 24h volume for a $2.22B coin. The biggest venues are CoinUp.io ($4.64M), Crypto.com Exchange USD ($1.11M), bitcastle, BTCC and OKX. The issuer's own exchange is a top venue.
- −95% from ATH, −62.6% over a year.

## 🧑‍💻 Product & development · 6/10 · ✅ PASS

- Cronos EVM and Cronos POS are live. Repo `crypto-org-chain/cronos` last commit 12 Nov 2026 ([commit](https://github.com/crypto-org-chain/cronos/commit/0801cdef03b15788a81698cef368a44a6f60c031)).

## 🤝 Adoption & customers · 4/10 · ❌ FAIL

- Large Crypto.com app user base, but on-chain fee income is ~$136k a year (DefiLlama), which points to light real use of the chains.

## 🛡️ Security & audits · 6/10 · ✅ PASS

- No chain-level exploit found. The Jan 2022 incident hit the Crypto.com exchange, not the Cronos chains [Unverified this pass]. Validator set and upgrades are issuer-led.

## ⚖️ Regulatory · 6/10 · ✅ PASS

- Crypto.com: MiCA CASP (Malta, passported across the EEA since Feb 2025), US broker-dealer, DCM/DCO and more ([licences](https://crypto.com/en/licenses), [MiCA notice](https://crypto.com/en/company-news/mica-change-in-license), Tier A).
- US CRO ETFs: Canary Staked CRO ETF (S-1 filed 30 May 2025; latest amendment 8 May 2026) and 21Shares Cronos ETF (filed 13 Mar 2026); none effective ([Crypto.com news](https://crypto.com/en/company-news/canary-capital-submits-s1-registration-for-cro-spot-etf) · [tracker](https://cryptoetf.today/en/cronos-etf), Tier A + B).

## 📅 Catalysts & calendar · 4/10 · ❌ FAIL

| Date | Event |
|---|---|
| Every ~30.4 days | 1.167B CRO vests from the reserve (next around mid/late Nov 2026) |
| No set date | SEC action on the Canary and 21Shares CRO ETFs; a third, staking-based "Cronos Yield Maximizer" ETF was reported filed in Feb 2026 [Unverified] ([CoinDesk](https://www.coindesk.com/markets/2026/02/13/trump-linked-truth-social-seeks-sec-approval-for-two-crypto-etfs), Tier B) |
| ~Mar 2030 | Reserve vesting ends |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found at chain level |
| Treasury → exchange during a pump | 🟢 Not found: 2.5B moved, all on down days |
| Unenforced lock-ups | 🟡 Reserve enforced by the chain; released CRO in plain accounts |
| Live mint path | 🔴 **Yes:** the 2025 re-mint of 70B burned CRO; inflation continues |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| Reserve-vested CRO → memo exchange hot wallet | Crypto.com reserve | Cronos POS REST + memo label | medium | no | Selling: large undisclosed issuer transfers (not on pump days) keep the score at 4 |

## 📚 Sources

- [Tier A] Methodology update 16 Nov 2026: no new Arkham lookups; the attribution table uses evidence already cited in this report.
- [Tier A] Cronos POS REST (`rest.mainnet.crypto.org`): `cosmos/auth/v1beta1/accounts`, `bank/v1beta1/balances`, `staking/v1beta1/delegations`, `tx/v1beta1/txs` for the reserve and seven downstream accounts; read 16 Nov 2026 MST
- [Tier A] [Proposal discussion #1124](https://github.com/crypto-org-chain/chain-main/discussions/1124) · [Cronos blog](https://blog.cronos.com/p/the-new-golden-age-for-cronos) · [Crypto.com licences](https://crypto.com/en/licenses) · [MiCA notice](https://crypto.com/en/company-news/mica-change-in-license) · [Canary S-1 notice](https://crypto.com/en/company-news/canary-capital-submits-s1-registration-for-cro-spot-etf) · [GitHub](https://github.com/crypto-org-chain/cronos)
- [Tier A] DefiLlama chain fees; CoinGecko `crypto-com-chain` (16 Nov 2026 6:51 AM MST); KuCoin CRO-USDT daily candles for every pump test
- [Tier B] [Cronos ETF tracker](https://cryptoetf.today/en/cronos-etf) · [Cronos POS explorer](https://cronos-pos.org/explorer/account/cro1w2kvwrzp23aq54n3amwav4yy4a9ahq2kz2wtmj) (exchange-style account, 980k+ txs) · community posts naming the reserve and unlock accounts
- [Tier B] Arkham, read 16 Nov 2026 (signed-in account): ERC-20 contract labelled Crypto.com: Cronos Token (CRO); Cronos POS is not an Arkham-supported network
- [Unverified] owner of `cro1w2kv` (very likely Crypto.com Exchange; not checkable on Arkham); purpose of each 500M–1B transfer; Ethereum and Cronos EVM treasury flows

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Reserve = PeriodicVestingAccount, 70B original vesting, 47.83B balance | [account](https://cronos-pos.org/explorer/account/cro198pra975lcj526974r80fflr6retphnl3l7f4h) | A | 16 Nov 2026 |
| First release to unlock account 1 (Jun 2025) | [tx](https://cronos-pos.org/explorer/tx/158E42AB9136C512D08B5288C917B644FB7F038337DBE5370F7BD2C0C28F2873) | A | 16 Nov 2026 |
| 1.0B to exchange hot wallet, 23 Sep 2025 | [relay](https://cronos-pos.org/explorer/tx/61D7E742600578BB0EBCF413531A234F265CBAD4F97D868C653310F015375C49) · [deposit](https://cronos-pos.org/explorer/tx/8966AD09274BEB68506C7134EC2EB3588E178C232263DD4B9C6D27CC35988563) | A + B label | 16 Nov 2026 |
| 1.5B to exchange hot wallet, 2026 | [Feb](https://cronos-pos.org/explorer/tx/2529A12142156C90DD0571DE4B805C8D32B5F499B17AA0C20DA960DF875F1C67) · [Apr](https://cronos-pos.org/explorer/tx/A781A209D12D07F5F6E21AFC5C0FF4D85A6F11A99B05B1B95EB98709F14B3E71) · [Oct](https://cronos-pos.org/explorer/tx/7FD4B525FE8C031B01112AF68E5167014666FB6D206CD6CFBC55E682919A434F) | A + B label | 16 Nov 2026 |
| Re-mint and 5-year vesting design | [proposal](https://github.com/crypto-org-chain/chain-main/discussions/1124) | A | 16 Nov 2026 |
| Fees ~$136k/yr; holder revenue $0 | [DefiLlama](https://defillama.com/chain/cronos) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Owner of `cro1w2kv`** | Arkham does not cover Cronos POS (16 Nov 2026). Ask Crypto.com / Cronos Labs to confirm it is the exchange hot wallet, and find the Ethereum CRO cold wallets via Etherscan holder labels | Free |
| 2 | **Purpose of the 2.5B** | Ask Cronos Labs to map each reserve transfer to a disclosed use (ETF seeding, treasury deals, grants) | Free |
| 3 | **EVM and Ethereum side** | Trace Crypto.com's Ethereum CRO wallets and the Cronos EVM bridge for exchange deposits on the 20 pump days | Free (Etherscan; Cronoscan key) |
| 4 | **ETF** | Watch EDGAR for the Canary and 21Shares S-1 amendments | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
