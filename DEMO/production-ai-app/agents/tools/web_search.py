"""Curated stand-in for web retrieval."""

from __future__ import annotations

from app.models import RetrievedDocument


class WebSearchTool:
    def search(self, query: str) -> list[RetrievedDocument]:
        return [
            RetrievedDocument(
                id="web-1",
                title="External release summary",
                content="Curated summary for a latest-style question without making a live network call.",
                source="web-cache",
                score=0.4,
            ),
            RetrievedDocument(
                id="web-2",
                title="Public guidance article",
                content="A placeholder result that represents safe web-grounded retrieval in local development.",
                source="web-cache",
                score=0.3,
            ),
        ]
