# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class UserTaskRemedy(object):
    _types = {
        "user_id": str,
        "remedy_date": int,
        "punch_no": int,
        "work_type": int,
        "approval_id": str,
        "remedy_time": str,
        "status": int,
        "reason": str,
        "time": str,
        "time_zone": str,
        "create_time": str,
        "update_time": str,
    }

    def __init__(self, d=None):
        self.user_id: Optional[str] = None
        self.remedy_date: Optional[int] = None
        self.punch_no: Optional[int] = None
        self.work_type: Optional[int] = None
        self.approval_id: Optional[str] = None
        self.remedy_time: Optional[str] = None
        self.status: Optional[int] = None
        self.reason: Optional[str] = None
        self.time: Optional[str] = None
        self.time_zone: Optional[str] = None
        self.create_time: Optional[str] = None
        self.update_time: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UserTaskRemedyBuilder":
        return UserTaskRemedyBuilder()


class UserTaskRemedyBuilder(object):
    def __init__(self) -> None:
        self._user_task_remedy = UserTaskRemedy()

    def user_id(self, user_id: str) -> "UserTaskRemedyBuilder":
        self._user_task_remedy.user_id = user_id
        return self

    def remedy_date(self, remedy_date: int) -> "UserTaskRemedyBuilder":
        self._user_task_remedy.remedy_date = remedy_date
        return self

    def punch_no(self, punch_no: int) -> "UserTaskRemedyBuilder":
        self._user_task_remedy.punch_no = punch_no
        return self

    def work_type(self, work_type: int) -> "UserTaskRemedyBuilder":
        self._user_task_remedy.work_type = work_type
        return self

    def approval_id(self, approval_id: str) -> "UserTaskRemedyBuilder":
        self._user_task_remedy.approval_id = approval_id
        return self

    def remedy_time(self, remedy_time: str) -> "UserTaskRemedyBuilder":
        self._user_task_remedy.remedy_time = remedy_time
        return self

    def status(self, status: int) -> "UserTaskRemedyBuilder":
        self._user_task_remedy.status = status
        return self

    def reason(self, reason: str) -> "UserTaskRemedyBuilder":
        self._user_task_remedy.reason = reason
        return self

    def time(self, time: str) -> "UserTaskRemedyBuilder":
        self._user_task_remedy.time = time
        return self

    def time_zone(self, time_zone: str) -> "UserTaskRemedyBuilder":
        self._user_task_remedy.time_zone = time_zone
        return self

    def create_time(self, create_time: str) -> "UserTaskRemedyBuilder":
        self._user_task_remedy.create_time = create_time
        return self

    def update_time(self, update_time: str) -> "UserTaskRemedyBuilder":
        self._user_task_remedy.update_time = update_time
        return self

    def build(self) -> "UserTaskRemedy":
        return self._user_task_remedy
