# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .sheet_filter_info import SheetFilterInfo


class GetSpreadsheetSheetFilterResponseBody(object):
    _types = {
        "sheet_filter_info": SheetFilterInfo,
    }

    def __init__(self, d=None):
        self.sheet_filter_info: Optional[SheetFilterInfo] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetSpreadsheetSheetFilterResponseBodyBuilder":
        return GetSpreadsheetSheetFilterResponseBodyBuilder()


class GetSpreadsheetSheetFilterResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._get_spreadsheet_sheet_filter_response_body = GetSpreadsheetSheetFilterResponseBody()

    def sheet_filter_info(self, sheet_filter_info: SheetFilterInfo) -> "GetSpreadsheetSheetFilterResponseBodyBuilder":
        self._get_spreadsheet_sheet_filter_response_body.sheet_filter_info = sheet_filter_info
        return self

    def build(self) -> "GetSpreadsheetSheetFilterResponseBody":
        return self._get_spreadsheet_sheet_filter_response_body
