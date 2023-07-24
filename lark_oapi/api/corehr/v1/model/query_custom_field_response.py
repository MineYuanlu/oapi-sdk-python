# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .query_custom_field_response_body import QueryCustomFieldResponseBody


class QueryCustomFieldResponse(BaseResponse):
    _types = {
        "data": QueryCustomFieldResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[QueryCustomFieldResponseBody] = None
        init(self, d, self._types)
