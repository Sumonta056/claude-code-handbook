# Agents Guide

## Ownership Map

- `agents/document_grader.py`: document quality gates
- `agents/query_decomposer.py`: query splitting and task extraction
- `agents/adaptive_router.py`: route refinement based on query structure
- `agents/tools/`: pluggable retrieval adapters

## Expectations

- Agent modules should stay deterministic in local development.
- Tool adapters must degrade gracefully when no external system exists.
- Routing decisions should remain explainable through trace events.
