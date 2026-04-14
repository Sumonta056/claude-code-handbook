"""Curated stand-in for repository search."""

from __future__ import annotations

from app.models import RetrievedDocument


class CodeSearchTool:
    def search(self, query: str) -> list[RetrievedDocument]:
        return [
            RetrievedDocument(
                id="code-1",
                title="FastAPI query endpoint",
                content="POST /query validates input, runs the pipeline, and returns answer plus trace.",
                source="codebase",
                score=0.5,
            ),
            RetrievedDocument(
                id="code-2",
                title="Routing service",
                content="Rule-based routing sends code questions to repository search and docs questions to references.",
                source="codebase",
                score=0.4,
            ),
        ]
