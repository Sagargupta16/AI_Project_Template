from __future__ import annotations

import logging
from dataclasses import dataclass
from datetime import UTC, datetime

logger = logging.getLogger(__name__)


@dataclass
class Feedback:
    run_id: str
    score: int  # -1, 0, 1 (thumbs down / neutral / up)
    comment: str = ""
    timestamp: datetime = datetime.now(UTC)


def record_feedback(feedback: Feedback) -> None:
    """Persist user feedback. Stub - write to DB, Langfuse, LangSmith, etc."""
    logger.info("Feedback for %s: score=%d", feedback.run_id, feedback.score)
