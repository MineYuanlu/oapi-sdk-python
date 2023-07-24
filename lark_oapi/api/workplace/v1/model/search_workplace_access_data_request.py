# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class SearchWorkplaceAccessDataRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.from_date: Optional[str] = None
        self.to_date: Optional[str] = None
        self.page_size: Optional[int] = None
        self.page_token: Optional[str] = None

    @staticmethod
    def builder() -> "SearchWorkplaceAccessDataRequestBuilder":
        return SearchWorkplaceAccessDataRequestBuilder()


class SearchWorkplaceAccessDataRequestBuilder(object):

    def __init__(self) -> None:
        search_workplace_access_data_request = SearchWorkplaceAccessDataRequest()
        search_workplace_access_data_request.http_method = HttpMethod.POST
        search_workplace_access_data_request.uri = "/open-apis/workplace/v1/workplace_access_data/search"
        search_workplace_access_data_request.token_types = {AccessTokenType.TENANT}
        self._search_workplace_access_data_request: SearchWorkplaceAccessDataRequest = search_workplace_access_data_request

    def from_date(self, from_date: str) -> "SearchWorkplaceAccessDataRequestBuilder":
        self._search_workplace_access_data_request.from_date = from_date
        self._search_workplace_access_data_request.add_query("from_date", from_date)
        return self

    def to_date(self, to_date: str) -> "SearchWorkplaceAccessDataRequestBuilder":
        self._search_workplace_access_data_request.to_date = to_date
        self._search_workplace_access_data_request.add_query("to_date", to_date)
        return self

    def page_size(self, page_size: int) -> "SearchWorkplaceAccessDataRequestBuilder":
        self._search_workplace_access_data_request.page_size = page_size
        self._search_workplace_access_data_request.add_query("page_size", page_size)
        return self

    def page_token(self, page_token: str) -> "SearchWorkplaceAccessDataRequestBuilder":
        self._search_workplace_access_data_request.page_token = page_token
        self._search_workplace_access_data_request.add_query("page_token", page_token)
        return self

    def build(self) -> SearchWorkplaceAccessDataRequest:
        return self._search_workplace_access_data_request
