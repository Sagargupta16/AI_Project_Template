from __future__ import annotations

import pandas as pd
import pytest


@pytest.fixture
def sample_dataframe() -> pd.DataFrame:
    """Create a small sample DataFrame for testing."""
    return pd.DataFrame(
        {
            "feature_a": [1.0, 2.0, 3.0, 4.0, 5.0],
            "feature_b": [10, 20, 30, 40, 50],
            "target": [0, 1, 0, 1, 1],
        }
    )
