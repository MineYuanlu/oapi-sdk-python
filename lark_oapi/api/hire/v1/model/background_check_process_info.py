# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class BackgroundCheckProcessInfo(object):
    _types = {
        "process": str,
        "update_time": str,
    }

    def __init__(self, d=None):
        self.process: Optional[str] = None
        self.update_time: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BackgroundCheckProcessInfoBuilder":
        return BackgroundCheckProcessInfoBuilder()


class BackgroundCheckProcessInfoBuilder(object):
    def __init__(self) -> None:
        self._background_check_process_info = BackgroundCheckProcessInfo()

    def process(self, process: str) -> "BackgroundCheckProcessInfoBuilder":
        self._background_check_process_info.process = process
        return self

    def update_time(self, update_time: str) -> "BackgroundCheckProcessInfoBuilder":
        self._background_check_process_info.update_time = update_time
        return self

    def build(self) -> "BackgroundCheckProcessInfo":
        return self._background_check_process_info
