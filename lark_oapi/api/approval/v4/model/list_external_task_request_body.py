# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class ListExternalTaskRequestBody(object):
    _types = {
        "approval_codes": List[str],
        "instance_ids": List[str],
        "user_ids": List[str],
        "status": str,
    }

    def __init__(self, d=None):
        self.approval_codes: Optional[List[str]] = None
        self.instance_ids: Optional[List[str]] = None
        self.user_ids: Optional[List[str]] = None
        self.status: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListExternalTaskRequestBodyBuilder":
        return ListExternalTaskRequestBodyBuilder()


class ListExternalTaskRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._list_external_task_request_body = ListExternalTaskRequestBody()

    def approval_codes(self, approval_codes: List[str]) -> "ListExternalTaskRequestBodyBuilder":
        self._list_external_task_request_body.approval_codes = approval_codes
        return self

    def instance_ids(self, instance_ids: List[str]) -> "ListExternalTaskRequestBodyBuilder":
        self._list_external_task_request_body.instance_ids = instance_ids
        return self

    def user_ids(self, user_ids: List[str]) -> "ListExternalTaskRequestBodyBuilder":
        self._list_external_task_request_body.user_ids = user_ids
        return self

    def status(self, status: str) -> "ListExternalTaskRequestBodyBuilder":
        self._list_external_task_request_body.status = status
        return self

    def build(self) -> "ListExternalTaskRequestBody":
        return self._list_external_task_request_body
