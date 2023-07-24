# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .room_level import RoomLevel


class MgetRoomLevelResponseBody(object):
    _types = {
        "items": List[RoomLevel],
    }

    def __init__(self, d=None):
        self.items: Optional[List[RoomLevel]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "MgetRoomLevelResponseBodyBuilder":
        return MgetRoomLevelResponseBodyBuilder()


class MgetRoomLevelResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._mget_room_level_response_body = MgetRoomLevelResponseBody()

    def items(self, items: List[RoomLevel]) -> "MgetRoomLevelResponseBodyBuilder":
        self._mget_room_level_response_body.items = items
        return self

    def build(self) -> "MgetRoomLevelResponseBody":
        return self._mget_room_level_response_body
