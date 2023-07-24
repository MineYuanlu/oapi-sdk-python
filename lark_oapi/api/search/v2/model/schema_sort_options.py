# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class SchemaSortOptions(object):
    _types = {
        "priority": int,
        "order": str,
    }

    def __init__(self, d=None):
        self.priority: Optional[int] = None
        self.order: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SchemaSortOptionsBuilder":
        return SchemaSortOptionsBuilder()


class SchemaSortOptionsBuilder(object):
    def __init__(self) -> None:
        self._schema_sort_options = SchemaSortOptions()

    def priority(self, priority: int) -> "SchemaSortOptionsBuilder":
        self._schema_sort_options.priority = priority
        return self

    def order(self, order: str) -> "SchemaSortOptionsBuilder":
        self._schema_sort_options.order = order
        return self

    def build(self) -> "SchemaSortOptions":
        return self._schema_sort_options
