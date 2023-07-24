# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .find_condition import FindCondition


class Replace(object):
    _types = {
        "find_condition": FindCondition,
        "find": str,
        "replacement": str,
    }

    def __init__(self, d=None):
        self.find_condition: Optional[FindCondition] = None
        self.find: Optional[str] = None
        self.replacement: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ReplaceBuilder":
        return ReplaceBuilder()


class ReplaceBuilder(object):
    def __init__(self) -> None:
        self._replace = Replace()

    def find_condition(self, find_condition: FindCondition) -> "ReplaceBuilder":
        self._replace.find_condition = find_condition
        return self

    def find(self, find: str) -> "ReplaceBuilder":
        self._replace.find = find
        return self

    def replacement(self, replacement: str) -> "ReplaceBuilder":
        self._replace.replacement = replacement
        return self

    def build(self) -> "Replace":
        return self._replace
