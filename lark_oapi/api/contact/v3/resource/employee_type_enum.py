# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.create_employee_type_enum_request import CreateEmployeeTypeEnumRequest
from ..model.create_employee_type_enum_response import CreateEmployeeTypeEnumResponse
from ..model.delete_employee_type_enum_request import DeleteEmployeeTypeEnumRequest
from ..model.delete_employee_type_enum_response import DeleteEmployeeTypeEnumResponse
from ..model.list_employee_type_enum_request import ListEmployeeTypeEnumRequest
from ..model.list_employee_type_enum_response import ListEmployeeTypeEnumResponse
from ..model.update_employee_type_enum_request import UpdateEmployeeTypeEnumRequest
from ..model.update_employee_type_enum_response import UpdateEmployeeTypeEnumResponse


class EmployeeTypeEnum(object):
    def __init__(self, config: Config) -> None:
        self.config: Optional[Config] = config

    def create(self, request: CreateEmployeeTypeEnumRequest,
               option: Optional[RequestOption] = None) -> CreateEmployeeTypeEnumResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: CreateEmployeeTypeEnumResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                  CreateEmployeeTypeEnumResponse)
        response.raw = resp

        return response

    def delete(self, request: DeleteEmployeeTypeEnumRequest,
               option: Optional[RequestOption] = None) -> DeleteEmployeeTypeEnumResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: DeleteEmployeeTypeEnumResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                  DeleteEmployeeTypeEnumResponse)
        response.raw = resp

        return response

    def list(self, request: ListEmployeeTypeEnumRequest,
             option: Optional[RequestOption] = None) -> ListEmployeeTypeEnumResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: ListEmployeeTypeEnumResponse = JSON.unmarshal(str(resp.content, UTF_8), ListEmployeeTypeEnumResponse)
        response.raw = resp

        return response

    def update(self, request: UpdateEmployeeTypeEnumRequest,
               option: Optional[RequestOption] = None) -> UpdateEmployeeTypeEnumResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: UpdateEmployeeTypeEnumResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                  UpdateEmployeeTypeEnumResponse)
        response.raw = resp

        return response
