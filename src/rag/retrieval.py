from __future__ import annotations

import logging
from typing import Any, Protocol

logger = logging.getLogger(__name__)


class Retriever(Protocol):
    """Minimal retriever interface. Implement with your vector store of choice."""

    def retrieve(self, query: str, top_k: int = 5) -> list[dict[str, Any]]: ...


class InMemoryRetriever:
    """Trivial keyword retriever for tests and scaffolding. Swap for a real vector store."""

    def __init__(self, documents: list[dict[str, Any]]) -> None:
        self._docs = documents

    def retrieve(self, query: str, top_k: int = 5) -> list[dict[str, Any]]:
        q = query.lower()
        scored = sorted(
            self._docs,
            key=lambda d: sum(1 for tok in q.split() if tok in d.get("text", "").lower()),
            reverse=True,
        )
        logger.info("Retrieved %d docs for query", min(top_k, len(scored)))
        return scored[:top_k]
