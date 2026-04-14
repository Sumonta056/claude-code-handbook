"""Toy cost estimation for demo traces."""

from __future__ import annotations

from app.models import RetrievedDocument


class CostTracker:
    def __init__(self) -> None:
        self.tokens = 0
        self.documents = 0

    def add(self, query: str, answer: str, documents: list[RetrievedDocument]) -> None:
        self.tokens += len(query.split()) + len(answer.split())
        self.documents += len(documents)

    def summary(self) -> str:
        estimated_cost = round(self.tokens * 0.000002, 6)
        return (
            f"cost:tokens={self.tokens},documents={self.documents},"
            f"estimated_usd={estimated_cost}"
        )
