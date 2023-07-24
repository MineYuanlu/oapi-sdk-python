# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.get_daily_report_request import GetDailyReportRequest
from ..model.get_daily_report_response import GetDailyReportResponse
from ..model.get_top_user_report_request import GetTopUserReportRequest
from ..model.get_top_user_report_response import GetTopUserReportResponse


class Report(object):
    def __init__(self, config: Config) -> None:
        self.config: Optional[Config] = config

    def get_daily(self, request: GetDailyReportRequest,
                  option: Optional[RequestOption] = None) -> GetDailyReportResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: GetDailyReportResponse = JSON.unmarshal(str(resp.content, UTF_8), GetDailyReportResponse)
        response.raw = resp

        return response

    def get_top_user(self, request: GetTopUserReportRequest,
                     option: Optional[RequestOption] = None) -> GetTopUserReportResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: GetTopUserReportResponse = JSON.unmarshal(str(resp.content, UTF_8), GetTopUserReportResponse)
        response.raw = resp

        return response
