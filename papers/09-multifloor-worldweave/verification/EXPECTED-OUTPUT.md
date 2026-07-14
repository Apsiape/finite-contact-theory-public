# Expected Output — multifloor_worldweave.py

Frozen at the v0.9.0 release. Dependency-free; run from this directory (or
from `verification/scripts/` — the live copy is identical):

```powershell
python multifloor_worldweave.py
```

Runtime is a few seconds (exhaustive exact arithmetic, including the full
`4^9` self-dual code census). Expected output, verbatim:

```text
## 1: the triality boundary K = C_2 x C_2 with S_3 triality
  [PASS] the boundary group K = GF(4)-additive is Klein-four (every nonzero element an involution, v+s=c cyclically: True); its structure automorphisms realize all 6 permutations of {v,s,c} = S_3. This D_4 triality boundary is the substrate every cell carries into the multi-floor code.
## 2: two cells close uniquely into the E_8 root system
  [PASS] the two cells' D_4 boundaries close into 240 roots = 48 (D_4+D_4) + three triality-matched 64-root bridges (8v,8v)/(8s,8s)/(8c,8c) (True); the set is reflection-closed (True) -- the E_8 root system; the glue-lattice determinant ladder D_4^2 / D_8 / E_8 = 16 / 4 / 1 = 16 / 4 / 1 (bridge debt 4 -> 2 -> 0 bits). E_8 is the unique debt-free two-cell world -- the complete bridge geometry, not a physical gauge group.
## 3: local fusion dynamics is octonionic (a three-contact receipt)
  [PASS] of the C(7,3) = 35 triples of distinct octonion imaginary units, exactly 7 associate and 28 have a nonzero associator (the 7 Fano lines / 28 non-lines). Nonassociativity is carried only by triples -- an exact three-contact order receipt: every pair looks quaternionic while the triple retains information belonging to no pair.
## 4: normed monolithic fusion stops at the octonions
  [PASS] the sedenions (dimension 16) have a zero divisor (e_1+e_10)(e_4-e_15) = 0 with both factors nonzero, while the octonions have none (True). So positive normed monolithic fusion stops at the octonions; a larger population cannot be one division algebra and must remain a code worldweave of octonionic cells.
## 5: the self-dual bridge-code census is |GU(k,2)| = 3 / 18 / 648
  [PASS] triality-covariant Hermitian self-dual standard-form codes number 3 (N=2), 18 (N=4), 648 (N=6) -- exactly |GU(k,2)| for k = N/2 (3, 18, 648). Receiver-complete worlds are the unitary orbit over GF(4), so the exhaustive standard-form search is confirmed by closed form.
## 6: six cells are the first hidden collective world
  [PASS] the hexacode [6,3,4] over GF(4) has weight enumerator 1 + 45 y^4 + 18 y^6 (True), is Hermitian self-dual (True), and has minimum distance 4 = 4 (no one-, two-, or three-cell bridge words); and of the 648 self-dual six-cell codes, exactly 162 have minimum distance 2 and 486 have minimum distance 4 (162 / 486). Six cells are the first population that can form a complete world whose binding is invisible to every pairwise and triple glue probe.

# RESULT: 6 passed, 0 failed
```

The script exits `0` on all-pass. Every load-bearing quantity is exact
(`fractions.Fraction` and exact `GF(4)` arithmetic); the E_8 decomposition
and reflection closure, the octonion associator census, the sedenion
zero-divisor search, the hexacode, and the self-dual code census (all
`4^9` candidate matrices) are exhaustive.
