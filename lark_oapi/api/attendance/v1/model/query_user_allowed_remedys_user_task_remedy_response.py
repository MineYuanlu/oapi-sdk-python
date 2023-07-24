# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .query_user_allowed_remedys_user_task_remedy_response_body import QueryUserAllowedRemedysUserTaskRemedyResponseBody


class QueryUserAllowedRemedysUserTaskRemedyResponse(BaseResponse):
    _types = {
        "data": QueryUserAllowedRemedysUserTaskRemedyResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[QueryUserAllowedRemedysUserTaskRemedyResponseBody] = None
        init(self, d, self._types)
