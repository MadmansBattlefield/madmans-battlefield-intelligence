---
ticker: REUSD
name: Re Protocol reUSD
chain: ethereum
contract: "0x5086bf358635b81d8c47c66d1c8b9e567db70c72"
overall_score: 5.5
overall_verdict: FAIL
section_scores:
  revenue: 7
  foundation_team: 5
  insider_holdings: 6
  selling_behavior: 4
  tokenomics_supply: 6
  liquidity_market: 4
  product_development: 6
  adoption_customers: 6
  security_audits: 7
  regulatory: 4
  catalysts: 5
gates_failed: []
red_lines:
  hack_exploit: "none found"
  mint_path_live: "yes by design: minted against deposits, burned on redemption"
  team_wallet_to_exchange_during_pump: "not proven: NAV token with no pump days; issuer mint/redeem flows not traced"
  entity_concentration: "largest holders are DeFi protocols (Fluid, Morpho); issuer controls mint and redemption"
price_usd: 1.11
price_source: "CoinGecko, 16 Nov 2026 ~8:52 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### REUSD · Overall grade **5.5 / 10 · ❌ FAIL**

**Summary:** reUSD is the senior tranche of Re Protocol, which takes real reinsurance risk on-chain. It earns about SOFR + 2.5% off-chain (sUSDe + 2.5% on-chain), and its value grows in a NAV that started at $1.00 and is now $1.11. It is the strongest coin in this batch: real yield, daily third-party reserve attestations and three audits. It fails at 5.5 because liquidity is thin for a $366M token, the regulatory setup of an offshore reinsurance vehicle is untested, and holders depend on the issuer to redeem.

**🚨 Top warning:** exit depends on the issuer and two DeFi pools. There was **$1.73M** of 24h trading volume (Fluid, Curve) against a **$366M** market cap. In a reinsurance loss event, the reinsurer's equity (~$77M) and the reUSDe tranche absorb losses first. After that, reUSD holders would need redemption from Re or would sell into pools of that size. The docs describe the loss order; Etherscan shows the DeFi holdings. Every link is in the 🔗 Evidence trail below.

**Sections passed: 6 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 7/10 | ✅ PASS |
| 🏛️ Foundation & team | 5/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 6/10 | ✅ PASS |
| 📉 Selling behavior | 4/10 | ❌ FAIL (not proven) |
| 📊 Tokenomics & supply | 6/10 | ✅ PASS |
| 💧 Liquidity & market | 4/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 6/10 | ✅ PASS |
| 🤝 Adoption & customers | 6/10 | ✅ PASS |
| 🛡️ Security & audits | 7/10 | ✅ PASS |
| ⚖️ Regulatory | 4/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 5/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 REUSD · Re Protocol reUSD · 5.5 / 10 · ❌ FAIL

> **One line:** Real reinsurance yield with proper attestations, but thin exits for a $366M token.

| 📊 Market (CoinGecko, 16 Nov 2026 ~8:52 AM MST) | 🔗 On-chain ([Etherscan](https://etherscan.io/token/0x5086bf358635b81d8c47c66d1c8b9e567db70c72), 16 Nov 2026 ~9:10 AM MST) |
|---|---|
| **NAV / price** $1.11 | **Ethereum supply** 308,901,942 reUSD |
| **24h / 30d** +0.04% / +0.38% | **Circulating (all chains, CoinGecko)** 328.9M |
| **Market cap** $365.9M | **Fluid Liquidity** 36.5M · **Morpho** 9.3M |
| **24h volume** $1.73M (Fluid, Curve) | **Protocol TVL** $799M (31 Oct 2026) |
| **CoinGecko low** $0.873 (17 Jul 2025) [Unverified: likely thin early print] | |

---

## 💰 Revenue — Does it make money? · 7/10 · ✅ PASS

- Yield comes from reinsurance premiums and collateral return: SOFR + 250 bps off-chain, sUSDe + 250 bps on-chain ([About reUSD](https://docs.re.xyz/products/about-reusd)). NAV is up 11% since launch.

## 🏛️ Foundation & team — Who is in charge? · 5/10 · ❌ FAIL

- Re Protocol runs the issuer and works with a licensed reinsurer. Leaders are described by role only. The full legal structure was not reviewed [Unverified].

## 🪙 Foundation / team holdings — How many coins do they hold? · 6/10 · ✅ PASS

- The largest on-chain holders are DeFi protocols (Fluid Liquidity, Morpho). No large issuer-held float was found. Arkham ([Tier B] Arkham, read 16 Nov 2026 (signed-in account)) labels [0x52aa](https://intel.arkm.com/explorer/address/0x52aa899454998be5b000ad077a46bbe360f4e497) **Fluid (Instadapp): FluidLiquidityProxy** and shows 40.7M reUSD there across networks; Etherscan shows 36.53M on Ethereum. Its page-1 transfers are small live swaps (up to ~47K) through aggregators and Fluid DEX, with no large exits.

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL (not proven)

- Arkham ([Tier B] Arkham, read 16 Nov 2026 (signed-in account)) labels the token contract [0x5086](https://intel.arkm.com/explorer/address/0x5086bf358635b81d8c47c66d1c8b9e567db70c72) as the Re Protocol Deposit Token and shows no transfers for it, so issuer mint and redemption flows are not visible there either.
- reUSD is a NAV token. Its price only accrues, so it has no pump days, and the pump-day test can't show either selling or the absence of it. Insider exits would happen through issuer redemptions or pool sales, which I did not trace. Under the repo's rule, selling that can't be traced is **not proven → 4.**
- **Alternative:** if value-accruing tokens with no pump days are treated as "not applicable" and scored 6, Selling passes. The overall would then be 5.8, still ❌ FAIL, with no gate failed. No existing report in this folder covers a NAV or stable token, so the stricter score is used here.

## 📊 Tokenomics & supply · 6/10 · ✅ PASS

- Supply is minted against deposits and burned on redemption. Holders are protected by the loss order: reinsurer equity (~$77M), then reUSDe, then reUSD ([FAQ](https://docs.re.xyz/getting-started-with-re/faq)).

## 💧 Liquidity & market · 4/10 · ❌ FAIL

- $1.73M of 24h volume, about 0.5% of market cap. Exits mostly depend on issuer redemption.

## 🧑‍💻 Product & development · 6/10 · ✅ PASS

- Live on Ethereum, with contracts listed in the docs ([smart contracts](https://docs.re.xyz/products/smart-contracts)).

## 🤝 Adoption & customers · 6/10 · ✅ PASS

- $799M protocol TVL (31 Oct 2026). Integrated with Pendle, Morpho and Fluid.

## 🛡️ Security & audits · 7/10 · ✅ PASS

- Audits by Sherlock, Certora and Hacken. Off-chain reserves are attested daily by The Network Firm and published on-chain through Chainlink ([audits and attestations](https://docs.re.xyz/transparency-and-data-show-me-the-receipts/audits-attestations-custody-structure)). No exploit found.

## ⚖️ Regulatory · 4/10 · ❌ FAIL

- A tokenised, yield-bearing reinsurance claim sold to on-chain buyers. How securities and insurance rules apply is untested [Unverified].

## 📅 Catalysts & calendar · 5/10 · ❌ FAIL

- Reinsurance renewal seasons and catastrophe-loss periods are the main risk dates. No token unlocks.

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | ⚪ Not proven (NAV token, no pump days; redemptions not traced) |
| Live mint path | 🟠 Issuer mint and redemption by design |
| Entity concentration | 🟠 Exits depend on the issuer and a few DeFi pools |

## 📚 Sources

- [Tier A] [Re docs: About reUSD](https://docs.re.xyz/products/about-reusd), [FAQ](https://docs.re.xyz/getting-started-with-re/faq), [Smart contracts](https://docs.re.xyz/products/smart-contracts), [Audits / attestations](https://docs.re.xyz/transparency-and-data-show-me-the-receipts/audits-attestations-custody-structure)
- [Tier A] Etherscan token supply and holders; CoinGecko `re-protocol-reusd`
- [Tier B] Arkham, read 16 Nov 2026 (signed-in account): Re Protocol Deposit Token label on the token contract (no transfers shown); Fluid (Instadapp) FluidLiquidityProxy holding 40.7M

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Senior tranche, loss order | [About reUSD](https://docs.re.xyz/products/about-reusd) | A | 16 Nov 2026 |
| Daily attestation via Chainlink | [Audits / attestations](https://docs.re.xyz/transparency-and-data-show-me-the-receipts/audits-attestations-custody-structure) | A | 16 Nov 2026 |
| Supply and holders | [Etherscan](https://etherscan.io/token/0x5086bf358635b81d8c47c66d1c8b9e567db70c72#balances) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Redemption terms (notice period, gates)** | Read the redemption section of the docs | Free |
| 2 | **Legal wrapper and licensing** | Read the custody-structure page and the reinsurer's filings | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.

- Research only. Not investment advice.
