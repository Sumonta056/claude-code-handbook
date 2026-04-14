"""FastAPI entrypoint for the production AI app demo."""

from __future__ import annotations

from typing import Any

from fastapi import Body, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app import __version__
from app.config import settings
from app.models import HealthResponse, QueryRequest
from app.services.rag_pipeline import RAGPipeline


app = FastAPI(title=settings.app_name, version=__version__)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.frontend_origin, "http://localhost:5001"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

pipeline = RAGPipeline()


@app.get("/")
def root() -> dict[str, str]:
    return {"message": f"{settings.app_name} is running."}


@app.get("/health")
def health() -> dict[str, Any]:
    response = HealthResponse(
        status="ok",
        app_name=settings.app_name,
        version=__version__,
    )
    return response.to_dict()


@app.post("/query")
def query(payload: dict[str, Any] = Body(...)) -> dict[str, Any]:
    try:
        request = QueryRequest.from_dict(payload)
        response = pipeline.run(request)
        return response.to_dict()
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
