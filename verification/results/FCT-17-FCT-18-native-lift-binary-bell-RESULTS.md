# Native Lift Binary-Bell Core - RESULTS

Claim IDs: FCT-17, FCT-18 / T-06, T-07  
Status: PASS  
Script: `verification/scripts/native_lift_binary_bell.py`  
Command: `python verification/scripts/native_lift_binary_bell.py`  
Date run: 2026-07-07  
Environment: Windows, Python 3.13.12  
Dependencies: Python standard library only  
Expected runtime: under 10 seconds  
Observed runtime: under 1 second as part of `run_all.py`

## Frozen Registration

- Claim under test: small exact identities in the binary-Bell native carrier
  lift.
- Inputs and parameters: binary fork projectors; witness-overlap families
  `n=4,6`; site-disjoint product check with overlaps `1/4` and `2/6`.
- Success gate:
  - binary fork projectors produce a signed involution;
  - `t(k,n)=k/n` exactly for all tested `k`;
  - site-disjoint witness products factor exactly.
- Failure gate: any exact identity fails.
- Controls: this public script is a dependency-free core identity check. The
  private native-lift work includes larger scope, positivity, and
  imported Sliwa certificate context.
- Exploratory-only outputs: none.

## Results

Stable output:

```text
native_lift_binary_bell
involution_check=PASS
t_values_n4=['0', '1/4', '1/2', '3/4', '1']
t_values_n6=['0', '1/6', '1/3', '1/2', '2/3', '5/6', '1']
omega_a=1/4 omega_b=1/3 omega_ab=1/12
RESULT: PASS
```

Verdict: PASS.

## Residuals

- This is not the private native-lift work.
- It does not ship the Sliwa certificates.
- It does not ship the positivity/temperature measurement.
- Scope remains binary-Bell / finite carrier; q >= 3, more outcomes, and
  cross-site interlocking remain open.

## Reproduction

1. Start from a clean clone.
2. Run `python verification/scripts/native_lift_binary_bell.py`.
3. Confirm the stable output ends in `RESULT: PASS`.
