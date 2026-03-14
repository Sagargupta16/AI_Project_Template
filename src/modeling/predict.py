from __future__ import annotations

import logging
from pathlib import Path

import joblib
import pandas as pd

logger = logging.getLogger(__name__)


def load_model(path: Path | str):
    """Load a trained model from disk."""
    path = Path(path)
    logger.info("Loading model from %s", path)
    return joblib.load(path)


def make_prediction(model, data: pd.DataFrame) -> pd.Series:
    """Run prediction using a trained model."""
    logger.info("Making predictions on %d samples", len(data))
    return pd.Series(model.predict(data))
