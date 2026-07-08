# Finite Contact Theory

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21253591.svg)](https://doi.org/10.5281/zenodo.21253591)

> **Quantum mechanics, not assumed — grown.**
> From a finite floor of one-use marks, with no Hilbert space, no probability,
> and no continuum granted at the start, this program reconstructs the
> CHSH/Bell arena, the Born rule as counting, and the Tsirelson boundary — and
> generates the quantum carrier grammar itself — machine-verified at
> binary-Bell scope.

Most attempts to rebuild physics from something deeper ask you to take a lot on
faith. This one hands you a script. Run it and watch a fragment of quantum
mechanics fall out of pure finite counting, with the exact edge of the result
printed on the screen — then read the list of everything we killed to get here.

**This is v0.1 — _Growing the Bell/CHSH Quantum Boundary from a Finite One-Use
Floor_ — the first published chapter of a much larger reconstruction program.**
Everything past this chapter (spacetime, gravity, the continuum, and the general
quantum case) is held open by name in the horizon and roadmap below. The point of
a first chapter is that you can check it now.

![The reconstruction ladder: quantum structure grown from a finite one-use floor, each rung labeled by status and scope.](assets/reconstruction-ladder.svg)

## Run it yourself (about 30 seconds)

No dependencies beyond Python's standard library.

```powershell
python verification\scripts\run_all.py
```

Expected final line:

```text
ALL SHIPPED VERIFICATION: PASS
```

Along the way it runs five exact checks: the no-jam core clearing depth 7; the
rational Born weights matching their counting shares; the CHSH ladder climbing
to `2*sqrt(2)` with every rung on the exact Pell fence `p^2 - 2q^2 = -1`; and
the complementarity angle coming out as a pure fraction of shared witnesses,
`t(k,n) = k/n`, exactly. This reproduces the shipped public subset — not the
full private corpus.

## The one claim

The whole release ceiling is a single sentence, and it is quoted identically in
the paper, the claim register, and the release notes:

> Finite Contact Theory is a finite reconstruction program with a scoped
> theorem stack — from one-use contact to counting, to one-receiver gluing, to
> rational Born weights, to the CHSH/Pell boundary, to a carrier grammar grown
> from one-use contact — under which the quantum boundary is a floor theorem at
> **binary-Bell finite-carrier scope**, with every unearned generalization left
> open by name.

The scope fence is not an apology. It is the result. We tell you precisely how
far the proof reaches; that edge is the theorem. In particular this does **not**
claim that all quantum mechanics is derived — the general selector, `q >= 3`
carriers, cross-site interlocking, and every nature-facing prediction are held
open and named below.

## What we killed — and why that is the point

A theory of everything that never discards anything is not a theory; it is a
mood. This one keeps a public [correction ledger](docs/correction-ledger.md),
and the kill count is a feature, not an embarrassment. Claims that looked
beautiful and died on the evidence include:

- binary arity as uniquely forced by a matter–memory coincidence;
- matter fixed at dimension 2 across arities;
- closure dynamics reaching the Tsirelson value on its own;
- a simple time-arrow statistic as a nature-facing bet;
- graph-floor gravity as a generic divergence from general relativity;
- raw record capacity read as memory;
- the completed continuum as a native object.

Each was pursued hard, then retired under adversarial review. The positive
results in this repository are the ones that survived that discipline.

## The ladder — each rung earns its own label

```text
finite one-use contact                                      [ primitive ]
  -> witness fibers and trace classes                       [ definition ]
  -> coherent counting measure                              THEOREM
  -> one-receiver gluing                                    THEOREM
  -> rational Born weights = counting through gluing        THEOREM  (rational scope)
  -> CHSH / Pell boundary -> 2*sqrt(2)                      THEOREM + RECOVERY (rational scope)
  -> carrier grammar grown from one-use contact, t = k/n    THEOREM  (binary-Bell scope)
  -> the quantum boundary is a floor theorem                (binary-Bell finite-carrier scope)
```

**The counting, Born, CHSH/Pell, and native-carrier rungs each ship an exact
check** — five scripts in all, counting no-totality — so the chain above is not
a promise, it is runnable. Every label and scope is defended in the
[theorem bank](docs/theorem-bank.md) and controlled by the
[public claim register](docs/public-claim-register.md). Nothing is banked on a
single implementation: the no-jam core, for one, was reproduced by an
independent repo-barred replicator before it earned its label.

## The horizon — bold, and not yet proven

These are the possibilities the program is built to attack. They are the
*horizon*, explicitly not results, and each will only enter the theory if it
becomes a scoped theorem, a recovery, a model result, or a clean failure:

- **Quantum structure as a reception theorem** — begun at binary-Bell scope; the general case open.
- **Spacetime as contact bookkeeping** — geometry as what stable coarse reception looks like.
- **Gravity as aperture thermodynamics** — energy and temperature appearing at visible-sector boundaries, not at the floor.
- **The continuum as an admitted completion** — real numbers and Hilbert hosts as overlays whose finite content is reconstructed horizon by horizon.
- **Observers as reception classes** — a bounded pattern of what can be jointly received, not a primitive subject.
- **Constants as biography** — dimensionful constants belonging to a branch's received history, not the forced grammar.

## Read it

1. [papers/finite-contact-theory-v0.1.md](papers/finite-contact-theory-v0.1.md) — the release narrative.
2. [docs/mathematical-core.md](docs/mathematical-core.md) — the formal vocabulary.
3. [docs/theorem-bank.md](docs/theorem-bank.md) — theorem rows and proof sketches.
4. [docs/public-claim-register.md](docs/public-claim-register.md) — every public claim, labeled and scoped.
5. [verification/evidence-manifest.md](verification/evidence-manifest.md) — what evidence is shipped, cited, historical, or held.
6. [docs/finite-contact-theory.md](docs/finite-contact-theory.md) — the extraction plan for the full theory spine: where this chapter sits in the larger program.

Short on time? Start with [docs/how-to-read.md](docs/how-to-read.md), and keep
[docs/glossary.md](docs/glossary.md) open for terms. Where the whole program is
going, and what remains open, is in
[docs/release-roadmap.md](docs/release-roadmap.md).

## Verify and audit

```powershell
python verification\scripts\run_all.py   # the shipped theorem subset
python scripts\release_audit.py          # release hygiene: scope, links, no overclaims
```

The audit refuses stale scope language, private paths, and un-scoped overclaim
phrases. The release is designed to feel powerful because it is exact, not
because it says too much.

## Status

This is v0.1.0: a complete, scoped chapter with its theorem stack, claim
register, and shipped verification in place. The general quantum selector,
cross-site interlocking, `q >= 3`, and nature-facing claims are deliberately
held or open, and named as such — this is a first chapter, not a finished
program.

## Author

- Seth Douglas
- Email: apsiape@gmail.com
- ORCID: https://orcid.org/0009-0007-4708-3252
- GitHub: https://github.com/Apsiape

## Citation

Archived and citable via Zenodo. Please cite as:

> Douglas, S. (2026). *Finite Contact Theory v0.1: Growing the Bell/CHSH
> Quantum Boundary from a Finite One-Use Floor* (v0.1.0). Zenodo.
> https://doi.org/10.5281/zenodo.21253592

- **Concept DOI** (always the latest version): [10.5281/zenodo.21253591](https://doi.org/10.5281/zenodo.21253591)
- **Version DOI** (v0.1.0 specifically): [10.5281/zenodo.21253592](https://doi.org/10.5281/zenodo.21253592)

Machine-readable metadata is in [CITATION.cff](CITATION.cff).

## Rights

This work is licensed under [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)](https://creativecommons.org/licenses/by-nc-nd/4.0/).
You may share it with attribution; you may not use it commercially or
distribute modified versions. For anything beyond that — commercial use or
derivative works — contact the author. See [LICENSE.md](LICENSE.md).

## A note from the author

A bit of honesty about where this comes from. I'm not a physicist. I work in AI
and software, and I follow physics as an outsider. I read and watch a lot, so I
have a decent feel for the open questions, but I don't have the formal training.

It didn't start as a theory of physics anyway. It started with one question I
couldn't put down: what is the least that has to exist when something finite
touches something it can't fully take in? A finite thing makes contact with
something larger than itself. The contact is real but partial, so it leaves a
difference. And once that difference is there, it can't just be wiped away. The
finite thing becomes, in a sense, answerable for it.

I kept pulling on that thread. Not starting from physics, or consciousness, or
big systems, but from that one small event: finite contact with what exceeds
it. For a while I thought of it as finite answerability, the idea that a finite
thing is only being honest if it never pretends it isn't finite. It slowly
turned into what's here: finite contact theory.

I'm not a mathematician either, so the way I chased it is unusual. Over the last
seven months or so I built a setup where several AI models work together as a
research team, and pointed it at that question. It took around 15 private repos
and a lot of dead ends. The hardest part was never the physics. It was getting
the models to reach for something new instead of repeating what they were
trained on.

This is the first small piece of what came out of it, with more built out
privately that I'll share as it's ready. I know an AI-assisted theory from
someone outside the field is easy to doubt. That's fair, and it's exactly why
everything here is scoped, labeled, and runnable. If I've gotten something
wrong, I want to know. And if you'd like to talk or work on this together, I'm
at apsiape@gmail.com.
