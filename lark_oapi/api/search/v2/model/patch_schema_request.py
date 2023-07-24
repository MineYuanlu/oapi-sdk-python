# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .patch_schema_request_body import PatchSchemaRequestBody


class PatchSchemaRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.schema_id: Optional[str] = None
        self.request_body: Optional[PatchSchemaRequestBody] = None

    @staticmethod
    def builder() -> "PatchSchemaRequestBuilder":
        return PatchSchemaRequestBuilder()


class PatchSchemaRequestBuilder(object):

    def __init__(self) -> None:
        patch_schema_request = PatchSchemaRequest()
        patch_schema_request.http_method = HttpMethod.PATCH
        patch_schema_request.uri = "/open-apis/search/v2/schemas/:schema_id"
        patch_schema_request.token_types = {AccessTokenType.TENANT}
        self._patch_schema_request: PatchSchemaRequest = patch_schema_request

    def schema_id(self, schema_id: str) -> "PatchSchemaRequestBuilder":
        self._patch_schema_request.schema_id = schema_id
        self._patch_schema_request.paths["schema_id"] = str(schema_id)
        return self

    def request_body(self, request_body: PatchSchemaRequestBody) -> "PatchSchemaRequestBuilder":
        self._patch_schema_request.request_body = request_body
        self._patch_schema_request.body = request_body
        return self

    def build(self) -> PatchSchemaRequest:
        return self._patch_schema_request
