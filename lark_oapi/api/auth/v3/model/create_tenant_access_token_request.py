# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod
from lark_oapi.core.model import BaseRequest
from .create_tenant_access_token_request_body import CreateTenantAccessTokenRequestBody


class CreateTenantAccessTokenRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.request_body: Optional[CreateTenantAccessTokenRequestBody] = None

    @staticmethod
    def builder() -> "CreateTenantAccessTokenRequestBuilder":
        return CreateTenantAccessTokenRequestBuilder()


class CreateTenantAccessTokenRequestBuilder(object):

    def __init__(self) -> None:
        create_tenant_access_token_request = CreateTenantAccessTokenRequest()
        create_tenant_access_token_request.http_method = HttpMethod.POST
        create_tenant_access_token_request.uri = "/open-apis/auth/v3/tenant_access_token"
        create_tenant_access_token_request.token_types = {}
        self._create_tenant_access_token_request: CreateTenantAccessTokenRequest = create_tenant_access_token_request

    def request_body(self, request_body: CreateTenantAccessTokenRequestBody) -> "CreateTenantAccessTokenRequestBuilder":
        self._create_tenant_access_token_request.request_body = request_body
        self._create_tenant_access_token_request.body = request_body
        return self

    def build(self) -> CreateTenantAccessTokenRequest:
        return self._create_tenant_access_token_request
