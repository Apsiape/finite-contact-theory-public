# Chapter 64 — freeze record

- Release tag: `v0.36.0`
- Concept DOI (the program, all versions): `10.5281/zenodo.21253591`
- Version DOI (v0.36.0): `10.5281/zenodo.21506169`
- Chapter deposit DOI: none (repository deposit only).
- Freeze date: 2026-07-23.

Shipped artifact: `verify_64_tower.py` (stdlib only: `fractions`, `itertools`,
`math`; no third-party dependencies). Prints per-check `[PASS]`/`[FAIL]`, exits
nonzero on any failure, and closes with a falsifiability note. Re-derives the
chapter's exact results: the top-cell half-eraser at rungs 2–5 over mod 2 and
mod 4; the characteristic-two Weyl relation `DU + UD = 1` and the four-way law
sector on `F2[x]`; the `p = 2` uniqueness; vertical exactness `x^4 = D(x^5)`;
the Bockstein carry `beta(omega_n)` pattern for `n = 1..6`; the Witt / `Z/4`
extension-class identification of the mirror; and the carry-depth formula
`nu_2(Catalan(n-1)) = s_2(n) - 1` for `n = 2..40`.
