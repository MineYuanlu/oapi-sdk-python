# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .custom_field_data import CustomFieldData
from .i18n import I18n


class WorkExperienceInfo(object):
    _types = {
        "company_organization": List[I18n],
        "department": List[I18n],
        "job": List[I18n],
        "description": List[I18n],
        "start_date": str,
        "end_date": str,
        "custom_fields": List[CustomFieldData],
    }

    def __init__(self, d=None):
        self.company_organization: Optional[List[I18n]] = None
        self.department: Optional[List[I18n]] = None
        self.job: Optional[List[I18n]] = None
        self.description: Optional[List[I18n]] = None
        self.start_date: Optional[str] = None
        self.end_date: Optional[str] = None
        self.custom_fields: Optional[List[CustomFieldData]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "WorkExperienceInfoBuilder":
        return WorkExperienceInfoBuilder()


class WorkExperienceInfoBuilder(object):
    def __init__(self) -> None:
        self._work_experience_info = WorkExperienceInfo()

    def company_organization(self, company_organization: List[I18n]) -> "WorkExperienceInfoBuilder":
        self._work_experience_info.company_organization = company_organization
        return self

    def department(self, department: List[I18n]) -> "WorkExperienceInfoBuilder":
        self._work_experience_info.department = department
        return self

    def job(self, job: List[I18n]) -> "WorkExperienceInfoBuilder":
        self._work_experience_info.job = job
        return self

    def description(self, description: List[I18n]) -> "WorkExperienceInfoBuilder":
        self._work_experience_info.description = description
        return self

    def start_date(self, start_date: str) -> "WorkExperienceInfoBuilder":
        self._work_experience_info.start_date = start_date
        return self

    def end_date(self, end_date: str) -> "WorkExperienceInfoBuilder":
        self._work_experience_info.end_date = end_date
        return self

    def custom_fields(self, custom_fields: List[CustomFieldData]) -> "WorkExperienceInfoBuilder":
        self._work_experience_info.custom_fields = custom_fields
        return self

    def build(self) -> "WorkExperienceInfo":
        return self._work_experience_info
