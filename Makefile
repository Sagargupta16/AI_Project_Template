.PHONY: help setup dev test test-cov lint lint-fix format clean notebook api eval pre-commit

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

setup: ## Install base deps with uv (add extras with: uv sync --extra ml --extra llm ...)
	uv sync

dev: ## Install everything (ml, llm, rag, agents, eval, api, jupyter, dev)
	uv sync --extra all

test: ## Run tests
	uv run pytest tests/ -v

test-cov: ## Run tests with coverage
	uv run pytest tests/ --cov=src --cov-report=html --cov-report=term

lint: ## Run ruff linter
	uv run ruff check .

lint-fix: ## Run ruff linter with auto-fix
	uv run ruff check --fix .

format: ## Format code with ruff
	uv run ruff format .

clean: ## Remove build artifacts and caches
	rm -rf __pycache__ .pytest_cache .coverage htmlcov .ruff_cache .mypy_cache dist build *.egg-info
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true

notebook: ## Launch Jupyter notebook server
	uv run jupyter notebook notebooks/

api: ## Run FastAPI dev server (requires the [api] extra)
	uv run uvicorn src.api.main:app --reload --port 8000

eval: ## Run offline evals against the golden dataset
	uv run python -m src.evals.offline.run_eval

pre-commit: ## Install pre-commit hooks
	uv run pre-commit install
