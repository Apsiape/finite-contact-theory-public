# Results — `becoming_webs.py` (FCT-34..FCT-37 / T-26..T-29)

Status: shipped result ledger for the chapter-5 verification script.

## What the script verifies

Dependency-free (Python 3 standard library only), fully deterministic (no
randomness — every check exhaustive at its stated scope). Five checks:

1. **T-26 (FCT-34), torsor time**: heap axioms (including
   para-associativity, five nested quantifiers) exhaustive on `Z_5`, `Z_6`,
   `Z_7`; group recovery at every choice of origin; freeness and
   transitivity of translations — no invariant element.
2. **T-27 (FCT-35), the helix**: unique path lifting from every start;
   monodromy exactly `q = 1` per visible cycle from every basepoint; deck
   translations commute with the dynamics.
3. **T-28 (FCT-36), the arrow**: exhaustive over all 510 step words to
   length 8 on the reversible `Z_4` rotation with a step ledger — 170
   visible returns, zero nonempty joint returns, ledger gap = steps asked.
4. **T-29a (FCT-37), productive self-reference**: `x = cons(a, x)` has one
   solution at every truncation depth 1..4 from every initial guess;
   `x = tail(x)` has two at every depth.
5. **T-29b (FCT-37), the Möbius twist**: zero global sections for the
   twisted cover, two for the untwisted control, local sections perfect.

## Reproduction

```powershell
python verification\scripts\becoming_webs.py
```

Expected output is frozen verbatim in
[`papers/05-becoming-webs/verification/EXPECTED-OUTPUT.md`](../../papers/05-becoming-webs/verification/EXPECTED-OUTPUT.md).
All five checks print `[PASS]`; the script exits `0` and prints
`RESULT: ALL CHAPTER-5 CHECKS PASS`.

## What this does not show

These are possibility/impossibility theorems about time-like structure at
finite-model scope. They do not show that nature's time is a torsor, that
its arrow is ledger-bookkeeping, or that its simultaneity is twisted — the
program-facing readings are cited, not claimed.
