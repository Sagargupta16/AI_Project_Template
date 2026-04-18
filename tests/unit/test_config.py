from __future__ import annotations

from src.core.config import Settings, get_settings


def test_settings_loads_defaults():
    s = Settings()
    assert s.ml.random_seed == 42
    assert 0.0 < s.ml.test_size < 1.0
    assert s.llm.provider == "anthropic"
    assert s.rag.top_k > 0


def test_derived_paths_are_under_project_root():
    s = Settings()
    assert s.raw_data_dir == s.data_dir / "raw"
    assert s.data_dir.parent == s.project_root


def test_get_settings_is_cached():
    assert get_settings() is get_settings()
