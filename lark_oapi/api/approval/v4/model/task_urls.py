# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class TaskUrls(object):
    _types = {
        "helpdesk": str,
        "mobile": str,
        "pc": str,
    }

    def __init__(self, d=None):
        self.helpdesk: Optional[str] = None
        self.mobile: Optional[str] = None
        self.pc: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TaskUrlsBuilder":
        return TaskUrlsBuilder()


class TaskUrlsBuilder(object):
    def __init__(self) -> None:
        self._task_urls = TaskUrls()

    def helpdesk(self, helpdesk: str) -> "TaskUrlsBuilder":
        self._task_urls.helpdesk = helpdesk
        return self

    def mobile(self, mobile: str) -> "TaskUrlsBuilder":
        self._task_urls.mobile = mobile
        return self

    def pc(self, pc: str) -> "TaskUrlsBuilder":
        self._task_urls.pc = pc
        return self

    def build(self) -> "TaskUrls":
        return self._task_urls
