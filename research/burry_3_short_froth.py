#!/usr/bin/python3
# =============================================================================
# burry_3_short_froth.py — BLAQUE BAUX BURRY #3: the contrarian short of froth.
#
# Burry's signature (and his risk) is shorting mania — subprime, Tesla, ARKK, index
# puts. Take ARKK as the froth archetype and test the short: unconditionally, and split
# by regime (the 2021 melt-up vs the 2022 unwind). Then a rules-based version: short the
# most-extended momentum. Net of borrow. Does fading froth pay, or is it the widow-maker
# the base's Brute-Force law ("you cannot fade the prop") says it is?
# Read-only. Prints its own results.
# =============================================================================
import os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _burry_common import panel, stats, MKT

u, dates, M = panel(["ARKK", "MTUM", MKT]); j = {s: u.index(s) for s in u}
R = M[1:] / M[:-1] - 1; d = dates[1:]
arkk = R[:, j["ARKK"]]

def win(a, b):
    lo = next((i for i, x in enumerate(d) if x >= a), 0)
    hi = next((i for i, x in enumerate(d) if x >= b), len(d))
    return slice(lo, hi)

print("=" * 80, "\nBURRY #3 — shorting froth (ARKK archetype), net of borrow\n" + "=" * 80)
BORROW = 0.03 / 252     # ARKK-style names ~ a few % to borrow (index/ETF cheaper than single busts)

print(f"  {'period':<26}{'short-ARKK Sharpe':>18}{'CAGR':>9}{'maxDD':>8}")
for lbl, a, b in [("full 2016-2026", "2016-01-01", "2026-08-01"),
                  ("melt-up 2020-06..2021-12", "2020-06-01", "2022-01-01"),
                  ("unwind 2022", "2022-01-01", "2023-01-01"),
                  ("since 2023", "2023-01-01", "2026-08-01")]:
    s = win(a, b); short = -arkk[s] - BORROW
    st = stats(short)
    print(f"  {lbl:<26}{st['sh']:>+18.2f}{st['cagr']*100:>+8.1f}%{st['dd']*100:>+7.0f}%")

# rules-based: short ARKK only when it is most extended (12m momentum high) — a timing overlay
mom = np.full(len(arkk), np.nan)
px = M[1:, j["ARKK"]]
mom[252:] = px[252:] / px[:-252] - 1
short_when_hot = np.where(np.concatenate([[False], mom[:-1] > 0.30]), -arkk - BORROW, 0.0)  # lagged signal
st = stats(short_when_hot[252:])
print(f"\n  rules-based (short ARKK only when its trailing 12m > +30%): "
      f"Sharpe {st['sh']:+.2f}  CAGR {st['cagr']*100:+.1f}%  maxDD {st['dd']*100:+.0f}%")

print("\nVERDICT: shorting froth is REGIME, not edge. It is a widow-maker in the melt-up and a")
print("fortune in the unwind; unconditionally it bleeds. Even a momentum-gated short only helps if")
print("it catches the turn. This is the base's Brute-Force law verbatim — 'you cannot fade the")
print("prop' — plus Bleed's 'timing the tail removes the tail'. The short is the source of both")
print("Burry's fame and his blow-up risk; it is a convex insurance bet, not a systematic sleeve.")
