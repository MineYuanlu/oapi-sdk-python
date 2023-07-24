# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class ChildField(object):
    _types = {
        "code": str,
        "title": str,
        "time_unit": str,
    }

    def __init__(self, d=None):
        self.code: Optional[str] = None
        self.title: Optional[str] = None
        self.time_unit: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ChildFieldBuilder":
        return ChildFieldBuilder()


class ChildFieldBuilder(object):
    def __init__(self) -> None:
        self._child_field = ChildField()

    def code(self, code: str) -> "ChildFieldBuilder":
        self._child_field.code = code
        return self

    def title(self, title: str) -> "ChildFieldBuilder":
        self._child_field.title = title
        return self

    def time_unit(self, time_unit: str) -> "ChildFieldBuilder":
        self._child_field.time_unit = time_unit
        return self

    def build(self) -> "ChildField":
        return self._child_field
