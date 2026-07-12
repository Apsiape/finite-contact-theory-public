# Expected Output — exact_gap_certificate.py

Frozen at the v0.2.0 release. Run from this directory:

```powershell
python exact_gap_certificate.py
```

Expected output, verbatim:

```text
behavior p = ['49/100', '25/81', '16/25', '36/121', '4/9']
beta = 2137213/980100 = 2.180607080910

  [PASS] real rigidity system nonsingular (det != 0): Re(H) = H* UNIQUE  det = 112/495
  [PASS] H* v = beta v (exact)
  [PASS] witness: y^T H* y < 0 (exact; kills the WHOLE Hermitian family)  = -17658032557963925693/179590693860103680000 = -0.098323762
  [PASS] H_feas: diag = 1, exclusivity edges = 0 (by construction)
  [PASS] H_feas - v v^T POSITIVE DEFINITE (exact LDL, all 5 pivots > 0)  pivots ~ ['0.51000', '0.39482', '0.02160', '0.02902', '0.01905']

CERTIFIED: Delta_prep(p) > 0 for p = (49/100, 25/81, 16/25, 36/121, 4/9).
Every sharp quantum realization of this behavior has capacity strictly
greater than beta = 2137213/980100. (Numerical SDP value of the gap:
Delta_prep ~ 0.0096474 -- the strictness is what this file proves.)
```

Exit code 0. Every load-bearing check is exact rational arithmetic
(`fractions.Fraction`); the two decimal expansions shown are display-only.
The float pivot display may differ in the last digit across platforms; the
PASS/CERTIFIED lines and all exact fractions may not.
