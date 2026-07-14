# Expected Output — wcd_actualization.py

Frozen at the v0.9.0 release. Dependency-free; exact arithmetic; runs in a
fraction of a second. Run from this directory (or from
`verification/scripts/` — the live copy is identical):

```powershell
python wcd_actualization.py
## 1: 12 rays, 3 orthonormal frames, and the 48 return / 96 transfer split
  [PASS] the 12 rays split into 3 orthonormal frames of 4 (ortho=True); overlaps are {0,1} within a frame (True) and exactly 1/4 across frames (True); so the 144 = 12x12 ordered histories split into 48 return (same frame) + 96 transfer (cross frame).
## 2: the equivariant weight family (alpha,beta); Born kernel ONLY at alpha=beta
  [PASS] the weight family is a lawful positive stochastic response for all alpha,beta>0 (True); its closed form is P(p->p)=alpha/(alpha+2beta), P(cross)=beta/(4alpha+8beta), P(orthogonal)=0 (True); and the Born kernel {0,1/12,1/3} occurs at equal tickets alpha=beta (True) and there only -- P(p->p)=1/3 forces alpha=beta algebraically (True), while (alpha,beta)=(2,1) gives identity 1/2 (True). Counting forces the FORM; equal-tickets is an ADDED magnitude law.
## 4: the sign scar's real amplitude calculus -- 3 real MUBs, +-1/2 cocycle, 768 Hadamards
  [PASS] the three frames are three real mutually-unbiased bases: each frame is orthonormal (True), every cross-frame transition entry is +-1/2 (True), and the transition matrices compose exactly as a cocycle U_ut . U_ts = U_us (True); and there are exactly 768 real 4x4 Hadamard matrices supplying the {+1,-1} sign alphabet. So the retained Z_2 scar (z -> -z) makes amplitudes ADD with a real sign, with P=|A|^2 applied after.
## 3: positive additive counting is decohered (no interference); signs restore it
  [PASS] positive additive counting sums PROBABILITIES and is decohered: the minimal two-path witness has coherent |+1/2 + (-1/2)|^2 = 0 but decohered 1/4 + 1/4 = 1/2 (True); and across all 576 two-path interference configurations on the three frames the positive (probability-summing) value differs from the coherent |sum|^2 in every case (True), with the destructive value 0 reached coherently (288 configs) but never by positive counting. Amplitudes that ADD (the sign scar) are required for interference.
## 5: two independent gaps held open -- (a) the magnitude law, (b) the complex phase
  [PASS] (a) the magnitude law alpha=beta is not forced: (alpha,beta)=(2,1) and (1,2) are equally lawful positive stochastic phases with identity weights 1/2 and 1/5, neither 1/3 (True); and (b) the binary sign phase reaches only |1+s|^2 in {0,4} for s in {+1,-1}, so the complex value |1+i|^2 = 2 is unreachable (True) -- the enlargement from the {+1,-1} sign scar to a complex U(1) phase is a separate added ingredient. The two gaps are independent.

# RESULT: 5 passed, 0 failed
```

Every load-bearing quantity is exact (`fractions.Fraction` and exact integer
arithmetic); the frame geometry, the `(alpha,beta)` closed forms, the
two-path decoherence sweep, the mutually-unbiased-basis cocycle, and the
enumeration of the 768 order-4 Hadamard matrices are all exhaustive.
