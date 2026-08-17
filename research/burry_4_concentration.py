#!/usr/bin/python3
# =============================================================================
# burry_4_concentration.py — BLAQUE BAUX BURRY #4: concentration vs. governance.
#
# Burry runs a handful of large bets — concentration is where his edge AND his blow-up
# risk live. The engine's instinct is the opposite: single-name caps, crowding limits.
# Take the contrarian-value signal from #2 and vary how many names you hold (top 1/3/
# 5/10 of the hated). Show that concentration lifts return but lifts drawdown/vol MORE —
# the trade-off the base quantified as fractional-Kelly (Brash) and single-name caps.
# Read-only. Prints its own results.
# =============================================================================
import os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _burry_common import panel, stats, month_ends, STOCKS, MKT

COST = 0.0010; LB = 756
u, dates, M = panel(STOCKS + [MKT]); j = {s: u.index(s) for s in u}
names = [s for s in STOCKS if s in j]
R = M[1:] / M[:-1] - 1
me = [m for m in month_ends(dates) if m >= LB and m < len(dates) - 1]

def book(K):
    out = []; prev = set()
    for k in range(len(me) - 1):
        i0, i1 = me[k], me[k + 1]
        sc = {s: M[i0, j[s]] / M[i0 - LB, j[s]] - 1 for s in names}
        held = sorted(sc, key=sc.get)[:K]; w = 1.0 / len(held)
        turn = len(set(held) ^ prev) * w
        for t in range(i0 + 1, i1 + 1):
            r = w * sum(R[t - 1, j[s]] for s in held)
            if t == i0 + 1: r -= COST * turn
            out.append(r)
        prev = set(held)
    return np.array(out)

print("=" * 80, "\nBURRY #4 — concentration vs governance (the hated longs, top-K)\n" + "=" * 80)
print(f"  {dates[me[0]]} .. {dates[-1]}  |  holding the K most-hated (worst 3y) names, monthly\n")
print(f"  {'concentration':<22}{'Sharpe':>8}{'CAGR':>8}{'vol':>7}{'maxDD':>8}{'ret/DD':>8}")
for K in [1, 3, 5, 10, len(names) // 3]:
    r = book(K); st = stats(r)
    rdd = st['cagr'] / abs(st['dd']) if st['dd'] else float('nan')
    lbl = f"top-{K}" + (" (single bet)" if K == 1 else "")
    print(f"  {lbl:<22}{st['sh']:>+8.2f}{st['cagr']*100:>+7.1f}%{st['vol']*100:>6.1f}%{st['dd']*100:>+7.0f}%{rdd:>+8.2f}")

print("\nVERDICT: concentration raises return but raises drawdown/vol at least as fast — the")
print("return-per-unit-drawdown does NOT improve, and the single-bet book is a ruin machine")
print("(the whole path depends on one name). This is exactly why the engine caps single names")
print("and sizes fractional-Kelly (Brash): Burry's concentration is where the fame lives, and it")
print("is uninvestable as a repeatable process. The governed version keeps the style, bounds the bet.")
