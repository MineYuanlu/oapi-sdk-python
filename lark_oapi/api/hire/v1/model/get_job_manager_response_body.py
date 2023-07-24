# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .job_manager import JobManager


class GetJobManagerResponseBody(object):
    _types = {
        "info": JobManager,
    }

    def __init__(self, d=None):
        self.info: Optional[JobManager] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetJobManagerResponseBodyBuilder":
        return GetJobManagerResponseBodyBuilder()


class GetJobManagerResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._get_job_manager_response_body = GetJobManagerResponseBody()

    def info(self, info: JobManager) -> "GetJobManagerResponseBodyBuilder":
        self._get_job_manager_response_body.info = info
        return self

    def build(self) -> "GetJobManagerResponseBody":
        return self._get_job_manager_response_body
