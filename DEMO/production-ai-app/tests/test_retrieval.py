import unittest

from app.models import QueryRequest
from app.services.rag_pipeline import RAGPipeline


class RetrievalTests(unittest.TestCase):
    def test_pipeline_returns_documents(self) -> None:
        pipeline = RAGPipeline()
        response = pipeline.run(QueryRequest(query="Explain retrieval and caching"))

        self.assertTrue(response.documents)
        self.assertTrue(response.answer)
        self.assertEqual(response.route, "rag")


if __name__ == "__main__":
    unittest.main()
