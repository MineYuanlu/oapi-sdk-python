# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class ListAppTableViewRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.page_size: Optional[int] = None
        self.page_token: Optional[str] = None
        self.user_id_type: Optional[str] = None
        self.app_token: Optional[str] = None
        self.table_id: Optional[str] = None

    @staticmethod
    def builder() -> "ListAppTableViewRequestBuilder":
        return ListAppTableViewRequestBuilder()


class ListAppTableViewRequestBuilder(object):

    def __init__(self) -> None:
        list_app_table_view_request = ListAppTableViewRequest()
        list_app_table_view_request.http_method = HttpMethod.GET
        list_app_table_view_request.uri = "/open-apis/bitable/v1/apps/:app_token/tables/:table_id/views"
        list_app_table_view_request.token_types = {AccessTokenType.USER, AccessTokenType.TENANT}
        self._list_app_table_view_request: ListAppTableViewRequest = list_app_table_view_request

    def page_size(self, page_size: int) -> "ListAppTableViewRequestBuilder":
        self._list_app_table_view_request.page_size = page_size
        self._list_app_table_view_request.add_query("page_size", page_size)
        return self

    def page_token(self, page_token: str) -> "ListAppTableViewRequestBuilder":
        self._list_app_table_view_request.page_token = page_token
        self._list_app_table_view_request.add_query("page_token", page_token)
        return self

    def user_id_type(self, user_id_type: str) -> "ListAppTableViewRequestBuilder":
        self._list_app_table_view_request.user_id_type = user_id_type
        self._list_app_table_view_request.add_query("user_id_type", user_id_type)
        return self

    def app_token(self, app_token: str) -> "ListAppTableViewRequestBuilder":
        self._list_app_table_view_request.app_token = app_token
        self._list_app_table_view_request.paths["app_token"] = str(app_token)
        return self

    def table_id(self, table_id: str) -> "ListAppTableViewRequestBuilder":
        self._list_app_table_view_request.table_id = table_id
        self._list_app_table_view_request.paths["table_id"] = str(table_id)
        return self

    def build(self) -> ListAppTableViewRequest:
        return self._list_app_table_view_request
