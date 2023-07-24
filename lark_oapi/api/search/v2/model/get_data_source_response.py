# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .get_data_source_response_body import GetDataSourceResponseBody


class GetDataSourceResponse(BaseResponse):
    _types = {
        "data": GetDataSourceResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[GetDataSourceResponseBody] = None
        init(self, d, self._types)
