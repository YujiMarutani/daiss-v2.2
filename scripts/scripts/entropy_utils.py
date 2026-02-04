import numpy as np

def compute_v1_3_metrics(current_idea, context_history):
    """
    Compute CIFF v1.3 metrics:
    - E_t: Semantic Radius (distance from context centroid)
    - R_t: Kripkean Robustness (inverse variance under perturbation)
    """

    # Semantic Radius (E_t)
    centroid = np.mean(context_history, axis=0)
    E_t = float(np.linalg.norm(current_idea - centroid))

    # Kripkean Robustness (R_t)
    perturbations = context_history - current_idea
    variance = np.mean(np.linalg.norm(perturbations, axis=1))
    R_t = float(1.0 / (variance + 1e-6))

    return {
        "E_t": E_t,
        "R_t": R_t
    }
fix: add entropy_utils for CIFF v1.3 protocol
