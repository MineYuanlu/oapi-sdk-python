# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .room import Room


class CreateRoomRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.request_body: Optional[Room] = None

    @staticmethod
    def builder() -> "CreateRoomRequestBuilder":
        return CreateRoomRequestBuilder()


class CreateRoomRequestBuilder(object):

    def __init__(self) -> None:
        create_room_request = CreateRoomRequest()
        create_room_request.http_method = HttpMethod.POST
        create_room_request.uri = "/open-apis/vc/v1/rooms"
        create_room_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._create_room_request: CreateRoomRequest = create_room_request

    def user_id_type(self, user_id_type: str) -> "CreateRoomRequestBuilder":
        self._create_room_request.user_id_type = user_id_type
        self._create_room_request.add_query("user_id_type", user_id_type)
        return self

    def request_body(self, request_body: Room) -> "CreateRoomRequestBuilder":
        self._create_room_request.request_body = request_body
        self._create_room_request.body = request_body
        return self

    def build(self) -> CreateRoomRequest:
        return self._create_room_request
