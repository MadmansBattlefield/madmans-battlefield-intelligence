---
ticker: NUVA
name: NUVA Finance (no NUVA token; vault tokens HOME, nvPRIME, nvYLDS)
chain: ethereum
contract: "no NUVA token; vaults HOME 0xdc1c0534109e2db74fe800c84096547541607859, nvPRIME 0xc360e625f19a7ea47e47810b13e386221d5187d1"
overall_score: 3.5
overall_verdict: FAIL
section_scores:
  revenue: 1
  foundation_team: 6
  insider_holdings: 4
  selling_behavior: 4
  tokenomics_supply: 2
  liquidity_market: 2
  product_development: 6
  adoption_customers: 4
  security_audits: 6
  regulatory: 4
  catalysts: 4
gates_failed: [revenue]
red_lines:
  hack_exploit: "none found"
  mint_path_live: "n/a; no NUVA token; vault tokens mint 1:1 against deposits"
  team_wallet_to_exchange_during_pump: "not proven: there is no NUVA token to sell"
  one_hop_sale_status: none_found
  entity_concentration: "HOME vault: the top 8 holders each hold almost exactly 1.0M"
price_usd: null
price_source: "No NUVA token exists (checked CoinGecko and nuva.finance, 16 Nov 2026 ~1:30 PM MST)"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "no NUVA token exists; vault yield goes to vault-token holders as the underlying RWA income, not as protocol revenue"
pump_day_price_source: "none: no NUVA token trades"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions: []
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### NUVA · Overall grade **3.5 / 10 · ❌ FAIL**

**Summary:** NUVA is an Ethereum marketplace for tokenized real-world-asset vaults, co-created by Animoca Brands and Nuva Labs and launched on 12 May 2026. There is no NUVA token, only NUVA Points, so there is nothing for holders to own and no revenue reaching a token. The vault tokens (HOME, nvPRIME, nvYLDS) hold ~$17M. Engineering looks solid (Halborn audit, 6-of-9 multisig, 48-hour timelock). The revenue gate fails because there is no token.

**🚨 Top warning:** **there is no NUVA token, only points that "unlock future opportunities".** Anything trading as "NUVA" isn't from this project. The live products are vault tokens: HOME [`0xdc1c…7859`](https://etherscan.io/address/0xdc1c0534109e2db74fe800c84096547541607859) at ~$10.0M (eight wallets hold almost exactly 1.0M each) and nvPRIME [`0xc360…87d1`](https://etherscan.io/address/0xc360e625f19a7ea47e47810b13e386221d5187d1) at ~$6.9M ([nuva.finance](https://nuva.finance/)). Every link is in the 🔗 Evidence trail below.

**Sections passed: 3 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 1/10 | ❌ FAIL (hard gate) |
| 🏛️ Foundation & team | 6/10 | ✅ PASS |
| 🪙 Foundation / team holdings | 4/10 | ❌ FAIL (not proven) |
| 📉 Selling behavior | 4/10 | ❌ FAIL (not proven) |
| 📊 Tokenomics & supply | 2/10 | ❌ FAIL |
| 💧 Liquidity & market | 2/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 6/10 | ✅ PASS |
| 🤝 Adoption & customers | 4/10 | ❌ FAIL |
| 🛡️ Security & audits | 6/10 | ✅ PASS |
| ⚖️ Regulatory | 4/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 4/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 NUVA · NUVA Finance (no NUVA token; vault tokens HOME, nvPRIME, nvYLDS) · 3.5 / 10 · ❌ FAIL

> **One line:** An RWA vault marketplace with points but no token; nothing accrues to a NUVA holder because none exists.

| 📊 Market (CoinGecko vault listings, 16 Nov 2026 ~1:30 PM MST) | 🔗 Chain (Etherscan) |
|---|---|
| **NUVA token** none | **HOME** ~$10.07M (NAV ~$1.007) |
| **nvPRIME** ~$5.76M (NAV ~$1.069) | **nvYLDS** ~$25.6k |
| **24h volume** $0 on CoinGecko for all three | **HOME top 8** ~1.0M each |
| **Pump days** n/a (no token) | |

---

## 💰 Revenue — Does it make money? · 1/10 · ❌ FAIL (hard gate)

- NUVA passes through RWA yield (est. 3.3–7% APY) to vault-token holders. That is the assets' income, not protocol revenue, and there is no NUVA token ([NUVA](https://nuva.finance/)).

**What it means:** with no token, the token has no claim on revenue. **Holder test: no.** **1 → hard-gate FAIL.**

## 🏛️ Foundation & team — Who is in charge? · 6/10 · ✅ PASS

- Co-created by Animoca Brands and Nuva Labs ([launch release](https://nuva.finance/press/nuva-live)). Distribution partner for Hastra's PRIME, which is backed by Figure. Leaders are described by role only.

## 🪙 Foundation / team holdings — How many coins do they hold? · 4/10 · ❌ FAIL (not proven)

- No token, so there are no insider token holdings. Admin functions sit with a 6-of-9 multisig ([technical deep dive](https://nuva.finance/docs/technical-deep-dive)). **Not proven → 4.**

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL (not proven)

- No token to sell. **Not proven → 4.** **Disclosure quality:** not applicable.

## 📊 Tokenomics & supply · 2/10 · ❌ FAIL

- No token supply or schedule. Points only, with no published conversion.

## 💧 Liquidity & market · 2/10 · ❌ FAIL

- Vault tokens show $0 exchange volume on CoinGecko; exits are through NUVA (nvPRIME withdrawals take up to two US business days).

## 🧑‍💻 Product & development · 6/10 · ✅ PASS

- Three live vaults with on-chain proof of reserves via Provenance ([technical deep dive](https://nuva.finance/docs/technical-deep-dive)).

## 🤝 Adoption & customers · 4/10 · ❌ FAIL

- ~$17M across the vaults. HOME is capped at $12M; its top eight holders hold ~1.0M each, which looks like a few allocators seeding it ([`0xdc1c…7859`](https://etherscan.io/address/0xdc1c0534109e2db74fe800c84096547541607859)).

## 🛡️ Security & audits · 6/10 · ✅ PASS

- Halborn audit completed Jan 2026; 6-of-9 multisig; 48-hour upgrade timelock; emergency pause ([technical deep dive](https://nuva.finance/docs/technical-deep-dive)).

## ⚖️ Regulatory · 4/10 · ❌ FAIL

- Vaults hold securities-like RWAs (YLDS is SEC-registered) and aren't available everywhere. No enforcement found.

## 📅 Catalysts & calendar · 4/10 · ❌ FAIL

- A possible future token via points (not announced); more RWA vaults during 2026.

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | ⚪ Not proven: no token |
| Live mint path | ⚪ n/a (no token) |
| Entity concentration | 🟡 HOME vault held mostly by eight ~1.0M wallets |

## 📚 Sources

- [Tier A] [NUVA site](https://nuva.finance/), [technical deep dive](https://nuva.finance/docs/technical-deep-dive), [nvPRIME](https://nuva.finance/docs/nvprime-deep-dive), [launch release](https://nuva.finance/press/nuva-live)
- [Tier A] Etherscan vault-token holders (linked above); CoinGecko vault listings
- Pump days from none available (no NUVA token)

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| HOME vault holders | [`0xdc1c…7859`](https://etherscan.io/address/0xdc1c0534109e2db74fe800c84096547541607859) | A | 16 Nov 2026 |
| nvPRIME vault holders | [`0xc360…87d1`](https://etherscan.io/address/0xc360e625f19a7ea47e47810b13e386221d5187d1) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Will NUVA Points convert to a token, and on what terms?** | Watch NUVA announcements | Free |
| 2 | **Who are the eight ~1.0M HOME holders?** | Arkham entity view | Arkham (no lookup yet) |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.

- Research only. Not investment advice.
