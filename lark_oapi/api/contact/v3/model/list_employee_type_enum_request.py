# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class ListEmployeeTypeEnumRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.page_token: Optional[str] = None
        self.page_size: Optional[int] = None

    @staticmethod
    def builder() -> "ListEmployeeTypeEnumRequestBuilder":
        return ListEmployeeTypeEnumRequestBuilder()


class ListEmployeeTypeEnumRequestBuilder(object):

    def __init__(self) -> None:
        list_employee_type_enum_request = ListEmployeeTypeEnumRequest()
        list_employee_type_enum_request.http_method = HttpMethod.GET
        list_employee_type_enum_request.uri = "/open-apis/contact/v3/employee_type_enums"
        list_employee_type_enum_request.token_types = {AccessTokenType.TENANT}
        self._list_employee_type_enum_request: ListEmployeeTypeEnumRequest = list_employee_type_enum_request

    def page_token(self, page_token: str) -> "ListEmployeeTypeEnumRequestBuilder":
        self._list_employee_type_enum_request.page_token = page_token
        self._list_employee_type_enum_request.add_query("page_token", page_token)
        return self

    def page_size(self, page_size: int) -> "ListEmployeeTypeEnumRequestBuilder":
        self._list_employee_type_enum_request.page_size = page_size
        self._list_employee_type_enum_request.add_query("page_size", page_size)
        return self

    def build(self) -> ListEmployeeTypeEnumRequest:
        return self._list_employee_type_enum_request
