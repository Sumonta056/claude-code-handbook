"""Small Flask frontend for exercising the API."""

from __future__ import annotations

import os

from flask import Flask, Response, render_template_string


app = Flask(__name__, static_folder="static")
API_BASE_URL = os.getenv("API_BASE_URL", "http://127.0.0.1:8000")
PORT = int(os.getenv("PORT", "5001"))


PAGE = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Production AI App Demo</title>
    <link rel="stylesheet" href="/static/styles.css">
  </head>
  <body>
    <main class="shell">
      <section class="panel">
        <p class="eyebrow">Frontend Demo</p>
        <h1>Production AI App</h1>
        <p class="lede">A tiny UI that sends queries to the FastAPI backend and shows traceable results.</p>
        <form id="query-form">
          <label for="query">Ask a question</label>
          <textarea id="query" name="query" rows="4">How does the code query endpoint work?</textarea>
          <button type="submit">Run Query</button>
        </form>
      </section>
      <section class="panel output">
        <p class="eyebrow">Response</p>
        <pre id="result">Waiting for query...</pre>
      </section>
    </main>
    <script>
      const form = document.getElementById("query-form");
      const result = document.getElementById("result");

      form.addEventListener("submit", async (event) => {
        event.preventDefault();
        result.textContent = "Loading...";

        const payload = {
          query: document.getElementById("query").value,
          session_id: "frontend-demo",
          top_k: 3
        };

        try {
          const response = await fetch("{{ api_base_url }}/query", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload)
          });
          const data = await response.json();
          result.textContent = JSON.stringify(data, null, 2);
        } catch (error) {
          result.textContent = "Request failed: " + error.message;
        }
      });
    </script>
  </body>
</html>
"""


@app.get("/")
def index() -> Response:
    return render_template_string(PAGE, api_base_url=API_BASE_URL)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT, debug=True)
