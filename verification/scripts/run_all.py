#!/usr/bin/env python3
"""Run the shipped public verification.

Default: run all scripts in parallel with per-script progress output.
  python run_all.py            # full suite, parallel
  python run_all.py --fast     # curated flagship subset (about a minute)
  python run_all.py --serial   # full suite, one at a time
"""

from __future__ import annotations

import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path


HERE = Path(__file__).resolve().parent
SCRIPTS = [
    "no_jam_open_rule.py",
    "frequency_bridge_exchangeable.py",
    "rational_born_gluing.py",
    "chsh_pell_boundary.py",
    "native_lift_binary_bell.py",
    "exact_gap_certificate.py",
    "identifiability_debt_calculus.py",
    "inquiry_calculus.py",
    "becoming_webs.py",
    "floor_engine_measurements.py",
    "nonexact_return_reconstruction.py",
    "multifloor_worldweave.py",
    "forcing_audit.py",
    "wcd_actualization.py",
    "negative_gram_holonomy.py",
    "mixed_state_exclusion.py",
    "count_regions.py",
    "floor_to_interface.py",
    "atlas_of_floors.py",
    "ladder_of_scars.py",
    "debt_ledger.py",
    "mint_and_bill.py",
    "emergent_hierarchy.py",
    "seventh_attempt.py",
    "observers_price.py",
    "genesis_of_space.py",
    "price_of_chance.py",
    "decay_of_worlds.py",
    "particles_of_floor.py",
    "the_up.py",
    "habitability.py",
    "floor_thermodynamics.py",
    "maintained_structures.py",
    "two_kinds_of_the_given.py",
    "where_i_lives.py",
    "the_reading_law.py",
    "the_coat_and_the_count.py",
    "the_codes_of_the_coat.py",
    "pin_lemma.py",
    "stratified_sector.py",
    "coat_composition.py",
    "actuality_protocol.py",
    "alien_coat.py",
    "alien_reading.py",
    "permission_map.py",
    "grammar_closure.py",
    "sequence_grammar.py",
    "mortal_observer.py",
    "breathing_floor.py",
    "two_switches.py",
    "fourth_column.py",
    "controls_engine.py",
    "phase_hunt.py",
    "fourth_table.py",
    "critical_corner.py",
    "minimal_pair.py",
    "observer_corner.py",
    "quantum_dividend.py",
    "third_root.py",
    "sixfold_coat.py",
    "harmonic_law.py",
    "octave_law.py",
    "rf_boundary.py",
    "causal_ceiling_family.py",
    "amalgamation_boundary.py",
    "admission_forks.py",
    "obstruction_spectrum.py",
    "carrier_anatomy.py",
    "fixed_point_registry.py",
    "ledger_books.py",
    "valuation_prices.py",
    "spine_forks.py",
    "twisted_worlds.py",
    "born_price.py",
    "verify_62_equality.py",
    "verify_63_charge.py",
    "verify_64_tower.py",
    "verify_65_e8.py",
    "verify_66_carry.py",
    "verify_67_chromatic.py",
]

# The curated flagship path: one representative exact result per major line,
# chosen to finish in about a minute on an ordinary machine.
FAST = [
    "no_jam_open_rule.py",
    "rational_born_gluing.py",
    "chsh_pell_boundary.py",
    "exact_gap_certificate.py",
    "nonexact_return_reconstruction.py",
    "negative_gram_holonomy.py",
    "mixed_state_exclusion.py",
    "rf_boundary.py",
    "causal_ceiling_family.py",
    "admission_forks.py",
    "spine_forks.py",
    "born_price.py",
]


def run_one(script: str) -> tuple[str, int, float, str]:
    path = HERE / script
    t0 = time.time()
    proc = subprocess.run(
        [sys.executable, str(path)], check=False,
        capture_output=True, text=True,
    )
    dt = time.time() - t0
    tail = (proc.stdout or "").strip().splitlines()
    last = tail[-1] if tail else ""
    return script, proc.returncode, dt, last


def main() -> int:
    args = set(sys.argv[1:])
    scripts = FAST if "--fast" in args else SCRIPTS
    serial = "--serial" in args
    total = len(scripts)
    label = "fast path" if "--fast" in args else "full suite"
    print(f"running the {label}: {total} scripts, "
          f"{'serial' if serial else 'parallel'}")
    t0 = time.time()
    failures = []
    done = 0

    def report(script, code, dt, last):
        nonlocal done
        done += 1
        mark = "PASS" if code == 0 else f"FAIL ({code})"
        print(f"[{done}/{total}] {script:<38} {mark:>9}  {dt:5.1f}s  {last}")
        if code != 0:
            failures.append(script)

    if serial:
        for s in scripts:
            report(*run_one(s))
    else:
        with ThreadPoolExecutor(max_workers=8) as pool:
            futures = {pool.submit(run_one, s): s for s in scripts}
            for fut in as_completed(futures):
                report(*fut.result())

    dt = time.time() - t0
    print("=" * 78)
    if failures:
        print(f"FAILED ({len(failures)}): " + ", ".join(failures))
        return 1
    print(f"ALL SHIPPED VERIFICATION: PASS  ({total} scripts, {dt:.0f}s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
