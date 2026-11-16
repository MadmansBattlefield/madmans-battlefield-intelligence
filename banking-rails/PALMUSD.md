---
ticker: PALMUSD
name: Palm USD (PUSD)
chain: ethereum
contract: "0xfaf0cee6b20e2aaa4b80748a6af4cd89609a3d78"
overall_score: 2.6
overall_verdict: FAIL
section_scores:
  revenue: 1
  foundation_team: 3
  insider_holdings: 2
  selling_behavior: 5
  tokenomics_supply: 3
  liquidity_market: 1
  product_development: 4
  adoption_customers: 1
  security_audits: 4
  regulatory: 3
  catalysts: 3
gates_failed: [revenue]
red_lines:
  hack_exploit: "none found"
  mint_path_live: "yes; OPERATOR_ROLE can mint, and ADMIN_ROLE can upgrade the contract (UUPS)"
  team_wallet_to_exchange_during_pump: "none found: a $1 stablecoin has no pump days, and the Treasury has made no exchange deposits"
  one_hop_sale_status: none_found
  entity_concentration: "the Treasury and one wallet it funded hold 2.72B of 2.83B PUSD (96%) on Ethereum; 46 holders"
price_usd: null
price_source: "No exchange market found; not listed on CoinGecko (16 Nov 2026 ~1:30 PM MST)"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "none; a stablecoin with no yield, so reserve income stays with the issuer"
pump_day_price_source: "none: no exchange-native PUSD series exists (Binance, Gate, MEXC, KuCoin and Kraken have no pair; CoinGecko doesn't list it)"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions:
  - address: "0x4b3974aaabdc251b3086ae4a8163110d766c88c8"
    label: "PUSD Treasury"
    confidence: high
    independent_corroboration: true
    basis: "returned by the contract's own treasuryAddress() call, and received the 2.8B mint from the zero address"
  - address: "0x1760bfb0f8461fcf4c6768a82436840d23f40252"
    label: "unlabelled wallet funded by the Treasury"
    confidence: low
    independent_corroboration: false
    basis: "all 1.37B came from the Treasury in Dec 2025; no label and no Arkham pass, so it cannot move Holdings on its own"
  - address: "0x6d3174d8fa8a24d19253e8b479c5ab58d0a2e898"
    label: "OPERATOR_ROLE holder (minter)"
    confidence: high
    independent_corroboration: false
    basis: "RoleGranted event on the token contract"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### PALMUSD · Overall grade **2.6 / 10 · ❌ FAIL**

**Summary:** Palm USD (PUSD) is a stablecoin pitched as Shariah-compliant and backed by AED and SAR reserves, run by an unnamed team in Dubai and Riyadh. Ethereum shows 2.83B PUSD, which dashboards count as ~$2.8B. But 96% of it sits in the issuer's Treasury and one wallet the Treasury funded, and the whole Ethereum token has only 46 holders. No exchange lists it, the promised reserve API returns nothing, and the site's "no admin backdoor" claim conflicts with an upgradeable contract. The revenue gate fails.

**🚨 Top warning:** **a $2.8B headline with almost no real circulation, and an admin key the site says doesn't exist.** The contract's own `treasuryAddress()` is [`0x4b39…88c8`](https://etherscan.io/address/0x4b3974aaabdc251b3086ae4a8163110d766c88c8), which received the 2.8B mint. It and [`0x1760…0252`](https://etherscan.io/address/0x1760bfb0f8461fcf4c6768a82436840d23f40252) hold **2.72B of 2.83B PUSD**, and the token has just 46 holders. The [site](https://www.palmusd.com/pages/about.html) promises "no admin backdoor", yet the implementation lets `ADMIN_ROLE` upgrade the contract ([verified source](https://etherscan.io/address/0x9f41fb03aaf87c2b02f2d44bc98cd22a40ef3999#code)). Every link is in the 🔗 Evidence trail below.

**Sections passed: 0 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 1/10 | ❌ FAIL (hard gate) |
| 🏛️ Foundation & team | 3/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 2/10 | ❌ FAIL |
| 📉 Selling behavior | 5/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 3/10 | ❌ FAIL |
| 💧 Liquidity & market | 1/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 4/10 | ❌ FAIL |
| 🤝 Adoption & customers | 1/10 | ❌ FAIL |
| 🛡️ Security & audits | 4/10 | ❌ FAIL |
| ⚖️ Regulatory | 3/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 3/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 PALMUSD · Palm USD (PUSD) · 2.6 / 10 · ❌ FAIL

> **One line:** A stablecoin whose $2.8B on-chain supply is almost all issuer inventory, with an upgradeable contract and no attestation published.

| 📊 Market (16 Nov 2026 ~1:30 PM MST) | 🔗 Chain (Etherscan) |
|---|---|
| **Price** no exchange market (Etherscan shows ~$0.999 from a third-party feed) | **Supply** 2.83B PUSD on Ethereum |
| **24h / 7d / 30d** n/a | **Treasury** 1.36B · **Treasury-funded wallet** 1.37B |
| **Market cap** not listed on CoinGecko | **Holders** 46; next largest 399k |
| **24h volume** none found | **Solana** 2.9M PUSD |
| **ATH** n/a | **Contract** UUPS proxy, upgraded 3 times (Sep–Nov 2025) |
| **Pump days** none (pegged asset; no exchange series) | |

---

## 💰 Revenue — Does it make money? · 1/10 · ❌ FAIL (hard gate)

- A non-yield stablecoin: income on the reserves stays with the issuer. No burn, buyback or fee share.

**What it means:** none of it reaches holders. **Holder test: no.** **1 → hard-gate FAIL.**

## 🏛️ Foundation & team — Who is in charge? · 3/10 · ❌ FAIL

- The site describes a team "hubbed in Dubai and Riyadh" and says bios will publish later. No legal entity, licence or Shariah board is named, and it says its regulatory framework is "under review" ([about](https://www.palmusd.com/pages/about.html)).

## 🪙 Foundation / team holdings — How many coins do they hold? · 2/10 · ❌ FAIL

- The contract's own `treasuryAddress()` returns [`0x4b39…88c8`](https://etherscan.io/address/0x4b3974aaabdc251b3086ae4a8163110d766c88c8), which received **2.8B PUSD** minted from the zero address. **Attribution confidence:** high (contract state plus the mint record).
- In Dec 2025 the Treasury moved **1.37B** to [`0x1760…0252`](https://etherscan.io/address/0x1760bfb0f8461fcf4c6768a82436840d23f40252) (low confidence: an unlabelled wallet linked only by its funding, with no Arkham pass yet) and 101M to another wallet. Together they hold **2.72B (96%)**, but under the 16 Nov 2026 rule a low-confidence attribution can't move Holdings on its own. On the Treasury's own **1.36B (48%)** alone, which is proven by contract state, the score is **2** (it was 1). **Alternative:** if 0x1760 is confirmed as issuer-controlled, Holdings returns to 1 and the overall to 2.5.

## 📉 Selling behavior — Do insiders sell into pumps? · 5/10 · ❌ FAIL

- A $1 stablecoin has no pump days, and no exchange-native series exists. The Treasury's only outflows went to two wallets in Dec 2025, with no exchange deposits: none found. Score 5, because the issuer controls almost all supply and could move it at any time.

## 📊 Tokenomics & supply · 3/10 · ❌ FAIL

- Mint by `OPERATOR_ROLE` ([`0x6d31…e898`](https://etherscan.io/address/0x6d3174d8fa8a24d19253e8b479c5ab58d0a2e898)); upgrades by `ADMIN_ROLE`; role changes have a 1-day delay. Supply on BNB Chain and TRON couldn't be read (BscScan needs a paid key; the TRON address isn't published).

## 💧 Liquidity & market · 1/10 · ❌ FAIL

- No exchange listing found; a Uniswap v4 pool holds ~$13.

## 🧑‍💻 Product & development · 4/10 · ❌ FAIL

- Contracts are live on Ethereum, BNB Chain, Solana and ADI Chain. The public reserves and circulation API, promised for Q2 2026, returns empty responses ([developers](https://www.palmusd.com/pages/developers.html)).

## 🤝 Adoption & customers · 1/10 · ❌ FAIL

- 46 Ethereum holders; little use beyond the issuer's own wallets.

## 🛡️ Security & audits · 4/10 · ❌ FAIL

- The site claims "no admin key, no blacklist, no pause". The verified implementation `PalmUSDV3` has no blacklist, but it has `_authorizeUpgrade … onlyRole(ADMIN_ROLE)`, so admins can replace the code ([source](https://etherscan.io/address/0x9f41fb03aaf87c2b02f2d44bc98cd22a40ef3999#code)). Audit reports weren't checked.

## ⚖️ Regulatory · 3/10 · ❌ FAIL

- "Regulatory framework under review", with no licence named. Monthly ISAE 3000 attestations are claimed, but none were found [Unverified].

## 📅 Catalysts & calendar · 3/10 · ❌ FAIL

- TRON address and status page are still pending.

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | 🟢 None found (no pump days on a peg) |
| Live mint path | 🔴 Operator mint; admin can upgrade |
| Entity concentration | 🔴 Issuer wallets hold 96% |

## 📚 Sources

- [Tier A] Etherscan: [token](https://etherscan.io/token/0xfaf0cee6b20e2aaa4b80748a6af4cd89609a3d78), holders, `treasuryAddress()`, RoleGranted events, [implementation source](https://etherscan.io/address/0x9f41fb03aaf87c2b02f2d44bc98cd22a40ef3999#code)
- [Tier A] [Palm USD about](https://www.palmusd.com/pages/about.html), [developers](https://www.palmusd.com/pages/developers.html), [networks](https://www.palmusd.com/pages/networks.html)
- [Tier A] Solana RPC `getTokenSupply` for the PUSD mint
- [Tier B] [Stablecoin Beat profile](https://stablecoinbeat.com/companies/palm-usd/palm-usd/)
- Pump days from none available (no exchange-native PUSD series; the hierarchy found no pair)

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Treasury received the 2.8B mint; holds 1.36B | [`0x4b39…88c8`](https://etherscan.io/address/0x4b3974aaabdc251b3086ae4a8163110d766c88c8) | A | 16 Nov 2026 |
| Treasury-funded wallet holds 1.37B | [`0x1760…0252`](https://etherscan.io/address/0x1760bfb0f8461fcf4c6768a82436840d23f40252) | A | 16 Nov 2026 |
| Upgradeable by ADMIN_ROLE | [PalmUSDV3 source](https://etherscan.io/address/0x9f41fb03aaf87c2b02f2d44bc98cd22a40ef3999#code) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Do reserves match 2.83B, or only the coins in circulation?** | Get the ISAE 3000 attestation; the issuer's API is empty | Ask the issuer |
| 2 | **Who controls the admin and operator roles?** | Arkham entity view of the role holders | Arkham (no lookup yet) |
| 3 | **Supply on BNB Chain and TRON** | BscScan holders; TRON address once published | Paid BscScan key, or manual |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.

- Research only. Not investment advice.
