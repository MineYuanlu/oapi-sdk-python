# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .access_record import AccessRecord


class ListAccessRecordResponseBody(object):
    _types = {
        "items": List[AccessRecord],
        "page_token": str,
        "has_more": bool,
    }

    def __init__(self, d=None):
        self.items: Optional[List[AccessRecord]] = None
        self.page_token: Optional[str] = None
        self.has_more: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListAccessRecordResponseBodyBuilder":
        return ListAccessRecordResponseBodyBuilder()


class ListAccessRecordResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._list_access_record_response_body = ListAccessRecordResponseBody()

    def items(self, items: List[AccessRecord]) -> "ListAccessRecordResponseBodyBuilder":
        self._list_access_record_response_body.items = items
        return self

    def page_token(self, page_token: str) -> "ListAccessRecordResponseBodyBuilder":
        self._list_access_record_response_body.page_token = page_token
        return self

    def has_more(self, has_more: bool) -> "ListAccessRecordResponseBodyBuilder":
        self._list_access_record_response_body.has_more = has_more
        return self

    def build(self) -> "ListAccessRecordResponseBody":
        return self._list_access_record_response_body
