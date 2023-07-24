# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .period import Period


class ListPeriodResponseBody(object):
    _types = {
        "page_token": str,
        "has_more": bool,
        "items": List[Period],
    }

    def __init__(self, d=None):
        self.page_token: Optional[str] = None
        self.has_more: Optional[bool] = None
        self.items: Optional[List[Period]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListPeriodResponseBodyBuilder":
        return ListPeriodResponseBodyBuilder()


class ListPeriodResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._list_period_response_body = ListPeriodResponseBody()

    def page_token(self, page_token: str) -> "ListPeriodResponseBodyBuilder":
        self._list_period_response_body.page_token = page_token
        return self

    def has_more(self, has_more: bool) -> "ListPeriodResponseBodyBuilder":
        self._list_period_response_body.has_more = has_more
        return self

    def items(self, items: List[Period]) -> "ListPeriodResponseBodyBuilder":
        self._list_period_response_body.items = items
        return self

    def build(self) -> "ListPeriodResponseBody":
        return self._list_period_response_body
