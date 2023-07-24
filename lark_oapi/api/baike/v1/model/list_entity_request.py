# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class ListEntityRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.page_size: Optional[int] = None
        self.page_token: Optional[str] = None
        self.provider: Optional[str] = None
        self.user_id_type: Optional[str] = None

    @staticmethod
    def builder() -> "ListEntityRequestBuilder":
        return ListEntityRequestBuilder()


class ListEntityRequestBuilder(object):

    def __init__(self) -> None:
        list_entity_request = ListEntityRequest()
        list_entity_request.http_method = HttpMethod.GET
        list_entity_request.uri = "/open-apis/baike/v1/entities"
        list_entity_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._list_entity_request: ListEntityRequest = list_entity_request

    def page_size(self, page_size: int) -> "ListEntityRequestBuilder":
        self._list_entity_request.page_size = page_size
        self._list_entity_request.add_query("page_size", page_size)
        return self

    def page_token(self, page_token: str) -> "ListEntityRequestBuilder":
        self._list_entity_request.page_token = page_token
        self._list_entity_request.add_query("page_token", page_token)
        return self

    def provider(self, provider: str) -> "ListEntityRequestBuilder":
        self._list_entity_request.provider = provider
        self._list_entity_request.add_query("provider", provider)
        return self

    def user_id_type(self, user_id_type: str) -> "ListEntityRequestBuilder":
        self._list_entity_request.user_id_type = user_id_type
        self._list_entity_request.add_query("user_id_type", user_id_type)
        return self

    def build(self) -> ListEntityRequest:
        return self._list_entity_request
