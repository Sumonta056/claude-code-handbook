"""Rule-based router for sending queries to the right subsystem."""

from __future__ import annotations


ROUTE_KEYWORDS = {
    "code": ("code", "python", "function", "bug", "stack trace", "repository", "repo"),
    "web": ("latest", "news", "website", "browser", "internet", "external"),
    "docs": ("docs", "readme", "guide", "reference", "playbook"),
}


def route_query(query: str, default_route: str = "rag") -> str:
    lowered_query = query.lower()
    for route, keywords in ROUTE_KEYWORDS.items():
        if any(keyword in lowered_query for keyword in keywords):
            return route
    return default_route
