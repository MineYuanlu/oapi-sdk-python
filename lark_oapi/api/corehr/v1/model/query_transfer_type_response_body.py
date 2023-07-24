# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .transfer_type import TransferType


class QueryTransferTypeResponseBody(object):
    _types = {
        "items": List[TransferType],
    }

    def __init__(self, d=None):
        self.items: Optional[List[TransferType]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "QueryTransferTypeResponseBodyBuilder":
        return QueryTransferTypeResponseBodyBuilder()


class QueryTransferTypeResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._query_transfer_type_response_body = QueryTransferTypeResponseBody()

    def items(self, items: List[TransferType]) -> "QueryTransferTypeResponseBodyBuilder":
        self._query_transfer_type_response_body.items = items
        return self

    def build(self) -> "QueryTransferTypeResponseBody":
        return self._query_transfer_type_response_body
