# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .count import Count
from .task import Task


class QueryTaskResponseBody(object):
    _types = {
        "tasks": List[Task],
        "page_token": str,
        "has_more": bool,
        "count": Count,
    }

    def __init__(self, d=None):
        self.tasks: Optional[List[Task]] = None
        self.page_token: Optional[str] = None
        self.has_more: Optional[bool] = None
        self.count: Optional[Count] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "QueryTaskResponseBodyBuilder":
        return QueryTaskResponseBodyBuilder()


class QueryTaskResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._query_task_response_body = QueryTaskResponseBody()

    def tasks(self, tasks: List[Task]) -> "QueryTaskResponseBodyBuilder":
        self._query_task_response_body.tasks = tasks
        return self

    def page_token(self, page_token: str) -> "QueryTaskResponseBodyBuilder":
        self._query_task_response_body.page_token = page_token
        return self

    def has_more(self, has_more: bool) -> "QueryTaskResponseBodyBuilder":
        self._query_task_response_body.has_more = has_more
        return self

    def count(self, count: Count) -> "QueryTaskResponseBodyBuilder":
        self._query_task_response_body.count = count
        return self

    def build(self) -> "QueryTaskResponseBody":
        return self._query_task_response_body
