# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.create_agent_schedule_request import CreateAgentScheduleRequest
from ..model.create_agent_schedule_response import CreateAgentScheduleResponse
from ..model.list_agent_schedule_request import ListAgentScheduleRequest
from ..model.list_agent_schedule_response import ListAgentScheduleResponse


class AgentSchedule(object):
    def __init__(self, config: Config) -> None:
        self.config: Optional[Config] = config

    def create(self, request: CreateAgentScheduleRequest,
               option: Optional[RequestOption] = None) -> CreateAgentScheduleResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: CreateAgentScheduleResponse = JSON.unmarshal(str(resp.content, UTF_8), CreateAgentScheduleResponse)
        response.raw = resp

        return response

    def list(self, request: ListAgentScheduleRequest,
             option: Optional[RequestOption] = None) -> ListAgentScheduleResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: ListAgentScheduleResponse = JSON.unmarshal(str(resp.content, UTF_8), ListAgentScheduleResponse)
        response.raw = resp

        return response
