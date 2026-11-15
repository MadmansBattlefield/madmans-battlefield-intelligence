---
ticker: SERV
name: OpenServ
chain: ethereum
contract: "0x40e3d1A4B2C47d9AA61261F5606136ef73E28042"
bridged_copy_base: "0x5576D6ed9181F2225afF5282Ac0ED29f755437Ea"
overall_score: 2.8
overall_verdict: FAIL
section_scores:
  revenue: 2
  foundation_team: 3
  insider_holdings: 3
  selling_behavior: 1
  tokenomics_supply: 4
  liquidity_market: 4
  product_development: 5
  adoption_customers: 2
  security_audits: 3
  regulatory: 3
  catalysts: 3
gates_failed: [revenue, selling_behavior]
red_lines:
  treasury_sells_into_pumps: tripped
  treasury_to_exchange: tripped_10M_to_MEXC_11_Nov_2026
  owner_can_freeze_transfers: present_unused
  blacklist: present_unused
  burns_since_10_Oct: none
price_usd: 0.01242
price_source: "CoinGecko, 14 Nov 2026 12:12 PM MST"
chain_read_block_eth: 26415266
last_updated: 2026-11-14
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### SERV · Overall grade **2.8 / 10 · ❌ FAIL**

**Summary:** No revenue can be seen on-chain, and there have been no burns since 10 Oct. Meanwhile a treasury wallet named in the docs has sold about 12.2M SERV into Uniswap since January, including on pump days. On 21 and 31 Oct the main treasury Safe pulled 212M SERV out of vesting, then on 11 Nov sent 10M to MEXC through a fresh wallet.

**Sections passed: 0 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 2/10 | ❌ FAIL |
| 🏛️ Foundation & team | 3/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 3/10 | ❌ FAIL |
| 📉 Selling behavior | 1/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 4/10 | ❌ FAIL |
| 💧 Liquidity & market | 4/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 5/10 | ❌ FAIL |
| 🤝 Adoption & customers | 2/10 | ❌ FAIL |
| 🛡️ Security & audits | 3/10 | ❌ FAIL |
| ⚖️ Regulatory | 3/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 3/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 SERV · OpenServ · 2.8 / 10 · ❌ FAIL

> **One line:** No revenue can be seen on-chain, and there have been no burns since 10 Oct. Meanwhile a treasury wallet named in the docs has sold about 12.2M SERV into Uniswap since January, including on pump days. On 21 and 31 Oct the main treasury Safe pulled 212M SERV out of vesting, then on 11 Nov sent 10M to MEXC through a fresh wallet.

⚠️ **The Ethereum token is canonical.** The Base token is a Wormhole-bridged copy (lock-and-mint).

| 📊 Market (CoinGecko + DexScreener, 14 Nov 2026 ~12:12–12:40 PM MST) | 🔗 On-chain (Ethereum block 26,415,266 · Base 57,467,762) |
|---|---|
| **Price** $0.01242 | **Token** `0x40e3…8042` OpenServ.sol, Solidity 0.8.21, verified · no mint, no proxy |
| **24h / 7d / 30d** 🔴 −3.4% / −15.4% / −34.8% | **Supply** 1,000,000,000 fixed |
| **Market cap** $9.56M · **FDV** $12.42M | **Owner** Safe `0x42CA…f168`, **2 of 5**, nonce 177 |
| **24h volume** $558k | **Owner Safe holds** 206,203,533 (20.62%) + 1,051,635 on Base |
| **ATH** $0.139 (20 Dec 2024) · now −91% | **Fees** buy 0 / sell 0 (cap 5% each side) |
| **Holders** 6,676 (Blockscout) | **Base copy** 95,014,551 vs 95,019,642 locked in the Wormhole bridge |

---

## 💰 Revenue — Does it make money? · 2/10 · ❌ FAIL

| Metric | Value | Source |
|---|---:|---|
| Stated model | "25% of all SERV Reasoning API revenue is used to market-buy and burn $SERV". Same 25% rule for Build, enterprise, and launchpad LP trading fees. Launch key paid in SERV | [Tier A] [docs.openserv.ai/what-is-serv/the-serv-token](https://docs.openserv.ai/what-is-serv/the-serv-token) (fetched 14 Nov 2026) |
| Revenue figures | **Not published.** No DefiLlama listing | [Tier A] (absence) |
| Burned, Ethereum dead address | 55.57 SERV (same on 10 Oct) | [Tier A] `balanceOf(0x…dEaD)` |
| Burned, Base dead address | 206,764 SERV (same on 10 Oct) | [Tier A] |
| Burns in last 35 days | **0** | Calculated |
| Total burned to date | ~206.8k SERV ≈ **0.02% of supply** (~$2.6k) | Calculated |
| Staking ("platform dividend") | "(Coming)" | [Tier A] docs |

**What it means:** The docs promise buy-and-burn. The chain shows no burns at all in five weeks, and no revenue is disclosed.

## 🏛️ Foundation & team — Who is in charge? · 3/10 · ❌ FAIL

| Item | Finding | Source |
|---|---|---|
| Entity | "OpenServ Inc., Bloc Office Hub, Fifth Floor, Santa Maria Business District, Panama". **No registry record retrieved** | [Tier A] docs · registry [Unverified] |
| Signers claimed | "secured by a multisig wallet requiring five board-level signers" | [Tier A] docs |
| Signers on-chain | **2 of 5**: `0x4a48…23e1`, `0x5964…d3c9`, `0xe4ef…57de`, `0x8db4…00f6` (token deployer), `0x4005…5072` | [Tier A] `getThreshold` = 2, `getOwners` |
| Published treasury addresses | Safe `0x42CA…f168` · `0xeF6A15b3…779e` (**plain wallet**) · `0x9193f0B6…3376` (**plain wallet**) | [Tier A] docs + Blockscout (`is_contract` = false) |
| Named founder (Tim Hafner) | From third-party trackers | [Unverified] |
| Priced round / VCs | Not found | [Unverified] |

**What it means:** Two keys move everything. Two of the three "multisig-secured" treasury addresses are single-key wallets.

## 🪙 Foundation / team holdings — How many coins do they hold? · 3/10 · ❌ FAIL

| Wallet | Role | 10 Oct 2026 | 14 Nov 2026 | % supply | Locked? |
|---|---|---:|---:|---:|---|
| `0x42CAb3696a60C6Fc51381Bb533797E4121e1f168` | Owner / treasury Safe (2/5) | 3,695,716 | **206,203,533** | 20.62% | 🔓 liquid |
| same Safe on Base | | 1,051,635 | 1,051,635 | 0.11% | 🔓 |
| Sablier V2 LockupTranched `0xf86B3590…` | Vesting | 130,000,000 | **0** (paid to Safe 21 Oct) | 0% | — |
| Sablier V2 LockupLinear `0x3962f658…` | Vesting | 100,000,000 | 15,381,348 | 1.54% | 🔒 streaming to the Safe (~0.2M/day) |
| `0xeF6A15b3…779e` | Docs "treasury" (plain wallet) | 16,976 + 657,935 Base | 16,515 + 427,474 Base | 0.04% | 🔓 |
| `0x9193f0B6…3376` | Docs "treasury" (plain wallet) | 533,455 | **0** | 0% | 🔓 (sold out, see below) |
| `0xeD16D0Fe…9479` | Safe, owner [Unverified] | 8,093,307 | 8,093,307 | 0.81% | 🔓 |

**Vesting releases into the Safe** ([Tier A] Blockscout transfer log):

| Date (UTC) | From | Amount | Tx |
|---|---|---:|---|
| 21 Oct 2026 08:45 | Sablier Tranched | **130,000,000** | `0x6a0e8d9d58ca…` |
| 31 Oct 2026 02:07 | Sablier Linear | **82,098,553** | `0xa7fd135f6d62…` |
| 5–13 Nov 2026 | Sablier Linear (daily) | ~0.2–0.95M per day | e.g. `0x9343902a8f44…` |

**What it means:** The treasury went from ~0.4% to ~21% of supply liquid in three weeks, all controlled by two keys.

## 📉 Selling behavior — Do insiders sell into pumps? · 1/10 · ❌ FAIL

**Pump test:** 95 of 360 days in the last year had a ≥10% 5-day rise (CoinGecko daily closes). The most recent were 4 Nov (+16.3%) and 5 Nov (+11.1%).

### A. A docs-listed treasury wallet sells into Uniswap every day

`0x9193f0B639097e2AD0f22E5692Cd10e3A28a3376` (published as a treasury address) is refilled by the owner Safe, then sells ~40–90k SERV a few times a day into the main pools (`0x9C7e…CbB` Uniswap V3, `0xB771…600E` Uniswap V2, CoW Swap, Uniswap V4):

| Item | Value |
|---|---:|
| Safe → `0x9193…` refills since Jan 2026 | 5.0M (16 Jan) · 2.73M (22 Apr) · 1.25M (9 Sep) · 1.5M (26 Sep, two sends) · 1.0M (13 Oct) · 1.5M (3 Nov) |
| SERV sent from `0x9193…` to DEX pools, Jan–Nov 2026 | **12,233,122** |
| …of which on **pump days** | **3,163,928 in 46 swaps** |
| By month | Jan 2.16M · Feb 2.43M · Mar 3.12M · Apr 0.50M · May 1.02M · Sep 1.04M · Oct 1.81M · Nov 0.17M |
| Example pump-day swaps | 21 Sep `0x301aeebf335a…` (+40.6%) · 22 Sep 339,622 to `0xD54e…` (+62.1%) · 23 Sep `0x75ea73008328…` (+58.7%) · 4 Nov 00:24 `0x8de4bcbe9a23…` (+16.3%) |
| Other pump-day outflow | 4 Nov 06:26: 1,084,000 to `0x8210…` (unlabeled) |
| Balance now | 0 |

### B. Safe → fresh wallet on a pump day → daily sells

| Time (UTC) | Tx | What happened |
|---|---|---|
| 5 Nov 2026 02:28 | `0xdfb8916bfd9a…` | Safe sent 1,500,000 to `0x406b510F688d113c0A78d2a7B3af6a438b6B1aEb` (5-day move **+11.1%**) |
| 5 Nov 02:30 | `0xbe6c1e869e21…` | 100,000 to `0x1111…1605` (unlabeled) |
| 6–13 Nov | 26 transfers, e.g. `0x080981ed1d58…` | **1,215,000** sold into Uniswap V3/V2, ~70–80k per swap |
| 14 Nov | — | 185,000 left on Ethereum, 40,000 on Base |

### C. Safe → fresh wallet → MEXC

| Time (UTC) | Tx | Amount |
|---|---|---:|
| 11 Nov 2026 15:57 / 16:20 | `0xeb85533b141a…` / `0x41133022e49b…` | Safe → `0x56F966721FdA11F95ee8C0bd5b031751f682fF47`: 10,000 + 9,990,000 |
| 11 Nov 16:03 / 16:22 | `0xb4bc23558460…` / `0xddb18a93b9aa…` | `0x56F9…` → **MEXC 21** `0x9642b23E…` (exchange label, Blockscout): 10,000 + 9,990,000 |

- 11 Nov was not a pump day (price was falling, $0.01289). Whether MEXC sold it cannot be seen on-chain.

**What it means:** Yes. Treasury wallets sell into the open market almost daily, including on pump days, and 10M went to an exchange two days ago. None of it was announced. The addresses are published, but the sales are not.

## 📊 Tokenomics & supply · 4/10 · ❌ FAIL

| Item | Value | Source |
|---|---|---|
| Supply | 1,000,000,000 fixed (constructor), no mint, no proxy | [Tier A] verified source |
| Freeze switch | `closeTrade()` (`onlyOwner`) sets `launched = false`, which blocks holder transfers | [Tier A] source L280–283, L189–191 |
| Blacklist | `isBlackListed`, owner-controlled. Never used | [Tier A] |
| Tax switch | `setFees`, ≤5% per side. Now 0 / 0 (`buyTotalFees()` = 0, `sellTotalFees()` = 0, 14 Nov) | [Tier A] live read |
| Limits | `limitsInEffect` = false (permanent) | [Tier A] live read |
| Vesting left | ~15.4M in Sablier Linear | [Tier A] |
| CoinGecko circulating | 770M | [Tier B] |

**What it means:** Supply is fixed, but the owner keeps freeze, blacklist and tax powers. Most vesting is finished and now sits liquid in the Safe.

## 💧 Liquidity & market · 4/10 · ❌ FAIL

| Pool | Pair | Liquidity | 24h volume | 24h buys / sells |
|---|---|---:|---:|---|
| Uniswap V3 `0x9C7eD68B…CbB` (Ethereum) | SERV/WETH | $891,545 | $15,748 | 15 / 12 |
| Uniswap V2 `0xB771f724…600E` | SERV/WETH | $32,154 | $1,773 | 11 / 8 |
| Aero `0xF59bA5bD…7d92` (Base) | SERV/WETH | $521,942 | $19,104 | 31 / 23 |
| All pools | | ~$1.48M | | |

- CEX: LBank ($327k), XT.COM ($191k), Bilaxy, MEXC ([Tier B] CoinGecko tickers).
- The Safe's liquid 206.2M SERV is worth ~$2.56M at spot, about 1.7× all DEX liquidity combined.

## 🧑‍💻 Product & development · 5/10 · ❌ FAIL

- Products in the docs: Reasoning Engine API (OpenAI/Anthropic-compatible), Build, Launch (launchpad) and Run ([Tier A] docs).
- The launchpad is live: Solrouter (ROUTER) launched on it 30 Apr 2026 and pays OpenServ a 33% LP-fee share ([Tier A] OpenServ launchpad docs; see [ROUTER.md](ROUTER.md)).
- Performance claims for the reasoning engine are company-published ([Unverified]). GitHub activity was not checked this pass.

## 🤝 Adoption & customers · 2/10 · ❌ FAIL

- No named paying enterprise, bank or government customer found in a primary source.
- 24h DEX volume is ~$37k across all pools, and holders are 6,676.

## 🛡️ Security & audits · 3/10 · ❌ FAIL

| Item | Finding | Source |
|---|---|---|
| Audit | None found in official docs | [Tier A] (absence) |
| Admin keys | 2-of-5 Safe controls freeze, blacklist, tax and treasury | [Tier A] |
| Base copy | Wormhole Token Bridge is owner (mint/burn/upgrade via beacon) | [Tier A] 10 Oct read |
| Hacks | None found | [Tier A] (absence) |

## ⚖️ Regulatory · 3/10 · ❌ FAIL

- Panama company per the docs only. No registry, licence, SEC, CFTC or court record found. The search was not exhaustive.

## 📅 Catalysts & calendar · 3/10 · ❌ FAIL

| Date | Event | Effect |
|---|---|---|
| Daily | ~0.2M SERV streams from Sablier to the Safe until the Linear stream empties (~15.4M left) | Supply ↑ |
| Unknown | Staking "Ecosystem Index" ("Coming") | Product news |
| Unknown | "SERV Layer 3" | No date |

## 🚩 Red lines status

| Red line | Status | Evidence |
|---|---|---|
| Treasury sells into pumps | 🔴 **Tripped** | 3.16M from `0x9193…` on pump days; 5 Nov Safe-funded seller |
| Treasury → exchange | 🔴 **Tripped** | 10M → MEXC, 11 Nov 2026 |
| Owner freeze / blacklist / tax | 🟡 Present, unused | Live reads |
| Promised burns happening | 🔴 No burns since 10 Oct | Dead-address balances |

## 📚 Sources

- [Tier A] Ethereum RPC (`ethereum-rpc.publicnode.com`, `eth.drpc.org`) and Base RPC: balances, Safe threshold and owners, fee getters; 14 Nov 2026
- [Tier A] Blockscout `eth.blockscout.com` token-transfer logs for the Safe, `0x9193…`, `0x406b…`, `0x56F9…`, `0xeF6A…` and holder list, 14 Nov 2026
- [Tier A] Verified source OpenServ.sol (line references from 10 Oct 2026 review)
- [Tier A] [docs.openserv.ai — SERV token](https://docs.openserv.ai/what-is-serv/the-serv-token), fetched 14 Nov 2026
- [Tier B] CoinGecko market data, tickers and 365-day closes · DexScreener pools, 14 Nov 2026
- [Unverified] Founder identity; Panama registry entry; owner of `0xeD16…`, `0x8210…`, `0x406b…`, `0x56F9…` (funded by the Safe, not disclosed); whether MEXC sold the 10M; reasoning-engine benchmarks

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
