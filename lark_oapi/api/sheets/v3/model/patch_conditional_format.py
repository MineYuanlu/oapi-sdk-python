# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .conditional_format_range import ConditionalFormatRange
from .conditional_format_rule import ConditionalFormatRule


class PatchConditionalFormat(object):
    _types = {
        "ranges": List[ConditionalFormatRange],
        "conditional_format_rule": ConditionalFormatRule,
        "index": int,
    }

    def __init__(self, d=None):
        self.ranges: Optional[List[ConditionalFormatRange]] = None
        self.conditional_format_rule: Optional[ConditionalFormatRule] = None
        self.index: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "PatchConditionalFormatBuilder":
        return PatchConditionalFormatBuilder()


class PatchConditionalFormatBuilder(object):
    def __init__(self) -> None:
        self._patch_conditional_format = PatchConditionalFormat()

    def ranges(self, ranges: List[ConditionalFormatRange]) -> "PatchConditionalFormatBuilder":
        self._patch_conditional_format.ranges = ranges
        return self

    def conditional_format_rule(self,
                                conditional_format_rule: ConditionalFormatRule) -> "PatchConditionalFormatBuilder":
        self._patch_conditional_format.conditional_format_rule = conditional_format_rule
        return self

    def index(self, index: int) -> "PatchConditionalFormatBuilder":
        self._patch_conditional_format.index = index
        return self

    def build(self) -> "PatchConditionalFormat":
        return self._patch_conditional_format
