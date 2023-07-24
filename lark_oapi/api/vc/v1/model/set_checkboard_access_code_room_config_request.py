# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .set_checkboard_access_code_room_config_request_body import SetCheckboardAccessCodeRoomConfigRequestBody


class SetCheckboardAccessCodeRoomConfigRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.request_body: Optional[SetCheckboardAccessCodeRoomConfigRequestBody] = None

    @staticmethod
    def builder() -> "SetCheckboardAccessCodeRoomConfigRequestBuilder":
        return SetCheckboardAccessCodeRoomConfigRequestBuilder()


class SetCheckboardAccessCodeRoomConfigRequestBuilder(object):

    def __init__(self) -> None:
        set_checkboard_access_code_room_config_request = SetCheckboardAccessCodeRoomConfigRequest()
        set_checkboard_access_code_room_config_request.http_method = HttpMethod.POST
        set_checkboard_access_code_room_config_request.uri = "/open-apis/vc/v1/room_configs/set_checkboard_access_code"
        set_checkboard_access_code_room_config_request.token_types = {AccessTokenType.TENANT}
        self._set_checkboard_access_code_room_config_request: SetCheckboardAccessCodeRoomConfigRequest = set_checkboard_access_code_room_config_request

    def request_body(self,
                     request_body: SetCheckboardAccessCodeRoomConfigRequestBody) -> "SetCheckboardAccessCodeRoomConfigRequestBuilder":
        self._set_checkboard_access_code_room_config_request.request_body = request_body
        self._set_checkboard_access_code_room_config_request.body = request_body
        return self

    def build(self) -> SetCheckboardAccessCodeRoomConfigRequest:
        return self._set_checkboard_access_code_room_config_request
