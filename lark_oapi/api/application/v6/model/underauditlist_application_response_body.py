# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .application import Application


class UnderauditlistApplicationResponseBody(object):
    _types = {
        "items": List[Application],
        "has_more": bool,
        "page_token": str,
    }

    def __init__(self, d=None):
        self.items: Optional[List[Application]] = None
        self.has_more: Optional[bool] = None
        self.page_token: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UnderauditlistApplicationResponseBodyBuilder":
        return UnderauditlistApplicationResponseBodyBuilder()


class UnderauditlistApplicationResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._underauditlist_application_response_body = UnderauditlistApplicationResponseBody()

    def items(self, items: List[Application]) -> "UnderauditlistApplicationResponseBodyBuilder":
        self._underauditlist_application_response_body.items = items
        return self

    def has_more(self, has_more: bool) -> "UnderauditlistApplicationResponseBodyBuilder":
        self._underauditlist_application_response_body.has_more = has_more
        return self

    def page_token(self, page_token: str) -> "UnderauditlistApplicationResponseBodyBuilder":
        self._underauditlist_application_response_body.page_token = page_token
        return self

    def build(self) -> "UnderauditlistApplicationResponseBody":
        return self._underauditlist_application_response_body
