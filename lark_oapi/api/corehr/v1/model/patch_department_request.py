# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .department import Department


class PatchDepartmentRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.client_token: Optional[str] = None
        self.user_id_type: Optional[str] = None
        self.department_id_type: Optional[str] = None
        self.department_id: Optional[str] = None
        self.request_body: Optional[Department] = None

    @staticmethod
    def builder() -> "PatchDepartmentRequestBuilder":
        return PatchDepartmentRequestBuilder()


class PatchDepartmentRequestBuilder(object):

    def __init__(self) -> None:
        patch_department_request = PatchDepartmentRequest()
        patch_department_request.http_method = HttpMethod.PATCH
        patch_department_request.uri = "/open-apis/corehr/v1/departments/:department_id"
        patch_department_request.token_types = {AccessTokenType.TENANT}
        self._patch_department_request: PatchDepartmentRequest = patch_department_request

    def client_token(self, client_token: str) -> "PatchDepartmentRequestBuilder":
        self._patch_department_request.client_token = client_token
        self._patch_department_request.add_query("client_token", client_token)
        return self

    def user_id_type(self, user_id_type: str) -> "PatchDepartmentRequestBuilder":
        self._patch_department_request.user_id_type = user_id_type
        self._patch_department_request.add_query("user_id_type", user_id_type)
        return self

    def department_id_type(self, department_id_type: str) -> "PatchDepartmentRequestBuilder":
        self._patch_department_request.department_id_type = department_id_type
        self._patch_department_request.add_query("department_id_type", department_id_type)
        return self

    def department_id(self, department_id: str) -> "PatchDepartmentRequestBuilder":
        self._patch_department_request.department_id = department_id
        self._patch_department_request.paths["department_id"] = str(department_id)
        return self

    def request_body(self, request_body: Department) -> "PatchDepartmentRequestBuilder":
        self._patch_department_request.request_body = request_body
        self._patch_department_request.body = request_body
        return self

    def build(self) -> PatchDepartmentRequest:
        return self._patch_department_request
