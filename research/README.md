# Blaque Baux Burry — research

First-pass Path-A research on **the Burry mechanism, not the man.** All sketches read Alpaca SIP daily
bars, are read-only, and print their own results. 2016 – 2026.

> **Data note, up front.** Alpaca serves *price bars* — no fundamentals, no 13F holdings, no
> short-interest feed. A 13F is a 45-day-stale, long-only *label* anyway. So we test the style with
> price-only proxies: "deeply hated" → long-term price **reversal**; "deep value / hard assets" →
> tradable style **ETFs**; "contrarian short of froth" → short **ARKK** / high-momentum.

```bash
export $(grep -v '^#' ~/.config/blaquebaux/alpaca.env | xargs)   # or source it
python research/burry_1_pillars.py        # what the style is, in numbers
python research/burry_2_reversal.py       # does buying the hated still pay?
python research/burry_3_short_froth.py    # the contrarian short — edge or regime?
python research/burry_4_concentration.py  # concentration vs governance
```

## Scorecard

| # | Question | Result | Verdict |
|---|----------|--------|---------|
| 1 | What is the style, in numbers? | value pillars ~1.0 beta / +0.6 corr-to-momentum (equity beta); **no pillar beats SPY**; only **gold** (+0.83 Sharpe, 0.08 beta) is a real diversifier | ⚠️ half-legend — the residue is *own some gold*, not a value tilt |
| 2 | Does buying the *hated* pay? | HATED (worst-3y) **+0.76** < loved +0.83 < equal-wt +0.86 < SPY +0.89; long/short spread **Sharpe −0.00** | ❌ null — the contrarian entry is not a factor at scale |
| 3 | Is fading froth an edge? | short-ARKK **−0.59 Sharpe, −98% DD** full period; +1.26 only in the 2022 unwind; momentum-gated still −0.75 | ❌ regime, not edge — a widow-maker |
| 4 | Concentration vs governance? | top-1 CAGR +19.9% but **44% vol, −58% DD, ret/DD +0.34**; diversified top-15 has the *best* ret/DD (+0.39) | ❌ concentration raises drawdown as fast as return |

## The synthesis

**You cannot systematize Burry — and the honest attempt to says so cleanly.** Every replicable piece
of the style either collapses to beta, nulls out, or is a regime bet dressed as an edge:

1. **The style is half-legend.** The "contrarian, anti-momentum" value pillars (deep value, small
   value, water, timber) are in fact ~1.0 market beta and **+0.6 correlated to momentum** — equity
   beta wearing a value label — and *none of them beat the market* over 2016–2026. The only pillar
   that is genuinely contrarian and diversifying is **hard assets**: gold (Sharpe +0.83 at 0.08 market
   beta) and commodities. The tradable residue of "the Burry style" is *own some gold*, not a
   market-beating value tilt.
2. **Buying the hated is a null.** Long-term (3-year) reversal — the price-only proxy for Burry's
   deep-contrarian entry — *underperforms* buying the loved, equal-weighting, and the index, and the
   long-hated/short-loved spread is dead flat (Sharpe −0.00). At large-cap scale in this era, "buy what
   everyone hates" is a lumpy, regime-dependent patience bet, not a factor.
3. **Fading froth is regime, not edge.** Shorting the ARKK archetype *lost 27%/yr with a −98%
   drawdown* over the full decade — near-total ruin — and paid (+86%) only in the 2022 unwind. Even a
   momentum-gated version still bled (−0.75). This is the base's **Brute-Force law verbatim** ("you
   cannot fade the prop") plus **Bleed's** "timing the tail removes the tail." Burry's signature short
   is a *convex insurance bet*, not a systematic sleeve — and the family already expresses that
   properly through [Bleed](https://github.com/blaquebaux/bleed).
4. **Concentration is where the fame and the ruin both live.** Holding the single most-hated name
   returned +19.9%/yr — but at 44% vol, a −58% drawdown, and a *worse* return-per-drawdown (+0.34) than
   the diversified book (+0.39). Concentration lifts return and drawdown together; it does not improve
   risk-adjusted return, and the one-name book is a ruin machine whose whole path rides on a single
   position. This is exactly why the engine caps single names and sizes fractional-Kelly
   ([Brash](https://github.com/blaquebaux/brash)).

**Net:** Burry's edge is discretionary — timing, conviction, and concentration — which is precisely
what a governed process bounds *away*. What survives the test is not a Burry sleeve; it is two things
the family already has: **hard-asset diversification** and **tail insurance (Bleed)**. Burry joins
[Brute-Force](https://github.com/blaquebaux/brute-force) and
[Backsliders](https://github.com/blaquebaux/backsliders) on the honest shelf — a legend that does not
survive contact with the scorecard.

## Status
**Research: first pass complete — a cautionary null** (`research/`). The style is mostly beta, the
contrarian entry nulls out, the signature short is regime/ruin, and the concentration is uninvestable
as process. Tradable residue (gold, Bleed) already exists elsewhere in the family. No keeper, no live
driver; nothing validated to the spine's bar.
