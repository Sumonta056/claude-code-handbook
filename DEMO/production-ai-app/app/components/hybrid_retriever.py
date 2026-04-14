"""Simple hybrid retriever that mixes lexical and semantic-style scoring."""

from __future__ import annotations

from app.models import RetrievedDocument


DEFAULT_DOCUMENTS = [
    RetrievedDocument(
        id="doc-architecture",
        title="RAG pipeline architecture",
        content="Hybrid retrieval, reranking, caching, routing, and observability.",
        source="internal",
    ),
    RetrievedDocument(
        id="doc-security",
        title="Security guardrails",
        content="Input filtering, content moderation, and output filtering for safe responses.",
        source="internal",
    ),
    RetrievedDocument(
        id="doc-evals",
        title="Evaluation workflow",
        content="Golden datasets, offline evaluation, and online monitoring for quality tracking.",
        source="internal",
    ),
]


def _terms(text: str) -> set[str]:
    return {token.strip(".,:;!?").lower() for token in text.split() if token.strip()}


class HybridRetriever:
    def __init__(self, documents: list[RetrievedDocument] | None = None) -> None:
        self.documents = documents or DEFAULT_DOCUMENTS

    def retrieve(
        self,
        query: str,
        top_k: int = 3,
        candidates: list[RetrievedDocument] | None = None,
    ) -> list[RetrievedDocument]:
        query_terms = _terms(query)
        pool = self._merge_candidates(candidates or [])
        scored_documents: list[RetrievedDocument] = []

        for document in pool:
            document_terms = _terms(f"{document.title} {document.content} {document.source}")
            overlap = len(query_terms & document_terms)
            if overlap:
                score = overlap / max(len(query_terms), 1)
                scored_documents.append(document.with_score(score))

        if not scored_documents:
            return [document.with_score(0.1) for document in pool[:top_k]]

        scored_documents.sort(key=lambda document: document.score, reverse=True)
        return scored_documents[:top_k]

    def _merge_candidates(self, candidates: list[RetrievedDocument]) -> list[RetrievedDocument]:
        merged: dict[str, RetrievedDocument] = {document.id: document for document in self.documents}
        for document in candidates:
            merged[document.id] = document
        return list(merged.values())
