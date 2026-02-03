#!/usr/bin/env python3
"""
DAISS v2.2 - CIFF Thermodynamic Survival Proof Verifier
Strictly aligned with DAISS_Core_v2_2 implementation.
"""

import os
import sys
import numpy as np
import yaml

# Path resolution to find daiss_core.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

try:
    # Importing the specific class name from your repository
    from daiss_core import DAISS_Core_v2_2
except ImportError as e:
    print(f"CRITICAL ERROR: {e}")
    sys.exit(1)

def verify():
    print("Executing DAISS v2.2 Verification...")
    
    # Initialize the core as defined in your repository
    core = DAISS_Core_v2_2(r=0.14, D=0.38)
    
    # Execute the simulation using the correct method name: 'heartbeat'
    result = core.heartbeat(steps=1000)
    
    print(f"Simulation Result Status: {result['status']}")
    print(f"Metrics: {result}")

    # Success Criteria based on the 'Healthy' status returned by your core
    if result["status"] == "Healthy":
        print("SUCCESS: Civilizational Stability Verified.")
        
        # Ensure the output directory for GitHub Actions exists
        os.makedirs("output", exist_ok=True)
        
        snapshot = {
            "version": "v2.2",
            "coordinates": {"r": 0.14, "D": 0.38},
            "metrics": result,
            "timestamp": "2026-02-03"
        }
        
        # Save the evidence for Zenodo/DOI
        with open("output/verified_snapshot.yaml", "w") as f:
            yaml.dump(snapshot, f, sort_keys=False)
            
        print("Artifact saved: output/verified_snapshot.yaml")
        sys.exit(0)
    else:
        print("FAILED: Critical Instability Detected.")
        sys.exit(1)

if __name__ == "__main__":
    verify()
