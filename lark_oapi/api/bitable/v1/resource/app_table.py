# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.batch_create_app_table_request import BatchCreateAppTableRequest
from ..model.batch_create_app_table_response import BatchCreateAppTableResponse
from ..model.batch_delete_app_table_request import BatchDeleteAppTableRequest
from ..model.batch_delete_app_table_response import BatchDeleteAppTableResponse
from ..model.create_app_table_request import CreateAppTableRequest
from ..model.create_app_table_response import CreateAppTableResponse
from ..model.delete_app_table_request import DeleteAppTableRequest
from ..model.delete_app_table_response import DeleteAppTableResponse
from ..model.list_app_table_request import ListAppTableRequest
from ..model.list_app_table_response import ListAppTableResponse
from ..model.patch_app_table_request import PatchAppTableRequest
from ..model.patch_app_table_response import PatchAppTableResponse


class AppTable(object):
    def __init__(self, config: Config) -> None:
        self.config: Optional[Config] = config

    def batch_create(self, request: BatchCreateAppTableRequest,
                     option: Optional[RequestOption] = None) -> BatchCreateAppTableResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: BatchCreateAppTableResponse = JSON.unmarshal(str(resp.content, UTF_8), BatchCreateAppTableResponse)
        response.raw = resp

        return response

    def batch_delete(self, request: BatchDeleteAppTableRequest,
                     option: Optional[RequestOption] = None) -> BatchDeleteAppTableResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: BatchDeleteAppTableResponse = JSON.unmarshal(str(resp.content, UTF_8), BatchDeleteAppTableResponse)
        response.raw = resp

        return response

    def create(self, request: CreateAppTableRequest, option: Optional[RequestOption] = None) -> CreateAppTableResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: CreateAppTableResponse = JSON.unmarshal(str(resp.content, UTF_8), CreateAppTableResponse)
        response.raw = resp

        return response

    def delete(self, request: DeleteAppTableRequest, option: Optional[RequestOption] = None) -> DeleteAppTableResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: DeleteAppTableResponse = JSON.unmarshal(str(resp.content, UTF_8), DeleteAppTableResponse)
        response.raw = resp

        return response

    def list(self, request: ListAppTableRequest, option: Optional[RequestOption] = None) -> ListAppTableResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: ListAppTableResponse = JSON.unmarshal(str(resp.content, UTF_8), ListAppTableResponse)
        response.raw = resp

        return response

    def patch(self, request: PatchAppTableRequest, option: Optional[RequestOption] = None) -> PatchAppTableResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: PatchAppTableResponse = JSON.unmarshal(str(resp.content, UTF_8), PatchAppTableResponse)
        response.raw = resp

        return response
