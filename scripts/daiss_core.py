#!/usr/bin/env python3
"""
DAISS v2.2 Core
Canonical Civilization Engine

This module defines the single source of truth
for DAISS thermodynamic dynamics.
"""

import numpy as np
import networkx as nx
from collections import Counter


class DAISSCore:
    """
    Distributed Autonomous Intelligence Simulation System
    v2.2 Canonical Core
    """

    def __init__(
        self,
        N=100,
        clusters=10,
        r=0.14,
        D=0.38,
        T_target=1.0,
        seed=42,
        fork_threshold=3.0,
        s_max=5.0,
        alpha=0.20,
        beta=0.09,
    ):
        self.N = N
        self.clusters = clusters
        self.r = r
        self.D = D
        self.T_target = T_target
        self.seed = seed
        self.fork_threshold = fork_threshold
        self.s_max = s_max
        self.alpha = alpha
        self.beta = beta

        np.random.seed(seed)

        # Scale-free topology (civilization substrate)
        self.G = nx.barabasi_albert_graph(N, 3, seed=seed)

        # Node state
        self.s = np.random.normal(1.0, 0.5, N)   # freedom / energy
        self.T = np.ones(N) * T_target           # governance temperature

        # Degree-balanced clusters
        degrees = np.array([self.G.degree(n) for n in range(N)])
        order = np.argsort(-degrees)
        self.cluster_of = np.zeros(N, dtype=int)
        for i, node in enumerate(order):
            self.cluster_of[node] = i % clusters

        self.history = {
            "forks": [],
            "ternary": [],
        }

    # -----------------------------
    # Ternary State Engine
    # -----------------------------
    def ternary_state(self, s_i, T_i):
        if s_i > self.fork_threshold + 0.8:
            return -1  # Purge
        if abs(s_i - 1.0) < 0.35 and abs(T_i - self.T_target) < 0.12:
            return 0   # Equilibrium
        return 1       # Amplify

    # -----------------------------
    # Single Time Step
    # -----------------------------
    def step(self):
        new_s = self.s.copy()
        new_T = self.T.copy()

        for i in range(self.N):
            nbrs = list(self.G.neighbors(i))
            if not nbrs:
                continue

            diffusion_s = self.D * np.mean([self.s[j] - self.s[i] for j in nbrs])
            diffusion_T = self.alpha * np.mean([self.T[j] - self.T[i] for j in nbrs])

            reaction = (
                self.r * self.s[i] * (1 - self.s[i] / self.s_max)
                - self.beta * (self.T[i] - self.T_target)
            )

            new_s[i] += reaction + diffusion_s
            new_T[i] += diffusion_T + 0.5 * self.beta * (self.T_target - self.T[i])

        self.s = np.clip(new_s, 0.05, self.s_max)
        self.T = np.clip(new_T, 0.4, 2.2)

        # Fork detection (cluster-level)
        forked = set()
        for c in range(self.clusters):
            idx = np.where(self.cluster_of == c)[0]
            if np.max(self.s[idx]) > self.fork_threshold:
                forked.add(c)

        # Cooling / merge if overheated consensus
        if np.std(self.T) < 0.10:
            for c in forked:
                idx = np.where(self.cluster_of == c)[0]
                self.s[idx] = 0.55 * self.s[idx] + 0.45 * np.mean(self.s)

        # Record history
        ternary = [self.ternary_state(self.s[i], self.T[i]) for i in range(self.N)]
        counts = Counter(ternary)

        self.history["forks"].append(len(forked))
        self.history["ternary"].append({
            "+1": counts.get(1, 0) / self.N,
            "0": counts.get(0, 0) / self.N,
            "-1": counts.get(-1, 0) / self.N,
        })

    # -----------------------------
    # Run Civilization
    # -----------------------------
    def run(self, steps=1000):
        for _ in range(steps):
            self.step()
        return self.history

# --- Existing DAISSCore implementation above ---

class DAISS_Core_v2_2(DAISSCore):
    """
    Official Interface for CIFF / DOI / Zenodo.
    This class acts as the Canonical Contract for DAISS v2.2.
    """

    def heartbeat(self, steps=1000):
        # Execute the research-grade simulation
        history = self.run(steps)

        # Evaluation based on the stability of persistence (last 200 steps)
        forks_window = np.array(history["forks"][-200:])
        mean_forks = float(np.mean(forks_window))
        last_ternary = history["ternary"][-1]

        # CIFF Acceptance Criteria:
        # 1. Golden Fluctuation (2.0 - 5.0)
        # 2. Creativity (+1 ratio >= 15%)
        # 3. Immunity Control (-1 ratio <= 30%)
        is_healthy = (
            2.0 <= mean_forks <= 5.0 and
            last_ternary["+1"] >= 0.15 and
            last_ternary["-1"] <= 0.30
        )

        return {
            "status": "Healthy" if is_healthy else "Unhealthy",
            "mean_forks": mean_forks,
            "ternary": last_ternary,
            "timestamp": "2026-02-03"
        }
