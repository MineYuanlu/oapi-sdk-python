# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .password import Password


class ResetPasswordRequestBody(object):
    _types = {
        "password": Password,
        "user_id": str,
    }

    def __init__(self, d=None):
        self.password: Optional[Password] = None
        self.user_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ResetPasswordRequestBodyBuilder":
        return ResetPasswordRequestBodyBuilder()


class ResetPasswordRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._reset_password_request_body = ResetPasswordRequestBody()

    def password(self, password: Password) -> "ResetPasswordRequestBodyBuilder":
        self._reset_password_request_body.password = password
        return self

    def user_id(self, user_id: str) -> "ResetPasswordRequestBodyBuilder":
        self._reset_password_request_body.user_id = user_id
        return self

    def build(self) -> "ResetPasswordRequestBody":
        return self._reset_password_request_body
