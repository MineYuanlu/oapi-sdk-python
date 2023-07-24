# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class EcoBackgroundCheckPackageData(object):
    _types = {
        "id": str,
        "name": str,
        "description": str,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.name: Optional[str] = None
        self.description: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "EcoBackgroundCheckPackageDataBuilder":
        return EcoBackgroundCheckPackageDataBuilder()


class EcoBackgroundCheckPackageDataBuilder(object):
    def __init__(self) -> None:
        self._eco_background_check_package_data = EcoBackgroundCheckPackageData()

    def id(self, id: str) -> "EcoBackgroundCheckPackageDataBuilder":
        self._eco_background_check_package_data.id = id
        return self

    def name(self, name: str) -> "EcoBackgroundCheckPackageDataBuilder":
        self._eco_background_check_package_data.name = name
        return self

    def description(self, description: str) -> "EcoBackgroundCheckPackageDataBuilder":
        self._eco_background_check_package_data.description = description
        return self

    def build(self) -> "EcoBackgroundCheckPackageData":
        return self._eco_background_check_package_data
