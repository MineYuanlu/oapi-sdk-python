# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .job import Job


class GetJobResponseBody(object):
    _types = {
        "job": Job,
    }

    def __init__(self, d=None):
        self.job: Optional[Job] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetJobResponseBodyBuilder":
        return GetJobResponseBodyBuilder()


class GetJobResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._get_job_response_body = GetJobResponseBody()

    def job(self, job: Job) -> "GetJobResponseBodyBuilder":
        self._get_job_response_body.job = job
        return self

    def build(self) -> "GetJobResponseBody":
        return self._get_job_response_body
