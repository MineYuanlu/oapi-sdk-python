# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .update_permission_public_password_response_body import UpdatePermissionPublicPasswordResponseBody


class UpdatePermissionPublicPasswordResponse(BaseResponse):
    _types = {
        "data": UpdatePermissionPublicPasswordResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[UpdatePermissionPublicPasswordResponseBody] = None
        init(self, d, self._types)
