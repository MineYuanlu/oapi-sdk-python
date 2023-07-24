# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .national_id_type import NationalIdType


class GetNationalIdTypeResponseBody(object):
    _types = {
        "national_id_type": NationalIdType,
    }

    def __init__(self, d=None):
        self.national_id_type: Optional[NationalIdType] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetNationalIdTypeResponseBodyBuilder":
        return GetNationalIdTypeResponseBodyBuilder()


class GetNationalIdTypeResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._get_national_id_type_response_body = GetNationalIdTypeResponseBody()

    def national_id_type(self, national_id_type: NationalIdType) -> "GetNationalIdTypeResponseBodyBuilder":
        self._get_national_id_type_response_body.national_id_type = national_id_type
        return self

    def build(self) -> "GetNationalIdTypeResponseBody":
        return self._get_national_id_type_response_body
