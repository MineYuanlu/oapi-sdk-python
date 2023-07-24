# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class RevertEvent(object):
    _types = {
        "type": str,
        "instance_code": str,
        "operate_time": int,
        "status": str,
    }

    def __init__(self, d=None):
        self.type: Optional[str] = None
        self.instance_code: Optional[str] = None
        self.operate_time: Optional[int] = None
        self.status: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "RevertEventBuilder":
        return RevertEventBuilder()


class RevertEventBuilder(object):
    def __init__(self) -> None:
        self._revert_event = RevertEvent()

    def type(self, type: str) -> "RevertEventBuilder":
        self._revert_event.type = type
        return self

    def instance_code(self, instance_code: str) -> "RevertEventBuilder":
        self._revert_event.instance_code = instance_code
        return self

    def operate_time(self, operate_time: int) -> "RevertEventBuilder":
        self._revert_event.operate_time = operate_time
        return self

    def status(self, status: str) -> "RevertEventBuilder":
        self._revert_event.status = status
        return self

    def build(self) -> "RevertEvent":
        return self._revert_event
