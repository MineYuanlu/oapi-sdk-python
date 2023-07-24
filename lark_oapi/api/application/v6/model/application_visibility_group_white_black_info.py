# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class ApplicationVisibilityGroupWhiteBlackInfo(object):
    _types = {
        "group_id": str,
        "in_white_list": bool,
        "in_black_list": bool,
    }

    def __init__(self, d=None):
        self.group_id: Optional[str] = None
        self.in_white_list: Optional[bool] = None
        self.in_black_list: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ApplicationVisibilityGroupWhiteBlackInfoBuilder":
        return ApplicationVisibilityGroupWhiteBlackInfoBuilder()


class ApplicationVisibilityGroupWhiteBlackInfoBuilder(object):
    def __init__(self) -> None:
        self._application_visibility_group_white_black_info = ApplicationVisibilityGroupWhiteBlackInfo()

    def group_id(self, group_id: str) -> "ApplicationVisibilityGroupWhiteBlackInfoBuilder":
        self._application_visibility_group_white_black_info.group_id = group_id
        return self

    def in_white_list(self, in_white_list: bool) -> "ApplicationVisibilityGroupWhiteBlackInfoBuilder":
        self._application_visibility_group_white_black_info.in_white_list = in_white_list
        return self

    def in_black_list(self, in_black_list: bool) -> "ApplicationVisibilityGroupWhiteBlackInfoBuilder":
        self._application_visibility_group_white_black_info.in_black_list = in_black_list
        return self

    def build(self) -> "ApplicationVisibilityGroupWhiteBlackInfo":
        return self._application_visibility_group_white_black_info
