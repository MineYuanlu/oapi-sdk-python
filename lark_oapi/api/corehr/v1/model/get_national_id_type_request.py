# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class GetNationalIdTypeRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.national_id_type_id: Optional[str] = None

    @staticmethod
    def builder() -> "GetNationalIdTypeRequestBuilder":
        return GetNationalIdTypeRequestBuilder()


class GetNationalIdTypeRequestBuilder(object):

    def __init__(self) -> None:
        get_national_id_type_request = GetNationalIdTypeRequest()
        get_national_id_type_request.http_method = HttpMethod.GET
        get_national_id_type_request.uri = "/open-apis/corehr/v1/national_id_types/:national_id_type_id"
        get_national_id_type_request.token_types = {AccessTokenType.TENANT}
        self._get_national_id_type_request: GetNationalIdTypeRequest = get_national_id_type_request

    def national_id_type_id(self, national_id_type_id: str) -> "GetNationalIdTypeRequestBuilder":
        self._get_national_id_type_request.national_id_type_id = national_id_type_id
        self._get_national_id_type_request.paths["national_id_type_id"] = str(national_id_type_id)
        return self

    def build(self) -> GetNationalIdTypeRequest:
        return self._get_national_id_type_request
