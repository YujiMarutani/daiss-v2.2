#!/usr/bin/env python3
"""
DAISS v2.2 - Thermodynamic Survival Proof Verifier
Gatekeeper for CIFF (Continuous Integration of Formal Fragments)
"""

import os
import sys
import numpy as np
import yaml

# ① Robust Import Logic
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

try:
    from daiss_core import DAISSCore
except ImportError as e:
    print(f"CRITICAL ERROR: Could not find daiss_core.py in {BASE_DIR}")
    print(f"Current sys.path: {sys.path}")
    sys.exit(1)

def run_verification():
    print("--- DAISS v2.2: Initiating Civilizational Health Check ---")
    
    # Target Coordinates: The Heartbeat of Civilization
    core = DAISSCore(r=0.14, D=0.38, seed=42)
    history = core.run(steps=1000)
    
    # ② History Key Existence Check
    required_keys = {"forks", "ternary"}
    missing = required_keys - history.keys()
    if missing:
        print(f"FAILED: Integrity Breach. Missing history keys: {missing}")
        sys.exit(1)
    
    # Evaluation: Stability of Persistence (Last 200 steps)
    final_forks = np.mean(history["forks"][-200:])
    last_ternary = history["ternary"][-1]
    
    print(f"Observed Mean Forks (Persistence): {final_forks:.2f}")
    print(f"Ternary Distribution: {last_ternary}")

    # --- Acceptance Criteria (The Gatekeeper) ---
    
    # 1. Vitality & Rhythm (Golden Fluctuation Zone)
    if not (2.0 <= final_forks <= 5.0):
        print(f"FAILED: Rhythm Out of Range. Value: {final_forks:.2f}")
        sys.exit(1)
        
    # 2. Distribution Sanity (Creativity & Immunity)
    if last_ternary['+1'] < 0.15:
        print(f"FAILED: Stagnation. Amplify ratio ({last_ternary['+1']:.2%}) too low.")
        sys.exit(1)
    if last_ternary['-1'] > 0.30:
        print(f"FAILED: Hyper-reaction. Purge ratio ({last_ternary['-1']:.2%}) too high.")
        sys.exit(1)

    # --- ③ Behavior on Success: Export Artifact ---
    print("\nSUCCESS: Proof of Life confirmed at Golden Coordinates.")
    
    snapshot = {
        "metadata": {
            "version": "v2.2",
            "coordinates": {"r": 0.14, "D": 0.38},
            "protocol": "CIFF-Verified-Stability",
            "timestamp": "2026-02-03"
        },
        "evidence": {
            "mean_forks_persistence": float(final_forks),
            "final_ternary_ratio": last_ternary
        }
    }
    
    # Ensure output directory exists
    os.makedirs("output", exist_ok=True)
    output_path = "output/verified_snapshot.yaml"
    
    with open(output_path, "w") as f:
        # sort_keys=False preserves logical readability for Zenodo/Human eyes
        yaml.dump(snapshot, f, sort_keys=False)
    
    print(f"Artifact Frozen: {output_path}")
    sys.exit(0)

if __name__ == "__main__":
    run_verification()
