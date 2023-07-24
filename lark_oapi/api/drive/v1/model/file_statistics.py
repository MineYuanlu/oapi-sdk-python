# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class FileStatistics(object):
    _types = {
        "uv": int,
        "pv": int,
        "like_count": int,
        "timestamp": int,
    }

    def __init__(self, d=None):
        self.uv: Optional[int] = None
        self.pv: Optional[int] = None
        self.like_count: Optional[int] = None
        self.timestamp: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "FileStatisticsBuilder":
        return FileStatisticsBuilder()


class FileStatisticsBuilder(object):
    def __init__(self) -> None:
        self._file_statistics = FileStatistics()

    def uv(self, uv: int) -> "FileStatisticsBuilder":
        self._file_statistics.uv = uv
        return self

    def pv(self, pv: int) -> "FileStatisticsBuilder":
        self._file_statistics.pv = pv
        return self

    def like_count(self, like_count: int) -> "FileStatisticsBuilder":
        self._file_statistics.like_count = like_count
        return self

    def timestamp(self, timestamp: int) -> "FileStatisticsBuilder":
        self._file_statistics.timestamp = timestamp
        return self

    def build(self) -> "FileStatistics":
        return self._file_statistics
