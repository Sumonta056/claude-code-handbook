"""Shared data models used across the demo application."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any


@dataclass
class QueryRequest:
    query: str
    session_id: str = "default"
    top_k: int = 3

    @classmethod
    def from_dict(cls, payload: dict[str, Any]) -> "QueryRequest":
        return cls(
            query=str(payload.get("query") or "").strip(),
            session_id=str(payload.get("session_id") or "default").strip() or "default",
            top_k=int(payload.get("top_k") or 3),
        )


@dataclass
class RetrievedDocument:
    id: str
    title: str
    content: str
    source: str
    score: float = 0.0

    def with_score(self, score: float) -> "RetrievedDocument":
        return RetrievedDocument(
            id=self.id,
            title=self.title,
            content=self.content,
            source=self.source,
            score=round(score, 3),
        )

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class QueryResponse:
    answer: str
    route: str
    cached: bool = False
    documents: list[RetrievedDocument] = field(default_factory=list)
    trace: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "answer": self.answer,
            "route": self.route,
            "cached": self.cached,
            "documents": [document.to_dict() for document in self.documents],
            "trace": list(self.trace),
        }


@dataclass
class HealthResponse:
    status: str
    app_name: str
    version: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class EvaluationCase:
    query: str
    expected_route: str
    expected_snippet: str
