# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .user_contact_info import UserContactInfo


class BatchGetIdUserResponseBody(object):
    _types = {
        "user_list": List[UserContactInfo],
    }

    def __init__(self, d=None):
        self.user_list: Optional[List[UserContactInfo]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BatchGetIdUserResponseBodyBuilder":
        return BatchGetIdUserResponseBodyBuilder()


class BatchGetIdUserResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._batch_get_id_user_response_body = BatchGetIdUserResponseBody()

    def user_list(self, user_list: List[UserContactInfo]) -> "BatchGetIdUserResponseBodyBuilder":
        self._batch_get_id_user_response_body.user_list = user_list
        return self

    def build(self) -> "BatchGetIdUserResponseBody":
        return self._batch_get_id_user_response_body
