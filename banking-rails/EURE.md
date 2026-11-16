---
ticker: EURE
name: Monerium EUR e-money (EURe)
chain: gnosis + ethereum + 5 more
contract: "0x420ca0f9b9b604ce0fd9c18ef134c705e5fa3430"
overall_score: 5.0
overall_verdict: FAIL
section_scores:
  revenue: 3
  foundation_team: 6
  insider_holdings: 6
  selling_behavior: 6
  tokenomics_supply: 7
  liquidity_market: 4
  product_development: 6
  adoption_customers: 4
  security_audits: 6
  regulatory: 7
  catalysts: 3
gates_failed: [revenue]
red_lines:
  asset_type: "EUR e-money token (stablecoin), not an investment token"
  hack_exploit: "none found"
  mint_path_live: "yes, issuer mint against euro deposits; Ethereum max mint allowance 21,000,000; owner 0x5591a6495d726c7efafb9a9dad32695d137b4d9f (3-of-6 Safe)"
  team_wallet_to_exchange_during_pump: "not applicable (EUR peg, no CEX market)"
  reserve_attestation: "none published"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "EURe is e-money with no yield to holders and Monerium's reserve income stays with the issuer, so revenue does not reach holders."
pump_day_price_source: "not applicable (EUR peg, no CEX market)"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions:
  - address: "0x39b8b6385416f4ca36a20319f70d28621895279d"
    label: "Monerium: Monerium EURe (token)"
    confidence: high
    independent_corroboration: true
    basis: "Arkham + Etherscan"
  - address: "0x5591a6495d726c7efafb9a9dad32695d137b4d9f"
    label: "Gnosis Safe Proxy (generic); token owner() on-chain"
    confidence: medium
    independent_corroboration: true
    basis: "Arkham + RPC owner()"
  - address: "0x03b15b0fd8dc5fd25d52fe3cf5f82135d80c641b"
    label: "BlacklistValidatorUpgradeable (verified proxy)"
    confidence: high
    independent_corroboration: true
    basis: "Arkham + RPC validator()"
  - address: "0xe34cc5d6a66328cde7caf0155f8dffebd953c201"
    label: "Gnosis Safe (SafeProxy), largest Ethereum holder; owner [Unverified]"
    confidence: low
    independent_corroboration: false
    basis: "Blockscout holder list: SafeProxy holding 694,565.1 EURe (read 16 Nov 2026); address verified against Blockscout; not yet read on Arkham"
price_usd: 1.1
price_source: "CoinGecko, 16 Nov 2026 9:56 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### EURE · Overall grade **5.0 / 10 · ❌ FAIL**

**Summary:** EURe is a euro **e-money token** issued by Monerium, an e-money institution supervised by the Central Bank of Iceland's FSA and notified under MiCA ([MiCA white paper](https://monerium.com/whitepapers/eure-whitepaper.xhtml), Tier A). It is redeemable at par by SEPA for Monerium customers. Supply read on-chain is about **25.4M EURe**: Gnosis 12.77M, Arbitrum 5.52M, Ethereum 4.00M, Polygon 3.01M and Linea 0.13M. Base and Noble were not read. The token itself has no revenue. Monerium earns on reserves but discloses no figures, and **publishes no reserve attestation** [Tier B ×2]. Revenue trips the hard gate, mostly because the framework doesn't fit a stablecoin. The main demand risk is that **Gnosis Pay's consumer card, EURe's biggest use, shuts on 20 Dec 2026** [Tier B].

**🚨 Top warning:** There is no public proof of reserves; holders rely on annual audits and supervisor filings. Issuance is controlled by 3-of-6 Safes on Ethereum and Gnosis. Gnosis Pay's consumer exit in Dec 2026 removes the main retail use case on Gnosis, where half the supply lives.

**Sections passed: 7 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 3/10 | ❌ FAIL |
| 🏛️ Foundation & team | 6/10 | ✅ PASS |
| 🪙 Foundation / team holdings | 6/10 | ✅ PASS |
| 📉 Selling behavior | 6/10 | ✅ PASS |
| 📊 Tokenomics & supply | 7/10 | ✅ PASS |
| 💧 Liquidity & market | 4/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 6/10 | ✅ PASS |
| 🤝 Adoption & customers | 4/10 | ❌ FAIL |
| 🛡️ Security & audits | 6/10 | ✅ PASS |
| ⚖️ Regulatory | 7/10 | ✅ PASS |
| 📅 Catalysts & calendar | 3/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 EURE · Monerium EUR e-money (EURe) · 5.0 / 10 · ❌ FAIL

> **One line:** A properly licensed euro e-money token with thin DEX liquidity, no attestation and a shrinking main use case.

| 📊 Market (CoinGecko, 16 Nov 2026 9:56 AM MST) | 🔗 On-chain (RPC / Etherscan v2, 16 Nov 2026) |
|---|---|
| **Price** $1.10 (EUR peg; 1y −4.9% in USD terms) | **Supply** Gnosis 12,770,058 · Arbitrum 5,519,377 · Ethereum 3,995,144 · Polygon 3,006,439 · Linea 133,234 |
| **Market cap** $28.2M · rank #615 | **Ethereum owner** [3-of-6 Safe](https://etherscan.io/address/0x5591a6495d726c7efafb9a9dad32695d137b4d9f) · max mint allowance 21,000,000 |
| **24h volume** $1.34M, all DEX: Uniswap V3 Ethereum $1.09M, Oku and Curve on Gnosis | **Gnosis owner** [3-of-6 Safe](https://gnosisscan.io/address/0x8001ea269cb9715bf7acff89c664ffc134a519ec) |
| **Pump days** not applicable (pegged; no CEX price history) | 2,317 holders on Ethereum (Blockscout) |

---

## 💰 Revenue — Does it make money? · 3/10 · ❌ FAIL

| Metric | Value | Source |
|---|---:|---|
| Token-level revenue | None (e-money; no yield to holders) | [Tier A] MiCA white paper |
| Issuer reserve income | Not disclosed; issuance and redemption are free | [Tier B] cjsoi; Skrumble |
| DefiLlama fees | Not listed | [Tier A] api.llama.fi |

**What it means:** this framework scores protocol revenue; a regulated e-money token has none to holders. **3 (hard gate).**

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** EURe is e-money with no yield to holders and Monerium's reserve income stays with the issuer, so revenue does not reach holders.

## 🏛️ Foundation & team — Who is in charge? · 6/10 · ✅ PASS

- Monerium hf. (Iceland) has been licensed since 2019, is on ESMA's MiCA e-money token list, and issues EURe, GBPe and USDe [Tier A, white paper].

## 🪙 Foundation / team holdings — How many coins do they hold? · 6/10 · ✅ PASS

- There is no insider allocation: every token is minted against deposited euros.
- The largest Ethereum holders are smart wallets (Safes), led by [0xE34c…C201](https://etherscan.io/address/0xE34cC5d6A66328CdE7cAf0155f8DfFEBd953C201) with 694,565 EURe, plus the Polygon bridge tunnel [0x0cC2…7F2c](https://etherscan.io/address/0x0cC2CaeD31490B546c741BD93dbba8Ab387f7F2c) (191,298) [Tier A, Blockscout]. The Gnosis holder list was not reachable (explorer bot-blocked).
- **Arkham (16 Nov 2026):** the Ethereum EURe token [0x39b8…279d](https://intel.arkm.com/explorer/address/0x39b8b6385416f4ca36a20319f70d28621895279d) is labelled **Monerium EURe**, and the transfer validator [0x03b1…641b](https://intel.arkm.com/explorer/address/0x03b15b0fd8dc5fd25d52fe3cf5f82135d80c641b) is a verified BlacklistValidatorUpgradeable proxy. The issuance-owner Safe [0x5591…4d9f](https://intel.arkm.com/explorer/address/0x5591a6495d726c7efafb9a9dad32695d137b4d9f) carries only a generic Gnosis Safe label and holds no EURe, so it controls minting but is not a holder. Arkham was not read for the largest holder [0xE34c…C201](https://intel.arkm.com/explorer/address/0xe34cc5d6a66328cde7caf0155f8dffebd953c201) (the 16 Nov 2026 lookup used a mistyped address; the correct address, checked on [Blockscout](https://eth.blockscout.com/address/0xE34cC5d6A66328CdE7cAf0155f8DfFEBd953C201), is a SafeProxy holding 694,565.1 EURe), so its owner is [Unverified]; the 694,565 balance is from Blockscout. Nothing here changes the score. [Tier B] Arkham, read 16 Nov 2026 (signed-in account).

## 📉 Selling behavior — Do insiders sell into pumps? · 6/10 · ✅ PASS

- Not applicable: there is no team float and no CEX market. The peg is held by mint and redemption at par, not by sellers.

**What it means:** neutral. **6**.

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from not applicable (EUR peg, no CEX market).

## 📊 Tokenomics & supply · 7/10 · ✅ PASS

- 1:1 backed by euro deposits at Arion Bank, LHV and State Street, mostly in the State Street EUR Liquidity LVNAV fund [Tier B ×2]. There is no attestation, and the split between fund and deposits is unknown, so the MiCA 30%-in-deposits rule can't be checked [Unverified]. **7**.

## 💧 Liquidity & market · 4/10 · ❌ FAIL

- Only DEX liquidity ($1.34M a day), concentrated in one Uniswap V3 pool on Ethereum. No CEX listing. **4**.

## 🧑‍💻 Product & development · 6/10 · ✅ PASS

- Natively issued on seven networks. Each wallet gets an IBAN, so SEPA payments mint EURe and redemptions pay out euros.

## 🤝 Adoption & customers · 4/10 · ❌ FAIL

- Mainly Gnosis Pay card spend plus Gnosis DeFi. Gnosis Pay's consumer card and web app end 20 Dec 2026 (it is moving to business customers) [Tier B]. MetaMask Card and Bleap also integrate EURe.

## 🛡️ Security & audits · 6/10 · ✅ PASS

- No exploit found. Upgradeable controller token with `mint`, `burn`, `recover` and a validator contract ([0x03b1…641b](https://etherscan.io/address/0x03b15b0fd8dc5fd25d52fe3cf5f82135d80c641b)) that can block transfers. Owned by 3-of-6 Safes on Ethereum and Gnosis [Tier A, RPC]. `recover` is a strong issuer power, as with most regulated stablecoins.

## ⚖️ Regulatory · 7/10 · ✅ PASS

- Authorised EMI under MiCA. Not available to US residents [Tier B]. **7**.

## 📅 Catalysts & calendar · 3/10 · ❌ FAIL

| Date | Event |
|---|---|
| 20 Dec 2026 | Gnosis Pay consumer card and web app shut down |
| Unscheduled | First public reserve attestation (promised since 2023) |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | ⚪ Not applicable (stablecoin) |
| Live mint path | 🟡 Issuer mint (3-of-6 Safe), 21M max allowance on Ethereum |
| Reserve attestation | 🔴 None published |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| [0x39b8…279d](https://intel.arkm.com/explorer/address/0x39b8b6385416f4ca36a20319f70d28621895279d) | Monerium: Monerium EURe (token) | Arkham + Etherscan | high | yes | None |
| [0x5591…4d9f](https://intel.arkm.com/explorer/address/0x5591a6495d726c7efafb9a9dad32695d137b4d9f) | Gnosis Safe Proxy (generic); token owner() on-chain | Arkham + RPC owner() | medium | yes (on-chain owner()) | None |
| [0x03b1…641b](https://intel.arkm.com/explorer/address/0x03b15b0fd8dc5fd25d52fe3cf5f82135d80c641b) | BlacklistValidatorUpgradeable (verified proxy) | Arkham + RPC validator() | high | yes | None |
| [0xE34c…C201](https://intel.arkm.com/explorer/address/0xe34cc5d6a66328cde7caf0155f8dffebd953c201) | Gnosis Safe (SafeProxy) holding 694,565.1 EURe; owner [Unverified] | Blockscout (address verified 16 Nov 2026); not yet read on Arkham | low | no | None |

## 📚 Sources

- [Tier B] Arkham, read 16 Nov 2026 (signed-in account): the EURe token, the issuance Safe, the validator and the largest holder
- [Tier A] [Monerium EURe MiCA white paper](https://monerium.com/whitepapers/eure-whitepaper.xhtml) · [Monerium 2023 risk assessment](https://monerium.com/blog/2023/eure-asset-risk-assessment/)
- [Tier A] Etherscan v2 `tokensupply` (Ethereum, Polygon, Arbitrum); Gnosis and Linea RPC `totalSupply`; Ethereum and Gnosis RPC reads of `owner()`, `getThreshold()`, `getOwners()`, `getMaxMintAllowance()`, `validator()`; Blockscout Ethereum holders and verified ABI
- [Tier B] [cjsoi EURe profile](https://www.cjsoi.com/stablecoin-list/eure) · [Skrumble EURe explainer](https://skrumble.com/stablecoins/eure/)
- [Tier A] CoinGecko `monerium-eur-money-2` (16 Nov 2026 9:56 AM MST)

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Ethereum issuance owned by a 3-of-6 Safe | [0x5591…4d9f](https://etherscan.io/address/0x5591a6495d726c7efafb9a9dad32695d137b4d9f) | A | 16 Nov 2026 |
| Gnosis issuance owned by a 3-of-6 Safe | [0x8001…19ec](https://gnosisscan.io/address/0x8001ea269cb9715bf7acff89c664ffc134a519ec) | A | 16 Nov 2026 |
| EMI under MiCA, redeemable at par | [white paper](https://monerium.com/whitepapers/eure-whitepaper.xhtml) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Who owns the largest Ethereum holder `0xE34c…C201`** | Address verified on [Blockscout](https://eth.blockscout.com/address/0xE34cC5d6A66328CdE7cAf0155f8DfFEBd953C201) (a SafeProxy); look it up on Arkham or ask Monerium who controls it | Free |
| 2 | **Reserve composition** | Monerium audited accounts; ask for an attestation | Free |
| 3 | **Gnosis holder concentration** | Gnosisscan holder page (manual) | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
