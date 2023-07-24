# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class GetJobFamilyRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.job_family_id: Optional[str] = None

    @staticmethod
    def builder() -> "GetJobFamilyRequestBuilder":
        return GetJobFamilyRequestBuilder()


class GetJobFamilyRequestBuilder(object):

    def __init__(self) -> None:
        get_job_family_request = GetJobFamilyRequest()
        get_job_family_request.http_method = HttpMethod.GET
        get_job_family_request.uri = "/open-apis/contact/v3/job_families/:job_family_id"
        get_job_family_request.token_types = {AccessTokenType.TENANT}
        self._get_job_family_request: GetJobFamilyRequest = get_job_family_request

    def job_family_id(self, job_family_id: str) -> "GetJobFamilyRequestBuilder":
        self._get_job_family_request.job_family_id = job_family_id
        self._get_job_family_request.paths["job_family_id"] = str(job_family_id)
        return self

    def build(self) -> GetJobFamilyRequest:
        return self._get_job_family_request
