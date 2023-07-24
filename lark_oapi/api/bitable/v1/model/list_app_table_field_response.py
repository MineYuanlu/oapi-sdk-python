# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .list_app_table_field_response_body import ListAppTableFieldResponseBody


class ListAppTableFieldResponse(BaseResponse):
    _types = {
        "data": ListAppTableFieldResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[ListAppTableFieldResponseBody] = None
        init(self, d, self._types)
