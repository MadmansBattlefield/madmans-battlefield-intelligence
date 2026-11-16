---
ticker: AEON
name: AEON (agentic settlement, aeon.xyz)
chain: bsc
contract: "0x277add739c6e0477616948357af9e79fe1ec9b80"
overall_score: 3.3
overall_verdict: FAIL
section_scores:
  revenue: 2
  foundation_team: 5
  insider_holdings: 3
  selling_behavior: 4
  tokenomics_supply: 3
  liquidity_market: 3
  product_development: 4
  adoption_customers: 2
  security_audits: 4
  regulatory: 5
  catalysts: 3
gates_failed: [revenue]
red_lines:
  identity_caveat: "three CoinGecko ids named AEON; this report covers aeon-3 = BSC 0x277add739c6e0477616948357af9e79fe1ec9b80 (aeon.xyz)"
  hack_exploit: "none found"
  mint_path_live: "yes, MinterRole with no cap; current minter not identified"
  team_wallet_to_exchange_during_pump: "not proven: the Safe emptied 45.6M AEON to EOA 0xfd6a on 3 Sep 2026 (not a pump day); 0xfd6a then sent 15M to a Bitget deposit and ~31M to Cobo deposits on 14, 15 and 29 Oct 2026, none pump days; its one pump-day transfer (3M, 21 Sep) went to a contract that still holds it"
  treasury_in_single_key_wallets: "no: vesting owner is a 6-of-10 Safe 0xd8a63d36f9474f361d77c31e6d53d5c78c92add4; it can revoke ~76.6% of supply"
methodology_2026_11_16:
  revenue_reaches_holders: "no"
  disclosure_quality: not_applicable
  pump_day_undisclosed_penalty_applied: false
  pump_day_price_source: "Gate AEON_USDT and Bitget AEONUSDT UTC daily closes"
  dual_review: not_run
price_usd: 0.0231
price_source: "CoinGecko, 16 Nov 2026 9:11 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### AEON · Overall grade **3.3 / 10 · ❌ FAIL**

**Summary:** ⚠️ **Identity caveat:** CoinGecko lists three coins named AEON. This report covers id `aeon-3`, BSC contract [0x277a…9b80](https://bscscan.com/address/0x277add739c6e0477616948357af9e79fe1ec9b80), the "agentic economy" settlement token from aeon.xyz (TGE 27 Jul 2026). DefiLlama's `aeon` slug is a different project (aeon.fun). AEON pitches x402 / AI-agent payments and claims 2M users. On-chain, its published x402 facilitator signer [0xe91e…5036](https://bscscan.com/address/0xe91e0e6080b0c19c71b616e628d7b715313d5036) has nonce **575,885 on BSC**, up just **59** since 2 Aug 2026, and **46** on Base. All six vesting contracts (~76.6% of supply) are `revocable` by one [6-of-10 Safe](https://bscscan.com/address/0xd8a63d36f9474f361d77c31e6d53d5c78c92add4). On 3 Sep that Safe sent its entire unlocked **45.6M AEON** to an unlabeled EOA ([tx](https://bscscan.com/tx/0x3bae8d5cd3899c23e84411a1a224bf2f2d4b43a1fe98dcc1a295d7585aadc3d8)), which has since dispersed all but 1.08M. Revenue trips the hard gate.

**🚨 Top warning:** Revocable vesting: one 6-of-10 Safe can claw back about 766M AEON in a single transaction, with no timelock. The token has an uncapped MinterRole and is pausable. The Safe's unlocked 45.6M went to EOA [0xfd6a…19b8](https://bscscan.com/address/0xfd6a0c523ed829a21281a2a3e627ad242ab619b8) on 3 Sep 2026, and only 1.08M remains there. Price is −87.7% from its 27 Jul ATH in under four months.

**Sections passed: 0 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 2/10 | ❌ FAIL |
| 🏛️ Foundation & team | 5/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 3/10 | ❌ FAIL |
| 📉 Selling behavior | 4/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 3/10 | ❌ FAIL |
| 💧 Liquidity & market | 3/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 4/10 | ❌ FAIL |
| 🤝 Adoption & customers | 2/10 | ❌ FAIL |
| 🛡️ Security & audits | 4/10 | ❌ FAIL |
| ⚖️ Regulatory | 5/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 3/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 AEON · AEON (agentic settlement, aeon.xyz) · 3.3 / 10 · ❌ FAIL

> **One line:** A new AI-payments token whose settlement layer barely settles, with fully revocable insider vesting.

| 📊 Market (CoinGecko `aeon-3`, 16 Nov 2026 9:11 AM MST) | 🔗 On-chain (BSC RPC / Safe API, 16 Nov 2026) |
|---|---|
| **Price** $0.0231 · 30d −38.6% · ATH $0.1875 (27 Jul 2026) −87.7% | **Supply** 1,000,000,000 (8 decimals) · MinterRole, no cap |
| **Market cap** $5.80M · FDV $23.1M · circ 250.9M | **Vesting owner** [6-of-10 Safe](https://bscscan.com/address/0xd8a63d36f9474f361d77c31e6d53d5c78c92add4) · Safe balance 0 |
| **24h volume** $1.95M: LBank $0.99M (~50%), PancakeSwap $0.30M, Bitget, OKX, Bithumb | **Team vesting** [0xeac0…80b6](https://bscscan.com/address/0xeac0b41cc7485fca6cfdf2ab145895e43dfb80b6): 200M, released 0, revocable |
| **Pump days** 17 in 113 trading days (Gate AEON/USDT, data from 27 Jul 2026) | **x402 signer** nonce 575,885 (BSC), 46 (Base) |

---

## 💰 Revenue — Does it make money? · 2/10 · ❌ FAIL

| Metric | Value | Source |
|---|---:|---|
| DefiLlama fees | Not listed (the `aeon` slug is aeon.fun, a different project) | [Tier A] api.llama.fi |
| x402 facilitator settlements | +59 on BSC between 2 Aug and 16 Nov 2026; 46 lifetime on Base | [Tier A] RPC nonce of [0xe91e…5036](https://bscscan.com/address/0xe91e0e6080b0c19c71b616e628d7b715313d5036); Aug baseline [Tier B] [dossier](https://tokendossier.com/tokens/AI/AEON) |
| Claimed 30M monthly transactions | Not visible on-chain | [Unverified] |

**What it means:** no measurable protocol revenue. **2 (hard gate).**

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** No protocol fee burn, automatic buyback, staking yield from fees or fee share is live, so revenue does not reach holders.

## 🏛️ Foundation & team — Who is in charge? · 5/10 · ❌ FAIL

- The predecessor, AEON Pay (emerging-market merchant acquiring), pivoted to AI-agent settlement in Oct 2025. An $8M pre-seed led by YZi Labs, with IDG Capital and HashKey [Tier B ×2: CoinGecko project description; [dossier](https://tokendossier.com/tokens/AI/AEON)]. The team is reported as public.

## 🪙 Foundation / team holdings — How many coins do they hold? · 3/10 · ❌ FAIL

| Bucket | AEON | Vesting | Source |
|---|---:|---|---|
| Team | 200,000,000 | [0xeac0…80b6](https://bscscan.com/address/0xeac0b41cc7485fca6cfdf2ab145895e43dfb80b6): start Aug 2027, 47 months, revocable, released 0 | [Tier A] RPC |
| Ecosystem / Foundation / Marketing remainders | ~393M across 3 contracts | linear from Aug–Sep 2026 | [Tier B] dossier |
| Pre-seed / Angel | 123.2M / 50M | start Aug 2027, 35 months | [Tier B] dossier; [tokenomics.com](https://app.tokenomics.com/tokenomics/aeon) |
| [0x8de0…2b42](https://bscscan.com/address/0x8de06d956f1ba5cd83d00777f515ab95ccd82b42) (Arkham tags "AEON", "Whale"; no entity name) | 25,000,000 | none (35M on 2 Aug; 10M to Cobo deposits on 29 Oct) | [Tier A] RPC; baseline [Tier B] |

- Every vesting contract's owner is the Safe (team contract verified: `owner()` = [0xd8a6…add4](https://bscscan.com/address/0xd8a63d36f9474f361d77c31e6d53d5c78c92add4), `revocable()` = true).
- Of the 1B supply, ~76.6% sits in revocable vesting.

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL

*Gate AEON/USDT daily closes (UTC): 17 pump days since listing (113 days).*

- The Safe received 45.6M AEON at launch ([tx](https://bscscan.com/tx/0xe027154b86e6b24f499d51233479d2ddf05bba3b00c24ad734a73db93ba0599f), 25 Jul 2026). On **3 Sep 2026** it sent all 45.6M to EOA [0xfd6a…19b8](https://bscscan.com/address/0xfd6a0c523ed829a21281a2a3e627ad242ab619b8) ([tx](https://bscscan.com/tx/0x3bae8d5cd3899c23e84411a1a224bf2f2d4b43a1fe98dcc1a295d7585aadc3d8)). That was not a pump day (Gate close $0.0544, versus $0.0629 on 31 Aug).
- Arkham shows [0xfd6a…19b8](https://intel.arkm.com/explorer/address/0xfd6a0c523ed829a21281a2a3e627ad242ab619b8) as **unlabelled**, first funded by [0x7D7e…3D27](https://intel.arkm.com/explorer/address/0x7D7e7fD485C27D8547e1C8C906f7A8AA528c3D27) (one of the Safe's signer tags), and also receiving TokenVesting releases. BSC transfer logs (UTC) show where the 45.6M went:
  - **21 Sep 2026** (a pump day: Gate +14.6%, Bitget +20.6%): 1M + 2M to contract [0xc818…35c9](https://bscscan.com/address/0xc8189537aed663d3a13e6ea1cc3800ae9ae235c9) ([tx](https://bscscan.com/tx/0xfb1f810d7f478f759b6aa4e13173f4a95013848a538f034a2bfca4a73efe3997), [tx](https://bscscan.com/tx/0x4595ff677aa82fcd1970269ec0decd5b886230d978e22555fcb1f2756bf8842b)). That contract still holds ~4.0M AEON and has sent none, so this was not an exchange deposit.
  - **14 Oct 2026** (Gate −35.3%, Bitget −31.9%): 3 × 5M to Bitget Deposit [0x7b71…017e](https://intel.arkm.com/explorer/address/0x7b71a5f9a07a3f38a22538c2e4b753316058e17e) ([tx](https://bscscan.com/tx/0xfe30ed07d8540b43539f8a1154746922bc447f0a64b052f22d7c452e185304e3)); 18.67M to [0x01d6…ede0](https://bscscan.com/address/0x01d64ad9af3d2f1c94cf6b22baa294204fe5ede0) ([tx](https://bscscan.com/tx/0x5c99db65cfde785bc15febc882aaee9f65c2064b980cbc7c970caebd1ebae807)), which forwarded it to [Cobo.com: Custody Hot Wallet 0xb0b1…aa77](https://intel.arkm.com/explorer/address/0xb0b1177e8b32bfb9744c50f1350c6a614cc1aa77).
  - **15 Oct 2026** (Gate −31.2%, Bitget −33.9%): 4M + 4M + 3.64M to Cobo Deposit [0xdbfb…8a87](https://intel.arkm.com/explorer/address/0xdbfb07fffcf7e467af671bb48dc2828eb47e8a87) ([tx](https://bscscan.com/tx/0x81cccc1f1a242940a13f4a11429caf34d349a0adec672294dcbc373023e8e454)).
  - **29 Oct 2026** (Gate −13.5%, Bitget −20.8%): 750.7K to the same Cobo deposit ([tx](https://bscscan.com/tx/0x41be7e9c61f2b0a5d798f867b5c23133ad84e9ffcecc282feb1a62651304e4bf)).
  - Lookalike zero-value transfers to addresses imitating the Bitget and Cobo deposits (address poisoning) are ignored.
- [0x8de0…2b42](https://bscscan.com/address/0x8de06d956f1ba5cd83d00777f515ab95ccd82b42) (Arkham tags "AEON" and "Whale", no entity name, [Arkham](https://intel.arkm.com/explorer/address/0x8de06d956f1ba5cd83d00777f515ab95ccd82b42)) fell from 35M to 25M on **29 Oct 2026**: 5M to Cobo Deposit [0xdbfb…8a87](https://intel.arkm.com/explorer/address/0xdbfb07fffcf7e467af671bb48dc2828eb47e8a87) and 5M to Cobo Deposit [0xefb7…e8a5](https://intel.arkm.com/explorer/address/0xefb7472554da5e154cdacf695f67b2c46f83e8a5) ([tx](https://bscscan.com/tx/0x2f65aecea7e830cb69c02b21883e1f479fb43926319229ac860c58903429e59a)), not a pump day; it received gas from a Cobo custody hot wallet.

**What it means:** a team-linked wallet moved ~46M AEON into Bitget and Cobo deposits during a 30%+ slide, but none on a pump day, and its one pump-day transfer went to a contract that still holds it. Cobo deposits are custody, not proof of a sale. Pump-day selling is not proven. **4**.

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from Gate AEON_USDT and Bitget AEONUSDT UTC daily closes.

## 📊 Tokenomics & supply · 3/10 · ❌ FAIL

- The token is OpenZeppelin ERC20 with MinterRole, PauserRole and Burnable, with **no cap** (verified ABI: `mint`, `addMinter`, `pause`). The Safe is not a minter (`isMinter` = false), so the minter is unidentified.
- Fixed-supply claims rest only on the 1B total so far. **3**.

## 💧 Liquidity & market · 3/10 · ❌ FAIL

- $1.95M of 24h volume on a $5.8M cap. LBank prints about 50% of it. The token is under four months old and −87.7% from ATH.

## 🧑‍💻 Product & development · 4/10 · ❌ FAIL

- facilitator.aeon.xyz is live and lists BSC, Base, X Layer and Solana [Tier B], but settles almost nothing.

## 🤝 Adoption & customers · 2/10 · ❌ FAIL

- 59 BSC settlements in 3.5 months contradicts the claimed 30M monthly transactions.

## 🛡️ Security & audits · 4/10 · ❌ FAIL

- No exploit found. The control surface is uncapped mint, pause, and revocable vesting via the 6-of-10 Safe, with a pending `swapOwner` proposal in the Safe queue (Safe Transaction Service).

## ⚖️ Regulatory · 5/10 · ❌ FAIL

- No enforcement found.

## 📅 Catalysts & calendar · 3/10 · ❌ FAIL

| Date | Event |
|---|---|
| Monthly | Ecosystem / Foundation / Marketing linear unlocks (~8.8M a month) [Tier B] |
| Aug 2027 | Team, pre-seed and angel vesting begins (373M) |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | 🟡 Not proven: 45.6M → EOA → Bitget and Cobo deposits on 14, 15 and 29 Oct (not pump days) |
| Live mint path | 🔴 MinterRole, no cap; minter unidentified |
| Revocable vesting | 🔴 ~76.6% revocable by one 6-of-10 Safe |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| [0xd8a6…add4](https://intel.arkm.com/explorer/address/0xd8a63d36f9474f361d77c31e6d53d5c78c92add4) | Safe (6-of-10), 10 signer tags; owner of all vesting contracts | Arkham + RPC `owner()` | high | yes (on-chain) | Holdings (revocable vesting) |
| [0xfd6a…19b8](https://intel.arkm.com/explorer/address/0xfd6a0c523ed829a21281a2a3e627ad242ab619b8) | Unlabelled EOA; funded by a Safe signer; received the Safe's 45.6M | Arkham + BSC logs | medium (team link is on-chain flow, no label) | on-chain flows only | None: Selling stays 4 |
| [0x7b71…017e](https://intel.arkm.com/explorer/address/0x7b71a5f9a07a3f38a22538c2e4b753316058e17e) | Bitget Deposit | Arkham | medium | no | None (not a pump day) |
| [0xdbfb…8a87](https://intel.arkm.com/explorer/address/0xdbfb07fffcf7e467af671bb48dc2828eb47e8a87), [0xefb7…e8a5](https://intel.arkm.com/explorer/address/0xefb7472554da5e154cdacf695f67b2c46f83e8a5), [0xb0b1…aa77](https://intel.arkm.com/explorer/address/0xb0b1177e8b32bfb9744c50f1350c6a614cc1aa77) | Cobo.com deposits / Custody Hot Wallet | Arkham; on-chain sweep 0x01d6 → 0xb0b1 | medium | no | None (custody) |
| [0x8de0…2b42](https://intel.arkm.com/explorer/address/0x8de06d956f1ba5cd83d00777f515ab95ccd82b42) | Tags "AEON", "Whale" (no entity name) | Arkham | low | no | None |
| [0xe91e…5036](https://intel.arkm.com/explorer/address/0xe91e0e6080b0c19c71b616e628d7b715313d5036) | Unlabelled; first funder SWFT Swap | Arkham | low | no | None (Arkham does not tag it as an x402 facilitator) |

## 📚 Sources

- [Tier B] Arkham, read 16 Nov 2026 (signed-in account): the vesting Safe, 0xfd6a, 0x8de0, the team TokenVesting contract, the x402 signer, and the Bitget and Cobo deposits; exact dates from BSC transfer logs (public RPC)
- [Tier A] BSC RPC (`balanceOf`, `isMinter`, `getThreshold`, `getOwners`, `nonce`, vesting `owner`/`revocable`/`released`); Base RPC nonce; BSC verified ABI
- [Tier A] Safe Transaction Service (transfers and queued transactions of the Safe)
- [Tier B] [tokendossier AEON deep dive](https://tokendossier.com/tokens/AI/AEON) (2 Aug 2026 baseline) · [tokenomics.com](https://app.tokenomics.com/tokenomics/aeon) · [AEON whitepaper](https://web3-revolution.gitbook.io/aeon-whitepaper/tokenomics/usdaeon)
- [Tier A] CoinGecko `aeon-3` (16 Nov 2026 9:11 AM MST); Gate AEON/USDT daily candles; DefiLlama

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Safe sent all 45.6M AEON to an EOA | [tx](https://bscscan.com/tx/0x3bae8d5cd3899c23e84411a1a224bf2f2d4b43a1fe98dcc1a295d7585aadc3d8) | A | 16 Nov 2026 |
| Team vesting revocable by the Safe | [0xeac0…80b6](https://bscscan.com/address/0xeac0b41cc7485fca6cfdf2ab145895e43dfb80b6) | A | 16 Nov 2026 |
| x402 signer nearly idle | [0xe91e…5036](https://bscscan.com/address/0xe91e0e6080b0c19c71b616e628d7b715313d5036) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Arkham attribution of the AEON wallets** | Done 16 Nov 2026: the Safe's signer tags, the Bitget and Cobo deposits and the "AEON"/"Whale" tag are recorded; 0xfd6a stays unlabelled. Ask AEON to publish its treasury and market-making wallets | Free |
| 2 | **What contract [0xc818…35c9](https://bscscan.com/address/0xc8189537aed663d3a13e6ea1cc3800ae9ae235c9) is** | Read its verified source on BscScan (browser) | Free |
| 3 | **Who holds MinterRole** | MinterAdded events since deploy block 111,448,773 | API plan |
| 4 | **Which AEON is intended** | Confirm the `aeon-3` mapping in the scan list | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
