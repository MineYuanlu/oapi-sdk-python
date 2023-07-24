# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .enum import Enum
from .object_field_data import ObjectFieldData
from .support_cost_center_item import SupportCostCenterItem


class JobData(object):
    _types = {
        "id": str,
        "version_id": str,
        "job_level_id": str,
        "employee_type_id": str,
        "working_hours_type_id": str,
        "work_location_id": str,
        "department_id": str,
        "job_id": str,
        "probation_start_date": str,
        "probation_end_date": str,
        "primary_job_data": bool,
        "employment_id": str,
        "effective_time": str,
        "expiration_time": str,
        "job_family_id": str,
        "assignment_start_reason": Enum,
        "probation_expected_end_date": str,
        "probation_outcome": Enum,
        "weekly_working_hours": int,
        "direct_manager_id": str,
        "dotted_line_manager_id_list": List[str],
        "second_direct_manager_id": str,
        "cost_center_rate": List[SupportCostCenterItem],
        "custom_fields": List[ObjectFieldData],
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.version_id: Optional[str] = None
        self.job_level_id: Optional[str] = None
        self.employee_type_id: Optional[str] = None
        self.working_hours_type_id: Optional[str] = None
        self.work_location_id: Optional[str] = None
        self.department_id: Optional[str] = None
        self.job_id: Optional[str] = None
        self.probation_start_date: Optional[str] = None
        self.probation_end_date: Optional[str] = None
        self.primary_job_data: Optional[bool] = None
        self.employment_id: Optional[str] = None
        self.effective_time: Optional[str] = None
        self.expiration_time: Optional[str] = None
        self.job_family_id: Optional[str] = None
        self.assignment_start_reason: Optional[Enum] = None
        self.probation_expected_end_date: Optional[str] = None
        self.probation_outcome: Optional[Enum] = None
        self.weekly_working_hours: Optional[int] = None
        self.direct_manager_id: Optional[str] = None
        self.dotted_line_manager_id_list: Optional[List[str]] = None
        self.second_direct_manager_id: Optional[str] = None
        self.cost_center_rate: Optional[List[SupportCostCenterItem]] = None
        self.custom_fields: Optional[List[ObjectFieldData]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "JobDataBuilder":
        return JobDataBuilder()


class JobDataBuilder(object):
    def __init__(self) -> None:
        self._job_data = JobData()

    def id(self, id: str) -> "JobDataBuilder":
        self._job_data.id = id
        return self

    def version_id(self, version_id: str) -> "JobDataBuilder":
        self._job_data.version_id = version_id
        return self

    def job_level_id(self, job_level_id: str) -> "JobDataBuilder":
        self._job_data.job_level_id = job_level_id
        return self

    def employee_type_id(self, employee_type_id: str) -> "JobDataBuilder":
        self._job_data.employee_type_id = employee_type_id
        return self

    def working_hours_type_id(self, working_hours_type_id: str) -> "JobDataBuilder":
        self._job_data.working_hours_type_id = working_hours_type_id
        return self

    def work_location_id(self, work_location_id: str) -> "JobDataBuilder":
        self._job_data.work_location_id = work_location_id
        return self

    def department_id(self, department_id: str) -> "JobDataBuilder":
        self._job_data.department_id = department_id
        return self

    def job_id(self, job_id: str) -> "JobDataBuilder":
        self._job_data.job_id = job_id
        return self

    def probation_start_date(self, probation_start_date: str) -> "JobDataBuilder":
        self._job_data.probation_start_date = probation_start_date
        return self

    def probation_end_date(self, probation_end_date: str) -> "JobDataBuilder":
        self._job_data.probation_end_date = probation_end_date
        return self

    def primary_job_data(self, primary_job_data: bool) -> "JobDataBuilder":
        self._job_data.primary_job_data = primary_job_data
        return self

    def employment_id(self, employment_id: str) -> "JobDataBuilder":
        self._job_data.employment_id = employment_id
        return self

    def effective_time(self, effective_time: str) -> "JobDataBuilder":
        self._job_data.effective_time = effective_time
        return self

    def expiration_time(self, expiration_time: str) -> "JobDataBuilder":
        self._job_data.expiration_time = expiration_time
        return self

    def job_family_id(self, job_family_id: str) -> "JobDataBuilder":
        self._job_data.job_family_id = job_family_id
        return self

    def assignment_start_reason(self, assignment_start_reason: Enum) -> "JobDataBuilder":
        self._job_data.assignment_start_reason = assignment_start_reason
        return self

    def probation_expected_end_date(self, probation_expected_end_date: str) -> "JobDataBuilder":
        self._job_data.probation_expected_end_date = probation_expected_end_date
        return self

    def probation_outcome(self, probation_outcome: Enum) -> "JobDataBuilder":
        self._job_data.probation_outcome = probation_outcome
        return self

    def weekly_working_hours(self, weekly_working_hours: int) -> "JobDataBuilder":
        self._job_data.weekly_working_hours = weekly_working_hours
        return self

    def direct_manager_id(self, direct_manager_id: str) -> "JobDataBuilder":
        self._job_data.direct_manager_id = direct_manager_id
        return self

    def dotted_line_manager_id_list(self, dotted_line_manager_id_list: List[str]) -> "JobDataBuilder":
        self._job_data.dotted_line_manager_id_list = dotted_line_manager_id_list
        return self

    def second_direct_manager_id(self, second_direct_manager_id: str) -> "JobDataBuilder":
        self._job_data.second_direct_manager_id = second_direct_manager_id
        return self

    def cost_center_rate(self, cost_center_rate: List[SupportCostCenterItem]) -> "JobDataBuilder":
        self._job_data.cost_center_rate = cost_center_rate
        return self

    def custom_fields(self, custom_fields: List[ObjectFieldData]) -> "JobDataBuilder":
        self._job_data.custom_fields = custom_fields
        return self

    def build(self) -> "JobData":
        return self._job_data
