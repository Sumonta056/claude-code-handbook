"""Small tracing helper used to expose pipeline stages."""

from __future__ import annotations


class TraceRecorder:
    def __init__(self) -> None:
        self._events: list[str] = []

    def log(self, event: str) -> None:
        self._events.append(event)

    def snapshot(self) -> list[str]:
        return list(self._events)
