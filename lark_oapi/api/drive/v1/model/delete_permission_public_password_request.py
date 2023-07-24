# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class DeletePermissionPublicPasswordRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.type: Optional[str] = None
        self.token: Optional[str] = None

    @staticmethod
    def builder() -> "DeletePermissionPublicPasswordRequestBuilder":
        return DeletePermissionPublicPasswordRequestBuilder()


class DeletePermissionPublicPasswordRequestBuilder(object):

    def __init__(self) -> None:
        delete_permission_public_password_request = DeletePermissionPublicPasswordRequest()
        delete_permission_public_password_request.http_method = HttpMethod.DELETE
        delete_permission_public_password_request.uri = "/open-apis/drive/v1/permissions/:token/public/password"
        delete_permission_public_password_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._delete_permission_public_password_request: DeletePermissionPublicPasswordRequest = delete_permission_public_password_request

    def type(self, type: str) -> "DeletePermissionPublicPasswordRequestBuilder":
        self._delete_permission_public_password_request.type = type
        self._delete_permission_public_password_request.add_query("type", type)
        return self

    def token(self, token: str) -> "DeletePermissionPublicPasswordRequestBuilder":
        self._delete_permission_public_password_request.token = token
        self._delete_permission_public_password_request.paths["token"] = str(token)
        return self

    def build(self) -> DeletePermissionPublicPasswordRequest:
        return self._delete_permission_public_password_request
