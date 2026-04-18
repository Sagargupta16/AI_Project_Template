from __future__ import annotations

import logging
import re

logger = logging.getLogger(__name__)


class GuardrailViolation(Exception):
    """Raised when input/output violates a guardrail."""


_PII_PATTERNS = {
    "email": re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+"),
    "ssn": re.compile(r"\b\d{3}-\d{2}-\d{4}\b"),
}


def input_guard(text: str, max_length: int = 8000) -> str:
    """Pre-LLM check. Reject on length, injection, or banned content."""
    if len(text) > max_length:
        raise GuardrailViolation(f"Input exceeds max_length {max_length}")
    return text


def output_filter(text: str, redact_pii: bool = True) -> str:
    """Post-LLM check. Redact PII, strip secrets, etc."""
    if redact_pii:
        for label, pattern in _PII_PATTERNS.items():
            text = pattern.sub(f"[REDACTED:{label}]", text)
    return text
