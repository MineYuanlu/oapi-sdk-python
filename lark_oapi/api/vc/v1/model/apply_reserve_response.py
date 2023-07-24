# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .apply_reserve_response_body import ApplyReserveResponseBody


class ApplyReserveResponse(BaseResponse):
    _types = {
        "data": ApplyReserveResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[ApplyReserveResponseBody] = None
        init(self, d, self._types)
