from __future__ import annotations

import pytest

from src.guardrails.filters import GuardrailViolation, input_guard, output_filter


def test_input_guard_accepts_short_input():
    assert input_guard("hello") == "hello"


def test_input_guard_rejects_too_long():
    with pytest.raises(GuardrailViolation):
        input_guard("x" * 9000, max_length=8000)


def test_output_filter_redacts_email():
    result = output_filter("contact me at a@b.com please")
    assert "a@b.com" not in result
    assert "[REDACTED:email]" in result


def test_output_filter_can_disable_redaction():
    result = output_filter("a@b.com", redact_pii=False)
    assert result == "a@b.com"
