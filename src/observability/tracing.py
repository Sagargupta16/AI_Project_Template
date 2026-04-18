from __future__ import annotations

import logging

from src.core.config import get_settings

logger = logging.getLogger(__name__)


def setup_tracing() -> None:
    """Initialize tracing. Stub - wire to Phoenix / LangSmith / MLflow Tracing / OTel collector."""
    settings = get_settings()
    if not settings.observability.tracing_enabled:
        logger.info("Tracing disabled")
        return
    logger.info("Tracing enabled with backend=%s", settings.observability.tracing_backend)
