"""
LLM Client wrapper.

Abstracts calls to external LLM.
Supports chat completions and embeddings.
"""

from typing import List, Dict, Any

class LLMClient:
    def chat(self, system_prompt: str, user_prompt: str) -> str:
        raise NotImplementedError()

    def embed(self, texts: List[str]) -> List[List[float]]:
        raise NotImplementedError()