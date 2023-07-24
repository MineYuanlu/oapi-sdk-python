# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class UserSetting(object):
    _types = {
        "user_id": str,
        "face_key": str,
        "face_key_update_time": str,
    }

    def __init__(self, d=None):
        self.user_id: Optional[str] = None
        self.face_key: Optional[str] = None
        self.face_key_update_time: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UserSettingBuilder":
        return UserSettingBuilder()


class UserSettingBuilder(object):
    def __init__(self) -> None:
        self._user_setting = UserSetting()

    def user_id(self, user_id: str) -> "UserSettingBuilder":
        self._user_setting.user_id = user_id
        return self

    def face_key(self, face_key: str) -> "UserSettingBuilder":
        self._user_setting.face_key = face_key
        return self

    def face_key_update_time(self, face_key_update_time: str) -> "UserSettingBuilder":
        self._user_setting.face_key_update_time = face_key_update_time
        return self

    def build(self) -> "UserSetting":
        return self._user_setting
