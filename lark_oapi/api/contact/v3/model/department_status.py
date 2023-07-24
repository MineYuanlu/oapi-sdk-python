# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class DepartmentStatus(object):
    _types = {
        "is_deleted": bool,
    }

    def __init__(self, d=None):
        self.is_deleted: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DepartmentStatusBuilder":
        return DepartmentStatusBuilder()


class DepartmentStatusBuilder(object):
    def __init__(self) -> None:
        self._department_status = DepartmentStatus()

    def is_deleted(self, is_deleted: bool) -> "DepartmentStatusBuilder":
        self._department_status.is_deleted = is_deleted
        return self

    def build(self) -> "DepartmentStatus":
        return self._department_status
