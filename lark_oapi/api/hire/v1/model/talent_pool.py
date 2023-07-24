# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .i18n import I18n


class TalentPool(object):
    _types = {
        "id": str,
        "i18n_name": I18n,
        "i18n_description": I18n,
        "parent_id": str,
        "is_private": int,
        "create_time": str,
        "modify_time": str,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.i18n_name: Optional[I18n] = None
        self.i18n_description: Optional[I18n] = None
        self.parent_id: Optional[str] = None
        self.is_private: Optional[int] = None
        self.create_time: Optional[str] = None
        self.modify_time: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TalentPoolBuilder":
        return TalentPoolBuilder()


class TalentPoolBuilder(object):
    def __init__(self) -> None:
        self._talent_pool = TalentPool()

    def id(self, id: str) -> "TalentPoolBuilder":
        self._talent_pool.id = id
        return self

    def i18n_name(self, i18n_name: I18n) -> "TalentPoolBuilder":
        self._talent_pool.i18n_name = i18n_name
        return self

    def i18n_description(self, i18n_description: I18n) -> "TalentPoolBuilder":
        self._talent_pool.i18n_description = i18n_description
        return self

    def parent_id(self, parent_id: str) -> "TalentPoolBuilder":
        self._talent_pool.parent_id = parent_id
        return self

    def is_private(self, is_private: int) -> "TalentPoolBuilder":
        self._talent_pool.is_private = is_private
        return self

    def create_time(self, create_time: str) -> "TalentPoolBuilder":
        self._talent_pool.create_time = create_time
        return self

    def modify_time(self, modify_time: str) -> "TalentPoolBuilder":
        self._talent_pool.modify_time = modify_time
        return self

    def build(self) -> "TalentPool":
        return self._talent_pool
