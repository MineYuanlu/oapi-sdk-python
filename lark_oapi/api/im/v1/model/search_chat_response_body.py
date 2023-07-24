# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .list_chat import ListChat


class SearchChatResponseBody(object):
    _types = {
        "items": List[ListChat],
        "page_token": str,
        "has_more": bool,
    }

    def __init__(self, d=None):
        self.items: Optional[List[ListChat]] = None
        self.page_token: Optional[str] = None
        self.has_more: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SearchChatResponseBodyBuilder":
        return SearchChatResponseBodyBuilder()


class SearchChatResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._search_chat_response_body = SearchChatResponseBody()

    def items(self, items: List[ListChat]) -> "SearchChatResponseBodyBuilder":
        self._search_chat_response_body.items = items
        return self

    def page_token(self, page_token: str) -> "SearchChatResponseBodyBuilder":
        self._search_chat_response_body.page_token = page_token
        return self

    def has_more(self, has_more: bool) -> "SearchChatResponseBodyBuilder":
        self._search_chat_response_body.has_more = has_more
        return self

    def build(self) -> "SearchChatResponseBody":
        return self._search_chat_response_body
