"""Tiny in-memory semantic cache for repeat queries."""

from __future__ import annotations

from app.models import QueryResponse


def _cache_key(query: str) -> str:
    return " ".join(query.lower().split())


class SemanticCache:
    def __init__(self) -> None:
        self._items: dict[str, QueryResponse] = {}

    def get(self, query: str) -> QueryResponse | None:
        return self._items.get(_cache_key(query))

    def set(self, query: str, response: QueryResponse) -> None:
        self._items[_cache_key(query)] = response
