# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.query_offboarding_request import QueryOffboardingRequest
from ..model.query_offboarding_response import QueryOffboardingResponse
from ..model.search_offboarding_request import SearchOffboardingRequest
from ..model.search_offboarding_response import SearchOffboardingResponse
from ..model.submit_offboarding_request import SubmitOffboardingRequest
from ..model.submit_offboarding_response import SubmitOffboardingResponse


class Offboarding(object):
    def __init__(self, config: Config) -> None:
        self.config: Optional[Config] = config

    def query(self, request: QueryOffboardingRequest,
              option: Optional[RequestOption] = None) -> QueryOffboardingResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: QueryOffboardingResponse = JSON.unmarshal(str(resp.content, UTF_8), QueryOffboardingResponse)
        response.raw = resp

        return response

    def search(self, request: SearchOffboardingRequest,
               option: Optional[RequestOption] = None) -> SearchOffboardingResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: SearchOffboardingResponse = JSON.unmarshal(str(resp.content, UTF_8), SearchOffboardingResponse)
        response.raw = resp

        return response

    def submit(self, request: SubmitOffboardingRequest,
               option: Optional[RequestOption] = None) -> SubmitOffboardingResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: SubmitOffboardingResponse = JSON.unmarshal(str(resp.content, UTF_8), SubmitOffboardingResponse)
        response.raw = resp

        return response
