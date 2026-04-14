"""End-to-end orchestration for the demo RAG flow."""

from __future__ import annotations

from dataclasses import replace

from agents.adaptive_router import AdaptiveRouter
from agents.document_grader import DocumentGrader
from agents.query_decomposer import QueryDecomposer
from agents.tools.code_search import CodeSearchTool
from agents.tools.vector_search import VectorSearchTool
from agents.tools.web_search import WebSearchTool
from app.components.hybrid_retriever import HybridRetriever
from app.components.reranker import Reranker
from app.config import settings
from app.models import QueryRequest, QueryResponse, RetrievedDocument
from app.services.conversation import ConversationStore
from app.services.query_rewriter import rewrite_query
from app.services.query_router import route_query
from app.services.semantic_cache import SemanticCache
from observability.cost_tracker import CostTracker
from observability.feedback import FeedbackStore
from observability.tracer import TraceRecorder
from prompts.registry import PromptRegistry
from security.content_filter import filter_documents
from security.input_guard import validate_input
from security.output_filter import filter_output


class RAGPipeline:
    def __init__(self) -> None:
        self.cache = SemanticCache()
        self.conversation = ConversationStore()
        self.retriever = HybridRetriever()
        self.reranker = Reranker()
        self.decomposer = QueryDecomposer()
        self.router = AdaptiveRouter(default_route=settings.default_route)
        self.grader = DocumentGrader()
        self.prompts = PromptRegistry()
        self.vector_tool = VectorSearchTool()
        self.web_tool = WebSearchTool()
        self.code_tool = CodeSearchTool()
        self.feedback = FeedbackStore()

    def run(self, request: QueryRequest) -> QueryResponse:
        trace = TraceRecorder()
        tracker = CostTracker()

        cleaned_query = validate_input(request.query)
        trace.log("input-accepted")

        cached = self.cache.get(cleaned_query)
        if cached:
            trace.log("semantic-cache-hit")
            cached_response = replace(
                cached,
                cached=True,
                trace=[*cached.trace, *trace.snapshot()],
            )
            return cached_response

        history = self.conversation.get_history(request.session_id)
        rewritten_query = rewrite_query(cleaned_query, history)
        trace.log("query-rewritten")

        subqueries = self.decomposer.decompose(rewritten_query)
        suggested_route = route_query(rewritten_query, default_route=settings.default_route)
        route = self.router.choose_route(rewritten_query, suggested_route, subqueries)
        trace.log(f"route:{route}")

        candidate_documents = self._search(route, rewritten_query)
        retrieved_documents = self.retriever.retrieve(
            query=rewritten_query,
            top_k=request.top_k or settings.top_k,
            candidates=candidate_documents,
        )
        trace.log("documents-retrieved")

        reranked_documents = self.reranker.rerank(rewritten_query, retrieved_documents, request.top_k)
        graded_documents = self.grader.grade(rewritten_query, reranked_documents)
        safe_documents = filter_documents(graded_documents)
        trace.log("documents-filtered")

        answer = self.prompts.render_answer(route, rewritten_query, safe_documents)
        answer = filter_output(answer)
        tracker.add(query=rewritten_query, answer=answer, documents=safe_documents)
        trace.log(tracker.summary())

        response = QueryResponse(
            answer=answer,
            route=route,
            cached=False,
            documents=safe_documents,
            trace=trace.snapshot(),
        )

        self.cache.set(cleaned_query, response)
        self.conversation.append(request.session_id, "user", cleaned_query, settings.max_history_messages)
        self.conversation.append(request.session_id, "assistant", answer, settings.max_history_messages)
        return response

    def _search(self, route: str, query: str) -> list[RetrievedDocument]:
        if route == "code":
            return self.code_tool.search(query)
        if route == "web":
            return self.web_tool.search(query)
        return self.vector_tool.search(query)
