"""Demo reranker that boosts title and source matches."""

from __future__ import annotations

from app.models import RetrievedDocument


def _contains_term(text: str, term: str) -> bool:
    return term and term.lower() in text.lower()


class Reranker:
    def rerank(
        self,
        query: str,
        documents: list[RetrievedDocument],
        top_k: int = 3,
    ) -> list[RetrievedDocument]:
        boosted_documents: list[RetrievedDocument] = []
        query_terms = [term.lower() for term in query.split() if term.strip()]

        for document in documents:
            bonus = 0.0
            for term in query_terms:
                if _contains_term(document.title, term):
                    bonus += 0.2
                if _contains_term(document.source, term):
                    bonus += 0.1
            boosted_documents.append(document.with_score(document.score + bonus))

        boosted_documents.sort(key=lambda document: document.score, reverse=True)
        return boosted_documents[:top_k]
