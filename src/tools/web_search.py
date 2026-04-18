from __future__ import annotations

import logging
from dataclasses import dataclass

logger = logging.getLogger(__name__)


@dataclass
class SearchResult:
    title: str
    url: str
    snippet: str


def web_search(query: str, max_results: int = 5) -> list[SearchResult]:
    """Search the web. Stub - wire to your provider (Tavily, SerpAPI, Brave, etc.)."""
    logger.info("web_search query=%r max_results=%d", query, max_results)
    return []
