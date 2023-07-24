# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .get_message_response_body import GetMessageResponseBody


class GetMessageResponse(BaseResponse):
    _types = {
        "data": GetMessageResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[GetMessageResponseBody] = None
        init(self, d, self._types)
