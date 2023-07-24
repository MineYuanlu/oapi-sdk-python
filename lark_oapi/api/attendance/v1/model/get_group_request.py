# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class GetGroupRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.employee_type: Optional[str] = None
        self.dept_type: Optional[str] = None
        self.group_id: Optional[str] = None

    @staticmethod
    def builder() -> "GetGroupRequestBuilder":
        return GetGroupRequestBuilder()


class GetGroupRequestBuilder(object):

    def __init__(self) -> None:
        get_group_request = GetGroupRequest()
        get_group_request.http_method = HttpMethod.GET
        get_group_request.uri = "/open-apis/attendance/v1/groups/:group_id"
        get_group_request.token_types = {AccessTokenType.TENANT}
        self._get_group_request: GetGroupRequest = get_group_request

    def employee_type(self, employee_type: str) -> "GetGroupRequestBuilder":
        self._get_group_request.employee_type = employee_type
        self._get_group_request.add_query("employee_type", employee_type)
        return self

    def dept_type(self, dept_type: str) -> "GetGroupRequestBuilder":
        self._get_group_request.dept_type = dept_type
        self._get_group_request.add_query("dept_type", dept_type)
        return self

    def group_id(self, group_id: str) -> "GetGroupRequestBuilder":
        self._get_group_request.group_id = group_id
        self._get_group_request.paths["group_id"] = str(group_id)
        return self

    def build(self) -> GetGroupRequest:
        return self._get_group_request
