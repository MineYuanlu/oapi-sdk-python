# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .patch_data_source_request_body import PatchDataSourceRequestBody


class PatchDataSourceRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.data_source_id: Optional[str] = None
        self.request_body: Optional[PatchDataSourceRequestBody] = None

    @staticmethod
    def builder() -> "PatchDataSourceRequestBuilder":
        return PatchDataSourceRequestBuilder()


class PatchDataSourceRequestBuilder(object):

    def __init__(self) -> None:
        patch_data_source_request = PatchDataSourceRequest()
        patch_data_source_request.http_method = HttpMethod.PATCH
        patch_data_source_request.uri = "/open-apis/search/v2/data_sources/:data_source_id"
        patch_data_source_request.token_types = {AccessTokenType.TENANT}
        self._patch_data_source_request: PatchDataSourceRequest = patch_data_source_request

    def data_source_id(self, data_source_id: str) -> "PatchDataSourceRequestBuilder":
        self._patch_data_source_request.data_source_id = data_source_id
        self._patch_data_source_request.paths["data_source_id"] = str(data_source_id)
        return self

    def request_body(self, request_body: PatchDataSourceRequestBody) -> "PatchDataSourceRequestBuilder":
        self._patch_data_source_request.request_body = request_body
        self._patch_data_source_request.body = request_body
        return self

    def build(self) -> PatchDataSourceRequest:
        return self._patch_data_source_request
