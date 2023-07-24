# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class ListApplicationRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.process_id: Optional[str] = None
        self.stage_id: Optional[str] = None
        self.talent_id: Optional[str] = None
        self.active_status: Optional[str] = None
        self.job_id: Optional[str] = None
        self.page_token: Optional[str] = None
        self.page_size: Optional[int] = None
        self.update_start_time: Optional[int] = None
        self.update_end_time: Optional[int] = None

    @staticmethod
    def builder() -> "ListApplicationRequestBuilder":
        return ListApplicationRequestBuilder()


class ListApplicationRequestBuilder(object):

    def __init__(self) -> None:
        list_application_request = ListApplicationRequest()
        list_application_request.http_method = HttpMethod.GET
        list_application_request.uri = "/open-apis/hire/v1/applications"
        list_application_request.token_types = {AccessTokenType.TENANT}
        self._list_application_request: ListApplicationRequest = list_application_request

    def process_id(self, process_id: str) -> "ListApplicationRequestBuilder":
        self._list_application_request.process_id = process_id
        self._list_application_request.add_query("process_id", process_id)
        return self

    def stage_id(self, stage_id: str) -> "ListApplicationRequestBuilder":
        self._list_application_request.stage_id = stage_id
        self._list_application_request.add_query("stage_id", stage_id)
        return self

    def talent_id(self, talent_id: str) -> "ListApplicationRequestBuilder":
        self._list_application_request.talent_id = talent_id
        self._list_application_request.add_query("talent_id", talent_id)
        return self

    def active_status(self, active_status: str) -> "ListApplicationRequestBuilder":
        self._list_application_request.active_status = active_status
        self._list_application_request.add_query("active_status", active_status)
        return self

    def job_id(self, job_id: str) -> "ListApplicationRequestBuilder":
        self._list_application_request.job_id = job_id
        self._list_application_request.add_query("job_id", job_id)
        return self

    def page_token(self, page_token: str) -> "ListApplicationRequestBuilder":
        self._list_application_request.page_token = page_token
        self._list_application_request.add_query("page_token", page_token)
        return self

    def page_size(self, page_size: int) -> "ListApplicationRequestBuilder":
        self._list_application_request.page_size = page_size
        self._list_application_request.add_query("page_size", page_size)
        return self

    def update_start_time(self, update_start_time: int) -> "ListApplicationRequestBuilder":
        self._list_application_request.update_start_time = update_start_time
        self._list_application_request.add_query("update_start_time", update_start_time)
        return self

    def update_end_time(self, update_end_time: int) -> "ListApplicationRequestBuilder":
        self._list_application_request.update_end_time = update_end_time
        self._list_application_request.add_query("update_end_time", update_end_time)
        return self

    def build(self) -> ListApplicationRequest:
        return self._list_application_request
