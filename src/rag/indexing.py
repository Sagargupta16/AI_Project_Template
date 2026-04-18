from __future__ import annotations

import logging
from pathlib import Path
from typing import Any

from src.rag.chunking import Chunk

logger = logging.getLogger(__name__)


def build_index(chunks: list[Chunk], index_path: Path | str) -> dict[str, Any]:
    """Persist chunks to a vector index. Stub - wire up to your vector DB (chroma, pgvector, qdrant)."""
    path = Path(index_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    logger.info("Would write %d chunks to %s", len(chunks), path)
    return {"num_chunks": len(chunks), "path": str(path)}
