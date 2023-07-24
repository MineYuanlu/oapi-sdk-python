# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class ApproverRange(object):
    _types = {
        "type": str,
        "id_list": List[str],
    }

    def __init__(self, d=None):
        self.type: Optional[str] = None
        self.id_list: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ApproverRangeBuilder":
        return ApproverRangeBuilder()


class ApproverRangeBuilder(object):
    def __init__(self) -> None:
        self._approver_range = ApproverRange()

    def type(self, type: str) -> "ApproverRangeBuilder":
        self._approver_range.type = type
        return self

    def id_list(self, id_list: List[str]) -> "ApproverRangeBuilder":
        self._approver_range.id_list = id_list
        return self

    def build(self) -> "ApproverRange":
        return self._approver_range
