# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .get_task_comment_response_body import GetTaskCommentResponseBody


class GetTaskCommentResponse(BaseResponse):
    _types = {
        "data": GetTaskCommentResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[GetTaskCommentResponseBody] = None
        init(self, d, self._types)
