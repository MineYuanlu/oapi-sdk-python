# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class ListUserOkrRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.offset: Optional[str] = None
        self.limit: Optional[str] = None
        self.lang: Optional[str] = None
        self.period_ids: Optional[List[str]] = None
        self.user_id: Optional[str] = None

    @staticmethod
    def builder() -> "ListUserOkrRequestBuilder":
        return ListUserOkrRequestBuilder()


class ListUserOkrRequestBuilder(object):

    def __init__(self) -> None:
        list_user_okr_request = ListUserOkrRequest()
        list_user_okr_request.http_method = HttpMethod.GET
        list_user_okr_request.uri = "/open-apis/okr/v1/users/:user_id/okrs"
        list_user_okr_request.token_types = {AccessTokenType.USER, AccessTokenType.TENANT}
        self._list_user_okr_request: ListUserOkrRequest = list_user_okr_request

    def user_id_type(self, user_id_type: str) -> "ListUserOkrRequestBuilder":
        self._list_user_okr_request.user_id_type = user_id_type
        self._list_user_okr_request.add_query("user_id_type", user_id_type)
        return self

    def offset(self, offset: str) -> "ListUserOkrRequestBuilder":
        self._list_user_okr_request.offset = offset
        self._list_user_okr_request.add_query("offset", offset)
        return self

    def limit(self, limit: str) -> "ListUserOkrRequestBuilder":
        self._list_user_okr_request.limit = limit
        self._list_user_okr_request.add_query("limit", limit)
        return self

    def lang(self, lang: str) -> "ListUserOkrRequestBuilder":
        self._list_user_okr_request.lang = lang
        self._list_user_okr_request.add_query("lang", lang)
        return self

    def period_ids(self, period_ids: List[str]) -> "ListUserOkrRequestBuilder":
        self._list_user_okr_request.period_ids = period_ids
        self._list_user_okr_request.add_query("period_ids", period_ids)
        return self

    def user_id(self, user_id: str) -> "ListUserOkrRequestBuilder":
        self._list_user_okr_request.user_id = user_id
        self._list_user_okr_request.paths["user_id"] = str(user_id)
        return self

    def build(self) -> ListUserOkrRequest:
        return self._list_user_okr_request
