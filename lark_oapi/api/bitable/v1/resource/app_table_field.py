# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.create_app_table_field_request import CreateAppTableFieldRequest
from ..model.create_app_table_field_response import CreateAppTableFieldResponse
from ..model.delete_app_table_field_request import DeleteAppTableFieldRequest
from ..model.delete_app_table_field_response import DeleteAppTableFieldResponse
from ..model.list_app_table_field_request import ListAppTableFieldRequest
from ..model.list_app_table_field_response import ListAppTableFieldResponse
from ..model.update_app_table_field_request import UpdateAppTableFieldRequest
from ..model.update_app_table_field_response import UpdateAppTableFieldResponse


class AppTableField(object):
    def __init__(self, config: Config) -> None:
        self.config: Optional[Config] = config

    def create(self, request: CreateAppTableFieldRequest,
               option: Optional[RequestOption] = None) -> CreateAppTableFieldResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: CreateAppTableFieldResponse = JSON.unmarshal(str(resp.content, UTF_8), CreateAppTableFieldResponse)
        response.raw = resp

        return response

    def delete(self, request: DeleteAppTableFieldRequest,
               option: Optional[RequestOption] = None) -> DeleteAppTableFieldResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: DeleteAppTableFieldResponse = JSON.unmarshal(str(resp.content, UTF_8), DeleteAppTableFieldResponse)
        response.raw = resp

        return response

    def list(self, request: ListAppTableFieldRequest,
             option: Optional[RequestOption] = None) -> ListAppTableFieldResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: ListAppTableFieldResponse = JSON.unmarshal(str(resp.content, UTF_8), ListAppTableFieldResponse)
        response.raw = resp

        return response

    def update(self, request: UpdateAppTableFieldRequest,
               option: Optional[RequestOption] = None) -> UpdateAppTableFieldResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: UpdateAppTableFieldResponse = JSON.unmarshal(str(resp.content, UTF_8), UpdateAppTableFieldResponse)
        response.raw = resp

        return response
