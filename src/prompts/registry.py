from __future__ import annotations

import logging
from dataclasses import dataclass, field
from pathlib import Path

logger = logging.getLogger(__name__)

PROMPTS_DIR = Path(__file__).parent / "templates"


@dataclass
class Prompt:
    name: str
    version: str
    template: str
    metadata: dict = field(default_factory=dict)

    def render(self, **kwargs: object) -> str:
        """Basic str.format rendering. Swap for jinja2.Template for complex logic."""
        return self.template.format(**kwargs)


class PromptRegistry:
    """In-memory registry. Graduate to MLflow/LangSmith/Langfuse in production."""

    def __init__(self) -> None:
        self._prompts: dict[tuple[str, str], Prompt] = {}

    def register(self, prompt: Prompt) -> None:
        self._prompts[(prompt.name, prompt.version)] = prompt
        logger.info("Registered prompt %s@%s", prompt.name, prompt.version)

    def get(self, name: str, version: str = "v1") -> Prompt:
        return self._prompts[(name, version)]

    def load_from_dir(self, dir_path: Path | None = None) -> None:
        """Load all `<name>.<version>.md` files from the templates directory."""
        base = dir_path or PROMPTS_DIR
        if not base.exists():
            return
        for path in base.glob("*.md"):
            stem_parts = path.stem.rsplit(".", 1)
            if len(stem_parts) != 2:
                continue
            name, version = stem_parts
            self.register(Prompt(name=name, version=version, template=path.read_text(encoding="utf-8")))


registry = PromptRegistry()
