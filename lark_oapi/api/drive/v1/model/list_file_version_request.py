# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class ListFileVersionRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.page_size: Optional[int] = None
        self.page_token: Optional[str] = None
        self.obj_type: Optional[str] = None
        self.user_id_type: Optional[str] = None
        self.file_token: Optional[str] = None

    @staticmethod
    def builder() -> "ListFileVersionRequestBuilder":
        return ListFileVersionRequestBuilder()


class ListFileVersionRequestBuilder(object):

    def __init__(self) -> None:
        list_file_version_request = ListFileVersionRequest()
        list_file_version_request.http_method = HttpMethod.GET
        list_file_version_request.uri = "/open-apis/drive/v1/files/:file_token/versions"
        list_file_version_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._list_file_version_request: ListFileVersionRequest = list_file_version_request

    def page_size(self, page_size: int) -> "ListFileVersionRequestBuilder":
        self._list_file_version_request.page_size = page_size
        self._list_file_version_request.add_query("page_size", page_size)
        return self

    def page_token(self, page_token: str) -> "ListFileVersionRequestBuilder":
        self._list_file_version_request.page_token = page_token
        self._list_file_version_request.add_query("page_token", page_token)
        return self

    def obj_type(self, obj_type: str) -> "ListFileVersionRequestBuilder":
        self._list_file_version_request.obj_type = obj_type
        self._list_file_version_request.add_query("obj_type", obj_type)
        return self

    def user_id_type(self, user_id_type: str) -> "ListFileVersionRequestBuilder":
        self._list_file_version_request.user_id_type = user_id_type
        self._list_file_version_request.add_query("user_id_type", user_id_type)
        return self

    def file_token(self, file_token: str) -> "ListFileVersionRequestBuilder":
        self._list_file_version_request.file_token = file_token
        self._list_file_version_request.paths["file_token"] = str(file_token)
        return self

    def build(self) -> ListFileVersionRequest:
        return self._list_file_version_request
