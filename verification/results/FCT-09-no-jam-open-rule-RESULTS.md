# No-Jam Open Rule - RESULTS

Claim ID: FCT-09 / T-01  
Status: PASS  
Script: `verification/scripts/no_jam_open_rule.py`  
Command: `python verification/scripts/no_jam_open_rule.py`  
Date run: 2026-07-07  
Environment: Windows, Python 3.13.12  
Dependencies: Python standard library only  
Expected runtime: under 10 seconds  
Observed runtime: under 1 second as part of `run_all.py`

## Frozen Registration

- Claim under test: under the open fresh-mark rule with act-indexed one-use,
  every reachable fragment through depth 7 has at least one legal extension.
- Inputs and parameters: exact BFS from the empty fragment; depth `7`.
- Enumeration rule: labeled fragments `(n, edges, records)`.
- Success gate: zero jammed reachable fragments.
- Failure gate: any reachable fragment with no legal successor.
- Controls: this public script is a core positive verification only; capped-rule
  controls remain cited from the private research corpus.
- Exploratory-only outputs: none.

## Results

Stable output:

```text
no_jam_open_rule
depth=7
reachable_states=1725
states_by_depth=[1, 1, 1, 2, 7, 34, 204, 1475]
jammed_states=0
RESULT: PASS
```

Verdict: PASS.

## Residuals

- This is a public subset of the private no-jam work, not the rest of the private research corpus.
- the private research corpus also catalogs capped-rule jams and blind replication.
- The theorem remains conditional on the open fresh-mark rule; it does not
  decide which admission rule nature runs.

## Reproduction

1. Start from a clean clone.
2. Run `python verification/scripts/no_jam_open_rule.py`.
3. Confirm the stable output ends in `RESULT: PASS`.
