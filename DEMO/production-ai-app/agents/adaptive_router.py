"""Route refinement based on simple heuristics."""

from __future__ import annotations


class AdaptiveRouter:
    def __init__(self, default_route: str = "rag") -> None:
        self.default_route = default_route

    def choose_route(self, query: str, suggested_route: str, subqueries: list[str]) -> str:
        lowered_query = query.lower()
        wants_docs = any(token in lowered_query for token in ("docs", "reference", "guide"))
        asks_about_api = "api" in lowered_query or "endpoint" in lowered_query
        asks_for_code = any(token in lowered_query for token in ("code", "function", "bug"))

        if (wants_docs or asks_about_api) and not asks_for_code:
            return "docs"
        if len(subqueries) > 1 and suggested_route == self.default_route:
            return "rag"
        return suggested_route or self.default_route
