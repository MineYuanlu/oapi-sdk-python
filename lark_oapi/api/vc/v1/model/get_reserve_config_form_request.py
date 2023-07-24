# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class GetReserveConfigFormRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.scope_type: Optional[int] = None
        self.user_id_type: Optional[str] = None
        self.reserve_config_id: Optional[str] = None

    @staticmethod
    def builder() -> "GetReserveConfigFormRequestBuilder":
        return GetReserveConfigFormRequestBuilder()


class GetReserveConfigFormRequestBuilder(object):

    def __init__(self) -> None:
        get_reserve_config_form_request = GetReserveConfigFormRequest()
        get_reserve_config_form_request.http_method = HttpMethod.GET
        get_reserve_config_form_request.uri = "/open-apis/vc/v1/reserve_configs/:reserve_config_id/form"
        get_reserve_config_form_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._get_reserve_config_form_request: GetReserveConfigFormRequest = get_reserve_config_form_request

    def scope_type(self, scope_type: int) -> "GetReserveConfigFormRequestBuilder":
        self._get_reserve_config_form_request.scope_type = scope_type
        self._get_reserve_config_form_request.add_query("scope_type", scope_type)
        return self

    def user_id_type(self, user_id_type: str) -> "GetReserveConfigFormRequestBuilder":
        self._get_reserve_config_form_request.user_id_type = user_id_type
        self._get_reserve_config_form_request.add_query("user_id_type", user_id_type)
        return self

    def reserve_config_id(self, reserve_config_id: str) -> "GetReserveConfigFormRequestBuilder":
        self._get_reserve_config_form_request.reserve_config_id = reserve_config_id
        self._get_reserve_config_form_request.paths["reserve_config_id"] = str(reserve_config_id)
        return self

    def build(self) -> GetReserveConfigFormRequest:
        return self._get_reserve_config_form_request
