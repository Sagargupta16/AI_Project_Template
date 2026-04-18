from __future__ import annotations

import json
import logging
from collections.abc import Callable
from pathlib import Path

logger = logging.getLogger(__name__)


def load_dataset(path: Path | str) -> list[dict]:
    return [json.loads(line) for line in Path(path).read_text(encoding="utf-8").splitlines() if line.strip()]


def run_eval(
    dataset_path: Path | str,
    predict_fn: Callable[[str], str],
    judge_fn: Callable[[str, str], float],
) -> dict:
    """Run `predict_fn` over each example, score with `judge_fn`, return aggregates."""
    data = load_dataset(dataset_path)
    scores: list[float] = []
    for ex in data:
        pred = predict_fn(ex["input"])
        scores.append(judge_fn(pred, ex["expected"]))
    mean = sum(scores) / len(scores) if scores else 0.0
    logger.info("Ran %d evals, mean score %.3f", len(scores), mean)
    return {"n": len(scores), "mean_score": mean, "scores": scores}
