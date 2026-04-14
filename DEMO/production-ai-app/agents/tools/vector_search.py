"""Offline vector-search style adapter."""

from __future__ import annotations

from app.models import RetrievedDocument


class VectorSearchTool:
    def search(self, query: str) -> list[RetrievedDocument]:
        return [
            RetrievedDocument(
                id="vec-1",
                title="Semantic retrieval patterns",
                content="Use embeddings, chunking, and reranking to improve retrieval precision.",
                source="vector-index",
                score=0.45,
            ),
            RetrievedDocument(
                id="vec-2",
                title="Caching query flows",
                content="A semantic cache can reduce repeated latency and cost for common questions.",
                source="vector-index",
                score=0.35,
            ),
        ]
