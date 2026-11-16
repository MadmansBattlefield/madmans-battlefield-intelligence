---
ticker: BP
name: Backpack
chain: solana
mint: BPxxfRCXkUVhig4HS1Lh7kZqV6SPJhzfEk4x6fVBjPCy
overall_score: 5.2
overall_verdict: FAIL
section_scores:
  revenue: 3
  foundation_team: 7
  insider_holdings: 2
  selling_behavior: 7
  tokenomics_supply: 3
  liquidity_market: 8
  product_development: 8
  adoption_customers: 6
  security_audits: 5
  regulatory: 7
  catalysts: 4
gates_failed: [revenue]
red_lines:
  one_hop_sale_status: none_found
  mint_authority_used: not_used
  treasury_outflow_without_milestone_notice: none_since_tge
  holder_freeze: none_found
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "None of the business income reaches BP; the only path is a conditional equity election that depends on an IPO or sale."
pump_day_price_source: "MEXC BPUSDT UTC daily closes, re-run 16 Nov 2026 with scripts/pump_day_test.py (48 of 232 days); the body's earlier count used CoinGecko daily closes"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions: []
price_usd: 0.8097
price_source: "CoinGecko, 14 Nov 2026 12:13 PM MST"
chain_read_slot: 469447370
last_updated: 2026-11-15
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### BP · Overall grade **5.2 / 10 · ❌ FAIL**

**Summary:** A real, EU-licensed exchange whose token has no claim on the exchange's revenue. BP gives fee perks plus a conditional, non-voting equity election if Backpack ever has an exit. The 750M treasury has not moved since before launch, and the 10M "cold-to-hot" move on a pump day is now confirmed as exchange custody (Backpack's own wallet list), not a sale. Backpack still holds the mint and freeze keys; its own treasury is 75% of supply, and another ~20% sits in its exchange wallets for customers.

**⚠️ Top warning:** Backpack's own multisig still holds the **mint and freeze keys** and the **750M BP treasury (75%)** with a 0 time lock, so the "lock" is a promise, not code. The 27 Sep 10M pump-day move was **internal exchange custody, not a sale**. Check it: [mint authority on Solscan](https://solscan.io/account/BPxxfRCXkUVhig4HS1Lh7kZqV6SPJhzfEk4x6fVBjPCy) · [treasury account (no tx since 19 Mar 2026)](https://solscan.io/account/2pWK2bHBah35yPDQdndtwTXry1JtR8LKF59tQrqgaU6s) · [tx `27 Sep move`](https://solscan.io/tx/4XQ19an6pPVHkrP5RnCKgqjxoG5brF9FasTvc7n5iUizdWybxLfk3FHksCsFNLZqR6fVebXXV8UYWjx5Khg2e8ND) · [Arkham: Backpack Squads Vault](https://intel.arkm.com/explorer/address/EyzzXxQcR7NicVhMvHZy5DAeoCrxpCoY11pRneuysJiS) · [Arkham: Backpack Hot Wallet](https://intel.arkm.com/explorer/address/43DbAvKxhXh1oSxkJSqGosNw3HpBnmsWiak6tB5wpecN).

**Sections passed: 6 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 3/10 | ❌ FAIL |
| 🏛️ Foundation & team | 7/10 | ✅ PASS |
| 🪙 Foundation / team holdings | 2/10 | ❌ FAIL |
| 📉 Selling behavior | 7/10 | ✅ PASS |
| 📊 Tokenomics & supply | 3/10 | ❌ FAIL |
| 💧 Liquidity & market | 8/10 | ✅ PASS |
| 🧑‍💻 Product & development | 8/10 | ✅ PASS |
| 🤝 Adoption & customers | 6/10 | ✅ PASS |
| 🛡️ Security & audits | 5/10 | ❌ FAIL |
| ⚖️ Regulatory | 7/10 | ✅ PASS |
| 📅 Catalysts & calendar | 4/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 BP · Backpack · 5.2 / 10 · ❌ FAIL

> **One line:** A real, EU-licensed exchange whose token has no claim on the exchange's revenue. BP gives fee perks plus a conditional, non-voting equity election if Backpack ever has an exit. The 750M treasury has not moved since before launch, and the 10M "cold-to-hot" move on a pump day is now confirmed as exchange custody (Backpack's own wallet list), not a sale. Backpack still holds the mint and freeze keys; its own treasury is 75% of supply, and another ~20% sits in its exchange wallets for customers.

| 📊 Market (CoinGecko + DexScreener, 14 Nov 2026 ~12:13–12:40 PM MST) | 🔗 On-chain (Solana RPC, slot 469,447,370) |
|---|---|
| **Price** $0.8097 (CoinGecko) · $0.8090 (Meteora BP/USDC) | **Mint** [`BPxxfRCX…VBjPCy`](https://solscan.io/account/BPxxfRCXkUVhig4HS1Lh7kZqV6SPJhzfEk4x6fVBjPCy) · SPL · 9 decimals |
| **24h / 7d / 30d** 🔴 −3.2% / −13.3% / −20.5% | **Supply** 999,998,478.21 (999,998,643.70 on 10 Oct) |
| **Market cap** $202.4M · **FDV** $809.5M | **Mint authority** [`GySF…MVH`](https://solscan.io/account/GySFHFS5ZiN4Z5YnyPZcjjxpYcGvD7qHZYVjE9QzMHVH) ⚠️ **live** · **Freeze authority** same ⚠️ **live** |
| **24h volume** $4.73M | **Treasury** [`GySF…`](https://solscan.io/account/GySFHFS5ZiN4Z5YnyPZcjjxpYcGvD7qHZYVjE9QzMHVH) 750,000,000 (75.0%) |
| **ATH** $1.65 (1 Oct 2026) · now −51% | **Exchange custody vault** [`Eyzz…JiS`](https://solscan.io/account/EyzzXxQcR7NicVhMvHZy5DAeoCrxpCoY11pRneuysJiS) 189,217,622 (18.9%) — Backpack-listed exchange wallet |
| **Circulating (CoinGecko)** 250M | **Holders** 28,410 non-zero owners (10 Oct full read) |

---

## 💰 Revenue — Does it make money? · 3/10 · ❌ FAIL

| Metric | Value | Source |
|---|---|---|
| What BP is | A loyalty / utility token: fee and withdrawal discounts, launch access, extra USD yield, free wires, and an optional "Equity Purchase Election" | [Tier A] backpack.exchange/bp, BP Program FAQ ("Last Updated: March 2026") |
| Fee share, buyback or burn to BP holders | **None found** | [Tier A] (absence in FAQ and docs) |
| Supply change since 10 Oct | −165.49 BP | [Tier A] mint reads |
| Exchange revenue | **Not published**; no audited figures | [Unverified] |
| DefiLlama "Backpack SOL" (the staked-SOL token, not BP) | 30-day fees $24,722 · revenue $719 | [Tier A] DefiLlama `backpack-sol` |
| Equity election (if a "Backpack Exit Event" happens) | Base: tokens × 12.5% of equity ÷ 625M after 1 year of staking. Bonus 7.5% over 3 more years. Pool max 20%. Paid as **non-voting** shares in SPVs (Trek ESOP Ltd, BVI; a Blue Coral SPV). Backpack can redeem at a value it calculates, or end the program with 30 days' notice | [Tier A] BP Program FAQ (10 Oct read). The full Terms override it |

**What it means:** The business makes money, but none of it flows to BP today. The only path is a conditional equity election that depends on an IPO or sale that may never happen.

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** None of the business income reaches BP; the only path is a conditional equity election that depends on an IPO or sale.

## 🏛️ Foundation & team — Who is in charge? · 7/10 · ✅ PASS

| Item | Finding | Source |
|---|---|---|
| Exchange operator | Trek Labs Ltd (BVI) | [Tier A] BP FAQ |
| Wallet operator | Blue Coral, Inc. (Delaware) | [Tier A] BP FAQ |
| Share counts fixed for equity program | 12,853,914 Trek Labs ordinary · 9,491,900 Blue Coral common (23 Feb 2026 snapshot) | [Tier A] BP FAQ |
| Treasury multisig | Squads v4 [`Aj8j59RnzzMhNXqdCzjS2eR7G3hCqzRpEjrBhgozBxqf`](https://solscan.io/account/Aj8j59RnzzMhNXqdCzjS2eR7G3hCqzRpEjrBhgozBxqf), **3 of 5**, **time lock 0**. Members `DArE3uM9…`, `Ev8WSPQs…`, `29FjkS8E…`, `3pdzLa3b…`, `Daf3efsL…` | [Tier A] decoded account (10 Oct) |
| Second multisig | Squads v4 `9Qne3WM4…iC1`, **3 of 7**, shares signer `Ev8WSPQs…` | [Tier A] |
| CEO Armani Ferrante; Series A $17M (Placeholder) | Press and news only | [Unverified] |
| Insider tokens | "No token allocations to investors or insiders … The team receives nothing unless the company IPOs." | [Tier A] BP FAQ |

**What it means:** The legal entities are named, and the EU entity is on regulator registers. People and funding are known only from press.

## 🪙 Foundation / team holdings — How many coins do they hold? · 2/10 · ❌ FAIL

| Wallet | Role | 10 Oct 2026 | 14 Nov 2026 | % supply | Locked? |
|---|---|---:|---:|---:|---|
| [`GySFHFS5ZiN4Z5YnyPZcjjxpYcGvD7qHZYVjE9QzMHVH`](https://solscan.io/account/GySFHFS5ZiN4Z5YnyPZcjjxpYcGvD7qHZYVjE9QzMHVH) (token acct [`2pWK2b…aU6s`](https://solscan.io/account/2pWK2bHBah35yPDQdndtwTXry1JtR8LKF59tQrqgaU6s)) | Treasury: 37.5% pre-IPO + 37.5% post-IPO | 750,000,000 | 750,000,000 | 75.00% | 🔓 **No on-chain lock** (multisig, 0 time lock) |
| [`EyzzXxQcR7NicVhMvHZy5DAeoCrxpCoY11pRneuysJiS`](https://solscan.io/account/EyzzXxQcR7NicVhMvHZy5DAeoCrxpCoY11pRneuysJiS) (acct [`CBGt4r…aTKE`](https://solscan.io/account/CBGt4r6n5KyPpV5D3XZaoFJReHGiNC1YbRqrY2zKKTaE)) | **Exchange custody** (Squads vault "BP"). On Backpack's official exchange-wallet list; Arkham: Backpack Exchange, Proof of Reserves ([Arkham](https://intel.arkm.com/explorer/address/EyzzXxQcR7NicVhMvHZy5DAeoCrxpCoY11pRneuysJiS)). Refills the hot wallet | 189,667,622 | 189,217,622 | 18.92% | 🔓 customer custody |
| [`BbHG9GvPActFGogv3iNrpDAj4qpXr8t3jF16uGxXcKci`](https://solscan.io/account/BbHG9GvPActFGogv3iNrpDAj4qpXr8t3jF16uGxXcKci) | **Exchange cold wallet**. On Backpack's official exchange-wallet list; Arkham: "Backpack Exchange: Cold Wallet (BbHG9)" ([Arkham](https://intel.arkm.com/explorer/address/BbHG9GvPActFGogv3iNrpDAj4qpXr8t3jF16uGxXcKci)) | 12,251,149 | 14,608,811 | 1.46% | 🔓 customer custody |
| [`43DbAvKxhXh1oSxkJSqGosNw3HpBnmsWiak6tB5wpecN`](https://solscan.io/account/43DbAvKxhXh1oSxkJSqGosNw3HpBnmsWiak6tB5wpecN) | **Exchange hot wallet**. On Backpack's official exchange-wallet list; Arkham: "Backpack Exchange: Hot Wallet (43DbA)" ([Arkham](https://intel.arkm.com/explorer/address/43DbAvKxhXh1oSxkJSqGosNw3HpBnmsWiak6tB5wpecN)) | — | 295,153 (Arkham 15 Nov: ~1.0M) | 0.03% | 🔓 customer custody |

- **Who owns what** ([Tier A] Backpack's exchange-wallet API [`api.backpack.exchange/api/v1/wallets`](https://api.backpack.exchange/api/v1/wallets), read 15 Nov 2026 ~11:10 AM MST, which lists 92 exchange wallets incl. all three above; [Tier B] Arkham, read 15 Nov 2026 ~11:05 AM MST (signed-in account)): `Eyzz…`, `BbHG…` and `43Db…` are Backpack **exchange** wallets that back customer balances (Arkham tags them "Backpack Exchange Proof of Reserves"). The treasury `GySF…` is **not** on that list. So Backpack's own stake is the 750M treasury (75%); the ~204.8M BP in exchange wallets (Arkham entity total) is held for customers, though Backpack controls the keys.
- Official schedule ([Tier A] backpack.exchange/bp): 25% at TGE (23 Mar 2026). The pre-IPO 37.5% is "progressively unlocked as Backpack hits regulatory, product, and market milestones", with **no dates and no milestone list**. The post-IPO 37.5% is "fully locked until 1 year post-IPO", **but only by promise**.

**What it means:** Backpack's own treasury is 75% of supply with no on-chain lock; the "lock" is a policy, not code. Another ~20% sits in Backpack's exchange wallets on behalf of customers. Score unchanged at 2/10.

## 📉 Selling behavior — Do insiders sell into pumps? · 7/10 · ✅ PASS

**Pump test:** 48 of 232 days since listing had a ≥10% 5-day rise (CoinGecko). The run was heaviest on 7–29 Sep 2026, up to +94%.

| Check | Result | Source |
|---|---|---|
| Treasury token account [`2pWK2b…`](https://solscan.io/account/2pWK2bHBah35yPDQdndtwTXry1JtR8LKF59tQrqgaU6s) | **4 transactions ever**, the last on **19 Mar 2026** (pre-TGE, [tx `4zVw1cQE…`](https://solscan.io/tx/4zVw1cQE4mGw9oDFt2N4iBuEoF4gy3QNBFD3XaPNFXoXgPfRgCcVWPwky4LdXm6FxxBmeECNipND2scxAeGsnpUE)). No outflow since launch | [Tier A] `getSignaturesForAddress` |
| `Eyzz…` → `43Db…` (exchange custody vault → exchange hot wallet; both Backpack-listed) | 10,000,000 on **27 Sep 2026** (5-day **+44.1%**, [tx `4XQ19an6pPVH…`](https://solscan.io/tx/4XQ19an6pPVHkrP5RnCKgqjxoG5brF9FasTvc7n5iUizdWybxLfk3FHksCsFNLZqR6fVebXXV8UYWjx5Khg2e8ND)) · 600k + 1.0M + 1.5M on 1 Oct · 1.5M 2 Oct · 4.0M 6 Oct · 1.0M 9 Oct · 150k 6 Nov · 300k 11 Nov ([1 Oct #1](https://solscan.io/tx/3XN2iZFrJMsXpKpLTHftiwC7kf338mngYMjdm8feHCYUDK8FeRWNq9xwUuSKKB9aKELFESqPS1n3HzFBx795KoBv) · [1 Oct #2](https://solscan.io/tx/39MtFSooE89BuWYcZEBc78zm9ojpAcvaDBjHY3rhQE88okQMPcWRg6FXVXLTk87YbdHaeG1Rf1mRappXwZcnZYcD) · [1 Oct #3](https://solscan.io/tx/4yD8AZUJYsQdUrnTBZPrafmPntwf8ZUd3r9mCx6gPGSHvBC4qKXJFniJYYapascnGSvbg5aUqGrTK8udEsedksNe) · [2 Oct](https://solscan.io/tx/5E3jGk57t51oWhB91RvWYHAsw2ugerJ2NC5x1pBLfkEGQfxGhNGW6H6qPVWMGswHnEdLiqzAs3kM9TpfeYj3miMx) · [6 Oct](https://solscan.io/tx/4FtGvvSMhqzcFXMCsFVB1qPiBk8q4jErKXK4hCYquLzWiTmrBEikq9xA2SBH3ge2kLf5eqRzwia4HRuFZemqvKZy) · [9 Oct](https://solscan.io/tx/2sEntZvU2YsLyT1oz9eBCijfcJ4jvgMCusdZhUkMgfk1wr9wUHkWjiujc1ERrhs4kUno3YaJjhTFsrrd2GmtjdVe) · [6 Nov](https://solscan.io/tx/3M51XbnvZedjcDA2bD4u2Bk2mNLT6BnDgSLAFTB7KAAe1K9oT9Zoyn5PiXTH1aACeouKqNDLdZ4nchZ9mkuKpNQb) · [11 Nov](https://solscan.io/tx/5ZZWBKEvQcH3ccxXBqr2ZCR4Aw2MGKx65YdTtYzUqQyiYyVLsAs26dtrC7fAeUTUf29KzbbDgyNYCd5uJBSCBGEM)). **Total 20.05M since TGE** | [Tier A] parsed transactions |
| Original funding of `Eyzz…` | 209,267,622 from `43Db…` on 21 Apr 2026 (see [`CBGt4r…` history on Solscan](https://solscan.io/account/CBGt4r6n5KyPpV5D3XZaoFJReHGiNC1YbRqrY2zKKTaE); exact tx among several that day not isolated) | [Tier A] |

- ✅ **Resolved: the `Eyzz…` → `43Db…` moves are exchange custody.** Both addresses (and `BbHG…`) are on Backpack's own exchange-wallet list ([Tier A] `api.backpack.exchange/api/v1/wallets`, the feed DefiLlama uses for Backpack's reserves), and Arkham independently labels them Backpack Exchange "Squads Vault \"BP\"", "Hot Wallet" and "Cold Wallet" ([Tier B] Arkham, read 15 Nov 2026 ~11:05 AM MST (signed-in account)). Arkham shows `Eyzz…` sending BP only to the hot wallet, and the hot wallet itself funded `Eyzz…` with 209.3M BP on 21 Apr 2026. The 27 Sep 10M BP move was a hot-wallet refill for customer withdrawals, not a sale.
- The hot wallet's own exchange flows (Arkham, ~30-day window: $122.8M out to Binance, Gate, OKX, Kraken, Gemini) are normal exchange rebalancing across all assets, not BP-specific selling.

**What it means:** The insider treasury has never moved, and the one 10M transfer on a pump day was Backpack moving customer coins between its own exchange wallets. No insider selling into pumps is visible. Score raised from 6 to 7; it is not higher because Backpack can still release 375M treasury tokens whenever it decides, with no notice period.

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from MEXC BPUSDT UTC daily closes, re-run 16 Nov 2026 with scripts/pump_day_test.py (48 of 232 days); the body's earlier count used CoinGecko daily closes.

## 📊 Tokenomics & supply · 3/10 · ❌ FAIL

| Item | Value | Source |
|---|---|---|
| Supply | 999,998,478.21 (1B launch, small burns) | [Tier A] RPC |
| Mint authority | `GySF…MVH`, **not revoked**. Can create BP beyond 1B | [Tier A] RPC |
| Freeze authority | `GySF…MVH`, **not revoked**. Can freeze any holder | [Tier A] RPC |
| Metadata | `isMutable = true`, update authority `GySF…`. URI on `trek-labs.github.io` | [Tier A] 10 Oct read |
| Unlock schedule | Milestone-based, undated | [Tier A] docs |

**What it means:** The code lets one 3-of-5 multisig mint, freeze, and release 375M whenever it decides.

## 💧 Liquidity & market · 8/10 · ✅ PASS

| Pool | Pair | Liquidity | 24h volume | 24h buys / sells |
|---|---|---:|---:|---|
| Meteora [`6qz7THwQvcjF3HyDGLuKaLBUk6EyJKeZXZMWLAeiwfjd`](https://solscan.io/account/6qz7THwQvcjF3HyDGLuKaLBUk6EyJKeZXZMWLAeiwfjd) | BP/USDC | **$5,628,956** | $1,819,031 | 1,244 / 1,905 |
| Meteora `7o3bfXje…FDDa` | BP/SOL | $155,651 | $238,076 | 586 / 559 |
| Raydium `6gBdoi5w…yDe` | BP/USDC | $73,466 | $63,139 | 77 / 113 |
| All pools (30) | | ~$6.17M | | |

- CEX: Backpack Exchange ($1.21M 24h), LBank ($1.01M), MEXC ([Tier B] CoinGecko tickers).

## 🧑‍💻 Product & development · 8/10 · ✅ PASS

- Live: Backpack Exchange (spot, staking on-exchange, Backpack EU), Backpack Wallet, Backpack Securities (not US) ([Tier A] official site / FAQ, 10 Oct).
- BP staking is custodial on the exchange. No public on-chain staking program was found ([Tier A] learn.backpack.exchange).

## 🤝 Adoption & customers · 6/10 · ✅ PASS

- 28,410 non-zero on-chain holders (10 Oct). The exchange's user and volume numbers are not audited.
- The claim that Backpack handled "91% of Solana tokenized-stock trading on 2 Nov" comes from a social post ([Unverified]).

## 🛡️ Security & audits · 5/10 · ❌ FAIL

- No exchange-level hack found in primary records. The 7 Oct "trader key compromise" drain is from social posts only ([Unverified]).
- Mint, freeze and the 750M treasury sit with a 3-of-5 multisig with **0 time lock**.
- No token audit is needed for a standard SPL mint. The risk is in the keys, not the code.

## ⚖️ Regulatory · 7/10 · ✅ PASS

| Register | Entry | Source |
|---|---|---|
| CySEC | Licence **273/15** (23 Apr 2015), trade name "Backpack EU", **previous name FTX EU Ltd**. MiFID services incl. execution, dealing on own account, safekeeping | [Tier A] cysec.gov.cy register, fetched 10 Oct 2026 |
| ESMA interim MiCA register | "Trek Technologies" SIA, LEI 6488C2PNI17093U2YA18, Latvijas Banka, **authorised 27 May 2026**. Custody, exchange, execution, transfer. Passported to 29 EEA states | [Tier A] ESMA CASPS.csv, fetched 10 Oct 2026 |
| US | Fiat deposits and withdrawals not supported. Equity-election eligibility for US persons not confirmed | [Tier A] FAQ · [Unverified] |
| FTX EU sale (court order, $32.7M) | Press release / news only | [Unverified] |

## 📅 Catalysts & calendar · 4/10 · ❌ FAIL

| Date | Event | Effect |
|---|---|---|
| Undated | Pre-IPO milestone releases from the 375M tranche | Supply ↑ |
| Undated | Backpack Exit Event (IPO / sale) | Equity election becomes live |
| ≥ 23 Mar 2027 | Earliest date anyone could have 1 year of continuous staking, if staking opened at TGE (start date [Unverified]) | First eligibility for the base equity amount |

## 🚩 Red lines status

| Red line | Status | Evidence |
|---|---|---|
| Mint authority used (supply above 1B) | 🟢 Not used | Supply 999,998,478 ([mint on Solscan](https://solscan.io/account/BPxxfRCXkUVhig4HS1Lh7kZqV6SPJhzfEk4x6fVBjPCy)) |
| Treasury outflow without a milestone notice | 🟢 None since TGE | Last treasury tx 19 Mar 2026 ([tx `4zVw1cQE…`](https://solscan.io/tx/4zVw1cQE4mGw9oDFt2N4iBuEoF4gy3QNBFD3XaPNFXoXgPfRgCcVWPwky4LdXm6FxxBmeECNipND2scxAeGsnpUE); [account history](https://solscan.io/account/2pWK2bHBah35yPDQdndtwTXry1JtR8LKF59tQrqgaU6s)) |
| Holder account frozen | 🟢 None found | — |
| Equity program redeemed or terminated | 🟢 Not found | — |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| Backpack exchange wallets (10M move on a pump day) | Backpack customer-coin movement | On-chain trace in this report | high | yes | None: not an insider sale |
| Insider treasury (375M) | Backpack treasury | On-chain, never moved | high | yes | Holdings |

## 📚 Sources

- [Tier A] Methodology update 16 Nov 2026: no new Arkham lookups; the attribution table uses evidence already cited in this report.
- [Tier A] Solana mainnet RPC: mint account, `getTokenAccountsByOwner`, `getSignaturesForAddress` and `getTransaction` for the treasury and `Eyzz…` accounts; slot ~469,447,370, 14 Nov 2026
- [Tier A] Prior forensic read, 10 Oct 2026 (full holder list; Squads multisig decode; CySEC and ESMA registers)
- [Tier A] [backpack.exchange/bp](https://backpack.exchange/bp) · BP Program FAQ · learn.backpack.exchange
- [Tier A] DefiLlama `backpack-sol`
- [Tier B] CoinGecko market data, tickers and daily closes · DexScreener pools, 14 Nov 2026
- [Tier A] Backpack exchange-wallet list, [`api.backpack.exchange/api/v1/wallets`](https://api.backpack.exchange/api/v1/wallets) (92 wallets, 18 on Solana), read 15 Nov 2026 ~11:10 AM MST; DefiLlama adapter `projects/backpack` reads the same feed
- [Tier B] Arkham, read 15 Nov 2026 ~11:05 AM MST (signed-in account): [entity "Backpack Exchange"](https://intel.arkm.com/explorer/entity/backpack-exchange) (550k addresses, ~$452M, 204.8M BP); [`43Db…` Hot Wallet](https://intel.arkm.com/explorer/address/43DbAvKxhXh1oSxkJSqGosNw3HpBnmsWiak6tB5wpecN), [`Eyzz…` Squads Vault "BP"](https://intel.arkm.com/explorer/address/EyzzXxQcR7NicVhMvHZy5DAeoCrxpCoY11pRneuysJiS), [`BbHG…` Cold Wallet](https://intel.arkm.com/explorer/address/BbHG9GvPActFGogv3iNrpDAj4qpXr8t3jF16uGxXcKci).
- [Tier A] Explorer pages (Solscan): mint [`BPxx…`](https://solscan.io/account/BPxxfRCXkUVhig4HS1Lh7kZqV6SPJhzfEk4x6fVBjPCy) · treasury [`GySF…`](https://solscan.io/account/GySFHFS5ZiN4Z5YnyPZcjjxpYcGvD7qHZYVjE9QzMHVH) / [`2pWK2b…`](https://solscan.io/account/2pWK2bHBah35yPDQdndtwTXry1JtR8LKF59tQrqgaU6s) · Squads [`Aj8j59…`](https://solscan.io/account/Aj8j59RnzzMhNXqdCzjS2eR7G3hCqzRpEjrBhgozBxqf) · [`Eyzz…`](https://solscan.io/account/EyzzXxQcR7NicVhMvHZy5DAeoCrxpCoY11pRneuysJiS) / [`CBGt4r…`](https://solscan.io/account/CBGt4r6n5KyPpV5D3XZaoFJReHGiNC1YbRqrY2zKKTaE) · [`BbHG…`](https://solscan.io/account/BbHG9GvPActFGogv3iNrpDAj4qpXr8t3jF16uGxXcKci) · [`43Db…`](https://solscan.io/account/43DbAvKxhXh1oSxkJSqGosNw3HpBnmsWiak6tB5wpecN); transactions linked inline Limits: relative ages only; ~30-day exchange window (all-time is Enterprise-locked); first page of transfers read
- [Unverified] CEO and funding rounds; FTX EU court documents; US eligibility; 91% tokenized-stock claim; 7 Oct drain

## 🔗 Evidence trail

*Strongest findings first. Each link opens the primary record (block explorer) or the label source (Arkham) for the claim, so any number can be checked by hand.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Mint and freeze authority = treasury `GySF…` (live, not revoked) | [mint account](https://solscan.io/account/BPxxfRCXkUVhig4HS1Lh7kZqV6SPJhzfEk4x6fVBjPCy) · [GySF…](https://solscan.io/account/GySFHFS5ZiN4Z5YnyPZcjjxpYcGvD7qHZYVjE9QzMHVH) | A | 14 Nov 2026 |
| Treasury token account `2pWK2b…` holds 750,000,000 BP; 4 txs ever, last 19 Mar 2026 (pre-TGE) | [account](https://solscan.io/account/2pWK2bHBah35yPDQdndtwTXry1JtR8LKF59tQrqgaU6s) · [tx `last tx`](https://solscan.io/tx/4zVw1cQE4mGw9oDFt2N4iBuEoF4gy3QNBFD3XaPNFXoXgPfRgCcVWPwky4LdXm6FxxBmeECNipND2scxAeGsnpUE) | A | 14 Nov 2026 |
| Treasury Squads multisig `Aj8j59…` is 3-of-5 with 0 time lock | [Squads account](https://solscan.io/account/Aj8j59RnzzMhNXqdCzjS2eR7G3hCqzRpEjrBhgozBxqf) | A (decoded 10 Oct) | 10 Oct 2026 |
| 27 Sep 2026 (pump day, +44.1%): 10M BP `Eyzz…` → `43Db…` = Backpack internal custody move, not a sale | [tx `tx`](https://solscan.io/tx/4XQ19an6pPVHkrP5RnCKgqjxoG5brF9FasTvc7n5iUizdWybxLfk3FHksCsFNLZqR6fVebXXV8UYWjx5Khg2e8ND) · [Arkham Eyzz… “Squads Vault BP”](https://intel.arkm.com/explorer/address/EyzzXxQcR7NicVhMvHZy5DAeoCrxpCoY11pRneuysJiS) · [Arkham 43Db… “Hot Wallet”](https://intel.arkm.com/explorer/address/43DbAvKxhXh1oSxkJSqGosNw3HpBnmsWiak6tB5wpecN) · [Backpack wallet list](https://api.backpack.exchange/api/v1/wallets) | A (chain + official list) + B | 15 Nov 2026 ~11:05–11:10 AM MST |
| Later `Eyzz…` → `43Db…` refills (1 Oct – 11 Nov 2026), 20.05M total since TGE | [1 Oct #1](https://solscan.io/tx/3XN2iZFrJMsXpKpLTHftiwC7kf338mngYMjdm8feHCYUDK8FeRWNq9xwUuSKKB9aKELFESqPS1n3HzFBx795KoBv) · [1 Oct #2](https://solscan.io/tx/39MtFSooE89BuWYcZEBc78zm9ojpAcvaDBjHY3rhQE88okQMPcWRg6FXVXLTk87YbdHaeG1Rf1mRappXwZcnZYcD) · [1 Oct #3](https://solscan.io/tx/4yD8AZUJYsQdUrnTBZPrafmPntwf8ZUd3r9mCx6gPGSHvBC4qKXJFniJYYapascnGSvbg5aUqGrTK8udEsedksNe) · [2 Oct](https://solscan.io/tx/5E3jGk57t51oWhB91RvWYHAsw2ugerJ2NC5x1pBLfkEGQfxGhNGW6H6qPVWMGswHnEdLiqzAs3kM9TpfeYj3miMx) · [6 Oct](https://solscan.io/tx/4FtGvvSMhqzcFXMCsFVB1qPiBk8q4jErKXK4hCYquLzWiTmrBEikq9xA2SBH3ge2kLf5eqRzwia4HRuFZemqvKZy) · [9 Oct](https://solscan.io/tx/2sEntZvU2YsLyT1oz9eBCijfcJ4jvgMCusdZhUkMgfk1wr9wUHkWjiujc1ERrhs4kUno3YaJjhTFsrrd2GmtjdVe) · [6 Nov](https://solscan.io/tx/3M51XbnvZedjcDA2bD4u2Bk2mNLT6BnDgSLAFTB7KAAe1K9oT9Zoyn5PiXTH1aACeouKqNDLdZ4nchZ9mkuKpNQb) · [11 Nov](https://solscan.io/tx/5ZZWBKEvQcH3ccxXBqr2ZCR4Aw2MGKx65YdTtYzUqQyiYyVLsAs26dtrC7fAeUTUf29KzbbDgyNYCd5uJBSCBGEM) | A | 14 Nov 2026 |
| Exchange cold wallet `BbHG…` holds 14.6M BP (customer custody) | [Solscan](https://solscan.io/account/BbHG9GvPActFGogv3iNrpDAj4qpXr8t3jF16uGxXcKci) · [Arkham](https://intel.arkm.com/explorer/address/BbHG9GvPActFGogv3iNrpDAj4qpXr8t3jF16uGxXcKci) | A + B | 15 Nov 2026 |
| Arkham entity Backpack Exchange holds 204.8M BP across exchange wallets | [Arkham entity](https://intel.arkm.com/explorer/entity/backpack-exchange) | B | 15 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exact path to close it | Cost / access |
|---|---|---|---|
| 1 | ✅ **Closed:** role of `Eyzz…`, `43Db…`, `BbHG…` | Backpack wallet API + Arkham (see Selling) | — |
| 2 | Pre-IPO milestone list and dates for the 375M tranche | Ask Backpack (support / BP Program FAQ contact); watch treasury token account `2pWK2b…aU6s` with `getSignaturesForAddress` | Free |
| 3 | Exchange revenue | Audited accounts of Trek Labs Ltd (BVI, not public) or Backpack EU (CySEC filings) | Request / paid registry |
| 4 | Whether the treasury Squads `Aj8j59…` ever adds a time lock | Re-decode the Squads v4 account (`timeLock` field) monthly | Free |
| 5 | 7 Oct "trader key compromise" drain and the 91% tokenized-stock claim | Backpack status page / official X; on-chain trace of the named wallets | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
