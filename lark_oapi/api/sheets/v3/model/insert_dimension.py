# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .dimension import Dimension


class InsertDimension(object):
    _types = {
        "dimension_range": Dimension,
        "inherit_from": str,
    }

    def __init__(self, d=None):
        self.dimension_range: Optional[Dimension] = None
        self.inherit_from: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "InsertDimensionBuilder":
        return InsertDimensionBuilder()


class InsertDimensionBuilder(object):
    def __init__(self) -> None:
        self._insert_dimension = InsertDimension()

    def dimension_range(self, dimension_range: Dimension) -> "InsertDimensionBuilder":
        self._insert_dimension.dimension_range = dimension_range
        return self

    def inherit_from(self, inherit_from: str) -> "InsertDimensionBuilder":
        self._insert_dimension.inherit_from = inherit_from
        return self

    def build(self) -> "InsertDimension":
        return self._insert_dimension
