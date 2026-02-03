#!/usr/bin/env python3
"""
DAISS v2.2 - CIFF Thermodynamic Survival Proof Verifier
"""

import os
import sys
import numpy as np
import yaml

# Robust Import Logic
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

try:
    from daiss_core import DAISSCore
except ImportError:
    print("CRITICAL ERROR: daiss_core.py not found.")
    sys.exit(1)

def verify():
    print("Executing DAISS v2.2 Verification...")
    core = DAISSCore(r=0.14, D=0.38)
    history = core.run(steps=1000)
    
    avg_forks = np.mean(history["forks"][-200:])
    last_dist = history["ternary"][-1]
    
    print(f"Mean Forks: {avg_forks:.2f}")
    print(f"Final Distribution: {last_dist}")

    # Success Criteria (Strict yet realistic)
    if 1.0 <= avg_forks <= 10.0 and last_dist["+1"] >= 0.10:
        print("SUCCESS: Civilizational Stability Verified.")
        # Create the missing 'output' directory
        os.makedirs("output", exist_ok=True)
        
        snapshot = {
            "status": "verified",
            "metrics": {"forks": float(avg_forks), "dist": last_dist}
        }
        with open("output/verified_snapshot.yaml", "w") as f:
            yaml.dump(snapshot, f, sort_keys=False)
        sys.exit(0)
    else:
        print("FAILED: Critical Instability.")
        sys.exit(1)

if __name__ == "__main__":
    verify()
