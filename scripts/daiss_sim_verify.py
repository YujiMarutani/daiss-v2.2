import os
import sys
import yaml
import numpy as np

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

from daiss_core import DAISS_Core_v2_2

def verify():
    print("Initiating CIFF Verification...")
    core = DAISS_Core_v2_2()
    result = core.heartbeat()
    
    if result["status"] == "Healthy":
        print(f"SUCCESS: System is Healthy (Mean Forks: {result['mean_forks']:.2f})")
        os.makedirs("output", exist_ok=True)
        with open("output/verified_snapshot.yaml", "w") as f:
            yaml.dump(result, f, sort_keys=False)
        sys.exit(0)
    else:
        print("FAILED: System Unhealthy.")
        sys.exit(1)

if __name__ == "__main__":
    verify()
