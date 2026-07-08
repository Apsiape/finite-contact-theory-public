# Evidence Manifest

Status: public evidence posture.

The public repository is being curated from a larger private research
laboratory. This manifest states whether evidence is shipped here, cited from
the locked private corpus, historical only, or held.

## Evidence States

| state | meaning |
|---|---|
| `shipped` | Script/result ledger is included in this public repository and should run from a clean clone. |
| `cited` | Locked private source or result ledger is named as evidence, but not copied into the public release yet. |
| `historical` | Source is provenance or context, not public-load-bearing evidence. |
| `held` | Source is not used as public evidence until scope, rights, dependencies, or packaging are resolved. |

## First-Release Evidence Posture

The first public release now has a small shipped verification subset plus cited
private evidence. The shipped subset is intentionally narrow and
dependency-free. It does not replace the larger locked private research ledgers.

## Candidate Evidence Items

| claim area | current evidence state | private source examples | public action |
|---|---|---|---|
| No-totality/open fresh-mark rule | `shipped` + `cited` | Public `no_jam_open_rule.py`; The private research corpus, `blind_open_rule_RECORD.md` | Public script verifies the open-rule no-jam core; private evidence carries capped controls/blind. |
| Frequency bridge | `shipped` + `cited` | Public `frequency_bridge_exchangeable.py`; The private research corpus | Public script verifies exchangeable finite-counting core; private evidence carries growing-floor compensator and controls. |
| Born composition and witness decomposition | `shipped` + `cited` | Public `rational_born_gluing.py`; cited private research corpus | Public script verifies the exact pushforward-counting, exclusivity-lift, and witness-interchange uniqueness core; private evidence carries the gluing-consistency certificate. |
| Native carrier lift | `shipped` + `cited` | Public `native_lift_binary_bell.py`; cited private research corpus | Public script verifies exact core identities; private evidence carries full native-lift study. |
| CHSH/Pell boundary core | `shipped` + `cited` | Public `chsh_pell_boundary.py`; cited private research corpus | Public script verifies the exact Pell ladder, the `p^2-2q^2=-1` fence, and the CHSH readout; the theta-body / glue-depth certificate remains cited. |
| Sliwa-23/41 certificates | `cited` / `held` split | cited admissibility-calculus tensor-carrier notes; private Sliwa scripts | Cite only as imported recovery unless public artifacts are copied. |
| CHSH weights / magic bridge | `held` | cited private research corpus (tensor-carrier and frontier notes) | Keep frontier/model-scope; no public-load-bearing use yet. |
| Level-2 thermodynamics | `cited` | The private research corpus | Cite for aperture/temperature row; avoid gravity overclaim. |
| Observer lattice / sourcing | `held` / `historical` | `leak_lattice`, `powered_sourcing` results | Keep as frontier until re-registration/power issue is resolved. |

## Shipped Public Scripts

Run all shipped scripts:

```powershell
python verification\scripts\run_all.py
```

Run release hygiene:

```powershell
python scripts\release_audit.py
```

Current shipped scripts:

- `verification/scripts/no_jam_open_rule.py`
- `verification/scripts/frequency_bridge_exchangeable.py`
- `verification/scripts/rational_born_gluing.py`
- `verification/scripts/chsh_pell_boundary.py`
- `verification/scripts/native_lift_binary_bell.py`

Current shipped result ledgers:

- `verification/results/FCT-09-no-jam-open-rule-RESULTS.md`
- `verification/results/FCT-10-frequency-bridge-exchangeable-RESULTS.md`
- `verification/results/T-04-rational-born-gluing-RESULTS.md`
- `verification/results/FCT-16-chsh-pell-boundary-RESULTS.md`
- `verification/results/FCT-17-FCT-18-native-lift-binary-bell-RESULTS.md`
- `verification/results/run-all-RESULTS.md`
- `verification/results/release-audit-RESULTS.md`

## Packaging Rule

Before an evidence item becomes `shipped`, it needs:

- a public claim ID;
- an exact command;
- dependency and runtime notes;
- frozen registration and controls;
- a result ledger with residuals;
- no private paths, private imports, secrets, or untriaged output.
