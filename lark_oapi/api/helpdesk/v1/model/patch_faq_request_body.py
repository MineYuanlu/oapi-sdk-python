# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .faq_update_info import FaqUpdateInfo


class PatchFaqRequestBody(object):
    _types = {
        "faq": FaqUpdateInfo,
    }

    def __init__(self, d=None):
        self.faq: Optional[FaqUpdateInfo] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "PatchFaqRequestBodyBuilder":
        return PatchFaqRequestBodyBuilder()


class PatchFaqRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._patch_faq_request_body = PatchFaqRequestBody()

    def faq(self, faq: FaqUpdateInfo) -> "PatchFaqRequestBodyBuilder":
        self._patch_faq_request_body.faq = faq
        return self

    def build(self) -> "PatchFaqRequestBody":
        return self._patch_faq_request_body
