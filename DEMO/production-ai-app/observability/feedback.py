"""Feedback capture for future extensions."""

from __future__ import annotations


class FeedbackStore:
    def __init__(self) -> None:
        self._items: list[dict[str, str]] = []

    def record(self, session_id: str, rating: str, comment: str = "") -> None:
        self._items.append(
            {
                "session_id": session_id,
                "rating": rating,
                "comment": comment,
            }
        )

    def all(self) -> list[dict[str, str]]:
        return list(self._items)
