# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class OldUserObject(object):
    _types = {
        "department_ids": List[str],
        "open_id": str,
    }

    def __init__(self, d=None):
        self.department_ids: Optional[List[str]] = None
        self.open_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "OldUserObjectBuilder":
        return OldUserObjectBuilder()


class OldUserObjectBuilder(object):
    def __init__(self) -> None:
        self._old_user_object = OldUserObject()

    def department_ids(self, department_ids: List[str]) -> "OldUserObjectBuilder":
        self._old_user_object.department_ids = department_ids
        return self

    def open_id(self, open_id: str) -> "OldUserObjectBuilder":
        self._old_user_object.open_id = open_id
        return self

    def build(self) -> "OldUserObject":
        return self._old_user_object
