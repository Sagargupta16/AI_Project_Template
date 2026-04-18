from __future__ import annotations

import logging

import pandas as pd

logger = logging.getLogger(__name__)


def build_features(df: pd.DataFrame) -> pd.DataFrame:
    """Build features from preprocessed data. Customize for your project."""
    logger.info("Building features from %d rows", len(df))

    # Example: add your feature engineering here
    # df["new_feature"] = df["col_a"] * df["col_b"]

    return df
