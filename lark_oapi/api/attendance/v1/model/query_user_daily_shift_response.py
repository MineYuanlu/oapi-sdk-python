# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .query_user_daily_shift_response_body import QueryUserDailyShiftResponseBody


class QueryUserDailyShiftResponse(BaseResponse):
    _types = {
        "data": QueryUserDailyShiftResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[QueryUserDailyShiftResponseBody] = None
        init(self, d, self._types)
