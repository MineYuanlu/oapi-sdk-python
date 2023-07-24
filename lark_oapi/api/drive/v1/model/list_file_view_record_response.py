# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .list_file_view_record_response_body import ListFileViewRecordResponseBody


class ListFileViewRecordResponse(BaseResponse):
    _types = {
        "data": ListFileViewRecordResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[ListFileViewRecordResponseBody] = None
        init(self, d, self._types)
