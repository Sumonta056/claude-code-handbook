"""Filters unsafe or irrelevant retrieved content."""

from __future__ import annotations

from app.models import RetrievedDocument


def filter_documents(documents: list[RetrievedDocument]) -> list[RetrievedDocument]:
    filtered_documents = [
        document
        for document in documents
        if "unsafe" not in document.content.lower()
    ]
    return filtered_documents or documents[:1]
