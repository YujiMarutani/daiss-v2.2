#!/usr/bin/env python3
"""
DAISS v2.2 - CIFF Thermodynamic Survival Proof Verifier
Strictly aligned with DAISS_Core_v2_2
"""

import os
import sys
import numpy as np
import yaml

# Path resolution
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

# Import the class name as defined in your daiss_core.py
try:
    from daiss_core import DAISS_Core_v2_2
except ImportError as e:
    print(f"CRITICAL ERROR: {e}")
    sys.exit(1)

def verify():
    print("Executing DAISS v2.2 Verification...")
    
    # Matching the class name in your repository
    core = DAISS_Core_v2_2(r=0.14, D=0.38)
    
    # Use the heartbeat method as defined in your daiss_core.py
    result = core.heartbeat(steps=1000)
    
    print(f"Simulation Status: {result['status']}")
    print(f"Final Distribution: {result}")

    # Success Criteria
    if result["status"] == "Healthy":
        print("SUCCESS: Civilizational Stability Verified.")
        os.makedirs("output", exist_ok=True)
        
        snapshot = {
            "version": "v2.2",
            "coordinates": {"r": 0.14, "D": 0.38},
            "metrics": result,
            "timestamp": "2026-02-03"
        }
        with open("output/verified_snapshot.yaml", "w") as f:
            yaml.dump(snapshot, f, sort_keys=False)
        sys.exit(0)
    else:
        print("FAILED: Critical Instability.")
        sys.exit(1)

if __name__ == "__main__":
    verify()
