# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .level import Level


class CreateMotoRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.department_id_type: Optional[str] = None
        self.user_id_type: Optional[str] = None
        self.request_body: Optional[Level] = None

    @staticmethod
    def builder() -> "CreateMotoRequestBuilder":
        return CreateMotoRequestBuilder()


class CreateMotoRequestBuilder(object):

    def __init__(self) -> None:
        create_moto_request = CreateMotoRequest()
        create_moto_request.http_method = HttpMethod.POST
        create_moto_request.uri = "/open-apis/gray_test_open_sg/v1/motos"
        create_moto_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._create_moto_request: CreateMotoRequest = create_moto_request

    def department_id_type(self, department_id_type: str) -> "CreateMotoRequestBuilder":
        self._create_moto_request.department_id_type = department_id_type
        self._create_moto_request.add_query("department_id_type", department_id_type)
        return self

    def user_id_type(self, user_id_type: str) -> "CreateMotoRequestBuilder":
        self._create_moto_request.user_id_type = user_id_type
        self._create_moto_request.add_query("user_id_type", user_id_type)
        return self

    def request_body(self, request_body: Level) -> "CreateMotoRequestBuilder":
        self._create_moto_request.request_body = request_body
        self._create_moto_request.body = request_body
        return self

    def build(self) -> CreateMotoRequest:
        return self._create_moto_request
