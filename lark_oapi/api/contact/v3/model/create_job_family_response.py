# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .create_job_family_response_body import CreateJobFamilyResponseBody


class CreateJobFamilyResponse(BaseResponse):
    _types = {
        "data": CreateJobFamilyResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[CreateJobFamilyResponseBody] = None
        init(self, d, self._types)
