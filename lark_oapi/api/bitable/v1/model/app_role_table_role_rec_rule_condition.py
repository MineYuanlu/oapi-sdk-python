# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class AppRoleTableRoleRecRuleCondition(object):
    _types = {
        "field_name": str,
        "operator": str,
        "value": List[str],
        "field_type": int,
    }

    def __init__(self, d=None):
        self.field_name: Optional[str] = None
        self.operator: Optional[str] = None
        self.value: Optional[List[str]] = None
        self.field_type: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AppRoleTableRoleRecRuleConditionBuilder":
        return AppRoleTableRoleRecRuleConditionBuilder()


class AppRoleTableRoleRecRuleConditionBuilder(object):
    def __init__(self) -> None:
        self._app_role_table_role_rec_rule_condition = AppRoleTableRoleRecRuleCondition()

    def field_name(self, field_name: str) -> "AppRoleTableRoleRecRuleConditionBuilder":
        self._app_role_table_role_rec_rule_condition.field_name = field_name
        return self

    def operator(self, operator: str) -> "AppRoleTableRoleRecRuleConditionBuilder":
        self._app_role_table_role_rec_rule_condition.operator = operator
        return self

    def value(self, value: List[str]) -> "AppRoleTableRoleRecRuleConditionBuilder":
        self._app_role_table_role_rec_rule_condition.value = value
        return self

    def field_type(self, field_type: int) -> "AppRoleTableRoleRecRuleConditionBuilder":
        self._app_role_table_role_rec_rule_condition.field_type = field_type
        return self

    def build(self) -> "AppRoleTableRoleRecRuleCondition":
        return self._app_role_table_role_rec_rule_condition
