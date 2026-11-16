---
ticker: LUMIA
name: Lumia (ex-Orion Protocol)
chain: ethereum + Lumia L2
contract: "0xd9343a049d5dbd89cd19dc6bca8c48fb3a0a42a7"
overall_score: 3.2
overall_verdict: FAIL
section_scores:
  revenue: 1
  foundation_team: 4
  insider_holdings: 3
  selling_behavior: 4
  tokenomics_supply: 4
  liquidity_market: 4
  product_development: 4
  adoption_customers: 2
  security_audits: 3
  regulatory: 5
  catalysts: 4
gates_failed: [revenue]
red_lines:
  hack_exploit: "none found"
  owner_burn_any_holder: "yes: burnFrom(account) is onlyOwner; owner 0xb10b260fbf5f33cc5ff81761e090aecdffcb1fd5 (3-of-4 Safe)"
  mint_path_live: "capped at 238,888,888 (already full); mint only after burns"
  team_wallet_to_exchange_during_pump: "not proven [relay wallets carry only generic Arkham tags; exchange endpoint Unverified]: ecosystem-Safe LUMIA relayed via 3 EOAs, the AggLayer bridge and an L2 relay to a high-volume L2 wallet that pays a Binance-labelled address; pump-day legs on 23 Dec 2025, 29 Apr and 23 Jun 2026"
  migration: "ORN→LUMIA converter enabled but holds 0 LUMIA"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "There is no fee or buyback stream; the L2's secured value is almost all LUMIA itself, so revenue does not reach holders."
pump_day_price_source: "Binance LUMIAUSDT UTC daily closes (Gate agrees)"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions:
  - address: "0xb10b260fbf5f33cc5ff81761e090aecdffcb1fd5"
    label: "Gnosis Safe (Whale); token owner() on-chain"
    confidence: medium
    independent_corroboration: true
    basis: "Arkham + RPC owner()"
  - address: "0x0ee999247f3e33406131bc6aa896192bd40cd6b7"
    label: "Generic Gnosis Safe (funded by owner Safe)"
    confidence: low
    independent_corroboration: false
    basis: "Arkham + Etherscan"
  - address: "0x2d7904788464a70f72628f632c75a7dd5fc8e57b"
    label: "Early LUMIA Holder (generic)"
    confidence: low
    independent_corroboration: false
    basis: "Arkham"
  - address: "0x74fb2aa81922cfb89f0574278557c25a995f699f"
    label: "Early LUMIA Holder (generic)"
    confidence: low
    independent_corroboration: false
    basis: "Arkham"
  - address: "0xa464bf835acb7dc775785e797740763804b56637"
    label: "Early LUMIA Holder (generic)"
    confidence: low
    independent_corroboration: false
    basis: "Arkham"
  - address: "0xfbaa4e673d0cd1159bed704fdc0e4379a41c2135"
    label: "Orion Protocol: OrionToLumiaConverter (verified)"
    confidence: high
    independent_corroboration: true
    basis: "Arkham + RPC"
price_usd: 0.077616
price_source: "CoinGecko, 16 Nov 2026 9:56 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### LUMIA · Overall grade **3.2 / 10 · ❌ FAIL**

**Summary:** Lumia is Orion Protocol rebranded (2024) as an RWA-focused Polygon AggLayer L2, with LUMIA as gas. Supply went from 100M ORN to a hard-capped **238,888,888 LUMIA**, all minted. The contract owner, a [3-of-4 Safe](https://etherscan.io/address/0xb10b260fbf5f33cc5ff81761e090aecdffcb1fd5) that also holds **18.47%** of supply, can call `burnFrom` on **any holder's** balance without approval. The official [ORN→LUMIA converter](https://etherscan.io/address/0xfbaa4e673d0cd1159bed704fdc0e4379a41c2135) reports conversion enabled but holds **0 LUMIA**, so conversions revert. 16.53M ORN sits in it. There is no measurable revenue: the L2's secured value is almost entirely LUMIA itself, and usage is under 0.01 ops/s [Tier B]. The key trace: ecosystem LUMIA from the owner Safe → a [2-of-3 Safe](https://etherscan.io/address/0x0ee999247f3e33406131bc6aa896192bd40cd6b7) → three EOAs → the AggLayer bridge → an L2 relay → a 14,685-transaction L2 wallet that pays the address Etherscan labels **Binance Cold Wallet 20**. Several legs fell on pump days.

**🚨 Top warning:** Treasury tokens reach a likely exchange hot wallet through a multi-hop relay that crosses to L2. On 23 Jun 2026, a pump day, [0x74fb…699f](https://etherscan.io/address/0x74fb2aa81922cfb89f0574278557c25a995f699f) moved 5M to [0xa464…6637](https://etherscan.io/address/0xa464bf835acb7dc775785e797740763804b56637), which bridged 5M and then sent seven 0.5M lots on L2 to the relay [0xd24f…b730](https://explorer.lumia.org/address/0xd24f7a7e86dccfcfd136437a094cc654f0c8b730). The owner Safe can burn anyone's LUMIA, and the migration contract is empty. Price is −43.6% in a year and −96.9% from ATH.

**Sections passed: 0 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 1/10 | ❌ FAIL |
| 🏛️ Foundation & team | 4/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 3/10 | ❌ FAIL |
| 📉 Selling behavior | 4/10 | ❌ FAIL (not proven) |
| 📊 Tokenomics & supply | 4/10 | ❌ FAIL |
| 💧 Liquidity & market | 4/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 4/10 | ❌ FAIL |
| 🤝 Adoption & customers | 2/10 | ❌ FAIL |
| 🛡️ Security & audits | 3/10 | ❌ FAIL |
| ⚖️ Regulatory | 5/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 4/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 LUMIA · Lumia (ex-Orion Protocol) · 3.2 / 10 · ❌ FAIL

> **One line:** A capped token with an owner burn-anyone key, a broken migration, and treasury relayed toward an exchange wallet.

| 📊 Market (CoinGecko, 16 Nov 2026 9:56 AM MST) | 🔗 On-chain (Blockscout / RPC / Lumia explorer, 16 Nov 2026) |
|---|---|
| **Price** $0.0776 · 30d −17.6% · 1y −43.6% | **Supply** 238,888,888 (cap reached) · 3,084 Ethereum holders |
| **Market cap** $18.5M · rank #806 | **AggLayer bridge** [0x2a3d…2ede](https://etherscan.io/address/0x2a3dd3eb832af982ec71669e178424b10dca2ede) holds 71.06% (bridged to L2) |
| **24h volume** $1.09M: LBank $0.39M, Binance $0.30M, Binance TRY $0.11M, CoinW, WEEX, MEXC | **Owner** [3-of-4 Safe](https://etherscan.io/address/0xb10b260fbf5f33cc5ff81761e090aecdffcb1fd5) · 18.47% |
| **ATH** $2.49 (Dec 2024) −96.9% · **Pump days** 57 in 365 (Binance LUMIA/USDT) | **Converter** enabled, LUMIA balance 0 · 16.53M ORN inside |

---

## 💰 Revenue — Does it make money? · 1/10 · ❌ FAIL

| Metric | Value | Source |
|---|---:|---|
| DefiLlama fees / TVL | Not listed | [Tier A] api.llama.fi |
| L2 total value secured | ~$14M, 99.9% LUMIA itself; <0.01 UOPS | [Tier B] ethbeat L2 tracker |

**What it means:** no revenue. **1 (hard gate).**

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** There is no fee or buyback stream; the L2's secured value is almost all LUMIA itself, so revenue does not reach holders.

## 🏛️ Foundation & team — Who is in charge? · 4/10 · ❌ FAIL

- Orion Protocol raised $7.8M in 2020, rebranded to Lumia (Feb 2024) and ran a node sale (Jul 2024) [Tier B].
- The ORN migration was left unfinished: the converter holds 16.53M ORN and 0 LUMIA (RPC). ORN `totalSupply` is still 100M [Tier A]. About 46% of ORN is reported unaccounted for [Unverified, single Tier B: [dossier](https://tokendossier.com/tokens/RWA/LUMIA)].

## 🪙 Foundation / team holdings — How many coins do they hold? · 3/10 · ❌ FAIL

| Holder | % supply | Note |
|---|---:|---|
| AggLayer unified bridge [0x2a3d…2ede](https://etherscan.io/address/0x2a3dd3eb832af982ec71669e178424b10dca2ede) | 71.06% | LUMIA on the L2 (gas token) |
| Owner Safe [0xb10b…1fd5](https://etherscan.io/address/0xb10b260fbf5f33cc5ff81761e090aecdffcb1fd5) (3-of-4) | 18.47% | sent 92.63M (legacy-swap pool) and 73.13M to [0x0ee9…d6b7](https://etherscan.io/address/0x0ee999247f3e33406131bc6aa896192bd40cd6b7) on 10 Sep 2024 ([0x252fa9f9…](https://etherscan.io/tx/0x252fa9f9cfb36c04a2c18da51c6a869be25d735d6a84d68e54f149828bd0c8dd)) |
| [0x0ee9…d6b7](https://etherscan.io/address/0x0ee999247f3e33406131bc6aa896192bd40cd6b7) Safe (2-of-3) | 0.24% | ecosystem-pool Safe [inferred from 73.13M ≈ 72.82M ecosystem allocation] |
| [0x8dad…E1C7](https://etherscan.io/address/0x8dad9806893500f4e30f2681503939ba638bE1C7) | 4.41% | fed by [0x2d79…e57b](https://etherscan.io/address/0x2d7904788464a70f72628f632c75a7dd5fc8e57b) |

- The project says 0% goes to the team [Tier B]. In practice, insider control runs through the two Safes.

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL (not proven)

*Binance LUMIA/USDT daily closes (UTC): 57 pump days in the last 365.*

| Leg | Transfer |
|---|---|
| Ecosystem Safe → EOA | [0x0ee9…d6b7](https://etherscan.io/address/0x0ee999247f3e33406131bc6aa896192bd40cd6b7) → [0x2d79…e57b](https://etherscan.io/address/0x2d7904788464a70f72628f632c75a7dd5fc8e57b): 30.0M over 365 days, incl. **6.40M on 23 Dec 2025 (pump day)** [0xf5e0b6e1…](https://etherscan.io/tx/0xf5e0b6e1f38eca4ccae068e891d23331c8bd9088b3013abc394a3d3fc0d566db) and 14.3M on 12 Jan 2026 [0x0f68443d…](https://etherscan.io/tx/0x0f68443df4315be3cbc57ae1a0f98211daa7fa0b70165d19f9d859f642ef4a62) |
| EOA → EOA | [0x2d79…e57b](https://etherscan.io/address/0x2d7904788464a70f72628f632c75a7dd5fc8e57b) → [0x74fb…699f](https://etherscan.io/address/0x74fb2aa81922cfb89f0574278557c25a995f699f) 27.6M; [0x2d79…e57b](https://etherscan.io/address/0x2d7904788464a70f72628f632c75a7dd5fc8e57b) → [0xa464…6637](https://etherscan.io/address/0xa464bf835acb7dc775785e797740763804b56637) **4.24M on 29 Apr 2026 (pump day)** [0xffb266b6…](https://etherscan.io/tx/0xffb266b6316ad243c6321895bc80016a2c39d0dec6295170f5489fd43bbc38a6) |
| EOA → EOA | [0x74fb…699f](https://etherscan.io/address/0x74fb2aa81922cfb89f0574278557c25a995f699f) → [0xa464…6637](https://etherscan.io/address/0xa464bf835acb7dc775785e797740763804b56637) **2×2.5M on 23 Jun 2026 (pump day)** [0xccbf6c02…](https://etherscan.io/tx/0xccbf6c02d5729f995619cf351015afccdfb17ff2795eaeafeba07f07fe7a5554) |
| → AggLayer bridge (to L2) | [0xa464…6637](https://etherscan.io/address/0xa464bf835acb7dc775785e797740763804b56637) → [0x2a3d…2ede](https://etherscan.io/address/0x2a3dd3eb832af982ec71669e178424b10dca2ede) 30.49M total, incl. 4.30M on 29 Apr [0xb4da640a…](https://etherscan.io/tx/0xb4da640ae7f661b5de6b4e530febe7942f565f5f47dfa7cb92b7d0e1bd6b8c1c) and 5M on 23 Jun [0x5c45603f…](https://etherscan.io/tx/0x5c45603f92e41cb6702e4e35f99d98d785ff7a034c8e5bbea1fd9a4e49c96ad0) |
| L2: → relay | [0xa464…6637](https://explorer.lumia.org/address/0xa464bf835acb7dc775785e797740763804b56637) → [0xd24f…b730](https://explorer.lumia.org/address/0xd24f7a7e86dccfcfd136437a094cc654f0c8b730) in 0.5M lots, seven on 23 Jun ([0x4f698790…](https://explorer.lumia.org/tx/0x4f698790fa06f6edf0cc129beee2aebc29bd9f5b2be4ba3f2091e4801de1e3c9)) |
| L2: relay → hot wallet | [0xd24f…b730](https://explorer.lumia.org/address/0xd24f7a7e86dccfcfd136437a094cc654f0c8b730) forwards each lot within minutes to [0x6831…f7b2](https://explorer.lumia.org/address/0x6831bd720bad232fb0dece27c836badb0751f7b2) (13.49M in the latest 50 transactions, e.g. [0xf6bf05bc…](https://explorer.lumia.org/tx/0xf6bf05bcc4694c21180d304b278e85c1b4f9568269cd0e1264a3163a0d7e2479)) |
| L2: hot wallet → Binance-labelled address | [0x6831…f7b2](https://explorer.lumia.org/address/0x6831bd720bad232fb0dece27c836badb0751f7b2) (14,685 transactions) pays [0xf977…acec](https://explorer.lumia.org/address/0xf977814e90da44bfa03b6295a0616a897441acec), the EOA Etherscan labels "Binance: Cold Wallet 20" (an EOA is one key on every EVM chain), e.g. 1.03M on 29 Oct [0xbda55907…](https://explorer.lumia.org/tx/0xbda55907ef7a5d72a4cadae651bf517e040fec7db572a9658f2fcad85c76aaa2) |

- That [0x6831…f7b2](https://explorer.lumia.org/address/0x6831bd720bad232fb0dece27c836badb0751f7b2) is a Binance hot wallet is [Unverified]; its flows to the Binance-labelled EOA make it likely.

- **Arkham (16 Nov 2026):** the owner Safe [0xb10b…1fd5](https://intel.arkm.com/explorer/address/0xb10b260fbf5f33cc5ff81761e090aecdffcb1fd5) and the ecosystem Safe [0x0ee9…d6b7](https://intel.arkm.com/explorer/address/0x0ee999247f3e33406131bc6aa896192bd40cd6b7) carry only generic Gnosis Safe / Whale tags, and the relay EOAs [0x2d79…e57b](https://intel.arkm.com/explorer/address/0x2d7904788464a70f72628f632c75a7dd5fc8e57b), [0x74fb…699f](https://intel.arkm.com/explorer/address/0x74fb2aa81922cfb89f0574278557c25a995f699f) and [0xa464…6637](https://intel.arkm.com/explorer/address/0xa464bf835acb7dc775785e797740763804b56637) carry only generic "Early LUMIA Holder" tags. None is labelled as Lumia or Orion. Arkham shows no exchange-labelled LUMIA transfer from any of them; the Ethereum legs end at the Polygon zkEVM (AggLayer) bridge. [Tier B] Arkham, read 16 Nov 2026 (signed-in account).
- Why this is not proven: the owner Safe is tied to the project on-chain (it is the token's `owner()`), but the Etherscan trail only shows it *funding* the ecosystem Safe, which then funds the relay EOAs. Funding does not prove who controls those wallets, the pump-day legs are wallet-to-wallet hops rather than exchange deposits, and the exchange endpoint on L2 is itself [Unverified]. Under the 16 Nov 2026 rule, generic low-confidence tags cannot hold the Selling gate, so Selling moves **3 → 4**. **Alternative:** if Lumia confirms the relays as its own, or the L2 wallet 0x6831 is shown to be a Binance deposit, Selling returns to 3.

**What it means:** treasury-funded supply is routed toward a likely exchange wallet, partly on pump days, but team control of the relays is not proven. **4 (not proven).**

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from Binance LUMIAUSDT UTC daily closes (Gate agrees).

## 📊 Tokenomics & supply · 4/10 · ❌ FAIL

- Hard cap 238,888,888, already minted; `mint` works only after burns.
- Node rewards (73.4M) vest over ~20 years and ecosystem rewards (72.8M) to 2034 [Tier B]. Governance proposal LGP-01 (Sep 2026) would buy back future HyperNode rewards at $0.09 [Tier B]. **4**.

## 💧 Liquidity & market · 4/10 · ❌ FAIL

- $1.09M of 24h volume on an $18.5M cap. LBank leads, then Binance (USDT and TRY).

## 🧑‍💻 Product & development · 4/10 · ❌ FAIL

- Mainnet since Feb 2025. Moved to pessimistic proofs in Oct 2025; listed with no data-availability bridge and a non-functional proof system by an L2 risk tracker [Tier B].

## 🤝 Adoption & customers · 2/10 · ❌ FAIL

- L2 activity is under 0.01 ops/s; secured value is almost entirely its own token.

## 🛡️ Security & audits · 3/10 · ❌ FAIL

- `burnFrom(address,uint256)` is `onlyOwner` (verified source): the 3-of-4 Safe can destroy any holder's LUMIA. The token audit never went past a preliminary report [Tier B]. **3**.

## ⚖️ Regulatory · 5/10 · ❌ FAIL

- No enforcement found.

## 📅 Catalysts & calendar · 4/10 · ❌ FAIL

| Date | Event |
|---|---|
| Q4 2026 | LGP-01 HyperNode rewards buyback vote |
| 18 Jan 2027 | ~3.5M LUMIA quarterly unlock [Tier B] |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | ⚪ Not proven: ecosystem Safe → generic-tagged relays → bridge → L2 wallet paying a Binance address; pump-day legs |
| Owner can burn any holder | 🔴 Yes (3-of-4 Safe) |
| Migration | 🔴 Converter enabled but empty |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| [0xb10b…1fd5](https://intel.arkm.com/explorer/address/0xb10b260fbf5f33cc5ff81761e090aecdffcb1fd5) | Gnosis Safe (Whale); token owner() on-chain | Arkham + RPC owner() | medium | yes (on-chain owner()) | Holdings: insider control |
| [0x0ee9…d6b7](https://intel.arkm.com/explorer/address/0x0ee999247f3e33406131bc6aa896192bd40cd6b7) | Generic Gnosis Safe (funded by owner Safe) | Arkham + Etherscan | low | funding only | None alone |
| [0x2d79…e57b](https://intel.arkm.com/explorer/address/0x2d7904788464a70f72628f632c75a7dd5fc8e57b), [0x74fb…699f](https://intel.arkm.com/explorer/address/0x74fb2aa81922cfb89f0574278557c25a995f699f), [0xa464…6637](https://intel.arkm.com/explorer/address/0xa464bf835acb7dc775785e797740763804b56637) | Early LUMIA Holder (generic) | Arkham | low | no | Selling 3 → 4 (cannot hold the gate) |
| [0xfbaa…2135](https://intel.arkm.com/explorer/address/0xfbaa4e673d0cd1159bed704fdc0e4379a41c2135) | Orion Protocol: OrionToLumiaConverter (verified) | Arkham + RPC | high | yes | None |

## 📚 Sources

- [Tier B] Arkham, read 16 Nov 2026 (signed-in account): the owner and ecosystem Safes, three relay EOAs and the converter
- [Tier A] Etherscan v2 transfers; Blockscout Ethereum holders and verified source; Ethereum RPC `owner()`, `getThreshold()`, `getOwners()`, `cap()`, converter `isConversionEnabled()` and balances; Lumia L2 Blockscout (explorer.lumia.org) addresses, counters and transactions
- [Tier A] Etherscan labels (Polygon Agglayer Unified Bridge; Binance Cold Wallet 20)
- [Tier B] [tokendossier LUMIA](https://tokendossier.com/tokens/RWA/LUMIA) · [Phemex: What is Lumia](https://phemex.com/academy/what-is-lumia) · [ethbeat Lumia Prism](https://ethbeat.org/layer2s/projects/lumia) · [CoinLaunch vesting](https://coinlaunch.space/projects/lumia/vesting/) · [CMC updates](https://coinmarketcap.com/cmc-ai/lumia/latest-updates/)
- [Tier A] CoinGecko `lumia` (16 Nov 2026 9:56 AM MST); Binance LUMIAUSDT daily klines (Gate agrees: 57)

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Ecosystem Safe → EOA on a pump day | [0xf5e0b6e1…](https://etherscan.io/tx/0xf5e0b6e1f38eca4ccae068e891d23331c8bd9088b3013abc394a3d3fc0d566db) | A | 16 Nov 2026 |
| Bridge leg on a pump day | [0x5c45603f…](https://etherscan.io/tx/0x5c45603f92e41cb6702e4e35f99d98d785ff7a034c8e5bbea1fd9a4e49c96ad0) | A | 16 Nov 2026 |
| L2 hot wallet → Binance-labelled EOA | [0xbda55907…](https://explorer.lumia.org/tx/0xbda55907ef7a5d72a4cadae651bf517e040fec7db572a9658f2fcad85c76aaa2) | A | 16 Nov 2026 |
| Converter empty | [0xfbaa…2135](https://etherscan.io/address/0xfbaa4e673d0cd1159bed704fdc0e4379a41c2135) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Who controls the relay EOAs** (0x2d79, 0x74fb, 0xa464) | Arkham (16 Nov 2026) shows only generic Early LUMIA Holder tags; ask Lumia | Free |
| 2 | **Confirm the L2 hot wallet entity** | Arkham on [0x6831…f7b2](https://explorer.lumia.org/address/0x6831bd720bad232fb0dece27c836badb0751f7b2); Binance LUMIA deposit network | Free |
| 3 | **Where 0x8dad… came from** | Its two inbound transfers | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
