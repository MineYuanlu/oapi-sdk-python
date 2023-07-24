# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class JobDataCostCenter(object):
    _types = {
        "cost_center_id": str,
        "rate": int,
    }

    def __init__(self, d=None):
        self.cost_center_id: Optional[str] = None
        self.rate: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "JobDataCostCenterBuilder":
        return JobDataCostCenterBuilder()


class JobDataCostCenterBuilder(object):
    def __init__(self) -> None:
        self._job_data_cost_center = JobDataCostCenter()

    def cost_center_id(self, cost_center_id: str) -> "JobDataCostCenterBuilder":
        self._job_data_cost_center.cost_center_id = cost_center_id
        return self

    def rate(self, rate: int) -> "JobDataCostCenterBuilder":
        self._job_data_cost_center.rate = rate
        return self

    def build(self) -> "JobDataCostCenter":
        return self._job_data_cost_center
