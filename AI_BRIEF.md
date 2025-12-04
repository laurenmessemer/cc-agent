# Customer Communication Agent

This project is a Python AI agent for trades business owners.

The agent:
- Drafts customer messages
- Learns the owner's tone
- Flags risky conversations
- Remembers job & customer context
- Suggests follow-ups

Architecture:
- Orchestrator coordinates LLM tools
- Tools = small classes in app/tools/
- SQLite with SQLAlchemy
- CLI via Typer
- LLM adapters in llm_client.py

Rules:
- Keep functions small
- Do not put LLM calls directly in UI
- Memory = SQLite
- Avoid tight coupling between modules
- Prefer deterministic logic before LLM calls
