# Verification Scripts

This directory contains the shipped public verification subset for v0.1.

Run all shipped scripts:

```powershell
python verification\scripts\run_all.py
```

Current scripts:

- `no_jam_open_rule.py` - public no-jam/open fresh-mark core.
- `frequency_bridge_exchangeable.py` - exact fixed-fork frequency bridge core.
- `native_lift_binary_bell.py` - exact binary-Bell native-lift identity core.
- `run_all.py` - runs all shipped scripts.

Held held-material scripts remain split: general selector, cross-site,
q >= 3, CHSH-weight, and unbanked certificate scripts are not admitted here.
