"""Data loading utilities for the fraud detection project."""

from pathlib import Path
import pandas as pd

# Project root = parent of the src/ folder = .../fraud-detector/
PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_CSV_PATH = PROJECT_ROOT / "data" / "raw" / "creditcard.csv"

# Expected data contract — used for validation
EXPECTED_SHAPE = (284807, 31)
EXPECTED_FRAUD_COUNT = 492


def load_raw(validate: bool = True) -> pd.DataFrame:
    """Load the raw credit card fraud dataset.

    Args:
        validate: If True, run data contract assertions after loading.
                  Set to False only in performance-critical contexts.

    Returns:
        DataFrame with 284,807 rows and 31 columns.

    Raises:
        FileNotFoundError: If the CSV doesn't exist at RAW_CSV_PATH.
        AssertionError: If validate=True and the data doesn't match the contract.
    """
    if not RAW_CSV_PATH.exists():
        raise FileNotFoundError(
            f"Raw CSV not found at {RAW_CSV_PATH}. "
            "Download from Kaggle and place in data/raw/."
        )

    df = pd.read_csv(RAW_CSV_PATH)

    if validate:
        assert df.shape == EXPECTED_SHAPE, (
            f"Wrong shape: expected {EXPECTED_SHAPE}, got {df.shape}"
        )
        assert df.isnull().sum().sum() == 0, "Unexpected nulls in dataset"
        assert df['Class'].sum() == EXPECTED_FRAUD_COUNT, (
            f"Wrong fraud count: expected {EXPECTED_FRAUD_COUNT}, "
            f"got {df['Class'].sum()}"
        )
        assert set(df['Class'].unique()) == {0, 1}, (
            f"Unexpected class values: {df['Class'].unique()}"
        )
        assert df['Amount'].min() >= 0, (
            f"Negative transaction amount found: {df['Amount'].min()}"
        )

    return df