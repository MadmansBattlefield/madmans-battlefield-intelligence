---
ticker: SERV
name: OpenServ
chain: ethereum
contract: "0x40e3d1A4B2C47d9AA61261F5606136ef73E28042"
bridged_copy_base: "0x5576D6ed9181F2225afF5282Ac0ED29f755437Ea"
overall_score: 2.6
overall_verdict: FAIL
section_scores:
  revenue: 2
  foundation_team: 3
  insider_holdings: 3
  selling_behavior: 0
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
  treasury_to_exchange: tripped_10M_into_MEXC_deposit_address_11_Nov_2026
  owner_can_freeze_transfers: present_unused
  blacklist: present_unused
  burns_since_10_Oct: none
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "The promised buy-and-burn has not executed (no burns found in five weeks) and no revenue is disclosed."
pump_day_price_source: "MEXC SERVUSDT UTC daily closes, re-run 16 Nov 2026 with scripts/pump_day_test.py (87 of 360 days); the body's earlier count used CoinGecko daily closes"
pump_day_disclosure_quality: silence
pump_day_undisclosed_penalty_applied: true
dual_review: not_run
attributions: []
price_usd: 0.01242
price_source: "CoinGecko, 14 Nov 2026 12:12 PM MST"
chain_read_block_eth: 26415266
last_updated: 2026-11-15
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### SERV · Overall grade **2.6 / 10 · ❌ FAIL**

**Summary:** No revenue can be seen on-chain, and there have been no burns since 10 Oct. Meanwhile a treasury wallet named in the docs has sold about 12.2M SERV into Uniswap since January, including on pump days. On 21 and 31 Oct the main treasury Safe pulled 212M SERV out of vesting, then on 11 Nov sent 10M straight into an address Arkham labels a MEXC deposit address. The wallet the Safe funded on the 5 Nov pump day sells daily and pays its USDC to the same address the docs-listed treasury wallets pay.

**🚨 Top warning (red line):** On 11 Nov 2026 the 2-of-5 treasury Safe sent **10,000,000 SERV straight into a MEXC deposit address** (Arkham “MEXC Deposit”), swept to MEXC's hot wallet within minutes, with no announcement. Check it: [tx `Safe → MEXC deposit`](https://etherscan.io/tx/0x41133022e49b1bc6457b87583e3af7531faef15e76445a7876b1e75a6437cfbb) · [tx `sweep to MEXC hot wallet`](https://etherscan.io/tx/0xddb18a93b9aaa37c8394c69cf3b2d0b68f49fd590a6e71b48ea12003a887641c) · [deposit address on Arkham](https://intel.arkm.com/explorer/address/0x56F966721FdA11F95ee8C0bd5b031751f682fF47) · [Safe on Etherscan](https://etherscan.io/address/0x42CAb3696a60C6Fc51381Bb533797E4121e1f168). Every transfer is linked in the 🔗 Evidence trail below.

**Sections passed: 0 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 2/10 | ❌ FAIL |
| 🏛️ Foundation & team | 3/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 3/10 | ❌ FAIL |
| 📉 Selling behavior | 0/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 4/10 | ❌ FAIL |
| 💧 Liquidity & market | 4/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 5/10 | ❌ FAIL |
| 🤝 Adoption & customers | 2/10 | ❌ FAIL |
| 🛡️ Security & audits | 3/10 | ❌ FAIL |
| ⚖️ Regulatory | 3/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 3/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 SERV · OpenServ · 2.6 / 10 · ❌ FAIL

> **One line:** No revenue can be seen on-chain, and there have been no burns since 10 Oct. Meanwhile a treasury wallet named in the docs has sold about 12.2M SERV into Uniswap since January, including on pump days. On 21 and 31 Oct the main treasury Safe pulled 212M SERV out of vesting, then on 11 Nov sent 10M straight into an address Arkham labels a MEXC deposit address. The wallet the Safe funded on the 5 Nov pump day sells daily and pays its USDC to the same address the docs-listed treasury wallets pay.

⚠️ **The Ethereum token is canonical.** The Base token is a Wormhole-bridged copy (lock-and-mint).

| 📊 Market (CoinGecko + DexScreener, 14 Nov 2026 ~12:12–12:40 PM MST) | 🔗 On-chain (Ethereum block 26,415,266 · Base 57,467,762) |
|---|---|
| **Price** $0.01242 | **Token** [`0x40e3…8042`](https://etherscan.io/address/0x40e3d1A4B2C47d9AA61261F5606136ef73E28042) OpenServ.sol, Solidity 0.8.21, verified · no mint, no proxy |
| **24h / 7d / 30d** 🔴 −3.4% / −15.4% / −34.8% | **Supply** 1,000,000,000 fixed |
| **Market cap** $9.56M · **FDV** $12.42M | **Owner** Safe [`0x42CA…f168`](https://etherscan.io/address/0x42CAb3696a60C6Fc51381Bb533797E4121e1f168) ([Arkham](https://intel.arkm.com/explorer/address/0x42CAb3696a60C6Fc51381Bb533797E4121e1f168)), **2 of 5**, nonce 177 |
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

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** The promised buy-and-burn has not executed (no burns found in five weeks) and no revenue is disclosed.

## 🏛️ Foundation & team — Who is in charge? · 3/10 · ❌ FAIL

| Item | Finding | Source |
|---|---|---|
| Entity | "OpenServ Inc., Bloc Office Hub, Fifth Floor, Santa Maria Business District, Panama". **No registry record retrieved** | [Tier A] docs · registry [Unverified] |
| Signers claimed | "secured by a multisig wallet requiring five board-level signers" | [Tier A] docs |
| Signers on-chain | **2 of 5**: `0x4a48…23e1`, `0x5964…d3c9`, `0xe4ef…57de`, `0x8db4…00f6` (token deployer), `0x4005…5072` | [Tier A] `getThreshold` = 2, `getOwners` |
| Published treasury addresses | Safe [`0x42CA…f168`](https://etherscan.io/address/0x42CAb3696a60C6Fc51381Bb533797E4121e1f168) · [`0xeF6A15b3…779e`](https://etherscan.io/address/0xeF6A15b3675390e2896c99A4D12d51f9dfbd779e) (**plain wallet**) · [`0x9193f0B6…3376`](https://etherscan.io/address/0x9193f0B639097e2AD0f22E5692Cd10e3A28a3376) (**plain wallet**) | [Tier A] docs + Blockscout (`is_contract` = false) |
| Named founder (Tim Hafner) | From third-party trackers | [Unverified] |
| Treasury payout address [`0x14f6165DFA03335bEAdFb42c49B7dF063DDDFC25`](https://etherscan.io/address/0x14f6165DFA03335bEAdFb42c49B7dF063DDDFC25) | Arkham labels it **"@open_founder"** ([Arkham](https://intel.arkm.com/explorer/address/0x14f6165DFA03335bEAdFb42c49B7dF063DDDFC25)). On-chain it has received **318,513 USDC** since 19 Jan 2026, of which 260,795 from the two docs-listed treasury wallets and 13,773 from the Safe-funded seller `0x406b…` (see Selling B). It passes almost all of it on to [`0x0510B1a8…CfE7`](https://etherscan.io/address/0x0510b1a8b756836e0563358737d445aa8589cfe7) (313,513 USDC; 45,122 txs, no label) | [Tier A] Circle USDC transfers, Blockscout · founder identity [Tier B] Arkham, read 15 Nov 2026 ~11:05 AM MST (signed-in account), one source → [Unverified] |
| Priced round / VCs | Not found | [Unverified] |

**What it means:** Two keys move everything. Two of the three "multisig-secured" treasury addresses are single-key wallets.

## 🪙 Foundation / team holdings — How many coins do they hold? · 3/10 · ❌ FAIL

| Wallet | Role | 10 Oct 2026 | 14 Nov 2026 | % supply | Locked? |
|---|---|---:|---:|---:|---|
| [`0x42CAb3696a60C6Fc51381Bb533797E4121e1f168`](https://etherscan.io/address/0x42CAb3696a60C6Fc51381Bb533797E4121e1f168) | Owner / treasury Safe (2/5) | 3,695,716 | **206,203,533** | 20.62% | 🔓 liquid |
| same Safe on Base | | 1,051,635 | 1,051,635 | 0.11% | 🔓 |
| Sablier V2 LockupTranched [`0xf86B3590…`](https://etherscan.io/address/0xf86B359035208e4529686A1825F2D5BeE38c28A8) | Vesting | 130,000,000 | **0** (paid to Safe 21 Oct) | 0% | — |
| Sablier V2 LockupLinear [`0x3962f658…`](https://etherscan.io/address/0x3962f6585946823440d274aD7C719B02b49DE51E) | Vesting | 100,000,000 | 15,381,348 | 1.54% | 🔒 streaming to the Safe (~0.2M/day) |
| [`0xeF6A15b3…779e`](https://etherscan.io/address/0xeF6A15b3675390e2896c99A4D12d51f9dfbd779e) | Docs "treasury" (plain wallet) | 16,976 + 657,935 Base | 16,515 + 427,474 Base | 0.04% | 🔓 |
| [`0x9193f0B6…3376`](https://etherscan.io/address/0x9193f0B639097e2AD0f22E5692Cd10e3A28a3376) | Docs "treasury" (plain wallet) | 533,455 | **0** | 0% | 🔓 (sold out, see below) |
| [`0xeD16D0Fe…9479`](https://etherscan.io/address/0xeD16D0FeCFA95d4a041d16Bf15F98c6BE49f9479) | Safe, owner [Unverified] | 8,093,307 | 8,093,307 | 0.81% | 🔓 |

**Vesting releases into the Safe** ([Tier A] Blockscout transfer log):

| Date (UTC) | From | Amount | Tx |
|---|---|---:|---|
| 21 Oct 2026 08:45 | Sablier Tranched | **130,000,000** | [tx `0x6a0e8d9d58ca…`](https://etherscan.io/tx/0x6a0e8d9d58caae16d6cce03684e771c5179bf279eda1d5da5855f9f13c9bfbf7) |
| 31 Oct 2026 02:07 | Sablier Linear | **82,098,553** | [tx `0xa7fd135f6d62…`](https://etherscan.io/tx/0xa7fd135f6d62c4f1555932fdbc74275183273ca330d0a072a442b295d7916f6e) |
| 5–13 Nov 2026 | Sablier Linear (daily) | ~0.2–0.95M per day | e.g. [tx `0x9343902a8f44…`](https://etherscan.io/tx/0x9343902a8f449120ec9dee62cf84f58bd5d0165296a68f75816924bc143e1cc1) |

**What it means:** The treasury went from ~0.4% to ~21% of supply liquid in three weeks, all controlled by two keys.

## 📉 Selling behavior — Do insiders sell into pumps? · 0/10 · ❌ FAIL

**Pump test:** 95 of 360 days in the last year had a ≥10% 5-day rise (CoinGecko daily closes). The most recent were 4 Nov (+16.3%) and 5 Nov (+11.1%).

### A. A docs-listed treasury wallet sells into Uniswap every day

[`0x9193f0B639097e2AD0f22E5692Cd10e3A28a3376`](https://etherscan.io/address/0x9193f0B639097e2AD0f22E5692Cd10e3A28a3376) (published as a treasury address; [Arkham](https://intel.arkm.com/explorer/address/0x9193f0B639097e2AD0f22E5692Cd10e3A28a3376)) is refilled by the owner Safe, then sells ~40–90k SERV a few times a day into the main pools ([`0x9C7e…CbB`](https://etherscan.io/address/0x9C7eD68B00DC4f45243b07Ce71a54A86e8f8FcBB) Uniswap V3, [`0xB771…600E`](https://etherscan.io/address/0xB771f724C504b329623B0ce9199907137670600E) Uniswap V2, CoW Swap, Uniswap V4):

| Item | Value |
|---|---:|
| Safe → `0x9193…` refills since Jan 2026 | [5.0M (16 Jan)](https://etherscan.io/tx/0x127363983404882fb16e492ee404a3711f4d43987522145f738bcec8dc4cfc4b) · [2.73M (22 Apr)](https://etherscan.io/tx/0xa93b2827ce9f79b873bb74c744f3e907ba3cb197638db4e9a08a2479ea1a2bb2) · [1.25M (9 Sep)](https://etherscan.io/tx/0xe8246c8fc0c50e51318054c7b64ef8db32b79e30996f4eb2d07c7844d6487e4b) · [0.5M (26 Sep)](https://etherscan.io/tx/0xe3ff65ca00a24ecec05bc6c6bb99701787a2408375264290fd66fb0baa0c1c8c) · [1.0M (26 Sep)](https://etherscan.io/tx/0x8eab41c1f0243cb6eed9d757b182b5e09a8f2f39a5c156cdc2cad835c2feecce) · [1.0M (13 Oct)](https://etherscan.io/tx/0xd60e145b6a7f5659d23248db23d37f4fd123dc47ded95cfc1a958ceab7bada32) · [1.5M (3 Nov)](https://etherscan.io/tx/0xb788ae064b53f4655e945acff7f6de88292442137db87e330245e0f8c4cbae4d) |
| SERV sent from `0x9193…` to DEX pools, Jan–Nov 2026 | **12,233,122** |
| …of which on **pump days** | **3,163,928 in 46 swaps** |
| By month | Jan 2.16M · Feb 2.43M · Mar 3.12M · Apr 0.50M · May 1.02M · Sep 1.04M · Oct 1.81M · Nov 0.17M |
| Example pump-day swaps | 21 Sep [tx `0x301aeebf335a…`](https://etherscan.io/tx/0x301aeebf335a9161b21fed9da7b08621e85ae357548941162a0a60424b473152) (+40.6%) · 22 Sep 339,622 to [`0xD54e…`](https://etherscan.io/address/0xd54eea1a55cdb7d03c83b7b3e333e728355b1d53) ([tx `0xead1ef0cf3c2…`](https://etherscan.io/tx/0xead1ef0cf3c207c30c0bf36a24c780089b2536e40bfa7640172e1a7ccef296b6)) (+62.1%) · 23 Sep [tx `0x75ea73008328…`](https://etherscan.io/tx/0x75ea73008328fe3e72f72de81ed5a61dd4dd359132632afc3b57518877a59c93) (+58.7%) · 4 Nov 00:24 [tx `0x8de4bcbe9a23…`](https://etherscan.io/tx/0x8de4bcbe9a234b2d2958f885437e667230cf4d8bec1cbf9bd246b4b58680013e) (+16.3%) |
| Other pump-day outflow | 4 Nov 06:26: 1,084,000 to [`0x8210…`](https://etherscan.io/address/0x8210201496876814ceb86b29fcf6f0f3f1ab8e6e) (unlabeled; [tx `0x89c51fd22623…`](https://etherscan.io/tx/0x89c51fd2262345435dbb2eb1896b3b6114013abdd7c4563a0c5a5426e8733461)) |
| Balance now | 0 |

### B. Safe → fresh wallet on a pump day → daily sells → USDC to the treasury payout address

| Time (UTC) | Tx | What happened |
|---|---|---|
| 5 Nov 2026 02:28 | [tx `0xdfb8916bfd9a…`](https://etherscan.io/tx/0xdfb8916bfd9a27427a2c9a1a08b6a9d168ab6cb58e9eda59f103d1881fbd949d) | Safe sent 1,500,000 to [`0x406b510F688d113c0A78d2a7B3af6a438b6B1aEb`](https://etherscan.io/address/0x406b510F688d113c0A78d2a7B3af6a438b6B1aEb) ([Arkham](https://intel.arkm.com/explorer/address/0x406b510F688d113c0A78d2a7B3af6a438b6B1aEb)) (5-day move **+11.1%**) |
| 5 Nov 02:30 | [tx `0xbe6c1e869e21…`](https://etherscan.io/tx/0xbe6c1e869e215557723354d4ed3fb4fffd01ddde79f2910258b0b18d49ed584f) | 100,000 to `0x1111…1605` (unlabeled) |
| 6–13 Nov | 26 transfers, e.g. [tx `0x080981ed1d58…`](https://etherscan.io/tx/0x080981ed1d5868a218c96348931770141be72465417e8d77f6063a185a0002d0) | **1,215,000** sold into Uniswap V3/V2, ~70–80k per swap |
| 9 Nov 2026 20:17 · 13 Nov 13:26 | [tx `0x86bc81f24a80…`](https://etherscan.io/tx/0x86bc81f24a80f397468ac5b1433899d14e26600d5783d40103bb18db2b7613cc) · [tx `0xbd6c1f9ed3d0…`](https://etherscan.io/tx/0xbd6c1f9ed3d006026736750f4cd375e7a1c49c23d30783efad6ecaf378237cb5) | Sale proceeds out: **8,773.15 + 5,000 USDC** to [`0x14f6165D…FC25`](https://etherscan.io/address/0x14f6165DFA03335bEAdFb42c49B7dF063DDDFC25), the same address the docs-listed treasury wallets `0xeF6A…` (219,308 USDC, Jan–Jun 2026) and `0x9193…` (41,487 USDC, Feb–Sep 2026) pay |
| 14 Nov 20:22 | [tx `0x3359efb4c668…`](https://etherscan.io/tx/0x3359efb4c66821db7fb264ca7f1f85ae8352d317a0d321264cb76a6faeebad0d) | Another 185,000 sold into Uniswap V3/V2 |
| 14 Nov | — | 185,000 left on Ethereum before that sale, 40,000 on Base (Arkham on 15 Nov: 40,000 SERV + 7,104 USDC) |

- **Is `0x406b…` a team wallet?** It is funded by the 2-of-5 Safe, and it pays its USDC to the same address (`0x14f6…`) that both docs-listed treasury wallets pay. That ties it to the treasury's own cash-out route on-chain ([Tier A] Circle USDC transfers). Arkham labels `0x14f6…` "@open_founder"; that founder link is one Tier B source, so it stays [Unverified]. Arkham shows no entity on `0x406b…` itself.
- Both `0x406b…` and `0x14f6…` are targets of **address poisoning**: dozens of fake "USDC" tokens and zero-value transfers from look-alike addresses (`0x14f6…FC25` variants, `0x0510…cfE7` variants). Only transfers of Circle USDC (`0xA0b8…eB48`) are counted above.

### C. Safe → MEXC deposit address → MEXC hot wallet

| Time (UTC) | Tx | Amount |
|---|---|---:|
| 11 Nov 2026 15:57 / 16:20 (8:57 / 9:20 AM MST) | [tx `0xeb85533b141a…`](https://etherscan.io/tx/0xeb85533b141a8bfba8c6710014f9657c52ddc5cbef6fe073fc5df929fca0e1f2) / [tx `0x41133022e49b…`](https://etherscan.io/tx/0x41133022e49b1bc6457b87583e3af7531faef15e76445a7876b1e75a6437cfbb) | Safe → [`0x56F966721FdA11F95ee8C0bd5b031751f682fF47`](https://etherscan.io/address/0x56F966721FdA11F95ee8C0bd5b031751f682fF47) ([Arkham: “MEXC Deposit”](https://intel.arkm.com/explorer/address/0x56F966721FdA11F95ee8C0bd5b031751f682fF47)): 10,000 test + 9,990,000 |
| 11 Nov 16:02 | [tx `0x564ad44702d4…`](https://etherscan.io/tx/0x564ad44702d4942329011c246f3a73af4fab9ba39df900d7ee755f27cca74eb3) | 0.001 ETH gas into `0x56F9…` from [`0xE8832A86…dd91`](https://etherscan.io/address/0xe8832a868c091263ed190a9f4be304a03895dd91), which Arkham labels "MEXC: Gas Supplier" ([Arkham](https://intel.arkm.com/explorer/address/0xe8832a868c091263ed190a9f4be304a03895dd91)) |
| 11 Nov 16:03 / 16:22 | [tx `0xb4bc23558460…`](https://etherscan.io/tx/0xb4bc23558460b00992a2f5b700ba8eca8fb4341dd338d2a74639f63765f735e5) / [tx `0xddb18a93b9aa…`](https://etherscan.io/tx/0xddb18a93b9aaa37c8394c69cf3b2d0b68f49fd590a6e71b48ea12003a887641c) | `0x56F9…` → [`0x9642b23Ed1E01Df1092B92641051881a322F5D4E`](https://etherscan.io/address/0x9642b23Ed1E01Df1092B92641051881a322F5D4E): 10,000 + 9,990,000. That wallet is **MEXC** on two independent labels: Blockscout/OLI "MEXC 21" ([Blockscout](https://eth.blockscout.com/address/0x9642b23Ed1E01Df1092B92641051881a322F5D4E)) and Arkham "MEXC: Hot Wallet" ([Arkham](https://intel.arkm.com/explorer/address/0x9642b23Ed1E01Df1092B92641051881a322F5D4E)) |

- **`0x56F9…` is a MEXC deposit address, not a team hop.** Arkham labels it "MEXC Deposit (0x56F)"; on-chain it has only these five transfers, was gassed by MEXC's gas supplier, and swept everything to MEXC within two minutes of each deposit. So the Safe paid **directly into a MEXC customer account** ([Tier B] Arkham, read 15 Nov 2026 ~11:05 AM MST (signed-in account) · [Tier A] Blockscout flows). Which account it credits is Not found.
- 11 Nov was not a pump day (5-day move −10.9%, price $0.01289). Whether MEXC sold it cannot be seen on-chain.

**What it means:** Yes. Treasury wallets sell into the open market almost daily, including on pump days, and the Safe paid 10M straight into a MEXC deposit address on 11 Nov. Arkham adds that the pump-day seller sends its dollars to the same address the treasury wallets pay. Score unchanged at 1/10. None of it was announced. The addresses are published, but the sales are not.

- **Disclosure quality (16 Nov 2026 rules): silence.** The addresses are published but the sales are not. **Penalty applied (16 Nov 2026 rules):** a proven pump-day sale with no disclosure takes 2 points off the ordinary Selling score, floored at 0: **1 → 0**. On MEXC prices 4–5 Nov 2026 are not pump days, but the 21–22 Sep 2026 swaps still are. Pump days from MEXC SERVUSDT UTC daily closes, re-run 16 Nov 2026 with scripts/pump_day_test.py (87 of 360 days); the body's earlier count used CoinGecko daily closes.

- **One-hop amendment (16 Nov 2026):** Still a **proven sale** under the amended rule. (b) holds: treasury wallets sold into DEX pools on pump days, and the seller sends its dollars to the address the treasury wallets pay. Silence stands, so the penalty above is unchanged.

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
| Uniswap V3 [`0x9C7eD68B…CbB`](https://etherscan.io/address/0x9C7eD68B00DC4f45243b07Ce71a54A86e8f8FcBB) (Ethereum) | SERV/WETH | $891,545 | $15,748 | 15 / 12 |
| Uniswap V2 [`0xB771f724…600E`](https://etherscan.io/address/0xB771f724C504b329623B0ce9199907137670600E) | SERV/WETH | $32,154 | $1,773 | 11 / 8 |
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
| Treasury sells into pumps | 🔴 **Tripped** | 3.16M from [`0x9193…`](https://etherscan.io/address/0x9193f0B639097e2AD0f22E5692Cd10e3A28a3376) on pump days (e.g. [tx `22 Sep`](https://etherscan.io/tx/0xead1ef0cf3c207c30c0bf36a24c780089b2536e40bfa7640172e1a7ccef296b6), [tx `4 Nov`](https://etherscan.io/tx/0x8de4bcbe9a234b2d2958f885437e667230cf4d8bec1cbf9bd246b4b58680013e)); 5 Nov Safe-funded seller ([tx `funding tx`](https://etherscan.io/tx/0xdfb8916bfd9a27427a2c9a1a08b6a9d168ab6cb58e9eda59f103d1881fbd949d)) |
| Treasury → exchange | 🔴 **Tripped** | 10M from the Safe straight into a MEXC deposit address, 11 Nov 2026: [tx `Safe → deposit`](https://etherscan.io/tx/0x41133022e49b1bc6457b87583e3af7531faef15e76445a7876b1e75a6437cfbb) · [tx `deposit → MEXC hot wallet`](https://etherscan.io/tx/0xddb18a93b9aaa37c8394c69cf3b2d0b68f49fd590a6e71b48ea12003a887641c) · [Arkham “MEXC Deposit”](https://intel.arkm.com/explorer/address/0x56F966721FdA11F95ee8C0bd5b031751f682fF47) · [Arkham “MEXC: Hot Wallet”](https://intel.arkm.com/explorer/address/0x9642b23Ed1E01Df1092B92641051881a322F5D4E) |
| Owner freeze / blacklist / tax | 🟡 Present, unused | Live reads |
| Promised burns happening | 🔴 No burns since 10 Oct | Dead-address balances |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| Published treasury Safe and `0x9193…` seller | OpenServ treasury | Project-published addresses + Etherscan flows | high | yes (project publication) | Selling: 3.16M sold on pump days; 10M to a MEXC deposit |

## 📚 Sources

- [Tier A] Methodology update 16 Nov 2026: no new Arkham lookups; the attribution table uses evidence already cited in this report.
- [Tier A] Ethereum RPC (`ethereum-rpc.publicnode.com`, `eth.drpc.org`) and Base RPC: balances, Safe threshold and owners, fee getters; 14 Nov 2026
- [Tier A] Blockscout `eth.blockscout.com` token-transfer logs for the Safe, `0x9193…`, `0x406b…`, `0x56F9…`, `0xeF6A…` and holder list, 14 Nov 2026
- [Tier A] Explorer pages (Etherscan) for every wallet named above: token [`0x40e3…`](https://etherscan.io/address/0x40e3d1A4B2C47d9AA61261F5606136ef73E28042) · Safe [`0x42CA…`](https://etherscan.io/address/0x42CAb3696a60C6Fc51381Bb533797E4121e1f168) · [`0x9193…`](https://etherscan.io/address/0x9193f0B639097e2AD0f22E5692Cd10e3A28a3376) · [`0xeF6A…`](https://etherscan.io/address/0xeF6A15b3675390e2896c99A4D12d51f9dfbd779e) · [`0x406b…`](https://etherscan.io/address/0x406b510F688d113c0A78d2a7B3af6a438b6B1aEb) · [`0x56F9…`](https://etherscan.io/address/0x56F966721FdA11F95ee8C0bd5b031751f682fF47) · [`0x9642…`](https://etherscan.io/address/0x9642b23Ed1E01Df1092B92641051881a322F5D4E) · [`0x14f6…`](https://etherscan.io/address/0x14f6165DFA03335bEAdFb42c49B7dF063DDDFC25) · [`0x0510…`](https://etherscan.io/address/0x0510b1a8b756836e0563358737d445aa8589cfe7) · [`0xeD16…`](https://etherscan.io/address/0xeD16D0FeCFA95d4a041d16Bf15F98c6BE49f9479) · [`0x8210…`](https://etherscan.io/address/0x8210201496876814ceb86b29fcf6f0f3f1ab8e6e) · Sablier [`Tranched`](https://etherscan.io/address/0xf86B359035208e4529686A1825F2D5BeE38c28A8) / [`Linear`](https://etherscan.io/address/0x3962f6585946823440d274aD7C719B02b49DE51E); every transaction is linked inline and in the 🔗 Evidence trail
- [Tier A] Verified source OpenServ.sol (line references from 10 Oct 2026 review)
- [Tier A] [docs.openserv.ai — SERV token](https://docs.openserv.ai/what-is-serv/the-serv-token), fetched 14 Nov 2026
- [Tier B] CoinGecko market data, tickers and 365-day closes · DexScreener pools, 14 Nov 2026
- [Tier A] Blockscout Circle USDC transfers for `0x406b…` and `0x14f6165D…`, and `0x56F9…` transactions; CoinGecko daily closes for the pump test; 15 Nov 2026 ~11:10 AM MST
- [Tier B] Arkham, read 15 Nov 2026 ~11:05 AM MST (signed-in account): [`0x56F9…` “MEXC Deposit (0x56F)”](https://intel.arkm.com/explorer/address/0x56F966721FdA11F95ee8C0bd5b031751f682fF47); [`0x9642…` “MEXC: Hot Wallet”](https://intel.arkm.com/explorer/address/0x9642b23Ed1E01Df1092B92641051881a322F5D4E); [`0xE883…` “MEXC: Gas Supplier”](https://intel.arkm.com/explorer/address/0xe8832a868c091263ed190a9f4be304a03895dd91); [`0x14f6…` “@open_founder”](https://intel.arkm.com/explorer/address/0x14f6165DFA03335bEAdFb42c49B7dF063DDDFC25); [no entity on `0x406b…`](https://intel.arkm.com/explorer/address/0x406b510F688d113c0A78d2a7B3af6a438b6B1aEb); Safe [`0x42CA…`](https://intel.arkm.com/explorer/address/0x42CAb3696a60C6Fc51381Bb533797E4121e1f168). Limits: Arkham gives relative ages only (exact times above are from Blockscout); its all-time exchange totals are Enterprise-locked; only the first page of transfers was read
- [Unverified] Founder identity (incl. Arkham's "@open_founder" label, one source); Panama registry entry; owner of `0xeD16…`, `0x8210…`, `0x406b…`, `0x0510B1a8…`; which MEXC account `0x56F9…` credits and whether MEXC sold the 10M; reasoning-engine benchmarks

## 🔗 Evidence trail

*Strongest findings first. Each link opens the primary record (block explorer) or the label source (Arkham) for the claim, so any number can be checked by hand.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| **Red line:** Safe `0x42CA…` → MEXC deposit `0x56F9…`: 10,000 test (15:57 UTC) + 9,990,000 SERV (16:20 UTC), 11 Nov 2026 | [tx `test send`](https://etherscan.io/tx/0xeb85533b141a8bfba8c6710014f9657c52ddc5cbef6fe073fc5df929fca0e1f2) · [tx `9.99M send`](https://etherscan.io/tx/0x41133022e49b1bc6457b87583e3af7531faef15e76445a7876b1e75a6437cfbb) · [deposit on Etherscan](https://etherscan.io/address/0x56F966721FdA11F95ee8C0bd5b031751f682fF47) · [Arkham “MEXC Deposit (0x56F)”](https://intel.arkm.com/explorer/address/0x56F966721FdA11F95ee8C0bd5b031751f682fF47) | A (chain) + B (label) | 15 Nov 2026 ~11:05 AM MST |
| `0x56F9…` swept both deposits to MEXC hot wallet `0x9642…` within 2 min; gassed by MEXC's gas supplier | [tx `sweep 10k`](https://etherscan.io/tx/0xb4bc23558460b00992a2f5b700ba8eca8fb4341dd338d2a74639f63765f735e5) · [tx `sweep 9.99M`](https://etherscan.io/tx/0xddb18a93b9aaa37c8394c69cf3b2d0b68f49fd590a6e71b48ea12003a887641c) · [tx `gas tx`](https://etherscan.io/tx/0x564ad44702d4942329011c246f3a73af4fab9ba39df900d7ee755f27cca74eb3) · [Arkham “MEXC: Hot Wallet”](https://intel.arkm.com/explorer/address/0x9642b23Ed1E01Df1092B92641051881a322F5D4E) · [Blockscout “MEXC 21”](https://eth.blockscout.com/address/0x9642b23Ed1E01Df1092B92641051881a322F5D4E) · [Arkham “MEXC: Gas Supplier”](https://intel.arkm.com/explorer/address/0xe8832a868c091263ed190a9f4be304a03895dd91) | A + 2× B | 15 Nov 2026 |
| Pump-day funding: Safe → fresh wallet `0x406b…` 1.5M SERV on 5 Nov 2026 (+11.1% 5-day), which then sold ~1.4M into Uniswap | [tx `funding tx`](https://etherscan.io/tx/0xdfb8916bfd9a27427a2c9a1a08b6a9d168ab6cb58e9eda59f103d1881fbd949d) · [tx `example sale`](https://etherscan.io/tx/0x080981ed1d5868a218c96348931770141be72465417e8d77f6063a185a0002d0) · [tx `14 Nov sale`](https://etherscan.io/tx/0x3359efb4c66821db7fb264ca7f1f85ae8352d317a0d321264cb76a6faeebad0d) · [0x406b… on Etherscan](https://etherscan.io/address/0x406b510F688d113c0A78d2a7B3af6a438b6B1aEb) · [Arkham](https://intel.arkm.com/explorer/address/0x406b510F688d113c0A78d2a7B3af6a438b6B1aEb) | A | 15 Nov 2026 |
| `0x406b…` pays sale USDC to `0x14f6…` (Arkham “@open_founder”), the same address both docs-listed treasury wallets pay | [tx `8,773 USDC`](https://etherscan.io/tx/0x86bc81f24a80f397468ac5b1433899d14e26600d5783d40103bb18db2b7613cc) · [tx `5,000 USDC`](https://etherscan.io/tx/0xbd6c1f9ed3d006026736750f4cd375e7a1c49c23d30783efad6ecaf378237cb5) · [0x14f6… on Etherscan](https://etherscan.io/address/0x14f6165DFA03335bEAdFb42c49B7dF063DDDFC25) · [Arkham “@open_founder”](https://intel.arkm.com/explorer/address/0x14f6165DFA03335bEAdFb42c49B7dF063DDDFC25) | A (flows) + B (label, one source → Unverified) | 15 Nov 2026 |
| Docs-listed treasury `0x9193…` sold 12.23M SERV into DEX pools since Jan 2026, 3.16M on pump days | [0x9193… on Etherscan](https://etherscan.io/address/0x9193f0B639097e2AD0f22E5692Cd10e3A28a3376) · pump-day swaps [tx `21 Sep`](https://etherscan.io/tx/0x301aeebf335a9161b21fed9da7b08621e85ae357548941162a0a60424b473152) · [tx `22 Sep`](https://etherscan.io/tx/0xead1ef0cf3c207c30c0bf36a24c780089b2536e40bfa7640172e1a7ccef296b6) · [tx `23 Sep`](https://etherscan.io/tx/0x75ea73008328fe3e72f72de81ed5a61dd4dd359132632afc3b57518877a59c93) · [tx `4 Nov`](https://etherscan.io/tx/0x8de4bcbe9a234b2d2958f885437e667230cf4d8bec1cbf9bd246b4b58680013e) | A | 14–15 Nov 2026 |
| Safe refilled `0x9193…` seven times (16 Jan – 3 Nov 2026) | [16 Jan](https://etherscan.io/tx/0x127363983404882fb16e492ee404a3711f4d43987522145f738bcec8dc4cfc4b) · [22 Apr](https://etherscan.io/tx/0xa93b2827ce9f79b873bb74c744f3e907ba3cb197638db4e9a08a2479ea1a2bb2) · [9 Sep](https://etherscan.io/tx/0xe8246c8fc0c50e51318054c7b64ef8db32b79e30996f4eb2d07c7844d6487e4b) · [26 Sep](https://etherscan.io/tx/0xe3ff65ca00a24ecec05bc6c6bb99701787a2408375264290fd66fb0baa0c1c8c) · [26 Sep](https://etherscan.io/tx/0x8eab41c1f0243cb6eed9d757b182b5e09a8f2f39a5c156cdc2cad835c2feecce) · [13 Oct](https://etherscan.io/tx/0xd60e145b6a7f5659d23248db23d37f4fd123dc47ded95cfc1a958ceab7bada32) · [3 Nov](https://etherscan.io/tx/0xb788ae064b53f4655e945acff7f6de88292442137db87e330245e0f8c4cbae4d) | A | 15 Nov 2026 |
| 4 Nov 2026 pump day (+16.3%): 1,084,000 SERV from `0x9193…` to unlabelled `0x8210…` | [tx `tx`](https://etherscan.io/tx/0x89c51fd2262345435dbb2eb1896b3b6114013abdd7c4563a0c5a5426e8733461) · [0x8210…](https://etherscan.io/address/0x8210201496876814ceb86b29fcf6f0f3f1ab8e6e) | A | 15 Nov 2026 |
| Safe pulled 212M SERV from Sablier vesting (21 and 31 Oct 2026) → Safe now holds 206.2M (20.6%), controlled by 2 of 5 keys | [tx `130M`](https://etherscan.io/tx/0x6a0e8d9d58caae16d6cce03684e771c5179bf279eda1d5da5855f9f13c9bfbf7) · [tx `82.1M`](https://etherscan.io/tx/0xa7fd135f6d62c4f1555932fdbc74275183273ca330d0a072a442b295d7916f6e) · [Safe](https://etherscan.io/address/0x42CAb3696a60C6Fc51381Bb533797E4121e1f168) · [Safe on Arkham](https://intel.arkm.com/explorer/address/0x42CAb3696a60C6Fc51381Bb533797E4121e1f168) | A | 14 Nov 2026 |
| No burns since 10 Oct 2026 (dead-address balance unchanged) | [Etherscan dead address holdings](https://etherscan.io/token/0x40e3d1A4B2C47d9AA61261F5606136ef73E28042?a=0x000000000000000000000000000000000000dEaD) | A | 14 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exact path to close it | Cost / access |
|---|---|---|---|
| 1 | Whose MEXC account deposit address `0x56F9…` credits, and whether the 10M SERV was sold | Ask OpenServ (docs list the treasury addresses; ask which counterparty received 10M on 11 Nov 2026); watch MEXC SERV order book and `0x9642…` outflows on Blockscout | Free / request to team |
| 2 | Whether "@open_founder" (`0x14f6165D…FC25`) is the founder's wallet | A second independent label (Etherscan name tag, Nansen) or a statement from OpenServ; ENS reverse record (none now) | Nansen paid; others free |
| 3 | Who receives the treasury's USDC at `0x0510B1a8…CfE7` (313,513 USDC from `0x14f6…`; 45,122 txs) | Arkham entity page for that address (not read this pass); Blockscout outflows to see if it reaches an exchange or off-ramp | Arkham account (have) · free |
| 4 | Owners of `0xeD16…` (8.09M SERV Safe) and `0x8210…` (1.08M on the 4 Nov pump day) | Arkham entity pages; Safe owner lists via `getOwners` | Arkham account (have) · free |
| 5 | Panama registry entry for OpenServ Inc. | Registro Público de Panamá online search | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
