# Release Notes — v0.8.0

**Finite Contact Theory v0.8: The Non-Exact-Return Reconstruction — Finite
Born Valuation and Contextuality from a Retained Contact Interface.**

Eighth public release. It opens a third line of the program — a
contact-interface reconstruction — and follows it to a single finite
object on which Born valuation and Kochen-Specker contextuality turn out
to be two faces of one closure. Every load-bearing statement is exact and
machine-checked from a clean clone.

## The new live release ceiling

> Finite Contact Theory is a finite reconstruction program with a scoped
> theorem stack on three published lines — a quantum-facing axis, from
> one-use contact to counting, one-receiver gluing, rational Born weights,
> the CHSH/Pell boundary, a carrier grammar grown from one-use contact, and
> a behavior-conditioned contextual capacity with an exact strict
> preparation gap; a finite-epistemics axis, from the identifiability and
> debt calculus to the inquiry calculus and its second law of asking, four
> theorems separating the structure of time, and a measured generative
> floor; and a contact-interface reconstruction, in which a retained
> interface forces a quaternionic state/receiver cell whose self-dual
> closure is the 24-cell and the F_4 root system and whose finite
> measurement calculus forces the quadratic Born frame rule (a finite
> Gleason theorem) exactly where a global noncontextual assignment is
> impossible (a triality Kochen-Specker obstruction) — under which the
> quantum boundary is a floor theorem at binary-Bell finite-carrier scope,
> the preparation gap is an exact theorem at KCBS-pentagon scope, the
> interface reconstruction is a finite model-scope recovery on a
> real-quantum cell, and every unearned generalization — complex quantum
> mechanics, the actuality of one outcome, the universal Born rule, and
> every nature-facing prediction — is left open by name.

This supersedes the v0.7 ceiling as the live ceiling; the v0.1, v0.2, and
v0.7 ceilings remain quoted, unchanged, in their frozen chapters and
release notes.

## What is new

- **Chapter 8**:
  [papers/08-nonexact-return/](papers/08-nonexact-return/paper.md) — the
  non-exact-return reconstruction. Six shipped claim rows
  (**FCT-45 through FCT-50**) and four theorem rows (**T-33 through
  T-36**), all `shipped` and verified by one dependency-free script:
  - **FCT-45** — the primitive receiver is the quaternions `H` (minimal
    real dimension four, irreducible, unique invariant positive form,
    forced 1+3 split);
  - **FCT-46** — the unit states are the 24-cell and its polar dual is
    again a 24-cell (a self-hosting state/receiver fixed point), by
    exhaustive polar enumeration;
  - **FCT-47** — the 48 combined vectors are the `F_4` root system
    (Weyl order 1152);
  - **FCT-48** — every state/receiver contact has the forced scale-free
    overlap ratio `1/2`;
  - **FCT-49** — a finite Gleason theorem: the 24-ray context family
    forces the quadratic Born frame rule `f(x)=tr(rho P_x)`, with no
    continuum and no continuity;
  - **FCT-50** — a triality Kochen-Specker obstruction: no global
    noncontextual assignment exists (exactly sixteen minimal nine-context
    parity proofs, all in the state/receiver interface); Born valuation
    and contextuality are the two faces of one finite closure — the
    valuation is uniquely lawful exactly where a global pointing is
    impossible.
- **New shipped verification**:
  `verification/scripts/nonexact_return_reconstruction.py` (also frozen
  under the chapter). Dependency-free, exact, exhaustive; runs in a few
  seconds and is wired into `run_all.py` (now eleven scripts).
- **README overhauled** to the three-line stack; the claim register's
  Release Ceiling section and the theorem bank are updated; the audit
  script carries the new required files, the migrated canonical ceilings,
  and additional overclaim bans.

## Scope and honesty

The chapter's objects — the Hurwitz units and 24-cell, the `F_4` root
system, Gleason's theorem in finite real form, and the Peres 24-ray
Kochen-Specker set with its Kernaghan-type parity proofs — are known
mathematics, **recovered here in a derivational role** and named as such.
The novelty claim is the composition and the two-faces reading, graded in
the register. Scope is a real-quantum cell (`Sym(4,R)`): complex quantum
mechanics, the actuality of one outcome, the universal Born rule, and
every nature-facing prediction are held open by name.

## Verify

```powershell
python verification\scripts\run_all.py    # expects: ALL SHIPPED VERIFICATION: PASS
python scripts\release_audit.py           # expects: PUBLIC RELEASE AUDIT: PASS
```

## Citation

Cite the program by its concept DOI
[10.5281/zenodo.21253591](https://doi.org/10.5281/zenodo.21253591); the
v0.8.0 version DOI is
[10.5281/zenodo.21360609](https://doi.org/10.5281/zenodo.21360609).
