# RELEASE — Chapter 62, "Equality Is an Event"

- **Tag:** v0.36.0
- **Concept DOI:** 10.5281/zenodo.21253591
- **Version DOI (v0.36.0):** recorded post-mint
- **Freeze date:** 2026-07-23

## Freeze record

This chapter freezes at v0.36.0 with one dependency-free verification script,
`verify_62_equality.py` (stdlib only: `fractions`, `itertools`, `math`; no
third-party packages). The script re-derives every exact result in the chapter
from first principles and exits nonzero on any failure.

## What the shipped script certifies (all [PASS] at freeze)

- **(a) Reception census.** One-use exactly-once = proper 2-coloring;
  realizability = bipartiteness. Two independent engines (brute-force
  enumeration; components-and-bipartiteness) agree on every topology. Exact
  N-counts: single edge N=2; odd 3- and 5-cycles N=0; even 4- and 6-cycles
  N=2; the discrete `ln 2` ladder.
- **(b) The three-object taxonomy (the correction).** `a ⊕ b ⊕ c = 0` is
  pairwise-complete with a positive global section (classical); the odd
  2-coloring cycle is pairwise-constrained and globally frustrated (the object
  the census actually hit); the Peres–Mermin square is pairwise-complete with
  no global `±1` assignment (genuine contextuality), certified via exact
  Gaussian-integer two-qubit observables and the row/column parity
  contradiction (rows → +1, columns → −1). The (B)≠(C) distinction is the
  retracted-conflation kill, made exact.
- **(c) The exact twins.** The depth-2 genesis reading-law amplitude table,
  recomputed inline from a self-contained successor engine in exact
  Gaussian-rational arithmetic, is rank-deficient for C5 (4 of 5) and C6 (5 of
  6) with `det G = 0` exactly; C4 is full rank. The null vector in each case is
  one canonical class minus another, coefficients `±1` — exact twins.

## Falsifiability

The script tests RANK, never PSD-ness (an `A·A†` construction is
positive-semidefinite by construction and cannot be falsified for positivity —
the retracted floor-run's exact error). Its closing comment enumerates, per
part, the outcome that would refute each claim.

## Runtime

Under one second on a standard interpreter (well within the ~30 s budget).
- Version DOI (v0.36.0): `10.5281/zenodo.21506169`
