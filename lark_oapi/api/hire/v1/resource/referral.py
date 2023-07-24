# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.get_by_application_referral_request import GetByApplicationReferralRequest
from ..model.get_by_application_referral_response import GetByApplicationReferralResponse


class Referral(object):
    def __init__(self, config: Config) -> None:
        self.config: Optional[Config] = config

    def get_by_application(self, request: GetByApplicationReferralRequest,
                           option: Optional[RequestOption] = None) -> GetByApplicationReferralResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: GetByApplicationReferralResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                    GetByApplicationReferralResponse)
        response.raw = resp

        return response
