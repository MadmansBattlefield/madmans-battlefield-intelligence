---
ticker: KTA
name: Keeta
chain: base
contract: "0xc0634090f2fe6c6d75e61be2b949464abb498973"
overall_score: 3.5
overall_verdict: FAIL
section_scores:
  revenue: 1
  foundation_team: 5
  insider_holdings: 4
  selling_behavior: 4
  tokenomics_supply: 4
  liquidity_market: 3
  product_development: 5
  adoption_customers: 3
  security_audits: 5
  regulatory: 5
  catalysts: 4
gates_failed: [revenue]
red_lines:
  hack_exploit: "none found in this pass"
  team_wallet_to_exchange_during_pump: "not tested: team and treasury wallets unpublished"
  one_hop_sale_status: none_found
  entity_concentration: "~364M of 1B not circulating; wallets unpublished"
price_usd: 0.04499516
price_source: "CoinGecko `keeta`, 16 Nov 2026 ~3:00 PM MST"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "No burn, buyback, fee share or fee-funded staking yield was found; network fees are not reported."
pump_day_price_source: "MEXC KTAUSDT UTC daily closes"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions:
  - address: "0xc0634090f2fe6c6d75e61be2b949464abb498973"
    label: "Keeta: Keeta (KTA) token contract"
    confidence: medium
    independent_corroboration: false
    basis: "Arkham contract label"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### KTA · Overall grade **3.5 / 10 · ❌ FAIL**

**Summary:** Keeta is a payments-focused layer-1 whose KTA token also trades as an ERC-20 on Base. No fee or revenue record on DefiLlama and none published by the project was found. KTA is down about 85% in a year and 97% from its Jun 2025 high. About 36% of the 1B supply is not yet circulating, and the team and treasury wallets are not published, so insider selling could not be tested. The Revenue gate fails.

**🚨 Top warning:** **No revenue reaches the token, and the 364M non-circulating KTA have no published wallets.** The pump test (MEXC KTAUSDT) found 47 pump days in the last year, but with no disclosed team wallets none could be checked.

**Sections passed: 0 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 1/10 | ❌ FAIL (hard gate) |
| 🏛️ Foundation & team | 5/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 4/10 | ❌ FAIL |
| 📉 Selling behavior | 4/10 | ❌ FAIL (not proven) |
| 📊 Tokenomics & supply | 4/10 | ❌ FAIL |
| 💧 Liquidity & market | 3/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 5/10 | ❌ FAIL |
| 🤝 Adoption & customers | 3/10 | ❌ FAIL |
| 🛡️ Security & audits | 5/10 | ❌ FAIL |
| ⚖️ Regulatory | 5/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 4/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 KTA · Keeta · 3.5 / 10 · ❌ FAIL

> **One line:** A payments chain with a big pitch and no measurable fee income; insider wallets unpublished.

| 📊 Market (CoinGecko `keeta`, 16 Nov 2026 ~3:00 PM MST) | 🔗 Chain |
|---|---|
| **Price** $0.045 | **Supply** 636M circulating / 1B max |
| **7d / 30d / 1y** 🔴 −7.2% / 🔴 −38.5% / 🔴 −85.1% | **Base ERC-20** `0xc063…8973` |
| **Market cap** $28.6M · **FDV** $45M | **Holders** not read (Basescan API needs a paid key) |
| **24h volume** $626k (top venues: Aerodrome (Base) $165k, Biconomy.com $113k, XT.COM $95.4k) |  |
| **ATH** $1.68 (2025-06-09) |  |
| **Pump days** 47 of 360 days (MEXC KTAUSDT UTC daily closes); latest 2026-09-12, 2026-09-13 |  |

---

## 💰 Revenue — Does it make money? · 1/10 · ❌ FAIL (hard gate)

- No fee or revenue record on DefiLlama and none published by the project was found.

**What it means:** Nothing to measure and nothing reaches holders. **1 → hard-gate FAIL.**

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** No burn, buyback, fee share or fee-funded staking yield was found; network fees are not reported.

## 🏛️ Foundation & team — Who is in charge? · 5/10 · ❌ FAIL

- Keeta is developed by Keeta Inc. ([site](https://keeta.com)); team pages name the founders, described here by role. Corporate filings were not read in this pass.

## 🪙 Foundation / team holdings — How many coins do they hold? · 4/10 · ❌ FAIL

- Team, investor and treasury allocations are not mapped to published wallets. ~364M KTA (36%) is outside circulating supply per CoinGecko. Not proven → **4**.

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL (not proven)

- No team or treasury wallet is published for the native chain or Base.
- No exchange-labelled deposit from a disclosed team or treasury wallet on a pump day was found in this pass, including in the Arkham batch b24 read (16 Nov 2026).

**What it means:** Not proven → **4**.

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from MEXC KTAUSDT UTC daily closes.

## 📊 Tokenomics & supply · 4/10 · ❌ FAIL

- 1B max supply, 636M circulating (CoinGecko). The unlock schedule was not verified on-chain.

## 💧 Liquidity & market · 3/10 · ❌ FAIL

- ~$0.6M a day, led by Aerodrome (Base), Biconomy.com, XT.COM, MEXC and Coinbase. Thin for a $29M market cap.

## 🧑‍💻 Product & development · 5/10 · ❌ FAIL

- Public code at [github.com/keetanetwork](https://github.com/keetanetwork). Mainnet throughput claims are self-reported [Tier B].

## 🤝 Adoption & customers · 3/10 · ❌ FAIL

- No independent payment-volume figure was found.

## 🛡️ Security & audits · 5/10 · ❌ FAIL

- No exploit found in this pass; audit reports were not located.

## ⚖️ Regulatory · 5/10 · ❌ FAIL

- US company; no enforcement action found.

## 📅 Catalysts & calendar · 4/10 · ❌ FAIL

- Remaining unlocks of ~364M KTA; dates not verified.

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | ⚪ Not tested: team and treasury wallets unpublished |
| Entity concentration | 🟡 ~36% not circulating, holders unknown |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Entity labels below come from Arkham batch b24 (signed-in read on 16 Nov 2026, page 1 of transfers): an Arkham label alone is medium confidence; an Etherscan name tag that agrees makes it high. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| [`0xc063…8973`](https://basescan.org/address/0xc0634090f2fe6c6d75e61be2b949464abb498973) | Keeta: Keeta (KTA) token contract | [Arkham](https://arkm.com/explorer/address/0xc0634090f2fe6c6d75e61be2b949464abb498973) contract label | medium | no | None: token contract page only; holder question not answered |

## 📚 Sources

- [Tier A] [CoinGecko `keeta`](https://www.coingecko.com/en/coins/keeta): price, supply, venues and description, read 16 Nov 2026
- [Tier A] MEXC KTAUSDT UTC daily closes via `scripts/pump_day_test.py` (47 pump days of 360); Binance returned HTTP 451, so the hierarchy fell through to this venue
- [Tier A] Token contract and [holders](https://basescan.org/token/0xc0634090f2fe6c6d75e61be2b949464abb498973#balances) on the chain explorer; top holders from the Ethplorer API; contract or EOA status from Etherscan v2 `eth_getCode`

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Entity labels for the top holders (Arkham batch b24) | [0xc063…8973](https://arkm.com/explorer/address/0xc0634090f2fe6c6d75e61be2b949464abb498973) | B | 16 Nov 2026 |
| Market data and venues | [CoinGecko `keeta`](https://www.coingecko.com/en/coins/keeta) | A | 16 Nov 2026 |
| Token contract and holders | [contract](https://basescan.org/token/0xc0634090f2fe6c6d75e61be2b949464abb498973) · [holders](https://basescan.org/token/0xc0634090f2fe6c6d75e61be2b949464abb498973#balances) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Team and treasury wallets** | Ask Keeta to publish them, or run an Arkham entity lookup on the largest Base holders | Arkham |
| 2 | **Base holder list** | Read Basescan holders with a paid key | Paid API |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior. Under the 16 Nov 2026 one-hop amendment, a transfer to an exchange counts as a sale only with a team-attributed exchange account, evidence of a sale, or no plausible published reason.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.

- Research only. Not investment advice.

## Nansen-month findings, 24 Nov 2026 (MST) — reported only, unscored

This appendix publishes findings from the desk's 24 Nov 2026 holder and treasury research. It does not change the v3 score, badge, gates, formula or `revenue_reaches_holders`. Labels marked **Nansen-labeled** come from one third-party labeler and are treated as leads. Under process rule P12, every Nansen balance or holder figure used here was checked against a direct on-chain read before use, and mismatches were discarded. Hypotheses are labelled **Unverified**. Times are MST.

### Tracking update: the monthly KTA releases are Sablier vesting-stream withdrawals; about 192M still unexplained
- [`0xb5d7…fe3b`](https://basescan.org/address/0xb5d78dd3276325f5faf3106cc4acc56e28e0fe3b) is not a foundation wallet. It is the Sablier Lockup vesting contract: its on-chain `name()` reads "Sablier Lockup NFT", and it is **Nansen-labeled** "Sablier: Vesting".
- **The streams (on-chain, Base):**
  - Its KTA sits in four non-cancelable Sablier streams, IDs 417–420, holding 600M KTA deposited on 5 Mar 2025. Two streams of 100M and one of 200M end on 5 Mar 2029; one of 200M ends on 5 Mar 2028.
  - Each stream's sender and recipient is [`0xbb76…92a3`](https://basescan.org/address/0xbb767517c6fcbbbb8cef73769d4034e77a9692a3), which is **Nansen-labeled** "Keeta: KTA Treasury" (owner Unverified).
  - About 240.0M has been withdrawn so far, and 359.98M remained on 24 Nov 2026.
- **Who withdraws:** an operator wallet, [`0xdbc0…7be9`](https://basescan.org/address/0xdbc0f78f4271c4ef8856ba0bedc0ea931b097be9), sends the withdraw calls. For example, the 12 Nov 2026, 10:09 PM MST withdrawal of 3,533,333.92 KTA ([tx `0xf27bf96c…`](https://basescan.org/tx/0xf27bf96c7270f2a39f2c246a68e47d23e9d766ffeb8eb5d411a74781d4b244f0)) explains the drop seen in the 16 Nov weekly check.
- **Reading:** the monthly releases are scheduled stream withdrawals to the stream owner. That this is Keeta's team or treasury vesting is **Unverified**, because there is no official wallet disclosure.
- **Still unexplained:**
  - `0xbb76…92a3` passes the released KTA on to the reported treasury [`0x5799…55ba`](https://basescan.org/address/0x57998b9a481421988135c47d82740d3e432855ba), the reported foundation wallet [`0x428d…8676`](https://basescan.org/address/0x428d28564f28804ece2353b943e6c89909dd8676), and the plain wallet [`0xc439…bec6`](https://basescan.org/address/0xc439eba7e79496f42e996f7ebd5835934f56bec6) (**Nansen-labeled** "Keeta").
  - `0xc439…bec6` pays fixed lots, often after a test send, to brand-new single-use wallets. For example, it sent 2.3M after a 20-KTA test send, then 1.44M and 100k. Several of those wallets are now empty, and their onward transfers were not captured.
  - **About 192M KTA released over 12 months has moved on this way, and where it ends up is not explained.** None of the endpoints has a public label, so it can't be called an exchange deposit.
- **Sources and method:**
  - The wallet sources for `0x5799…55ba` and `0x428d…8676` are community-reported (Reddit r/keeta, CryptoRank holders).
  - Original trace: 3 Nov 2026, free Base RPC. Stream reads: 24 Nov 2026.

### Holder mix (top 100 holders)
- Exchange share of the top 100 holders: **22.57%** of supply in Nansen-labeled exchange and DEX-pool wallets (Nansen holders pass, 24 Nov 2026).
- Issuer and other named holders: Issuer-related: 36.00% sits in the Nansen-labeled Sablier vesting contract. On-chain, that is four non-cancelable streams (600M KTA deposited 5 Mar 2025, ending 2028/2029) whose sender and recipient is the wallet Nansen labels "Keeta: KTA Treasury". That wallet holds a further 1.72% directly. A wallet Nansen labels "Keeta" holds 9.97%, and "KTA Custody Vaults" holds 1.42%.
- Checked on-chain: `balanceOf` / `totalSupply` read on each wallet named above (public Base RPC), 24 Nov 2026, about 4:35 AM MST; every figure matched. The Sablier contract's `name()` reads "Sablier Lockup NFT". The exchange share itself is Nansen's top-100 sum and was checked on-chain only through its largest wallets.
- Unscored: this line has no effect on the score, badge or ranking. Labels are Nansen's (a third-party labeler) and are leads, not confirmed ownership.
