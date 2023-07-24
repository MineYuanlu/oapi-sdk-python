# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .setting import Setting


class UpdateSpaceSettingResponseBody(object):
    _types = {
        "setting": Setting,
    }

    def __init__(self, d=None):
        self.setting: Optional[Setting] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UpdateSpaceSettingResponseBodyBuilder":
        return UpdateSpaceSettingResponseBodyBuilder()


class UpdateSpaceSettingResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._update_space_setting_response_body = UpdateSpaceSettingResponseBody()

    def setting(self, setting: Setting) -> "UpdateSpaceSettingResponseBodyBuilder":
        self._update_space_setting_response_body.setting = setting
        return self

    def build(self) -> "UpdateSpaceSettingResponseBody":
        return self._update_space_setting_response_body
