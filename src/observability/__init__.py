"""Observability: tracing, cost tracking, feedback capture.

OpenTelemetry-based. Call `setup_tracing()` once at app boot; instrumentation
is then applied automatically, not scattered across business logic.
"""

from src.observability.cost import CostTracker
from src.observability.tracing import setup_tracing

__all__ = ["CostTracker", "setup_tracing"]
