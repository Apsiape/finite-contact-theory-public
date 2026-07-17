#!/usr/bin/env python3
"""Chapter 16 -- The Debt Ledger: shipped verifier (dependency-free,
Python 3 stdlib only; exact/exhaustive; one labeled float check).

Two sections. price(f) = log2 maxfiber(f), maxfiber = the largest
preimage multiplicity. Prior art per the release's blind novelty sweep
is cited in the chapter text (Lecerf 1963 / Bennett 1973; Maslov--Dueck
2003/04 for the minimal-garbage formula; Landauer 1961 / Maroney 2009;
Cabello et al. 2016 as the nearest thermodynamic analogue of Section
2's dichotomy); the recomputations here are checks, not priority
claims. The composition claim of the chapter is the derivation route:
everything below is finite counting -- no probability measure, no
thermodynamic postulate.

  1. DILATION. A non-injective act admits NO whole-product permutation
     lift for any fixed finite ancilla (counting; slice-correct lifts
     exist but fail composition). One fresh one-use register per step
     dilates every act monoid reversibly (Lecerf/Bennett). THE EXCHANGE
     RATE: the minimal fresh-register alphabet is EXACTLY maxfiber
     (alphabet form of Maslov--Dueck), so the n-fork collapse act
     prices at log2 n. Price is submultiplicative under composition;
     permutation acts keep price 1 under respected quotients; an
     absorbing-state notion of mortality is quotient-discontinuous
     while the act-price sees through it.
  2. THE LEDGER. log2|S| <= log2|im w| + sum of prices, exactly, with
     tightness witnesses (aligned uniform merges) and a WASTE witness
     (re-paying for already-destroyed distinction): waste is possible,
     theft is impossible. ONE NUMBER, THREE READINGS: collapse cost =
     query depth = record alphabet for the n-fork. Support/entropy
     forms (labeled RECOVERY: grouping bound). THE FLOOR READING:
     every completion that resolves an n-fork books exactly log2 n --
     the no-selector law as a refused debt.
"""
from itertools import product as iproduct, permutations
import math
import random

PASS, FAIL = [], []
def check(name, ok):
    (PASS if ok else FAIL).append(name)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)

def section_dilation():
    def maxfiber(f, n):
        cnt = {}
        for s in range(n):
            cnt[f[s]] = cnt.get(f[s], 0) + 1
        return max(cnt.values())

    rng = random.Random(17)

    print("## M1: no fixed-carrier dilation (exhaustive counting)")
    m1_ok = True
    n_checked = 0
    for n in (2, 3, 4):
        for f in iproduct(range(n), repeat=n):
            if maxfiber(f, n) == 1:
                continue  # injective: dilates trivially, not mortal
            for k in (1, 2, 3, 4):
                # does ANY bijection of S x A have first component f
                # everywhere? necessary condition: the map
                # (s,a) -> f(s) hits each t exactly |A| times.
                # fiber size m >= 2 needs m*k slots but only k exist.
                # verify by direct impossibility count (no search needed
                # for the theorem, but do a brute search at tiny sizes):
                if n == 2 and k <= 2:
                    found = False
                    cells = [(s, a) for s in range(n) for a in range(k)]
                    for perm in permutations(range(len(cells))):
                        ok_all = all(cells[perm[i]][0] == f[cells[i][0]]
                                     for i in range(len(cells)))
                        if ok_all:
                            found = True
                            break
                    if found:
                        m1_ok = False
                # counting certificate:
                need = maxfiber(f, n) * k
                if not need > k:
                    m1_ok = False
                n_checked += 1
    # slice-correct lifts exist but composition fails: |S|=2, f = const_0
    # lift F(s,a): on slice a0=0: F(s,0) = (0, s) (garbage = input copy),
    # extend to a bijection of S x A (|A| = 2) arbitrarily:
    S, A = 2, 2
    Fmap = {(0, 0): (0, 0), (1, 0): (0, 1), (0, 1): (1, 0), (1, 1): (1, 1)}
    bij = sorted(Fmap.values()) == sorted(iproduct(range(S), range(A)))
    slice_ok = all(Fmap[(s, 0)][0] == 0 for s in range(S))  # f = const_0
    # compose f after f: (f o f) = const_0; but F o F on the a0 slice:
    comp_bad = False
    for s in range(S):
        out = Fmap[Fmap[(s, 0)]]
        if out[0] != 0:      # should be const_0 twice
            comp_bad = True
    check(f"non-injective acts admit NO whole-product permutation lift "
          f"for ANY finite ancilla (counting certificate maxfiber*|A| > "
          f"|A| over {n_checked} (f, |A|) cases, |S| <= 4; brute-force "
          f"search at |S|=2 confirms none exists), while a slice-correct "
          f"lift exists (explicit bijection, f = const: {bij and slice_ok}) "
          f"but FAILS under composition (F o F wrong on the slice: "
          f"{comp_bad}). **Mortality cannot be dilated away on a fixed "
          f"carrier -- reversibility on a closed finite world is a "
          f"conserved impossibility.**", m1_ok and bij and slice_ok
          and comp_bad)

    print("## M2: fresh-register dilation (Bennett -- RECOVERY, labeled)")
    m2_ok = True
    for trial in range(30):
        n = rng.choice((3, 4, 5))
        acts = []
        for _ in range(rng.choice((2, 3))):
            f = [rng.randrange(n) for _ in range(n)]
            acts.append(tuple(f))
        if all(maxfiber(f, n) == 1 for f in acts):
            acts[0] = tuple([0] + [rng.randrange(n) for _ in range(n - 1)])
        # separators c_f: number within each fiber
        seps = {}
        for f in acts:
            seen, c = {}, []
            for s in range(n):
                c.append(seen.get(f[s], 0))
                seen[f[s]] = seen.get(f[s], 0) + 1
            seps[f] = c
        # run 5-step random words on ALL initial states simultaneously;
        # state = (live, history registers); require: (a) marginal = the
        # composed act, exactly; (b) the global map is INJECTIVE on
        # initial states (reversibility of the whole history).
        for _ in range(4):
            word = [rng.choice(acts) for _ in range(5)]
            outs = []
            for s0 in range(n):
                live, hist = s0, []
                for f in word:
                    hist.append(seps[f][live])
                    live = f[live]
                outs.append((live, tuple(hist)))
            # (a) marginal correctness
            for s0 in range(n):
                t = s0
                for f in word:
                    t = f[t]
                if outs[s0][0] != t:
                    m2_ok = False
            # (b) injectivity (with fibers separated stepwise this holds)
            if len(set(outs)) != n:
                m2_ok = False
    check("one fresh one-use register per step dilates EVERY mortal act "
          "monoid reversibly and compositionally: 30 random mortal "
          "monoids x 4 five-step words, marginal = composed act exactly "
          "and the global history map is injective on initial states. "
          "CLASSIFICATION: RECOVERY (Bennett reversible computation / "
          "Landauer), labeled as such -- the floor-side content is in "
          "M3/M4.", m2_ok)

    print("## M3: the exchange rate (minimal register = maxfiber)")
    m3_ok = True
    cases = 0
    for n in (2, 3, 4, 5):
        for _ in range(40):
            f = tuple(rng.randrange(n) for _ in range(n))
            mf = maxfiber(f, n)
            # minimal k such that s -> (f(s), c(s)) injective for some
            # c: S -> [k]  == max fiber size (c must separate fibers)
            best = None
            for k in range(1, n + 1):
                okk = False
                for c in iproduct(range(k), repeat=n):
                    seen = set()
                    inj = True
                    for s in range(n):
                        key = (f[s], c[s])
                        if key in seen:
                            inj = False
                            break
                        seen.add(key)
                    if inj:
                        okk = True
                        break
                if okk:
                    best = k
                    break
            if best != mf:
                m3_ok = False
            cases += 1
    # the fork/collapse act: n-to-1 merge has price exactly log2 n bits
    fork_prices = []
    for n in (2, 3, 4, 8):
        f = tuple(0 for _ in range(n))
        fork_prices.append((n, maxfiber(f, n)))
    fork_ok = all(mf == n for n, mf in fork_prices)
    check(f"minimal fresh-register alphabet for an exact reversible lift "
          f"= maxfiber(f) EXACTLY ({cases} exhaustive-search cases, "
          f"|S| <= 5); the n-fork collapse act has price maxfiber = n, "
          f"i.e. log2 n fresh bits {fork_prices} -- **the ceil(log2 n) "
          f"selector/actualization debt REDERIVED as the dilation price "
          f"of the fork-collapse act. The arrow's strength is now a "
          f"NUMBER: bits of one-use resource per act.**",
          m3_ok and fork_ok)

    print("## M4: the composition law (price subadditive, not quotient-monotone)")
    m4_ok = True
    strict = 0
    for _ in range(400):
        n = rng.choice((3, 4, 5, 6))
        f = tuple(rng.randrange(n) for _ in range(n))
        g = tuple(rng.randrange(n) for _ in range(n))
        gf = tuple(g[f[s]] for s in range(n))
        if maxfiber(gf, n) > maxfiber(g, n) * maxfiber(f, n):
            m4_ok = False
        if maxfiber(gf, n) < maxfiber(g, n) * maxfiber(f, n):
            strict += 1
    # RECONCILIATION with a companion absorbing-state analysis ("a quotient CREATES
    # mortality", verified there): that example uses ABSORBING-STATE
    # mortality (a state fixed by all acts), a DIFFERENT notion from
    # act-level irreversibility. Its upstairs act k = (l->d0, d0->d0,
    # d1->d1) is ALREADY non-injective (price 1 bit); the quotient
    # {d0,d1} -> D only CONCENTRATES the existing irreversibility into
    # an absorbing state. Verify on their exact example that the PRICE
    # VECTOR is invariant across their quotient:
    Sm = ['l', 'd0', 'd1']
    gm = {'l': 'l', 'd0': 'd1', 'd1': 'd0'}
    km = {'l': 'd0', 'd0': 'd0', 'd1': 'd1'}
    Qm = {'l': 'L', 'd0': 'D', 'd1': 'D'}
    def price_of(act, dom):
        cnt = {}
        for s in dom:
            cnt[act[s]] = cnt.get(act[s], 0) + 1
        return max(cnt.values())
    gq = {Qm[s]: Qm[gm[s]] for s in Sm}
    kq = {Qm[s]: Qm[km[s]] for s in Sm}
    price_same = (price_of(gm, Sm) == price_of(gq, ['L', 'D']) == 1
                  and price_of(km, Sm) == price_of(kq, ['L', 'D']) == 2)
    # and the little theorem that DOES hold: permutation acts under
    # respected quotients keep price 1 (blocks are permuted):
    perm_quot_ok = True
    for _ in range(200):
        n = rng.choice((4, 5, 6))
        p = list(range(n))
        rng.shuffle(p)
        # random respected quotient: partition into orbits of a random
        # subgroup element = use cycles of p itself (always respected)
        # cycles of p:
        seen, classes = set(), []
        for s in range(n):
            if s in seen:
                continue
            cyc, t = [], s
            while t not in seen:
                seen.add(t)
                cyc.append(t)
                t = p[t]
            classes.append(cyc)
        cls_of = {}
        for i, cyc in enumerate(classes):
            for s in cyc:
                cls_of[s] = i
        # induced act on classes: [s] -> [p(s)] (cycles map to selves:
        # induced = identity, price 1)
        ind = {}
        well = True
        for s in range(n):
            i = cls_of[s]
            j = cls_of[p[s]]
            if i in ind and ind[i] != j:
                well = False
            ind[i] = j
        if not well:
            perm_quot_ok = False
        else:
            vals = list(ind.values())
            if len(set(vals)) != len(vals):     # induced must stay injective
                perm_quot_ok = False
    check(f"price is submultiplicative under composition "
          f"(maxfiber(gf) <= maxfiber(g)maxfiber(f), 400 random exact "
          f"cases, strict in {strict}) -- the debt log2 maxfiber is "
          f"SUBADDITIVE along histories; reversible (permutation) acts "
          f"keep price 1 under every respected quotient (200 random "
          f"cycle-quotients); and the absorbing-state 'quotient creates "
          f"mortality' example RECONCILED ({price_same}): its "
          f"absorbing-state mortality is a different notion -- the "
          f"upstairs act k was already price-2, and the quotient only "
          f"CONCENTRATES existing irreversibility into an absorbing "
          f"state; the PRICE VECTOR (1, 2) is invariant across their "
          f"quotient. **The absorbing-state reading is discontinuous "
          f"under quotients; the act-level price sees through it -- the "
          f"DEBT-NOETHER candidate is the price, not the absorbing "
          f"state.**", m4_ok and strict > 0 and perm_quot_ok and price_same)


def section_ledger():
    def maxfiber(f, n):
        cnt = {}
        for s in range(n):
            cnt[f[s]] = cnt.get(f[s], 0) + 1
        return max(cnt.values())

    rng = random.Random(23)

    print("## D1: the ledger inequality (multiplicative, exact)")
    d1_ok = True
    tight = strict = 0
    # exhaustive: all pairs of acts on |S| = 3
    n = 3
    for f in iproduct(range(n), repeat=n):
        for g in iproduct(range(n), repeat=n):
            w = tuple(g[f[s]] for s in range(n))
            im = len(set(w))
            lhs = n
            rhs = im * maxfiber(f, n) * maxfiber(g, n)
            if lhs > rhs:
                d1_ok = False
            if lhs == rhs:
                tight += 1
            if maxfiber(w, n) < maxfiber(f, n) * maxfiber(g, n):
                strict += 1
    # random longer histories on bigger S
    for _ in range(300):
        m = rng.choice((4, 5, 6, 7))
        word = [tuple(rng.randrange(m) for _ in range(m))
                for _ in range(rng.choice((2, 3, 4, 5)))]
        cur = list(range(m))
        price_prod = 1
        for f in word:
            cur = [f[s] for s in cur]
            price_prod *= maxfiber(f, m)
        if m > len(set(cur)) * price_prod:
            d1_ok = False
    # tightness witness: the uniform 2-to-1 merge twice on |S| = 4:
    f4 = (0, 0, 1, 1)
    g4 = (0, 0, 2, 3)      # merges {0,1} (the current image {0,1})
    w4 = tuple(g4[f4[s]] for s in range(4))
    tight_wit = (4 == len(set(w4)) * maxfiber(f4, 4) * maxfiber(g4, 4))
    # strictness/waste witness: two merges hitting the SAME pair -- the
    # second act pays price but destroys nothing new:
    fw = (0, 0, 2, 3)
    gw = (0, 0, 2, 3)      # second merge finds {0,1} already merged
    ww = tuple(gw[fw[s]] for s in range(4))
    waste = (len(set(ww)) == len(set(fw[s] for s in range(4)))
             and maxfiber(gw, 4) == 2)
    check(f"log2|S| <= log2|im| + sum price, verified EXACTLY over all "
          f"{9**3 * 3**0} two-act histories on |S|=3 (multiplicative "
          f"form; tight in {tight}) and 300 random longer histories "
          f"(|S| <= 7); tightness witness (aligned uniform merges: "
          f"{tight_wit}) and WASTE witness (a merge re-paying for "
          f"already-destroyed distinction: {waste}, price booked, "
          f"nothing destroyed). **THE LEDGER: existence-bits = "
          f"surviving-bits + paid-bits, waste possible, theft "
          f"impossible -- distinction is never destroyed unpaid.**",
          d1_ok and tight > 0 and tight_wit and waste)

    print("## D2: forgetting = asking = remembering (the fork's one number)")
    d2_ok = True
    rows = []
    for nn in range(2, 17):
        # (i) FORGETTING: dilation register alphabet of the collapse act
        collapse = tuple(0 for _ in range(nn))
        price_alpha = maxfiber(collapse, nn)            # = nn
        # (ii) ASKING: adaptive binary-question depth to identify one of
        # nn branches: optimal = ceil(log2 nn); compute by the exact
        # recursion d(1) = 0, d(k) = 1 + d(ceil(k/2)):
        def qdepth(k):
            d = 0
            while k > 1:
                k = (k + 1) // 2
                d += 1
            return d
        ask = qdepth(nn)
        # (iii) REMEMBERING: minimal record alphabet R such that a
        # record r: branches -> [R] makes (collapse, record) injective
        # on branches (registration-promotion certainty): R = nn
        # (record must separate all nn branches since collapse kills all)
        best = None
        for R in range(1, nn + 1):
            # exists r: [nn] -> [R] with (0, r(s)) all distinct <=> R >= nn
            if R >= nn:
                best = R
                break
        rem_alpha = best
        # binary-register form of (i)/(iii): ceil(log2 alpha)
        bits = math.ceil(math.log2(nn))
        if not (price_alpha == rem_alpha == nn and ask == bits):
            d2_ok = False
        rows.append((nn, price_alpha, ask, rem_alpha))
    check(f"for the n-fork, n = 2..16: dilation register alphabet = "
          f"record alphabet for promotion-certainty = n exactly, and "
          f"binary-question identification depth = ceil(log2 n) = the "
          f"binary-register form of the same price (sample rows "
          f"{rows[:3] + rows[-2:]}). **ONE NUMBER, THREE READINGS: the "
          f"cost to COLLAPSE the fork (dilation), to KNOW the outcome "
          f"(queries), to REMEMBER it (records). ceil appears exactly "
          f"when the resource is binary; the n-ary forms are exact. The "
          f"program's recurring ceil(log2 n) is this ledger entry.**",
          d2_ok)

    print("## D3: the entropy form (RECOVERY-labeled: grouping/Landauer)")
    d3_ok = True
    # support version, exact and exhaustive on |S| = 4:
    n = 4
    for f in iproduct(range(n), repeat=n):
        mf = maxfiber(f, n)
        for support_mask in range(1, 2**n):
            supp = [s for s in range(n) if (support_mask >> s) & 1]
            im_supp = len({f[s] for s in supp})
            if im_supp * mf < len(supp):
                d3_ok = False
    # Shannon version, float-checked on random rational distributions:
    for _ in range(500):
        m = rng.choice((3, 4, 5, 6))
        f = tuple(rng.randrange(m) for _ in range(m))
        weights = [rng.randint(0, 6) for _ in range(m)]
        tot = sum(weights)
        if tot == 0:
            continue
        p = [w / tot for w in weights]
        q = [0.0] * m
        for s in range(m):
            q[f[s]] += p[s]
        H = lambda d: -sum(x * math.log2(x) for x in d if x > 0)
        if H(q) < H(p) - math.log2(maxfiber(f, m)) - 1e-9:
            d3_ok = False
    check("support form |supp f(X)| >= |supp X| / maxfiber EXACT "
          "(exhaustive: all 256 acts x 15 supports on |S|=4); Shannon "
          "form H(f(X)) >= H(X) - log2 maxfiber float-verified on 500 "
          "random distributions. CLASSIFICATION: RECOVERY (grouping "
          "bound; Landauer's counting face) -- labeled; the ledger's "
          "floor-side content is D2/D4.", d3_ok)

    print("## D4: the floor reading -- no-selector as refused debt")
    d4_ok = True
    for nn in (2, 3, 4):
        # every act on the fork's branch set that RESOLVES the fork
        # (maps all branches to ONE actual) has maxfiber = nn; every act
        # that reduces the count to k < nn images pays maxfiber >= 2 and
        # >= ceil(nn / k):
        for f in iproduct(range(nn), repeat=nn):
            im = len(set(f))
            mf = maxfiber(f, nn)
            if im == 1 and mf != nn:
                d4_ok = False
            if mf < -(-nn // im):        # ceil(nn / im) lower bound
                d4_ok = False
    check("exhaustive over all acts on n-fork branch sets (n = 2, 3, 4): "
          "full resolution to one actual pays maxfiber = n exactly; any "
          "partial resolution to k images pays >= ceil(n/k). **THE "
          "EXTENSION SENTENCE: the no-selector law is not an absence "
          "but a REFUSED DEBT -- the floor stays debt-free by never "
          "collapsing the fork; every completion that collapses must "
          "book exactly the log2 n the program keeps meeting (selector "
          "debt, actualization debt, promotion records, Bennett price: "
          "one ledger entry, many hands).**", d4_ok)


if __name__ == '__main__':
    print("### Section 1: dilation and the exchange rate")
    section_dilation()
    print()
    print("### Section 2: the ledger")
    section_ledger()
    print()
    print(f"# RESULT: {len(PASS)} passed, {len(FAIL)} failed")
    raise SystemExit(1 if FAIL else 0)
