# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.create_agent_skill_request import CreateAgentSkillRequest
from ..model.create_agent_skill_response import CreateAgentSkillResponse
from ..model.delete_agent_skill_request import DeleteAgentSkillRequest
from ..model.delete_agent_skill_response import DeleteAgentSkillResponse
from ..model.get_agent_skill_request import GetAgentSkillRequest
from ..model.get_agent_skill_response import GetAgentSkillResponse
from ..model.list_agent_skill_request import ListAgentSkillRequest
from ..model.list_agent_skill_response import ListAgentSkillResponse
from ..model.patch_agent_skill_request import PatchAgentSkillRequest
from ..model.patch_agent_skill_response import PatchAgentSkillResponse


class AgentSkill(object):
    def __init__(self, config: Config) -> None:
        self.config: Optional[Config] = config

    def create(self, request: CreateAgentSkillRequest,
               option: Optional[RequestOption] = None) -> CreateAgentSkillResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: CreateAgentSkillResponse = JSON.unmarshal(str(resp.content, UTF_8), CreateAgentSkillResponse)
        response.raw = resp

        return response

    def delete(self, request: DeleteAgentSkillRequest,
               option: Optional[RequestOption] = None) -> DeleteAgentSkillResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: DeleteAgentSkillResponse = JSON.unmarshal(str(resp.content, UTF_8), DeleteAgentSkillResponse)
        response.raw = resp

        return response

    def get(self, request: GetAgentSkillRequest, option: Optional[RequestOption] = None) -> GetAgentSkillResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: GetAgentSkillResponse = JSON.unmarshal(str(resp.content, UTF_8), GetAgentSkillResponse)
        response.raw = resp

        return response

    def list(self, request: ListAgentSkillRequest, option: Optional[RequestOption] = None) -> ListAgentSkillResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: ListAgentSkillResponse = JSON.unmarshal(str(resp.content, UTF_8), ListAgentSkillResponse)
        response.raw = resp

        return response

    def patch(self, request: PatchAgentSkillRequest, option: Optional[RequestOption] = None) -> PatchAgentSkillResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: PatchAgentSkillResponse = JSON.unmarshal(str(resp.content, UTF_8), PatchAgentSkillResponse)
        response.raw = resp

        return response
