"""Guardrails: input/output validators that wrap LLM calls.

Wire three layers: input_guard (pre-LLM), content_filter (mid), output_filter (post-LLM).
"""
