# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class BatchRecallProgress(object):
    _types = {
        "recall_count": str,
        "total_recall_count": str,
    }

    def __init__(self, d=None):
        self.recall_count: Optional[str] = None
        self.total_recall_count: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BatchRecallProgressBuilder":
        return BatchRecallProgressBuilder()


class BatchRecallProgressBuilder(object):
    def __init__(self) -> None:
        self._batch_recall_progress = BatchRecallProgress()

    def recall_count(self, recall_count: str) -> "BatchRecallProgressBuilder":
        self._batch_recall_progress.recall_count = recall_count
        return self

    def total_recall_count(self, total_recall_count: str) -> "BatchRecallProgressBuilder":
        self._batch_recall_progress.total_recall_count = total_recall_count
        return self

    def build(self) -> "BatchRecallProgress":
        return self._batch_recall_progress
