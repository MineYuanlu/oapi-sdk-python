# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .department import Department


class ListDepartmentResponseBody(object):
    _types = {
        "items": List[Department],
        "has_more": bool,
        "page_token": str,
    }

    def __init__(self, d=None):
        self.items: Optional[List[Department]] = None
        self.has_more: Optional[bool] = None
        self.page_token: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListDepartmentResponseBodyBuilder":
        return ListDepartmentResponseBodyBuilder()


class ListDepartmentResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._list_department_response_body = ListDepartmentResponseBody()

    def items(self, items: List[Department]) -> "ListDepartmentResponseBodyBuilder":
        self._list_department_response_body.items = items
        return self

    def has_more(self, has_more: bool) -> "ListDepartmentResponseBodyBuilder":
        self._list_department_response_body.has_more = has_more
        return self

    def page_token(self, page_token: str) -> "ListDepartmentResponseBodyBuilder":
        self._list_department_response_body.page_token = page_token
        return self

    def build(self) -> "ListDepartmentResponseBody":
        return self._list_department_response_body
