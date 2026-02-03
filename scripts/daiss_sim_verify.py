import os
import sys
import numpy as np
import yaml

# --- (Existing simulation logic above) ---

# --- Behavior on Success: Export Verified Fragment ---
print("\nSUCCESS: Proof of Life confirmed. Generating Verified Fragment...")

# Ensure the "organ" directory exists for the CI artifact
os.makedirs("output", exist_ok=True)

snapshot = {
    "metadata": {
        "version": "v2.2",
        "coordinates": {"r": 0.14, "D": 0.38},
        "status": "Verified: Stable Fluctuation",
        "timestamp": "2026-02-03"
    },
    "final_metrics": {
        "mean_forks": float(final_forks),
        "ternary_distribution": last_ternary
    }
}

# The path must strictly match the CI workflow's expectation
with open("output/verified_snapshot.yaml", "w") as f:
    yaml.dump(snapshot, f, sort_keys=False)

print("Artifact saved: output/verified_snapshot.yaml")
sys.exit(0)
