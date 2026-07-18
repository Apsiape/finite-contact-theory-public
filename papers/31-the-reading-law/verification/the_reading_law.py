#!/usr/bin/env python3
"""Chapter 31 -- The Reading Law (public verifier).

Exact, exhaustive, dependency-free. The amplitude calculus of the
quarter-turn sector (Chapter 30) related, channel by channel, to
the base probability -- and read through a maintained structure
(Chapter 28). Per the blind sweep, the strongest honest framing is
adopted throughout: this is AN EXACTLY SOLVABLE COMBINATORIAL MODEL
IN WHICH THE DECOHERENT-HISTORIES PACKAGE HOLDS EXACTLY RATHER
THAN APPROXIMATELY -- the consistency/additivity condition
(Griffiths; Omnes; Gell-Mann-Hartle, cited), the records route to
it (Gell-Mann-Hartle strong decoherence; Zurek, cited), the
per-unread-bit visibility decay (the spin-bath product form and
the Englert visibility lineage, cited), Sorkin-style preclusion of
null history classes (cited), the i-per-deviation mass mechanism
(the Feynman checkerboard -- Feynman-Hibbs; Jacobson-Schulman,
cited), and the Zeno tier (Misra-Sudarshan, cited). What is called
"additivity-exact" below is |amp| = P -- the consistency
condition, NOT Born's squared-modulus rule; the constants 1/sqrt2,
pi/4, pi/2 are kernel-inherited (moduli/args of (1+i)/2), not
emergent. The artifacts: every law is exact, with closed forms.
"""
from itertools import combinations, permutations, product
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

def induced(E, S):
    return frozenset(e for e in E if e[0] in S and e[1] in S)

def interface(E, S):
    return frozenset(e for e in E if (e[0] in S) != (e[1] in S))

def transpose_edges(E, a, b):
    m = {a: b, b: a}
    return frozenset(tuple(sorted((m.get(x, x), m.get(y, y))))
                     for x, y in E)

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

def sector_classes(E0, n, canonN):
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
    return rep

IP = [(Fraction(1), Fraction(0)), (Fraction(0), Fraction(1)),
      (Fraction(-1), Fraction(0)), (Fraction(0), Fraction(-1))]

if __name__ == '__main__':
    C4 = frozenset(((0, 1), (1, 2), (2, 3), (0, 3)))
    C5 = frozenset(((0, 1), (1, 2), (2, 3), (3, 4), (0, 4)))
    C6 = frozenset(((0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (0, 5)))

    print("## 1: the swap-pairing lemma and the identity move")
    swap_ok = ident_ok = True
    ncases = 0
    sects = []
    for E0, n in ((C4, 4), (C5, 5), (C6, 6)):
        canonN = make_canon(n)
        rep = sector_classes(E0, n, canonN)
        sects.append((E0, n, canonN, rep))
        for c, E in rep.items():
            for (a, b) in E:
                singles = contact_singles(E, a, b)
                parent = {u: (a if u in nb(E, a) else b)
                          for u in singles}
                if succ_max(E, a, b, dict(parent), singles) != E:
                    ident_ok = False
                for choice in product((a, b),
                                      repeat=len(singles)):
                    assign = dict(zip(singles, choice))
                    swapped = {u: (b if v == a else a)
                               for u, v in assign.items()}
                    S1 = succ_max(E, a, b, assign, singles)
                    S2 = succ_max(E, a, b, swapped, singles)
                    if S2 != transpose_edges(S1, a, b):
                        swap_ok = False
                    ncases += 1
    ok = swap_ok and ident_ok
    check(f"flipping every single's assignment conjugates the "
          f"successor by the transposition (a b), on all {ncases} "
          f"cases across three sectors ({swap_ok}); the "
          f"stay-with-parent assignment is the exact labeled "
          f"identity ({ident_ok}) ({ok}). A sign-reversing-"
          f"involution structure (the Lindstrom / Gessel-Viennot "
          f"proof device, cited): contributions pair as "
          f"(dev, k - dev) toward the same class.", ok)

    print("## 2: rest is precluded on the cycles")
    even_ok = True
    diag_zero_ok = True
    for E0, n, canonN, rep in sects:
        classes = sorted(rep)
        idx = {c: i for i, c in enumerate(classes)}
        N = len(classes)
        T1re = [[Fraction(0)] * N for _ in range(N)]
        T1im = [[Fraction(0)] * N for _ in range(N)]
        for c in classes:
            i = idx[c]
            E = rep[c]
            m = len(E)
            for (a, b) in E:
                singles = contact_singles(E, a, b)
                k = len(singles)
                parent = {u: (a if u in nb(E, a) else b)
                          for u in singles}
                table = {}
                for choice in product((a, b), repeat=k):
                    assign = dict(zip(singles, choice))
                    dev = sum(1 for u in singles
                              if assign[u] != parent[u])
                    j = idx[canonN(succ_max(E, a, b, assign,
                                            singles))]
                    if j not in table:
                        table[j] = [0, 0, 0, 0]
                    table[j][dev % 4] += 1
                for j, ms in table.items():
                    if k % 4 == 2 and ms[0] != ms[2]:
                        even_ok = False
                    T1re[i][j] += Fraction(ms[0] - ms[2],
                                           m * 2 ** k)
                    T1im[i][j] += Fraction(ms[1] - ms[3],
                                           m * 2 ** k)
        ci = idx[canonN(E0)]
        if T1re[ci][ci] != 0 or T1im[ci][ci] != 0:
            diag_zero_ok = False
    ok = even_ok and diag_zero_ok
    check(f"even-sector cancellation is exact at every k = 2 mod 4 "
          f"channel (cnt[dev 0] == cnt[dev 2]) ({even_ok}); the "
          f"cycle classes C4, C5, C6 have quarter-turn survival "
          f"amplitude EXACTLY ZERO ({diag_zero_ok}) ({ok}). The "
          f"identity path and its swap-mirror arrive in antiphase "
          f"(1 + i^2 = 0): a Sorkin-style PRECLUSION of the "
          f"survival class (cited), by the checkerboard's "
          f"i-per-deviation mechanism (Feynman-Hibbs; "
          f"Jacobson-Schulman, cited) -- one mechanism yields the "
          f"damped diagonal and the pure-imaginary movement "
          f"channels at once.", ok)

    print("## 3: the additivity dichotomy")
    bound_ok = dich_ok = True
    census = {}
    for E0, n, canonN, rep in sects:
        classes = sorted(rep)
        idx = {c: i for i, c in enumerate(classes)}
        N = len(classes)
        pure = mixed = 0
        for c in classes:
            E = rep[c]
            m = len(E)
            for (a, b) in E:
                singles = contact_singles(E, a, b)
                k = len(singles)
                parent = {u: (a if u in nb(E, a) else b)
                          for u in singles}
                table = {}
                for choice in product((a, b), repeat=k):
                    assign = dict(zip(singles, choice))
                    dev = sum(1 for u in singles
                              if assign[u] != parent[u])
                    j = idx[canonN(succ_max(E, a, b, assign,
                                            singles))]
                    if j not in table:
                        table[j] = [0, 0, 0, 0]
                    table[j][dev % 4] += 1
                for j, ms in table.items():
                    re = Fraction(ms[0] - ms[2])
                    im = Fraction(ms[1] - ms[3])
                    amp2 = re * re + im * im
                    base2 = Fraction(sum(ms)) ** 2
                    if amp2 > base2:
                        bound_ok = False
                    if amp2 == base2:
                        pure += 1
                    else:
                        mixed += 1
                        if not amp2 < base2:
                            dich_ok = False
        census[f"n={n}"] = (pure, mixed,
                            round(pure / (pure + mixed), 3))
    falling = (census["n=4"][2] > census["n=5"][2]
               > census["n=6"][2])
    ok = bound_ok and dich_ok and falling
    check(f"|amplitude| <= probability ENTRYWISE, exact squares "
          f"({bound_ok}) -- interference can veto, never amplify "
          f"(the triangle-inequality structure, stated as such); "
          f"every channel is either ADDITIVITY-EXACT (phase-pure: "
          f"|amp| = P -- the decoherent-histories consistency "
          f"condition, Griffiths/Omnes/Gell-Mann-Hartle, cited; "
          f"NOT Born's squared-modulus rule) or strictly "
          f"destructive ({dich_ok}); and the phase-pure fraction "
          f"FALLS with sector size: {census} ({falling}) ({ok}). "
          f"Generic channels interfere -- the Dowker-Kent "
          f"genericity phenomenon (cited) realized exactly.", ok)

    print("## 4: the reading law (records make it exact)")
    WORLDS = {
        "C6": C6,
        "octahedron": frozenset(e for e in
                                combinations(range(6), 2)
                                if e not in ((0, 3), (1, 4),
                                             (2, 5))),
        "K6-e": frozenset(e for e in combinations(range(6), 2)
                          if e != (0, 1)),
        "prism": frozenset(((0, 1), (1, 2), (0, 2), (3, 4),
                            (4, 5), (3, 5), (0, 3), (1, 4),
                            (2, 5))),
    }
    def bodies(E, n=6):
        out = []
        for kk in (2, 3, 4):
            for S in combinations(range(n), kk):
                Sset = set(S)
                Ein = induced(E, Sset)
                if not Ein and kk > 1:
                    continue
                seen = {S[0]}
                stack = [S[0]]
                while stack:
                    v = stack.pop()
                    for x, y in Ein:
                        w = (y if x == v
                             else (x if y == v else None))
                        if w is not None and w not in seen:
                            seen.add(w)
                            stack.append(w)
                if seen == Sset:
                    out.append(Sset)
        return out
    grip_ok = inj_ok = law_ok = zeno_ok = True
    vis_channels = 0
    for wname, E in WORLDS.items():
        for S in bodies(E):
            shape = induced(E, S)
            iface = interface(E, S)
            for (a, b) in E:
                singles = contact_singles(E, a, b)
                k = len(singles)
                touching = a in S or b in S
                parent = {u: (a if u in nb(E, a) else b)
                          for u in singles}
                Ssing = [u for u in singles if u in S]
                admissible = []
                anchor = []
                for choice in product((a, b), repeat=k):
                    assign = dict(zip(singles, choice))
                    E2 = succ_max(E, a, b, assign, singles)
                    if induced(E2, S) != shape:
                        continue
                    admissible.append((assign, E2))
                    if interface(E2, S) == iface:
                        anchor.append(assign)
                if touching:
                    if len(anchor) != 1 or any(
                            anchor[0][u] != parent[u]
                            for u in singles):
                        zeno_ok = False
                adm_n = len(admissible)
                chans = {}
                for assign, E2 in admissible:
                    f2 = interface(E2, S)
                    dev = sum(1 for u in singles
                              if assign[u] != parent[u])
                    dr = (dev if touching else
                          sum(1 for u in Ssing
                              if assign[u] != parent[u]))
                    chans.setdefault(f2, []).append((dev, dr))
                m_unread = 0 if touching else k - len(Ssing)
                for f2, paths in chans.items():
                    if touching:
                        vis_channels += 1
                        if len(paths) != 1:
                            inj_ok = False
                    if len(paths) != 2 ** m_unread:
                        law_ok = False
                    are = sum(IP[d % 4][0] for d, _ in paths)
                    ime = sum(IP[d % 4][1] for d, _ in paths)
                    are = Fraction(are, adm_n)
                    ime = Fraction(ime, adm_n)
                    dr = paths[0][1]
                    cre, cim = Fraction(1), Fraction(0)
                    for _ in range(m_unread):
                        cre, cim = cre - cim, cre + cim
                    ir, ii = IP[dr % 4]
                    wre = (cre * ir - cim * ii) / adm_n
                    wim = (cre * ii + cim * ir) / adm_n
                    if (are, ime) != (wre, wim):
                        law_ok = False
    ok = grip_ok and inj_ok and law_ok and zeno_ok
    check(f"full anchoring admits ONLY the identity (the Zeno "
          f"tier -- Misra-Sudarshan, cited: an observer holding "
          f"everything sees nothing) ({zeno_ok}); for a "
          f"shape-locked structure every touching-contact outcome "
          f"channel is SINGLE-PATH ({vis_channels} channels, "
          f"{inj_ok}) -- the trivially-consistent case of "
          f"decoherent histories, reached structurally (records "
          f"imply exact consistency -- Gell-Mann-Hartle strong "
          f"decoherence; environment-as-witness, Zurek, cited); "
          f"and THE READING LAW holds exactly on every channel: "
          f"amplitude = P x ((1+i)/2)^m x i^d, m = unread "
          f"singles, d = read deviations ({law_ok}) ({ok}). The "
          f"(1+i)/2-per-unread-bit factor is the spin-bath "
          f"product/visibility form (Zurek; Englert lineage, "
          f"cited) with the overlap fixed at (1+i)/2 by the "
          f"kernel; the exactness -- consistency exact, not "
          f"approximate, from a graph-readability criterion -- is "
          f"the artifact.", ok)

    print(f"\n# RESULT: {len(PASS)} passed, {len(FAIL)} failed")
    raise SystemExit(1 if FAIL else 0)
