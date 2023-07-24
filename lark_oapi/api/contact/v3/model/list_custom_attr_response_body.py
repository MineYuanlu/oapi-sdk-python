# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .custom_attr import CustomAttr


class ListCustomAttrResponseBody(object):
    _types = {
        "items": List[CustomAttr],
        "page_token": str,
        "has_more": bool,
    }

    def __init__(self, d=None):
        self.items: Optional[List[CustomAttr]] = None
        self.page_token: Optional[str] = None
        self.has_more: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListCustomAttrResponseBodyBuilder":
        return ListCustomAttrResponseBodyBuilder()


class ListCustomAttrResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._list_custom_attr_response_body = ListCustomAttrResponseBody()

    def items(self, items: List[CustomAttr]) -> "ListCustomAttrResponseBodyBuilder":
        self._list_custom_attr_response_body.items = items
        return self

    def page_token(self, page_token: str) -> "ListCustomAttrResponseBodyBuilder":
        self._list_custom_attr_response_body.page_token = page_token
        return self

    def has_more(self, has_more: bool) -> "ListCustomAttrResponseBodyBuilder":
        self._list_custom_attr_response_body.has_more = has_more
        return self

    def build(self) -> "ListCustomAttrResponseBody":
        return self._list_custom_attr_response_body
