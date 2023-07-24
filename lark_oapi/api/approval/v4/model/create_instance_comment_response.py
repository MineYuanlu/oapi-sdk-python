# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .create_instance_comment_response_body import CreateInstanceCommentResponseBody


class CreateInstanceCommentResponse(BaseResponse):
    _types = {
        "data": CreateInstanceCommentResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[CreateInstanceCommentResponseBody] = None
        init(self, d, self._types)
