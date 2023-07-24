# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class InsertGridColumnRequest(object):
    _types = {
        "column_index": int,
    }

    def __init__(self, d=None):
        self.column_index: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "InsertGridColumnRequestBuilder":
        return InsertGridColumnRequestBuilder()


class InsertGridColumnRequestBuilder(object):
    def __init__(self) -> None:
        self._insert_grid_column_request = InsertGridColumnRequest()

    def column_index(self, column_index: int) -> "InsertGridColumnRequestBuilder":
        self._insert_grid_column_request.column_index = column_index
        return self

    def build(self) -> "InsertGridColumnRequest":
        return self._insert_grid_column_request
