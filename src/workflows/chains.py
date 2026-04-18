from __future__ import annotations

import logging
from collections.abc import Callable

logger = logging.getLogger(__name__)


def chain(*steps: Callable[[str], str]) -> Callable[[str], str]:
    """Compose steps left-to-right: chain(a, b, c)(x) == c(b(a(x)))."""

    def run(value: str) -> str:
        for step in steps:
            value = step(value)
        return value

    return run
