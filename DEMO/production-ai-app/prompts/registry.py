"""Prompt registry with tiny rendering helpers."""

from __future__ import annotations

from app.models import RetrievedDocument
from prompts.templates import ANSWER_TEMPLATES


class PromptRegistry:
    def get_template(self, route: str) -> str:
        return ANSWER_TEMPLATES.get(route, ANSWER_TEMPLATES["rag"])

    def render_answer(
        self,
        route: str,
        query: str,
        documents: list[RetrievedDocument],
    ) -> str:
        intro = self.get_template(route)
        if not documents:
            return f"{intro} No supporting documents were retrieved for '{query}'."

        references = "; ".join(
            f"{document.title} [{document.source}]"
            for document in documents
        )
        return f"{intro} For '{query}', the strongest references are {references}."
