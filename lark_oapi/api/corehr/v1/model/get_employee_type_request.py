# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class GetEmployeeTypeRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.employee_type_id: Optional[str] = None

    @staticmethod
    def builder() -> "GetEmployeeTypeRequestBuilder":
        return GetEmployeeTypeRequestBuilder()


class GetEmployeeTypeRequestBuilder(object):

    def __init__(self) -> None:
        get_employee_type_request = GetEmployeeTypeRequest()
        get_employee_type_request.http_method = HttpMethod.GET
        get_employee_type_request.uri = "/open-apis/corehr/v1/employee_types/:employee_type_id"
        get_employee_type_request.token_types = {AccessTokenType.TENANT}
        self._get_employee_type_request: GetEmployeeTypeRequest = get_employee_type_request

    def employee_type_id(self, employee_type_id: str) -> "GetEmployeeTypeRequestBuilder":
        self._get_employee_type_request.employee_type_id = employee_type_id
        self._get_employee_type_request.paths["employee_type_id"] = str(employee_type_id)
        return self

    def build(self) -> GetEmployeeTypeRequest:
        return self._get_employee_type_request
