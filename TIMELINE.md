---
title: Project timeline
last_updated: 2026-11-24
timezone: MST
disclaimer: Research only. Not financial advice. Not a recommendation to buy or sell. Not the work of a licensed fiduciary.
---

# Project timeline

**Research only. Not financial advice.** Times are in **MST**.

This is a chronological account of how Madman's Battlefield Intelligence and the Real Rails research desk grew. Counts are included only when a file in the research tree or this repository supports them. Unsourced figures are not invented. A dated log of methodology, scoring-version and process-rule changes is in [CHANGELOG.md](CHANGELOG.md). Published v3 scores over time are in [HISTORY.md](HISTORY.md).

The desk answers a single research question: is a token actually used by a business that moves money or tokenized assets, or is it only marketing? Nothing here is financial advice, a recommendation to buy or sell, or the work of a licensed fiduciary.

---

## Two published layers

The public GitHub tree and the internal Real Rails ranking are related, but they are not the same scorecard and they do not have the same head-count.

| Layer | What it is | Latest sourced count | As of (MST) |
|---|---|---|---|
| Daily market tape in this repo | One Markdown + JSON report per saved day | **26** daily reports, 16 October – 13 November 2026 | First commit, 15 November |
| Published v3 token reports in this repo | 11-section, 0–10 scorecard | **184** scored reports (**7** pass, **177** fail) | 16–17 November |
| All Projects catalog in this repo | Every name in the public pipeline | **292** coins: 184 scored, 15 not a token, 93 dead or wound down (21 of those Unverified) | 16 November |
| Real Rails triage, v69 | 0–100 first-pass ranking | **155** ranked, **70** Watch, **812** disqualified (**1,037** screened) | 10 November version; still the live stamp on 22 November |
| Real Rails coin reports | Markdown + JSON write-out of the triage reports | **284** unique coins (**568** files) | 22 November |

The v3 cover sheet in this repository states that the published grade is the v3 scorecard, not the 0–100 triage script. [CHANGELOG.md](CHANGELOG.md) explains each methodology version.

---

## 16 October 2026 — Daily market tape begins

The earliest dated public artifact in this repository is [daily/2026-10-16.md](daily/2026-10-16.md), a morning market snapshot in MST from public sources (CoinGecko, DexScreener, DefiLlama Hacks, and vetted headlines). The first commit later bundled **26** daily reports running through [13 November 2026](daily/2026-11-13.md). Days without a file are not a claim that the market was quiet; they are days without a saved public snapshot.

---

## 3 November 2026 — Real Rails first-pass ranking

Dated snapshots `ranking_v60_post` through `ranking_v62_post` were generated on 3 November. Each has **222** ranked coins and **815** disqualified, labelled as first-pass proxies, not verified rankings. The internal element table dates the first screening and scoring layers to this day: disqualifiers, token necessity, usage and revenue, partner confirmation, licences, creator fact-check, decay, evidence tiers, a dated-promise ledger, 90-day GitHub activity, and a treasury-health rubric. **1,037** coins were screened.

---

## 4–8 November 2026 — Deeper evidence layers

On 4 November the desk added legal-entity registry checks, team-page reads, and (from file dates) a daily video scan plus fact-check workflow. On 6 November Madman approved reported-only elements #22–#28 (admin keys, holder concentration, audits, real yield, reserve attestations, and company-level litigation or sanctions) and a standing rule: every new element is back-applied to all previously investigated projects, then **281** coins (222 ranked plus 59 hand-reviewed non-ranked).

On 8 November the promise-ledger math and a conservative hack-response rubric were adopted (ranking snapshots v63–v65), and Element #29 widened personnel checks to the whole listed core team and claimed developers. Response grades from that first pass stayed Unverified, which under the rubric is a neutral adjustment, not a hidden penalty.

---

## 9–10 November 2026 — v66 through v69, and reported burn/unlock

9 November was a dense scoring day, all on the 0–100 triage, not on the public v3 grades:

- **v66** incorporated fact-check upgrades from a weekly self-review.
- **v67** stopped single-claim amplification and clamped negative reported revenue at zero for the usage formula.
- Elements **#30** (real burn vs marketing burn) and **#31** (unlock and inflation pressure) were approved as reported-only checks.
- **v68** (1:12 PM MST) added Midnight (NIGHT), Ethena (ENA) and Backpack (BP). Ranked coins rose to **225**, with 812 disqualified. All 225 later received burn and unlock checks. A quality pass then required a primary source URL before a check could be marked done.

On 10 November at 1:19 PM MST, **v69** became the current methodology version. Treasury scoring switched to badge-driven Option B, a Watch tier was added for thinly evidenced coins, missing-evidence defaults were lowered, and every report was version-stamped. The numbered list fell from 225 to **155**, with **70** coins scored but unranked in Watch, and **812** still disqualified. The mean 0–100 score fell from 35.0 to 26.4, mostly because of those lower defaults and because Watch coins left the numbered list. A frozen snapshot from that afternoon is the v69 baseline. The live ranking file still carries the v69 stamp as of 22 November, 4:48 PM MST.

---

## 12–13 November 2026 — Process rules P1–P11

After an outside audit of a 12 November EDEL report, Madman approved seven research process rules (P1–P7) on 12 November: bridge-peer enumeration, address typing, documented sweeps for absence claims, the latest-status rule, checking the standard source before calling a figure unsourced, reconciling prior research, and a blind review of negative claims. These are process rules. They do not change the v69 formula.

On 13 November four more rules (P8–P11) were approved: resolve every proxy, count staked or receipt positions toward the depositor, timestamp snapshot figures after the last material event, and record the destination and announcement when liquidity moves. Three display and research corrections were applied the same morning (EDEL address typing, a ZAMA multi-chain supply check, and a sourced DefiLlama fees-and-revenue line on 83 reports). P8–P11 have not yet been back-filled to other coins. The last daily report currently in this public tree is also dated 13 November.

---

## 14–17 November 2026 — The public repository

| When (MST) | What the files show |
|---|---|
| 14 November, 7:48 AM | GitHub created the public repository `MadmansBattlefield/madmans-battlefield-intelligence`. |
| 14 November (ranking date in the first tree) | **18** scored v3 reports were already in the ranking file that shipped with the first commit. |
| 15 November, 6:07 AM | First commit. The tree also held the 26 daily reports, the cover sheet, and the v3 rulebook. The research desk is credited to **Sentinel**. |
| 15 November, 6:37 PM | Nine v3 reports added; the ranking listed **27** notes, with clickable evidence trails. |
| 16 November, 4:55 AM – evening | The public ranking climbed through the day (28, 33, 38, 43, 48, 53, 58, 63, 68, 73, 83, 88, 92, 96, 99, 104, 108, 112, 113, then 118 and upward under the 16 November rules) and closed at **184** scored v3 reports. The All Projects catalog was added (293 names, then **292** after a duplicate was removed). Fifteen not-a-token entries and 93 dead or wound-down names were excluded from the ranking and the base rates. The 16 November v3 upgrades — companion JSON, Arkham label confidence, pre-registered pump-day rules, the holder-accrual test, dual review, history, base rates, the dead list, and the reproducibility package — were published. They apply to reports first published or substantively updated on or after that date. |
| 17 November, 4:43–5:39 AM | CoinGecko pump-day dates were corrected, a predecessor-ATH rule was added, confirmed report fixes were applied, and ONDO's 0xEA57 Coinbase payouts were treated as a proven one-hop sale. [HISTORY.md](HISTORY.md) was generated at 5:38 AM. The last commit to `main` in this repository, as of 24 November, is 5:39 AM; **68** commits in total, on 15–17 November. |

---

## 22 November 2026 — Element #32 and a 284-coin report rebuild

Madman approved Element **#32**, "Revenue / income stream in testing," as a reported-only layer (stages R0–R5; no score credit until live revenue is observed). A daily REV-TEST flag was added to queue primary-source checks. First items: HBAR CLPR and ICP Cloud Engines, plus a dated CRO buy-and-burn promise.

The same day brought approved supply, fee-routing and fact-check corrections (HBAR, INJ, CFG, APT, ONDO, JST, SKY, ENA, PACT and others; detail in the changelog), and @CheekyCryptoPlus was added as a lead-only video source. Coin reports were rebuilt: **284** unique coins, **568** Markdown and JSON files.

A v69 triage rerun after the morning batch moved a few mid-list ranks (SOL, already #1, 62.6 → 62.9; DOT and TRAC entered the top 50; RED and ACH left it). The top 10 did not change, and the formula did not change. Two later reruns the same afternoon produced no further score or rank changes. The live ranking file at 4:48 PM MST still reads **155** ranked, **70** Watch, **812** disqualified, methodology **v69**.

Work after 22 November, including any later wallet-label research, is not in this timeline until it is approved and logged.

---

## What this file does not claim

- It does not treat the 0–100 triage scores as the published v3 grades, or the 284 internal coin reports as if they were all in this public tree.
- It does not invent a start date earlier than 16 October 2026, the first dated daily report here.
- It does not project future counts. New milestones should be added in date order, in MST, with a source in this repository or in a dated ranking snapshot.
