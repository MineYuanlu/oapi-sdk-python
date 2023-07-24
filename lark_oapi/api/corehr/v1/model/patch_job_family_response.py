# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .patch_job_family_response_body import PatchJobFamilyResponseBody


class PatchJobFamilyResponse(BaseResponse):
    _types = {
        "data": PatchJobFamilyResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[PatchJobFamilyResponseBody] = None
        init(self, d, self._types)
