# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .create_job_change_request_body import CreateJobChangeRequestBody


class CreateJobChangeRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.department_id_type: Optional[str] = None
        self.request_body: Optional[CreateJobChangeRequestBody] = None

    @staticmethod
    def builder() -> "CreateJobChangeRequestBuilder":
        return CreateJobChangeRequestBuilder()


class CreateJobChangeRequestBuilder(object):

    def __init__(self) -> None:
        create_job_change_request = CreateJobChangeRequest()
        create_job_change_request.http_method = HttpMethod.POST
        create_job_change_request.uri = "/open-apis/corehr/v1/job_changes"
        create_job_change_request.token_types = {AccessTokenType.TENANT}
        self._create_job_change_request: CreateJobChangeRequest = create_job_change_request

    def user_id_type(self, user_id_type: str) -> "CreateJobChangeRequestBuilder":
        self._create_job_change_request.user_id_type = user_id_type
        self._create_job_change_request.add_query("user_id_type", user_id_type)
        return self

    def department_id_type(self, department_id_type: str) -> "CreateJobChangeRequestBuilder":
        self._create_job_change_request.department_id_type = department_id_type
        self._create_job_change_request.add_query("department_id_type", department_id_type)
        return self

    def request_body(self, request_body: CreateJobChangeRequestBody) -> "CreateJobChangeRequestBuilder":
        self._create_job_change_request.request_body = request_body
        self._create_job_change_request.body = request_body
        return self

    def build(self) -> CreateJobChangeRequest:
        return self._create_job_change_request
