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
