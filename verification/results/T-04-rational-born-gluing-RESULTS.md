# Rational Born As Counting Through Gluing - RESULTS

Claim IDs: T-04, T-04b (supports FCT-10 counting and FCT-16 CHSH/Pell)  
Status: PASS  
Script: `verification/scripts/rational_born_gluing.py`  
Command: `python verification/scripts/rational_born_gluing.py`  
Date run: 2026-07-07  
Environment: Windows, Python 3.13.12  
Dependencies: Python standard library only  
Expected runtime: under 5 seconds  
Observed runtime: under 1 second as part of `run_all.py`

## Frozen Registration

- Claim under test: rational Born weights are witness counts on a refined
  exclusive fiber, pushed through the reception/gluing quotient.
- Inputs and parameters: a normalized context with witness counts `(2,2,1)`,
  `K = 5` (the same fork as the shipped frequency-bridge check); a two-context
  structure with counts `(2,1)` and `(1,2)` and non-exclusive cross pairs.
- Enumeration rule: exhaustive over the refined sub-event set and all sub-event
  pairs.
- Success gate:
  - uniform counting `1/K` on the refined fiber pushes forward to `p_i = k_i/K`;
  - each weight equals a witness-fiber cardinality, `p_i = k_i/N` with `N = K`;
  - refined sub-events are exclusive iff siblings or lifting a base
    exclusivity; non-exclusive base pairs stay non-exclusive;
  - with interchangeable witnesses the only normalized invariant weighting is
    uniform counting (zero free degrees of freedom).
- Failure gate: any exact identity fails.
- Controls: a within-block-only interchange admits a non-counting normalized
  weighting (two free degrees of freedom), so the witness-interchange premise
  is shown to be load-bearing rather than vacuous.
- Exploratory-only outputs: none. All checks are exact rational arithmetic.

## Results

Stable output:

```text
rational_born_gluing
counts=[2, 2, 1] K=5 p=['2/5', '2/5', '1/5']
pushforward=PASS sub_weight=1/5 N=5 (uniform counting -> p)
exclusivity_lift=PASS sibling_pairs=2 cross_exclusive=4 cross_free=9
uniqueness_core=PASS full_interchange_free_dof=0 within_block_free_dof=2 (premise is load-bearing)
RESULT: PASS
```

Verdict: PASS.

## Residuals

- This ships the exact pushforward-counting and exclusivity-lift core plus the
  witness-interchange uniqueness argument. It does not ship the one-receiver /
  theta-body gluing-consistency certificate (a semidefinite feasibility check),
  which remains cited from the private research corpus.
- Residuals `[E-FREE]`, general `[GLUE]`, `[REAL]`, and `[GENERIC]` remain as
  named in the theorem bank and claim register.

## Reproduction

1. Start from a clean clone.
2. Run `python verification/scripts/rational_born_gluing.py`.
3. Confirm the stable output ends in `RESULT: PASS`.
