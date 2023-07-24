# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class UnderauditlistApplicationRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.lang: Optional[str] = None
        self.page_token: Optional[str] = None
        self.page_size: Optional[int] = None
        self.user_id_type: Optional[str] = None

    @staticmethod
    def builder() -> "UnderauditlistApplicationRequestBuilder":
        return UnderauditlistApplicationRequestBuilder()


class UnderauditlistApplicationRequestBuilder(object):

    def __init__(self) -> None:
        underauditlist_application_request = UnderauditlistApplicationRequest()
        underauditlist_application_request.http_method = HttpMethod.GET
        underauditlist_application_request.uri = "/open-apis/application/v6/applications/underauditlist"
        underauditlist_application_request.token_types = {AccessTokenType.TENANT}
        self._underauditlist_application_request: UnderauditlistApplicationRequest = underauditlist_application_request

    def lang(self, lang: str) -> "UnderauditlistApplicationRequestBuilder":
        self._underauditlist_application_request.lang = lang
        self._underauditlist_application_request.add_query("lang", lang)
        return self

    def page_token(self, page_token: str) -> "UnderauditlistApplicationRequestBuilder":
        self._underauditlist_application_request.page_token = page_token
        self._underauditlist_application_request.add_query("page_token", page_token)
        return self

    def page_size(self, page_size: int) -> "UnderauditlistApplicationRequestBuilder":
        self._underauditlist_application_request.page_size = page_size
        self._underauditlist_application_request.add_query("page_size", page_size)
        return self

    def user_id_type(self, user_id_type: str) -> "UnderauditlistApplicationRequestBuilder":
        self._underauditlist_application_request.user_id_type = user_id_type
        self._underauditlist_application_request.add_query("user_id_type", user_id_type)
        return self

    def build(self) -> UnderauditlistApplicationRequest:
        return self._underauditlist_application_request
