# Security Policy

## Reporting a vulnerability

**Do not open a public issue for security problems.**

- Preferred: open a [GitHub Security Advisory](https://github.com/Sagargupta16/ai-project-template/security/advisories/new) (private).
- Alternative: email `sg85207@gmail.com`.

Include:
- Affected file(s) / commit SHA
- Reproduction steps
- Impact assessment
- Suggested fix, if you have one

We aim to acknowledge within **3 business days** and provide a patch plan within **14 days** for confirmed issues.

## Supported versions

Only `main` is supported. Tagged releases are snapshots; fixes land on `main` and flow into the next release.

## Scope

In scope:
- Secret leakage (accidental commits of `.env`, keys)
- Vulnerable dependencies surfaced by Dependabot / Trivy
- Insecure defaults in template code
- Prompt-injection or data-exfil paths in the sample agents / RAG wiring

Out of scope:
- Issues in your fork's application code (report to your team)
- Known limitations of upstream deps that are already tracked

Last updated: 2026-04-18
