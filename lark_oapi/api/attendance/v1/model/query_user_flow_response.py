# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .query_user_flow_response_body import QueryUserFlowResponseBody


class QueryUserFlowResponse(BaseResponse):
    _types = {
        "data": QueryUserFlowResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[QueryUserFlowResponseBody] = None
        init(self, d, self._types)
