# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .filter_view_condition import FilterViewCondition


class GetSpreadsheetSheetFilterViewConditionResponseBody(object):
    _types = {
        "condition": FilterViewCondition,
    }

    def __init__(self, d=None):
        self.condition: Optional[FilterViewCondition] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetSpreadsheetSheetFilterViewConditionResponseBodyBuilder":
        return GetSpreadsheetSheetFilterViewConditionResponseBodyBuilder()


class GetSpreadsheetSheetFilterViewConditionResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._get_spreadsheet_sheet_filter_view_condition_response_body = GetSpreadsheetSheetFilterViewConditionResponseBody()

    def condition(self, condition: FilterViewCondition) -> "GetSpreadsheetSheetFilterViewConditionResponseBodyBuilder":
        self._get_spreadsheet_sheet_filter_view_condition_response_body.condition = condition
        return self

    def build(self) -> "GetSpreadsheetSheetFilterViewConditionResponseBody":
        return self._get_spreadsheet_sheet_filter_view_condition_response_body
