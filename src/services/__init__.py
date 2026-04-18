"""Services: business logic, DB access, and external API clients.

Services are invoked by `api/` routes and by `tools/` callables. They should
never hold agent/LLM control flow - that lives in `agents/` or `workflows/`.
"""
