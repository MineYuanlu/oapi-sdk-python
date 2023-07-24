# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .eco_account_custom_field_data import EcoAccountCustomFieldData


class EcoAccountCustomField(object):
    _types = {
        "scope": int,
        "custom_field_list": List[EcoAccountCustomFieldData],
    }

    def __init__(self, d=None):
        self.scope: Optional[int] = None
        self.custom_field_list: Optional[List[EcoAccountCustomFieldData]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "EcoAccountCustomFieldBuilder":
        return EcoAccountCustomFieldBuilder()


class EcoAccountCustomFieldBuilder(object):
    def __init__(self) -> None:
        self._eco_account_custom_field = EcoAccountCustomField()

    def scope(self, scope: int) -> "EcoAccountCustomFieldBuilder":
        self._eco_account_custom_field.scope = scope
        return self

    def custom_field_list(self, custom_field_list: List[EcoAccountCustomFieldData]) -> "EcoAccountCustomFieldBuilder":
        self._eco_account_custom_field.custom_field_list = custom_field_list
        return self

    def build(self) -> "EcoAccountCustomField":
        return self._eco_account_custom_field
