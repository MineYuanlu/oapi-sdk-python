# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .search_chat_response_body import SearchChatResponseBody


class SearchChatResponse(BaseResponse):
    _types = {
        "data": SearchChatResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[SearchChatResponseBody] = None
        init(self, d, self._types)
