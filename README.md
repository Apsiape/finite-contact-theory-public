# Preface

Hello — my name is Seth. I am a professional AI researcher/architect and
software engineer, and an unapologetic armchair theoretical physicist: I spend a
lot of time down YouTube rabbit holes trying to keep up with where the field is
going. For a long time I have been convinced we are missing something
fundamental.

So over the past seven-plus months I built something to go looking for it: a
multi-model, multi-agent AI research lab. The premise was simple — assume
classical math and physics are incomplete, go all the way down to the very
bottom of things, and build back up from there. Behind this release sit around
15 private repositories, hundreds of thousands of lines of code, and a great
many dead ends.

The hard part was never the physics. It was getting language models to genuinely
think outside the box of their own training data — to be creative, and to build
something new rather than re-describe what is already known. I have re-engineered
the agent loops, the workflow, and the research architecture five times over to
get there. I think I finally have something worth sharing.

I eventually found the "floor" I wanted to build from. What follows is only the
first, smallest piece of it — the theory is built out much further in private,
and I will be sharing the rest soon.

If you would like to collaborate, or to help support the work (the tokens are
not cheap), I would genuinely love to hear from you: apsiape@gmail.com.

---

# Finite Contact Theory

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

Citation metadata is in [CITATION.cff](CITATION.cff). The preferred citation
will be finalized at the first tagged DOI release.

## Rights

This work is licensed under [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)](https://creativecommons.org/licenses/by-nc-nd/4.0/).
You may share it with attribution; you may not use it commercially or
distribute modified versions. For anything beyond that — commercial use or
derivative works — contact the author. See [LICENSE.md](LICENSE.md).
