# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .query_user_task_remedy_response_body import QueryUserTaskRemedyResponseBody


class QueryUserTaskRemedyResponse(BaseResponse):
    _types = {
        "data": QueryUserTaskRemedyResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[QueryUserTaskRemedyResponseBody] = None
        init(self, d, self._types)
