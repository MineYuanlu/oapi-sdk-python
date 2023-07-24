# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class DeleteSpreadsheetSheetFloatImageRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.spreadsheet_token: Optional[str] = None
        self.sheet_id: Optional[str] = None
        self.float_image_id: Optional[str] = None

    @staticmethod
    def builder() -> "DeleteSpreadsheetSheetFloatImageRequestBuilder":
        return DeleteSpreadsheetSheetFloatImageRequestBuilder()


class DeleteSpreadsheetSheetFloatImageRequestBuilder(object):

    def __init__(self) -> None:
        delete_spreadsheet_sheet_float_image_request = DeleteSpreadsheetSheetFloatImageRequest()
        delete_spreadsheet_sheet_float_image_request.http_method = HttpMethod.DELETE
        delete_spreadsheet_sheet_float_image_request.uri = "/open-apis/sheets/v3/spreadsheets/:spreadsheet_token/sheets/:sheet_id/float_images/:float_image_id"
        delete_spreadsheet_sheet_float_image_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._delete_spreadsheet_sheet_float_image_request: DeleteSpreadsheetSheetFloatImageRequest = delete_spreadsheet_sheet_float_image_request

    def spreadsheet_token(self, spreadsheet_token: str) -> "DeleteSpreadsheetSheetFloatImageRequestBuilder":
        self._delete_spreadsheet_sheet_float_image_request.spreadsheet_token = spreadsheet_token
        self._delete_spreadsheet_sheet_float_image_request.paths["spreadsheet_token"] = str(spreadsheet_token)
        return self

    def sheet_id(self, sheet_id: str) -> "DeleteSpreadsheetSheetFloatImageRequestBuilder":
        self._delete_spreadsheet_sheet_float_image_request.sheet_id = sheet_id
        self._delete_spreadsheet_sheet_float_image_request.paths["sheet_id"] = str(sheet_id)
        return self

    def float_image_id(self, float_image_id: str) -> "DeleteSpreadsheetSheetFloatImageRequestBuilder":
        self._delete_spreadsheet_sheet_float_image_request.float_image_id = float_image_id
        self._delete_spreadsheet_sheet_float_image_request.paths["float_image_id"] = str(float_image_id)
        return self

    def build(self) -> DeleteSpreadsheetSheetFloatImageRequest:
        return self._delete_spreadsheet_sheet_float_image_request
