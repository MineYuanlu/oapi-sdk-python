# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .i18n import I18n


class CostCenterVersion(object):
    _types = {
        "cost_center_id": str,
        "version_id": str,
        "name": List[I18n],
        "code": str,
        "parent_cost_center_id": str,
        "managers": List[str],
        "description": List[I18n],
        "effective_time": str,
        "expiration_time": str,
        "active": bool,
        "operation_reason": str,
    }

    def __init__(self, d=None):
        self.cost_center_id: Optional[str] = None
        self.version_id: Optional[str] = None
        self.name: Optional[List[I18n]] = None
        self.code: Optional[str] = None
        self.parent_cost_center_id: Optional[str] = None
        self.managers: Optional[List[str]] = None
        self.description: Optional[List[I18n]] = None
        self.effective_time: Optional[str] = None
        self.expiration_time: Optional[str] = None
        self.active: Optional[bool] = None
        self.operation_reason: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CostCenterVersionBuilder":
        return CostCenterVersionBuilder()


class CostCenterVersionBuilder(object):
    def __init__(self) -> None:
        self._cost_center_version = CostCenterVersion()

    def cost_center_id(self, cost_center_id: str) -> "CostCenterVersionBuilder":
        self._cost_center_version.cost_center_id = cost_center_id
        return self

    def version_id(self, version_id: str) -> "CostCenterVersionBuilder":
        self._cost_center_version.version_id = version_id
        return self

    def name(self, name: List[I18n]) -> "CostCenterVersionBuilder":
        self._cost_center_version.name = name
        return self

    def code(self, code: str) -> "CostCenterVersionBuilder":
        self._cost_center_version.code = code
        return self

    def parent_cost_center_id(self, parent_cost_center_id: str) -> "CostCenterVersionBuilder":
        self._cost_center_version.parent_cost_center_id = parent_cost_center_id
        return self

    def managers(self, managers: List[str]) -> "CostCenterVersionBuilder":
        self._cost_center_version.managers = managers
        return self

    def description(self, description: List[I18n]) -> "CostCenterVersionBuilder":
        self._cost_center_version.description = description
        return self

    def effective_time(self, effective_time: str) -> "CostCenterVersionBuilder":
        self._cost_center_version.effective_time = effective_time
        return self

    def expiration_time(self, expiration_time: str) -> "CostCenterVersionBuilder":
        self._cost_center_version.expiration_time = expiration_time
        return self

    def active(self, active: bool) -> "CostCenterVersionBuilder":
        self._cost_center_version.active = active
        return self

    def operation_reason(self, operation_reason: str) -> "CostCenterVersionBuilder":
        self._cost_center_version.operation_reason = operation_reason
        return self

    def build(self) -> "CostCenterVersion":
        return self._cost_center_version
