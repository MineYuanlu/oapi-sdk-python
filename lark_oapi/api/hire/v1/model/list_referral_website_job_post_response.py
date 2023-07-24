# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .list_referral_website_job_post_response_body import ListReferralWebsiteJobPostResponseBody


class ListReferralWebsiteJobPostResponse(BaseResponse):
    _types = {
        "data": ListReferralWebsiteJobPostResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[ListReferralWebsiteJobPostResponseBody] = None
        init(self, d, self._types)
