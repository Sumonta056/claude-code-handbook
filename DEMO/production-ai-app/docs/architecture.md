# Architecture

The demo keeps the same high-level shape as the reference:

- `app/` exposes the API and config
- `components/` handle retrieval and reranking primitives
- `services/` orchestrate routing, rewriting, caching, and response generation
- `agents/` refine routing and provide pluggable tools
- `security/` provides input, content, and output guard layers
- `evaluation/` covers offline and online quality checks
- `observability/` captures traces, feedback, and estimated cost

The implementation is intentionally small but the seams are realistic enough to
grow into a larger codebase.
