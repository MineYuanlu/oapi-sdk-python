# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .i18n import I18n
from .talent_customized_data_child import TalentCustomizedDataChild


class TalentCustomizedData(object):
    _types = {
        "object_id": str,
        "name": I18n,
        "object_type": int,
        "children": List[TalentCustomizedDataChild],
    }

    def __init__(self, d=None):
        self.object_id: Optional[str] = None
        self.name: Optional[I18n] = None
        self.object_type: Optional[int] = None
        self.children: Optional[List[TalentCustomizedDataChild]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TalentCustomizedDataBuilder":
        return TalentCustomizedDataBuilder()


class TalentCustomizedDataBuilder(object):
    def __init__(self) -> None:
        self._talent_customized_data = TalentCustomizedData()

    def object_id(self, object_id: str) -> "TalentCustomizedDataBuilder":
        self._talent_customized_data.object_id = object_id
        return self

    def name(self, name: I18n) -> "TalentCustomizedDataBuilder":
        self._talent_customized_data.name = name
        return self

    def object_type(self, object_type: int) -> "TalentCustomizedDataBuilder":
        self._talent_customized_data.object_type = object_type
        return self

    def children(self, children: List[TalentCustomizedDataChild]) -> "TalentCustomizedDataBuilder":
        self._talent_customized_data.children = children
        return self

    def build(self) -> "TalentCustomizedData":
        return self._talent_customized_data
