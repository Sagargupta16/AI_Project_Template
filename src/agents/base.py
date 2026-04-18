from __future__ import annotations

import logging
from dataclasses import dataclass, field
from typing import Any, Protocol

logger = logging.getLogger(__name__)


class Tool(Protocol):
    """A tool an agent can invoke. Keep tools stateless and typed."""

    name: str

    def __call__(self, **kwargs: Any) -> Any: ...


@dataclass
class AgentRun:
    """One execution of an agent. Captures steps, tool calls, and final output for tracing."""

    input: str
    output: str = ""
    steps: list[dict[str, Any]] = field(default_factory=list)
    cost_usd: float = 0.0


class Agent:
    """Minimal agent scaffold. Replace the `run` loop with your framework of choice
    (Anthropic tool use, OpenAI function calling, LangGraph, Pydantic AI, etc.)."""

    def __init__(self, name: str, system_prompt: str, tools: list[Tool] | None = None) -> None:
        self.name = name
        self.system_prompt = system_prompt
        self.tools = {t.name: t for t in tools or []}

    def run(self, user_input: str) -> AgentRun:
        run = AgentRun(input=user_input)
        logger.info("Agent %s received input", self.name)
        run.output = "TODO: wire up your LLM call + tool loop"
        return run
