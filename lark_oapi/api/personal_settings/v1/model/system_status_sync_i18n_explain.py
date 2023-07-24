# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class SystemStatusSyncI18nExplain(object):
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
    def builder() -> "SystemStatusSyncI18nExplainBuilder":
        return SystemStatusSyncI18nExplainBuilder()


class SystemStatusSyncI18nExplainBuilder(object):
    def __init__(self) -> None:
        self._system_status_sync_i18n_explain = SystemStatusSyncI18nExplain()

    def zh_cn(self, zh_cn: str) -> "SystemStatusSyncI18nExplainBuilder":
        self._system_status_sync_i18n_explain.zh_cn = zh_cn
        return self

    def en_us(self, en_us: str) -> "SystemStatusSyncI18nExplainBuilder":
        self._system_status_sync_i18n_explain.en_us = en_us
        return self

    def ja_jp(self, ja_jp: str) -> "SystemStatusSyncI18nExplainBuilder":
        self._system_status_sync_i18n_explain.ja_jp = ja_jp
        return self

    def build(self) -> "SystemStatusSyncI18nExplain":
        return self._system_status_sync_i18n_explain
