# Related Work: Partial Distinguishability in Linear Optics (Chapters 10–12)

Status: prior-art companion note for the extension and count-region lines
(Chapters 10, 11, 12). Added at v0.13.0. Tied to claim rows FCT-60..FCT-67
and theorem rows T-44..T-50.

## Why this note exists

Chapter 2 ships a formal **novelty posture** (§4 of its paper): a
repository-barred, four-lens blind literature sweep with published query
strings, an `INTERNAL-BLIND` evidence grade, and named nearest precedents.
That protocol is the program's honest substitute for external refereeing.

It was **not rerun** when the work pivoted, at Chapter 10, into a literature
the earlier chapters never touched: multiphoton interference with partial
distinguishability, permanents/immanants, and real-versus-complex quantum
mechanics. Chapters 10–12 build directly on that subfield's standard
formalism — coincidence probabilities as permanents/immanants weighted by a
Gram matrix of internal states — but shipped without a related-work section
naming it. An independent read of the public repository flagged the gap.

This note closes it: it applies the Chapter-2 novelty protocol
retroactively, records the prior art Chapters 10–12 rest on, and separates
what is **recovery** (standard results, cited here as such) from the
**surviving residue** (the parts a blind sweep did not match verbatim, which
must be framed as sharpenings of known material, not discoveries). The
correction is logged as **C-18** in the [correction ledger](correction-ledger.md).
It does not change any theorem or any released ceiling; it changes what is
cited and how the novelty of Chapters 10–12 is graded.

**Evidence class: INTERNAL-BLIND.** The sweep below was run as a
repository-barred blind literature search from a self-contained
mathematical specification of the four results, with no framework language.
It is below an external quantum-optics referee's check — which the open
crux of Chapters 10–11 still explicitly awaits — and far above the
unstated-novelty posture the chapters shipped with.

## The must-cite list

Any competent referee in photonic quantum information would require these.
Chapters 10–12 are hereby positioned against them; future chapters in this
line cite them directly.

**Partial-distinguishability formalism (the frame Chapters 10–12 use):**

1. S. Aaronson & A. Arkhipov, *The computational complexity of linear
   optics*, Theory of Computing 9, 143 (2013) [STOC 2011] — boson sampling.
2. C. K. Hong, Z. Y. Ou, L. Mandel, Phys. Rev. Lett. 59, 2044 (1987) — the
   n=2 two-photon interference that the whole line generalizes.
3. M. C. Tichy, *Sampling of partially distinguishable bosons and the
   relation to the multidimensional permanent*, Phys. Rev. A 91, 022316
   (2015) — probabilities as a matrix of Gram matrices / multidimensional
   permanent.
4. V. S. Shchesnovich, *Partial indistinguishability theory for multiphoton
   experiments in multiport devices*, Phys. Rev. A 91, 013844 (2015) — the
   independent twin of Tichy.
5. H. de Guise, S.-H. Tan, I. P. Poulin, B. C. Sanders, *Coincidence
   landscapes for three-channel linear optical networks*, Phys. Rev. A 89,
   063819 (2014); and Y. L. Tan, H. de Guise, B. C. Sanders, *SU(3) Quantum
   Interferometry with single-photon input pulses*, Phys. Rev. Lett. 110,
   220501 (2013) — the n=3 tritter coincidence via permanent + immanant +
   determinant. **This is the Chapter-10/11 n=3 case in the standard basis.**
6. M. Tillmann et al. (incl. H. de Guise, P. Walther), *Generalized
   Multiphoton Quantum Interference*, Phys. Rev. X 5, 041015 (2015) —
   immanants in the three-photon coincidence landscape, experimentally.

**Genuine-indistinguishability witnesses (closest to the Chapter-11 W ≥ 0):**

7. A. J. Menssen et al., *Distinguishability and Many-Particle
   Interference*, Phys. Rev. Lett. 118, 153603 (2017) — the triad /
   collective phase, the genuinely-tripartite term; plus the collective-phase
   follow-up, Phys. Rev. Research 4, 023134 (2022).
8. D. J. Brod, E. F. Galvão et al., *Witnessing Genuine Multiphoton
   Indistinguishability*, Phys. Rev. Lett. 122, 063602 (2019) — a positive
   combination of coincidence probabilities bounded below by a Gram-matrix
   quantity. **Closest prior art to Chapter 11's P111 + D2 ≥ 2/3.**

**Non-PSD internal matrix with valid bosonic positivity (the Chapter-10 motif):**

9. B. Seron, L. Novo, N. J. Cerf, *Boson bunching is not maximized by
   indistinguishable particles*, Nature Photonics 17, 1105 (2023) — a
   distinguishability matrix that is not positive semidefinite, yet the
   bosonic probability stays valid. **This is the established treatment of
   the exact phenomenon Chapter 10 exploits (a sector outside the PSD Gram
   cone whose passive-linear-optical probabilities stay nonnegative), and the
   single citation the negative-Gram line most needs.**
10. R. B. Bapat & V. S. Sunder, permanent-of-Gram conjecture (1985/86); and
    S. W. Drury, a 7×7 counterexample (2016) — the matrix-inequality
    backbone under result 9 and under Chapter 10's polynomial certificate.
11. I. Schur (1918) and E. H. Lieb's permanental-dominance conjecture — the
    permanent / immanant / determinant inequality genre that
    `152‖z‖² + 9|per A|² − 36|det A|² ≥ 0` belongs to.

**Permutation-symmetry structure (the Chapter-12 n=5 material):**

12. C. Dittel et al., *Totally Destructive Interference for
    Permutation-Symmetric Many-Particle States*, Phys. Rev. Lett. 120,
    240404 (2018) / Phys. Rev. A 97, 062116 (2018); and M. C. Tichy et al.,
    *Zero-transmission law for multiport beam splitters*, Phys. Rev. Lett.
    104, 220405 (2010) — count-space structure and suppression from
    permutation symmetry alone.
13. Schur–Weyl duality and decoherence-free-subspace theory (P. Zanardi &
    M. Rasetti 1997; D. Lidar, I. Chuang, K. B. Whaley 1998) — a protected
    logical qubit from collective/permutation symmetry: the standard home of
    the "emergent qubit."

**Real-versus-complex quantum mechanics (the two witnesses):**

14. M.-O. Renou et al., *Quantum theory based on real numbers can be
    experimentally falsified*, Nature 600, 625 (2021); with the photonic and
    superconducting realizations, Li et al., Phys. Rev. Lett. 128, 040402
    (2022) and Chen et al., Phys. Rev. Lett. 128, 040403 (2022). **The
    reference point for any real-vs-complex witness with a numerical gap.**
15. M. McKague, M. Mosca, N. Gisin, *Simulating Quantum Systems Using Real
    Hilbert Spaces*, Phys. Rev. Lett. 102, 020505 (2009) — governs whether a
    "real internal states + mode-only optics" foil is a fair one. (Also
    relevant: L. M. Procopio et al., *Single-photon test of hyper-complex
    quantum theories*, Nat. Commun. 8, 15044 (2017).)

## Recovery versus surviving residue, per result

The verdict below is the blind sweep's, stated at the weakest accurate
label per the program's discipline.

| Chapter result | Standing versus prior art | Grade |
|---|---|---|
| **Ch10/11** — coincidence statistics of partially distinguishable photons as permanents/immanants weighted by a Gram matrix `G` | The founding formalism of the subfield (refs 3–6). Used, not invented, here. | **RECOVERY — must cite.** |
| **Ch11** — `P111 + D2 = (2/9) det G`, hence `≥ 0`, hence the count witness `W ≥ 0` for every partial-distinguishability Hilbert model | The *mechanism* (Gram positivity `det G ≥ 0` forcing a coincidence-sum nonnegative) is the Brod–Galvão indistinguishability-witness mechanism (ref 8) and the immanant positivity of refs 3–6. | **RECOVERY in mechanism.** Residue: the exact closed identity with the specific rational coefficients (2/3, 2/9) for the Fourier tritter is a plausibly-new *special case*, citable as a sharpening — not a new positivity. |
| **Ch10** — `152‖z‖² + 9|per A|² − 36|det A|² ≥ 0` for every complex `3×3 A`, sharper `(7/2)` margin on `U(3)` | The governing question — permanent/immanant positivity surviving a non-PSD internal matrix — is refs 9–11 (Seron–Novo–Cerf; Bapat–Sunder; Drury; Schur/Lieb). | **PARTIALLY KNOWN.** Residue: the specific integer-coefficient certificate and the `U(3)` margin had no verbatim match; likely derivable from permanental-dominance / Bapat–Sunder, which **must be checked** — it may be implied by Drury / Seron–Novo–Cerf. Framed as "a possibly-tighter certificate," not a discovery. |
| **Ch12** — σ_y-blindness of single-shot cyclic counts; permutation-symmetry counting no-go; real/complex/quaternionic single-source no-go | σ_y-blindness = collective-phase invisibility (ref 7); the counting no-go = the Dittel/Tichy suppression-law program (ref 12); real-vs-complex = Renou / McKague (refs 14–15). | **RECOVERY / known-packaging — must cite.** |
| **Ch12** — the achievable count region is an exact simplex for `n ≤ 4` and undergoes a structural change at `n = 5` (the polytope geometry) | The blind sweep found the **weakest prior-art match** here; the convex-geometry statement about count space is the item most plausibly new to the subfield. | **SURVIVING RESIDUE — the line's strongest novelty candidate**, still to be checked against the boson-sampling output-polytope and suppression-law literature before any priority language. |
| **Ch10/12** — the two experiment-open witnesses (negative-Gram vector; conjugation gap `5√2/256`) | "A witness with a numerical gap separating model classes" is the Renou methodology (ref 14); the *specific foils and numbers* are the authors' own. | **Method KNOWN; specific witness plausibly new**, and in both chapters already labeled registered-conditional, not a discovery. |

## Net effect on the claims

- No theorem is withdrawn; the Chapter-11 `W = (2/9) det G` identity and the
  Chapter-10 accessible-positivity theorem stand as **proven** (they are
  independently reproduced by the shipped scripts). What changes is their
  **novelty grade**: the formalism and the positivity *mechanism* are
  recovery of standard partial-distinguishability results and are now cited
  as such; the citable contributions are the *specific* closed forms and,
  most of all, the `n=5` count-region geometry.
- The negative-Gram line's motivating claim — a lawful sector outside the
  PSD Gram cone — now carries its true nearest precedent, **Seron–Novo–Cerf
  2023** (ref 9). This *strengthens* the program's honesty without weakening
  the theorem: the phenomenon is real and studied; the program's move is the
  specific `Z₂` identity-holonomy anchor and the registered count vector,
  which remain conditional and bridge-premise-gated.
- The open crux stands unchanged: the mixed-state layer (multiphoton,
  detector, transfer-matrix, drift nuisances) still awaits a dedicated
  experiment — measurement is the arbiter there. This note is prior-art
  discipline, not that experimental analysis.

## Governance consequence

The Chapter-2 novelty protocol is, from v0.13.0, a **release-checklist gate**
for any chapter that enters a literature not previously swept: the four-lens
blind search is rerun and the nearest precedents are named in the chapter or
in a companion note like this one, before the tag. See
[`release-checklist.md`](release-checklist.md) §2a.
