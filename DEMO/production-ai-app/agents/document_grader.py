"""Filters out low-value documents after retrieval."""

from __future__ import annotations

from app.models import RetrievedDocument


class DocumentGrader:
    def grade(
        self,
        query: str,
        documents: list[RetrievedDocument],
        minimum_score: float = 0.1,
    ) -> list[RetrievedDocument]:
        kept_documents = [document for document in documents if document.score >= minimum_score]
        return kept_documents or documents[:1]
