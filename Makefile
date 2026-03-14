.PHONY: help setup dev test lint format clean

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

setup: ## Install project dependencies
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

dev: ## Install project in editable mode with all extras
	pip install -e ".[dev,jupyter]"

test: ## Run tests with pytest
	python -m pytest tests/ -v

test-cov: ## Run tests with coverage
	python -m pytest tests/ --cov=src --cov-report=html --cov-report=term

lint: ## Run ruff linter
	ruff check .

lint-fix: ## Run ruff linter with auto-fix
	ruff check --fix .

format: ## Format code with ruff
	ruff format .

clean: ## Remove build artifacts and caches
	rm -rf __pycache__ .pytest_cache .coverage htmlcov .ruff_cache dist build *.egg-info
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true

notebook: ## Launch Jupyter notebook server
	jupyter notebook notebooks/

pre-commit: ## Install pre-commit hooks
	pre-commit install
