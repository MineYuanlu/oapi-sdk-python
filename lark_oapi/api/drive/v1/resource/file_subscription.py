# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.create_file_subscription_request import CreateFileSubscriptionRequest
from ..model.create_file_subscription_response import CreateFileSubscriptionResponse
from ..model.get_file_subscription_request import GetFileSubscriptionRequest
from ..model.get_file_subscription_response import GetFileSubscriptionResponse
from ..model.patch_file_subscription_request import PatchFileSubscriptionRequest
from ..model.patch_file_subscription_response import PatchFileSubscriptionResponse


class FileSubscription(object):
    def __init__(self, config: Config) -> None:
        self.config: Optional[Config] = config

    def create(self, request: CreateFileSubscriptionRequest,
               option: Optional[RequestOption] = None) -> CreateFileSubscriptionResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: CreateFileSubscriptionResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                  CreateFileSubscriptionResponse)
        response.raw = resp

        return response

    def get(self, request: GetFileSubscriptionRequest,
            option: Optional[RequestOption] = None) -> GetFileSubscriptionResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: GetFileSubscriptionResponse = JSON.unmarshal(str(resp.content, UTF_8), GetFileSubscriptionResponse)
        response.raw = resp

        return response

    def patch(self, request: PatchFileSubscriptionRequest,
              option: Optional[RequestOption] = None) -> PatchFileSubscriptionResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: PatchFileSubscriptionResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                 PatchFileSubscriptionResponse)
        response.raw = resp

        return response
