"""Cost-based evaluation: price predictions in pounds, find the cheapest threshold.

Money model: a missed fraud (false negative) costs cost_fn pounds, a false alarm
(false positive) costs cost_fp pounds. Defaults are 150 and 5 (a 30:1 ratio).
"""
from __future__ import annotations
import numpy as np


def cost_at_threshold(y_true, y_proba, threshold, cost_fn=150, cost_fp=5):
    """Total pounds lost if we block everything scoring >= threshold."""
    y_true = np.asarray(y_true)                 # be safe: plain arrays, no index surprises
    y_pred = (y_proba >= threshold).astype(int) # scores -> yes/no fraud decisions
    fn = int(((y_true == 1) & (y_pred == 0)).sum())  # real fraud we missed
    fp = int(((y_true == 0) & (y_pred == 1)).sum())  # legit we wrongly blocked
    return fn * cost_fn + fp * cost_fp


def sweep_costs(y_true, y_proba, cost_fn=150, cost_fp=5, n=99):
    """Try n thresholds from 0.01 to 0.99; return (thresholds, cost_of_each)."""
    thresholds = np.linspace(0.01, 0.99, n)
    costs = np.array([cost_at_threshold(y_true, y_proba, t, cost_fn, cost_fp)
                      for t in thresholds])
    return thresholds, costs


def best_threshold_by_cost(y_true, y_proba, cost_fn=150, cost_fp=5):
    """The cheapest threshold and its cost."""
    thresholds, costs = sweep_costs(y_true, y_proba, cost_fn, cost_fp)
    i = int(np.argmin(costs))          # position of the cheapest
    return float(thresholds[i]), int(costs[i])
