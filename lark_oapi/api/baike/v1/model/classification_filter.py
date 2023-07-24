# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class ClassificationFilter(object):
    _types = {
        "include": List[str],
        "exclude": List[str],
    }

    def __init__(self, d=None):
        self.include: Optional[List[str]] = None
        self.exclude: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ClassificationFilterBuilder":
        return ClassificationFilterBuilder()


class ClassificationFilterBuilder(object):
    def __init__(self) -> None:
        self._classification_filter = ClassificationFilter()

    def include(self, include: List[str]) -> "ClassificationFilterBuilder":
        self._classification_filter.include = include
        return self

    def exclude(self, exclude: List[str]) -> "ClassificationFilterBuilder":
        self._classification_filter.exclude = exclude
        return self

    def build(self) -> "ClassificationFilter":
        return self._classification_filter
