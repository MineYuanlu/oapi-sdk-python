# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .job_processes_stage import JobProcessesStage


class JobProcesses(object):
    _types = {
        "id": str,
        "zh_name": str,
        "en_name": str,
        "type": int,
        "stage_list": List[JobProcessesStage],
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.zh_name: Optional[str] = None
        self.en_name: Optional[str] = None
        self.type: Optional[int] = None
        self.stage_list: Optional[List[JobProcessesStage]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "JobProcessesBuilder":
        return JobProcessesBuilder()


class JobProcessesBuilder(object):
    def __init__(self) -> None:
        self._job_processes = JobProcesses()

    def id(self, id: str) -> "JobProcessesBuilder":
        self._job_processes.id = id
        return self

    def zh_name(self, zh_name: str) -> "JobProcessesBuilder":
        self._job_processes.zh_name = zh_name
        return self

    def en_name(self, en_name: str) -> "JobProcessesBuilder":
        self._job_processes.en_name = en_name
        return self

    def type(self, type: int) -> "JobProcessesBuilder":
        self._job_processes.type = type
        return self

    def stage_list(self, stage_list: List[JobProcessesStage]) -> "JobProcessesBuilder":
        self._job_processes.stage_list = stage_list
        return self

    def build(self) -> "JobProcesses":
        return self._job_processes
