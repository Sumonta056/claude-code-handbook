# Production AI App Demo

This is a minimal, runnable template for a production-style AI application layout.
It includes a FastAPI backend, a lightweight Flask frontend, simple retrieval and
reranking components, demo agents, evaluation scripts, and a small testing setup.

## Quick Start

```bash
cd DEMO/production-ai-app
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
python -m unittest discover -s tests
uvicorn app.main:app --reload
```

Run the frontend in another terminal:

```bash
cd DEMO/production-ai-app
pip install -r frontend/requirements.txt
python frontend/app.py
```

API: `http://127.0.0.1:8000`
Frontend: `http://127.0.0.1:5001`

## Highlights

- `app/`: FastAPI entrypoint, config, models, and container image
- `components/`: retrieval and reranking primitives
- `services/`: orchestration pipeline, cache, rewriting, routing, conversation memory
- `agents/`: decomposition, grading, adaptive routing, and tool adapters
- `security/`: basic input, content, and output guards
- `evaluation/`: golden dataset, offline evaluation, online monitoring
- `observability/`: trace, feedback, and cost utilities
- `frontend/`: lightweight UI for poking the API

## Notes

- The search tools are offline-safe demo implementations. They do not call the web.
- The template favors simple, readable code over framework-heavy abstractions.
- A few extra files such as `__init__.py` and `frontend/static/styles.css` are
  included so the project is importable and usable immediately.
