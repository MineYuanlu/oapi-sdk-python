# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class MgetRoomLevelRequestBody(object):
    _types = {
        "level_ids": List[str],
    }

    def __init__(self, d=None):
        self.level_ids: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "MgetRoomLevelRequestBodyBuilder":
        return MgetRoomLevelRequestBodyBuilder()


class MgetRoomLevelRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._mget_room_level_request_body = MgetRoomLevelRequestBody()

    def level_ids(self, level_ids: List[str]) -> "MgetRoomLevelRequestBodyBuilder":
        self._mget_room_level_request_body.level_ids = level_ids
        return self

    def build(self) -> "MgetRoomLevelRequestBody":
        return self._mget_room_level_request_body
