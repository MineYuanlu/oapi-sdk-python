# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class Statistics(object):
    _types = {
        "like_count": int,
        "dislike_count": int,
    }

    def __init__(self, d=None):
        self.like_count: Optional[int] = None
        self.dislike_count: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "StatisticsBuilder":
        return StatisticsBuilder()


class StatisticsBuilder(object):
    def __init__(self) -> None:
        self._statistics = Statistics()

    def like_count(self, like_count: int) -> "StatisticsBuilder":
        self._statistics.like_count = like_count
        return self

    def dislike_count(self, dislike_count: int) -> "StatisticsBuilder":
        self._statistics.dislike_count = dislike_count
        return self

    def build(self) -> "Statistics":
        return self._statistics
