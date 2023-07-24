# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .app_table_view_property_filter_info import AppTableViewPropertyFilterInfo
from .app_table_view_property_hierarchy_config import AppTableViewPropertyHierarchyConfig


class AppTableViewProperty(object):
    _types = {
        "filter_info": AppTableViewPropertyFilterInfo,
        "hidden_fields": List[str],
        "hierarchy_config": AppTableViewPropertyHierarchyConfig,
    }

    def __init__(self, d=None):
        self.filter_info: Optional[AppTableViewPropertyFilterInfo] = None
        self.hidden_fields: Optional[List[str]] = None
        self.hierarchy_config: Optional[AppTableViewPropertyHierarchyConfig] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AppTableViewPropertyBuilder":
        return AppTableViewPropertyBuilder()


class AppTableViewPropertyBuilder(object):
    def __init__(self) -> None:
        self._app_table_view_property = AppTableViewProperty()

    def filter_info(self, filter_info: AppTableViewPropertyFilterInfo) -> "AppTableViewPropertyBuilder":
        self._app_table_view_property.filter_info = filter_info
        return self

    def hidden_fields(self, hidden_fields: List[str]) -> "AppTableViewPropertyBuilder":
        self._app_table_view_property.hidden_fields = hidden_fields
        return self

    def hierarchy_config(self, hierarchy_config: AppTableViewPropertyHierarchyConfig) -> "AppTableViewPropertyBuilder":
        self._app_table_view_property.hierarchy_config = hierarchy_config
        return self

    def build(self) -> "AppTableViewProperty":
        return self._app_table_view_property
