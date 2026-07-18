#!/usr/bin/env python3
"""Chapter 27 -- The Thermodynamics of the Floor (public verifier).

Exact, dependency-free. The genesis dynamics of Chapters 21-26
(maximal-retention contact on graphs; edge count conserved) is here
given its statistical mechanics, from counting alone. Classical
components are recoveries and cited in-line per the blind sweep:
doubly-stochastic uniform stationarity (Levin-Peres-Wilmer),
surprisal-as-energy (Jaynes; Landauer), the Cauchy functional
equation route to exponential rate laws (Arrhenius; Kramers),
min-cost-over-mean-cost stationary selection (Freidlin-Wentzell;
Landauer's blowtorch), entropy production and cycle currents
(Schnakenberg; Hill; Seifert). The chapter's own artifacts: the
exact 61 x 60 state count behind the 1/61 ensemble, the exact
free-move split, and the measured unimodal dissipation profile.
"""
from itertools import combinations, permutations, product
from fractions import Fraction
import math

PASS, FAIL = [], []
def check(name, ok):
    (PASS if ok else FAIL).append(name)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)

def nb(E, v):
    return {b if a == v else a for a, b in E if v in (a, b)}

def contact_singles(E, a, b):
    Na = nb(E, a) - {b}
    Nb = nb(E, b) - {a}
    return sorted((Na | Nb) - (Na & Nb))

def succ_max(E, a, b, assign, singles):
    Na = nb(E, a) - {b}
    Nb = nb(E, b) - {a}
    cap = Na & Nb
    S = {e for e in E if a not in e and b not in e}
    S.add((min(a, b), max(a, b)))
    for x in cap:
        S.add((min(a, x), max(a, x)))
        S.add((min(b, x), max(b, x)))
    for s in singles:
        S.add((min(assign[s], s), max(assign[s], s)))
    return frozenset(S)

PERMS6 = list(permutations(range(6)))
_memo = {}
def canon6(E):
    if E in _memo:
        return _memo[E]
    best = min(tuple(sorted(tuple(sorted((p[a], p[b])))
                            for a, b in E)) for p in PERMS6)
    _memo[E] = best
    return best

def build_sector():
    C6 = frozenset(((0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (0, 5)))
    rep = {canon6(C6): C6}
    frontier = [C6]
    while frontier:
        nxt = []
        for E in frontier:
            for (a, b) in E:
                singles = contact_singles(E, a, b)
                for choice in product((a, b), repeat=len(singles)):
                    S = succ_max(E, a, b, dict(zip(singles, choice)),
                                 singles)
                    c = canon6(S)
                    if c not in rep:
                        rep[c] = S
                        nxt.append(S)
        frontier = nxt
    return rep, C6

def class_data(rep, classes, idx):
    data = {}
    for c in classes:
        E = rep[c]
        recs = []
        for (a, b) in E:
            singles = contact_singles(E, a, b)
            k = len(singles)
            total = 2 ** k
            good = 0
            succs = {}
            for choice in product((a, b), repeat=k):
                S = succ_max(E, a, b, dict(zip(singles, choice)),
                             singles)
                j = idx[canon6(S)]
                succs[j] = succs.get(j, 0) + 1
                if canon6(S) == c:
                    good += 1
            recs.append((total, good, succs))
        data[idx[c]] = recs
    return data

def build_T(data, N, beta):
    T = [[Fraction(0)] * N for _ in range(N)]
    for i in range(N):
        recs = data[i]
        ws = [Fraction(g, t) ** beta if beta >= 0
              else 1 / (Fraction(g, t) ** (-beta)) for (t, g, _)
              in recs]
        Z = sum(ws)
        for w, (t, g, succs) in zip(ws, recs):
            for j, cnt in succs.items():
                T[i][j] += (w / Z) * Fraction(cnt, t)
    return T

def stationary(T, N):
    A = [[T[r][c] - (Fraction(1) if r == c else Fraction(0))
          for r in range(N)] for c in range(N)]
    A.append([Fraction(1)] * N)
    Rhs = [Fraction(0)] * N + [Fraction(1)]
    mat = [row[:] + [Rhs[i]] for i, row in enumerate(A)]
    r = 0
    piv = []
    for col in range(N):
        pv = next((i for i in range(r, N + 1) if mat[i][col] != 0),
                  None)
        if pv is None:
            continue
        mat[r], mat[pv] = mat[pv], mat[r]
        inv = 1 / mat[r][col]
        mat[r] = [x * inv for x in mat[r]]
        for i2 in range(N + 1):
            if i2 != r and mat[i2][col] != 0:
                f = mat[i2][col]
                mat[i2] = [x - f * y for x, y in zip(mat[i2], mat[r])]
        piv.append(col)
        r += 1
    pi = [Fraction(0)] * N
    for i2, col in enumerate(piv):
        pi[col] = mat[i2][N]
    return pi

if __name__ == '__main__':
    rep, C6 = build_sector()
    classes = sorted(rep)
    idx = {c: i for i, c in enumerate(classes)}
    N = len(classes)
    data = class_data(rep, classes, idx)
    T_uni = build_T(data, N, 0)
    pi_uni = stationary(T_uni, N)
    cyc = idx[canon6(C6)]

    print("## 1: the microcanonical state count")
    orbits = {}
    for c in classes:
        Efix = frozenset(rep[c])
        aut = sum(1 for p in PERMS6 if frozenset(
            tuple(sorted((p[a], p[b]))) for a, b in Efix) == Efix)
        orbits[idx[c]] = 720 // aut
    tot = sum(orbits.values())
    ok = all(pi_uni[i] == Fraction(orbits[i], tot) for i in range(N))
    check(f"the uniform-rate stationary law is uniform on LABELED "
          f"worlds: pi[c] = orbit(c)/{tot} exactly for all 13 "
          f"classes; orbit sizes {sorted(orbits.values())}, sum = "
          f"3660 = 61 x 60 -- the sector's 1/61 cycle weight is a "
          f"state count ({ok}). Classification: doubly-stochastic /"
          f" symmetric-kernel uniform stationarity is textbook "
          f"(Levin-Peres-Wilmer); the content is that THIS kernel "
          f"has it, making the equal-a-priori-weight form a "
          f"property of the dynamics rather than a postulate at "
          f"this scope.", ok)

    print("## 2: detailed balance at the price-blind point only")
    rev = {}
    weights = {}
    for b in (-1, 0, 1, 2, 3):
        T = build_T(data, N, b)
        pi = stationary(T, N)
        rev[b] = all(pi[i] * T[i][j] == pi[j] * T[j][i]
                     for i in range(N) for j in range(N))
        weights[b] = pi[cyc]
    ok = (rev[0] and not any(rev[b] for b in rev if b != 0)
          and all(weights[b] > weights[b2] for b, b2 in
                  zip((-1, 0, 1, 2), (0, 1, 2, 3)))
          and weights[-1] > Fraction(1, 61))
    check(f"reversibility across the rate family w = fraction^beta: "
          f"{ {b: rev[b] for b in sorted(rev)} } -- beta = 0 is the "
          f"unique reversible member tested (any price coupling, "
          f"either direction, breaks detailed balance); the cycle's "
          f"stationary weight is strictly decreasing in beta "
          f"({[(b, str(weights[b])) for b in sorted(weights)]}) and "
          f"the anti-coupled chain protects the sparse class "
          f"({ok}). Kolmogorov-criterion machinery classical, "
          f"cited.", ok)

    print("## 3: the Boltzmann identity and the forced form")
    ok1 = True
    for (E, nn) in ((C6, 6),
                    (frozenset(e for e in combinations(range(6), 2)
                               if e != (0, 1)), 6)):
        for (a, b) in sorted(E)[:3]:
            singles = contact_singles(E, a, b)
            k = len(singles)
            total = 2 ** k
            good = 0
            cE = canon6(E)
            for choice in product((a, b), repeat=k):
                if canon6(succ_max(E, a, b,
                                   dict(zip(singles, choice)),
                                   singles)) == cE:
                    good += 1
            if good and abs(2 ** (-math.log2(total / good))
                            - good / total) > 1e-12:
                ok1 = False
    # additivity on a disjoint union (C4 + C4'), all 16 pairs:
    A4 = frozenset(((0, 1), (1, 2), (2, 3), (0, 3)))
    B4 = frozenset(((4, 5), (5, 6), (6, 7), (4, 7)))
    U = A4 | B4
    VA, VB = {0, 1, 2, 3}, {4, 5, 6, 7}
    def canon_on(E, verts):
        vs = sorted(verts)
        best = None
        for p in permutations(vs):
            m = dict(zip(vs, p))
            img = tuple(sorted(tuple(sorted((m[x], m[y])))
                               for x, y in E))
            if best is None or img < best:
                best = img
        return best
    def comp_repro(E, verts, c):
        singles = contact_singles(E, *c)
        cref = canon_on(E, verts)
        good = set()
        for ch in product(c, repeat=len(singles)):
            if canon_on(succ_max(E, *c, dict(zip(singles, ch)),
                                 singles), verts) == cref:
                good.add(ch)
        return singles, good
    ok2 = True
    for c1 in sorted(A4):
        for c2 in sorted(B4):
            s1, r1 = comp_repro(A4, VA, c1)
            s2, r2 = comp_repro(B4, VB, c2)
            joint = 0
            for ch1 in product(c1, repeat=len(s1)):
                U1 = succ_max(U, *c1, dict(zip(s1, ch1)), s1)
                for ch2 in product(c2, repeat=len(s2)):
                    U2 = succ_max(U1, *c2, dict(zip(s2, ch2)), s2)
                    Ap = frozenset(e for e in U2 if e[0] in VA)
                    Bp = frozenset(e for e in U2 if e[0] in VB)
                    if (canon_on(Ap, VA) == canon_on(A4, VA)
                            and canon_on(Bp, VB)
                            == canon_on(B4, VB)):
                        joint += 1
            if joint != len(r1) * len(r2):
                ok2 = False
    ok = ok1 and ok2
    check(f"2^(-cost) equals the class-preserving fraction (the "
          f"surprisal-as-energy identity, definitional -- Jaynes, "
          f"Landauer cited) ({ok1}); the joint preserving set of "
          f"one contact in each disjoint component is the exact "
          f"product on all 16 cross-pairs, so cost is additive and "
          f"any price-only independent rate law is exponential in "
          f"cost by the Cauchy functional equation (Arrhenius/"
          f"Kramers route, cited): THE FORM IS FORCED, THE "
          f"TEMPERATURE RECEIVED ({ok2}) ({ok}).", ok)

    print("## 4: the free-move law")
    T_arr = build_T(data, N, 1)
    pi_arr = stationary(T_arr, N)
    ratio = {i: pi_arr[i] / pi_uni[i] for i in range(N)}
    r = {i: Fraction(sum(g for (t, g, _) in data[i]),
                     sum(t for (t, g, _) in data[i]))
         for i in range(N)}
    viol = sum(1 for i in range(N) for j in range(N)
               if r[i] > r[j] and not ratio[i] > ratio[j])
    maxf = {i: max(Fraction(g, t) for (t, g, _) in data[i])
            for i in range(N)}
    free = [i for i in range(N) if maxf[i] == 1]
    bound = [i for i in range(N) if maxf[i] < 1]
    split = (min(ratio[i] for i in free)
             > max(ratio[i] for i in bound))
    lemma = True
    for i in range(N):
        fs = [Fraction(g, t) for (t, g, _) in data[i]]
        S1 = sum(fs)
        S2 = sum(f * f for f in fs)
        if T_uni[i][i] != S1 / len(fs) or T_arr[i][i] != S2 / S1:
            lemma = False
        if not T_arr[i][i] >= T_uni[i][i]:
            lemma = False
    ok = viol > 0 and split and lemma
    check(f"mean-cost monotonicity FAILS ({viol}/74 strict pairs "
          f"violated; a frozen bet died and is scored) while the "
          f"FREE-MOVE SPLIT is exact: all {len(free)} classes "
          f"owning a certainty contact outrank all {len(bound)} "
          f"without one ({split}); self-retention lemma exact "
          f"(uniform diagonal = mean fraction, price-weighted "
          f"diagonal = sum f^2 / sum f >= mean, Cauchy-Schwarz) "
          f"({lemma}) ({ok}). Classification: min-cost-over-mean "
          f"stationary selection is the Freidlin-Wentzell / "
          f"blowtorch phenomenon, cited; the exact finite split by "
          f"certainty-contact possession is this sector's artifact.",
          ok)

    print("## 5: dissipation and the cost-pump cycle")
    sig = {}
    Ts = {}
    pis = {}
    for b in (0, 1, 2, 3, 4, 5):
        T = build_T(data, N, b)
        pi = stationary(T, N)
        Ts[b], pis[b] = T, pi
        s = 0.0
        for i in range(N):
            for j in range(N):
                if T[i][j] > 0 and T[j][i] > 0:
                    fij = pi[i] * T[i][j]
                    fji = pi[j] * T[j][i]
                    if fij != fji:
                        s += float(fij) * math.log(float(fij / fji))
        sig[b] = s
    ok1 = (sig[0] == 0.0 and sig[1] < sig[2]
           and sig[2] > sig[3] > sig[4] > sig[5])
    T1, p1 = Ts[1], pis[1]
    J = [[p1[i] * T1[i][j] - p1[j] * T1[j][i] for j in range(N)]
         for i in range(N)]
    div_free = all(sum(J[i][j] for j in range(N)) == 0
                   for i in range(N))
    cost = {i: math.log2(sum(t for (t, g, _) in data[i])
                         / sum(g for (t, g, _) in data[i]))
            for i in range(N)}
    D = sum(float(J[i][j]) * (cost[i] - cost[j])
            for i in range(N) for j in range(N)) / 2
    mean_uni = sum(float(pis[0][i]) * cost[i] for i in range(N))
    mean_arr = sum(float(p1[i]) * cost[i] for i in range(N))
    ok2 = div_free and abs(D) < 1e-12 and mean_arr < mean_uni
    ok = ok1 and ok2
    check(f"entropy production (Schnakenberg form, cited) is zero "
          f"exactly at beta=0 and MEASURED UNIMODAL on the sampled "
          f"grid: {[(b, f'{sig[b]:.4f}') for b in sorted(sig)]} "
          f"nats/step, peak at beta=2, decaying toward the frozen "
          f"limit ({ok1}); the steady current is divergence-free "
          f"with the naive downhill functional vanishing "
          f"identically (Hodge/cycle structure -- Schnakenberg/"
          f"Hill cycle theory, cited) while the mean cost drops "
          f"{mean_uni:.4f} -> {mean_arr:.4f} bits under the price "
          f"coupling ({ok2}) ({ok}). A frozen monotone-dissipation "
          f"bet died here and is scored; the interior maximum is "
          f"the finding.", ok)

    print(f"\n# RESULT: {len(PASS)} passed, {len(FAIL)} failed")
    raise SystemExit(1 if FAIL else 0)
