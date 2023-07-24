# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class EventUid(object):
    _types = {
        "uid": str,
        "original_time": int,
    }

    def __init__(self, d=None):
        self.uid: Optional[str] = None
        self.original_time: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "EventUidBuilder":
        return EventUidBuilder()


class EventUidBuilder(object):
    def __init__(self) -> None:
        self._event_uid = EventUid()

    def uid(self, uid: str) -> "EventUidBuilder":
        self._event_uid.uid = uid
        return self

    def original_time(self, original_time: int) -> "EventUidBuilder":
        self._event_uid.original_time = original_time
        return self

    def build(self) -> "EventUid":
        return self._event_uid
