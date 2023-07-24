# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class GetDataSourceRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.data_source_id: Optional[str] = None

    @staticmethod
    def builder() -> "GetDataSourceRequestBuilder":
        return GetDataSourceRequestBuilder()


class GetDataSourceRequestBuilder(object):

    def __init__(self) -> None:
        get_data_source_request = GetDataSourceRequest()
        get_data_source_request.http_method = HttpMethod.GET
        get_data_source_request.uri = "/open-apis/search/v2/data_sources/:data_source_id"
        get_data_source_request.token_types = {AccessTokenType.TENANT}
        self._get_data_source_request: GetDataSourceRequest = get_data_source_request

    def data_source_id(self, data_source_id: str) -> "GetDataSourceRequestBuilder":
        self._get_data_source_request.data_source_id = data_source_id
        self._get_data_source_request.paths["data_source_id"] = str(data_source_id)
        return self

    def build(self) -> GetDataSourceRequest:
        return self._get_data_source_request
