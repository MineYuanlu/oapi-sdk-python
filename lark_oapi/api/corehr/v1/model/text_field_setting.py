# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class TextFieldSetting(object):
    _types = {
        "is_multilingual": bool,
        "is_multiline": bool,
        "max_length": int,
        "is_url_type": bool,
    }

    def __init__(self, d=None):
        self.is_multilingual: Optional[bool] = None
        self.is_multiline: Optional[bool] = None
        self.max_length: Optional[int] = None
        self.is_url_type: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TextFieldSettingBuilder":
        return TextFieldSettingBuilder()


class TextFieldSettingBuilder(object):
    def __init__(self) -> None:
        self._text_field_setting = TextFieldSetting()

    def is_multilingual(self, is_multilingual: bool) -> "TextFieldSettingBuilder":
        self._text_field_setting.is_multilingual = is_multilingual
        return self

    def is_multiline(self, is_multiline: bool) -> "TextFieldSettingBuilder":
        self._text_field_setting.is_multiline = is_multiline
        return self

    def max_length(self, max_length: int) -> "TextFieldSettingBuilder":
        self._text_field_setting.max_length = max_length
        return self

    def is_url_type(self, is_url_type: bool) -> "TextFieldSettingBuilder":
        self._text_field_setting.is_url_type = is_url_type
        return self

    def build(self) -> "TextFieldSetting":
        return self._text_field_setting
