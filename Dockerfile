FROM python:3.13-slim AS base

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1

RUN useradd -m appuser
WORKDIR /app

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Deps layer (cached when pyproject.toml is unchanged)
COPY pyproject.toml ./
RUN uv sync --extra ml --extra llm --extra api --no-install-project

# Source
COPY src/ src/
RUN uv sync --extra ml --extra llm --extra api

USER appuser
EXPOSE 8000

CMD ["uv", "run", "uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
