# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class ListTaskFollowerRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.page_size: Optional[int] = None
        self.page_token: Optional[str] = None
        self.user_id_type: Optional[str] = None
        self.task_id: Optional[str] = None

    @staticmethod
    def builder() -> "ListTaskFollowerRequestBuilder":
        return ListTaskFollowerRequestBuilder()


class ListTaskFollowerRequestBuilder(object):

    def __init__(self) -> None:
        list_task_follower_request = ListTaskFollowerRequest()
        list_task_follower_request.http_method = HttpMethod.GET
        list_task_follower_request.uri = "/open-apis/task/v1/tasks/:task_id/followers"
        list_task_follower_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._list_task_follower_request: ListTaskFollowerRequest = list_task_follower_request

    def page_size(self, page_size: int) -> "ListTaskFollowerRequestBuilder":
        self._list_task_follower_request.page_size = page_size
        self._list_task_follower_request.add_query("page_size", page_size)
        return self

    def page_token(self, page_token: str) -> "ListTaskFollowerRequestBuilder":
        self._list_task_follower_request.page_token = page_token
        self._list_task_follower_request.add_query("page_token", page_token)
        return self

    def user_id_type(self, user_id_type: str) -> "ListTaskFollowerRequestBuilder":
        self._list_task_follower_request.user_id_type = user_id_type
        self._list_task_follower_request.add_query("user_id_type", user_id_type)
        return self

    def task_id(self, task_id: str) -> "ListTaskFollowerRequestBuilder":
        self._list_task_follower_request.task_id = task_id
        self._list_task_follower_request.paths["task_id"] = str(task_id)
        return self

    def build(self) -> ListTaskFollowerRequest:
        return self._list_task_follower_request
