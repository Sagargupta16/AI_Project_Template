from __future__ import annotations

import logging
from pathlib import Path

import joblib
import pandas as pd
from sklearn.model_selection import train_test_split

from src.config import Config

logger = logging.getLogger(__name__)


def train_model(
    df: pd.DataFrame,
    target_column: str = "target",
    config: Config | None = None,
):
    """Train a model on the given data. Returns the trained model."""
    config = config or Config()
    logger.info("Training model on %d samples", len(df))

    X = df.drop(columns=[target_column])
    y = df[target_column]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=config.test_size, random_state=config.random_seed
    )

    # Replace with your model of choice
    from sklearn.ensemble import RandomForestClassifier

    model = RandomForestClassifier(random_state=config.random_seed)
    model.fit(X_train, y_train)

    score = model.score(X_test, y_test)
    logger.info("Test accuracy: %.4f", score)

    return model


def save_model(model, path: Path | str) -> None:
    """Save a trained model to disk."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, path)
    logger.info("Model saved to %s", path)
