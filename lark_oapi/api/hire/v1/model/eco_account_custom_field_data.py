# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .i18n import I18n


class EcoAccountCustomFieldData(object):
    _types = {
        "key": str,
        "name": I18n,
        "is_required": bool,
        "description": I18n,
    }

    def __init__(self, d=None):
        self.key: Optional[str] = None
        self.name: Optional[I18n] = None
        self.is_required: Optional[bool] = None
        self.description: Optional[I18n] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "EcoAccountCustomFieldDataBuilder":
        return EcoAccountCustomFieldDataBuilder()


class EcoAccountCustomFieldDataBuilder(object):
    def __init__(self) -> None:
        self._eco_account_custom_field_data = EcoAccountCustomFieldData()

    def key(self, key: str) -> "EcoAccountCustomFieldDataBuilder":
        self._eco_account_custom_field_data.key = key
        return self

    def name(self, name: I18n) -> "EcoAccountCustomFieldDataBuilder":
        self._eco_account_custom_field_data.name = name
        return self

    def is_required(self, is_required: bool) -> "EcoAccountCustomFieldDataBuilder":
        self._eco_account_custom_field_data.is_required = is_required
        return self

    def description(self, description: I18n) -> "EcoAccountCustomFieldDataBuilder":
        self._eco_account_custom_field_data.description = description
        return self

    def build(self) -> "EcoAccountCustomFieldData":
        return self._eco_account_custom_field_data
