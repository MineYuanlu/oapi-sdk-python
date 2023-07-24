# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class Employee(object):
    _types = {
        "id": str,
        "application_id": str,
        "onboard_status": int,
        "conversion_status": int,
        "onboard_time": int,
        "expected_conversion_time": int,
        "actual_conversion_time": int,
        "overboard_time": int,
        "overboard_note": str,
        "onboard_city_code": str,
        "department": str,
        "leader": str,
        "sequence": str,
        "level": str,
        "employee_type": str,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.application_id: Optional[str] = None
        self.onboard_status: Optional[int] = None
        self.conversion_status: Optional[int] = None
        self.onboard_time: Optional[int] = None
        self.expected_conversion_time: Optional[int] = None
        self.actual_conversion_time: Optional[int] = None
        self.overboard_time: Optional[int] = None
        self.overboard_note: Optional[str] = None
        self.onboard_city_code: Optional[str] = None
        self.department: Optional[str] = None
        self.leader: Optional[str] = None
        self.sequence: Optional[str] = None
        self.level: Optional[str] = None
        self.employee_type: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "EmployeeBuilder":
        return EmployeeBuilder()


class EmployeeBuilder(object):
    def __init__(self) -> None:
        self._employee = Employee()

    def id(self, id: str) -> "EmployeeBuilder":
        self._employee.id = id
        return self

    def application_id(self, application_id: str) -> "EmployeeBuilder":
        self._employee.application_id = application_id
        return self

    def onboard_status(self, onboard_status: int) -> "EmployeeBuilder":
        self._employee.onboard_status = onboard_status
        return self

    def conversion_status(self, conversion_status: int) -> "EmployeeBuilder":
        self._employee.conversion_status = conversion_status
        return self

    def onboard_time(self, onboard_time: int) -> "EmployeeBuilder":
        self._employee.onboard_time = onboard_time
        return self

    def expected_conversion_time(self, expected_conversion_time: int) -> "EmployeeBuilder":
        self._employee.expected_conversion_time = expected_conversion_time
        return self

    def actual_conversion_time(self, actual_conversion_time: int) -> "EmployeeBuilder":
        self._employee.actual_conversion_time = actual_conversion_time
        return self

    def overboard_time(self, overboard_time: int) -> "EmployeeBuilder":
        self._employee.overboard_time = overboard_time
        return self

    def overboard_note(self, overboard_note: str) -> "EmployeeBuilder":
        self._employee.overboard_note = overboard_note
        return self

    def onboard_city_code(self, onboard_city_code: str) -> "EmployeeBuilder":
        self._employee.onboard_city_code = onboard_city_code
        return self

    def department(self, department: str) -> "EmployeeBuilder":
        self._employee.department = department
        return self

    def leader(self, leader: str) -> "EmployeeBuilder":
        self._employee.leader = leader
        return self

    def sequence(self, sequence: str) -> "EmployeeBuilder":
        self._employee.sequence = sequence
        return self

    def level(self, level: str) -> "EmployeeBuilder":
        self._employee.level = level
        return self

    def employee_type(self, employee_type: str) -> "EmployeeBuilder":
        self._employee.employee_type = employee_type
        return self

    def build(self) -> "Employee":
        return self._employee
