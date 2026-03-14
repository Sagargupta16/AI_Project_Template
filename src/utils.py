from __future__ import annotations

import logging
import random

import numpy as np


def set_seed(seed: int = 42) -> None:
    """Set random seed for reproducibility."""
    random.seed(seed)
    np.random.seed(seed)
    logging.getLogger(__name__).info("Random seed set to %d", seed)
