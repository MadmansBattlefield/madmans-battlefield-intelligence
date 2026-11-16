---
ticker: ONDO
name: Ondo
chain: ethereum
contract: "0xfAbA6f8e4a5E8Ab82F62fe7C39859FA577269BE3"
overall_score: 4.7
overall_verdict: FAIL
section_scores:
  revenue: 3
  foundation_team: 4
  insider_holdings: 3
  selling_behavior: 4
  tokenomics_supply: 2
  liquidity_market: 9
  product_development: 7
  adoption_customers: 7
  security_audits: 6
  regulatory: 7
  catalysts: 3
gates_failed: [revenue]
red_lines:
  hack_exploit: none
  mint_role_used: not_used_still_possible
  control_dispute_at_company: active_litigation
  admin_safe_funds_to_exchange: "yes (100.5M ONDO via Safe 0xEA57 into 5 Coinbase deposit addresses, 27 Aug – 13 Oct 2026; 18.2M on the 21 Sep pump day; undisclosed)"
price_usd: 0.3115
price_source: "CoinGecko, 14 Nov 2026 9:08 AM MST"
last_updated: 2026-11-15
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### ONDO · Overall grade **4.7 / 10 · ❌ FAIL**

**Summary:** Ondo the company runs billions in real tokenized products. ONDO the token earns none of it, has a live mint role, and half the supply sits in one 4-of-7 Safe with no on-chain lock. New: a Safe funded only by that admin Safe sent 100.5M ONDO into Coinbase deposit addresses in Aug–Oct 2026, one batch on a pump day, with no disclosure.

**🚨 Top warning (red line):** Ondo's admin Safe funded Safe [`0xEA57…75e1`](https://etherscan.io/address/0xEA5785e1727DE2Ba2CEfd102Cb2Dd91E018675e1), which sent **100.5M ONDO (≈ $43.7M) into five Coinbase deposit addresses** between 27 Aug and 13 Oct 2026, including **18.2M ONDO on the 21 Sep pump day (+31.8%)**. Nothing was disclosed. Check it yourself: [pump-day send](https://etherscan.io/tx/0x13df98ebcd46cb359d06022a5ae2631780a5e532e36fef7dd35c8546d3fb13f7) · [sweep into Coinbase 10](https://etherscan.io/tx/0xcb2612aa97f6b20693de46c4df4220468a0f0c8328bbf13858d69b616741dd9f) · [0xEA57… on Etherscan](https://etherscan.io/address/0xEA5785e1727DE2Ba2CEfd102Cb2Dd91E018675e1) · [0xEA57… on Arkham](https://intel.arkm.com/explorer/address/0xEA5785e1727DE2Ba2CEfd102Cb2Dd91E018675e1) · [deposit address on Arkham (“Coinbase Deposit”)](https://intel.arkm.com/explorer/address/0x8119e9ffc2aca20b8a121792fe21149c1b7d1f46). Every transfer is linked in the 🔗 Evidence trail below.

**Sections passed: 5 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 3/10 | ❌ FAIL |
| 🏛️ Foundation & team | 4/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 3/10 | ❌ FAIL |
| 📉 Selling behavior | 4/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 2/10 | ❌ FAIL |
| 💧 Liquidity & market | 9/10 | ✅ PASS |
| 🧑‍💻 Product & development | 7/10 | ✅ PASS |
| 🤝 Adoption & customers | 7/10 | ✅ PASS |
| 🛡️ Security & audits | 6/10 | ✅ PASS |
| ⚖️ Regulatory | 7/10 | ✅ PASS |
| 📅 Catalysts & calendar | 3/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 ONDO · Ondo · 4.7 / 10 · ❌ FAIL

> **One line:** Ondo the company runs billions in real tokenized products. ONDO the token earns none of it, has a live mint role, and half the supply sits in one 4-of-7 Safe with no on-chain lock. New: a Safe funded only by that admin Safe sent 100.5M ONDO into Coinbase deposit addresses in Aug–Oct 2026, one batch on a pump day, with no disclosure.

| 📊 Market (CoinGecko, 14 Nov 2026 9:08 AM MST) | 🔗 On-chain (Ethereum, 10 Oct 2026) |
|---|---|
| **Price** $0.3115 | **Token** [`0xfAbA…9BE3`](https://etherscan.io/address/0xfAbA6f8e4a5E8Ab82F62fe7C39859FA577269BE3) "Ondo", Solidity 0.8.3, not a proxy |
| **24h / 7d / 30d** 🔴 −9.2% / −13.9% / −29.5% | **Supply** 10,000,000,000 (no mint used yet) |
| **Market cap** $1.52B · **FDV** $3.12B | **Admin Safe (4 of 7)** [`0x677F…A1A1`](https://etherscan.io/address/0x677FD4Ed8aE623f2f625DEB2D64F2070E46cA1A1) 5,179,207,574 (51.8%, 15 Nov) |
| **24h volume** $95.8M | **Roles on Safe** `DEFAULT_ADMIN`, `MINTER`, `TRANSFER` since 28 Apr 2022 |
| **ATH** $2.14 (15 Dec 2024) · now −85% | **Circulating (CoinGecko)** 4.87B |

---

## 💰 Revenue — Does it make money? · 3/10 · ❌ FAIL

| Metric | Value | Source |
|---|---:|---|
| 30-day fees (product side) | $7,933,472 | [Tier A] DefiLlama `ondo-yield-assets`, `ondo-global-markets`, `ondo-perps` |
| 30-day revenue to protocol/token | **$0** | [Tier A] DefiLlama |
| All-time fees | $97,351,480 | [Tier A] DefiLlama |
| USDY TVL | $2.40B (152.85% collateralised) | [Tier A] ondo.finance, 3 Nov 2026 |
| OUSG | $317.7M (BUIDL, SWEEP, BENJI, FYOXX) | [Tier A] ondo.finance |
| Ondo Global Markets (stocks) | $1.35B, 470+ assets | [Tier A] ondo.finance |
| Token's claim | "The governance token for the Ondo DAO and Flux Finance." **No contractual claim** on Ondo Finance Inc. revenue or equity | [Tier A] docs.ondo.foundation |
| Company revenue | No audited financials | [Unverified] |

**What it means:** The business clearly makes money. The token is a governance coupon with no cash flow. Real Rails: "TOKEN EARNS NOTHING."

## 🏛️ Foundation & team — Who is in charge? · 4/10 · ❌ FAIL

| Item | Finding | Source |
|---|---|---|
| Token steward | Ondo Foundation — filings not checked | [Unverified] |
| Operating company | Ondo Finance Inc. (Delaware) | [Tier A] court docket |
| Founder | Nathan Allman, Founder & CEO — verified as executive officer on SEC Form D (Ondo I LP, CIK 0001957431, filed 19 Jan 2024) | [Tier A] EDGAR |
| Founder status | Death reported 25 May 2026 | [Tier B] CoinDesk 23 Sep 2026 · [Unverified] by a primary record |
| Litigation | *Kathleen C. Allman v. Ondo Finance Inc.*, Del. Ch. C.A. No. 2026-0978, filed 24 Jul 2026, ACTIVE (Chancellor McCormick) | [Tier A] Delaware CourtConnect |
| Token admin | 4-of-7 Safe [`0x677FD4Ed8aE623f2f625DEB2D64F2070E46cA1A1`](https://etherscan.io/address/0x677FD4Ed8aE623f2f625DEB2D64F2070E46cA1A1) ([Arkham](https://intel.arkm.com/explorer/address/0x677FD4Ed8aE623f2f625DEB2D64F2070E46cA1A1)) — signers not publicly named. Arkham: "Ondo Finance: Gnosis Safe Proxy", inside its "Ondo Finance" entity (2.0K addresses, ~$1.59B, almost all this Safe's ONDO) | [Tier A] chain · [Tier B] Arkham, read 15 Nov 2026 ~11:00 AM MST (signed-in account) |
| Regulated subsidiaries | Ondo Capital Management (SEC RIA); Ondo USDY LLC (FinCEN MSB); acquired Oasis Pro (BD, ATS, TA) | [Tier A] SEC/FinCEN · [Tier A] Ondo |

**What it means:** Who controls the company is in court, and who signs for half the token supply is not public.

## 🪙 Foundation / team holdings — How many coins do they hold? · 3/10 · ❌ FAIL

| Wallet | ONDO | % of 10B | Locked? |
|---|---:|---:|---|
| Admin Safe [`0x677F…A1A1`](https://etherscan.io/address/0x677FD4Ed8aE623f2f625DEB2D64F2070E46cA1A1) · [Arkham](https://intel.arkm.com/explorer/address/0x677FD4Ed8aE623f2f625DEB2D64F2070E46cA1A1) (Nansen: "Ondo Finance: Multisig 2"; Arkham: "Ondo Finance: Gnosis Safe Proxy". Two Tier B labels, so **verified Ondo**) | 5,179,207,574 (15 Nov) | 51.8% | 🔓 **Plain balance** — LinearTimelock does not apply |
| Safe [`0xEA5785e1727DE2Ba2CEfd102Cb2Dd91E018675e1`](https://etherscan.io/address/0xEA5785e1727DE2Ba2CEfd102Cb2Dd91E018675e1) · [Arkham](https://intel.arkm.com/explorer/address/0xEA5785e1727DE2Ba2CEfd102Cb2Dd91E018675e1) (received 125M on 22 Apr, then 150M each on 11 May, 22 Jun, 21 Aug and 23 Sep 2026, all from the admin Safe: [22 Apr 125M](https://etherscan.io/tx/0x95b3e7409ba22bbac9e7157114ab83a8491d70a25dcaaecd2e9cd876784d9070) · [11 May 150M](https://etherscan.io/tx/0xe53c865f6e9fe67c1ece9a5edbd72696541e7011955c5f1ff6281ae3c01229c5) · [22 Jun 150M](https://etherscan.io/tx/0x33cca98b95a4141495fc7ae7d483e2472b7699e27ee528e265f22505e113d19b) · [21 Aug 150M](https://etherscan.io/tx/0xf84d62650ccacd6e4e98841fe86c1f961d984957873dc07f96610c206f8ae3d8) · [23 Sep 150M](https://etherscan.io/tx/0xaf248808b0611bc75d73db9d36f9c48be12144610aee61026471a7d732491256)) | 725,000,000 received; 687.5M paid out in 33 sends of ≥1M; **36,007,902 left** (15 Nov). Arkham: no entity name | 7.25% | 🔓 |
| Safe [`0x524083970c7a1e62fbaa61d38781f87a4f191fd0`](https://etherscan.io/address/0x524083970c7a1e62fbaa61d38781f87a4f191fd0) · [Arkham](https://intel.arkm.com/explorer/address/0x524083970c7a1e62fbaa61d38781f87a4f191fd0) (received 2025 – Jan 2026) | 1,548,000,000 received, then distributed; ~238K left. Arkham: no entity name | 15.48% | 🔓 |
| Safe [`0xD2e6E930E25456fFcD4Df0124563cC334F3284f4`](https://etherscan.io/address/0xD2e6E930E25456fFcD4Df0124563cC334F3284f4) | Nansen "Smart Account by Safe" | — | traced |

**What it means:** Over half the supply can be moved by four signatures today, despite the "January 2027 unlock" story.

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL

| Test | Result | Source |
|---|---|---|
| Admin Safe outflows | 825M traced (725M → `0xEA5785E1…`, 100M → `0x52408397…`). **Correction (15 Nov):** the earlier line "neither forwarded to an exchange within one hop" was wrong. `0xEA57…` sent ONDO straight into five Coinbase deposit addresses (table below) | [Tier A] chain |
| Nansen 7-day exchange net flow | −$4.43M (net out of exchanges) | [Tier B] Nansen |
| Nansen 7-day smart-trader net flow | −$128,705 | [Tier B] Nansen |
| Top exchange-holder balance | 731.4M (+7.27M in 7 days) | [Tier B] Nansen |
| Pump-window test on `0xEA57…` sends (new) | **11 of its 33 sends of ≥1M** (22 Apr – 13 Oct 2026) fell on pump days, vs ~6 expected by chance (38 of 208 days since 22 Apr were pump days). Most went to other Safes whose owners are unknown | [Tier A] Etherscan v2 `tokentx` + CoinGecko daily closes |

**`0xEA57…` → Coinbase (new, 15 Nov).** Arkham labels all five receivers "Coinbase Deposit". On-chain, each one got a 1-ONDO test from wallet `0xd6471797…b176` (which test-pays every recipient of this Safe shortly before the Safe pays), then the main send, then forwarded everything to Etherscan's "Coinbase 10" hot wallet [`0xA9D1e08C…3E43`](https://etherscan.io/address/0xA9D1e08C7793af67e9d92fe308d5697FB81d3E43) within 3–4 minutes. Test-payer: [`0xd6471797…b176`](https://etherscan.io/address/0xd64717976a3416e5add4c9740a96b90763b8b176). That is how exchange deposit addresses behave.

| Date (UTC) | Coinbase deposit address (explorer · label) | ONDO | ≈ USD at that day's close | 5-day change | Pump? | Send → sweep to Coinbase 10 |
|---|---|---:|---:|---:|---|---|
| 27 Aug 2026 15:38 | [`0x9532fc43…91d0`](https://etherscan.io/address/0x9532fc43f31a21b709f61c10413d875703da91d0) ([Arkham](https://intel.arkm.com/explorer/address/0x9532fc43f31a21b709f61c10413d875703da91d0)) | 22,857,892 | ≈ $8.6M | −5.5% | ❌ No | [tx `0xbb656309…`](https://etherscan.io/tx/0xbb656309edb5acdfe0e5694b20b3cf4b04cb50252d9df9dae81479ce9b1fc6ca) → sweep [tx `0xa4a0211e…`](https://etherscan.io/tx/0xa4a0211e989888dd183dca5c73b891b0b328d876c7fc4321cd203c84f716237f) |
| 9 Sep 2026 15:02 | [`0x48576f7b…e7ff`](https://etherscan.io/address/0x48576f7bccebf15381a4a11a42b277bbb8b4e7ff) ([Arkham](https://intel.arkm.com/explorer/address/0x48576f7bccebf15381a4a11a42b277bbb8b4e7ff)) | 15,055,000 | ≈ $5.6M | +3.3% | ❌ No | [tx `0x1a1d988d…`](https://etherscan.io/tx/0x1a1d988d01373fa49d9dd843e7f53cf0205255538011417387b1ee95d4a74818) → sweep [tx `0xfe18e591…`](https://etherscan.io/tx/0xfe18e59112479e1b21936c51cc16464979f2b24f20e83451a83ba9839ddada4c) |
| **21 Sep 2026 14:03** | [`0x8119e9ff…1f46`](https://etherscan.io/address/0x8119e9ffc2aca20b8a121792fe21149c1b7d1f46) ([Arkham](https://intel.arkm.com/explorer/address/0x8119e9ffc2aca20b8a121792fe21149c1b7d1f46)) | **18,196,018** | **≈ $7.9M** | **+31.8%** | 🔴 **Yes** | [tx `0x13df98eb…`](https://etherscan.io/tx/0x13df98ebcd46cb359d06022a5ae2631780a5e532e36fef7dd35c8546d3fb13f7) → sweep [tx `0xcb2612aa…`](https://etherscan.io/tx/0xcb2612aa97f6b20693de46c4df4220468a0f0c8328bbf13858d69b616741dd9f) |
| 30 Sep 2026 15:06 | [`0xfca06e6d…6175`](https://etherscan.io/address/0xfca06e6de9e8259342cff142e1e3821da8ed6175) ([Arkham](https://intel.arkm.com/explorer/address/0xfca06e6de9e8259342cff142e1e3821da8ed6175)) | 23,786,466 | ≈ $11.9M | −3.8% | ❌ No | [tx `0xfd53e492…`](https://etherscan.io/tx/0xfd53e492a7e5e2f9b67ee25ce9c3dbed4597c2b83815e90b1dc2d181d4b57831) → sweep [tx `0xbfe030e3…`](https://etherscan.io/tx/0xbfe030e3f9c01bcf68ba5e5ea85cda7f0462a7e569efe2a35676e91959e14b31) |
| 13 Oct 2026 15:21 | [`0x2b47bca4…60f9`](https://etherscan.io/address/0x2b47bca4fa2e744231727ad9b8245f285ab760f9) ([Arkham](https://intel.arkm.com/explorer/address/0x2b47bca4fa2e744231727ad9b8245f285ab760f9)) | 20,602,074 | ≈ $9.7M | −0.2% | ❌ No | [tx `0xcc47888e…`](https://etherscan.io/tx/0xcc47888e5f6a89d10eae81026508f7b9602c31cc52af8bfe13de71cdf7a1042b) → sweep [tx `0x81df2c58…`](https://etherscan.io/tx/0x81df2c582e943b0cdde341e3d42f448c3b2e6e3b5e69bd07ecd3367921a43348) |
| **Total** | 5 addresses | **100,497,450** | **≈ $43.7M** | | 1 of 5 | |

- The 21 Sep send ([tx `0x13df98ebcd46…`](https://etherscan.io/tx/0x13df98ebcd46cb359d06022a5ae2631780a5e532e36fef7dd35c8546d3fb13f7)) was swept to Coinbase 10 four minutes later ([tx `0xcb2612aa97f6…`](https://etherscan.io/tx/0xcb2612aa97f6b20693de46c4df4220468a0f0c8328bbf13858d69b616741dd9f)). 21 Sep and 22 Sep were both pump days (+31.8% / +31.9%), so the call does not depend on how the day boundary is drawn.
- `0x5240…` also sent **8,316,583 ONDO to [`0x90b1dd36…2486`](https://etherscan.io/address/0x90b1dd36e7379b85a16a898b35d8fe77a9e02486) on 10 Apr 2026** ([tx `0x5541807c…`](https://etherscan.io/tx/0x5541807cc730c536b47535cfd6edb8c5596d538b79909685c78a00e45f953747); not a pump day, −0.3%). Arkham labels that address "Coinbase Prime Custody" ([Arkham](https://intel.arkm.com/explorer/address/0x90b1dd36e7379b85a16a898b35d8fe77a9e02486)). It moved the same amount on to [`0x1d1daecc…`](https://etherscan.io/address/0x1d1daeccc6a2eeb5044b5ef25a3837591211bac0) on 16 Jul 2026 ([tx `0x12f827c1…`](https://etherscan.io/tx/0x12f827c16fe3564097d0bde007631d39e3528437a9c00dee1945dfe95bbc5b61)), a pump day (+11.4%); that receiver is not identified.
- **Labels:** the Coinbase link rests on two independent Tier B sources, Arkham's "Coinbase Deposit" labels on the five receivers ([Tier B] Arkham, read 15 Nov 2026 ~11:00 AM MST (signed-in account)) and Etherscan's public "Coinbase 10" tag on the address they all swept into, plus the [Tier A] sweep pattern. Treated as verified. The "Coinbase Prime Custody" label on `0x90b1…` is Arkham only, so [Unverified].
- **Who sent it:** `0xEA57…` is funded only by Ondo's admin Safe, and the same test-payer `0xd6471797…` precedes every one of its payouts. That looks like a scheduled payout to many parties (investors, staff, partners). The five Coinbase addresses could belong to payees, not to Ondo itself. Ondo publishes no recipient list, so this can't be told apart.
- Exchange deposits are credited to one account. Whether that ONDO was sold happens inside Coinbase and is not visible on-chain.
- Real Rails treasury badge: **CAUTION**.

**What it means:** Tokens released from Ondo's admin Safe reached Coinbase directly: 100.5M ONDO (~$44M) in seven weeks, including 18.2M on a +32% pump day. Nothing was disclosed. One of five exchange sends on a pump day is in line with chance, and the coins may have gone to payees, not to Ondo, so this is not proof that Ondo dumped. Still, undisclosed releases from the issuer's Safe reached an exchange on a pump day, so the score drops from 5 to 4 (fail, but not the hard gate).

## 📊 Tokenomics & supply · 2/10 · ❌ FAIL

| Item | Value | Source |
|---|---|---|
| Max supply (docs / MiCA) | 10B, "no scheduled or planned inflation" | [Tier A] docs |
| Mint function | **Live.** Any `MINTER_ROLE` holder can mint, capped only by uint96 | [Tier A] verified source |
| FIP-08 | Anniversary unlocks each January 2025–2029 | [Tier A] [FIP-08](https://forum.fluxfinance.com/t/fip-08-release-of-the-ondo-token-lock-up/563) |
| Jan 2027 tranche | Real Rails: 1.94B (19.4%) on 18 Jan 2027 · trackers: ~1.71B | [Unverified] — governance promise, not an on-chain vest |
| Observed releases | ~100–150M ONDO a month leaking into supply recently | Research model from chain flows |
| Burns | None claimed | [Tier A] |

**What it means:** The code allows unlimited minting and the "unlock schedule" is a promise, not a lock.

## 💧 Liquidity & market · 9/10 · ✅ PASS

- $95.8M 24h volume on a $1.52B cap; listed on all major venues.

## 🧑‍💻 Product & development · 7/10 · ✅ PASS

- Live: USDY, OUSG, Ondo Global Markets (tokenized stocks), Flux.
- **Abandoned:** Ondo Chain L1 — never reached mainnet, discontinued 27 Jul 2026, replaced by off-chain "Ondo Network."
- GitHub `ondoprotocol`: 16 repos, 4 pushed in 90 days, last push 27 Oct 2026.

## 🤝 Adoption & customers · 7/10 · ✅ PASS

| Claim | Status |
|---|---|
| Mastercard MTN's first RWA provider; OUSG backed mainly by BlackRock BUIDL + Franklin + WisdomTree | Confirmed |
| Acquired Oasis Pro (BD, ATS, TA) | Confirmed |
| SEC investigation closed without charges | Confirmed |
| DTCC Industry Working Group participant | Confirmed |
| "Partnered with BlackRock" | Partly |
| "BlackRock, Fidelity, JPMorgan, Goldman are inside Ondo" | False |

## 🛡️ Security & audits · 6/10 · ✅ PASS

- No ONDO hack on file. Token has no pause or blacklist and is not upgradeable. USDY/OUSG admin and KYC controls not fully reviewed [Unverified].

## ⚖️ Regulatory · 7/10 · ✅ PASS

- SEC-registered adviser, FinCEN MSB, broker-dealer/ATS via Oasis Pro; OUSG under Reg D 506(c)/3(c)(7); USDY under Reg S. SEC investigation closed without charges.

**What it means:** The company is one of the more regulated names in crypto. None of that attaches to the ONDO token.

## 📅 Catalysts & calendar · 3/10 · ❌ FAIL

| Date | Event |
|---|---|
| 18 Jan 2027 | FIP-08 anniversary unlock (1.71–1.94B, figures disputed) |
| Open | Del. Ch. 2026-0978 outcome |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None |
| Mint role used | 🟢 Not used (supply exactly 10B on 10 Oct) — 🔴 still possible |
| Control dispute at the company | 🟡 Active litigation |
| Admin-Safe funds → exchange, undisclosed | 🔴 Yes: 100.5M ONDO into Coinbase via [`0xEA57…`](https://etherscan.io/address/0xEA5785e1727DE2Ba2CEfd102Cb2Dd91E018675e1), 27 Aug – 13 Oct 2026; 18.2M on the 21 Sep pump day ([send](https://etherscan.io/tx/0x13df98ebcd46cb359d06022a5ae2631780a5e532e36fef7dd35c8546d3fb13f7) · [sweep](https://etherscan.io/tx/0xcb2612aa97f6b20693de46c4df4220468a0f0c8328bbf13858d69b616741dd9f) · [Arkham label](https://intel.arkm.com/explorer/address/0x8119e9ffc2aca20b8a121792fe21149c1b7d1f46)) |

## 📚 Sources

- [Tier A] Ethereum verified source, RPC and Blockscout holder/log reads, 10 Oct 2026
- [Tier A] [docs.ondo.foundation/ondo-token](https://docs.ondo.foundation/ondo-token) · [FIP-08](https://forum.fluxfinance.com/t/fip-08-release-of-the-ondo-token-lock-up/563)
- [Tier A] [Delaware CourtConnect 2026-0978](https://courtconnect.courts.delaware.gov/cc/cconnect/ck_public_qry_doct.cp_dktrpt_docket_report?case_id=2026-0978)
- [Tier A] [SEC EDGAR CIK 1949480](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=1949480)
- [Tier A] DefiLlama fees/revenue, 13 Nov 2026 · ondo.finance product figures, 3 Nov 2026
- [Tier A] CoinGecko `ondo-finance`, 14 Nov 2026 9:08 AM MST
- [Tier A] Etherscan v2 API `tokentx` / `tokenbalance` for `0x677F…`, `0xEA57…`, `0x5240…`, the five Coinbase deposit addresses and `0x90b1dd36…`; read 15 Nov 2026 ~11:15 AM MST · CoinGecko `ondo-finance` 365-day daily closes, 15 Nov 2026
- [Tier B] CoinDesk 23 Sep 2026 · Nansen pack 9 Nov 2026
- [Tier B] Arkham, read 15 Nov 2026 ~11:00 AM MST (signed-in account): "Ondo Finance" entity; labels for `0x677F…` (Ondo Finance Safe), the five "Coinbase Deposit" addresses and "Coinbase Prime Custody" `0x90b1…`. Arkham shows relative ages only; dates above come from on-chain reads where amounts match. Arkham's all-time exchange totals are Enterprise-locked, and the browser read only the first page of transfers
- [Tier B] Etherscan public name tag "Coinbase 10" for [`0xA9D1e08C7793af67e9d92fe308d5697FB81d3E43`](https://etherscan.io/address/0xA9D1e08C7793af67e9d92fe308d5697FB81d3E43)
- [Tier A] Explorer pages used (Etherscan): admin Safe [`0x677F…`](https://etherscan.io/address/0x677FD4Ed8aE623f2f625DEB2D64F2070E46cA1A1) · [`0xEA57…`](https://etherscan.io/address/0xEA5785e1727DE2Ba2CEfd102Cb2Dd91E018675e1) · [`0x5240…`](https://etherscan.io/address/0x524083970c7a1e62fbaa61d38781f87a4f191fd0) · test-payer [`0xd647…`](https://etherscan.io/address/0xd64717976a3416e5add4c9740a96b90763b8b176) · deposit addresses [`0x9532fc…`](https://etherscan.io/address/0x9532fc43f31a21b709f61c10413d875703da91d0) · [`0x48576f…`](https://etherscan.io/address/0x48576f7bccebf15381a4a11a42b277bbb8b4e7ff) · [`0x8119e9…`](https://etherscan.io/address/0x8119e9ffc2aca20b8a121792fe21149c1b7d1f46) · [`0xfca06e…`](https://etherscan.io/address/0xfca06e6de9e8259342cff142e1e3821da8ed6175) · [`0x2b47bc…`](https://etherscan.io/address/0x2b47bca4fa2e744231727ad9b8245f285ab760f9) · [`0x90b1…`](https://etherscan.io/address/0x90b1dd36e7379b85a16a898b35d8fe77a9e02486) · [`0x1d1d…`](https://etherscan.io/address/0x1d1daeccc6a2eeb5044b5ef25a3837591211bac0)
- [Tier B] Arkham address pages used: [0x677F…](https://intel.arkm.com/explorer/address/0x677FD4Ed8aE623f2f625DEB2D64F2070E46cA1A1) · [0xEA57…](https://intel.arkm.com/explorer/address/0xEA5785e1727DE2Ba2CEfd102Cb2Dd91E018675e1) · [0x5240…](https://intel.arkm.com/explorer/address/0x524083970c7a1e62fbaa61d38781f87a4f191fd0) · [0x9532fc…](https://intel.arkm.com/explorer/address/0x9532fc43f31a21b709f61c10413d875703da91d0) · [0x48576f…](https://intel.arkm.com/explorer/address/0x48576f7bccebf15381a4a11a42b277bbb8b4e7ff) · [0x8119e9…](https://intel.arkm.com/explorer/address/0x8119e9ffc2aca20b8a121792fe21149c1b7d1f46) · [0xfca06e…](https://intel.arkm.com/explorer/address/0xfca06e6de9e8259342cff142e1e3821da8ed6175) · [0x2b47bc…](https://intel.arkm.com/explorer/address/0x2b47bca4fa2e744231727ad9b8245f285ab760f9) · [0x90b1…](https://intel.arkm.com/explorer/address/0x90b1dd36e7379b85a16a898b35d8fe77a9e02486) · [Coinbase 10](https://intel.arkm.com/explorer/address/0xA9D1e08C7793af67e9d92fe308d5697FB81d3E43)
- [Unverified] Founder death date; Jan 2027 tranche size; company revenue; Foundation filings; owners of the `0xEA57…` / `0x5240…` recipient Safes and of the five Coinbase accounts; "Coinbase Prime Custody" label on `0x90b1…` (Arkham only)

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer) or the label source (Arkham) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| **Red line:** 100.5M ONDO (≈ $43.7M) from Ondo's admin Safe, through middle Safe `0xEA57…`, into five Coinbase deposit addresses, 27 Aug – 13 Oct 2026 | Middle Safe [Etherscan](https://etherscan.io/address/0xEA5785e1727DE2Ba2CEfd102Cb2Dd91E018675e1) · [Arkham](https://intel.arkm.com/explorer/address/0xEA5785e1727DE2Ba2CEfd102Cb2Dd91E018675e1); sends: [27 Aug](https://etherscan.io/tx/0xbb656309edb5acdfe0e5694b20b3cf4b04cb50252d9df9dae81479ce9b1fc6ca) · [9 Sep](https://etherscan.io/tx/0x1a1d988d01373fa49d9dd843e7f53cf0205255538011417387b1ee95d4a74818) · [21 Sep](https://etherscan.io/tx/0x13df98ebcd46cb359d06022a5ae2631780a5e532e36fef7dd35c8546d3fb13f7) · [30 Sep](https://etherscan.io/tx/0xfd53e492a7e5e2f9b67ee25ce9c3dbed4597c2b83815e90b1dc2d181d4b57831) · [13 Oct](https://etherscan.io/tx/0xcc47888e5f6a89d10eae81026508f7b9602c31cc52af8bfe13de71cdf7a1042b) | A (chain) + 2× B labels | 15 Nov 2026 ~11:15 AM MST |
| **Pump-day send:** 18,196,018 ONDO on 21 Sep 2026 14:03 UTC (+31.8% 5-day) into Coinbase deposit `0x8119…1f46`, swept 4 min later | [send tx](https://etherscan.io/tx/0x13df98ebcd46cb359d06022a5ae2631780a5e532e36fef7dd35c8546d3fb13f7) · [sweep tx](https://etherscan.io/tx/0xcb2612aa97f6b20693de46c4df4220468a0f0c8328bbf13858d69b616741dd9f) · [deposit on Etherscan](https://etherscan.io/address/0x8119e9ffc2aca20b8a121792fe21149c1b7d1f46) · [Arkham “Coinbase Deposit”](https://intel.arkm.com/explorer/address/0x8119e9ffc2aca20b8a121792fe21149c1b7d1f46) | A + B | 15 Nov 2026 |
| The five receivers are Coinbase deposit addresses (all swept to Coinbase 10 within 3–5 min) | Sweeps: [27 Aug](https://etherscan.io/tx/0xa4a0211e989888dd183dca5c73b891b0b328d876c7fc4321cd203c84f716237f) · [9 Sep](https://etherscan.io/tx/0xfe18e59112479e1b21936c51cc16464979f2b24f20e83451a83ba9839ddada4c) · [21 Sep](https://etherscan.io/tx/0xcb2612aa97f6b20693de46c4df4220468a0f0c8328bbf13858d69b616741dd9f) · [30 Sep](https://etherscan.io/tx/0xbfe030e3f9c01bcf68ba5e5ea85cda7f0462a7e569efe2a35676e91959e14b31) · [13 Oct](https://etherscan.io/tx/0x81df2c582e943b0cdde341e3d42f448c3b2e6e3b5e69bd07ecd3367921a43348) · Coinbase 10 [Etherscan tag](https://etherscan.io/address/0xA9D1e08C7793af67e9d92fe308d5697FB81d3E43) · Arkham labels: [0x9532](https://intel.arkm.com/explorer/address/0x9532fc43f31a21b709f61c10413d875703da91d0) · [0x4857](https://intel.arkm.com/explorer/address/0x48576f7bccebf15381a4a11a42b277bbb8b4e7ff) · [0x8119](https://intel.arkm.com/explorer/address/0x8119e9ffc2aca20b8a121792fe21149c1b7d1f46) · [0xfca0](https://intel.arkm.com/explorer/address/0xfca06e6de9e8259342cff142e1e3821da8ed6175) · [0x2b47](https://intel.arkm.com/explorer/address/0x2b47bca4fa2e744231727ad9b8245f285ab760f9) | A pattern + 2× B | 15 Nov 2026 |
| `0xEA57…` is funded only by the admin Safe: 725M ONDO in five lots (22 Apr – 23 Sep 2026) | [22 Apr 125M](https://etherscan.io/tx/0x95b3e7409ba22bbac9e7157114ab83a8491d70a25dcaaecd2e9cd876784d9070) · [11 May 150M](https://etherscan.io/tx/0xe53c865f6e9fe67c1ece9a5edbd72696541e7011955c5f1ff6281ae3c01229c5) · [22 Jun 150M](https://etherscan.io/tx/0x33cca98b95a4141495fc7ae7d483e2472b7699e27ee528e265f22505e113d19b) · [21 Aug 150M](https://etherscan.io/tx/0xf84d62650ccacd6e4e98841fe86c1f961d984957873dc07f96610c206f8ae3d8) · [23 Sep 150M](https://etherscan.io/tx/0xaf248808b0611bc75d73db9d36f9c48be12144610aee61026471a7d732491256) | A | 15 Nov 2026 |
| Admin Safe `0x677F…A1A1` holds 5,179,207,574 ONDO (51.8%) and has MINTER / ADMIN roles; Arkham: "Ondo Finance: Gnosis Safe Proxy" | [Etherscan](https://etherscan.io/address/0x677FD4Ed8aE623f2f625DEB2D64F2070E46cA1A1) · [Arkham](https://intel.arkm.com/explorer/address/0x677FD4Ed8aE623f2f625DEB2D64F2070E46cA1A1) · token [contract](https://etherscan.io/address/0xfAbA6f8e4a5E8Ab82F62fe7C39859FA577269BE3) | A + B | 15 Nov 2026 |
| Same test-payer `0xd647…b176` precedes every `0xEA57…` payout (scheduled-payout pattern) | [Etherscan](https://etherscan.io/address/0xd64717976a3416e5add4c9740a96b90763b8b176) | A | 15 Nov 2026 |
| `0x5240…` → "Coinbase Prime Custody" `0x90b1…` 8.32M ONDO (10 Apr 2026), then on to `0x1d1d…` on a 16 Jul pump day | [10 Apr send](https://etherscan.io/tx/0x5541807cc730c536b47535cfd6edb8c5596d538b79909685c78a00e45f953747) · [16 Jul onward](https://etherscan.io/tx/0x12f827c16fe3564097d0bde007631d39e3528437a9c00dee1945dfe95bbc5b61) · [Arkham label (one source)](https://intel.arkm.com/explorer/address/0x90b1dd36e7379b85a16a898b35d8fe77a9e02486) | A + one B → label [Unverified] | 15 Nov 2026 |
| `0x5240…` received 1.548B ONDO from the admin Safe (2025 – Jan 2026) | [Etherscan](https://etherscan.io/address/0x524083970c7a1e62fbaa61d38781f87a4f191fd0) · [Arkham](https://intel.arkm.com/explorer/address/0x524083970c7a1e62fbaa61d38781f87a4f191fd0) | A | 15 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Whose Coinbase accounts got the 100.5M ONDO** (`0xEA57…` → 5 deposit addresses, incl. 18.2M on 21 Sep) | Ask Ondo for the `0xEA57…` payout list (investor / contributor / partner unlocks) and whether any Ondo entity holds a Coinbase account; look for a matching Coinbase Prime / Coinbase custody disclosure | Free (request) |
| 2 | **Owners of the ~30 Safes paid by `0xEA57…` and `0x5240…`** (11 of 33 `0xEA57…` sends were on pump days, ~6 expected) | Read each Safe's `getOwners()` and match signers across Safes and to `0xd6471797…` (the wallet that test-pays every recipient); Arkham / Nansen labels for each Safe; trace their onward sends to exchanges | Free (RPC) · Nansen paid |
| 3 | **Second label for `0x90b1…` (Arkham: Coinbase Prime Custody)** | Nansen or Etherscan label for the address | Nansen paid / free |
| 4 | **Where `0x1d1daecc…` took the 8.32M on 16 Jul (pump day)** | Etherscan `tokentx` for `0x1d1daecc…` and its next hop | Free |
| 5 | **Jan 2027 tranche size (1.71B vs 1.94B)** | Ondo Foundation governance post or a signed FIP-08 schedule | Free |
| 6 | **Who signs the 4-of-7 admin Safe** | Safe `getOwners()` plus Ondo disclosure; Arkham signer tags | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
