# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .get_import_task_response_body import GetImportTaskResponseBody


class GetImportTaskResponse(BaseResponse):
    _types = {
        "data": GetImportTaskResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[GetImportTaskResponseBody] = None
        init(self, d, self._types)
