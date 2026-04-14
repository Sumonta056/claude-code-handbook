"""Breaks multi-part questions into smaller subqueries."""

from __future__ import annotations


class QueryDecomposer:
    def decompose(self, query: str) -> list[str]:
        normalized = query.replace(" then ", ", ").replace(" and ", ", ")
        parts = [part.strip() for part in normalized.split(",") if part.strip()]
        return parts or [query]
