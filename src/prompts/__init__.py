"""Prompt templates and registry.

Convention: one file per prompt, versioned with `v1`, `v2` suffixes.
Use Jinja2 for interpolation. Register prompts in `registry.py` so they
can be hot-swapped via config.
"""

from src.prompts.registry import PromptRegistry, registry

__all__ = ["PromptRegistry", "registry"]
