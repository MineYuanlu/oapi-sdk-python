# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class NumberSetting(object):
    _types = {
        "format": str,
        "custom_symbol": str,
        "custom_symbol_position": str,
        "separator": str,
        "decimal_count": int,
    }

    def __init__(self, d=None):
        self.format: Optional[str] = None
        self.custom_symbol: Optional[str] = None
        self.custom_symbol_position: Optional[str] = None
        self.separator: Optional[str] = None
        self.decimal_count: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "NumberSettingBuilder":
        return NumberSettingBuilder()


class NumberSettingBuilder(object):
    def __init__(self) -> None:
        self._number_setting = NumberSetting()

    def format(self, format: str) -> "NumberSettingBuilder":
        self._number_setting.format = format
        return self

    def custom_symbol(self, custom_symbol: str) -> "NumberSettingBuilder":
        self._number_setting.custom_symbol = custom_symbol
        return self

    def custom_symbol_position(self, custom_symbol_position: str) -> "NumberSettingBuilder":
        self._number_setting.custom_symbol_position = custom_symbol_position
        return self

    def separator(self, separator: str) -> "NumberSettingBuilder":
        self._number_setting.separator = separator
        return self

    def decimal_count(self, decimal_count: int) -> "NumberSettingBuilder":
        self._number_setting.decimal_count = decimal_count
        return self

    def build(self) -> "NumberSetting":
        return self._number_setting
