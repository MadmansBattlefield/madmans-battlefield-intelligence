---
ticker: MBG
name: MBG By MultiBank Group
chain: ethereum
contract: "0x45e02bc2875a2914c4f585bbf92a6f28bc07cb70"
overall_score: 3.9
overall_verdict: FAIL
section_scores:
  revenue: 3
  foundation_team: 5
  insider_holdings: 3
  selling_behavior: 4
  tokenomics_supply: 4
  liquidity_market: 3
  product_development: 5
  adoption_customers: 4
  security_audits: 6
  regulatory: 5
  catalysts: 3
gates_failed: [revenue]
red_lines:
  hack_exploit: "none found"
  mint_path_live: "no (no mint function; 1B minted once on 13 Jul 2025)"
  team_wallet_to_exchange_during_pump: "small: allocation distributors sent <0.5M MBG on pump days; ~49M MBG flowed through an unlabelled trading hub (OKX and Wintermute deposit counterparties) in 365d"
  treasury_in_single_key_wallets: "yes, 7 EOAs hold ~452M MBG (46%); vesting vault 338.5M has a salvage role"
price_usd: 0.101719
price_source: "CoinGecko, 16 Nov 2026 8:34 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### MBG · Overall grade **3.9 / 10 · ❌ FAIL**

**Summary:** MBG is the utility token of MultiBank Group, a large CFD and FX broker. The group reports $362M of 2024 revenue (company white paper, not audited here) and promised up to **$58.2M of MBG buybacks in year one** and $440M over five years. On-chain there have been only two burns in 16 months: [4.86M MBG on 27 Aug 2025](https://etherscan.io/tx/0x29fec376927e337f79ba4db2c74791984a4206d38c12af799cc69586d3560af8) and [17.63M MBG on 8 May 2026](https://etherscan.io/tx/0x18e904e19ebe2f3818916afe7df5708cbce7bcf8164ca7939d4aceace9e760ec), about $16.6M at the closes on those days. The second burn's tokens came **from an allocation wallet funded by the vesting vault, not from visible market buying** ([funding tx](https://etherscan.io/tx/0x78486bb588b3295a436826148f193ff6624760c678020c6d15d01b16bf934b95)). The price is down 96% from its Jul 2025 ATH and 78% in a year. Monthly unlocks of 2–2.4% of supply run through 2027, and 97% of exchange volume is on BingX. Revenue trips the hard gate.

**🚨 Top warning:** The "buyback" cannot be told apart from burning treasury tokens. The May 2026 burn of 17.63M MBG went vesting-vault payout → [`0x8D2e…A70E`](https://etherscan.io/address/0x8D2e6580c64654D7fa6dEc98E728Ac1F0e52A70E) → [[`0xE8d3…28cB`](https://etherscan.io/address/0xE8d399554937dB18E89b45fC6D032A31B14828cB)](https://etherscan.io/tx/0xd06a1518d2c661b2938a4fcb6561b28d7ad96a16bb3a1a03750c5ab01c6a6bb1) → deployer [`0x3b55…6376`](https://etherscan.io/address/0x3b5593322b63e96457b1da2dea7f53d7100c6376) → [zero address](https://etherscan.io/tx/0x18e904e19ebe2f3818916afe7df5708cbce7bcf8164ca7939d4aceace9e760ec). Meanwhile allocation distributors fed **~49M MBG (13% of circulating) in the last year** into the unlabeled high-volume hub [`0xf972…c241`](https://etherscan.io/address/0xf97271e1e37308e197679e3aa017c8595a45c241) (11,870 transactions, mostly USDC/USDT). Arkham leaves it unlabelled, but it pays into OKX and Wintermute (market maker) deposit addresses, so it is a trading wallet, not an exchange [owner Unverified].

**Sections passed: 1 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 3/10 | ❌ FAIL |
| 🏛️ Foundation & team | 5/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 3/10 | ❌ FAIL |
| 📉 Selling behavior | 4/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 4/10 | ❌ FAIL |
| 💧 Liquidity & market | 3/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 5/10 | ❌ FAIL |
| 🤝 Adoption & customers | 4/10 | ❌ FAIL |
| 🛡️ Security & audits | 6/10 | ✅ PASS |
| ⚖️ Regulatory | 5/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 3/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 MBG · MBG By MultiBank Group · 3.9 / 10 · ❌ FAIL

> **One line:** A real broker behind the token, but the promised revenue buyback is mostly missing, and insider allocations keep streaming into an unlabelled trading hub.

| 📊 Market (CoinGecko, 16 Nov 2026 8:34 AM MST) | 🔗 On-chain (Ethereum, 16 Nov 2026) |
|---|---|
| **Price** $0.1017 · 24h / 7d / 30d 🔴 +0.4% / −0.9% / −2.6% · 1y −78.0% | **ERC-20** [`0x45e0…cb70`](https://etherscan.io/address/0x45e02bc2875a2914c4f585bbf92a6f28bc07cb70) · 977,514,798 supply (1B minted, 22.49M burned) |
| **Market cap** $37.1M · **FDV** $99.4M · rank #499 | **Circulating** 364.7M (CoinGecko) · 5,284 holders (Blockscout) |
| **24h volume** $4.45M: BingX $4.32M (97%), MEXC $0.65M; Uniswap $136 | **Vesting vault** [`0x11dF…Ebb7`](https://etherscan.io/address/0x11dFF0780c79e1E866e8961D7993D1172B8eEbb7) 338.53M |
| **ATH** $2.56 (23 Jul 2025) · now −96.0% | **Owner / deployer** [`0x3b55…6376`](https://etherscan.io/address/0x3b5593322b63e96457b1da2dea7f53d7100c6376) (EOA) |

---

## 💰 Revenue — Does it make money? · 3/10 · ❌ FAIL

| Item | Value | Source |
|---|---:|---|
| Group revenue 2024 / H1 2025 | ~$362M / $209M | [Tier B ×2] [MultiBank news](https://multibankfx.com/en/about/company-news/multibank-group-completed-first-mbg-buyback-and-burn-removing-4-86-m-tokens-after-record-h1-2025-financial-results) · [Gate Learn](https://www.gate.com/learn/articles/mbg-by-multibank-group-ushering-in-a-new-era-of-smart-finance/10566) (company figures, unaudited here) |
| Promised buyback | up to $58.2M in year 1; $440M over 5 years | [Tier A] [MultiBank announcement, 27 Aug 2025](https://multibankfx.com/en/about/company-news/multibank-group-completed-first-mbg-buyback-and-burn-removing-4-86-m-tokens-after-record-h1-2025-financial-results) |
| Burn 1 | 4,860,000 MBG, 27 Aug 2025 (≈$11.2M at the $2.30 close) | [Tier A] [tx](https://etherscan.io/tx/0x29fec376927e337f79ba4db2c74791984a4206d38c12af799cc69586d3560af8) |
| Burn 2 | 17,625,202 MBG, 8 May 2026 (≈$5.4M at the $0.305 close) | [Tier A] [tx](https://etherscan.io/tx/0x18e904e19ebe2f3818916afe7df5708cbce7bcf8164ca7939d4aceace9e760ec) |

- **Where burn 2 came from:** the vesting-vault-funded wallet [`0xE8d3…28cB`](https://etherscan.io/address/0xE8d399554937dB18E89b45fC6D032A31B14828cB) sent exactly 17,625,202 MBG to the deployer the same day ([tx](https://etherscan.io/tx/0x78486bb588b3295a436826148f193ff6624760c678020c6d15d01b16bf934b95)). That wallet's only earlier inflows were allocation transfers. No DEX or exchange purchase is visible.
- Token holders have no claim on group revenue. MBG gives fee discounts, staking and access perks.

**What it means:** ~$16.6M burned in 16 months against a $58.2M year-1 promise, with the latest burn sourced from allocations. **3 (hard gate).**

## 🏛️ Foundation & team — Who is in charge? · 5/10 · ❌ FAIL

- MultiBank Group: founded 2005, headquartered in the UAE, reports 18 regulatory licences and 2M clients [Tier B ×2, company white paper via Gate Learn and MultiBank site].
- The token is issued by a single deployer EOA with an `owner` role; no multisig governance.

## 🪙 Foundation / team holdings — How many coins do they hold? · 3/10 · ❌ FAIL

| Wallet | MBG | % of supply | Control |
|---|---:|---:|---|
| [`0x11dF…Ebb7`](https://etherscan.io/address/0x11dFF0780c79e1E866e8961D7993D1172B8eEbb7) [VestingVault](https://intel.arkm.com/explorer/address/0x11dFF0780c79e1E866e8961D7993D1172B8eEbb7) | 338.53M | 34.6% | Contract with `SALVAGE_ROLE` / `salvageERC20` and `cancelSchedule` |
| [`0xbfFB…0827`](https://etherscan.io/address/0xbfFBE2cb8866115440659b3b4A5B6EA484a70827) | 203.84M | 20.9% | EOA (single key) |
| [`0xE4E3…c432`](https://etherscan.io/address/0xE4E3A86AF9B8CE57df8707d330410cb923E3c432) | 78.83M | 8.1% | EOA, dormant |
| [`0xd419…f6d6`](https://etherscan.io/address/0xd41975feF5C9861F0A1aC74725234C161764f6d6) | 46.26M | 4.7% | EOA, distributor |
| [`0xE8d3…28cB`](https://etherscan.io/address/0xE8d399554937dB18E89b45fC6D032A31B14828cB) | 37.93M | 3.9% | EOA, funded burn 2 |
| [`0xCF8D…1af5`](https://etherscan.io/address/0xCF8D130CEbA6C4C0e8d48D1ed2452AB45AE11af5) | 33.33M | 3.4% | EOA |
| [`0x8D2e…A70E`](https://etherscan.io/address/0x8D2e6580c64654D7fa6dEc98E728Ac1F0e52A70E) | 27.78M | 2.8% | EOA |
| [`0x46D4…aF7F`](https://etherscan.io/address/0x46D4409dc368060889D35f03c45D29360f85aF7F) | 24.20M | 2.5% | EOA (received 50M at launch) |

*Balances: Blockscout holders API; contract / EOA status from `eth_getCode`, 16 Nov 2026. All but the vault were funded directly by the deployer on 14 Jul 2025 or by the vault.* Arkham ([Tier B] Arkham, read 16 Nov 2026 (signed-in account)) tags the large wallets only "MBG Whale"; the deployer and burn executor `0x3b55…6376` is unlabelled. `0xd419…f6d6` pays many small amounts to many addresses, like a rewards distributor.

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL

*Gate MBG/USDT daily closes (UTC): 18 pump days in the last 365.*

- **Pump-day outflows:** the distributor `0xd419…f6d6` and allocation wallets `0x09c8…e21e` and `0xde32…a83d` made 15 small transfers on 20 Jan, 20–23 Feb 2026 and other pump days (~0.5M MBG total, under $0.2M). Examples: [162,500 MBG on 20 Jan 2026](https://etherscan.io/tx/0x2d0ce412d1b601d4e9cf23fce628cafa1cedee12c536aee8b3110abee9b6ba73) and [93,941 MBG to the hub on 22 Feb 2026](https://etherscan.io/tx/0xacf23995b472c0be1109578f436c134a818d659ee341f695854803b4f88f4ebd).
- **Steady flow to an exchange-like hub:** [`0xf972…c241`](https://etherscan.io/address/0xf97271e1e37308e197679e3aa017c8595a45c241) received ~15.0M from `0xde32…`, 9.9M from `0x09c8…` and 15.0M from `0xf7cc…`. It then sent 45.5M onward to `0x824b…79b0da`. It has 11,870 transactions and mostly USDC/USDT flows. **Correction:** Arkham leaves both `0xf972` and `0x824b` unlabelled, and both pay stablecoins into **OKX deposit** addresses, and `0xf972` also into a **Wintermute deposit** address. An exchange's own hot wallet wouldn't normally do that, so these are trading wallets, not an exchange [owner Unverified]. `0x824b` sent 40.1M MBG back to `0x5f66…cfc9`, the funder of the 78.8M allocation wallet `0xE4E3`, so part of the flow loops back into allocation wallets.

**What it means:** no large dumps timed to pumps, but a constant flow of allocation tokens into an unlabelled trading hub with OKX and market-maker counterparties. Not proven clean → **4**.

## 📊 Tokenomics & supply · 4/10 · ❌ FAIL

- 1B minted once; no mint function (Blockscout verified source). Tax, reflection and deflation switches exist but revert, because the token was deployed with those features off.
- 57.4% released by 1 Nov 2026. Monthly unlocks of 23.6M (Dec 2026, Jan 2027), then 20.5M a month to Aug 2027 and 8.3M after, ending Apr 2029 [Tier B ×2] ([NAUT](https://naut.so/unlocks/multibankgroup) · [RootData via ChainCatcher](https://www.chaincatcher.com/en/article/2304864)).
- Unlocks of ~2.2% of supply a month exceed recent burns several times over.

## 💧 Liquidity & market · 3/10 · ❌ FAIL

- $4.45M of 24h volume, 97% on BingX; Uniswap V3 pool volume is $136 a day. Depth is effectively one exchange.
- −96% from ATH in 16 months.

## 🧑‍💻 Product & development · 5/10 · ❌ FAIL

- The MBG utility spans MultiBank TradFi, the MEX institutional ECN, the MultiBank.io crypto exchange and RWA tokenisation on Mavryk [Tier B]. No public GitHub.

## 🤝 Adoption & customers · 4/10 · ❌ FAIL

- The broker is large (2M clients claimed) but MBG usage (staking, fee discounts) is not published. 5,284 on-chain holders.

## 🛡️ Security & audits · 6/10 · ✅ PASS

- No exploit found. The token is a standard generator template with no mint; owner-settable fees revert.
- The vesting vault's admin can `salvageERC20` and `cancelSchedule`, so admin keys can move locked tokens [inference from verified ABI].

## ⚖️ Regulatory · 5/10 · ❌ FAIL

- A regulated broker group (multiple licences, Tier B). MBG is a utility token with no equity rights. No enforcement action against MBG found.

## 📅 Catalysts & calendar · 3/10 · ❌ FAIL

| Date | Event |
|---|---|
| 22 Nov / 1 Dec 2026 | Monthly unlock ~23.6–25M MBG (≈2.4%) |
| 1 Jan 2027 | 23.6M unlock |
| Feb–Aug 2027 | 20.5M a month |
| Unscheduled | Further burns (none dated) |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | 🟡 Small pump-day transfers (<0.5M MBG); steady ~49M a year to an unlabelled trading hub |
| Live mint path | 🟢 None |
| Treasury in single-key wallets | 🔴 ~452M MBG in 7 EOAs; vault admin can salvage |

## 📚 Sources

- [Tier A] Etherscan v2 token transfers and Blockscout holders, smart-contract and address APIs for the MBG contract and top wallets, read 16 Nov 2026 ~10:30 AM MST
- [Tier A] Ethereum RPC `eth_call` (`owner`, `isTaxable`, `taxBPS`) and `eth_getCode`
- [Tier B] [MultiBank burn announcement](https://multibankfx.com/en/about/company-news/multibank-group-completed-first-mbg-buyback-and-burn-removing-4-86-m-tokens-after-record-h1-2025-financial-results) · [Gate Learn](https://www.gate.com/learn/articles/mbg-by-multibank-group-ushering-in-a-new-era-of-smart-finance/10566) · [NAUT unlocks](https://naut.so/unlocks/multibankgroup) · [ChainCatcher](https://www.chaincatcher.com/en/article/2304864)
- [Tier A] CoinGecko `mbg-by-multibank-group` (16 Nov 2026 8:34 AM MST); Gate MBG/USDT daily candles
- [Tier B] Arkham, read 16 Nov 2026 (signed-in account): VestingVault label; MBG Whale tags; hub `0xf972` and `0x824b` unlabelled, with OKX Deposit and Wintermute Deposit counterparties
- [Unverified] owner of the hub `0xf972…c241`

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Burn 1: 4.86M MBG | [tx](https://etherscan.io/tx/0x29fec376927e337f79ba4db2c74791984a4206d38c12af799cc69586d3560af8) | A | 16 Nov 2026 |
| Burn 2: 17.63M MBG | [tx](https://etherscan.io/tx/0x18e904e19ebe2f3818916afe7df5708cbce7bcf8164ca7939d4aceace9e760ec) | A | 16 Nov 2026 |
| Burn 2 funded by an allocation wallet | [tx](https://etherscan.io/tx/0x78486bb588b3295a436826148f193ff6624760c678020c6d15d01b16bf934b95) | A | 16 Nov 2026 |
| Vault holds 338.5M; salvage role | [contract](https://etherscan.io/address/0x11dFF0780c79e1E866e8961D7993D1172B8eEbb7) | A | 16 Nov 2026 |
| Allocations to the hub | [hub](https://etherscan.io/address/0xf97271e1e37308e197679e3aa017c8595a45c241) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Who runs the trading hub** | Arkham (16 Nov 2026) leaves `0xf972` and `0x824b` unlabelled. Ask MultiBank whether they belong to its market maker or to MultiBank.io | Free |
| 2 | **Where the 40.7M MBG sent to `0x20c6…12bd` went** | Trace `0x20c6` onward on Etherscan | Free |
| 3 | **Burn funding** | Ask MultiBank for buyback fills behind the May 2026 burn | Free |
| 4 | **Who holds the vault admin roles** | Read `getRoleMember` on the vault for SALVAGE / DEFAULT_ADMIN | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
