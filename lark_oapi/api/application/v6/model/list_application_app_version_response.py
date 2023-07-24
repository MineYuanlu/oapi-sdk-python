# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .list_application_app_version_response_body import ListApplicationAppVersionResponseBody


class ListApplicationAppVersionResponse(BaseResponse):
    _types = {
        "data": ListApplicationAppVersionResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[ListApplicationAppVersionResponseBody] = None
        init(self, d, self._types)
