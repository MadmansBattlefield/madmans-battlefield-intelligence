---
ticker: TRUF
name: TRUF.Network (Truflation)
chain: ethereum
contract: "0x243c9be13faba09f945ccc565547293337da0ad7"
overall_score: 3.7
overall_verdict: FAIL
section_scores:
  revenue: 2
  foundation_team: 5
  insider_holdings: 4
  selling_behavior: 4
  tokenomics_supply: 4
  liquidity_market: 2
  product_development: 5
  adoption_customers: 3
  security_audits: 5
  regulatory: 6
  catalysts: 4
gates_failed: [revenue]
red_lines:
  hack_exploit: "none found"
  mint_path_live: "no; 1B fixed supply"
  team_wallet_to_exchange_during_pump: "not proven: the only pump-day exchange deposit found came from an unlabelled holder (low confidence)"
  one_hop_sale_status: none_found
  entity_concentration: "labelled TRUF Vesting contract 341.6M (34%); an unlabelled holder 154.4M (15%)"
price_usd: 0.00218364
price_source: "CoinGecko, 16 Nov 2026 ~12:30 PM MST"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "2% settlement fee goes 75% to LPs, 12.5% to validators, 12.5% to data publishers; the network keeps none and TRUF staking rewards were discontinued"
pump_day_price_source: "Gate TRUF_USDT daily closes (UTC); Binance unavailable (451), Gate is next in the hierarchy"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions:
  - address: "0x7e3ad114031acd0437ccba560f592874e62780b6"
    label: "Truflation: TRUF Vesting (TrufVesting)"
    confidence: high
    independent_corroboration: true
    basis: "Etherscan name tag plus Arkham's explicit TrufVesting verified-contract label; funded with 372M by 0xae9946fb686bb2e8c448066a8339d0d204e868a3"
  - address: "0xae9946fb686bb2e8c448066a8339d0d204e868a3"
    label: "unlabelled (funded the vesting contract)"
    confidence: low
    independent_corroboration: false
    basis: "sent 372M into the labelled vesting contract; no label"
  - address: "0xb2e53fbda93b92017e80a86a712a535da9cd167e"
    label: "unlabelled holder"
    confidence: low
    independent_corroboration: false
    basis: "funded by the TRUF Migrator and other holders; no project label (Arkham shows none)"
  - address: "0x8d78ea2adda1059bd62666779856efafdd25d740"
    label: "generic Gnosis Safe (154.4M TRUF)"
    confidence: low
    independent_corroboration: false
    basis: "Arkham generic Safe label; shares a signer with the Safe linked to the seller wallet"
  - address: "0x9052f3970ac942ca759e0068d9977cae88209222"
    label: "generic Gnosis Safe (funded the seller wallet)"
    confidence: low
    independent_corroboration: false
    basis: "Arkham generic Safe label; sent 14.99M TRUF to 0xb2e53fbda93b92017e80a86a712a535da9cd167e"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### TRUF · Overall grade **3.7 / 10 · ❌ FAIL**

**Summary:** TRUF.Network (formerly Truflation) runs data streams and, since May 2026, prediction markets settled on them. Its 2% settlement fee goes to liquidity providers, validators and data publishers. The network keeps none of it, and TRUF staking rewards stopped in Jan 2026, so holders get nothing. A labelled vesting contract holds 34% of supply. The only pump-day exchange deposit found came from an unlabelled wallet, so Selling is not proven. TRUF is down 99.8% from its 2024 peak. The revenue gate fails.

**🚨 Top warning:** **the token has no claim on the fees and a large vesting overhang.** The Etherscan-tagged "Truflation: TRUF Vesting" contract [`0x7e3a…80b6`](https://etherscan.io/address/0x7e3ad114031acd0437ccba560f592874e62780b6) still holds **341.6M TRUF (34%)**. The next unlock is ~8.5M on 1 Dec 2026 [Tier B]. An unlabelled holder sent 2M TRUF to a Gate deposit on a +21.3% pump day ([30 Apr 2026](https://etherscan.io/tx/0x64236090c17b34b59bdfadc74de99ed1b90c79997a89fa9a28cf0d799be42379)), but it can't be tied to the team. Every link is in the 🔗 Evidence trail below.

**Sections passed: 1 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 2/10 | ❌ FAIL (hard gate) |
| 🏛️ Foundation & team | 5/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 4/10 | ❌ FAIL |
| 📉 Selling behavior | 4/10 | ❌ FAIL (not proven) |
| 📊 Tokenomics & supply | 4/10 | ❌ FAIL |
| 💧 Liquidity & market | 2/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 5/10 | ❌ FAIL |
| 🤝 Adoption & customers | 3/10 | ❌ FAIL |
| 🛡️ Security & audits | 5/10 | ❌ FAIL |
| ⚖️ Regulatory | 6/10 | ✅ PASS |
| 📅 Catalysts & calendar | 4/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 TRUF · TRUF.Network (Truflation) · 3.7 / 10 · ❌ FAIL

> **One line:** A data and prediction-market network whose fees bypass TRUF holders; insider selling is not proven.

| 📊 Market (CoinGecko, 16 Nov 2026 ~12:30 PM MST) | 🔗 Chain (Etherscan) |
|---|---|
| **Price** $0.00218 | **Supply** 576.3M circulating / 1B |
| **24h / 7d / 30d** 🔴 −2.7% / 🔴 −15.1% / 🔴 −37.2% | **TRUF Vesting** 341.6M (34%) |
| **Market cap** $1.26M · **FDV** $2.18M | **Next holders** 154.4M, 47.4M, 42.9M (unlabelled) |
| **24h volume** ~$34.7k (KuCoin $19.0k, Gate $12.1k) | **veTRUF** 27.5M · **Migrator** 28.0M |
| **ATH** $0.9066 (14 Apr 2024) · now −99.8% | |
| **Pump days** 32 in the last year (Gate TRUF_USDT; largest +47.2% on 24 Jan 2026) | |

---

## 💰 Revenue — Does it make money? · 2/10 · ❌ FAIL (hard gate)

- Prediction markets charge a 2% settlement fee: 75% to LPs, 12.5% to validators, 12.5% to data publishers. The network keeps none ([TRUF.Network](https://truf.network/), [whitepaper](https://raw.githubusercontent.com/trufnetwork/docs/main/pdfs/TN-Whitepaper.pdf)). New TRUF staking rewards stopped in Jan 2026; staking is planned again for Q1 2027 [Tier B].

**What it means:** none of it reaches holders. **Holder test: no.** **2 → hard-gate FAIL.**

## 🏛️ Foundation & team — Who is in charge? · 5/10 · ❌ FAIL

- Operated by the TRUF.Network team (the former Truflation). Leaders are public on the site; described here by role. Governance is off-chain.

## 🪙 Foundation / team holdings — How many coins do they hold? · 4/10 · ❌ FAIL

- The labelled **TRUF Vesting** contract [`0x7e3a…80b6`](https://etherscan.io/address/0x7e3ad114031acd0437ccba560f592874e62780b6) holds **341.6M (34%)**. **Attribution confidence:** high: Etherscan's tag plus Arkham's explicit **TrufVesting** verified-contract label ([Arkham](https://intel.arkm.com/explorer/address/0x7e3ad114031acd0437ccba560f592874e62780b6)), which shows vesting payouts to Safes and unlabelled wallets and no exchange deposits on page 1.
- [`0x8d78…d740`](https://etherscan.io/address/0x8d78ea2adda1059bd62666779856efafdd25d740) holds **154.4M (15%)**. It got all of it from the TRUF Migrator and has sent 22.5M to [`0xae99…68a3`](https://etherscan.io/address/0xae9946fb686bb2e8c448066a8339d0d204e868a3), which funded the vesting contract. That suggests a project link, but Arkham labels [0x8d78…d740](https://intel.arkm.com/explorer/address/0x8d78ea2adda1059bd62666779856efafdd25d740) only as a generic Gnosis Safe, and [0xae99…68a3](https://intel.arkm.com/explorer/address/0xae9946fb686bb2e8c448066a8339d0d204e868a3) likewise: **confidence low**, so it doesn't move this score. Score 4. [Tier B] Arkham, read 16 Nov 2026 (signed-in account).

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL (not proven)

- **Trail:** the vesting contract and the top unlabelled holders were traced two hops. No transfer from the labelled vesting contract to an exchange was found.
- **Pump-day deposit:** unlabelled holder [`0xb2e5…167e`](https://etherscan.io/address/0xb2e53fbda93b92017e80a86a712a535da9cd167e) sent **2.0M TRUF (~$11k)** to Gate deposit [`0x17bd…b4b1`](https://etherscan.io/address/0x17bd634245698a6d8eedff3ddbaeb4d83478b4b1) on 30 Apr 2026 (+21.3%), [tx](https://etherscan.io/tx/0x64236090c17b34b59bdfadc74de99ed1b90c79997a89fa9a28cf0d799be42379) (status 1).
- **Attribution confidence:** low. The sender's TRUF came from the Migrator (an old-token swap) and from other holders. One link runs through [`0x9052…9222`](https://etherscan.io/address/0x9052f3970ac942ca759e0068d9977cae88209222), which received 7M from the 154.4M holder in Jun 2025, but only after this deposit.
- **Arkham (16 Nov 2026):** [0xb2e5…167e](https://intel.arkm.com/explorer/address/0xb2e53fbda93b92017e80a86a712a535da9cd167e) has no label. It received 14.99M TRUF from the generic Safe [0x9052…9222](https://intel.arkm.com/explorer/address/0x9052f3970ac942ca759e0068d9977cae88209222), which shares a listed signer with the Safe [0xae99…68a3](https://intel.arkm.com/explorer/address/0xae9946fb686bb2e8c448066a8339d0d204e868a3) that funded the vesting contract and is fed by the 154.4M holder. A shared signer between generic Safes is low confidence and can't move Selling on its own. Arkham's page 1 also shows the wallet's further deposits to KuCoin, Gate and MEXC deposit addresses; their dates weren't checked against pump days on Etherscan [Unverified]. [Tier B] Arkham, read 16 Nov 2026 (signed-in account).
- **Alternative:** an ordinary migrated holder or trader taking profit. A low-confidence attribution can't move Selling, so it stays **not proven → 4**. **Disclosure quality:** not applicable.

## 📊 Tokenomics & supply · 4/10 · ❌ FAIL

- 1B fixed supply, 58% circulating. Team, ecosystem and advisor tranches unlock monthly; ~8.5M is due 1 Dec 2026 [Tier B, naut.so].

## 💧 Liquidity & market · 2/10 · ❌ FAIL

- About $35k a day, mostly KuCoin and Gate.

## 🧑‍💻 Product & development · 5/10 · ❌ FAIL

- Data streams and prediction markets (live 14 May 2026) are running ([updates](https://truf.network/updates/what-exactly-are-we-building)).

## 🤝 Adoption & customers · 3/10 · ❌ FAIL

- Little evidence of paying users outside its own markets.

## 🛡️ Security & audits · 5/10 · ❌ FAIL

- No exploit found.

## ⚖️ Regulatory · 6/10 · ✅ PASS

- No enforcement found. Prediction markets carry regulatory risk in some places.

## 📅 Catalysts & calendar · 4/10 · ❌ FAIL

- Monthly unlocks; staking relaunch planned for Q1 2027.

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | ⚪ Not proven: one unlabelled holder only |
| Live mint path | 🟢 None |
| Entity concentration | 🟡 Vesting contract 34% |

## 📚 Sources

- [Tier B] Arkham, read 16 Nov 2026 (signed-in account): TrufVesting label; generic Safe labels and signer overlap for the 154.4M holder, the vesting funder and the seller's funder
- [Tier A] Etherscan: holders, the vesting contract and the traced transfers (linked above)
- [Tier A] [TRUF.Network](https://truf.network/), [whitepaper (value accrual)](https://raw.githubusercontent.com/trufnetwork/docs/main/pdfs/TN-Whitepaper.pdf), [updates](https://truf.network/updates/what-exactly-are-we-building)
- [Tier B] naut.so unlock schedule
- [Tier A] CoinGecko `truflation` (market, venues); pump days from Gate TRUF_USDT daily closes (UTC), per the price-source hierarchy

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Vesting contract holds 341.6M | [`0x7e3a…80b6`](https://etherscan.io/address/0x7e3ad114031acd0437ccba560f592874e62780b6) | A | 16 Nov 2026 |
| Pump-day Gate deposit by an unlabelled holder | [tx](https://etherscan.io/tx/0x64236090c17b34b59bdfadc74de99ed1b90c79997a89fa9a28cf0d799be42379) · [`0xb2e5…167e`](https://etherscan.io/address/0xb2e53fbda93b92017e80a86a712a535da9cd167e) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Who controls the 154.4M holder and the vesting funder?** | Arkham (16 Nov 2026) shows generic Safes with a shared signer; ask TRUF.Network who the signers are | Free |
| 2 | **Where unlocked team tokens go** | Trace the vesting contract's beneficiaries past two hops | Free (Etherscan) |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.

- Research only. Not investment advice.
