# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .user_allowed_remedy import UserAllowedRemedy


class QueryUserAllowedRemedysUserTaskRemedyResponseBody(object):
    _types = {
        "user_allowed_remedys": List[UserAllowedRemedy],
    }

    def __init__(self, d=None):
        self.user_allowed_remedys: Optional[List[UserAllowedRemedy]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "QueryUserAllowedRemedysUserTaskRemedyResponseBodyBuilder":
        return QueryUserAllowedRemedysUserTaskRemedyResponseBodyBuilder()


class QueryUserAllowedRemedysUserTaskRemedyResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._query_user_allowed_remedys_user_task_remedy_response_body = QueryUserAllowedRemedysUserTaskRemedyResponseBody()

    def user_allowed_remedys(self, user_allowed_remedys: List[
        UserAllowedRemedy]) -> "QueryUserAllowedRemedysUserTaskRemedyResponseBodyBuilder":
        self._query_user_allowed_remedys_user_task_remedy_response_body.user_allowed_remedys = user_allowed_remedys
        return self

    def build(self) -> "QueryUserAllowedRemedysUserTaskRemedyResponseBody":
        return self._query_user_allowed_remedys_user_task_remedy_response_body
