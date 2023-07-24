# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.search_job_change_request import SearchJobChangeRequest
from ..model.search_job_change_response import SearchJobChangeResponse


class JobChange(object):
    def __init__(self, config: Config) -> None:
        self.config: Optional[Config] = config

    def search(self, request: SearchJobChangeRequest,
               option: Optional[RequestOption] = None) -> SearchJobChangeResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: SearchJobChangeResponse = JSON.unmarshal(str(resp.content, UTF_8), SearchJobChangeResponse)
        response.raw = resp

        return response
