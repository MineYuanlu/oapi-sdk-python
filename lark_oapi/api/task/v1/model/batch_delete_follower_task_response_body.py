# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class BatchDeleteFollowerTaskResponseBody(object):
    _types = {
        "followers": List[str],
    }

    def __init__(self, d=None):
        self.followers: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BatchDeleteFollowerTaskResponseBodyBuilder":
        return BatchDeleteFollowerTaskResponseBodyBuilder()


class BatchDeleteFollowerTaskResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._batch_delete_follower_task_response_body = BatchDeleteFollowerTaskResponseBody()

    def followers(self, followers: List[str]) -> "BatchDeleteFollowerTaskResponseBodyBuilder":
        self._batch_delete_follower_task_response_body.followers = followers
        return self

    def build(self) -> "BatchDeleteFollowerTaskResponseBody":
        return self._batch_delete_follower_task_response_body
