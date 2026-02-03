#!/usr/bin/env python3
"""
DAISS v2.2 - CIFF Thermodynamic Survival Proof Verifier
"""

import os
import sys
import yaml
import numpy as np

# Set import path
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
if CURRENT_DIR not in sys.path:
    sys.path.insert(0, CURRENT_DIR)

from daiss_core import DAISS_Core_v2_2

def verify():
    core = DAISS_Core_v2_2(r=0.14, D=0.38)
    result = core.heartbeat(steps=1000)
    
    if result["status"] == "Healthy":
        print("SUCCESS: Civilization Verified.")
        
        # --- THE FIX: Create the 'output' folder automatically ---
        os.makedirs("output", exist_ok=True)
        
        # Save the evidence into the 'output' folder
        with open("output/verified_snapshot.yaml", "w") as f:
            yaml.dump(result, f, sort_keys=False)
        sys.exit(0)
    else:
        print("FAILED: Civilization Unhealthy.")
        sys.exit(1)

if __name__ == "__main__":
    verify()
