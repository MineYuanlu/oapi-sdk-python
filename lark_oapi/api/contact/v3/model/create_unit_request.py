# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .create_unit_request_body import CreateUnitRequestBody


class CreateUnitRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.request_body: Optional[CreateUnitRequestBody] = None

    @staticmethod
    def builder() -> "CreateUnitRequestBuilder":
        return CreateUnitRequestBuilder()


class CreateUnitRequestBuilder(object):

    def __init__(self) -> None:
        create_unit_request = CreateUnitRequest()
        create_unit_request.http_method = HttpMethod.POST
        create_unit_request.uri = "/open-apis/contact/v3/unit"
        create_unit_request.token_types = {AccessTokenType.TENANT}
        self._create_unit_request: CreateUnitRequest = create_unit_request

    def request_body(self, request_body: CreateUnitRequestBody) -> "CreateUnitRequestBuilder":
        self._create_unit_request.request_body = request_body
        self._create_unit_request.body = request_body
        return self

    def build(self) -> CreateUnitRequest:
        return self._create_unit_request
