---
ticker: REALIZ
name: Realiz (TPT30 "VuMe Bond 2030" on Stellar)
chain: stellar
contract: "CBUBVYRKTQLMDRUBPP6SH4GO33KZCEEYBIWB5AWNGKODP4A6KPKM2VJ4"
overall_score: 2.1
overall_verdict: FAIL
section_scores:
  revenue: 1
  foundation_team: 4
  insider_holdings: 1
  selling_behavior: 4
  tokenomics_supply: 1
  liquidity_market: 1
  product_development: 3
  adoption_customers: 1
  security_audits: 4
  regulatory: 3
  catalysts: 2
gates_failed: [revenue]
red_lines:
  hack_exploit: "none found"
  mint_path_live: "yes; the admin minted 460M to itself on 2 Apr 2026"
  team_wallet_to_exchange_during_pump: "not proven: no market; supply hasn't moved since 2 Apr 2026"
  one_hop_sale_status: none_found
  entity_concentration: "100% of the 500M TPT30 sits in the issuer's wallet; 1 holder"
price_usd: null
price_source: "No market; dashboards apply a nominal $1.00 (16 Nov 2026 ~1:30 PM MST)"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "none; a bond note whose deferrable 10% coupon starts Mar 2027, and no outside holder exists"
pump_day_price_source: "none: TPT30 doesn't trade"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions:
  - address: "GCUTJSAKAJMW3IO27XBQJP73BSI2HROFT7UVAWJEZYJSOSJW2JXXWQPR"
    label: "Realiz issuer/admin account"
    confidence: high
    independent_corroboration: true
    basis: "signed the TPT30 deploy and mint transactions (Horizon); identified as the issuer admin by two independent write-ups"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### REALIZ · Overall grade **2.1 / 10 · ❌ FAIL**

**Summary:** Realiz is a Luxembourg securitisation fund whose only Stellar asset is TPT30, a note lending to an over-the-counter-quoted US app company. Dashboards show it as a $500M RWA. But the issuer's own admin minted 460M of the 500M tokens to itself on 2 Apr 2026, the whole supply still sits in that one wallet, and the offering page shows $0 raised. There's no market and no outside holder. The revenue gate fails.

**🚨 Top warning:** **a $500M dashboard figure with one holder and $0 raised.** The admin account GCUTJS…WQPR deployed TPT30 with 40M tokens ([23 Feb 2026](https://horizon.stellar.org/transactions/578159f28ab3116ce31653bf227f09ddfad9e6be98cfd765ba88c38fb4912aa5)), then minted itself 460M more ([2 Apr 2026](https://horizon.stellar.org/transactions/df9b962f0e9bae08ec5daf49cb7b6c89fe1ea206940ee6ad678095ca9bcd9cbf)). RWA.xyz shows 1 holder and $500M ([RWA.xyz](https://app.rwa.xyz/platforms/realiz)); the Bitbond offering shows $0 raised ([review](https://daniilkozin.com/blog/realiz-tpt30-stellar-500m-bond-review/)). Every link is in the 🔗 Evidence trail below.

**Sections passed: 0 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 1/10 | ❌ FAIL (hard gate) |
| 🏛️ Foundation & team | 4/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 1/10 | ❌ FAIL |
| 📉 Selling behavior | 4/10 | ❌ FAIL (not proven) |
| 📊 Tokenomics & supply | 1/10 | ❌ FAIL |
| 💧 Liquidity & market | 1/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 3/10 | ❌ FAIL |
| 🤝 Adoption & customers | 1/10 | ❌ FAIL |
| 🛡️ Security & audits | 4/10 | ❌ FAIL |
| ⚖️ Regulatory | 3/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 2/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 REALIZ · Realiz (TPT30 "VuMe Bond 2030" on Stellar) · 2.1 / 10 · ❌ FAIL

> **One line:** A single unsubscribed bond token counted as $500M on dashboards; nothing reaches holders because there are none.

| 📊 Market (16 Nov 2026 ~1:30 PM MST) | 🔗 Chain (Stellar) |
|---|---|
| **Price** no market (nominal $1.00 on dashboards) | **Supply** 500M TPT30 |
| **Dashboard value** $500.0M (RWA.xyz) | **Holders** 1 (the issuer) |
| **24h volume** none | **Contract** [CBUBVY…2VJ4](https://stellar.expert/explorer/public/contract/CBUBVYRKTQLMDRUBPP6SH4GO33KZCEEYBIWB5AWNGKODP4A6KPKM2VJ4) |
| **Pump days** n/a | |

---

## 💰 Revenue — Does it make money? · 1/10 · ❌ FAIL (hard gate)

- TPT30 is a note: a 10% coupon, payable quarterly from Mar 2027 and deferrable by the issuer, funding a loan to TPT Global Tech. Nobody outside the issuer holds it, and $0 has been raised [Tier B ×2: RWA.xyz, independent review].

**What it means:** none of it reaches holders. **Holder test: no.** **1 → hard-gate FAIL.**

## 🏛️ Foundation & team — Who is in charge? · 4/10 · ❌ FAIL

- Realiz Digital Assets Fund is a Luxembourg securitisation fund ([realiz.io](https://realiz.io/)). Realiz says this compartment is unregulated and not CSSF-supervised; EY audits the fund [Tier B, issuer answers in the review].

## 🪙 Foundation / team holdings — How many coins do they hold? · 1/10 · ❌ FAIL

- 100% of 500M TPT30 sits in the issuer's wallet. **Attribution confidence:** high: the admin account signed the deploy and mint transactions ([deploy](https://horizon.stellar.org/transactions/578159f28ab3116ce31653bf227f09ddfad9e6be98cfd765ba88c38fb4912aa5), [mint](https://horizon.stellar.org/transactions/df9b962f0e9bae08ec5daf49cb7b6c89fe1ea206940ee6ad678095ca9bcd9cbf), both successful on Horizon), and two independent sources show the single holder. Score 1.

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL (not proven)

- No market and no transfers since 2 Apr 2026. **Not proven → 4.** **Disclosure quality:** not applicable.

## 📊 Tokenomics & supply · 1/10 · ❌ FAIL

- Supply jumped from 40M to 500M by an admin self-mint with no subscription behind it. The same admin issued two more notes (RICH31, VERT31), also self-held [Tier B].

## 💧 Liquidity & market · 1/10 · ❌ FAIL

- None: no venue, and redemption only at maturity.

## 🧑‍💻 Product & development · 3/10 · ❌ FAIL

- A tokenization pipeline with a Luxembourg vehicle; one live Stellar note.

## 🤝 Adoption & customers · 1/10 · ❌ FAIL

- $0 raised, 0 investors, 1 holder.

## 🛡️ Security & audits · 4/10 · ❌ FAIL

- A Soroban token contract; the admin can mint. No audit found [Unverified].

## ⚖️ Regulatory · 3/10 · ❌ FAIL

- Unregulated compartment, professional investors only, non-US. Aggregators list a CSSF supervisor, which the issuer says is wrong.

## 📅 Catalysts & calendar · 2/10 · ❌ FAIL

- First coupon due 16 Mar 2027 (deferrable); maturity 16 Mar 2031.

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | ⚪ Not proven: no market |
| Live mint path | 🔴 Admin self-mint of 460M |
| Entity concentration | 🔴 100% in the issuer's wallet |

## 📚 Sources

- [Tier A] Stellar Horizon transactions (linked above); [Realiz site](https://realiz.io/)
- [Tier B] [RWA.xyz Realiz](https://app.rwa.xyz/platforms/realiz), [independent TPT30 review](https://daniilkozin.com/blog/realiz-tpt30-stellar-500m-bond-review/), [WhaleHub Stellar RWA guide](https://whalehub.io/blog/best-rwa-platforms-stellar)
- Pump days from none available (no market). Stellar Expert's API asked for payment, so contract balances come from the two Tier B sources.

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Deploy with 40M, 23 Feb 2026 | [Horizon tx](https://horizon.stellar.org/transactions/578159f28ab3116ce31653bf227f09ddfad9e6be98cfd765ba88c38fb4912aa5) | A | 16 Nov 2026 |
| Self-mint of 460M, 2 Apr 2026 | [Horizon tx](https://horizon.stellar.org/transactions/df9b962f0e9bae08ec5daf49cb7b6c89fe1ea206940ee6ad678095ca9bcd9cbf) | A | 16 Nov 2026 |
| 1 holder, $500M shown | [RWA.xyz](https://app.rwa.xyz/platforms/realiz) | B | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Does the investor ever subscribe?** | Watch TPT30 balances leave the issuer wallet | Free (Soroban RPC) |
| 2 | **Read contract balances directly** | Soroban RPC `getLedgerEntries` for the TPT30 balance keys | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.

- Research only. Not investment advice.
