"""Conversation memory used by the query rewriter."""

from __future__ import annotations

from collections import defaultdict
from typing import TypedDict


class Message(TypedDict):
    role: str
    content: str


class ConversationStore:
    def __init__(self) -> None:
        self._sessions: dict[str, list[Message]] = defaultdict(list)

    def get_history(self, session_id: str) -> list[Message]:
        return list(self._sessions[session_id])

    def append(self, session_id: str, role: str, content: str, max_messages: int) -> None:
        self._sessions[session_id].append({"role": role, "content": content})
        self._sessions[session_id] = self._sessions[session_id][-max_messages:]
