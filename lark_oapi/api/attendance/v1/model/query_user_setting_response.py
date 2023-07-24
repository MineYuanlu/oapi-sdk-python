# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .query_user_setting_response_body import QueryUserSettingResponseBody


class QueryUserSettingResponse(BaseResponse):
    _types = {
        "data": QueryUserSettingResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[QueryUserSettingResponseBody] = None
        init(self, d, self._types)
