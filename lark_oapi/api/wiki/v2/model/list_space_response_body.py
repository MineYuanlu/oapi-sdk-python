# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .space import Space


class ListSpaceResponseBody(object):
    _types = {
        "items": List[Space],
        "page_token": str,
        "has_more": bool,
    }

    def __init__(self, d=None):
        self.items: Optional[List[Space]] = None
        self.page_token: Optional[str] = None
        self.has_more: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListSpaceResponseBodyBuilder":
        return ListSpaceResponseBodyBuilder()


class ListSpaceResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._list_space_response_body = ListSpaceResponseBody()

    def items(self, items: List[Space]) -> "ListSpaceResponseBodyBuilder":
        self._list_space_response_body.items = items
        return self

    def page_token(self, page_token: str) -> "ListSpaceResponseBodyBuilder":
        self._list_space_response_body.page_token = page_token
        return self

    def has_more(self, has_more: bool) -> "ListSpaceResponseBodyBuilder":
        self._list_space_response_body.has_more = has_more
        return self

    def build(self) -> "ListSpaceResponseBody":
        return self._list_space_response_body
