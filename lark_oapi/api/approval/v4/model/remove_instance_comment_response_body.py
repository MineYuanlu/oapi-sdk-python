# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class RemoveInstanceCommentResponseBody(object):
    _types = {
        "instance_id": str,
        "external_id": str,
    }

    def __init__(self, d=None):
        self.instance_id: Optional[str] = None
        self.external_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "RemoveInstanceCommentResponseBodyBuilder":
        return RemoveInstanceCommentResponseBodyBuilder()


class RemoveInstanceCommentResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._remove_instance_comment_response_body = RemoveInstanceCommentResponseBody()

    def instance_id(self, instance_id: str) -> "RemoveInstanceCommentResponseBodyBuilder":
        self._remove_instance_comment_response_body.instance_id = instance_id
        return self

    def external_id(self, external_id: str) -> "RemoveInstanceCommentResponseBodyBuilder":
        self._remove_instance_comment_response_body.external_id = external_id
        return self

    def build(self) -> "RemoveInstanceCommentResponseBody":
        return self._remove_instance_comment_response_body
