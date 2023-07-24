# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .list_security_group_response_body import ListSecurityGroupResponseBody


class ListSecurityGroupResponse(BaseResponse):
    _types = {
        "data": ListSecurityGroupResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[ListSecurityGroupResponseBody] = None
        init(self, d, self._types)
