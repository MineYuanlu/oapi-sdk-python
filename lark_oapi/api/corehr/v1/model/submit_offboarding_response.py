# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .submit_offboarding_response_body import SubmitOffboardingResponseBody


class SubmitOffboardingResponse(BaseResponse):
    _types = {
        "data": SubmitOffboardingResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[SubmitOffboardingResponseBody] = None
        init(self, d, self._types)
