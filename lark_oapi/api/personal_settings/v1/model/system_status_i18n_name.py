# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class SystemStatusI18nName(object):
    _types = {
        "zh_cn": str,
        "en_us": str,
        "ja_jp": str,
    }

    def __init__(self, d=None):
        self.zh_cn: Optional[str] = None
        self.en_us: Optional[str] = None
        self.ja_jp: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SystemStatusI18nNameBuilder":
        return SystemStatusI18nNameBuilder()


class SystemStatusI18nNameBuilder(object):
    def __init__(self) -> None:
        self._system_status_i18n_name = SystemStatusI18nName()

    def zh_cn(self, zh_cn: str) -> "SystemStatusI18nNameBuilder":
        self._system_status_i18n_name.zh_cn = zh_cn
        return self

    def en_us(self, en_us: str) -> "SystemStatusI18nNameBuilder":
        self._system_status_i18n_name.en_us = en_us
        return self

    def ja_jp(self, ja_jp: str) -> "SystemStatusI18nNameBuilder":
        self._system_status_i18n_name.ja_jp = ja_jp
        return self

    def build(self) -> "SystemStatusI18nName":
        return self._system_status_i18n_name
