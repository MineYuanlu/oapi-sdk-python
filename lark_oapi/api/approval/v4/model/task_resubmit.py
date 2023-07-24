# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class TaskResubmit(object):
    _types = {
        "approval_code": str,
        "instance_code": str,
        "user_id": str,
        "comment": str,
        "task_id": str,
        "form": str,
    }

    def __init__(self, d=None):
        self.approval_code: Optional[str] = None
        self.instance_code: Optional[str] = None
        self.user_id: Optional[str] = None
        self.comment: Optional[str] = None
        self.task_id: Optional[str] = None
        self.form: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TaskResubmitBuilder":
        return TaskResubmitBuilder()


class TaskResubmitBuilder(object):
    def __init__(self) -> None:
        self._task_resubmit = TaskResubmit()

    def approval_code(self, approval_code: str) -> "TaskResubmitBuilder":
        self._task_resubmit.approval_code = approval_code
        return self

    def instance_code(self, instance_code: str) -> "TaskResubmitBuilder":
        self._task_resubmit.instance_code = instance_code
        return self

    def user_id(self, user_id: str) -> "TaskResubmitBuilder":
        self._task_resubmit.user_id = user_id
        return self

    def comment(self, comment: str) -> "TaskResubmitBuilder":
        self._task_resubmit.comment = comment
        return self

    def task_id(self, task_id: str) -> "TaskResubmitBuilder":
        self._task_resubmit.task_id = task_id
        return self

    def form(self, form: str) -> "TaskResubmitBuilder":
        self._task_resubmit.form = form
        return self

    def build(self) -> "TaskResubmit":
        return self._task_resubmit
