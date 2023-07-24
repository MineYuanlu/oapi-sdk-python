# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .get_category_response_body import GetCategoryResponseBody


class GetCategoryResponse(BaseResponse):
    _types = {
        "data": GetCategoryResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[GetCategoryResponseBody] = None
        init(self, d, self._types)
