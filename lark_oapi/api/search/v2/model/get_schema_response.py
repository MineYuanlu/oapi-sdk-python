# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .get_schema_response_body import GetSchemaResponseBody


class GetSchemaResponse(BaseResponse):
    _types = {
        "data": GetSchemaResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[GetSchemaResponseBody] = None
        init(self, d, self._types)
