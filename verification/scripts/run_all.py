#!/usr/bin/env python3
"""Run the shipped public verification subset."""

from __future__ import annotations

import subprocess
import sys
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
]


def main() -> int:
    for script in SCRIPTS:
        path = HERE / script
        print("=" * 78)
        print(f"running {path.name}")
        proc = subprocess.run([sys.executable, str(path)], check=False)
        if proc.returncode != 0:
            print(f"FAILED: {path.name} exited {proc.returncode}")
            return proc.returncode
    print("=" * 78)
    print("ALL SHIPPED VERIFICATION: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
