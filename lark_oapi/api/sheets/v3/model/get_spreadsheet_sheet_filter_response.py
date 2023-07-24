# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .get_spreadsheet_sheet_filter_response_body import GetSpreadsheetSheetFilterResponseBody


class GetSpreadsheetSheetFilterResponse(BaseResponse):
    _types = {
        "data": GetSpreadsheetSheetFilterResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[GetSpreadsheetSheetFilterResponseBody] = None
        init(self, d, self._types)
