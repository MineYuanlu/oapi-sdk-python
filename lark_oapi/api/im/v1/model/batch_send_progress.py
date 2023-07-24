# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class BatchSendProgress(object):
    _types = {
        "send_count": str,
        "total_send_count": str,
    }

    def __init__(self, d=None):
        self.send_count: Optional[str] = None
        self.total_send_count: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BatchSendProgressBuilder":
        return BatchSendProgressBuilder()


class BatchSendProgressBuilder(object):
    def __init__(self) -> None:
        self._batch_send_progress = BatchSendProgress()

    def send_count(self, send_count: str) -> "BatchSendProgressBuilder":
        self._batch_send_progress.send_count = send_count
        return self

    def total_send_count(self, total_send_count: str) -> "BatchSendProgressBuilder":
        self._batch_send_progress.total_send_count = total_send_count
        return self

    def build(self) -> "BatchSendProgress":
        return self._batch_send_progress
