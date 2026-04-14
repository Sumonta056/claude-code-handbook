"""Basic input validation for the demo pipeline."""

from __future__ import annotations


BLOCKED_PATTERNS = (
    "ignore previous instructions",
    "drop table",
    "rm -rf",
    "<script",
)


def validate_input(query: str) -> str:
    cleaned_query = " ".join(query.split())
    if not cleaned_query:
        raise ValueError("Query must not be empty.")
    if len(cleaned_query) > 500:
        raise ValueError("Query exceeds the 500 character demo limit.")

    lowered_query = cleaned_query.lower()
    for pattern in BLOCKED_PATTERNS:
        if pattern in lowered_query:
            raise ValueError(f"Query contains a blocked pattern: {pattern}")

    return cleaned_query
