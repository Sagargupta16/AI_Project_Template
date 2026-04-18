from __future__ import annotations

import pandas as pd

from src.ml.dataset import preprocess_data


def test_preprocess_drops_duplicates():
    df = pd.DataFrame({"a": [1, 1, 2], "b": [3, 3, 4]})
    result = preprocess_data(df)
    assert len(result) == 2


def test_preprocess_drops_all_nan_rows():
    df = pd.DataFrame({"a": [1, None], "b": [2, None]})
    result = preprocess_data(df)
    assert len(result) == 1
