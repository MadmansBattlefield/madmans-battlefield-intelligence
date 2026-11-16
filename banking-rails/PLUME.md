---
ticker: PLUME
name: Plume
chain: plume
contract: "0x4C1746A800D224393fE2470C70A35717eD4eA5F1"
overall_score: 3.7
overall_verdict: FAIL
section_scores:
  revenue: 1
  foundation_team: 6
  insider_holdings: 2
  selling_behavior: 4
  tokenomics_supply: 3
  liquidity_market: 6
  product_development: 6
  adoption_customers: 3
  security_audits: 5
  regulatory: 6
  catalysts: 3
gates_failed: [revenue]
red_lines:
  upgradeable_mintable_token: "yes (contradicts MiCA paper)"
  exchange_inflows_on_pump_days: "explained (bridge → Binance on 23 Sep and 13 Oct 2026 was Binance moving its own inventory from Plume chain; traced 15 Nov)"
  issuer_wallets_published: "no"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "Chain fees are tiny and vault fees go to vault users and curators; there is no burn, buyback, fee share or fee-funded staking yield."
pump_day_price_source: "Gate PLUME_USDT UTC daily closes, re-run 16 Nov 2026 with scripts/pump_day_test.py (60 of 360 days); the body's earlier count used CoinGecko daily closes"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions: []
price_usd: 0.012343
price_source: "CoinGecko, 14 Nov 2026 12:12 PM MST"
last_updated: 2026-11-15
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### PLUME · Overall grade **3.7 / 10 · ❌ FAIL**

**Summary:** A real RWA chain with a proper EU MiCA white paper and a US-registered transfer agent, but the token earns almost nothing (about $2.3k of chain fees a month). The Ethereum token is an upgradeable proxy with live mint, burn and pause roles, which contradicts the white paper's "no ongoing minting" line. About 212M PLUME unlocks every month, and the issuer still hasn't published its wallets. The 210M that moved from the bridge to Binance, including on pump days, has now been traced to Binance moving its own coins between chains, not to issuer sales.

**🚨 Top warning:** The issuer still keeps **4.67B PLUME (46.7%) in wallets it has not published**, the Ethereum token [`0x4C17…A5F1`](https://etherscan.io/address/0x4C1746A800D224393fE2470C70A35717eD4eA5F1) is an upgradeable proxy with a live, uncapped mint role, and ~212M PLUME unlocks monthly. (The 210M bridge → Binance flow on pump days was traced to Binance's own wallet [`0xE69f…3Abb`](https://etherscan.io/address/0xE69f81b825d7Dc31ee9becef4DbEab5cf30e3Abb), [Arkham “Binance: Internal”](https://intel.arkm.com/explorer/address/0xE69f81b825d7Dc31ee9becef4DbEab5cf30e3Abb), so it is **not** issuer selling.)

**Sections passed: 4 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 1/10 | ❌ FAIL |
| 🏛️ Foundation & team | 6/10 | ✅ PASS |
| 🪙 Foundation / team holdings | 2/10 | ❌ FAIL |
| 📉 Selling behavior | 4/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 3/10 | ❌ FAIL |
| 💧 Liquidity & market | 6/10 | ✅ PASS |
| 🧑‍💻 Product & development | 6/10 | ✅ PASS |
| 🤝 Adoption & customers | 3/10 | ❌ FAIL |
| 🛡️ Security & audits | 5/10 | ❌ FAIL |
| ⚖️ Regulatory | 6/10 | ✅ PASS |
| 📅 Catalysts & calendar | 3/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 PLUME · Plume · 3.7 / 10 · ❌ FAIL

> **One line:** A real RWA chain with a proper EU MiCA white paper and a US-registered transfer agent, but the token earns almost nothing (about $2.3k of chain fees a month). The Ethereum token is an upgradeable proxy with live mint, burn and pause roles, which contradicts the white paper's "no ongoing minting" line. About 212M PLUME unlocks every month, and the issuer still hasn't published its wallets. The 210M that moved from the bridge to Binance, including on pump days, has now been traced to Binance moving its own coins between chains, not to issuer sales.

| 📊 Market (CoinGecko + DexScreener, 14 Nov 2026 ~12:12 PM MST) | 🔗 On-chain (Ethereum RPC + Blockscout; explorer.plume.org) |
|---|---|
| **Price** $0.012343 | **Token (Ethereum)** [`0x4C17…A5F1`](https://etherscan.io/address/0x4C1746A800D224393fE2470C70A35717eD4eA5F1) · "PProxy" EIP-1967 → impl `0x8ab0…5Ae9` "Plume" (0.8.25, verified) |
| **24h / 7d / 30d** 🔴 −11.3% / −6.8% / −36.0% | **Total supply** 10,000,000,000 |
| **Market cap** $84.08M · **FDV** $123.3M | **Roles** MINTER / BURNER / PAUSER / UPGRADER ⚠️ live · `paused()` = false |
| **24h volume** $11.1M | **Bridge** [`0x3538…EF83`](https://etherscan.io/address/0x35381f63091926750F43b2A7401B083263aDEF83) holds 4,511,760,175 (45.12%) |
| **ATH** $0.2475 (19 Mar 2025) · now −95% | **Holders (Ethereum)** 25,646 |
| **Circulating (CoinGecko)** 6.818B of 10B (68%) | **Plume chain** 254.99M total txs · 419,735 today · 973,425 addresses |

---

## 💰 Revenue — Does it make money? · 1/10 · ❌ FAIL

| Metric | Value | Source |
|---|---|---|
| Plume mainnet chain fees | 24h **$74** · 30d **$2,343** · all-time $1.04M | [Tier A] DefiLlama `plume-mainnet` |
| Plume vaults | 30d fees $1,084,205 · **revenue $0** | [Tier A] DefiLlama `plume-vaults` |
| Fee share, buyback or burn to PLUME holders | **None found.** The MiCA paper says "no burn mechanism" | [Tier A] MiCA white paper |
| Company revenue | Not published | Not found |

**What it means:** Chain fees are about $2.3k a month against an $84M market cap. Vault fees go to vault users and curators, not to the token.

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** Chain fees are tiny and vault fees go to vault users and curators; there is no burn, buyback, fee share or fee-funded staking yield.

## 🏛️ Foundation & team — Who is in charge? · 6/10 · ✅ PASS

| Item | Finding | Source |
|---|---|---|
| Issuer | **Plume Ltd** (BVI), registration 2147684, registered 2024-05-01, LEI 254900FXSZXTZUJLP764. Registered office: SHRM Trustees (BVI), Road Town | [Tier A] MiCA white paper |
| Parent and sole director | **Plume Foundation SEZC** (Cayman, Genesis Building, George Town) | [Tier A] MiCA |
| Service provider | Kimber Labs, Inc. | [Tier A] MiCA |
| Transfer agent | Kimber Transfer Agency LLC, CIK 0002083132, Form TA-1 filed 2025-08-29, file 084-07011 | [Tier A] SEC EDGAR |
| Public profile | General Counsel Salman Banaei testified to the House on 25 Mar 2026 | [Tier A] congressional record (earlier scan) |
| Funding | $30M raised in 2024 (Galaxy, Haun, Brevan Howard, Lightspeed) | [Tier A] MiCA |

**What it means:** The legal structure is unusually well documented for a crypto project. Token-role holders are not.

## 🪙 Foundation / team holdings — How many coins do they hold? · 2/10 · ❌ FAIL

| Item | Value | Source |
|---|---|---|
| Issuer retained | **4,666,554,520 PLUME (46.7%)**. **Addresses not published** | [Tier A] MiCA §G.5 |
| Bridge contract (Ethereum) | 4,511,760,175 (45.12%) | [Tier A] balanceOf |
| Top Plume-chain native holders | Binance 8, 813.6M · `0x57b83AAF…` 162.3M · PlumeStaking [`0x30c791E4…`](https://explorer.plume.org/address/0x30c791E4654EdAc575FA1700eD8633CB2FEDE871) 138.3M · WPLUME 66.1M · Gate.io 5, 58.0M | [Tier A] explorer.plume.org |
| Unlabeled Plume-chain wallets | Many holding **45–84M** each with only 1–5 transactions. The pattern suggests vesting or investor wallets | [Unverified] |

**What it means:** Nearly half of supply sits with the issuer in wallets it has not disclosed, so its holdings can't be tracked.

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL

**Pump test:** 74 of 360 days had a ≥10% 5-day rise (CoinGecko). The runs were 19–29 Sep and 12–16 Oct 2026.

| Date (2026) | Bridge [`0x3538…`](https://etherscan.io/address/0x35381f63091926750F43b2A7401B083263aDEF83) → "Binance: Internal 2" [`0xE69f…3Abb`](https://etherscan.io/address/0xE69f81b825d7Dc31ee9becef4DbEab5cf30e3Abb) (each forwarded to Binance 14 within ~3 min) | 5-day % | Source (Ethereum send · forward · Plume-chain start) |
|---|---:|---:|---|
| 4 Sep | 10,000,000 | +1.8% | [Tier A] [bridge out](https://etherscan.io/tx/0x8d43e2ca8720152dc16b889b65f43423ab777ac9c254a8d2be63f8926be097f1) · [→ Binance 14](https://etherscan.io/tx/0x7c526bd08fe387145fb8ce52fd5783d9271f2a8a0a0d7b70c6dfb856ed024478) · [Plume-chain withdrawal](https://explorer.plume.org/tx/0x9d8c7258b0f4ac7a6e687b0346ce5c0411b9079ea7e29b1c193c8e4a7505f10a) |
| 15 Sep | 20,000,000 | −2.0% | [Tier A] [bridge out](https://etherscan.io/tx/0xd3104c3827fb5e93369143708705c927b0583aaa78369ae0502cddda94fe3fef) · [→ Binance 14](https://etherscan.io/tx/0xfc394f667862b4f208d731c2546dcdc27525cf3eac9e4368746ef3c6ecc85654) · [Plume-chain withdrawal](https://explorer.plume.org/tx/0xa9b1906c584098fed9c5feda1e0c16060f7a3dcc94388e160b04850327c2923a) |
| **23 Sep** | **30,000,000** (tx `0xd7f3354ab17b80…`) | **+25.3% 🔴 pump** | [Tier A] [bridge out](https://etherscan.io/tx/0xd7f3354ab17b805cfa63fca24268bcbab73e274181343a1387799828ec17e8c9) · [→ Binance 14](https://etherscan.io/tx/0x4f381ddc11a296d9edbcd5aba291eb8c158a552940068eed6ed5992da63e0c1e) · [Plume-chain withdrawal](https://explorer.plume.org/tx/0xe5bf08bee1e888f30049c9ae73437cbde2794dbb3748c301b90effa182d3c667) |
| 5 Oct | 30,000,000 | +7.4% | [Tier A] [bridge out](https://etherscan.io/tx/0x43f28354c13016ae3c1bb85f97147a407f04470ac06c41038a403dadd26d5d19) · [→ Binance 14](https://etherscan.io/tx/0x7d815dddce69356d4f30353abae07e4996ffc9f49e114c7c0250d557514d73fb) · [Plume-chain withdrawal](https://explorer.plume.org/tx/0xf729bddd4f8c1bc0df3e878f5baaca8833cdd1ac84738df6695cb936f21184be) |
| 8 Oct | 20,000,000 | −1.7% | [Tier A] [bridge out](https://etherscan.io/tx/0x900a8e959b9ec2f685a9b41aa0514684fd94d7b4f5242449a2c261a42378aaaf) · [→ Binance 14](https://etherscan.io/tx/0x25dbd55caf052f96712f644be196fb89b74387854eb054b4fa503bd71676d4a2) · [Plume-chain withdrawal](https://explorer.plume.org/tx/0x538adff031767e90b59acfc1ece874dcbcdcac685239b19524729c8da72d05c0) |
| **13 Oct** | **30,000,000** (tx `0x097bd9ee589b74…`) | **+17.7% 🔴 pump** | [Tier A] [bridge out](https://etherscan.io/tx/0x097bd9ee589b744d550b590a2dd004c5f8baae460aebad81c30530dd97a79517) · [→ Binance 14](https://etherscan.io/tx/0xa96b2bbe6c0998da8091804cfdce61a1fa035dc67c1dde14bc3b1efb457a5d6f) · [Plume-chain withdrawal](https://explorer.plume.org/tx/0x699d57078274cae1b0801b5a6d5363503433b0baf1b8333d15183d4a1c1bb0f7) |
| 15 Oct | 20,000,000 | +8.9% | [Tier A] [bridge out](https://etherscan.io/tx/0x68f307c601536c3776f2632e087982d4d5129e4a71640d6d208c2222e521d3a8) · [→ Binance 14](https://etherscan.io/tx/0xd8cf5b30be9a9f34a3e38e0c65fdd24e2ba5233b2057c6225041880b84eb14f3) · [Plume-chain withdrawal](https://explorer.plume.org/tx/0xc7477ba073be3d16662b3ef5752cca8719bf93f44628c0291899cad9155b0261) |
| 20 Oct | 50,000,000 (tx `0x7a67d9aa08c9ce…`; forwarded to Binance 14 on 26 Oct) | −11.3% | [Tier A] [bridge out](https://etherscan.io/tx/0x7a67d9aa08c9ce6ccc962b219f115c726a6709ff2565520a53f3712b8af61645) · [→ Binance 14](https://etherscan.io/tx/0x2ea4106fcb57ac7192d7f10884b108596e6cf68547147615d5c4f3aad1ce2439) · [Plume-chain withdrawal](https://explorer.plume.org/tx/0x5998276c4c7a186fa23c11818712e287a1c172976f958ec5c4936bac342600cb) |

- **Total 210M** bridged straight to a Binance wallet in seven weeks, two batches of it on pump days (amounts and dates re-confirmed on 15 Nov, plus a 100-PLUME test on 15 Jul).
- **Sender now traced (15 Nov): it was Binance itself.** Each Ethereum receipt matches an Arbitrum-Orbit bridge withdrawal whose `OutBoxTransactionExecuted` event names the Plume-chain sender (`l2Sender`) as **`0xE69f…` itself**. On Plume chain, `0xE69f…` ([Plume explorer](https://explorer.plume.org/address/0xE69f81b825d7Dc31ee9becef4DbEab5cf30e3Abb)) was topped up by [`0x9d71d99c…26D9`](https://explorer.plume.org/address/0x9d71d99c65122D8378B25A6E5b82177a1cF426D9) (52.7K transactions; it also feeds Binance 8 `0xF977…`, so likely a Binance hot wallet [Unverified]) and started each withdrawal about 7 days before the Ethereum receipt: 28 Aug, 8 Sep, 16 Sep, 28 Sep, 1 Oct, 6 Oct, 8 Oct and 13 Oct, plus 30M on 27 Oct ([Plume withdrawal](https://explorer.plume.org/tx/0xa4448743a954d60d96aa540dc33f399bff188918608f8552495eaface4e20a72)) whose Ethereum receipt was not found. `0xE69f…` is labelled **"Binance: Internal"** by Arkham ([Arkham](https://intel.arkm.com/explorer/address/0xE69f81b825d7Dc31ee9becef4DbEab5cf30e3Abb)) and **"Binance: Internal 2"** by the Plume explorer, two independent Tier B labels, so **Binance ownership is verified**. These were exchange inventory moves, not issuer sales. So the pump-day timing says nothing about the issuer ([Tier A] explorer.plume.org API · Ethereum RPC · [Tier B] Arkham, read 15 Nov 2026 ~11:00 AM MST (signed-in account)).
- On 9 Oct, ~60.5M also left the bridge to four unlabeled wallets: [`0xcFb8896A…`](https://etherscan.io/address/0xcfb8896a769fb272604af5affae7ae6faa1a86ca) 15.15M, [`0xADbDDDa8…`](https://etherscan.io/address/0xADbDDDa802e4D4cd9887a6E05d7CbE0D93607242) 12.4M, [`0xe002B3B5…`](https://etherscan.io/address/0xe002b3b5d178a8fd211594114195db02a185ac28) 18.4M, [`0xeAA553F8…`](https://etherscan.io/address/0xeAA553F8E1F976C04c3DdfE7bd418Bb972265272) 14.5M (tx hashes not pulled; see each address page).
- **`0xe002…` / `0xcFb8…` traced:** `0xe002…` is funded on Plume chain by `0xcFb8…` (an 83.9M holder). `0xcFb8…` ([Plume explorer](https://explorer.plume.org/address/0xcfb8896a769fb272604af5affae7ae6faa1a86ca)) is in turn funded in 25M chunks by [`0xe92e6504…`](https://explorer.plume.org/address/0xe92e65049b3c2ca12806e9567b08895118c5a03f), which received 478.5M from `0x9d71…` (the Binance-feeding wallet) and more from Gate `0x0D07…` and Bitget `0x1AB4…`. `0xe002…` bridges about 25M a month to Ethereum and sends 2.2–4.3M chunks to wallets labelled "GSR Markets" (`0xa15A…`, `0xEb63…`; one label source, [Unverified]). Two of those pairs fell on pump days (26 May, 16 Jun), against about 4.5 expected by chance. This looks like a **trader or market-maker loop funded from exchanges, with no tie to the issuer found** [Unverified].
- **Arkham's "Plume" entity** has 28 addresses; its holdings are essentially the Ethereum bridge contract and it shows **$0 of exchange deposits**. Arkham's first page of `0xE69f…` transfers did not show the 210M only because the browser read one page; it is not a contradiction ([Tier B] Arkham, read 15 Nov 2026 ~11:00 AM MST (signed-in account)).

**What it means:** The large pump-day inflows that tripped the gate turned out to be Binance moving its own coins, so the selling gate is no longer tripped (3 → 4). The section still fails: the issuer holds 46.7% in wallets it has not published, so insider selling can't be ruled in or out.

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from Gate PLUME_USDT UTC daily closes, re-run 16 Nov 2026 with scripts/pump_day_test.py (60 of 360 days); the body's earlier count used CoinGecko daily closes.

## 📊 Tokenomics & supply · 3/10 · ❌ FAIL

| Item | Value | Source |
|---|---|---|
| Max / total | 10B | [Tier A] totalSupply |
| Circulating | 6.818B (68%). The old "2B" figure was the launch float (~2.65B) | [Tier B] CoinGecko · launch float [Unverified] |
| Unlock pace | ~**212M per month** until 21 Jan 2028 | [Unverified] Tokenomics.com |
| Next unlock | ~21 Nov 2026, ~211.8M (~$2.6M at today's price) | [Unverified] |
| Mint | **MINTER_ROLE can mint with no cap** in the implementation | [Tier A] verified source |
| MiCA claim | "no ongoing minting or inflation; no burn mechanism" | [Tier A] MiCA. **Contradicted by the code's capability**, though no mint above 10B has happened |

**What it means:** About 3% of circulating supply unlocks every month, and the supply cap is a promise, not code.

## 💧 Liquidity & market · 6/10 · ✅ PASS

| Venue | 24h volume (approx.) | Source |
|---|---:|---|
| Binance | $2.58M | [Tier B] CoinGecko tickers |
| HTX | $1.25M | [Tier B] |
| Upbit (KRW / USDT / BTC) | $635k | [Tier B] |
| BTCC, Paribu, Bybit | smaller | [Tier B] |
| DEX total | **~$95k** liquidity (Uniswap PLUME/USDC $42k) | [Tier A] DexScreener API |

**What it means:** Tradable on major CEXs, but on-chain depth is thin.

## 🧑‍💻 Product & development · 6/10 · ✅ PASS

- Plume mainnet live since 5 Jun 2025; token launched 21 Jan 2025 ([Tier A] MiCA).
- Chain activity: 254.99M total transactions, 419,735 today, 973,425 addresses ([Tier A] explorer.plume.org stats).
- Staking contract (PlumeStaking) holds 138.3M ([Tier A] explorer).

**What it means:** The chain is live and busy by transaction count. Fee data says most of that activity is very low value.

## 🤝 Adoption & customers · 3/10 · ❌ FAIL

- Chain fees of $2,343 in 30 days ([Tier A] DefiLlama) do not match the claimed RWA scale.
- Shinhan MoU, 14 Aug 2026 (PR Newswire; an MoU, not a deployment) [Tier B].
- Plume is **not** on DTCC's 4 May 2026 working-group list ([Tier A] DTCC).
- RWA "total value" on project dashboards is project-reported ([Unverified]).

**What it means:** The partnerships are announcements, and paying usage is minimal.

## 🛡️ Security & audits · 5/10 · ❌ FAIL

| Item | Finding | Source |
|---|---|---|
| Token | EIP-1967 proxy. `upgradeToAndCall` is gated by UPGRADER_ROLE, and mint, burn and pause are role-gated | [Tier A] verified implementation |
| Role holders | **Not enumerated** (the RoleGranted log scan timed out) | Not found; needs an archive `getLogs` |
| Correction | The earlier Treasury Health scan said PLUME "isn't a proxy". **That was wrong** | [Tier A] |
| Bridge | TransparentUpgradeableProxy → ERC20Bridge impl `0x81be…D9D6` | [Tier A] |
| Hacks | None found for PLUME | [Tier B] |

**What it means:** Whoever holds the roles can upgrade, mint or pause the token, and they are not public.

## ⚖️ Regulatory · 6/10 · ✅ PASS

- **MiCA white paper** published, notification date 2026-03-18 (type: Correction), offer start 2025-01-25 ([Tier A] plume.org PDF).
- SEC-registered transfer agent (Kimber Transfer Agency, TA-1) ([Tier A] EDGAR).
- House testimony by the General Counsel, 25 Mar 2026 ([Tier A]).

**What it means:** Plume engages with regulators better than most. The code contradiction above is a disclosure issue to watch.

## 📅 Catalysts & calendar · 3/10 · ❌ FAIL

| Date | Event | Source |
|---|---|---|
| ~21 Nov 2026 | Monthly unlock, ~211.8M | [Unverified] Tokenomics.com |
| Monthly to 21 Jan 2028 | ~212M per month | [Unverified] |
| — | No confirmed product or listing catalyst found | Not found |

**What it means:** The calendar is dominated by supply.

## 🚩 Red lines status

| Red line | Status | Evidence |
|---|---|---|
| Upgradeable, mintable token | 🔴 Yes | PProxy + MINTER_ROLE / UPGRADER_ROLE |
| Mint above 10B | 🟢 Not used | totalSupply 10,000,000,000 |
| Exchange inflows on pump days | 🟡 Explained: Binance's own cross-chain inventory moves (l2Sender = Binance wallet), not issuer sales | [23 Sep](https://etherscan.io/tx/0xd7f3354ab17b805cfa63fca24268bcbab73e274181343a1387799828ec17e8c9) · [13 Oct](https://etherscan.io/tx/0x097bd9ee589b744d550b590a2dd004c5f8baae460aebad81c30530dd97a79517) · [Arkham label](https://intel.arkm.com/explorer/address/0xE69f81b825d7Dc31ee9becef4DbEab5cf30e3Abb) · [Plume-chain sender](https://explorer.plume.org/address/0xE69f81b825d7Dc31ee9becef4DbEab5cf30e3Abb) |
| Issuer wallets published | 🔴 No | MiCA §G.5 gives amount only |
| Token paused | 🟢 No | `paused()` = false |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| Plume bridge → Binance flows (23 Sep, 13 Oct 2026) | Binance moving its own inventory | On-chain trace in this report | high | yes (on-chain) | None: removed as an insider sale |
| Unpublished issuer wallets (46.7%) | Issuer | Supply data only | low | no | Selling stays not proven (4) |

## 📚 Sources

- [Tier A] Methodology update 16 Nov 2026: no new Arkham lookups; the attribution table uses evidence already cited in this report.
- [Tier A] Ethereum RPC and eth.blockscout.com: token proxy, implementation source, balances, bridge transfers, 14 Nov 2026
- [Tier A] explorer.plume.org Blockscout API: native holders, chain stats
- [Tier A] Plume MiCA white paper (plume.org/landing/Plume-MiCA-Modified-White-Paper.pdf)
- [Tier A] SEC EDGAR, Kimber Transfer Agency LLC (CIK 0002083132) · DTCC 4 May 2026 list
- [Tier A] DefiLlama `plume-mainnet`, `plume-vaults` · DexScreener tokens API
- [Tier B] CoinGecko markets, tickers and daily closes · PR Newswire (Shinhan MoU)
- [Tier A] explorer.plume.org API v2 (`withdrawEth` calls and transfers for `0xE69f…`, `0xe002…`, `0xcFb8…`, `0xe92e…`) and Ethereum bridge `OutBoxTransactionExecuted` logs; read 15 Nov 2026 ~11:30 AM MST
- [Tier B] Arkham, read 15 Nov 2026 ~11:00 AM MST (signed-in account): `0xE69f…` "Binance: Internal"; "Plume" entity (28 addresses, $0 deposits); only the first page of transfers was read and all-time exchange totals are Enterprise-locked
- [Tier A] Explorer pages used: Etherscan [`bridge 0x3538…`](https://etherscan.io/address/0x35381f63091926750F43b2A7401B083263aDEF83) · [`0xE69f…`](https://etherscan.io/address/0xE69f81b825d7Dc31ee9becef4DbEab5cf30e3Abb) · [`token 0x4C17…`](https://etherscan.io/address/0x4C1746A800D224393fE2470C70A35717eD4eA5F1) · [`Binance 14`](https://etherscan.io/address/0x28C6c06298d514Db089934071355E5743bf21d60) · [`0xe002…`](https://etherscan.io/address/0xe002b3b5d178a8fd211594114195db02a185ac28) · [`0xcFb8…`](https://etherscan.io/address/0xcfb8896a769fb272604af5affae7ae6faa1a86ca); Plume explorer [`0xE69f…`](https://explorer.plume.org/address/0xE69f81b825d7Dc31ee9becef4DbEab5cf30e3Abb) · [`0x9d71…`](https://explorer.plume.org/address/0x9d71d99c65122D8378B25A6E5b82177a1cF426D9) · [`0xcFb8…`](https://explorer.plume.org/address/0xcfb8896a769fb272604af5affae7ae6faa1a86ca) · [`0xe002…`](https://explorer.plume.org/address/0xe002b3b5d178a8fd211594114195db02a185ac28) · [`0xe92e…`](https://explorer.plume.org/address/0xe92e65049b3c2ca12806e9567b08895118c5a03f)
- [Tier B] Arkham address pages used: [0xE69f…](https://intel.arkm.com/explorer/address/0xE69f81b825d7Dc31ee9becef4DbEab5cf30e3Abb) · [bridge 0x3538…](https://intel.arkm.com/explorer/address/0x35381f63091926750F43b2A7401B083263aDEF83) · [0xe002…](https://intel.arkm.com/explorer/address/0xe002b3b5d178a8fd211594114195db02a185ac28)
- [Unverified] Unlock schedule (Tokenomics.com); launch float; role holders; owner of `0x9d71…` (Binance by behaviour only); "GSR Markets" label; who controls `0xe002…`/`0xcFb8…`; identity of unlabeled 45–84M wallets

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer) or the label source (Arkham) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Issuer retained 4,666,554,520 PLUME (46.7%), addresses not published | [MiCA white paper §G.5](https://plume.org/landing/Plume-MiCA-Modified-White-Paper.pdf) (no addresses given) | A | 14 Nov 2026 |
| Ethereum token is an upgradeable proxy with live MINTER / UPGRADER roles | [token on Etherscan](https://etherscan.io/address/0x4C1746A800D224393fE2470C70A35717eD4eA5F1) | A | 14 Nov 2026 |
| Bridge holds 4,511,760,175 PLUME (45.12%) | [bridge on Etherscan](https://etherscan.io/address/0x35381f63091926750F43b2A7401B083263aDEF83) | A | 14 Nov 2026 |
| **210M bridge → `0xE69f…` → Binance 14 (4 Sep – 26 Oct 2026)**, incl. 30M on each of the 23 Sep and 13 Oct pump days | [4 Sep](https://etherscan.io/tx/0x8d43e2ca8720152dc16b889b65f43423ab777ac9c254a8d2be63f8926be097f1) · [15 Sep](https://etherscan.io/tx/0xd3104c3827fb5e93369143708705c927b0583aaa78369ae0502cddda94fe3fef) · [23 Sep](https://etherscan.io/tx/0xd7f3354ab17b805cfa63fca24268bcbab73e274181343a1387799828ec17e8c9) · [5 Oct](https://etherscan.io/tx/0x43f28354c13016ae3c1bb85f97147a407f04470ac06c41038a403dadd26d5d19) · [8 Oct](https://etherscan.io/tx/0x900a8e959b9ec2f685a9b41aa0514684fd94d7b4f5242449a2c261a42378aaaf) · [13 Oct](https://etherscan.io/tx/0x097bd9ee589b744d550b590a2dd004c5f8baae460aebad81c30530dd97a79517) · [15 Oct](https://etherscan.io/tx/0x68f307c601536c3776f2632e087982d4d5129e4a71640d6d208c2222e521d3a8) · [20 Oct](https://etherscan.io/tx/0x7a67d9aa08c9ce6ccc962b219f115c726a6709ff2565520a53f3712b8af61645) (bridge sends); forwards: [4 Sep](https://etherscan.io/tx/0x7c526bd08fe387145fb8ce52fd5783d9271f2a8a0a0d7b70c6dfb856ed024478) · [15 Sep](https://etherscan.io/tx/0xfc394f667862b4f208d731c2546dcdc27525cf3eac9e4368746ef3c6ecc85654) · [23 Sep](https://etherscan.io/tx/0x4f381ddc11a296d9edbcd5aba291eb8c158a552940068eed6ed5992da63e0c1e) · [5 Oct](https://etherscan.io/tx/0x7d815dddce69356d4f30353abae07e4996ffc9f49e114c7c0250d557514d73fb) · [8 Oct](https://etherscan.io/tx/0x25dbd55caf052f96712f644be196fb89b74387854eb054b4fa503bd71676d4a2) · [13 Oct](https://etherscan.io/tx/0xa96b2bbe6c0998da8091804cfdce61a1fa035dc67c1dde14bc3b1efb457a5d6f) · [15 Oct](https://etherscan.io/tx/0xd8cf5b30be9a9f34a3e38e0c65fdd24e2ba5233b2057c6225041880b84eb14f3) · [20 Oct](https://etherscan.io/tx/0x2ea4106fcb57ac7192d7f10884b108596e6cf68547147615d5c4f3aad1ce2439) | A | 15 Nov 2026 ~11:30 AM MST |
| **Sender = Binance:** each withdrawal was started on Plume chain by `0xE69f…` itself (l2Sender), ~7 days earlier | [4 Sep](https://explorer.plume.org/tx/0x9d8c7258b0f4ac7a6e687b0346ce5c0411b9079ea7e29b1c193c8e4a7505f10a) · [15 Sep](https://explorer.plume.org/tx/0xa9b1906c584098fed9c5feda1e0c16060f7a3dcc94388e160b04850327c2923a) · [23 Sep](https://explorer.plume.org/tx/0xe5bf08bee1e888f30049c9ae73437cbde2794dbb3748c301b90effa182d3c667) · [5 Oct](https://explorer.plume.org/tx/0xf729bddd4f8c1bc0df3e878f5baaca8833cdd1ac84738df6695cb936f21184be) · [8 Oct](https://explorer.plume.org/tx/0x538adff031767e90b59acfc1ece874dcbcdcac685239b19524729c8da72d05c0) · [13 Oct](https://explorer.plume.org/tx/0x699d57078274cae1b0801b5a6d5363503433b0baf1b8333d15183d4a1c1bb0f7) · [15 Oct](https://explorer.plume.org/tx/0xc7477ba073be3d16662b3ef5752cca8719bf93f44628c0291899cad9155b0261) · [20 Oct](https://explorer.plume.org/tx/0x5998276c4c7a186fa23c11818712e287a1c172976f958ec5c4936bac342600cb) · [27 Oct](https://explorer.plume.org/tx/0xa4448743a954d60d96aa540dc33f399bff188918608f8552495eaface4e20a72) · [Arkham “Binance: Internal”](https://intel.arkm.com/explorer/address/0xE69f81b825d7Dc31ee9becef4DbEab5cf30e3Abb) | A + 2× B | 15 Nov 2026 |
| `0xE69f…` topped up on Plume chain by `0x9d71…` (52.7K txs; feeds Binance 8) | [0x9d71… on Plume explorer](https://explorer.plume.org/address/0x9d71d99c65122D8378B25A6E5b82177a1cF426D9) | A (owner [Unverified]) | 15 Nov 2026 |
| 9 Oct: ~60.5M from the bridge to four unlabeled wallets; `0xe002…`/`0xcFb8…` look like an exchange-funded trader / market-maker loop | [0xcFb8…](https://etherscan.io/address/0xcfb8896a769fb272604af5affae7ae6faa1a86ca) · [0xADbD…](https://etherscan.io/address/0xADbDDDa802e4D4cd9887a6E05d7CbE0D93607242) · [0xe002…](https://etherscan.io/address/0xe002b3b5d178a8fd211594114195db02a185ac28) · [0xeAA5…](https://etherscan.io/address/0xeAA553F8E1F976C04c3DdfE7bd418Bb972265272) · [0xe92e… (Plume)](https://explorer.plume.org/address/0xe92e65049b3c2ca12806e9567b08895118c5a03f) — tx hashes not pulled | A (roles [Unverified]) | 15 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Where the issuer's 4.67B PLUME sits** | Ask Plume to publish its treasury and vesting addresses (MiCA §G.5 gives the amount only); match against the unlabeled 45–84M Plume-chain wallets | Free |
| 2 | **Token role holders** (MINTER / UPGRADER / PAUSER) | Archive `getLogs` for `RoleGranted` on `0x4C17…`, or call `getRoleMember` if enumerable | Free (archive RPC) |
| 3 | **Who controls `0xe002…` / `0xcFb8…`** | Second label source (Nansen) for `0xcFb8…`, `0xe92e…` and the GSR addresses; ask GSR | Nansen paid |
| 4 | **The 27 Oct 30M withdrawal from `0xE69f…`** | Find the matching Ethereum receipt (bridge `OutBoxTransactionExecuted` after ~3 Nov) | Free |
| 5 | **Unlock schedule** | Plume's official vesting doc or on-chain vesting contract | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
