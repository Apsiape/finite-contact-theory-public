# Release Notes — v0.9.0

**Finite Contact Theory v0.9: The Multi-Floor Worldweave — A Forcing Audit of the E_8-Hexacode Spine.**

Ninth public release. It extends the contact-interface line (opened in v0.8)
from a single cell to a population, and answers the structural question left
open by name in Chapter 8: how independently generated cells become one
world. The answer is that they do not combine by tensor product — they settle
their triality boundary debts into a self-dual code.

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
> Gleason theorem) exactly where a triality Kochen-Specker obstruction
> forbids a global noncontextual assignment, and in which independently
> generated cells recover the E_8–hexacode closure spine under named
> positive, integral, triality-covariant, self-dual, and delocalizing
> receiver laws while a forcing audit proves those laws are not selected by
> the floor over matched lawful alternatives — so the floor forces the atlas
> of lawful closures and the terminal self-dual class but never the specific
> member, and the selection of a world-phase is a conserved, received input
> — under which the quantum boundary is a floor theorem at binary-Bell
> finite-carrier scope, the preparation gap is an exact theorem at
> KCBS-pentagon scope, the interface reconstruction is a finite model-scope
> recovery on a real-quantum cell, the multi-floor closures are model-scope
> recoveries whose forcing boundary is exactly mapped, and every unearned
> generalization — complex quantum mechanics, the actuality of one outcome,
> the universal Born rule, whether nature realizes any of these structures,
> which world-phase is selected, and every nature-facing prediction — is
> left open by name.

This supersedes the v0.8 ceiling as the live ceiling; the v0.1, v0.2, v0.7,
and v0.8 ceilings remain quoted, unchanged, in their frozen chapters and
release notes.

## What is new

- **Chapter 9**:
  [papers/09-multifloor-worldweave/](papers/09-multifloor-worldweave/paper.md)
  — the multi-floor worldweave. Six shipped claim rows (**FCT-51 through
  FCT-56**) and four theorem rows (**T-37 through T-40**), all `shipped` and
  verified by one dependency-free script:
  - **FCT-51** — each cell's `D_4` triality boundary `K = C_2 x C_2` and the
    self-dual bridge-code model of multi-cell binding;
  - **FCT-52** — `E_8` as the unique debt-free two-cell closure
    (`240 = 48 + 3x64`, determinant ladder `16 -> 4 -> 1`);
  - **FCT-53** — octonionic local fusion (the `7/28` associator census: a
    pure three-contact receipt);
  - **FCT-54** — normed monolithic fusion stops at the octonions (sedenion
    zero divisors; none in `O`);
  - **FCT-55** — the self-dual code census is `|GU(N/2, 2)|` (3, 18, 648);
  - **FCT-56** — six cells are the first hidden world (the hexacode
    `[6,3,4]`, weight enumerator `1 + 45 y^4 + 18 y^6`; distance split
    `162 / 486` over all 648 codes).
- **New shipped verification**:
  `verification/scripts/multifloor_worldweave.py` (also frozen under the
  chapter). Dependency-free, exact, exhaustive (including the full `4^9`
  self-dual census); runs in a few seconds and is wired into `run_all.py`
  (now twelve scripts).
- **README, claim register, theorem bank, and audit** updated to the v0.9
  state (nine chapters; the migrated live ceiling; new required files and
  overclaim bans).

## Scope and honesty

The chapter's objects — the `D_4` triality group, the `E_8` root system, the
octonions and the Cayley-Dickson tower, the hexacode, and the unitary groups
`GU(k, 2)` — are known mathematics, **recovered here in a derivational role**
and named as such. The result is **structural**, under explicit closure
assumptions (positivity, integral receipt-preserving closure, triality
covariance, self-dual completion). It does **not** show that nature realizes
`E_8`, the hexacode, or any code, and derives no metric, spectrum, or
dimensionful constant. What is closed is the structural question: the native
global object is an evolving bridge code, not a tensor product or one
monolithic state space.

## Verify

```powershell
python verification\scripts
un_all.py    # expects: ALL SHIPPED VERIFICATION: PASS
python scripts
elease_audit.py           # expects: PUBLIC RELEASE AUDIT: PASS
```

## Citation

Cite the program by its concept DOI
[10.5281/zenodo.21253591](https://doi.org/10.5281/zenodo.21253591); the
v0.9.0 version DOI is recorded in
[papers/09-multifloor-worldweave/RELEASE.md](papers/09-multifloor-worldweave/RELEASE.md)
and [CITATION.cff](CITATION.cff) at mint.
