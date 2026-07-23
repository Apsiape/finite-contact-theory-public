# Chapter 65 — freeze record

- Release tag: `v0.36.0`
- Concept DOI (the program, all versions): `10.5281/zenodo.21253591`
- Version DOI (v0.36.0): recorded post-mint.
- Chapter deposit DOI: none (repository deposit only).
- Freeze date: 2026-07-23.

## Shipped with this chapter

- `paper.md` — the full chapter (house style; labels THEOREM (model scope) /
  RECOVERY / RECEIVED / EXTENSION / OPEN throughout; the McKay firewall and
  the Kitaev-E8 note as mandatory subsections).
- `verify_65_e8.py` — dependency-free (stdlib: `fractions`, `itertools`,
  `math`) re-derivation of every load-bearing count. Prints `[PASS]`/`[FAIL]`
  lines, exits nonzero on any failure, runtime well under 60 s. Closes with a
  falsifiability note.

## What the shipped script certifies (all exact, no floating point)

1. The pentagon five-edge loop-sign equals the 3-cochain coboundary δf, for all
   256 grading-local rules across all 16 charge sectors; 0/256 reproduce the
   essential class ω4 = abcd; the μ4 i-dressing flattens it (δg = 2·abcd mod 4).
2. ⟨i, j⟩ = Q8 (8 units); ⟨i, j, ω⟩ = the 24 Hurwitz units (2T = the 24-cell),
   equal to the constructed 8 Lipschitz + 16 half-integer set; each of the 16
   units outside Q8 regenerates 2T (minimality, index 3 prime); the rotor
   τ = (1+i+j+k)/2 satisfies τ² = ω, τ³ = −1, τ⁶ = 1, and conjugation by τ
   cycles i → j → k → i.
3. Glue enumeration over (Z/2)⁴: 35 order-4 subgroups, exactly 6 even, all 6
   graphs of automorphisms (= S3 = triality), each yielding 240 roots via
   24 + 24 + 3·8·8.
4. The E8 lattice has 240 norm-2 vectors with the D4+D4-frame decomposition
   24 + 24 + 64 + 128.
