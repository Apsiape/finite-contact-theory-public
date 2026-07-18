# Chapter 34 — The Strata and the Blindness

*Finite Contact Theory, v0.24. Closes the two named gaps of Chapter 33: the
pin lemma's general proof, and the misaligned sector's missing theory. Every
result below ships as a dependency-free exact script; frozen predictions are
scored in print, including the one that died.*

## What this chapter does

Chapter 33 proved the cap theorem — aligned solo channels never exceed
correlation distance two — at verified scope, with the pin lemma's general
proof a named gap, and left the misaligned sector (channels whose paths carry
different hidden-bit key-sets) uncharted. This chapter closes both, and the
closure produced one killed hypothesis and two laws stronger than the ones we
bet on.

## 1. The pin lemma, closed — and the hypothesis that died

The cap proof was decomposed into three machine-checkable lemmas and run
exhaustively over the census (C6 bodies at depths 3–4, K6−e, the W7a family;
1524 aligned channels):

- **Lemma A (position autonomy) — holds.** In an aligned channel, every
  hidden line's spot at every time is determined by its own bit prefix alone.
  A cross-line position dependence would change singles-membership per branch
  — which is misalignment.
- **Lemma B (two-spot oscillation) — KILLED, generically.** We froze the bet
  that each line occupies at most two spots. It fails on 1148 of 1524
  channels: **aligned wandering** is the norm — lines roam three or more
  spots without breaking alignment, because the extra spots are
  protocol-inert. Scored as a miss and kept in print.
- **Lemma C (interval duals) — holds.** Every per-line conservation law is a
  contiguous stretch of that line's own firing chronology.

The close: A + C alone carry the cap and dual autobiography. The theorem got
**stronger by losing a hypothesis** — the distance-2 cap and the per-line
direct-sum structure now stand as full theorems at censused solo-aligned
scope, with no appeal to spot confinement.

## 2. The stratification theorem

Every misaligned channel in the census (1896 channels) partitions by
bit-key-set into **aligned strata, each with affine support**; the channel
amplitude is the exact weighted sum of its stratum amplitudes. There is no
third kind of channel: the amplitude calculus is one calculus, stratified.
Within every equal-weight stratum, the Chapter-33 dual-sum code reading law
holds verbatim. (The strata decomposition is the model's exact instance of a
decoherent-histories branch decomposition; the consistency framework of
Griffiths, Omnès, and Gell-Mann–Hartle is the cited frame, as in Chapters
31–32.)

## 3. The operational blindness law

We froze a hunting bet — the *evasion*: a bright misaligned channel that
survives a single bit reveal (every conditioned branch keeping at least two
paths at coherence one), which would have been a loophole in the cap's
observational consequences. The hunt returned empty: **all twelve bright
misaligned channels die to one reveal.** Branching buys no loophole; the
persistence limit belongs to the floor's records themselves, not to
alignment. (Chapter 37 returns to this law with a different instrument and
finds its scope — the blindness is real and instrument-indexed.)

## 4. Darkness needs alignment

The misaligned spectrum is 1884 partial, 12 bright, **0 dark**: no misaligned
channel is ever exactly precluded. Exact preclusion — amplitude zero at
positive probability, Sorkin's term, cited as in Chapter 32 — is an aligned
phenomenon; strata never conspire to full cancellation at censused scope.

## 5. Composition, cleared

The modulus reading composes multiplicatively across interleaved independent
sectors (512 interleaved sequences, exact): joint amplitudes factorize, so
the composition critique that targets real-part readings (Diósi's objection
to linear-positivity-style measures) does not bite the squared reading here.
Among the actuality candidates of Chapter 35, composition does not
discriminate — the Sorkin grade does.

## Scope and honesty

All results are exact and exhaustive at their stated census scopes (C6
bodies, K6−e, W7a; depths 3–4). The general-n statements remain open by
name. The killed Lemma B is retained in print as the round's health metric:
the census beat our structural bet, and the surviving proof is leaner than
the one we designed.

## Verification

`verification/scripts/pin_lemma.py`, `verification/scripts/stratified_sector.py`,
and `verification/scripts/coat_composition.py` — exact rational arithmetic,
no dependencies beyond the standard library.
