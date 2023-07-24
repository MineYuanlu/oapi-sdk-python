# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .list_tabs_chat_tab_response_body import ListTabsChatTabResponseBody


class ListTabsChatTabResponse(BaseResponse):
    _types = {
        "data": ListTabsChatTabResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[ListTabsChatTabResponseBody] = None
        init(self, d, self._types)
