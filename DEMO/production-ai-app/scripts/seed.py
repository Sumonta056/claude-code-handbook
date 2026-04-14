"""Create tiny demo data files used by the template project."""

from __future__ import annotations

import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1]


def main() -> None:
    raw_dir = BASE_DIR / "data" / "raw"
    processed_dir = BASE_DIR / "data" / "processed"
    index_dir = BASE_DIR / "data" / "index_config"

    raw_dir.mkdir(parents=True, exist_ok=True)
    processed_dir.mkdir(parents=True, exist_ok=True)
    index_dir.mkdir(parents=True, exist_ok=True)

    (raw_dir / "sample_notes.txt").write_text(
        "Hybrid retrieval combines lexical and semantic signals.\n",
        encoding="utf-8",
    )
    (processed_dir / "chunks.json").write_text(
        json.dumps(
            [{"id": "chunk-1", "text": "Hybrid retrieval combines lexical and semantic signals."}],
            indent=2,
        ),
        encoding="utf-8",
    )
    (index_dir / "default.json").write_text(
        json.dumps({"index_name": "demo-index", "embedding_model": "local-demo"}, indent=2),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
