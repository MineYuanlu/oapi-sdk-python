# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .batch_delete_functional_role_member_response_body import BatchDeleteFunctionalRoleMemberResponseBody


class BatchDeleteFunctionalRoleMemberResponse(BaseResponse):
    _types = {
        "data": BatchDeleteFunctionalRoleMemberResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[BatchDeleteFunctionalRoleMemberResponseBody] = None
        init(self, d, self._types)
