# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .update_spreadsheet_sheet_filter_view_condition_response_body import \
    UpdateSpreadsheetSheetFilterViewConditionResponseBody


class UpdateSpreadsheetSheetFilterViewConditionResponse(BaseResponse):
    _types = {
        "data": UpdateSpreadsheetSheetFilterViewConditionResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[UpdateSpreadsheetSheetFilterViewConditionResponseBody] = None
        init(self, d, self._types)
