# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class PlainTextValueRange(object):
    _types = {
        "range": str,
        "values": List[list],
    }

    def __init__(self, d=None):
        self.range: Optional[str] = None
        self.values: Optional[List[list]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "PlainTextValueRangeBuilder":
        return PlainTextValueRangeBuilder()


class PlainTextValueRangeBuilder(object):
    def __init__(self) -> None:
        self._plain_text_value_range = PlainTextValueRange()

    def range(self, range: str) -> "PlainTextValueRangeBuilder":
        self._plain_text_value_range.range = range
        return self

    def values(self, values: List[list]) -> "PlainTextValueRangeBuilder":
        self._plain_text_value_range.values = values
        return self

    def build(self) -> "PlainTextValueRange":
        return self._plain_text_value_range
