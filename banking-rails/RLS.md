---
ticker: RLS
name: Rayls
chain: ethereum
contract: "0xb5f7b021a78f470d31d762c1dda05ea549904fbd (Ethereum); 0x17ea10b6ae4fde59fdbf471bd28ab9710f508816 (BNB Chain)"
overall_score: 4.5
overall_verdict: FAIL
section_scores:
  revenue: 4
  foundation_team: 6
  insider_holdings: 3
  selling_behavior: 5
  tokenomics_supply: 3
  liquidity_market: 4
  product_development: 5
  adoption_customers: 4
  security_audits: 6
  regulatory: 6
  catalysts: 5
gates_failed: []
red_lines:
  hack_exploit: "none found"
  mint_path_live: "no: fixed 10B, 58.5M burned"
  team_wallet_to_exchange_during_pump: "no: foundation-Safe wallets sent ~325M RLS to GSR Markets, Gate, MEXC and Coinbase Prime in 2026 and ~105M at TGE, none on a pump day (MEXC closes); selling is disclosed policy"
  entity_concentration: "yes: ~79% of supply is foundation, investor, team or Parfin allocation"
methodology_effective: 2026-11-16
revenue_reaches_holders: "yes"
revenue_mechanism: "Network fees are converted to RLS and half is burned; 58.5M RLS has already been burned (total supply 9.94B), so a fee-funded burn reaches holders as reduced supply. It is small next to foundation sales."
pump_day_price_source: "MEXC RLSUSDT UTC daily closes"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions:
  - address: "0x60f0e09e51704ea6e472f877f849269eede76309"
    label: "Gnosis Safe (minter; signer tags)"
    confidence: high
    independent_corroboration: true
    basis: "Arkham + on-chain mint"
  - address: "0x3c9d7bb7f8a73d8839f880cac9d2d214d4d6b1e4"
    label: "Gnosis Safes; \"RLS Whale\" tags; no foundation label"
    confidence: medium
    independent_corroboration: false
    basis: "Arkham + on-chain funding from the minter Safe"
  - address: "0x7cb325d864eaa3012b9f6bc7c0fd8ac4074bc72c"
    label: "Gnosis Safes; \"RLS Whale\" tags; no foundation label"
    confidence: medium
    independent_corroboration: false
    basis: "Arkham + on-chain funding from the minter Safe"
  - address: "0x98733289d202782d3f748048722bd4402aee5495"
    label: "Gnosis Safes; \"RLS Whale\" tags; no foundation label"
    confidence: medium
    independent_corroboration: false
    basis: "Arkham + on-chain funding from the minter Safe"
  - address: "0x6129bc5dc8cc7ed6ae595421a176dc9a76d496b5"
    label: "Unlabelled EOA"
    confidence: low
    independent_corroboration: false
    basis: "Arkham"
  - address: "0xb48d639e81315e7b1956de81c7e05f3f19babecc"
    label: "GSR Markets (market maker)"
    confidence: medium
    independent_corroboration: false
    basis: "Arkham"
  - address: "0xe2ff350eeb6ef5b9b9e274c6c2b012013e292f5a"
    label: "Gnosis Safes, 1B RLS each; \"RLS Whale\""
    confidence: low
    independent_corroboration: false
    basis: "Arkham"
  - address: "0x3077e6d294c6a152c34aaf3a5fe415ec628cfb27"
    label: "Gnosis Safes, 1B RLS each; \"RLS Whale\""
    confidence: low
    independent_corroboration: false
    basis: "Arkham"
price_usd: 0.00159392
price_source: "CoinGecko, 16 Nov 2026 ~9:45 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### RLS · Overall grade **4.5 / 10 · ❌ FAIL**

**Summary:** Rayls is an institutional blockchain. Banks run private Rayls Sovereign chains that connect to a public chain, which launched on 30 Apr 2026. Every network fee is converted to RLS: half is burned and half pays validators. So far fees have bought back and burned 58.5M RLS. The foundation also unlocks ~73M RLS a month, says openly it sells some to fund operations, and its wallets have sent ~430M RLS to exchanges since launch, none on a pump day. About 79% of supply is still held by insiders. The token is down 95.6% from its December 2025 high.

**🚨 Top warning:** **steady foundation selling into a falling market.** Since the Dec 2025 launch, wallets funded by the foundation's Safe (4 signatures required) (`0x60f0…6309`) have sent about **430M RLS** to exchanges and a market maker (Kraken, Gate, Bitget, MEXC, Coinbase Prime; 90M to GSR Markets), including **165M in Nov 2026 alone** ([tx](https://etherscan.io/tx/0xb9a5a63b97e99654234767d0a0e74e8d450e7a8544e0380333a429a2ef066fb5)). Rayls discloses that the foundation may sell to cover costs ([mainnet post](https://www.rayls.com/blog/rayls-public-chain-mainnet-launches)). Investor and team unlocks of 81.7M a month start in May 2027 ([vesting update](https://www.rayls.com/blog/rayls-investors-and-team-extend-rls-vesting)). Every link is in the 🔗 Evidence trail below.

**Sections passed: 3 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 4/10 | ❌ FAIL |
| 🏛️ Foundation & team | 6/10 | ✅ PASS |
| 🪙 Foundation / team holdings | 3/10 | ❌ FAIL |
| 📉 Selling behavior | 5/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 3/10 | ❌ FAIL |
| 💧 Liquidity & market | 4/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 5/10 | ❌ FAIL |
| 🤝 Adoption & customers | 4/10 | ❌ FAIL |
| 🛡️ Security & audits | 6/10 | ✅ PASS |
| ⚖️ Regulatory | 6/10 | ✅ PASS |
| 📅 Catalysts & calendar | 5/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 RLS · Rayls · 4.5 / 10 · ❌ FAIL

> **One line:** An institutional chain with fee-funded burns, but a token dominated by foundation sales and a large insider overhang.

| 📊 Market (CoinGecko, 16 Nov 2026 ~9:45 AM MST) | 🔗 Chain (Etherscan, Rayls) |
|---|---|
| **Price** $0.001594 | **Supply** 2.11B circulating · 9.94B total (58.5M burned) · 10B max |
| **24h / 7d / 30d** 🔴 −1.4% / 🔴 −14.6% / 🔴 −17.6% | **Minter** foundation Gnosis Safe `0x60f0…6309` (4 signatures required) |
| **Market cap** $3.37M · **FDV** $15.8M | **Top holders** OFT bridge adapter 1.58B; 1-signer Safes 1.0B, 1.0B, 625M |
| **24h volume** $0.33M (Toobit, MEXC, Gate, Bitget, Coinbase, KCEX, Kraken) | **Unlocks** foundation ~73M a month now; investors and team 81.7M a month from May 2027 |
| **ATH** $0.0364 (2 Dec 2025) · now −95.6% | |
| **Pump days** 45 since listing (MEXC RLSUSDT; largest +245.6% on 28 Apr 2026, mainnet week) | |

---

## 💰 Revenue — Does it make money? · 4/10 · ❌ FAIL

- Rayls' private chains pay real fees. They are converted to RLS, and half is burned. 58.5M RLS has been burned so far ([vesting update](https://www.rayls.com/blog/rayls-investors-and-team-extend-rls-vesting), [tokenomics](https://www.rayls.com/blog/rayls-tokenomics-a-united-tradfi-defi-economy)). That's real value accrual, but it's small next to foundation sales. **4.**

- **Reaches holders (binary test, 16 Nov 2026 rules): Yes.** Network fees are converted to RLS and half is burned; 58.5M RLS has already been burned (total supply 9.94B), so a fee-funded burn reaches holders as reduced supply. It is small next to foundation sales.

## 🏛️ Foundation & team — Who is in charge? · 6/10 · ✅ PASS

- Built by Parfin, an operating fintech that serves institutional clients. Investors and team extended their vesting in Oct 2026.

## 🪙 Foundation / team holdings — How many coins do they hold? · 3/10 · ❌ FAIL

- Foundation 35%, investors 22%, team 17%, Parfin 11% ([tokenomics](https://www.rayls.com/blog/rayls-tokenomics-a-united-tradfi-defi-economy)). Only ~2.1B of 9.94B circulates.

## 📉 Selling behavior — Do insiders sell into pumps? · 5/10 · ❌ FAIL

- I traced the minter Safe and the top 17 holders two hops out, for transfers of 10M RLS or more. Foundation-funded wallets deposited ~105M at the TGE (30 Nov–4 Dec 2025, before the MEXC series begins) and ~325M across 2026: 90M to GSR Markets on 10 Feb (a market maker per Arkham, not Gate as first read), 30M on 6 Mar, 30M on 15 May, 10.3M to MEXC on 19 Oct, and 165M to Coinbase Prime on 4–16 Nov. All have status 1, and none fell on a pump day. Selling is disclosed policy → **5.** Deposits from the bridge adapter are user withdrawals and were excluded.
- **Arkham (16 Nov 2026):** the Coinbase Prime senders are generic **Gnosis Safes**, not labelled as the foundation's. [0x7cb3…c72c](https://intel.arkm.com/explorer/address/0x7cb325d864eaa3012b9f6bc7c0fd8ac4074bc72c) (tag "RLS Whale") sent 49M and 50M to Coinbase Prime Deposit 0x500 and 15M + 20M to Anchorage Digital (custody); [0x3c9d…b1e4](https://intel.arkm.com/explorer/address/0x3c9d7bb7f8a73d8839f880cac9d2d214d4d6b1e4) sent 26M and 40M to the same deposit, and its signer tag is the minter Safe [0x60f0…6309](https://intel.arkm.com/explorer/address/0x60f0e09e51704ea6e472f877f849269eede76309). 0x3c9d is fed 72.917M at a time by [0x9873…5495](https://intel.arkm.com/explorer/address/0x98733289d202782d3f748048722bd4402aee5495) ("RLS Whale"), matching the disclosed ~73M monthly foundation unlock. The 90M of 10 Feb went from [0x6129…96b5](https://intel.arkm.com/explorer/address/0x6129bc5dc8cc7ed6ae595421a176dc9a76d496b5) (unlabelled, funded by the minter Safe) to **GSR Markets** [0xb48d…becc](https://intel.arkm.com/explorer/address/0xb48d639e81315e7b1956de81c7e05f3f19babecc) ([tx](https://etherscan.io/tx/0x15e82533f608e2127bff0cbd07f7cf48699e24e19044e1bb9cf81e741cd98eab)). The foundation link rests on on-chain funding from the minter Safe and the unlock cadence, not on an Arkham label; none of these moves fell on a pump day, so the score is unchanged. [Tier B] Arkham, read 16 Nov 2026 (signed-in account).

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from MEXC RLSUSDT UTC daily closes.

## 📊 Tokenomics & supply · 3/10 · ❌ FAIL

- Foundation unlocks of ~73M a month (10% burned since Apr 2026) plus investor and team unlocks from May 2027 add up to more than 1.5B RLS a year, against 2.1B circulating.

## 💧 Liquidity & market · 4/10 · ❌ FAIL

- Listed on Coinbase, Kraken, Bitget, Gate and MEXC, but only $0.33M a day.

## 🧑‍💻 Product & development · 5/10 · ❌ FAIL

- Public chain mainnet went live on 30 Apr 2026 ([mainnet post](https://www.rayls.com/blog/rayls-public-chain-mainnet-launches)), alongside private Sovereign chains and the Enygma privacy framework.

## 🤝 Adoption & customers · 4/10 · ❌ FAIL

- Fee usage from private chains is published on a transparency portal. Not independently sized.

## 🛡️ Security & audits · 6/10 · ✅ PASS

- No exploit found. Minting is closed, and the minter Safe needs 4 signatures.

## ⚖️ Regulatory · 6/10 · ✅ PASS

- Aimed at regulated institutions. No enforcement found.

## 📅 Catalysts & calendar · 5/10 · ❌ FAIL

- A DAO handover, the Parfin unlock (Dec 2027) and investor and team unlocks from May 2027.

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | 🟢 No: ~430M RLS deposited, none on pump days (disclosed policy) |
| Live mint path | 🟢 None (fixed supply) |
| Entity concentration | 🔴 ~79% insider-allocated |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| [0x60f0…6309](https://intel.arkm.com/explorer/address/0x60f0e09e51704ea6e472f877f849269eede76309) | Gnosis Safe (minter; signer tags) | Arkham + on-chain mint | high (on-chain minter) | yes (on-chain) | Sets the foundation origin |
| [0x3c9d…b1e4](https://intel.arkm.com/explorer/address/0x3c9d7bb7f8a73d8839f880cac9d2d214d4d6b1e4), [0x7cb3…c72c](https://intel.arkm.com/explorer/address/0x7cb325d864eaa3012b9f6bc7c0fd8ac4074bc72c), [0x9873…5495](https://intel.arkm.com/explorer/address/0x98733289d202782d3f748048722bd4402aee5495) | Gnosis Safes; "RLS Whale" tags; no foundation label | Arkham + on-chain funding from the minter Safe | medium | on-chain flows only | None (no pump-day deposit) |
| [0x6129…96b5](https://intel.arkm.com/explorer/address/0x6129bc5dc8cc7ed6ae595421a176dc9a76d496b5) | Unlabelled EOA | Arkham | low | no | None |
| [0xb48d…becc](https://intel.arkm.com/explorer/address/0xb48d639e81315e7b1956de81c7e05f3f19babecc) | GSR Markets (market maker) | Arkham | medium | no | Corrects "Gate" to market maker; no score change |
| [0xe2ff…2f5a](https://intel.arkm.com/explorer/address/0xe2ff350eeb6ef5b9b9e274c6c2b012013e292f5a), [0x3077…fb27](https://intel.arkm.com/explorer/address/0x3077e6d294c6a152c34aaf3a5fe415ec628cfb27) | Gnosis Safes, 1B RLS each; "RLS Whale" | Arkham | low | no | None |

## 📚 Sources

- [Tier B] Arkham, read 16 Nov 2026 (signed-in account): the minter Safe, the Coinbase Prime senders, the 1B-RLS Safes and the GSR Markets recipient; dates from Etherscan
- [Tier A] [Rayls tokenomics](https://www.rayls.com/blog/rayls-tokenomics-a-united-tradfi-defi-economy), [Vesting extension](https://www.rayls.com/blog/rayls-investors-and-team-extend-rls-vesting), [Parfin lock-up](https://www.rayls.com/blog/parfin-extends-rls-lock-up-by-one-year-and-migrates-allocation-onchain-to-rayls), [Mainnet launch](https://www.rayls.com/blog/rayls-public-chain-mainnet-launches)
- [Tier A] Etherscan transfers, Safe thresholds and holders for `0xb5f7…bd`
- [Tier B] [The Industry Spread on the unlock shift](https://theindustryspread.com/rayls-unlock-shifts-insider-vesting/)
- [Tier A] CoinGecko `rayls` (market, venues); pump days from MEXC RLSUSDT daily closes

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| 90M RLS → GSR Markets (Arkham label), 10 Feb 2026 | [tx](https://etherscan.io/tx/0x15e82533f608e2127bff0cbd07f7cf48699e24e19044e1bb9cf81e741cd98eab) | A | 16 Nov 2026 |
| 50M RLS → Coinbase Prime, 11 Nov 2026 | [tx](https://etherscan.io/tx/0x27346214b9c699df56b117d8a44506e16d7b821f239f26f0da7b3b8f55dfbfd9) | A | 16 Nov 2026 |
| 49M RLS → Coinbase Prime, 16 Nov 2026 | [tx](https://etherscan.io/tx/0xb9a5a63b97e99654234767d0a0e74e8d450e7a8544e0380333a429a2ef066fb5) | A | 16 Nov 2026 |
| 40M RLS → Coinbase Prime, 4 Nov 2026 | [tx](https://etherscan.io/tx/0x8aabd2adff2711eae995d7392bc35fdaecbfc3e69d62a0fb362fde9fea26f72b) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Owners of the 1-signer Safes `0xe2ff…2f5a`, `0x3077…fb27` and `0x9873…5495`** (foundation, investors or team?) | Arkham (16 Nov 2026) tags them only "RLS Whale"; ask Rayls to publish its wallet map | Free |
| 2 | **Fee revenue in USD** | Rayls transparency portal (browser) | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.

- Research only. Not investment advice.
