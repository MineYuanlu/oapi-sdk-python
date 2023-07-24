# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class ListUserRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.page_size: Optional[int] = None
        self.page_token: Optional[str] = None
        self.user_id_type: Optional[str] = None

    @staticmethod
    def builder() -> "ListUserRequestBuilder":
        return ListUserRequestBuilder()


class ListUserRequestBuilder(object):

    def __init__(self) -> None:
        list_user_request = ListUserRequest()
        list_user_request.http_method = HttpMethod.GET
        list_user_request.uri = "/open-apis/acs/v1/users"
        list_user_request.token_types = {AccessTokenType.TENANT}
        self._list_user_request: ListUserRequest = list_user_request

    def page_size(self, page_size: int) -> "ListUserRequestBuilder":
        self._list_user_request.page_size = page_size
        self._list_user_request.add_query("page_size", page_size)
        return self

    def page_token(self, page_token: str) -> "ListUserRequestBuilder":
        self._list_user_request.page_token = page_token
        self._list_user_request.add_query("page_token", page_token)
        return self

    def user_id_type(self, user_id_type: str) -> "ListUserRequestBuilder":
        self._list_user_request.user_id_type = user_id_type
        self._list_user_request.add_query("user_id_type", user_id_type)
        return self

    def build(self) -> ListUserRequest:
        return self._list_user_request
