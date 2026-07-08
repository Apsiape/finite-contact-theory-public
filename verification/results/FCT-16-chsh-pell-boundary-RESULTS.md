# CHSH/Pell Boundary Core - RESULTS

Claim IDs: FCT-16 / T-05  
Status: PASS  
Script: `verification/scripts/chsh_pell_boundary.py`  
Command: `python verification/scripts/chsh_pell_boundary.py`  
Date run: 2026-07-07  
Environment: Windows, Python 3.13.12  
Dependencies: Python standard library only  
Expected runtime: under 5 seconds  
Observed runtime: under 1 second as part of `run_all.py`

## Frozen Registration

- Claim under test: the exact CHSH/Pell boundary core at rational scope.
- Inputs and parameters: the refinement map `L(x) = (3x + 4)/(2x + 3)`; the
  ladder from `x0 = 1`; the CHSH readout `CHSH(x) = 4 - 4/(2 + x)`.
- Enumeration rule: five refinement steps from `x0 = 1`; a fixed control rung
  `x = 3/2`.
- Success gate:
  - the map fixed point satisfies `x^2 = 2`;
  - the ladder is `1, 7/5, 41/29, 239/169, 1393/985, 8119/5741` exactly;
  - every rung satisfies the negative-Pell equation `p^2 - 2 q^2 = -1`, so every
    rung is strictly below `sqrt(2)`;
  - the CHSH ladder is `8/3, 48/17, 280/99, 1632/577, 9512/3363` exactly and
    strictly increasing toward `2*sqrt(2)`;
  - the fence sign `2 q^2 - p^2` places the control rung `3/2` above `sqrt(2)`.
- Failure gate: any exact identity fails.
- Controls: the upper convergent `x = 3/2` verifies the fence discriminates both
  sides of the boundary.
- Exploratory-only outputs: none. Floating-point values are display-only; every
  gate is exact integer/rational arithmetic.

## Results

Stable output:

```text
chsh_pell_boundary
fixed_point=x^2=2 (2x^2=4 at the map fixed point)
ladder=1, 7/5, 41/29, 239/169, 1393/985, 8119/5741
pell_invariant=p^2-2q^2=-1 for every rung (strictly below sqrt(2))
chsh_ladder=8/3, 48/17, 280/99, 1632/577, 9512/3363
chsh_floats=2.666666667, 2.823529412, 2.828282828, 2.828422877, 2.828427000
tsirelson_2sqrt2=2.828427125 gap_last=1.25e-07
fence_control x=3/2 -> above sqrt(2), chsh=20/7 (2.857142857)
RESULT: PASS
```

Verdict: PASS.

## Residuals

- This is the exact rational ladder + fence core, not the full theta-body /
  semidefinite boundary certificate.
- Scope is the CHSH family and one graph family; general-scenario boundary
  results remain cited or held.
- Irrational weights (`2*sqrt(2)` itself) enter through the `[REAL]` completion
  posture; the shipped check verifies the rational approach and the exact Pell
  invariant, not a completed-real object.

## Reproduction

1. Start from a clean clone.
2. Run `python verification/scripts/chsh_pell_boundary.py`.
3. Confirm the stable output ends in `RESULT: PASS`.
