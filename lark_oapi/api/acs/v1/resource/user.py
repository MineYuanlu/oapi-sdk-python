# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.get_user_request import GetUserRequest
from ..model.get_user_response import GetUserResponse
from ..model.list_user_request import ListUserRequest
from ..model.list_user_response import ListUserResponse
from ..model.patch_user_request import PatchUserRequest
from ..model.patch_user_response import PatchUserResponse


class User(object):
    def __init__(self, config: Config) -> None:
        self.config: Optional[Config] = config

    def get(self, request: GetUserRequest, option: Optional[RequestOption] = None) -> GetUserResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: GetUserResponse = JSON.unmarshal(str(resp.content, UTF_8), GetUserResponse)
        response.raw = resp

        return response

    def list(self, request: ListUserRequest, option: Optional[RequestOption] = None) -> ListUserResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: ListUserResponse = JSON.unmarshal(str(resp.content, UTF_8), ListUserResponse)
        response.raw = resp

        return response

    def patch(self, request: PatchUserRequest, option: Optional[RequestOption] = None) -> PatchUserResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: PatchUserResponse = JSON.unmarshal(str(resp.content, UTF_8), PatchUserResponse)
        response.raw = resp

        return response
