---
ticker: PACT
name: PACT Protocol (Pact Foundation)
chain: aptos
contract: "0xc546cc2dd26d9e9a4516b4514288bedf1085259fcb106b84b6469337f527fb92"
overall_score: 2.9
overall_verdict: FAIL
section_scores:
  revenue: 3
  foundation_team: 4
  insider_holdings: 2
  selling_behavior: 0
  tokenomics_supply: 2
  liquidity_market: 2
  product_development: 5
  adoption_customers: 5
  security_audits: 4
  regulatory: 4
  catalysts: 5
gates_failed: [revenue, selling_behavior]
red_lines:
  hack_exploit: none found
  mint_path_live: "yes, uncapped: max supply in the Aptos asset is 2^128; Foundation 2-of-3 multisig is the token admin; 25B minted 23 Dec 2025 after a 6-voter Snapshot"
  team_wallet_to_exchange_during_pump: "yes: Foundation multisig released 3.44B PACT on 1 Oct 2026 (MST); 1.32B of it reached Gate deposit addresses within ~10 hours, on the 2 Oct 2026 (UTC) pump day (+11.1%)"
  one_hop_sale_status: proven
  undisclosed_reserve_releases: "yes: 3.44B (1 Oct 2026) and 6.25B (4–12 Nov 2026) out of the Foundation multisig; no announcement or vote found"
  freeze_blocklist: "enabled (admin can freeze wallets and blocklist addresses)"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "The buyback rule cannot be audited and bought tokens are locked, not burned or paid out."
pump_day_price_source: "the report's own daily-close series"
pump_day_disclosure_quality: silence
pump_day_undisclosed_penalty_applied: true
dual_review: not_run
attributions: []
price_usd: 0.00018056
price_source: "CoinGecko, 16 Nov 2026 5:46 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### PACT · Overall grade **2.9 / 10 · ❌ FAIL**

**Summary:** PACT is the governance token of an Aptos-based lending and payroll-credit protocol run by the Pact Foundation and Pact Labs (Tether led a $7M equity round in Pact Labs). The business is real, but the token earns nothing provable: the Foundation says fees fund buybacks, yet no buyback wallet is published. The Foundation's 2-of-3 multisig can mint without a cap (it minted 25B in Dec 2025), can freeze wallets, and has released 9.7B PACT since 1 Oct 2026 with no announcement found. **Part of the first release was on Gate within hours, on a pump day.** Trading is about $29K a day. Fails both hard gates.

**🚨 Top warning (red line):** the **Pact Foundation multisig** ([`0x36e7…9095`](https://explorer.aptoslabs.com/account/0x36e780c44f6e06c4678957bf3df239e394e42e4b03db01eb7c85ad226a879095?network=mainnet), 2-of-3, also the token admin) sent **3.44B PACT to five new wallets at 8:35 PM MST on 1 Oct 2026** ([e.g.](https://explorer.aptoslabs.com/txn/7449312283?network=mainnet)). Within ten hours, **1.32B of it was deposited at Gate** through two deposit addresses: [249.9M at 9:44 PM MST](https://explorer.aptoslabs.com/txn/7449993823?network=mainnet), then [341.9M](https://explorer.aptoslabs.com/txn/7455683932?network=mainnet) + [341.9M](https://explorer.aptoslabs.com/txn/7455692790?network=mainnet) + [384.7M](https://explorer.aptoslabs.com/txn/7455686848?network=mainnet) at 7:05 AM MST on 2 Oct. Those addresses swept [1,068.6M](https://explorer.aptoslabs.com/txn/7459432244?network=mainnet) and [250M](https://explorer.aptoslabs.com/txn/7451655382?network=mainnet) into **Gate 1** (the Aptos Labs explorer label). **2 Oct 2026 was a pump day: +11.1% vs five days earlier on CoinGecko, +18.2% on Kraken.** Another 612M followed to Gate on 20 and 27 Oct. Then the multisig released **6.25B more between 4 and 12 Nov 2026** ([4 × 781.2M](https://explorer.aptoslabs.com/txn/7903408704?network=mainnet), [1,875M](https://explorer.aptoslabs.com/txn/8006119888?network=mainnet), [625M](https://explorer.aptoslabs.com/txn/8010074291?network=mainnet), [1,000M](https://explorer.aptoslabs.com/txn/8010074741?network=mainnet)). No announcement, forum post or Snapshot vote for either release was found. Every transfer is linked in the 🔗 Evidence trail below.

**Sections passed: 0 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 3/10 | ❌ FAIL (hard gate) |
| 🏛️ Foundation & team | 4/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 2/10 | ❌ FAIL |
| 📉 Selling behavior | 0/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 2/10 | ❌ FAIL |
| 💧 Liquidity & market | 2/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 5/10 | ❌ FAIL |
| 🤝 Adoption & customers | 5/10 | ❌ FAIL |
| 🛡️ Security & audits | 4/10 | ❌ FAIL |
| ⚖️ Regulatory | 4/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 5/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 PACT · PACT Protocol (Pact Foundation) · 2.9 / 10 · ❌ FAIL

> **One line:** PACT is the governance token of an Aptos-based lending and payroll-credit protocol run by the Pact Foundation and Pact Labs (Tether led a $7M equity round in Pact Labs). The business is real, but the token earns nothing provable: the Foundation says fees fund buybacks, yet no buyback wallet is published. The Foundation's 2-of-3 multisig can mint without a cap (it minted 25B in Dec 2025), can freeze wallets, and has released 9.7B PACT since 1 Oct 2026 with no announcement found. **Part of the first release was on Gate within hours, on a pump day.** Trading is about $29K a day. Fails both hard gates.

| 📊 Market (CoinGecko, 16 Nov 2026 5:46 AM MST) | 🔗 On-chain (Aptos, 16 Nov 2026) |
|---|---|
| **Price** $0.00018056 | **Token** [`0xc546…fb92`](https://explorer.aptoslabs.com/fungible_asset/0xc546cc2dd26d9e9a4516b4514288bedf1085259fcb106b84b6469337f527fb92?network=mainnet) (LayerZero OFT, module [`0x81e9…c7a3`](https://explorer.aptoslabs.com/account/0x81e9fc91f9a890a1b465b5a7763047aa43e39b11359d335733f8247bf45c7a3?network=mainnet)) |
| **24h / 7d / 30d** 🔴 −1.6% / −7.5% / 🟢 +19.6% | **Aptos supply** 117.16B (indexer `supply_v2`); max in code 2^128 |
| **Market cap** $7.70M · **FDV** $22.57M | **Admin** Foundation multisig `0x36e7…` (2 of 3) · **delegate** [`0x866b…6121`](https://explorer.aptoslabs.com/account/0x866bee692bdd4f99e8bdb103e810b443fcf4b2edebd890367f5de395f3d46121?network=mainnet) |
| **24h volume** $29.0K (Gate $20.9K, Kraken $4.6K, Uniswap V4 $3.6K) | **Freeze** enabled · **blocklist** enabled · **transfer fee** 0 bps (admin can change) |
| **ATH** $0.00081776 (26 Aug 2026) · now −77.9% | **Vesting/vePACT contract** [`0x12c7…4688`](https://explorer.aptoslabs.com/account/0x12c782b869f2f2bd5f8fdcbe04aab6dbd1c579804f32738729a47678959d4688?network=mainnet) holds 67.42B (54% of 125B) |
| **Circulating** 42.65B of 125B (was 36.03B on 24 Oct 2026) | **Foundation multisig** holds 14.93B (was 21.56B on 24 Oct 2026) |

---

## 💰 Revenue — Does it make money? · 3/10 · ❌ FAIL

| Metric | Value | Source |
|---|---:|---|
| Protocol fees | **$466.7K "to date"** (no period, no fee wallet) | [Tier A self-reported] [Foundation post, 9 Oct 2026](https://www.linkedin.com/posts/pactfoundationofficial_pact-ecosystem-update-value-accrual-fee-funded-activity-7514368048921837568-OhnF) |
| Fee rule (PIP-003, vote 31 Jul – 7 Aug 2026) | After a $200K yearly budget, 80% of net fees buy PACT into a vote-gated vault, 20% to reserve | [Tier A] [PIP-003 forum post](https://forum.pact.foundation/t/proposal-pip-003-update-voting-is-live/87) |
| Buybacks claimed | 146.4M PACT | [self-reported] same post |
| Buyback vault address | **Not published**; DefiLlama lists [PACT Foundation](https://defillama.com/protocol/pact-foundation) with no fee data | [Tier A] |
| Paid to PACT holders | **$0 provable** | — |

**What it means:** A small lending business with self-reported fees, and a buyback rule nobody can audit. The bought tokens are locked, not burned or paid out. Score **3**. Hard-gate FAIL.

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** The buyback rule cannot be audited and bought tokens are locked, not burned or paid out.

## 🏛️ Foundation & team — Who is in charge? · 4/10 · ❌ FAIL

| Item | Finding | Source |
|---|---|---|
| Company | Lucid Finance, Inc. (D.B.A. Pact Labs); Oct 2026 restructuring says Pact Labs moved under PACT Deployment Inc., owned by the Foundation | [self-reported] [Foundation post](https://www.linkedin.com/posts/pactfoundationofficial_pact-ecosystem-update-value-accrual-fee-funded-activity-7514368048921837568-OhnF) |
| Investors | Tether led a **$7M Series A in Pact Labs** (equity, not tokens), with Blockchange and Lasagna | [Tier A] [tether.io, 14 Jul 2026](https://tether.io/news/tether-leads-7-million-series-a-in-pact-labs-to-expand-usat-across-payroll-and-payments/) |
| Token control | Foundation multisig `0x36e7…`: **2 of 3** owners [`0xbda3…`](https://explorer.aptoslabs.com/account/0xbda38fcb03d2c127ea1c61e5d901f6f390fe34d102c85caada1e8edd9a4d615e?network=mainnet), [`0xd581…`](https://explorer.aptoslabs.com/account/0xd581444cf5690ff15c258ffa36b25b7cbc28306dde26bbf1fbe6235e41cc7e96?network=mainnet), [`0x5548…`](https://explorer.aptoslabs.com/account/0x5548682ac2dc425c96df49f19b182905f47d7cb9cdcba5e066b87a47b80693b4?network=mainnet); it is the OFT `admin` | [Tier A] Aptos REST `MultisigAccount` and `OAppStore` resources |
| Governance | Dec 2025 Snapshot "DAO Governance Migration and Tokenomics Update": **6 voters**, 9.01B For, 0 Against | [Tier A] [Snapshot](https://snapshot.org/#/s:pactfoundation.eth/proposal/0xe6725b9e9a335a79c02e4cd5b5c8db10a08cebfac34ee00a70e9e441ad8318c3) |
| Foundation jurisdiction, named signers | Not found | [Unverified] |

## 🪙 Foundation / team holdings — How many coins do they hold? · 2/10 · ❌ FAIL

| Wallet | PACT | Notes |
|---|---:|---|
| Vesting / vePACT contract [`0x12c7…4688`](https://explorer.aptoslabs.com/account/0x12c782b869f2f2bd5f8fdcbe04aab6dbd1c579804f32738729a47678959d4688?network=mainnet) | **67,422.4M (53.9%)** | Team and investor tokens sit here; per-person split not public |
| Foundation multisig `0x36e7…` | **14,931.1M (11.9%)** | 25B minted into it on [23 Dec 2025](https://explorer.aptoslabs.com/txn/3969123121?network=mainnet); 10.07B released since |
| [`0x795a…e08f`](https://explorer.aptoslabs.com/account/0x795a61c533f6768673947b7c01f827b397f5826be1b620ef5e5ac80a46d5e08f?network=mainnet) | 9,615.6M (7.7%) | Received [24,999M via the LayerZero bridge on 24 Dec 2025](https://explorer.aptoslabs.com/txn/3974812167?network=mainnet), the day after the mint. Owner [Unverified], likely Foundation-side |
| [`0xa6eb…6045`](https://explorer.aptoslabs.com/account/0xa6ebcf9d3a7aa3e22a8b57c77489149bc969a00de87a8150f9bc105c969a6045?network=mainnet) | 3,125.0M | All from the Foundation multisig on 4 Nov 2026 |
| **Insider-controlled total (vesting + Foundation + 0x795a)** | **≈ 92.0B (≈ 74%)** | |

## 📉 Selling behavior — Do insiders sell into pumps? · 0/10 · ❌ FAIL

**Method:** every PACT transfer out of the Foundation multisig and `0x795a…` (Aptos indexer `fungible_asset_activities`), followed up to three hops. Exchange wallets come from the Aptos Labs explorer's [known-address list](https://github.com/aptos-labs/explorer/blob/main/app/data/mainnet/knownAddresses.ts) (Gate 1 = `0x0cf8…012a`, Kraken 1, MEXC 1). Deposit addresses are wallets that forward 80%+ to one of them. Pump days use CoinGecko daily closes (UTC), cross-checked with Kraken.

**A. Foundation multisig, Oct 2026 release (red line):**

| Time (MST) | From → to | PACT | Pump day? |
|---|---|---:|---|
| 1 Oct 8:35 PM | Multisig → 5 new wallets ([`0x7144`](https://explorer.aptoslabs.com/txn/7449311363?network=mainnet), [`0xe432`](https://explorer.aptoslabs.com/txn/7449312283?network=mainnet), [`0xa926`](https://explorer.aptoslabs.com/txn/7449313128?network=mainnet), [`0x124d`](https://explorer.aptoslabs.com/txn/7449314185?network=mainnet), [`0x6e37`](https://explorer.aptoslabs.com/txn/7449315095?network=mainnet)) | 3,443.8M | — |
| 1 Oct 9:44 PM | `0x6e37` → Gate deposit [`0xd215…`](https://explorer.aptoslabs.com/account/0xd215ef2f0d828e6a44074f3f0ee70c6d5acf3222b5e37870a2a683afa7625e75?network=mainnet) ([tx](https://explorer.aptoslabs.com/txn/7449993823?network=mainnet)) → [Gate 1](https://explorer.aptoslabs.com/txn/7451655382?network=mainnet) | **249.9M** | **Yes, 2 Oct UTC +11.1%** |
| 2 Oct 7:05 AM | `0xe432` → Gate deposit [`0x7fde…`](https://explorer.aptoslabs.com/account/0x7fdef7248f2e09fc8455fc14915fdbf2429e08231b70f543f344ed383fde722d?network=mainnet) ([1](https://explorer.aptoslabs.com/txn/7455683932?network=mainnet), [2](https://explorer.aptoslabs.com/txn/7455692790?network=mainnet)) | **683.7M** | **Yes** |
| 2 Oct 7:05 AM | `0x124d` → Gate deposit `0x7fde…` ([tx](https://explorer.aptoslabs.com/txn/7455686848?network=mainnet)); sweep [1,068.6M → Gate 1](https://explorer.aptoslabs.com/txn/7459432244?network=mainnet) | **384.7M** | **Yes** |
| 20 Oct 6:01 AM | `0xa926` → Gate deposit `0x7fde…` ([tx](https://explorer.aptoslabs.com/txn/7693341447?network=mainnet)) | 312.8M | No (−6.5%) |
| 27 Oct 2:51 PM | `0x124d` → Gate deposit `0x7fde…` ([tx](https://explorer.aptoslabs.com/txn/7792535615?network=mainnet)) | 299.7M | Borderline (CoinGecko +9.9%, Kraken +12.0%) |
| 2 & 27 Oct | `0x7144`, `0xa926`, `0x124d`, `0x6e37` → hop wallets → [`0x8158…3cef`](https://explorer.aptoslabs.com/account/0x815830ccfb7fb562d9ca51a7f7f569245859bc304295c8d65a97cb9cd0da3cef?network=mainnet) | 1,067.8M | `0x8158…` has sent 10–137M lots to Gate and MEXC deposits since May 2026 |

- **Pump-day total: 1,318.3M PACT ≈ $197K** at the 2 Oct close ($0.0001497), all to Gate within ten hours of leaving the Foundation multisig.
- **Nov 2026 release (6.25B) has not moved yet** ([`0xa6eb…`](https://explorer.aptoslabs.com/account/0xa6ebcf9d3a7aa3e22a8b57c77489149bc969a00de87a8150f9bc105c969a6045?network=mainnet), [`0x804d…`](https://explorer.aptoslabs.com/account/0x804dac9a21aa2d96ad8eeab7dda5e1c47ba34057bf23fad7d7d7be6343a8afcc?network=mainnet), [`0xf6ff…`](https://explorer.aptoslabs.com/account/0xf6ffb292829df6894c144a00f634036e55909e4690304c1b51e34fd4e646db44?network=mainnet), [`0x2f9a…`](https://explorer.aptoslabs.com/account/0x2f9a8db27704caf5ffd7b704ad5e7d7aa5e0b765c7e8b4d2e67a13d5f96ecbc0?network=mainnet)).

**B. `0x795a…` (got the bridged 25B), Feb–Jun 2026:** sent [1,562.5M to a Gate deposit](https://explorer.aptoslabs.com/txn/4409437962?network=mainnet) on 25 Feb 2026 and [39.1M to a Kraken deposit](https://explorer.aptoslabs.com/txn/4417425325?network=mainnet) on 26 Feb. Its recipients sent another ~1.9B to Gate, Kraken and MEXC deposits between 25 Feb and 12 Mar 2026 (e.g. [625M, 12 Mar](https://explorer.aptoslabs.com/txn/4543459492?network=mainnet)), during the 98% price fall. It also sent [47.5M](https://explorer.aptoslabs.com/txn/5804643109?network=mainnet) and [45.0M](https://explorer.aptoslabs.com/txn/5888529153?network=mainnet) to a Gate deposit on 18 and 23 Jun 2026. Those were pump days on CoinGecko (+11.0%, +12.2%) but not on Kraken. It has also *withdrawn* [500M from Gate 1](https://explorer.aptoslabs.com/txn/6918227022?network=mainnet) (25 Aug 2026), which looks like an exchange-trading account. Owner [Unverified].

**What it means:** The Foundation's own multisig, which also controls minting, released reserve tokens that were on an exchange within hours on a pump day, with no disclosure found. That is the clearest form of the red line. Score **1**. Hard-gate FAIL.

- **Disclosure quality (16 Nov 2026 rules): silence.** No disclosure was found. **Penalty applied (16 Nov 2026 rules):** a proven pump-day sale with no disclosure fails Selling (ordinary score at most 3) and then loses 2 points, floored at 0: **1 → 0**. Pump days from the report's own daily-close series.

- **One-hop amendment (16 Nov 2026):** Still a **proven sale** under the amended rule. (c) holds: no published reason was found for reserve tokens reaching an exchange within hours of release. Silence stands, so the penalty above is unchanged.

## 📊 Tokenomics & supply · 2/10 · ❌ FAIL

- **Mint:** `oft_fa::mint(signer, to, amount)` is a public entry function guarded by the admin (Foundation multisig). The asset's max supply is 2^128, so effectively **no cap**. Used once: [25B on 23 Dec 2025](https://explorer.aptoslabs.com/txn/3969123121?network=mainnet), +25% to supply, after the 6-voter Snapshot above.
- **Admin powers on the token:** freeze any wallet (enabled), blocklist (enabled, can be irrevocably disabled, not done), set transfer fee, set bridge rate limits ([module ABI](https://explorer.aptoslabs.com/account/0x81e9fc91f9a890a1b465b5a7763047aa43e39b11359d335733f8247bf45c7a3/modules/code/oft_fa?network=mainnet)).
- **Float:** 42.65B of 125B circulating (34%). Circulating supply grew **18% in three weeks** (36.03B on 24 Oct → 42.65B).
- **Vesting terms conflict:** the tokenomics doc v0.03 says team 25.69% and investors 20.91% with a 6-month lock then 6-month unlock; a Feb 2026 Medium post says a 12-month cliff then 24 months ([Medium](https://medium.com/pactfoundation/pact-tokenomics-2-0-review-analysis-7a7f5e116035)). Not reconciled.

## 💧 Liquidity & market · 2/10 · ❌ FAIL

- $29.0K of volume in 24h: Gate 72%, Kraken 16%, Uniswap V4 (Ethereum) 12%. Spreads 0.11% (Gate) and 0.17% (Kraken) (CoinGecko tickers).
- One Foundation release (1.32B) is about 17% of today's circulating market cap in coins; selling even $10K moves the price.
- 65 pump days in the last 365, and a 98% fall in Feb–Mar 2026.

## 🧑‍💻 Product & development · 5/10 · ❌ FAIL

- On-chain lending protocol on Aptos for regulated emerging-market lenders, plus Pact Labs payroll and earned-wage-access products (Toku and Payactiv wallet integrations, per their releases).
- Public code is thin: GitHub `pactlabs` governance contracts last pushed Jan 2026; core lending code is not public. An earlier scan (24 Oct 2026) counted three token-module upgrades [not re-checked].
- PACT went live on Ethereum in Aug 2026 ([forum](https://forum.pact.foundation/t/pact-is-going-live-on-ethereum/88)).

## 🤝 Adoption & customers · 5/10 · ❌ FAIL

| Item | Value | Source |
|---|---|---|
| Active loans on Aptos | ≈ $568M (24 Oct 2026 read) | [Tier B] [RWA.xyz](https://app.rwa.xyz/platforms/pact); not re-read this pass |
| Aptos Foundation | Confirms PACT's move to Aptos | [Tier A] [Aptos blog](https://aptosnetwork.com/currents/pact-enters-its-next-chapter) |
| Toku EWA partnership | Announced by Toku (Sep 2025) | [Tier A] [Business Wire](https://www.businesswire.com/news/home/20250923266461/en/Toku-and-Pact-Labs-To-Bring-Stablecoin-Powered-Earned-Wage-Access-to-Workers-Worldwide) |

The loan book is large next to a $7.7M market cap, but those loans pay lenders, not PACT holders.

## 🛡️ Security & audits · 4/10 · ❌ FAIL

- Protocol (Oct 2025) and governance (Dec 2025) audits by Adevar Labs: 0 critical or high ([reports](https://github.com/AdevarLabs/audit-reports)).
- **No audit found for the token (OFT) module,** which carries the uncapped mint, freeze and blocklist powers.
- 2-of-3 multisigs control the admin and the code upgrades.

## ⚖️ Regulatory · 4/10 · ❌ FAIL

- Foundation jurisdiction not found. Lending is done through local originators in emerging markets; their licences were not checked.
- The Foundation's own tokenomics doc says payouts are non-guaranteed and can be stopped at any time.

## 📅 Catalysts & calendar · 5/10 · ❌ FAIL

| Date | Event |
|---|---|
| Dec 2026 – Jan 2027 | Team/investor unlock window (per the tokenomics doc; dates conflict) |
| Jan 2027 | Pact Labs payroll protocol full launch (self-reported) |
| Any time | The Nov 2026 6.25B release could reach exchanges |
| Quarterly | Buyback disclosure promised (vault address still unpublished) |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team / treasury wallet → exchange during a pump | 🔴 Foundation multisig release → Gate, [1.32B on 2 Oct 2026](https://explorer.aptoslabs.com/txn/7459432244?network=mainnet) (+11.1%) |
| Undisclosed reserve releases | 🔴 3.44B (1 Oct) and 6.25B (4–12 Nov 2026), no announcement found |
| Live mint path | 🔴 Uncapped, admin-only, used for 25B in Dec 2025 |
| Freeze / blocklist | 🟡 Enabled |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| Foundation 2-of-3 multisig (token admin) | PACT Foundation | Aptos indexer (mint authority) | high | yes (on-chain) | Selling: released reserve tokens that reached an exchange within hours on a pump day |

## 📚 Sources

- [Tier A] Methodology update 16 Nov 2026: no new Arkham lookups; the attribution table uses evidence already cited in this report.
- [Tier A] Aptos indexer GraphQL (`fungible_asset_metadata`, `current_fungible_asset_balances`, `fungible_asset_activities`, `user_transactions`) and Aptos REST (OFT module ABI, `OAppStore`, `oft_impl_config::Config`, `MultisigAccount`); read 16 Nov 2026 ~5:10–5:50 AM MST
- [Tier B] Aptos Labs explorer known-address list ([GitHub](https://github.com/aptos-labs/explorer/blob/main/app/data/mainnet/knownAddresses.ts)) for Gate 1, Kraken 1, MEXC 1
- [Tier A] CoinGecko `pact-2` price, tickers and 365-day closes; Kraken PACTUSD daily OHLC
- [Tier A] [Snapshot proposal (Dec 2025)](https://snapshot.org/#/s:pactfoundation.eth/proposal/0xe6725b9e9a335a79c02e4cd5b5c8db10a08cebfac34ee00a70e9e441ad8318c3) · [PACT forum](https://forum.pact.foundation/latest) · [PIP-003](https://forum.pact.foundation/t/proposal-pip-003-update-voting-is-live/87)
- [Tier A] [Tether press release](https://tether.io/news/tether-leads-7-million-series-a-in-pact-labs-to-expand-usat-across-payroll-and-payments/) · [Aptos blog](https://aptosnetwork.com/currents/pact-enters-its-next-chapter) · [Adevar audits](https://github.com/AdevarLabs/audit-reports)
- [self-reported] [Foundation post on buybacks (9 Oct 2026)](https://www.linkedin.com/posts/pactfoundationofficial_pact-ecosystem-update-value-accrual-fee-funded-activity-7514368048921837568-OhnF) · [Tokenomics 2.0 (Medium)](https://medium.com/pactfoundation/pact-tokenomics-2-0-review-analysis-7a7f5e116035)
- [Tier B] [RWA.xyz](https://app.rwa.xyz/platforms/pact) loan figure (earlier read)
- [Unverified] owners of `0x795a…`, `0x8158…` and the five Oct release wallets; Foundation jurisdiction; buyback vault; OFT audit

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| 25B PACT minted to the Foundation multisig | [mint tx](https://explorer.aptoslabs.com/txn/3969123121?network=mainnet) · [multisig](https://explorer.aptoslabs.com/account/0x36e780c44f6e06c4678957bf3df239e394e42e4b03db01eb7c85ad226a879095?network=mainnet) | A | 16 Nov 2026 |
| Multisig released 3.44B on 1 Oct 2026 (MST) | [0x7144](https://explorer.aptoslabs.com/txn/7449311363?network=mainnet) · [0xe432](https://explorer.aptoslabs.com/txn/7449312283?network=mainnet) · [0xa926](https://explorer.aptoslabs.com/txn/7449313128?network=mainnet) · [0x124d](https://explorer.aptoslabs.com/txn/7449314185?network=mainnet) · [0x6e37](https://explorer.aptoslabs.com/txn/7449315095?network=mainnet) | A | 16 Nov 2026 |
| 1.32B of it reached Gate on the 2 Oct pump day | [249.9M](https://explorer.aptoslabs.com/txn/7449993823?network=mainnet) · [341.9M](https://explorer.aptoslabs.com/txn/7455683932?network=mainnet) · [341.9M](https://explorer.aptoslabs.com/txn/7455692790?network=mainnet) · [384.7M](https://explorer.aptoslabs.com/txn/7455686848?network=mainnet) · [sweep 250M → Gate 1](https://explorer.aptoslabs.com/txn/7451655382?network=mainnet) · [sweep 1,068.6M → Gate 1](https://explorer.aptoslabs.com/txn/7459432244?network=mainnet) | A chain + B label | 16 Nov 2026 |
| 612M more to Gate on 20 and 27 Oct | [20 Oct](https://explorer.aptoslabs.com/txn/7693341447?network=mainnet) · [27 Oct](https://explorer.aptoslabs.com/txn/7792535615?network=mainnet) | A + B | 16 Nov 2026 |
| 6.25B more released 4–12 Nov 2026 | [781.2M ×4 (first)](https://explorer.aptoslabs.com/txn/7903408704?network=mainnet) · [1,875M](https://explorer.aptoslabs.com/txn/8006119888?network=mainnet) · [625M](https://explorer.aptoslabs.com/txn/8010074291?network=mainnet) · [1,000M](https://explorer.aptoslabs.com/txn/8010074741?network=mainnet) | A | 16 Nov 2026 |
| `0x795a…` got the bridged 25B and fed exchanges in Feb–Jun 2026 | [bridge-in](https://explorer.aptoslabs.com/txn/3974812167?network=mainnet) · [1,562.5M Gate deposit](https://explorer.aptoslabs.com/txn/4409437962?network=mainnet) · [Kraken deposit](https://explorer.aptoslabs.com/txn/4417425325?network=mainnet) · [18 Jun](https://explorer.aptoslabs.com/txn/5804643109?network=mainnet) · [23 Jun](https://explorer.aptoslabs.com/txn/5888529153?network=mainnet) · [Gate withdrawal](https://explorer.aptoslabs.com/txn/6918227022?network=mainnet) | A + B · owner [Unverified] | 16 Nov 2026 |
| Admin, freeze, blocklist, mint | [OFT module](https://explorer.aptoslabs.com/account/0x81e9fc91f9a890a1b465b5a7763047aa43e39b11359d335733f8247bf45c7a3?network=mainnet) | A | 16 Nov 2026 |
| Gate 1 / Kraken 1 / MEXC 1 addresses | [Aptos Labs known addresses](https://github.com/aptos-labs/explorer/blob/main/app/data/mainnet/knownAddresses.ts) | B | 16 Nov 2026 |
| Dec 2025 tokenomics vote: 6 voters | [Snapshot](https://snapshot.org/#/s:pactfoundation.eth/proposal/0xe6725b9e9a335a79c02e4cd5b5c8db10a08cebfac34ee00a70e9e441ad8318c3) · [forum](https://forum.pact.foundation/t/new-dao-proposal-pact-tokenomics-aptos-migration/72) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Arkham pass on the Aptos wallets** (Oct release wallets, `0x795a…`, `0x8158…`, Nov recipients) | **Arkham does not support Aptos** (checked 16 Nov 2026), so the wallet list cannot be closed there. Use the Aptos explorer's known-address labels, or ask Gate and the PACT Foundation to confirm the deposit and release wallets | Free |
| 2 | **Was the Oct/Nov release disclosed?** | Ask the Pact Foundation on its forum/Telegram for the purpose of the 1 Oct and 4–12 Nov 2026 multisig transfers | Free |
| 3 | **Buyback vault** | Ask for the vault address; check for 146.4M+ PACT inflows matching 80% of net fees | Free |
| 4 | **Who is `0x795a…`?** | Find the Celo/Ethereum sender of the 24 Dec 2025 LayerZero bridge-in on LayerZero Scan | Free |
| 5 | **Watch the 6.25B Nov release** | Re-run the three-hop trace on the four Nov recipient wallets weekly | Free |
| 6 | **Token (OFT) audit and Foundation jurisdiction** | Ask the Foundation; check pactfoundation.com legal pages | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
