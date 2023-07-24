# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class MaskSession(object):
    _types = {
        "create_time": int,
        "terminal_type": int,
        "user_id": str,
    }

    def __init__(self, d=None):
        self.create_time: Optional[int] = None
        self.terminal_type: Optional[int] = None
        self.user_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "MaskSessionBuilder":
        return MaskSessionBuilder()


class MaskSessionBuilder(object):
    def __init__(self) -> None:
        self._mask_session = MaskSession()

    def create_time(self, create_time: int) -> "MaskSessionBuilder":
        self._mask_session.create_time = create_time
        return self

    def terminal_type(self, terminal_type: int) -> "MaskSessionBuilder":
        self._mask_session.terminal_type = terminal_type
        return self

    def user_id(self, user_id: str) -> "MaskSessionBuilder":
        self._mask_session.user_id = user_id
        return self

    def build(self) -> "MaskSession":
        return self._mask_session
