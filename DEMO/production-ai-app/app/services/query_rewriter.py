"""Helpers that make terse follow-up questions easier to resolve."""

from __future__ import annotations


def rewrite_query(query: str, history: list[dict[str, str]]) -> str:
    cleaned_query = " ".join(query.split())
    if not history:
        return cleaned_query

    lowered_query = cleaned_query.lower()
    is_follow_up = lowered_query.startswith(("it ", "that ", "those ", "they ", "what about"))
    if not is_follow_up:
        return cleaned_query

    last_user_message = ""
    for message in reversed(history):
        if message["role"] == "user":
            last_user_message = message["content"]
            break

    if not last_user_message:
        return cleaned_query

    return f"{cleaned_query} (context: {last_user_message})"
