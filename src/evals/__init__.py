"""Evaluation: golden datasets, offline evals, LLM-as-judge, online feedback.

Layout:
- datasets/   JSONL files of input/expected pairs
- offline/    Scripts that run evals against a specific model version
- judges/     LLM-as-judge prompt + scoring logic
"""
