# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class ListApplicationAppVersionRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.lang: Optional[str] = None
        self.page_size: Optional[int] = None
        self.page_token: Optional[str] = None
        self.order: Optional[int] = None
        self.user_id_type: Optional[str] = None
        self.app_id: Optional[str] = None

    @staticmethod
    def builder() -> "ListApplicationAppVersionRequestBuilder":
        return ListApplicationAppVersionRequestBuilder()


class ListApplicationAppVersionRequestBuilder(object):

    def __init__(self) -> None:
        list_application_app_version_request = ListApplicationAppVersionRequest()
        list_application_app_version_request.http_method = HttpMethod.GET
        list_application_app_version_request.uri = "/open-apis/application/v6/applications/:app_id/app_versions"
        list_application_app_version_request.token_types = {AccessTokenType.TENANT}
        self._list_application_app_version_request: ListApplicationAppVersionRequest = list_application_app_version_request

    def lang(self, lang: str) -> "ListApplicationAppVersionRequestBuilder":
        self._list_application_app_version_request.lang = lang
        self._list_application_app_version_request.add_query("lang", lang)
        return self

    def page_size(self, page_size: int) -> "ListApplicationAppVersionRequestBuilder":
        self._list_application_app_version_request.page_size = page_size
        self._list_application_app_version_request.add_query("page_size", page_size)
        return self

    def page_token(self, page_token: str) -> "ListApplicationAppVersionRequestBuilder":
        self._list_application_app_version_request.page_token = page_token
        self._list_application_app_version_request.add_query("page_token", page_token)
        return self

    def order(self, order: int) -> "ListApplicationAppVersionRequestBuilder":
        self._list_application_app_version_request.order = order
        self._list_application_app_version_request.add_query("order", order)
        return self

    def user_id_type(self, user_id_type: str) -> "ListApplicationAppVersionRequestBuilder":
        self._list_application_app_version_request.user_id_type = user_id_type
        self._list_application_app_version_request.add_query("user_id_type", user_id_type)
        return self

    def app_id(self, app_id: str) -> "ListApplicationAppVersionRequestBuilder":
        self._list_application_app_version_request.app_id = app_id
        self._list_application_app_version_request.paths["app_id"] = str(app_id)
        return self

    def build(self) -> ListApplicationAppVersionRequest:
        return self._list_application_app_version_request
