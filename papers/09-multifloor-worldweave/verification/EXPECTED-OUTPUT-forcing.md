# Expected Output — forcing_audit.py

Frozen at the v0.9.0 release. Dependency-free; exact arithmetic; runs in a
fraction of a second. Run from this directory (or from
`verification/scripts/` — the live copy is identical):

```powershell
python forcing_audit.py
## A1: Golay is not the unique doubly-even self-dual [24,12] code
  [PASS] the Golay enumerator (1 + 759y^8 + 2576y^12 + ..., d=8) and the matched alternative (1 + 6y^4 + 735y^8 + ..., d=4) are BOTH exactly MacWilliams-self-dual and doubly-even, each summing to 2^12 = 4096, and they are distinct (A_4 = 0 vs 6). Golay's d=8 is thus one point in the Pless-Sloane classification of doubly-even self-dual [24,12] codes, not a forced closure.
  [PASS] a concrete matched code is constructible: six local port receipts (the block all-ones words) plus a trace-lifted hexacode form a [24,12] binary code that is self-dual and doubly-even with exactly the alternative weight enumerator (A_4 = 6, the six receipts), for a port map found by exhaustive search (FOUND). This is a lawful alternative to Golay on the same six cells and four ports.
  [PASS] an independent construction confirms the class is nonempty: the [8,4,4] extended Hamming code is doubly-even self-dual (True), and three orthogonal copies give a doubly-even self-dual [24,12,4] code (True) -- again distinct from Golay's d=8. The counterworld does not depend on any one construction.
## A2: the bridge family selects neither positivity, integrality, nor a magnitude
  [PASS] det G_t = (1 - t^2)^4 computed from the built 8x8 matrix (True); its eigenvalues are exactly 1 +/- t (each multiplicity four), verified structurally (True); so it is positive-definite for |t| < 1 (exact LDL at t = 1/2 has all pivots > 0: True; the positive IRRATIONAL t = sqrt(2)/2 satisfies t^2 = 1/2 < 1 exactly, hence both 1 +/- t > 0: True), indefinite for |t| > 1 (t = 2 has a negative LDL pivot: True), and degenerate only at t = 1 (True). No-silent-loss singles out none of positivity, integrality, or a preferred magnitude -- the scale-free ceiling, from the multi-floor side.
## A3: both V4 and C3 are valid export quotients (alphabet not unique)
  [PASS] Q8 / center has order 4 with every nonidentity element an involution -- the Klein four-group V4 (True); and the binary tetrahedral group 2T = SL(2,3) (order 24) has a normal quaternion subgroup of order 8 with quotient of order 3 -- C3 (True). Both V4 and C3 are lawful export quotients; the floor does not rank one as the unique inter-floor alphabet.
## A4: operational completeness gives a dual pole H < H-perp, not self-duality
  [PASS] over GF(4) there are exactly 3 Hermitian self-dual codes on two cells, forming a single S_3 (triality) orbit (True); and an operationally complete receiver is a separating dual pole, not a self-dual code: the isotropic seed <(1,1,0,0)> has |H| = 4 strictly inside |H-perp| = 64 (True). Completeness needs a dual pole; self-duality is an extra condition that does not pick a member.
## A5: E_8 + E_8 + E_8 is even unimodular but has 720 roots (Leech is extra)
  [PASS] E_8 has 240 roots; the orthogonal sum E_8 + E_8 + E_8 is positive, integral, even, and unimodular in 24 dimensions, yet its norm-two vectors number 720 = 3 x 240 = 720 (a cross-block vector has norm >= 4). The Leech lattice's rootlessness is therefore an additional minimum-norm law, not implied by even-unimodular completion.
## B1: of 256 maps on 4 phases, exactly 64 strictly settle, each Lyapunov
  [PASS] of the 256 = 256 deterministic maps on four phases, exactly 64 strictly settle to a single terminal phase -- the rooted-tree count 4^3 = n^(n-1) -- and every one carries a Lyapunov ranking V(F(x)) = V(x) - 1 (True). Strict selection requires a ranking; it is not free.
## B2: reversible dynamics has stationary law pi proportional to e^{-V}
  [PASS] a reversible chain built from a potential V satisfies detailed balance pi_i P_ij = pi_j P_ji exactly with pi proportional to e^{-V} (True), and pi is its stationary law (True). Reversible dynamics does not create a selector; it encodes the conserved one as V = -log pi. SCOPE (stated honestly): this equivalence covers deterministic-settling (B1) and reversible-stochastic (B2) dynamics -- the class that includes the floor's gradient-on-a-potential dynamics. Genuinely IRREVERSIBLE, non-detailed-balance DRIVEN dynamics is out of scope here and held open; the program treats the floor as driven-dissipative, so this is a real edge -- though driven dynamics still carries an entropy-production / burden functional, itself a ranking, which is why the conserved-selector reading is expected but NOT proven to extend.
## B3: two passive potentials select an integral vs an irrational attractor
  [PASS] on the same bridge family, the passive potential V0(t) = t^2 selects the integral attractor t = 0 (True), while V_irr(t) = (t^2 - 1/2)^2 selects the irrational attractor t = 1/sqrt(2) (True); and the V4-vs-C3 scalarization crossover is at lambda* = 2 - log2(3) = 0.4150375 (True). The attractor is an input carried in the potential, not a floor output.
## B4: the terminal class is forceable; its members are S_3-transitive (uniform 1/3)
  [PASS] self-duality is forceable as a terminal CLASS (H = H-perp is a well-defined attractor set), but its 3 members form one S_3 orbit, so a target-blind equivariant dynamics can only assign the uniform measure 1/3 = 1/3 to each. The class is forced; the member never is.
## C1: Born-by-counting -- the response kernel and its spectrum
  [PASS] the response kernel K = (1/3)|<p,q>|^2 on the 12 rays takes only the values {0, 1/12, 1/3} (True), is row-stochastic (True) with every row profile (one 1/3, eight 1/12, three 0) (True), trace 4, and rank 10 = dim Sym(4,R) = 10. This K is the EQUAL-TICKET (alpha = beta) member of the one-parameter equivariant counting family (wcd_actualization.py): counting forces the FORM of an actual phase's response, but the Born magnitude law (equal tickets) is an added, received input -- the relocated selector Section B predicts.
## C2: the correlation-arity theorem (uniform marginals below the dual distance)
  [PASS] for a self-dual linear code phase the first visible global binding arity equals the dual distance: the hexacode has dual distance 4 with all marginals through 3 floors exactly uniform (True) and the first nonuniform marginal at 4 floors (True); the matched binary [24,12,4] phase has dual distance 4. So a population can carry exact global binding while every lower-arity observer sees maximum local randomness (Delsarte: dual distance = orthogonal-array strength + 1).

# RESULT: 13 passed, 0 failed
```

Every load-bearing quantity is exact (`fractions.Fraction`, exact `GF(2)`/
`GF(4)` and integer arithmetic); the code, group, lattice-root, settling-map,
and design computations are exhaustive (the single irrational magnitude
lambda* = 2 - log2(3) is checked to high precision).
