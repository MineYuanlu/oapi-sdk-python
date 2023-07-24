# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .user import User


class BatchUserResponseBody(object):
    _types = {
        "items": List[User],
    }

    def __init__(self, d=None):
        self.items: Optional[List[User]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BatchUserResponseBodyBuilder":
        return BatchUserResponseBodyBuilder()


class BatchUserResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._batch_user_response_body = BatchUserResponseBody()

    def items(self, items: List[User]) -> "BatchUserResponseBodyBuilder":
        self._batch_user_response_body.items = items
        return self

    def build(self) -> "BatchUserResponseBody":
        return self._batch_user_response_body
