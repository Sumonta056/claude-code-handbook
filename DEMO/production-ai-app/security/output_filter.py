"""Redacts simple blocked phrases from generated output."""

from __future__ import annotations


BLOCKED_OUTPUT_PATTERNS = {
    "drop table": "[redacted destructive instruction]",
}


def filter_output(answer: str) -> str:
    safe_answer = answer
    for pattern, replacement in BLOCKED_OUTPUT_PATTERNS.items():
        safe_answer = safe_answer.replace(pattern, replacement)
        safe_answer = safe_answer.replace(pattern.title(), replacement)
    return safe_answer
