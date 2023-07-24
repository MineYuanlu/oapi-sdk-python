# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class ListJobTitleRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.page_size: Optional[int] = None
        self.page_token: Optional[str] = None

    @staticmethod
    def builder() -> "ListJobTitleRequestBuilder":
        return ListJobTitleRequestBuilder()


class ListJobTitleRequestBuilder(object):

    def __init__(self) -> None:
        list_job_title_request = ListJobTitleRequest()
        list_job_title_request.http_method = HttpMethod.GET
        list_job_title_request.uri = "/open-apis/contact/v3/job_titles"
        list_job_title_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._list_job_title_request: ListJobTitleRequest = list_job_title_request

    def page_size(self, page_size: int) -> "ListJobTitleRequestBuilder":
        self._list_job_title_request.page_size = page_size
        self._list_job_title_request.add_query("page_size", page_size)
        return self

    def page_token(self, page_token: str) -> "ListJobTitleRequestBuilder":
        self._list_job_title_request.page_token = page_token
        self._list_job_title_request.add_query("page_token", page_token)
        return self

    def build(self) -> ListJobTitleRequest:
        return self._list_job_title_request
