# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.check_white_black_list_application_visibility_request import \
    CheckWhiteBlackListApplicationVisibilityRequest
from ..model.check_white_black_list_application_visibility_response import \
    CheckWhiteBlackListApplicationVisibilityResponse


class ApplicationVisibility(object):
    def __init__(self, config: Config) -> None:
        self.config: Optional[Config] = config

    def check_white_black_list(self, request: CheckWhiteBlackListApplicationVisibilityRequest, option: Optional[
        RequestOption] = None) -> CheckWhiteBlackListApplicationVisibilityResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: CheckWhiteBlackListApplicationVisibilityResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                                    CheckWhiteBlackListApplicationVisibilityResponse)
        response.raw = resp

        return response
