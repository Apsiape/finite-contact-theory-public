# Expected Output — count_regions.py

Frozen at the v0.12.0 release. Dependency-free; exact where the field allows
(`fractions.Fraction` over Q, `Q(sqrt3)`, `Q(sqrt2)`, and a rational Pauli
algebra): the n=3 bosonic occupation cross-check is done from first principles
(creation operators through the Fourier interferometer, internal states
traced) exactly on a rational witness; the n=4 counterexample, the n=5
rebit-blindness commutator, the K5 identities, and the G1 / conjugation-gap
facts are exact. Runs in under a second. Run from this directory (or from
`verification/scripts/` — the live copy is identical):

```powershell
python count_regions.py
## A: n=3 -- the complete region {B,R,L>=0, C>=B/2}; the sign facet is unique
  [PASS] first-principles bosonic n=3 occupation probs normalize (sum=1: True); C=P111=1043/5625, B(bunching)=1318/5625; the Ch11 count witness satisfies W = P111+D2-2/3 = 512/5625 = (4/3)(C - B/2) (True) = (2/9) det G (True); and D2 = 2/3 + C/3 - 2B/3 (True). So C - B/2 = (1/6) det G (True): the sign facet C >= B/2 <=> Gram PSD <=> Ch11's P111 + D2 >= 2/3 is THE boundary.
  [PASS] the four vertices (trivial (2/3,0,0,1/3), sign (0,0,0,1), standard-R, standard-L) all lie in the region (True); the maximal sign-facet violation on the raw simplex is W_min = (4/3)(0 - 1/2) = -2/3 (-2/3), and the registered Ch10 point W = -128/1125 sits at 0.1707 (64/375 = 64/375) of maximal depth (~17%).
## B: n=4 -- central-projector positivity is INSUFFICIENT (exact counterexample)
  [PASS] the n=4 counterexample x=(3/80,1/20,1/10,1/20,1/20,3/10,1/5,1/16,0,3/20) has sum 1 (=1) and all x_i >= 0 (True); its five central weights are all >= 0 (True, values ['1/10', '3/10', '1/5', '3/10', '1/10']) YET the primitive positivity alpha_211A = x9 - x2 = -1/20 < 0. So central-projector positivity is INSUFFICIENT at n=4.
  [PASS] the six new raw-count inequalities every quantum model obeys are exactly the six non-central primitive positivities: x9>=x2, x6>=x4, x7>=x8+x1, 3x10>=x3+x5, 2x3>=x5, 3x8>=x1 (barycentric forms verified: True); the counterexample violates the first (x9-x2 = -1/20).
## C: n=5 -- the emergent qubit and the REBIT-BLINDNESS theorem
  [PASS] the five fiber effects have zero sigma_y component and their (x,z) parts span a 2-dim space (rank 2) => the fiber operator system is {I, sigma_x, sigma_z}, dim 3: single-shot cyclic counts are SIGMA_Y BLIND. Multiplication recovers it: [F00131,F00212]|M2 = (1/125)[2sx-sz, sx+2sz] = -(2i/25) sigma_y (True, scaled coeff -0.08j); and P_M2 = (625/4)[A,B]^dag[A,B] = I (True); the coherence-witness map (det 5 != 0) inverts to recover (x,z).
  [PASS] commutant dims (n=3,4,5) = (4, 10, 28) (4,10,28: multiplicities <=1 for n<=4 give simplices; n=5 gains M_2(C)); exposure sparsity (N_n,C_n) = ((26, 28), (80, 136)) ((26,28),(80,136), the count-visible fraction of emergent structure shrinking); A4/Fibonacci capacities [1, 1, 2, 5, 13, 34] (1,1,2,5,13,34) with recursion D_(l+2)=3D_(l+1)-D_l (True), Perron rate phi^2=(3+sqrt5)/2.
  [PASS] hidden-center identity: the fiber's maximally-mixed count vector w0 = (5/6) v_(3,2),0 + (1/6) v_(1^5),0 is an exact convex combination of two classical vertices (weights sum to 1=1, one of them the SIGN representation); the K5 coherence cross-section is a DISK with radius tau(beta) = min{(6/5)beta_(3,2), 6 beta_(1^5)}, the two second-order-cone sheets meeting on the ridge beta_(3,2)=5 beta_(1^5) (True); affine dimension 25.
## D: single-source Fourier counting cannot discriminate R / C / H QM
  [PASS] every cyclic count effect is real-symmetric on the fiber (zero sigma_y component for all five, part C), so a quaternionic off-diagonal q = a+ib+jc+kd or a complex one contributes only its real part a: the achievable count bodies coincide, K_R = K_C = K_H exactly (measured affine dimension 25 in all three; Hausdorff distance zero). The common dimension is robustly certified (26 preparations; sigma_min ~ 0.128764 => valid for internal error eps < 0.0128). Single-source Fourier counting provably cannot discriminate real, complex, and quaternionic QM.
## E: general passive networks expose sigma_y; the conjugation-witness experiment
  [PASS] one passive network (gates B^R_03, B^R_13, B^i_01, B^i_14; detect s=(0,3,1,1,0)) compresses to G1 with Pauli coefficients a=21/1024, b=-1/256, d=-15/1024 (rational) and a nonzero sigma_y coefficient -(5/512) sqrt2: trace = 21/512 (21/512), rank 1 (det bracket 0=0), |y| = 5/512*sqrt2 (5 sqrt2/512). So a general passive network EXPOSES sigma_y, which the cyclic-Fourier POVM cannot.
  [PASS] the conjugation-witness experiment: for any real-symmetric internal state p_network = p_conjugate-network, but the complex preparation rho+ = (I+sigma_y)/2 gives p = (21 - 10 sqrt2)/1024 and p_bar = (21 + 10 sqrt2)/1024, an exact gap |p - p_bar| = 5/256*sqrt2 (5 sqrt2/256 ~ 0.0276); one source, two conjugate network settings, one count each; ideal-Bernoulli 5-sigma at ~1304 trials/setting (~1304). REGISTERED / EXPERIMENT-OPEN -- not a performed experiment, not a claim about nature.

# RESULT: 10 passed, 0 failed
# Proof-backed + independently reproduced; the conjugation-witness is a
# REGISTERED protocol with a named target model class, not a performed
# experiment and not a claim about nature.
```

Reminder on scope: the region theorems (n=3/4/5, the R/C/H no-go, the
sequential closure) are proof-backed and independently reproduced; the
conjugation-witness is a **registered, experiment-open** protocol excluding a
named real-internal-states + mode-only-optics model class — it does not
falsify all real quantum mechanics, is not a performed experiment, and is not
a claim about nature.
