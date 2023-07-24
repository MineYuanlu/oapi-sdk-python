# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class UpdatePermissionPublicPasswordResponseBody(object):
    _types = {
        "password": str,
    }

    def __init__(self, d=None):
        self.password: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UpdatePermissionPublicPasswordResponseBodyBuilder":
        return UpdatePermissionPublicPasswordResponseBodyBuilder()


class UpdatePermissionPublicPasswordResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._update_permission_public_password_response_body = UpdatePermissionPublicPasswordResponseBody()

    def password(self, password: str) -> "UpdatePermissionPublicPasswordResponseBodyBuilder":
        self._update_permission_public_password_response_body.password = password
        return self

    def build(self) -> "UpdatePermissionPublicPasswordResponseBody":
        return self._update_permission_public_password_response_body
