# Blaque Baux Burry

**Michael Burry's book, re-examined — the mechanism, not the man.**

Burry is a member of the Blaque Baux family. The [core repo](https://github.com/blaquebaux/base)
is the **engine and blueprint** — a governed, systematic platform (Julia) with a venue-agnostic
execution controller and a Layer-3 live-money safety gate. Burry points that engine in its own
direction and inherits the governance wholesale.

> **Not investment advice.** Educational/research software. Nothing here is validated. See [LICENSE](LICENSE).

```bash
git clone --recursive https://github.com/blaquebaux/burry.git
julia --project=engine -e 'using Pkg; Pkg.instantiate()'   # one-time engine setup
```

## The thesis

Michael Burry is famous for concentrated, contrarian, deeply-researched bets — subprime in 2007,
and a rotating book of hated deep-value names and macro shorts since. The temptation is to *copy the
man*: read the 13F, buy what he bought. That is a losing game — 13Fs are 45 days stale, show only
long US equity (not shorts, options, or sizing), and the edge was never the ticker; it was the
process.

Burry asks a different question: **is the mechanism underneath his book systematizable?** Strip the
personality and what remains is a recognizable style — low price-to-book, high free-cash-flow yield,
out-of-favor and heavily-shorted names, hard assets over narrative. We treat the disclosed book as a
*label*, decompose it into factor exposures, and test whether that exposure still carries a premium
**net of cost** — and whether the contrarian short leg is a real edge or a widow-maker.

## Research plan (Path A — not yet built)

- **Decompose the book.** Map the disclosed 13F positions onto factor exposures (value, quality,
  size, low-beta, "hatedness" = short interest / days-to-cover). What *style* is Burry, in numbers?
- **Does the style still pay?** Test the systematic version — deep value + high FCF yield + contrarian
  (high short interest) — cross-sectionally, net of cost, with the base's purged K-fold / walk-forward
  bar. Value has been a decade-long null; does the contrarian overlay revive it, or is this hindsight?
- **The short leg, honestly.** Burry's shorts are his signature and his biggest risk. Test whether a
  rules-based "expensive + deteriorating + crowded-long" short adds anything, or whether — like the
  base's Brute-Force finding — you cannot fade the prop and the tail eats the edge.
- **Concentration vs. governance.** Burry runs a handful of large bets; the engine's crowding and
  single-name caps are the opposite instinct. Study the trade-off explicitly.

Nothing above is implemented or validated. This is the map, not the territory.

## Status
**Concept.** Thesis and research plan only — no sketches run, no driver, nothing validated to the
spine's bar. A lens on a famous book, to be tested like everything else here.

## About Blaque Baux

**Blaque Baux** is a quantitative research initiative and a subsidiary of **[Carter Warrens](https://carterwarrens.com)**.
[**BlaqueBaux.com**](https://blaquebaux.com) is the home for the work; the code lives here on GitHub — open to
study, test, and build bespoke strategies on top of.

Anyone can point an AI at a market. The edge is **understanding what the data actually says — and turning it
into something you can act on.** We test relentlessly and put most of it *on the record as rejected, with the
reason*; what survives is built, governed, and validated before it is ever called real. That combination —
honest research, reproducible evidence, and execution you can trust — is why Carter Warrens leads on
**strategy and implementation**, not merely uses the tools everyone now has.

## The Blaque Baux family
This repo is one sleeve of the **Blaque Baux** family — a single governed engine steered in
many directions. The [core repo](https://github.com/blaquebaux/base) is the
base/blueprint and holds the [full family roster](https://github.com/blaquebaux/base#the-blaquebaux-family).

## Layout
```
engine/     the Blaque Baux platform (git submodule -> blaquebaux/base)
research/   the research plan (Path A) — sketches land here once run
live/       governed live drivers (once a sleeve graduates to paper A/B)
```

## License
[MIT](LICENSE). (c) 2026 Carter Warrens.
