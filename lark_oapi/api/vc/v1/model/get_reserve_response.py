# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .get_reserve_response_body import GetReserveResponseBody


class GetReserveResponse(BaseResponse):
    _types = {
        "data": GetReserveResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[GetReserveResponseBody] = None
        init(self, d, self._types)
