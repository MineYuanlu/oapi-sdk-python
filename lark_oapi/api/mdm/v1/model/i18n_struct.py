# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class I18nStruct(object):
    _types = {
        "lang_locale": str,
        "value": str,
        "valid_to": str,
    }

    def __init__(self, d=None):
        self.lang_locale: Optional[str] = None
        self.value: Optional[str] = None
        self.valid_to: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "I18nStructBuilder":
        return I18nStructBuilder()


class I18nStructBuilder(object):
    def __init__(self) -> None:
        self._i18n_struct = I18nStruct()

    def lang_locale(self, lang_locale: str) -> "I18nStructBuilder":
        self._i18n_struct.lang_locale = lang_locale
        return self

    def value(self, value: str) -> "I18nStructBuilder":
        self._i18n_struct.value = value
        return self

    def valid_to(self, valid_to: str) -> "I18nStructBuilder":
        self._i18n_struct.valid_to = valid_to
        return self

    def build(self) -> "I18nStruct":
        return self._i18n_struct
