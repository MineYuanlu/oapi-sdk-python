# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .reply_message_response_body import ReplyMessageResponseBody


class ReplyMessageResponse(BaseResponse):
    _types = {
        "data": ReplyMessageResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[ReplyMessageResponseBody] = None
        init(self, d, self._types)
