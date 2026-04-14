import unittest

from app.models import QueryRequest
from app.services.rag_pipeline import RAGPipeline


class CacheTests(unittest.TestCase):
    def test_repeated_query_hits_cache(self) -> None:
        pipeline = RAGPipeline()
        request = QueryRequest(query="How does the router work?")

        first = pipeline.run(request)
        second = pipeline.run(request)

        self.assertIs(first.cached, False)
        self.assertIs(second.cached, True)
        self.assertIn("semantic-cache-hit", second.trace)


if __name__ == "__main__":
    unittest.main()
