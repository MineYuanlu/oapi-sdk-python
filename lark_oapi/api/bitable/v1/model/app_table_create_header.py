# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .app_table_field_description import AppTableFieldDescription
from .app_table_field_property import AppTableFieldProperty


class AppTableCreateHeader(object):
    _types = {
        "field_id": str,
        "field_name": str,
        "type": int,
        "property": AppTableFieldProperty,
        "description": AppTableFieldDescription,
    }

    def __init__(self, d=None):
        self.field_id: Optional[str] = None
        self.field_name: Optional[str] = None
        self.type: Optional[int] = None
        self.property: Optional[AppTableFieldProperty] = None
        self.description: Optional[AppTableFieldDescription] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AppTableCreateHeaderBuilder":
        return AppTableCreateHeaderBuilder()


class AppTableCreateHeaderBuilder(object):
    def __init__(self) -> None:
        self._app_table_create_header = AppTableCreateHeader()

    def field_id(self, field_id: str) -> "AppTableCreateHeaderBuilder":
        self._app_table_create_header.field_id = field_id
        return self

    def field_name(self, field_name: str) -> "AppTableCreateHeaderBuilder":
        self._app_table_create_header.field_name = field_name
        return self

    def type(self, type: int) -> "AppTableCreateHeaderBuilder":
        self._app_table_create_header.type = type
        return self

    def property(self, property: AppTableFieldProperty) -> "AppTableCreateHeaderBuilder":
        self._app_table_create_header.property = property
        return self

    def description(self, description: AppTableFieldDescription) -> "AppTableCreateHeaderBuilder":
        self._app_table_create_header.description = description
        return self

    def build(self) -> "AppTableCreateHeader":
        return self._app_table_create_header
