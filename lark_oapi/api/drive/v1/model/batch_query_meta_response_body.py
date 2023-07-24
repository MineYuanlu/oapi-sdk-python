# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .meta import Meta
from .meta_failed import MetaFailed


class BatchQueryMetaResponseBody(object):
    _types = {
        "metas": List[Meta],
        "failed_list": List[MetaFailed],
    }

    def __init__(self, d=None):
        self.metas: Optional[List[Meta]] = None
        self.failed_list: Optional[List[MetaFailed]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BatchQueryMetaResponseBodyBuilder":
        return BatchQueryMetaResponseBodyBuilder()


class BatchQueryMetaResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._batch_query_meta_response_body = BatchQueryMetaResponseBody()

    def metas(self, metas: List[Meta]) -> "BatchQueryMetaResponseBodyBuilder":
        self._batch_query_meta_response_body.metas = metas
        return self

    def failed_list(self, failed_list: List[MetaFailed]) -> "BatchQueryMetaResponseBodyBuilder":
        self._batch_query_meta_response_body.failed_list = failed_list
        return self

    def build(self) -> "BatchQueryMetaResponseBody":
        return self._batch_query_meta_response_body
