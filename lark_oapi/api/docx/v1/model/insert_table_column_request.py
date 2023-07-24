# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class InsertTableColumnRequest(object):
    _types = {
        "column_index": int,
    }

    def __init__(self, d=None):
        self.column_index: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "InsertTableColumnRequestBuilder":
        return InsertTableColumnRequestBuilder()


class InsertTableColumnRequestBuilder(object):
    def __init__(self) -> None:
        self._insert_table_column_request = InsertTableColumnRequest()

    def column_index(self, column_index: int) -> "InsertTableColumnRequestBuilder":
        self._insert_table_column_request.column_index = column_index
        return self

    def build(self) -> "InsertTableColumnRequest":
        return self._insert_table_column_request
