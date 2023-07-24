# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .talent_customized_data_object_value import TalentCustomizedDataObjectValue


class TalentCombinedProjectInfo(object):
    _types = {
        "id": str,
        "name": str,
        "role": str,
        "link": str,
        "desc": str,
        "start_time": str,
        "end_time": str,
        "customized_data": List[TalentCustomizedDataObjectValue],
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.name: Optional[str] = None
        self.role: Optional[str] = None
        self.link: Optional[str] = None
        self.desc: Optional[str] = None
        self.start_time: Optional[str] = None
        self.end_time: Optional[str] = None
        self.customized_data: Optional[List[TalentCustomizedDataObjectValue]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TalentCombinedProjectInfoBuilder":
        return TalentCombinedProjectInfoBuilder()


class TalentCombinedProjectInfoBuilder(object):
    def __init__(self) -> None:
        self._talent_combined_project_info = TalentCombinedProjectInfo()

    def id(self, id: str) -> "TalentCombinedProjectInfoBuilder":
        self._talent_combined_project_info.id = id
        return self

    def name(self, name: str) -> "TalentCombinedProjectInfoBuilder":
        self._talent_combined_project_info.name = name
        return self

    def role(self, role: str) -> "TalentCombinedProjectInfoBuilder":
        self._talent_combined_project_info.role = role
        return self

    def link(self, link: str) -> "TalentCombinedProjectInfoBuilder":
        self._talent_combined_project_info.link = link
        return self

    def desc(self, desc: str) -> "TalentCombinedProjectInfoBuilder":
        self._talent_combined_project_info.desc = desc
        return self

    def start_time(self, start_time: str) -> "TalentCombinedProjectInfoBuilder":
        self._talent_combined_project_info.start_time = start_time
        return self

    def end_time(self, end_time: str) -> "TalentCombinedProjectInfoBuilder":
        self._talent_combined_project_info.end_time = end_time
        return self

    def customized_data(self,
                        customized_data: List[TalentCustomizedDataObjectValue]) -> "TalentCombinedProjectInfoBuilder":
        self._talent_combined_project_info.customized_data = customized_data
        return self

    def build(self) -> "TalentCombinedProjectInfo":
        return self._talent_combined_project_info
