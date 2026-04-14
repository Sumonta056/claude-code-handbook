"""Configuration helpers for the demo application."""

from __future__ import annotations

from dataclasses import dataclass
import os


def _read_bool(name: str, default: bool) -> bool:
    raw_value = os.getenv(name, str(default)).strip().lower()
    return raw_value in {"1", "true", "yes", "on"}


@dataclass(frozen=True)
class Settings:
    app_name: str
    debug: bool
    default_route: str
    max_history_messages: int
    top_k: int
    frontend_origin: str


def load_settings() -> Settings:
    return Settings(
        app_name=os.getenv("APP_NAME", "Production AI App Demo"),
        debug=_read_bool("DEBUG", False),
        default_route=os.getenv("DEFAULT_ROUTE", "rag"),
        max_history_messages=int(os.getenv("MAX_HISTORY_MESSAGES", "10")),
        top_k=int(os.getenv("TOP_K", "3")),
        frontend_origin=os.getenv("FRONTEND_ORIGIN", "http://127.0.0.1:5001"),
    )


settings = load_settings()
