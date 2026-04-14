"""Offline evaluation runner for the demo dataset."""

from __future__ import annotations

import json
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from app.models import QueryRequest
from app.services.rag_pipeline import RAGPipeline


BASE_DIR = Path(__file__).resolve().parent
DATASET_PATH = BASE_DIR / "golden_dataset.json"
RESULTS_PATH = BASE_DIR / "eval_results" / "summary.json"


def run_offline_eval() -> dict[str, object]:
    pipeline = RAGPipeline()
    dataset = json.loads(DATASET_PATH.read_text(encoding="utf-8"))
    results: list[dict[str, object]] = []
    passed = 0

    for case in dataset:
        response = pipeline.run(QueryRequest(query=case["query"]))
        route_ok = response.route == case["expected_route"]
        snippet_ok = case["expected_snippet"].lower() in response.answer.lower()
        case_passed = route_ok and snippet_ok
        if case_passed:
            passed += 1

        results.append(
            {
                "query": case["query"],
                "route": response.route,
                "route_ok": route_ok,
                "snippet_ok": snippet_ok,
                "passed": case_passed,
            }
        )

    summary = {
        "total": len(dataset),
        "passed": passed,
        "score": round(passed / max(len(dataset), 1), 2),
    }
    RESULTS_PATH.write_text(
        json.dumps({"summary": summary, "results": results}, indent=2),
        encoding="utf-8",
    )
    return summary


if __name__ == "__main__":
    print(json.dumps(run_offline_eval(), indent=2))
