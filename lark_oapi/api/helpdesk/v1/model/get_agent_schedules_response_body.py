# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .agent_schedule import AgentSchedule


class GetAgentSchedulesResponseBody(object):
    _types = {
        "agent_schedule": AgentSchedule,
    }

    def __init__(self, d=None):
        self.agent_schedule: Optional[AgentSchedule] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetAgentSchedulesResponseBodyBuilder":
        return GetAgentSchedulesResponseBodyBuilder()


class GetAgentSchedulesResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._get_agent_schedules_response_body = GetAgentSchedulesResponseBody()

    def agent_schedule(self, agent_schedule: AgentSchedule) -> "GetAgentSchedulesResponseBodyBuilder":
        self._get_agent_schedules_response_body.agent_schedule = agent_schedule
        return self

    def build(self) -> "GetAgentSchedulesResponseBody":
        return self._get_agent_schedules_response_body
