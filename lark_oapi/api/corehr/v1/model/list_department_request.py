# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class ListDepartmentRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.page_token: Optional[str] = None
        self.page_size: Optional[str] = None
        self.department_id_list: Optional[List[str]] = None
        self.name_list: Optional[List[str]] = None
        self.user_id_type: Optional[str] = None
        self.department_id_type: Optional[str] = None

    @staticmethod
    def builder() -> "ListDepartmentRequestBuilder":
        return ListDepartmentRequestBuilder()


class ListDepartmentRequestBuilder(object):

    def __init__(self) -> None:
        list_department_request = ListDepartmentRequest()
        list_department_request.http_method = HttpMethod.GET
        list_department_request.uri = "/open-apis/corehr/v1/departments"
        list_department_request.token_types = {AccessTokenType.TENANT}
        self._list_department_request: ListDepartmentRequest = list_department_request

    def page_token(self, page_token: str) -> "ListDepartmentRequestBuilder":
        self._list_department_request.page_token = page_token
        self._list_department_request.add_query("page_token", page_token)
        return self

    def page_size(self, page_size: str) -> "ListDepartmentRequestBuilder":
        self._list_department_request.page_size = page_size
        self._list_department_request.add_query("page_size", page_size)
        return self

    def department_id_list(self, department_id_list: List[str]) -> "ListDepartmentRequestBuilder":
        self._list_department_request.department_id_list = department_id_list
        self._list_department_request.add_query("department_id_list", department_id_list)
        return self

    def name_list(self, name_list: List[str]) -> "ListDepartmentRequestBuilder":
        self._list_department_request.name_list = name_list
        self._list_department_request.add_query("name_list", name_list)
        return self

    def user_id_type(self, user_id_type: str) -> "ListDepartmentRequestBuilder":
        self._list_department_request.user_id_type = user_id_type
        self._list_department_request.add_query("user_id_type", user_id_type)
        return self

    def department_id_type(self, department_id_type: str) -> "ListDepartmentRequestBuilder":
        self._list_department_request.department_id_type = department_id_type
        self._list_department_request.add_query("department_id_type", department_id_type)
        return self

    def build(self) -> ListDepartmentRequest:
        return self._list_department_request
