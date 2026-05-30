"""Reusable modelling pieces for the fraud detector.

  1. temporal_split  - train on the past, test on the future. No shuffling.
  2. build_baseline  - logistic regression: the bar XGBoost must beat.
  3. build_xgb       - gradient-boosted trees, weighted for the rare fraud class.

Imbalance handled WITHOUT resampling/SMOTE:
  - LogisticRegression via class_weight="balanced"
  - XGBoost via scale_pos_weight (= n_legit / n_fraud)
Reweighting the loss is cleaner than resampling and avoids leakage.
"""
from __future__ import annotations
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from xgboost import XGBClassifier

TARGET = "Class"
DATE_COL = "Time"


def feature_columns(df: pd.DataFrame) -> list[str]:
    """Everything that is not the label or the time axis."""
    return [c for c in df.columns if c not in (TARGET, DATE_COL)]


def temporal_split(df: pd.DataFrame, train_fraction: float = 0.80):
    """Earliest train_fraction of rows (by Time) -> train, the rest -> test.

    Random shuffling would let the model train on future transactions to
    predict past ones - temporal leakage that inflates the score. The assert
    is the tripwire: any time overlap means leakage slipped in.
    """
    df_sorted = df.sort_values(DATE_COL).reset_index(drop=True)
    cut = int(len(df_sorted) * train_fraction)
    train, test = df_sorted.iloc[:cut], df_sorted.iloc[cut:]
    assert test[DATE_COL].min() >= train[DATE_COL].max(), "TIME OVERLAP = leakage!"
    return train, test


def build_baseline() -> Pipeline:
    """Logistic regression baseline. NEEDS scaling (linear model).
    class_weight='balanced' makes it attend to the rare fraud class."""
    return Pipeline([
        ("scaler", StandardScaler()),
        ("model", LogisticRegression(max_iter=2000, class_weight="balanced", n_jobs=-1)),
    ])


def build_xgb(y_train: pd.Series) -> XGBClassifier:
    """XGBoost. NO scaler - trees split on thresholds, so scale is irrelevant.
    scale_pos_weight tilts the loss toward the rare positive (fraud) class."""
    n_neg = int((y_train == 0).sum())
    n_pos = int((y_train == 1).sum())
    pos_weight = n_neg / max(n_pos, 1)
    return XGBClassifier(
        n_estimators=300, max_depth=4, learning_rate=0.1,
        scale_pos_weight=pos_weight, eval_metric="aucpr",
        n_jobs=-1, random_state=42,
    )
