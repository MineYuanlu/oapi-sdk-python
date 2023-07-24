# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .dynamic_group_rule import DynamicGroupRule
from .group_visible_scope import GroupVisibleScope


class Group(object):
    _types = {
        "id": str,
        "name": str,
        "description": str,
        "member_user_count": int,
        "member_department_count": int,
        "type": int,
        "dynamic_group_rule": DynamicGroupRule,
        "visible_scope": GroupVisibleScope,
        "department_scope_list": List[str],
        "group_id": str,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.name: Optional[str] = None
        self.description: Optional[str] = None
        self.member_user_count: Optional[int] = None
        self.member_department_count: Optional[int] = None
        self.type: Optional[int] = None
        self.dynamic_group_rule: Optional[DynamicGroupRule] = None
        self.visible_scope: Optional[GroupVisibleScope] = None
        self.department_scope_list: Optional[List[str]] = None
        self.group_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GroupBuilder":
        return GroupBuilder()


class GroupBuilder(object):
    def __init__(self) -> None:
        self._group = Group()

    def id(self, id: str) -> "GroupBuilder":
        self._group.id = id
        return self

    def name(self, name: str) -> "GroupBuilder":
        self._group.name = name
        return self

    def description(self, description: str) -> "GroupBuilder":
        self._group.description = description
        return self

    def member_user_count(self, member_user_count: int) -> "GroupBuilder":
        self._group.member_user_count = member_user_count
        return self

    def member_department_count(self, member_department_count: int) -> "GroupBuilder":
        self._group.member_department_count = member_department_count
        return self

    def type(self, type: int) -> "GroupBuilder":
        self._group.type = type
        return self

    def dynamic_group_rule(self, dynamic_group_rule: DynamicGroupRule) -> "GroupBuilder":
        self._group.dynamic_group_rule = dynamic_group_rule
        return self

    def visible_scope(self, visible_scope: GroupVisibleScope) -> "GroupBuilder":
        self._group.visible_scope = visible_scope
        return self

    def department_scope_list(self, department_scope_list: List[str]) -> "GroupBuilder":
        self._group.department_scope_list = department_scope_list
        return self

    def group_id(self, group_id: str) -> "GroupBuilder":
        self._group.group_id = group_id
        return self

    def build(self) -> "Group":
        return self._group
