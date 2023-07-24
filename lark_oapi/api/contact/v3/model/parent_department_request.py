# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class ParentDepartmentRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.department_id_type: Optional[str] = None
        self.department_id: Optional[str] = None
        self.page_token: Optional[str] = None
        self.page_size: Optional[int] = None

    @staticmethod
    def builder() -> "ParentDepartmentRequestBuilder":
        return ParentDepartmentRequestBuilder()


class ParentDepartmentRequestBuilder(object):

    def __init__(self) -> None:
        parent_department_request = ParentDepartmentRequest()
        parent_department_request.http_method = HttpMethod.GET
        parent_department_request.uri = "/open-apis/contact/v3/departments/parent"
        parent_department_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._parent_department_request: ParentDepartmentRequest = parent_department_request

    def user_id_type(self, user_id_type: str) -> "ParentDepartmentRequestBuilder":
        self._parent_department_request.user_id_type = user_id_type
        self._parent_department_request.add_query("user_id_type", user_id_type)
        return self

    def department_id_type(self, department_id_type: str) -> "ParentDepartmentRequestBuilder":
        self._parent_department_request.department_id_type = department_id_type
        self._parent_department_request.add_query("department_id_type", department_id_type)
        return self

    def department_id(self, department_id: str) -> "ParentDepartmentRequestBuilder":
        self._parent_department_request.department_id = department_id
        self._parent_department_request.add_query("department_id", department_id)
        return self

    def page_token(self, page_token: str) -> "ParentDepartmentRequestBuilder":
        self._parent_department_request.page_token = page_token
        self._parent_department_request.add_query("page_token", page_token)
        return self

    def page_size(self, page_size: int) -> "ParentDepartmentRequestBuilder":
        self._parent_department_request.page_size = page_size
        self._parent_department_request.add_query("page_size", page_size)
        return self

    def build(self) -> ParentDepartmentRequest:
        return self._parent_department_request
