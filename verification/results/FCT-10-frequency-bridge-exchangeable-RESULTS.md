# Frequency Bridge Exchangeable Core - RESULTS

Claim ID: FCT-10 / T-03  
Status: PASS  
Script: `verification/scripts/frequency_bridge_exchangeable.py`  
Command: `python verification/scripts/frequency_bridge_exchangeable.py`  
Date run: 2026-07-07  
Environment: Windows, Python 3.13.12  
Dependencies: Python standard library only  
Expected runtime: under 10 seconds  
Observed runtime: under 1 second as part of `run_all.py`

## Frozen Registration

- Claim under test: for a finite fixed fork with multiplicities `(2,2,1)`,
  deviant empirical type shares are exactly countable and satisfy the finite
  type bound.
- Inputs and parameters: multiplicities `(2,2,1)`, shares `(2/5,2/5,1/5)`,
  exact checks at `T=12` and bound checks at `T=6,12,24,48`.
- Success gate: exact deviant shares match the registered rational targets and
  all tested shares lie below the type bound.
- Failure gate: any exact target or inequality fails.
- Controls: this is the exchangeable positive core. The growing-floor
  compensator and greedy/anti-greedy controls remain cited from the private research corpus.
- Exploratory-only outputs: none.

## Results

Stable output:

```text
frequency_bridge_exchangeable
multiplicities=(2, 2, 1)
shares=('2/5', '2/5', '1/5')
T=12 eps=1/10 share=227109457/244140625 share_float=0.930240336 bound=2069.056680285
T=12 eps=1/5 share=198724177/244140625 share_float=0.813974229 bound=1728.221410763
T=12 eps=2/5 share=73203793/244140625 share_float=0.299842736 bound=841.215670487
RESULT: PASS
```

Verdict: PASS.

## Residuals

- This verifies the fixed-fork exchangeable core, not the full private
  growing-floor frequency bridge.
- The single-case typicality residual `[TYP]` remains open by design.
- The exponential bound is loose at small `T`; exact finite counts are the main
  public content here.

## Reproduction

1. Start from a clean clone.
2. Run `python verification/scripts/frequency_bridge_exchangeable.py`.
3. Confirm the stable output ends in `RESULT: PASS`.
