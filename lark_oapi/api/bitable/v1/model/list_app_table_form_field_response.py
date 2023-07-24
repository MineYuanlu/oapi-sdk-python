# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .list_app_table_form_field_response_body import ListAppTableFormFieldResponseBody


class ListAppTableFormFieldResponse(BaseResponse):
    _types = {
        "data": ListAppTableFormFieldResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[ListAppTableFormFieldResponseBody] = None
        init(self, d, self._types)
