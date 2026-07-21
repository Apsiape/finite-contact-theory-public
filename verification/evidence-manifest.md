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

## Evidence Posture

The public repository now spans fifty-two chapters (this manifest details the
early chapters; from Chapter 34 onward verification scripts live in
verification/scripts/ and are indexed by run_all.py). Early scope: three recovery lines, a
first extension line, a count-regions line, and a floor-to-interface line,
with eighteen shipped, dependency-free verification scripts alongside cited
private evidence. The shipped subset is intentionally
self-contained and exact where it can be; it does not replace the larger locked
private research ledgers.

## Candidate Evidence Items

| claim area | current evidence state | private source examples | public action |
|---|---|---|---|
| Floor-to-interface forcing chain (FCT-68..71) | `shipped` + `cited` | Public `floor_to_interface.py`; the private corpus for the retention laws and the door verdict | Public script proves the pincer, Cl(3,0)/i/1/2, the double-cover selection, and the H minimality in exact arithmetic; the received inputs (readability, arity measurement, self-hosting, orientation) are named, with readability's not-forced status cited from the private corpus. |
| Mixed-state exclusion + count regions (FCT-62..67) | `shipped` | Public `mixed_state_exclusion.py`, `count_regions.py` | Exact public verifiers; frozen copies in the chapter directories. |
| No-totality/open fresh-mark rule | `shipped` + `cited` | Public `no_jam_open_rule.py`; The private research corpus, `blind_open_rule_RECORD.md` | Public script verifies the open-rule no-jam core; private evidence carries capped controls/blind. |
| Frequency bridge | `shipped` + `cited` | Public `frequency_bridge_exchangeable.py`; The private research corpus | Public script verifies exchangeable finite-counting core; private evidence carries growing-floor compensator and controls. |
| Born composition and witness decomposition | `shipped` + `cited` | Public `rational_born_gluing.py`; cited private research corpus | Public script verifies the exact pushforward-counting, exclusivity-lift, and witness-interchange uniqueness core; private evidence carries the gluing-consistency certificate. |
| Native carrier lift | `shipped` + `cited` | Public `native_lift_binary_bell.py`; cited private research corpus | Public script verifies exact core identities; private evidence carries full native-lift study. |
| CHSH/Pell boundary core | `shipped` + `cited` | Public `chsh_pell_boundary.py`; cited private research corpus | Public script verifies the exact Pell ladder, the `p^2-2q^2=-1` fence, and the CHSH readout; the theta-body / glue-depth certificate remains cited. |
| Behavior-conditioned capacity / preparation gap (chapter 2) | `shipped` + `cited` | Public `exact_gap_certificate.py`; cited private SDP, compression, phase-geometry, rigidity-bridge, and dual suites | Public script proves the exact strict-gap certificate end to end (FCT-22); the SDP magnitudes, geometry scans, headroom checks, and dual numerics remain cited (FCT-21/23/24/25). |
| Identifiability and debt calculus (chapter 3) | `shipped` + `cited` | Public `identifiability_debt_calculus.py`; cited private arrival ledgers (retention, merges, gluing, law-provenance, interaction receipts) | Public script proves the waist, debt, continuation, and depth theorems at finite-model scope (FCT-26..29); the eight program-facing arrivals of the debt formula remain cited. |
| Inquiry calculus (chapter 4) | `shipped` + `cited` | Public `inquiry_calculus.py`; cited private asking-algebra and update-calculus ledgers | Public script proves the residual algebra, the exact EC = H + KL + O decomposition, the adaptivity interest, and the typing witnesses (FCT-30..33); the program-facing noncommutative-asking readings remain cited. |
| Becoming webs / time structure (chapter 5) | `shipped` + `cited` | Public `becoming_webs.py`; cited private becoming-web, law-hysteresis, and chronofiber ledgers | Public script proves the torsor, helix, ledger-arrow, and no-foundation theorems at finite-model scope (FCT-34..37); the floor-native measurements and readings remain cited. |
| Measured floor phenomena (chapter 6) | `shipped` + `cited` | Public `floor_engine_measurements.py` (engine + suite); cited private twin-wait census, counterfactual-perturbation campaign, redundancy-inversion result | Public engine measures s-hat = 0.927, the short-tailed wait law, and the ballistic defect (FCT-38..41); the inversion and radius instruments remain cited with their scale fences stated. |
| Contact-interface reconstruction (chapter 8) | `shipped` + `cited` | Public `nonexact_return_reconstruction.py`; cited private NXR corpus | Public script verifies the quaternionic receiver, the 24-cell self-dual fixed point, the F_4 closure, the forced `1/2`, the finite Gleason theorem, and the triality Kochen-Specker obstruction (FCT-45..50); the full reconstruction study remains cited. |
| Multi-floor worldweave / forcing audit (chapter 9) | `shipped` + `cited` | Public `multifloor_worldweave.py`, `forcing_audit.py`, `wcd_actualization.py`; cited private MFW/ESFA/ESL/WCD corpus | Public scripts verify the `E_8`-hexacode closure atlas (FCT-51..56), the static/dynamic forcing audit (FCT-57/58), and actualization-by-counting where counting forces the FORM but not Born (FCT-59); the full audits remain cited. |
| Negative-Gram identity holonomy (chapter 10) | `shipped` | Public `negative_gram_holonomy.py` | Public script PROVES the universal accessible-positivity theorem `152N + 9\|per\|^2 - 36\|det\|^2 >= 0` for every complex `3x3` matrix (FCT-60 / T-44), verified exactly on rational toric witnesses plus an independent adversarial descent, with the `U(3)` strict `(7/2)`-margin corollary and the `-495` kill of the `(7/2)`-universal; and carries the exact conditional negative-Gram prediction (FCT-61). The empirical mixed-state PSD-exclusion is the open crux (external quantum-optics expert). |
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

Current shipped scripts (sixty-five, wired into `run_all.py`, one per shipped result line):

- `verification/scripts/no_jam_open_rule.py`
- `verification/scripts/frequency_bridge_exchangeable.py`
- `verification/scripts/rational_born_gluing.py`
- `verification/scripts/chsh_pell_boundary.py`
- `verification/scripts/native_lift_binary_bell.py`
- `verification/scripts/exact_gap_certificate.py`
- `verification/scripts/identifiability_debt_calculus.py`
- `verification/scripts/inquiry_calculus.py`
- `verification/scripts/becoming_webs.py`
- `verification/scripts/floor_engine_measurements.py`
- `verification/scripts/nonexact_return_reconstruction.py` (chapter 8)
- `verification/scripts/multifloor_worldweave.py` (chapter 9)
- `verification/scripts/forcing_audit.py` (chapter 9)
- `verification/scripts/wcd_actualization.py` (chapter 9)
- `verification/scripts/negative_gram_holonomy.py` (chapter 10)
- `verification/scripts/mixed_state_exclusion.py` (chapter 11)
- `verification/scripts/count_regions.py` (chapter 12)
- `verification/scripts/floor_to_interface.py` (chapter 13)
- `verification/scripts/atlas_of_floors.py` (chapter 14)
- `verification/scripts/ladder_of_scars.py` (chapter 15)
- `verification/scripts/debt_ledger.py` (chapter 16)
- `verification/scripts/mint_and_bill.py` (chapter 17)
- `verification/scripts/emergent_hierarchy.py` (chapter 18)
- `verification/scripts/seventh_attempt.py` (chapter 19)
- `verification/scripts/observers_price.py` (chapter 20)
- `verification/scripts/genesis_of_space.py` (chapter 21)
- `verification/scripts/price_of_chance.py` (chapter 22)
- `verification/scripts/decay_of_worlds.py` (chapter 23)
- `verification/scripts/particles_of_floor.py` (chapter 24)
- `verification/scripts/the_up.py` (chapter 25)
- `verification/scripts/habitability.py` (chapter 26)
- `verification/scripts/floor_thermodynamics.py` (chapter 27)
- `verification/scripts/maintained_structures.py` (chapter 28)
- `verification/scripts/two_kinds_of_the_given.py` (chapter 29)
- `verification/scripts/where_i_lives.py` (chapter 30)
- `verification/scripts/the_reading_law.py` (chapter 31)
- `verification/scripts/the_coat_and_the_count.py` (chapter 32)
- `verification/scripts/the_codes_of_the_coat.py` (chapter 33)
- `verification/scripts/pin_lemma.py` (chapter 34)
- `verification/scripts/stratified_sector.py` (chapter 34)
- `verification/scripts/coat_composition.py` (chapter 34)
- `verification/scripts/actuality_protocol.py` (chapter 35)
- `verification/scripts/alien_coat.py` (chapter 36)
- `verification/scripts/alien_reading.py` (chapter 36)
- `verification/scripts/permission_map.py` (chapter 37)
- `verification/scripts/grammar_closure.py` (chapter 38)
- `verification/scripts/sequence_grammar.py` (chapter 38)
- `verification/scripts/mortal_observer.py` (chapter 39)
- `verification/scripts/breathing_floor.py` (chapter 40)
- `verification/scripts/two_switches.py` (chapter 40)
- `verification/scripts/fourth_column.py` (chapter 41)
- `verification/scripts/controls_engine.py` (chapter 41)
- `verification/scripts/phase_hunt.py` (chapter 42)
- `verification/scripts/fourth_table.py` (chapter 42)
- `verification/scripts/critical_corner.py` (chapter 43)
- `verification/scripts/minimal_pair.py` (chapter 43)
- `verification/scripts/observer_corner.py` (chapter 44)
- `verification/scripts/quantum_dividend.py` (chapter 45)
- `verification/scripts/third_root.py` (chapter 46)
- `verification/scripts/sixfold_coat.py` (chapter 47)
- `verification/scripts/harmonic_law.py` (chapter 48)
- `verification/scripts/octave_law.py` (chapter 48)
- `verification/scripts/rf_boundary.py` (chapter 49)
- `verification/scripts/causal_ceiling_family.py` (chapter 51)
- `verification/scripts/amalgamation_boundary.py` (chapter 52)

Current shipped result ledgers:

- `verification/results/FCT-09-no-jam-open-rule-RESULTS.md`
- `verification/results/FCT-10-frequency-bridge-exchangeable-RESULTS.md`
- `verification/results/T-04-rational-born-gluing-RESULTS.md`
- `verification/results/FCT-16-chsh-pell-boundary-RESULTS.md`
- `verification/results/FCT-17-FCT-18-native-lift-binary-bell-RESULTS.md`
- `verification/results/FCT-22-exact-gap-certificate-RESULTS.md`
- `verification/results/FCT-26-FCT-29-identifiability-debt-calculus-RESULTS.md`
- `verification/results/FCT-30-FCT-33-inquiry-calculus-RESULTS.md`
- `verification/results/FCT-34-FCT-37-becoming-webs-RESULTS.md`
- `verification/results/FCT-38-FCT-41-measured-floor-RESULTS.md`
- `verification/results/run-all-RESULTS.md`
- `verification/results/release-audit-RESULTS.md`

Chapters 8-10 ship their expected output as frozen `EXPECTED-OUTPUT*.md` files
under each chapter's `papers/<NN>-*/verification/` directory rather than as
separate result ledgers.

## Packaging Rule

Before an evidence item becomes `shipped`, it needs:

- a public claim ID;
- an exact command;
- dependency and runtime notes;
- frozen registration and controls;
- a result ledger with residuals;
- no private paths, private imports, secrets, or untriaged output.
