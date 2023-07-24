# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .app_table_view_property import AppTableViewProperty


class AppTableView(object):
    _types = {
        "view_id": str,
        "view_name": str,
        "view_type": str,
        "property": AppTableViewProperty,
        "view_public_level": str,
        "view_private_owner_id": str,
    }

    def __init__(self, d=None):
        self.view_id: Optional[str] = None
        self.view_name: Optional[str] = None
        self.view_type: Optional[str] = None
        self.property: Optional[AppTableViewProperty] = None
        self.view_public_level: Optional[str] = None
        self.view_private_owner_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AppTableViewBuilder":
        return AppTableViewBuilder()


class AppTableViewBuilder(object):
    def __init__(self) -> None:
        self._app_table_view = AppTableView()

    def view_id(self, view_id: str) -> "AppTableViewBuilder":
        self._app_table_view.view_id = view_id
        return self

    def view_name(self, view_name: str) -> "AppTableViewBuilder":
        self._app_table_view.view_name = view_name
        return self

    def view_type(self, view_type: str) -> "AppTableViewBuilder":
        self._app_table_view.view_type = view_type
        return self

    def property(self, property: AppTableViewProperty) -> "AppTableViewBuilder":
        self._app_table_view.property = property
        return self

    def view_public_level(self, view_public_level: str) -> "AppTableViewBuilder":
        self._app_table_view.view_public_level = view_public_level
        return self

    def view_private_owner_id(self, view_private_owner_id: str) -> "AppTableViewBuilder":
        self._app_table_view.view_private_owner_id = view_private_owner_id
        return self

    def build(self) -> "AppTableView":
        return self._app_table_view
