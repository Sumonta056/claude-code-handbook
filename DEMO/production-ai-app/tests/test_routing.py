import unittest

from app.services.query_router import route_query


class RoutingTests(unittest.TestCase):
    def test_code_queries_route_to_code(self) -> None:
        self.assertEqual(route_query("Show me the code path for the query endpoint"), "code")

    def test_web_queries_route_to_web(self) -> None:
        self.assertEqual(route_query("What is the latest website guidance?"), "web")

    def test_docs_queries_route_to_docs(self) -> None:
        self.assertEqual(route_query("Open the API reference docs"), "docs")


if __name__ == "__main__":
    unittest.main()
