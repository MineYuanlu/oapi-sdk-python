# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .copy_app_response_body import CopyAppResponseBody


class CopyAppResponse(BaseResponse):
    _types = {
        "data": CopyAppResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[CopyAppResponseBody] = None
        init(self, d, self._types)
