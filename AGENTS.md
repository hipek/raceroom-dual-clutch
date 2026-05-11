# RaceRoom Dual Clutch — Agent Summary

**What:** Joystick Gremlin Python plugin + guide for dual-clutch launch in RaceRoom Racing Experience.

**Problem:** Racing wheels lack analog paddles for dual-clutch. Solution uses clutch pedal + wheel button.

**How it works:**
- `dual_clutch.py` maps physical clutch pedal + button to vJoy virtual axis
- Button held → vJoy clutch = 100% (clutch disengaged, full throttle rev)
- Button released → vJoy clutch snaps back to pedal position (bite point hold)
- Configurable via Joystick Gremlin UI variables

**Stack:** Python, Joystick Gremlin plugin API, vJoy, Windows-only

**Codebase:** Single file (`dual_clutch.py`, ~90 LOC), README with install guide, dead LICENSE file

**State:** Stable, no recent activity. One feature script, no tests, no CI.
