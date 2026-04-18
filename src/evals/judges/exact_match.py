from __future__ import annotations


def exact_match(prediction: str, expected: str) -> float:
    """1.0 if strings match (case/whitespace-insensitive), else 0.0."""
    return float(prediction.strip().lower() == expected.strip().lower())
