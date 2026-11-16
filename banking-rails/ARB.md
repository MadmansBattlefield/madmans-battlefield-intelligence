---
ticker: ARB
name: Arbitrum
chain: arbitrum-one
contract: "0x912CE59144191C1204E64559FE8253a0e49E6548"
overall_score: 5.8
overall_verdict: FAIL
section_scores:
  revenue: 4
  foundation_team: 7
  insider_holdings: 6
  selling_behavior: 5
  tokenomics_supply: 6
  liquidity_market: 7
  product_development: 8
  adoption_customers: 7
  security_audits: 7
  regulatory: 6
  catalysts: 5
gates_failed: []
red_lines:
  hack_exploit: none found on the ARB token or the Arbitrum One bridge in this pass
  mint_path_live: "yes, by design (owner = DAO UpgradeExecutor may mint up to 2% of supply per year after a governance vote; never used, supply still 9,999,998,978)"
  team_wallet_to_exchange_during_pump: "yes, partly disclosed (Coinbase Prime deposit address 0x905a, fed by Foundation and Arbitrum Safes, swept 137.5M ARB to the Coinbase Prime hot wallet on 13 pump days, incl. 27.55M on 4 Sep 2026 at +56.1%; the Foundation's reports say it runs 'ARB conversions' and pays costs in ARB, but give no trade-level detail)"
  treasury_in_single_key_wallets: "no for the DAO Treasury (on-chain governor + 3-day timelock) and Foundation Safe (3-of-6); the conversion hop 0x905a is a Coinbase Prime deposit address (Arkham), i.e. custodian-held, not a Foundation single-key wallet"
  revenue_to_holders: "none automatic; sequencer revenue (~$7.05M in 1y) goes to a DAO-controlled treasury; no DAO buyback approved"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "Sequencer revenue goes to the DAO treasury; there is no burn, buyback, fee share or fee-funded staking yield to holders. Holders have no live claim on revenue; the score describes the business, not holder accrual."
pump_day_price_source: "Gate ARB/USDT daily closes"
pump_day_disclosure_quality: buried_disclosure
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions: []
price_usd: 0.1322
price_source: "CoinGecko, 16 Nov 2026 5:25 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### ARB · Overall grade **5.8 / 10 · ❌ FAIL**

**Summary:** Arbitrum is still the largest Ethereum rollup: $1.30B of DeFi TVL, a live DAO with a 9-of-12 elected Security Council, and Foundation reports every six months. The governance plumbing is among the cleanest we have checked: the DAO treasury moves only by on-chain vote and timelock, there is no hidden mint, and 92% of supply is already unlocked. The token is the weak spot. Its revenue is tiny, about **$7.05M in the last year against a $911M market cap** (≈ 130x sales). No buyback or fee share exists. The Foundation's conversion wallet steadily feeds **Coinbase Prime**, including on the year's biggest pump days. The overall score falls just short of the 6.0 pass line.

**🚨 Top warning:** the Foundation's ARB keeps flowing to Coinbase Prime, including on pump days. Every Foundation vesting release goes to the Foundation's 3-of-6 Safe [`0xd6c8…17f6`](https://arbiscan.io/address/0xd6c8a4e72584f24bd5517afed6c01d21477c17f6). From there, ARB goes to [`0x905a…7d5d`](https://arbiscan.io/address/0x905ae0e37d838da462f6964ee1f7b249ae767d5d), which Arkham labels a **Coinbase Prime deposit address** ([Arkham](https://intel.arkm.com/explorer/address/0x905ae0e37d838da462f6964ee1f7b249ae767d5d)). It has swept **all 930M ARB it ever received** to the **Coinbase Prime hot wallet** [`0x1e70…9a10`](https://arbiscan.io/address/0x1e7016f7c23859d097668c27b72c170ed7129a10) (Etherscan: "Coinbase Prime 3"; Arkham: Coinbase Prime: Hot Wallet, tagged OTC, [Arkham](https://intel.arkm.com/explorer/address/0x1e7016f7c23859d097668c27b72c170ed7129a10)). That includes **137.5M ARB on 13 pump days**, the largest being **27.55M on 4 Sep 2026, when ARB was +56.1% on the week** ([tx](https://arbiscan.io/tx/0xb72d3b7616e0d8f7c87992c93a675dd4fee024c32d121dbda293624972436212)). The most recent deposit was 20.66M on 11 Nov 2026 ([tx](https://arbiscan.io/tx/0x34e408c44abe95ce7b78930990e7b65a66b91aa3fa96840d2b8f5958fcd8068c)). The Foundation's [H1 2026 report](https://docs.arbitrum.foundation/assets/ArbitrumFoundationBiannualReport2026H1.pdf) says it handles "ARB conversions" and uses Coinbase Prime custody, but it never says which transfers were sold. Every transfer is linked in the 🔗 Evidence trail below.

**Sections passed: 8 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 4/10 | ❌ FAIL |
| 🏛️ Foundation & team | 7/10 | ✅ PASS |
| 🪙 Foundation / team holdings | 6/10 | ✅ PASS |
| 📉 Selling behavior | 5/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 6/10 | ✅ PASS |
| 💧 Liquidity & market | 7/10 | ✅ PASS |
| 🧑‍💻 Product & development | 8/10 | ✅ PASS |
| 🤝 Adoption & customers | 7/10 | ✅ PASS |
| 🛡️ Security & audits | 7/10 | ✅ PASS |
| ⚖️ Regulatory | 6/10 | ✅ PASS |
| 📅 Catalysts & calendar | 5/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 ARB · Arbitrum · 5.8 / 10 · ❌ FAIL

> **One line:** Top-tier infrastructure with clean on-chain governance, but the token captures almost none of the chain's value. The Foundation's steady conversions through Coinbase Prime, including on rally days, keep a lid on it.

| 📊 Market (CoinGecko, 16 Nov 2026 5:25 AM MST) | 🔗 On-chain (Arbitrum One, 16 Nov 2026) |
|---|---|
| **Price** $0.1322 | **Token** [`0x912C…6548`](https://arbiscan.io/address/0x912CE59144191C1204E64559FE8253a0e49E6548#code) `ARB` (L2ArbitrumToken, proxy) |
| **24h / 7d / 30d** 🔴 −2.8% / −25.5% / −29.4% · 1y −44.7% | **`totalSupply()`** 9,999,998,978 · owner = [UpgradeExecutor](https://arbiscan.io/address/0xCF57572261c7c2BCF21ffD220ea7d1a27D40A827) |
| **Market cap** $911.4M · **FDV** $1.32B | **Circulating (CoinGecko)** 6,892,115,031 (68.9%) |
| **24h volume** $82.7M | **DAO Treasury** [`0xF3FC…9B58`](https://arbiscan.io/address/0xF3FC178157fb3c87548bAA86F9d24BA38E649B58) 2,558,085,309 (25.6%) |
| **ATH** $2.39 (12 Jan 2024) · now −94.5% | **Foundation** [vesting wallet](https://arbiscan.io/address/0x15533b77981cDa0F85c4F9a485237DF4285D6844) 80.98M · [Safe `0xd6c8…`](https://arbiscan.io/address/0xd6c8a4e72584f24bd5517afed6c01d21477c17f6) 329.0M |
| **Chain TVL** $1.30B (DefiLlama) | **Ethereum (bridged)** [`0xB507…4ad1`](https://etherscan.io/token/0xB50721BCf8d664c30412Cfbc6cf7a15145234ad1) · L2 gateway holds 261.5M |

---

## 💰 Revenue — Does it make money? · 4/10 · ❌ FAIL

| Metric | Value | Source |
|---|---:|---|
| Chain fees, last 30 days / 1 year | **$522k / $7.12M** | [Tier A] [DefiLlama Arbitrum fees](https://defillama.com/chain/arbitrum), read 16 Nov 2026 5:25 AM MST |
| Revenue (net sequencer revenue), last 30 days / 1 year | **$514k / $7.05M** | [Tier A] DefiLlama `dailyRevenue` |
| Where it goes | Net on-chain fee revenue "is now being sent to the ArbitrumDAO treasury" | [Tier A] [Foundation transparency report](https://docs.arbitrum.foundation/foundational-documents/transparency-report-initial-foundation-setup) |
| Holder accrual | **None automatic.** No DAO buyback has passed (a bond-funded buyback is only at forum stage). Offchain Labs runs its own ARB "strategic purchase plan" | [Tier A] [forum](https://forum.arbitrum.foundation/t/proposal-institutional-arb-buyback-via-bond-issuance/29491) · [Tier B] [The Block](https://www.theblock.co/news/business/2025-03-11-offchain-labs-arbitrum-token-345602) · [Cointelegraph](https://cointelegraph.com/news/offchain-labs-buys-arb-arbitrum-20b-value-secured) |

**What it means:** Revenue is real and goes to a treasury the token holders vote on. That is better than CFG or HUMA, where the token sees nothing. But it is small and shrinking: about $514k a month, or ≈ 130x price-to-sales. **4**, so the gate is not tripped.

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** Sequencer revenue goes to the DAO treasury; there is no burn, buyback, fee share or fee-funded staking yield to holders. Holders have no live claim on revenue; the score describes the business, not holder accrual.

## 🏛️ Foundation & team — Who is in charge? · 7/10 · ✅ PASS

| Item | Finding | Source |
|---|---|---|
| Builders | **Offchain Labs** (Nitro, Stylus, BoLD, Orbit) | [Tier A] [Arbitrum docs](https://docs.arbitrum.foundation/deployment-addresses) |
| Foundation | **The Arbitrum Foundation** publishes six-monthly and annual reports. In H1 2026, opex was **$24.6M plus 4.6M ARB** | [Tier A] [H1 2026 report](https://docs.arbitrum.foundation/assets/ArbitrumFoundationBiannualReport2026H1.pdf) |
| Governance | Live on-chain: [Core Governor](https://arbiscan.io/address/0xf07DeD9dC292157749B6Fd268E37DF6EA38395B9) → Core Timelock (**8 days**, `getMinDelay()` 192h); [Treasury Governor](https://arbiscan.io/address/0x789fC99093B09aD01C34DC7251D0C89ce743e5a4) → Treasury Timelock (**3 days**) | [Tier A] RPC |
| Treasury management | DAO-appointed Arbitrum Treasury Management Council (ATMC); the Foundation runs custody, payables and "ARB conversions" | [Tier A] [2025 report](https://docs.arbitrum.foundation/assets/ArbitrumFoundationTransparencyReport2025.pdf) |

**What it means:** This is the most mature governance in this batch. The weak point is that the Foundation executes conversions with wide discretion and reports only totals.

## 🪙 Foundation / team holdings — How many coins do they hold? · 6/10 · ✅ PASS

| Bucket | ARB | Control |
|---|---:|---|
| DAO Treasury [`0xF3FC…`](https://arbiscan.io/address/0xF3FC178157fb3c87548bAA86F9d24BA38E649B58) | **2,558,085,309 (25.6%)** | Treasury Governor vote + 3-day timelock |
| Foundation Safe [`0xd6c8…`](https://arbiscan.io/address/0xd6c8a4e72584f24bd5517afed6c01d21477c17f6) | 329,022,803 | **3-of-6** Safe; receives every vesting release, plus 230M from the DAO on [28 Jun 2026](https://arbiscan.io/tx/0x7b550630ce5b04349bfff58b5967f6cfe1dfc89d038e3ff4bd23a6dff5b5a76a) (Continued Funding proposal) |
| Foundation Vesting Budget Wallet [`0x1553…`](https://arbiscan.io/address/0x15533b77981cDa0F85c4F9a485237DF4285D6844) | 80,977,188 | Vesting contract; 618.5M released so far, all to `0xd6c8…` |
| Foundation-reported unlocked ARB (30 Jun 2026) | 427,046,391 | [Tier A] [H1 2026 report](https://docs.arbitrum.foundation/assets/ArbitrumFoundationBiannualReport2026H1.pdf) |
| Team / investor vesting left | **0.77B (7.7%)**, final vest March 2027 | [Tier A] [Foundation blog](https://blog.arbitrum.foundation/arbitrum-foundation-reports-first-half-2026-progress-update/) |

**What it means:** Large holdings, but they sit behind the most transparent controls in this batch: a governor and timelock for the DAO, and a multisig plus vesting contract for the Foundation. **6.**

## 📉 Selling behavior — Do insiders sell into pumps? · 5/10 · ❌ FAIL

*Pump test uses Gate ARB/USDT daily closes (UTC). 47 of the last 365 days were pump days. We traced the full ARB history of the Foundation vesting wallet, the Foundation Safe, the DAO Treasury and Coinbase Prime deposit address `0x905a…` via the Arbiscan (Etherscan v2) API.*

**Route:** Foundation Vesting → Foundation Safe `0xd6c8…` → Coinbase Prime deposit address `0x905a…` → **Coinbase Prime hot wallet** ("Coinbase Prime 3"). **Corrected after the Arkham pass:** `0x905a…` was described as a single-key EOA run by the Foundation. Arkham labels it a Coinbase Prime deposit address ([Arkham](https://intel.arkm.com/explorer/address/0x905ae0e37d838da462f6964ee1f7b249ae767d5d)). It is technically an EOA (no contract code), but the custodian holds the key, so ARB is at Coinbase Prime from the moment it lands there. The vesting release and the forward often happen in the same transaction (e.g. [8 Sep 2026](https://arbiscan.io/tx/0xaa9b88e3c3487f218766f5015cfd6e1b8ccfc94ae5631341ba073a88261d8abc)). `0x905a…` got 520M from the Foundation Safe and 215.6M from DAO-funded Safe [`0x140e…`](https://arbiscan.io/address/0x140e4d8d4229d5437efd6fc1beeb86cb2bcf9d98), a 3-of-6 Safe that shares signer `0xd1a4…` with the Foundation Safe. It also got 140.8M from [`0x3964…`](https://arbiscan.io/address/0x3964128e13e05d4a672b4b45a1a96a2d56c27efb). Arkham ([Tier B] Arkham, read 16 Nov 2026 ~7:07–7:18 AM MST (signed-in account)) labels `0xd6c8…` "Arbitrum: Gnosis Safe Proxy" (329.023M, with Foundation Vesting Wallet Proxy and DAO Treasury inflows, [Arkham](https://intel.arkm.com/explorer/address/0xd6c8a4e72584f24bd5517afed6c01d21477c17f6)) and `0x140e…` an Arbitrum Safe tagged Team Wallet (34.435M, [Arkham](https://intel.arkm.com/explorer/address/0x140e4d8d4229d5437efd6fc1beeb86cb2bcf9d98)). It tags `0x3964…` (71.991M) only as a delegator to Questbook's ARB DAO grants delegate, with no controller named ([Arkham](https://intel.arkm.com/explorer/address/0x3964128e13e05d4a672b4b45a1a96a2d56c27efb)). One deposit address taking ARB from all three suggests one Coinbase Prime client account [Unverified]. `0x905a…` has swept everything to Coinbase Prime 3 (88M in 2023, 247M in 2024, 306M in 2025, 289M in 2026).

| Day (UTC) | ARB to Coinbase Prime 3 | 5-day change | Pump? |
|---|---:|---:|---|
| 29 Sep 2023 | 25,000,000 ([tx](https://arbiscan.io/tx/0xfb07cf1fe9a09a87b11dc66a8e3d63da04a4a9b7b506f063868a0da83584f7bf)) | +11.8% | 🔴 Yes |
| 22 May 2024 | 25,000,000 ([tx](https://arbiscan.io/tx/0xecb3861676239438815f8176e78e31d5c62e5181158ca6b3d5ea755e13afa5df)) | +10.8% | 🔴 Yes |
| 25 Nov 2024 | 1,750,001 ([tx](https://arbiscan.io/tx/0xc4ea5e5926c14c0b64d1624da3c58de311d1eb1faaeffe2a1ab9811a3790f698)) | +34.8% | 🔴 Yes |
| 12–14 May 2025 | 22,499,453 (4 tx, e.g. [10M](https://arbiscan.io/tx/0x83dcc7450d78b3fa0e95c5f7210c867147fee433c2b3fe47e8f711e9377d7976)) | +12.7% to +38.7% | 🔴 Yes |
| 30 Jun 2025 | 10,000,000 ([tx](https://arbiscan.io/tx/0x98b63a0ac644727197345829c66e0e4832477a3db4f5d521c218d59d42a46642)) | +11.7% | 🔴 Yes |
| 17 Apr 2026 | 4,748,568 ([tx](https://arbiscan.io/tx/0x2d2deaf6f0b0e74ea7d55047720481550a61e62399f55fb3e95c99834c651c61)) | +18.3% | 🔴 Yes |
| 31 Aug 2026 | 10,000,000 ([tx](https://arbiscan.io/tx/0x87bacd9238c38a08948db595c87ddeb0051147953086c7af3f0450502789a613)) | +17.8% | 🔴 Yes |
| **4 Sep 2026** | **27,550,000** ([tx](https://arbiscan.io/tx/0xb72d3b7616e0d8f7c87992c93a675dd4fee024c32d121dbda293624972436212)) | **+56.1%** | 🔴 Yes |
| 8 Sep 2026 | 10,000,000 ([tx](https://arbiscan.io/tx/0x216d7e708564b405175fa030eed3c831d9535f07e270791bf0e5f5b57113ccf5)) | +17.0% | 🔴 Yes |
| *Plus 20 Sep 2024 (1.0M)* | **Total on pump days: 137.5M ARB** (13 transfers) | | |

- **Most deposits are not on pump days.** Of 97 deposits over 1M (930M in all), 13 fell on pump days. The pattern looks like a steady, scheduled programme (often 10M around month-end), not dumping into rallies. Recent examples: [30 Oct 2026](https://arbiscan.io/tx/0xc6c842c16b73c40b1f97728fe50b33bbfe14b5134745ea150f50e81ada08a6a9) and [11 Nov 2026, 20.66M](https://arbiscan.io/tx/0x34e408c44abe95ce7b78930990e7b65a66b91aa3fa96840d2b8f5958fcd8068c).
- **Coinbase Prime 3** is Coinbase Prime's hot wallet (Arkham tags it Hot Wallet and OTC): it sent 558M ARB to and got 514M back from [`0xf5ac…`](https://arbiscan.io/address/0xf5acf47847963bd0ae2b8e080729bf508b2482df) since Oct 2025. Arkham labels `0xf5ac…` another Coinbase Prime deposit address (44.407M ARB, [Arkham](https://intel.arkm.com/explorer/address/0xf5acf47847963bd0ae2b8e080729bf508b2482df)), so that loop is movement inside Coinbase Prime. Neither on-chain data nor Arkham can show whether a deposit was sold or held in custody.
- **Disclosure:** the Foundation says it executes "ARB conversions… in a prudent and systematic manner" ([2025 report](https://docs.arbitrum.foundation/assets/ArbitrumFoundationTransparencyReport2025.pdf)) and that it uses tri-party custody with Coinbase Prime ([H1 2026](https://docs.arbitrum.foundation/assets/ArbitrumFoundationBiannualReport2026H1.pdf)). Neither report links transfers to sales.

**What it means:** This is disclosed, programmatic conversion, not covert dumping. But 137.5M ARB reached an exchange venue on pump days, including the biggest rally of the year, with no trade-level disclosure. **5, unchanged after the Arkham pass.** Arkham confirms the venue (Coinbase Prime, whose hot wallet is tagged OTC as well as custody), which matches the Foundation's disclosed tri-party custody and "ARB conversions". It does not show which deposits were sold. Selling is the swing factor: a 6 would lift the overall to 89.5 / 15 = 5.97, rounded to 6.0, a PASS. That would need trade-level proof that pump-day deposits were held, not sold, and the Foundation only discloses conversions in general. Not proven counts as a fail, so it stays 5.

- **Disclosure quality (16 Nov 2026 rules): buried disclosure.** The Foundation discloses its custody arrangement and "ARB conversions" but not the trades, so this is partial disclosure and no penalty applies; Selling stays 5. Pump days from Gate ARB/USDT daily closes.

## 📊 Tokenomics & supply · 6/10 · ✅ PASS

- **Supply** is 10B, and `totalSupply()` reads 9,999,998,978 (a few tokens were burned). **Inflation is in code but never used:** the owner (DAO UpgradeExecutor) may mint up to **2%/yr** (`MINT_CAP_NUMERATOR` 200 / 10,000, `MIN_MINT_INTERVAL` 1 year), and only via a constitutional vote ([token](https://arbiscan.io/address/0x912CE59144191C1204E64559FE8253a0e49E6548#code)).
- **Unlocks:** 92.3% is unlocked or in the DAO treasury. The last 7.7% (team and investors) finishes vesting in **March 2027** ([Foundation](https://blog.arbitrum.foundation/arbitrum-foundation-reports-first-half-2026-progress-update/)).
- **Ongoing supply:** the DAO treasury (25.6% of supply) funds grants and programmes such as the 225M sent to [`0xae8c…`](https://arbiscan.io/address/0xae8cbcef7de8664c3ff5bfc58536c183ffa60b51) (Arkham: Arbitrum Safe tagged Team Wallet, programme not named, now ~0 ARB, [Arkham](https://intel.arkm.com/explorer/address/0xae8cbcef7de8664c3ff5bfc58536c183ffa60b51)) on 10 Jun 2024 ([tx](https://arbiscan.io/tx/0xeeaa92d5851e1c1e465bea71fa5493a5a69a8c4057878ce17a8dcd5fe852f078)) and the 250M sent to `0x140e…` on 20 Oct 2024 ([tx](https://arbiscan.io/tx/0xdc3f9a4c64ce1397767e0455fe747b0b3506dc5b310ec2ef97a35778804b6977)). Spending is slow but steady.

## 💧 Liquidity & market · 7/10 · ✅ PASS

- $82.7M of volume in 24h on a $911M cap (9% turnover). ARB trades on every major venue, Coinbase Prime included.
- Price is **−94.5% from ATH** and **−25.5% in 7 days**. The Gate close was $0.1348 on 15 Nov 2026, against $2.2591 at the Jan 2024 peak.

## 🧑‍💻 Product & development · 8/10 · ✅ PASS

- Arbitrum One and Nova; Nitro stack with Stylus (WASM contracts), BoLD permissionless validation, Orbit/Arbitrum chains and Timeboost (Offchain Labs; [DAO docs](https://docs.arbitrum.foundation/deployment-addresses)).
- The Foundation spent $6.59M on R&D in H1 2026 ([report](https://docs.arbitrum.foundation/assets/ArbitrumFoundationBiannualReport2026H1.pdf)).

## 🤝 Adoption & customers · 7/10 · ✅ PASS

- Chain TVL is **$1.30B** (DefiLlama, Tier A). Arbitrum is one of the two largest Ethereum L2s by TVL.
- Fees are falling: $522k in 30 days against $7.12M for the year, so the run-rate is below the yearly average. Enterprise and DeFi/fintech take 73% of the Foundation's growth spend.

## 🛡️ Security & audits · 7/10 · ✅ PASS

- Security Council: **9-of-12** Safes for both [emergency](https://arbiscan.io/address/0x423552c0F05baCCac5Bfa91C6dCF1dc53a0A1641) and [non-emergency](https://arbiscan.io/address/0xADd68bCb0f66878aB9D37a447C7b9067C5dfa941) actions (RPC `getThreshold()`), with members elected by the DAO.
- Upgrades go through an 8-day Core Timelock plus the L1 Timelock. No exploit of the token or the canonical bridge was found in this pass.
- Rollup-stage rating and the latest audit list were not re-checked in this pass [Unverified].

## ⚖️ Regulatory · 6/10 · ✅ PASS

- The Foundation is a Cayman foundation company that follows a published constitution. Its reports cover compliance (KYC/KYB) for DAO payables.
- No enforcement action against ARB was found. ARB is a governance token with no claim on revenue.

## 📅 Catalysts & calendar · 5/10 · ❌ FAIL

| Date | Event |
|---|---|
| Monthly to Mar 2027 | Final team / investor vesting (0.77B left) |
| Monthly | Foundation vesting releases → `0xd6c8…` → Coinbase Prime deposit `0x905a…` → Coinbase Prime hot wallet |
| Open | DAO debate on buyback / distribution of treasury revenue (no vote yet) |
| Ongoing | Offchain Labs ARB purchase plan |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | 🟡 Foundation Safe → Coinbase Prime deposit address ([Arkham](https://intel.arkm.com/explorer/address/0x905ae0e37d838da462f6964ee1f7b249ae767d5d)) → [Coinbase Prime hot wallet](https://arbiscan.io/address/0x1e7016f7c23859d097668c27b72c170ed7129a10) on 13 pump days (137.5M; [biggest](https://arbiscan.io/tx/0xb72d3b7616e0d8f7c87992c93a675dd4fee024c32d121dbda293624972436212)); the Foundation discloses that it converts ARB in general |
| Live mint path | 🟡 By design: 2%/yr cap, DAO vote only, [never used](https://arbiscan.io/address/0x912CE59144191C1204E64559FE8253a0e49E6548#code) |
| Treasury in single-key wallets | 🟢 No: DAO governor and timelock; the Foundation uses a 3-of-6 Safe. The hop `0x905a…` is a Coinbase Prime deposit address ([Arkham](https://intel.arkm.com/explorer/address/0x905ae0e37d838da462f6964ee1f7b249ae767d5d)), custodian-held, not a Foundation key |
| Revenue to holders | 🔴 None; ≈ 130x price-to-sales |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| Foundation vesting wallet → Coinbase Prime | Arbitrum Foundation | Foundation transparency report + Arkham venue label | high | yes (Foundation disclosure) | Selling: 137.5M ARB reached Coinbase Prime on pump days; disclosed as conversions |

## 📚 Sources

- [Tier A] Methodology update 16 Nov 2026: no new Arkham lookups; the attribution table uses evidence already cited in this report.
- [Tier A] Arbiscan via the Etherscan v2 API (chainid 42161): `tokentx` ARB history for the Foundation Vesting Budget Wallet, Foundation Safe `0xd6c8…`, DAO Treasury, `0x905a…` (1,330 tx) and Coinbase Prime 3 (latest 5,000); read 16 Nov 2026 ~8:30–8:50 AM MST
- [Tier A] Arbitrum One RPC (publicnode): `totalSupply()`, `owner()`, `MINT_CAP_NUMERATOR`/`DENOMINATOR`, `nextMint()`, balances, Safe `getThreshold()`/`getOwners()`, timelock `getMinDelay()`, 16 Nov 2026
- [Tier A] [Arbitrum DAO contract addresses](https://docs.arbitrum.foundation/deployment-addresses) · [Foundation documents](https://docs.arbitrum.foundation/foundation-documents) · [H1 2026 report](https://docs.arbitrum.foundation/assets/ArbitrumFoundationBiannualReport2026H1.pdf) · [2025 report](https://docs.arbitrum.foundation/assets/ArbitrumFoundationTransparencyReport2025.pdf) · [Initial setup report](https://docs.arbitrum.foundation/foundational-documents/transparency-report-initial-foundation-setup) · [H1 2026 blog](https://blog.arbitrum.foundation/arbitrum-foundation-reports-first-half-2026-progress-update/)
- [Tier B] Arkham, read 16 Nov 2026 ~7:07–7:18 AM MST (signed-in account): Coinbase Prime Deposit [0x905a…](https://intel.arkm.com/explorer/address/0x905ae0e37d838da462f6964ee1f7b249ae767d5d) · Coinbase Prime: Hot Wallet (OTC tag) [0x1e70…](https://intel.arkm.com/explorer/address/0x1e7016f7c23859d097668c27b72c170ed7129a10) · Coinbase Prime Deposit [0xf5ac…](https://intel.arkm.com/explorer/address/0xf5acf47847963bd0ae2b8e080729bf508b2482df) · Arbitrum: Gnosis Safe Proxy [0xd6c8…](https://intel.arkm.com/explorer/address/0xd6c8a4e72584f24bd5517afed6c01d21477c17f6) · Arbitrum Safes tagged Team Wallet [0x140e…](https://intel.arkm.com/explorer/address/0x140e4d8d4229d5437efd6fc1beeb86cb2bcf9d98), [0xae8c…](https://intel.arkm.com/explorer/address/0xae8cbcef7de8664c3ff5bfc58536c183ffa60b51) · Questbook grants-delegator tag [0x3964…](https://intel.arkm.com/explorer/address/0x3964128e13e05d4a672b4b45a1a96a2d56c27efb). Token filter is Enterprise-only; first transfer page only
- [Tier B] Etherscan label "Coinbase Prime 3" (same address on Arbitrum); [The Block](https://www.theblock.co/news/business/2025-03-11-offchain-labs-arbitrum-token-345602) · [Cointelegraph](https://cointelegraph.com/news/offchain-labs-buys-arb-arbitrum-20b-value-secured)
- [Tier A] [DefiLlama Arbitrum](https://defillama.com/chain/arbitrum) fees, revenue and TVL, 16 Nov 2026 5:25 AM MST; CoinGecko `arbitrum`; Gate ARB/USDT daily candles (UTC)
- [Unverified] whether `0x905a…` deposits were sold; whose Coinbase Prime account `0x905a…` credits; who controls `0x3964…`; which DAO programmes `0x140e…` and `0xae8c…` run; rollup-stage rating

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| DAO Treasury and Foundation Vesting Budget Wallet addresses | [DAO docs](https://docs.arbitrum.foundation/deployment-addresses) | A | 16 Nov 2026 |
| Vesting releases go to Safe `0xd6c8…` (3-of-6) and on to `0x905a…` in the same tx | [8 Sep 2026](https://arbiscan.io/tx/0xaa9b88e3c3487f218766f5015cfd6e1b8ccfc94ae5631341ba073a88261d8abc) · [30 Oct 2026 release](https://arbiscan.io/tx/0x26ee5a6df79a004ab742368677e892eb8bc9449d559477b3fc0b8be849daa3af) · [30 Oct forward](https://arbiscan.io/tx/0x7a9428a4f6d77a562f1579b8e2f688a02c2f045eb14236ab37399ff6849eaf7c) | A | 16 Nov 2026 |
| `0x905a…` (Coinbase Prime deposit address) swept all 930M ARB to Coinbase Prime 3 | [0x905a](https://arbiscan.io/address/0x905ae0e37d838da462f6964ee1f7b249ae767d5d) · [Coinbase Prime 3](https://arbiscan.io/address/0x1e7016f7c23859d097668c27b72c170ed7129a10) · Arkham [deposit label](https://intel.arkm.com/explorer/address/0x905ae0e37d838da462f6964ee1f7b249ae767d5d) · [hot wallet label](https://intel.arkm.com/explorer/address/0x1e7016f7c23859d097668c27b72c170ed7129a10) | A + B label | 16 Nov 2026 |
| 4 Sep 2026 (+56.1%): 27.55M to Coinbase Prime 3 | [tx](https://arbiscan.io/tx/0xb72d3b7616e0d8f7c87992c93a675dd4fee024c32d121dbda293624972436212) | A + B label | 16 Nov 2026 |
| 13 pump-day deposits total 137.5M | see Selling table (each row linked) | A | 16 Nov 2026 |
| DAO → Foundation Safe 230M (28 Jun 2026) | [tx](https://arbiscan.io/tx/0x7b550630ce5b04349bfff58b5967f6cfe1dfc89d038e3ff4bd23a6dff5b5a76a) · [H1 report, Continued Funding](https://docs.arbitrum.foundation/assets/ArbitrumFoundationBiannualReport2026H1.pdf) | A | 16 Nov 2026 |
| `0x140e…` (250M from DAO) shares a signer with the Foundation Safe and fed `0x905a…` | [DAO tx](https://arbiscan.io/tx/0xdc3f9a4c64ce1397767e0455fe747b0b3506dc5b310ec2ef97a35778804b6977) · [Safe](https://arbiscan.io/address/0x140e4d8d4229d5437efd6fc1beeb86cb2bcf9d98) | A | 16 Nov 2026 |
| 2%/yr mint cap, owner = UpgradeExecutor, never minted | [token code](https://arbiscan.io/address/0x912CE59144191C1204E64559FE8253a0e49E6548#code) · [UpgradeExecutor](https://arbiscan.io/address/0xCF57572261c7c2BCF21ffD220ea7d1a27D40A827) | A | 16 Nov 2026 |
| Security Council 9-of-12; Core Timelock 8 days; Treasury Timelock 3 days | [SC](https://arbiscan.io/address/0x423552c0F05baCCac5Bfa91C6dCF1dc53a0A1641) · [Core Timelock](https://arbiscan.io/address/0x34d45e99f7D8c45ed05B5cA72D54bbD1fb3F98f0) · [Treasury Timelock](https://arbiscan.io/address/0xbFc1FECa8B09A5c5D3EFfE7429eBE24b9c09EF58) | A | 16 Nov 2026 |
| Revenue $7.05M (1y) to DAO treasury; no holder accrual | [DefiLlama](https://defillama.com/chain/arbitrum) · [setup report](https://docs.arbitrum.foundation/foundational-documents/transparency-report-initial-foundation-setup) | A | 16 Nov 2026 |
| 7.7% left to vest, final in Mar 2027 | [Foundation blog](https://blog.arbitrum.foundation/arbitrum-foundation-reports-first-half-2026-progress-update/) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Arkham pass: done 16 Nov 2026** (first transfer page per wallet). `0x905a…` and `0xf5ac…` = Coinbase Prime deposit addresses; `0x1e70…` = Coinbase Prime hot wallet; `0xd6c8…`, `0x140e…`, `0xae8c…` = Arbitrum Safes. Still open: whose Prime account `0x905a…` credits; who controls `0x3964…` | Ask the Foundation to confirm `0x905a…` is its Prime account | Free |
| 2 | **Were the Coinbase Prime deposits sold?** | Ask the Foundation for a per-month conversion log (ARB sent vs USD received); compare with its six-monthly ARB-cost tables | Free |
| 3 | **Which DAO programmes run Safes `0x140e…` and `0xae8c…`?** | Match the DAO tx dates (20 Oct 2024, 10 Jun 2024) to Tally / Snapshot proposals | Free |
| 4 | **Rollup stage and latest audits** | Read L2BEAT's Arbitrum One page and the Offchain Labs audit repo | Free |
| 5 | **Will the DAO direct revenue to ARB holders?** | Watch the governance forum for a buyback or fee-distribution vote | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
