# Claude Context

This demo project is intentionally small and readable.

## Goals

- Preserve the architecture shape from the reference image.
- Keep business logic offline-safe and deterministic.
- Favor simple module boundaries over unnecessary abstractions.

## Development Preferences

- Add tests for behavior changes in routing, retrieval, or caching.
- Keep the FastAPI layer thin and move logic into `services/`.
- Treat `agents/tools/` as adapter modules rather than heavy frameworks.
