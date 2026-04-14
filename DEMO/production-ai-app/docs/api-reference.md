# API Reference

## `GET /`

Returns a simple service-ready message.

## `GET /health`

Returns:

```json
{
  "status": "ok",
  "app_name": "Production AI App Demo",
  "version": "0.1.0"
}
```

## `POST /query`

Request body:

```json
{
  "query": "How does the code query endpoint work?",
  "session_id": "demo-session",
  "top_k": 3
}
```

Response body includes:

- `answer`
- `route`
- `cached`
- `documents`
- `trace`
