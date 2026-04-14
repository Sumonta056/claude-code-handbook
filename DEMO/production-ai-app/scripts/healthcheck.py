"""Simple API healthcheck script."""

from __future__ import annotations

import json
import os
from urllib.request import urlopen


def main() -> None:
    base_url = os.getenv("API_BASE_URL", "http://127.0.0.1:8000")
    with urlopen(f"{base_url}/health", timeout=5) as response:
        payload = json.loads(response.read().decode("utf-8"))
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
