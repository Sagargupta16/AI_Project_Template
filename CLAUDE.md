# CLAUDE.md

This file exists for Claude Code. **The canonical agent spec is [AGENTS.md](AGENTS.md)** — Claude Code should read it in full.

The two files intentionally mirror each other's content; `AGENTS.md` is the open cross-tool standard (Codex, Cursor, Gemini CLI, Aider, Windsurf, Jules, Devin), and this file preserves Claude Code's expected filename. If the two ever diverge, `AGENTS.md` wins.

See [AGENTS.md](AGENTS.md) for:
- Architecture (domain-separated `src/` layout)
- The three-bucket rule (`agents/` vs `tools/` vs `services/` vs `workflows/`)
- Core conventions (imports, config, logging, prompts, evals)
- Tooling (ruff, pytest, mypy, pre-commit)
- Where new capabilities go
- Verification protocol
