# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class SystemStatusUserCloseResultEntity(object):
    _types = {
        "user_id": str,
        "result": str,
    }

    def __init__(self, d=None):
        self.user_id: Optional[str] = None
        self.result: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SystemStatusUserCloseResultEntityBuilder":
        return SystemStatusUserCloseResultEntityBuilder()


class SystemStatusUserCloseResultEntityBuilder(object):
    def __init__(self) -> None:
        self._system_status_user_close_result_entity = SystemStatusUserCloseResultEntity()

    def user_id(self, user_id: str) -> "SystemStatusUserCloseResultEntityBuilder":
        self._system_status_user_close_result_entity.user_id = user_id
        return self

    def result(self, result: str) -> "SystemStatusUserCloseResultEntityBuilder":
        self._system_status_user_close_result_entity.result = result
        return self

    def build(self) -> "SystemStatusUserCloseResultEntity":
        return self._system_status_user_close_result_entity
