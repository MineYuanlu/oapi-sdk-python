# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .get_active_meeting_reserve_response_body import GetActiveMeetingReserveResponseBody


class GetActiveMeetingReserveResponse(BaseResponse):
    _types = {
        "data": GetActiveMeetingReserveResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[GetActiveMeetingReserveResponseBody] = None
        init(self, d, self._types)
