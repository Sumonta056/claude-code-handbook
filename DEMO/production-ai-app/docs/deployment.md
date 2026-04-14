# Deployment

## Local Python

```bash
pip install -e .
uvicorn app.main:app --reload
python frontend/app.py
```

## Docker Compose

```bash
docker compose up --build
```

This starts:

- API on `http://127.0.0.1:8000`
- Frontend on `http://127.0.0.1:5001`

## Healthcheck

```bash
python scripts/healthcheck.py
```
