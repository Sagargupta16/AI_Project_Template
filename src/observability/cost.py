from __future__ import annotations

import logging
from dataclasses import dataclass, field

logger = logging.getLogger(__name__)


@dataclass
class CostTracker:
    """Aggregate LLM cost per run. Extend with per-model pricing lookup."""

    total_usd: float = 0.0
    by_model: dict[str, float] = field(default_factory=dict)

    def record(self, model: str, input_tokens: int, output_tokens: int, usd_per_1k: tuple[float, float]) -> None:
        cost = (input_tokens / 1000.0) * usd_per_1k[0] + (output_tokens / 1000.0) * usd_per_1k[1]
        self.total_usd += cost
        self.by_model[model] = self.by_model.get(model, 0.0) + cost
        logger.info("Recorded $%.6f for %s", cost, model)
