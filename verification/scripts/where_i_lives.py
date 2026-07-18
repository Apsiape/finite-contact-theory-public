#!/usr/bin/env python3
"""Chapter 30 -- Where i Lives (public verifier).

Exact, dependency-free: every claim below is certified in rational
(or Gaussian-rational) arithmetic -- Sturm sequences count real
roots exactly; no floating-point spectra are load-bearing.
Classical frames cited per the blind sweep: exceptional-point
real-to-complex transitions in stochastic families (Kato; the
Liouvillian-EP literature), 2-lifts and signed spectra
(Bilu-Linial; Zaslavsky; frustration-index gap bounds --
Belardo; Martin), complex unit gain graphs (Reff) and Hermitian
mixed graphs, character-sector decompositions of covering dynamics
(Mizuno-Sato; Diaconis), Galois conjugacy of sectors, and the
Frobenius-Schur real-vs-complex representation-type dichotomy.
The chapter's own artifacts: the exactly certified window
structure, the certified real-everywhere sign sector, and the
certified non-real charge sector at the reversible point.
"""
from itertools import permutations, product
from fractions import Fraction

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

def make_canon(n):
    PERMSn = list(permutations(range(n)))
    memo = {}
    def canonN(E):
        if E in memo:
            return memo[E]
        best = min(tuple(sorted(tuple(sorted((p[a], p[b])))
                                for a, b in E)) for p in PERMSn)
        memo[E] = best
        return best
    return canonN

def sector(E0, n):
    canonN = make_canon(n)
    rep = {canonN(E0): E0}
    frontier = [E0]
    while frontier:
        nxt = []
        for E in frontier:
            for (a, b) in E:
                singles = contact_singles(E, a, b)
                for choice in product((a, b), repeat=len(singles)):
                    S = succ_max(E, a, b,
                                 dict(zip(singles, choice)), singles)
                    c = canonN(S)
                    if c not in rep:
                        rep[c] = S
                        nxt.append(S)
        frontier = nxt
    classes = sorted(rep)
    idx = {c: i for i, c in enumerate(classes)}
    N = len(classes)
    data = {}
    for c in classes:
        E = rep[c]
        recs = []
        for (a, b) in E:
            singles = contact_singles(E, a, b)
            k = len(singles)
            total = 2 ** k
            good = 0
            parent = {u: (a if u in nb(E, a) else b)
                      for u in singles}
            succs = {}
            devtab = {}
            for choice in product((a, b), repeat=k):
                assign = dict(zip(singles, choice))
                dev = sum(1 for u in singles
                          if assign[u] != parent[u])
                S = succ_max(E, a, b, assign, singles)
                j = idx[canonN(S)]
                succs[j] = succs.get(j, 0) + 1
                key = (j, dev % 4)
                devtab[key] = devtab.get(key, 0) + 1
                if canonN(S) == c:
                    good += 1
            recs.append((total, good, succs, devtab))
        data[idx[c]] = recs
    return N, data, idx, canonN

def build_T(data, N, beta):
    T = [[Fraction(0)] * N for _ in range(N)]
    for i in range(N):
        recs = data[i]
        ws = [Fraction(g, t) ** beta if beta >= 0
              else 1 / (Fraction(g, t) ** (-beta))
              for (t, g, _, _) in recs]
        Z = sum(ws)
        for w, (t, g, succs, _) in zip(ws, recs):
            for j, cnt in succs.items():
                T[i][j] += (w / Z) * Fraction(cnt, t)
    return T

def build_charge(data, N, beta, charge):
    """charge-c kernel entries as (re, im) Fraction pairs."""
    IP = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    Tre = [[Fraction(0)] * N for _ in range(N)]
    Tim = [[Fraction(0)] * N for _ in range(N)]
    for i in range(N):
        recs = data[i]
        ws = [Fraction(g, t) ** beta if beta >= 0
              else 1 / (Fraction(g, t) ** (-beta))
              for (t, g, _, _) in recs]
        Z = sum(ws)
        for w, (t, g, _, devtab) in zip(ws, recs):
            for (j, m), cnt in devtab.items():
                pr, pi = IP[(charge * m) % 4]
                Tre[i][j] += (w / Z) * Fraction(cnt * pr, t)
                Tim[i][j] += (w / Z) * Fraction(cnt * pi, t)
    return Tre, Tim

def stationary(T, N):
    A = [[T[r][c] - (Fraction(1) if r == c else Fraction(0))
          for r in range(N)] for c in range(N)]
    A.append([Fraction(1)] * N)
    Rhs = [Fraction(0)] * N + [Fraction(1)]
    mat = [row[:] + [Rhs[i]] for i, row in enumerate(A)]
    rr = 0
    piv = []
    for col in range(N):
        pv = next((i for i in range(rr, N + 1)
                   if mat[i][col] != 0), None)
        if pv is None:
            continue
        mat[rr], mat[pv] = mat[pv], mat[rr]
        inv = 1 / mat[rr][col]
        mat[rr] = [x * inv for x in mat[rr]]
        for i2 in range(N + 1):
            if i2 != rr and mat[i2][col] != 0:
                f = mat[i2][col]
                mat[i2] = [x - f * y
                           for x, y in zip(mat[i2], mat[rr])]
        piv.append(col)
        rr += 1
    pi = [Fraction(0)] * N
    for i2, col in enumerate(piv):
        pi[col] = mat[i2][N]
    return pi

def charpoly(T, N):
    coeffs = [Fraction(1)]
    M = T
    Mk = [row[:] for row in M]
    for k in range(1, N + 1):
        tr = sum(Mk[i][i] for i in range(N))
        c = -tr / k
        coeffs.append(c)
        if k < N:
            for i in range(N):
                Mk[i][i] += c
            Mk = [[sum(M[i][x] * Mk[x][j] for x in range(N))
                   for j in range(N)] for i in range(N)]
    return coeffs

def sturm_real_roots(coeffs):
    def norm(p):
        while p and p[0] == 0:
            p = p[1:]
        return p
    def deriv(p):
        n = len(p) - 1
        return [c * (n - i) for i, c in enumerate(p[:-1])]
    def prem(a, b):
        a = a[:]
        while len(a) >= len(b) and norm(a):
            f = a[0] / b[0]
            for i in range(len(b)):
                a[i] -= f * b[i]
            a = norm(a[1:]) if a[0] == 0 else a[1:]
        return norm(a)
    chain = [norm(coeffs), norm(deriv(coeffs))]
    while chain[-1] and len(chain[-1]) > 1:
        r = prem(chain[-2][:], chain[-1])
        if not r:
            break
        chain.append([-c for c in r])
    def sgnch(at_inf_sign):
        signs = []
        for p in chain:
            if not p:
                continue
            lead = p[0]
            deg = len(p) - 1
            s = (1 if lead > 0 else -1)
            if at_inf_sign < 0 and deg % 2 == 1:
                s = -s
            signs.append(s)
        return sum(1 for i in range(len(signs) - 1)
                   if signs[i] != signs[i + 1])
    return sgnch(-1) - sgnch(1)

if __name__ == '__main__':
    C5 = frozenset(((0, 1), (1, 2), (2, 3), (3, 4), (0, 4)))
    C6 = frozenset(((0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (0, 5)))
    N6, data6, idx6, canon6 = sector(C6, 6)
    N5, data5, idx5, canon5 = sector(C5, 5)

    print("## 1: no phase without arrow (the reversible point)")
    T0 = build_T(data6, N6, 0)
    pi0 = stationary(T0, N6)
    flow_sym = all(pi0[i] * T0[i][j] == pi0[j] * T0[j][i]
                   for i in range(N6) for j in range(N6))
    rr0 = sturm_real_roots(charpoly(T0, N6))
    ok = flow_sym and rr0 == N6
    check(f"beta=0: the flow matrix pi_i T_ij is exactly symmetric "
          f"({flow_sym}), so T is similar to a real symmetric "
          f"matrix and its spectrum is real -- certified "
          f"independently by Sturm: {rr0}/{N6} real roots ({ok}). "
          f"The reversible point of the rate family carries no "
          f"complex eigenvalue (symmetrizability classical, "
          f"cited).", ok)

    print("## 2: the certified windows")
    certs = {}
    for label, data, N, b in (("n=6 beta=+1", data6, N6, 1),
                              ("n=6 beta=-1", data6, N6, -1),
                              ("n=6 beta=-4", data6, N6, -4),
                              ("n=5 beta=-2", data5, N5, -2),
                              ("n=5 beta=+3", data5, N5, 3)):
        T = build_T(data, N, b)
        rr = sturm_real_roots(charpoly(T, N))
        certs[label] = (N, rr, N - rr)
    ok = (certs["n=6 beta=+1"][2] == 0
          and certs["n=6 beta=-1"][2] == 2
          and certs["n=6 beta=-4"][2] == 4
          and certs["n=5 beta=-2"][2] == 2
          and certs["n=5 beta=+3"][2] == 0)
    check(f"STURM CERTIFICATES (exact rational char polys; "
          f"(degree, real roots, complex roots)): {certs} ({ok}). "
          f"Complex pairs exist at some couplings and not others, "
          f"on both sectors -- the phase lives in WINDOWS bounded "
          f"by real-eigenvalue collisions (the exceptional-point "
          f"mechanism, forced by continuity for real families -- "
          f"Kato, cited; the EP phenomenology in stochastic "
          f"families is established and cited; the certified "
          f"specimen is the artifact). Finer float scans place a "
          f"positive-side window near beta ~ 3.5 (reported, not "
          f"certified: irrational weights).", ok)

    print("## 3: the sign cover -- mass without phase")
    def build_AB(data, N, beta):
        A = [[Fraction(0)] * N for _ in range(N)]
        B = [[Fraction(0)] * N for _ in range(N)]
        for i in range(N):
            recs = data[i]
            ws = [Fraction(g, t) ** beta if beta >= 0
                  else 1 / (Fraction(g, t) ** (-beta))
                  for (t, g, _, _) in recs]
            Z = sum(ws)
            for w, (t, g, _, devtab) in zip(ws, recs):
                for (j, m), cnt in devtab.items():
                    tgt = A if m % 2 == 0 else B
                    tgt[i][j] += (w / Z) * Fraction(cnt, t)
        return A, B
    conn = {}
    real_sign = {}
    for name, data, N in (("n=6", data6, N6), ("n=5", data5, N5)):
        A, B = build_AB(data, N, 0)
        seen = {(0, 1)}
        stack = [(0, 1)]
        while stack:
            i, s = stack.pop()
            for j in range(N):
                for (M, flip) in ((A, 1), (B, -1)):
                    if M[i][j] > 0:
                        t = (j, s * flip)
                        if t not in seen:
                            seen.add(t)
                            stack.append(t)
        conn[name] = len(seen) == 2 * N
    for label, data, N, b in (("n=6 beta=0", data6, N6, 0),
                              ("n=6 beta=-1", data6, N6, -1),
                              ("n=6 beta=-4", data6, N6, -4),
                              ("n=5 beta=-2", data5, N5, -2)):
        A, B = build_AB(data, N, b)
        Ts = [[A[i][j] - B[i][j] for j in range(N)]
              for i in range(N)]
        rr = sturm_real_roots(charpoly(Ts, N))
        real_sign[label] = (rr == N)
    ok = all(conn.values()) and all(real_sign.values())
    check(f"the deviation-parity double cover is NONSPLIT "
          f"(connected: {conn}) -- the 2-lift's twisted sector is "
          f"the signed kernel (Bilu-Linial, cited; nonsplit = "
          f"unbalanced signing, Zaslavsky, cited); and the sign "
          f"sector is ALL-REAL-ROOTED, Sturm-certified, at beta = "
          f"0, -1, -4 (n=6) and -2 (n=5) -- INCLUDING inside the "
          f"base chain's certified complex windows ({real_sign}) "
          f"({ok}). The frustrated sector's spectral-radius "
          f"deficit ('mass') is the known signed-graph gap "
          f"phenomenon (Belardo; Martin, cited; gap sizes "
          f"reported in the paper); the certified realness where "
          f"the base rings -- a sign can carry mass but cannot "
          f"rotate -- is this model's artifact at the certified "
          f"points.", ok)

    print("## 4: the quarter-turn sector rings at the reversible "
          "point")
    ok_ladder = True
    nonreal = {}
    for name, data, N in (("n=6", data6, N6), ("n=5", data5, N5)):
        C0r, C0i = build_charge(data, N, 0, 0)
        C1r, C1i = build_charge(data, N, 0, 1)
        C2r, C2i = build_charge(data, N, 0, 2)
        C3r, C3i = build_charge(data, N, 0, 3)
        A, B = build_AB(data, N, 0)
        if any(C0i[i][j] != 0 for i in range(N) for j in range(N)):
            ok_ladder = False
        if any(C2i[i][j] != 0 for i in range(N) for j in range(N)):
            ok_ladder = False
        if any(C2r[i][j] != A[i][j] - B[i][j] for i in range(N)
               for j in range(N)):
            ok_ladder = False
        if any(C3r[i][j] != C1r[i][j] or C3i[i][j] != -C1i[i][j]
               for i in range(N) for j in range(N)):
            ok_ladder = False
        # Gaussian-rational char poly of charge-1 via complex
        # Faddeev-LeVerrier:
        def cp_gauss(Tr, Ti, N):
            cr = [Fraction(1)]
            ci = [Fraction(0)]
            Mr = [row[:] for row in Tr]
            Mi = [row[:] for row in Ti]
            Kr = [row[:] for row in Mr]
            Ki = [row[:] for row in Mi]
            for k in range(1, N + 1):
                trr = sum(Kr[i][i] for i in range(N))
                tri = sum(Ki[i][i] for i in range(N))
                ar = -trr / k
                ai = -tri / k
                cr.append(ar)
                ci.append(ai)
                if k < N:
                    for i in range(N):
                        Kr[i][i] += ar
                        Ki[i][i] += ai
                    K2r = [[sum(Mr[i][x] * Kr[x][j]
                                - Mi[i][x] * Ki[x][j]
                                for x in range(N))
                            for j in range(N)] for i in range(N)]
                    K2i = [[sum(Mr[i][x] * Ki[x][j]
                                + Mi[i][x] * Kr[x][j]
                                for x in range(N))
                            for j in range(N)] for i in range(N)]
                    Kr, Ki = K2r, K2i
            return cr, ci
        cr, ci = cp_gauss(C1r, C1i, N)
        nonreal[name] = any(c != 0 for c in ci)
    ok = ok_ladder and all(nonreal.values())
    check(f"the Z4 lift's ladder is exact: charge-0 = the base "
          f"(real), charge-2 = the sign sector (real), charge-3 = "
          f"the elementwise conjugate of charge-1 (Galois "
          f"conjugacy of sectors, automatic and cited) "
          f"({ok_ladder}); and the charge-1 characteristic "
          f"polynomial is GENUINELY NON-REAL at the reversible "
          f"point, in exact Gaussian rationals, on both sectors "
          f"({nonreal}) -- a polynomial with non-real coefficients "
          f"has a non-real root, so complex eigenvalues exist AT "
          f"EQUILIBRIUM in the quarter-turn sector ({ok}). "
          f"Character-sector machinery classical (gain graphs -- "
          f"Reff; covering L-functions -- Mizuno-Sato, cited); "
          f"the real-vs-complex sector dichotomy follows "
          f"Frobenius-Schur representation-type logic (cited); "
          f"the certified configuration -- reversible base, real "
          f"sign sector, non-real quarter-turn sectors -- is the "
          f"artifact. Measured args (~pi/2, reported) are "
          f"kernel-inherited (arg of (1+i)/2), not emergent.", ok)

    print(f"\n# RESULT: {len(PASS)} passed, {len(FAIL)} failed")
    raise SystemExit(1 if FAIL else 0)
