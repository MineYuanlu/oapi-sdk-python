# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .group import Group


class PatchGroupRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.department_id_type: Optional[str] = None
        self.group_id: Optional[str] = None
        self.request_body: Optional[Group] = None

    @staticmethod
    def builder() -> "PatchGroupRequestBuilder":
        return PatchGroupRequestBuilder()


class PatchGroupRequestBuilder(object):

    def __init__(self) -> None:
        patch_group_request = PatchGroupRequest()
        patch_group_request.http_method = HttpMethod.PATCH
        patch_group_request.uri = "/open-apis/contact/v3/group/:group_id"
        patch_group_request.token_types = {AccessTokenType.TENANT}
        self._patch_group_request: PatchGroupRequest = patch_group_request

    def user_id_type(self, user_id_type: str) -> "PatchGroupRequestBuilder":
        self._patch_group_request.user_id_type = user_id_type
        self._patch_group_request.add_query("user_id_type", user_id_type)
        return self

    def department_id_type(self, department_id_type: str) -> "PatchGroupRequestBuilder":
        self._patch_group_request.department_id_type = department_id_type
        self._patch_group_request.add_query("department_id_type", department_id_type)
        return self

    def group_id(self, group_id: str) -> "PatchGroupRequestBuilder":
        self._patch_group_request.group_id = group_id
        self._patch_group_request.paths["group_id"] = str(group_id)
        return self

    def request_body(self, request_body: Group) -> "PatchGroupRequestBuilder":
        self._patch_group_request.request_body = request_body
        self._patch_group_request.body = request_body
        return self

    def build(self) -> PatchGroupRequest:
        return self._patch_group_request
