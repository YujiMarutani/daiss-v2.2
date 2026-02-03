#!/usr/bin/env python3
"""
DAISS v2.2 - CIFF Thermodynamic Survival Proof Verifier
Final Path-Aligned Edition
"""

import os
import sys
import yaml
import numpy as np

# 1. Path Resolution: Force Python to find scripts/daiss_core.py
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(CURRENT_DIR) # One level up to Root
if CURRENT_DIR not in sys.path:
    sys.path.insert(0, CURRENT_DIR)

from daiss_core import DAISS_Core_v2_2

def verify():
    print("Initiating CIFF Verification...")
    core = DAISS_Core_v2_2(r=0.14, D=0.38)
    result = core.heartbeat(steps=1000)
    
    if result["status"] == "Healthy":
        print(f"SUCCESS: System is Healthy (Mean Forks: {result['mean_forks']:.2f})")
        
        # 2. THE FINAL FIX: Create 'output' folder at the Repository Root
        output_dir = os.path.join(REPO_ROOT, "output")
        os.makedirs(output_dir, exist_ok=True)
        
        # Save the evidence where CIFF expects it
        output_path = os.path.join(output_dir, "verified_snapshot.yaml")
        with open(output_path, "w") as f:
            yaml.dump(result, f, sort_keys=False)
            
        print(f"Artifact successfully frozen at: {output_path}")
        sys.exit(0)
    else:
        print(f"FAILED: System is {result['status']}.")
        sys.exit(1)

if __name__ == "__main__":
    verify()
