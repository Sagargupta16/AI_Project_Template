from __future__ import annotations

import logging
from pathlib import Path

import pandas as pd

logger = logging.getLogger(__name__)


def load_data(path: Path | str) -> pd.DataFrame:
    """Load data from a file path. Supports CSV, Excel, Parquet."""
    path = Path(path)
    logger.info("Loading data from %s", path)

    match path.suffix.lower():
        case ".csv":
            return pd.read_csv(path)
        case ".xlsx" | ".xls":
            return pd.read_excel(path)
        case ".parquet":
            return pd.read_parquet(path)
        case _:
            msg = f"Unsupported file format: {path.suffix}"
            raise ValueError(msg)


def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """Basic preprocessing pipeline. Customize for your project."""
    logger.info("Preprocessing data with %d rows", len(df))

    # Drop duplicates
    df = df.drop_duplicates()

    # Drop rows where all values are NaN
    df = df.dropna(how="all")

    logger.info("After preprocessing: %d rows", len(df))
    return df
