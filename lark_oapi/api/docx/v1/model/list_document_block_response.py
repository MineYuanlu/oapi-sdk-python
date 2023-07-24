# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .list_document_block_response_body import ListDocumentBlockResponseBody


class ListDocumentBlockResponse(BaseResponse):
    _types = {
        "data": ListDocumentBlockResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[ListDocumentBlockResponseBody] = None
        init(self, d, self._types)
