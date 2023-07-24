# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class FindCondition(object):
    _types = {
        "range": str,
        "match_case": bool,
        "match_entire_cell": bool,
        "search_by_regex": bool,
        "include_formulas": bool,
    }

    def __init__(self, d=None):
        self.range: Optional[str] = None
        self.match_case: Optional[bool] = None
        self.match_entire_cell: Optional[bool] = None
        self.search_by_regex: Optional[bool] = None
        self.include_formulas: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "FindConditionBuilder":
        return FindConditionBuilder()


class FindConditionBuilder(object):
    def __init__(self) -> None:
        self._find_condition = FindCondition()

    def range(self, range: str) -> "FindConditionBuilder":
        self._find_condition.range = range
        return self

    def match_case(self, match_case: bool) -> "FindConditionBuilder":
        self._find_condition.match_case = match_case
        return self

    def match_entire_cell(self, match_entire_cell: bool) -> "FindConditionBuilder":
        self._find_condition.match_entire_cell = match_entire_cell
        return self

    def search_by_regex(self, search_by_regex: bool) -> "FindConditionBuilder":
        self._find_condition.search_by_regex = search_by_regex
        return self

    def include_formulas(self, include_formulas: bool) -> "FindConditionBuilder":
        self._find_condition.include_formulas = include_formulas
        return self

    def build(self) -> "FindCondition":
        return self._find_condition
