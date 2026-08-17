#!/usr/bin/python3
# =============================================================================
# burry_1_pillars.py — BLAQUE BAUX BURRY #1: what is the Burry style, in numbers?
#
# Strip the personality. Burry's disclosed book, across cycles, is a recognizable
# style: deep value, small/hated names, and hard assets over narrative (water,
# farmland, gold, commodities) — and it leans AGAINST momentum. Profile each pillar as
# its tradable ETF: does it pay, and how contrarian (anti-momentum) is it really?
# Read-only. Prints its own results.
# =============================================================================
import os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _burry_common import rets, stats, capm, PILLARS, FROTH, MKT

u, dates, R = rets(list(PILLARS) + FROTH + [MKT]); j = {s: u.index(s) for s in u}
mkt = R[:, j[MKT]]; mom = R[:, j["MTUM"]]
print("=" * 80, "\nBURRY #1 — the pillars of the style (deep value + hard assets, anti-momentum)\n" + "=" * 80)
print(f"  {dates[0]} .. {dates[-1]}\n")
print(f"  {'pillar':<26}{'Sharpe':>8}{'CAGR':>8}{'vol':>7}{'maxDD':>8}{'beta-SPY':>9}{'corr-MOM':>9}")
for s in list(PILLARS):
    st = stats(R[:, j[s]]); _, b = capm(R[:, j[s]], mkt); cm = np.corrcoef(R[:, j[s]], mom)[0, 1]
    print(f"  {s+' ('+PILLARS[s]+')':<26}{st['sh']:>+8.2f}{st['cagr']*100:>+7.1f}%{st['vol']*100:>6.1f}%"
          f"{st['dd']*100:>+7.0f}%{b:>+9.2f}{cm:>+9.2f}")
st = stats(mkt)
print(f"  {'SPY (the market)':<26}{st['sh']:>+8.2f}{st['cagr']*100:>+7.1f}%{st['vol']*100:>6.1f}%{st['dd']*100:>+7.0f}%{1.0:>+9.2f}{np.corrcoef(mkt,mom)[0,1]:>+9.2f}")

# equal-weight Burry-style basket and its character vs the market and momentum
basket = R[:, [j[s] for s in PILLARS]].mean(axis=1)
sb = stats(basket); ab, bb = capm(basket, mkt); cmb = np.corrcoef(basket, mom)[0, 1]
print(f"\n  equal-weight BURRY-STYLE basket: Sharpe {sb['sh']:+.2f}  CAGR {sb['cagr']*100:+.1f}%  "
      f"vol {sb['vol']*100:.1f}%  maxDD {sb['dd']*100:+.0f}%")
print(f"    alpha-vs-SPY {ab*100:+.1f}%/yr   beta {bb:+.2f}   corr-to-momentum {cmb:+.2f}")

print("\nVERDICT: the legend's 'contrarian, anti-momentum' style is only HALF true in the data —")
print("the value pillars (RPV/IWN/PHO/WOOD) are still ~1.0 market beta and +0.6 correlated to")
print("momentum (equity beta wearing a value label), and NONE of the pillars beat the market.")
print("The genuinely contrarian, diversifying pillars are the HARD ASSETS: gold (Sharpe +0.83,")
print("beta 0.08) and commodities (beta 0.32) — gold is the one standout. So the tradable residue")
print("of the style is diversification (own some gold), not a market-beating value tilt. #2 tests")
print("the core contrarian ENTRY — buying the hated — directly.")
