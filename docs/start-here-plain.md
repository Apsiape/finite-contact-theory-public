# Start here if you're not a physicist

You don't need any physics to read this page. It explains, in plain
English, what this project asks, what it actually found, why you might
trust it, and where to go next.

## 1. The one question

Grow a tiny universe from a single, minimal rule and let it run. Some
features that show up will be *forced* — they'd appear in any universe
grown that way, no matter the details. Other features are *particular
to ours* — accidents of our starting point that could have gone another
way.

The whole program asks one question: **which is which?** Which features
of physical law are inevitable in any universe built from a minimal
rule, and which are peculiar to the one we happen to live in? The goal
is not a philosophy essay but a sorted table — the authors call it a
*taxonomy of inevitability*.

The single rule is deliberately spare: a finite thing touches something
larger than it can fully take in, and the contact leaves a mark that can
be used once. From that, and careful counting, universes are grown and
measured.

## 2. What was actually found — honestly tiered

The results come in three tiers, and the project is scrupulous about
keeping them apart.

**Recovered (the main result, and counted as success).** Starting from
nothing but counting — no Hilbert space, no probability, no spacetime
assumed — the program re-derives large parts of the standard machinery
of quantum mechanics. The Born rule (how quantum probabilities are
computed), and other well-known structures, fall out of the minimal
rule rather than being put in by hand.

Why call *reproducing known physics* a success rather than a letdown?
Because the point was never to overturn quantum mechanics — it was to
find out whether that machinery is *inevitable*. If a piece of standard
physics can be re-derived from a rule that never assumed it, that is
direct evidence the piece is forced, not arbitrary. A recovery here
means: known physics, obtained from strictly less. That is the win
condition, not a concession.

**Predicted (two registered bets, labeled as bets).** In two places the
toy models point *outside* what standard quantum mechanics allows. Both
are written down in advance — protocol, expected numbers, and the
conditions that would kill them frozen before anything is computed — and
both are labeled explicitly as *bets, not discoveries*.

The sharpest is the **tritter bet**: a specific three-photon experiment
in which this theory predicts a particular combination of raw detector
counts falling *below* a value (two-thirds) that standard quantum
mechanics says nothing can cross. The odds are written down, not
claimed as a win — whether nature actually contains this effect is
untested, the likeliest physical home is exotic matter rather than
photons, and the decisive check still needs a dedicated experiment and
outside quantum-optics review. It is a registered wager on a number,
nothing more.

**Open (deliberately not answered).** The models set up *what can
happen* but say nothing about *which thing does* happen. In the
project's own words, **the rules stage a menu; nothing in the rules
picks from it.** The list of possible outcomes is forced; the selection
of one actual outcome is not derived, on purpose. This is treated as an
honest boundary of the theory, not a gap to paper over.

## 3. Why trust any of it

The ambition is large, so the rules are strict — and the honesty
apparatus is the reason to take the work seriously:

- **Everything runs.** Every result ships as a plain script anyone can
  execute — no special software, exact arithmetic, the flagship path in
  about a minute. You can check the numbers yourself instead of taking
  anyone's word.
- **Predictions are frozen first.** Expected numbers are written into
  the design document *before* the engines run. The worlds regularly
  beat the authors' guesses, and a lost bet is printed, not buried.
- **The project kills its own claims, in public.** The
  [correction ledger](correction-ledger.md) records **24** claims that
  were killed, demoted, or narrowed — including some of the authors'
  prettiest ideas. One especially clean example: a proposed universal
  theorem was caught failing by a margin of −495 during pre-publication
  review, and that counterexample now ships permanently as a test so the
  mistake can never quietly return.

A theory that discards its own best ideas when the evidence turns is
*more* trustworthy, not less. The kill-count is a health metric: it
shows the claims that survived did so because they were checked hard and
held, not because no one looked.

## 4. How this was made

The author's note in the [README](../README.md) says it plainly: the
work is by someone who is **not a physicist** — an outsider working in
AI and software — pursued over about **seven months** using an unusual
setup in which **several AI models work together as a research team**,
pointed at the founding question. An AI-assisted theory from outside the
field is easy to doubt; that is exactly why everything here is scoped,
labeled, and runnable. (Nothing beyond what that note states is claimed
here.)

## 5. Where to go next

Pick by curiosity:

- **Run something.** Follow *Run it yourself* in the
  [README](../README.md#run-it-yourself) — one command, about a minute.
- **Read one theorem.** [Chapter 8](../papers/08-nonexact-return/paper.md):
  the Born rule and a companion no-go result, co-resident on one finite
  object — the sharpest single recovery.
- **Hunt a problem.** The [correction ledger](correction-ledger.md) and
  its reopening protocol, plus the open experiment in
  [Chapter 10](../papers/10-negative-gram-holonomy/paper.md) — the
  tritter bet, still awaiting a lab.
- **The philosophy.** [Chapter 1](../papers/finite-contact-theory-v0.1.md):
  what "one-use contact" means and why it stages a menu it cannot pick
  from. The [glossary](glossary.md) keeps every term plain.
