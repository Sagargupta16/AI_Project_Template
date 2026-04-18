# Changelog

## [3.0.0] - 2026-04-18

Major restructure for any AI workload (ML, DL, LLM, RAG, agents).

### Added
- Domain-separated `src/` layout: `core`, `ml`, `rag`, `agents`, `workflows`, `tools`, `prompts`, `evals`, `guardrails`, `observability`, `services`, `api`.
- `AGENTS.md` as canonical cross-tool agent spec (Codex, Cursor, Gemini CLI, Aider, Windsurf).
- `pydantic-settings` based config with nested sub-settings (`ml`, `llm`, `rag`, `observability`).
- Prompt registry with versioned templates in `src/prompts/templates/`.
- Offline eval runner + golden dataset in `src/evals/`.
- Guardrails module with input/output filters and PII redaction.
- Observability module: tracing setup, cost tracker, feedback capture.
- FastAPI entrypoint in `src/api/main.py` with lifespan for tracing setup.
- `uv` as the canonical package manager; Makefile switched to `uv run` commands.
- CI updated to use `astral-sh/setup-uv`; format-check enforced.

### Changed
- `src/modeling/` renamed to `src/ml/`; `src/config.py` → `src/core/config.py`.
- `requirements*.txt` removed; deps live in `pyproject.toml` extras (`ml`, `dl`, `llm`, `rag`, `agents`, `eval`, `api`, `jupyter`, `dev`, `all`).
- Base install is now lean (~4 packages); heavy deps are opt-in.
- `Config` dataclass → `Settings` pydantic model; loaded via `get_settings()`.
- `tests/` split into `unit/` and `integration/`.
- CLAUDE.md is now a thin pointer to AGENTS.md.

### Removed
- `requirements.txt` and `requirements-dev.txt` (replaced by `pyproject.toml` extras).
- `src/modeling/` directory (moved to `src/ml/`).

## [2.0.0] - 2026-03-14

- Fill skeleton with working code (config, dataset, features, train, predict)
- Add pyproject.toml, ruff, pre-commit, CI
- Expand requirements.txt with common ML dependencies

## [1.0.0] - 2025-08-22

- Initial AI project template structure (empty skeleton)
