# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .eco_background_check_package_additional_item import EcoBackgroundCheckPackageAdditionalItem
from .eco_background_check_package_data import EcoBackgroundCheckPackageData


class EcoBackgroundCheckPackage(object):
    _types = {
        "account_id": str,
        "package_list": List[EcoBackgroundCheckPackageData],
        "additional_item_list": List[EcoBackgroundCheckPackageAdditionalItem],
    }

    def __init__(self, d=None):
        self.account_id: Optional[str] = None
        self.package_list: Optional[List[EcoBackgroundCheckPackageData]] = None
        self.additional_item_list: Optional[List[EcoBackgroundCheckPackageAdditionalItem]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "EcoBackgroundCheckPackageBuilder":
        return EcoBackgroundCheckPackageBuilder()


class EcoBackgroundCheckPackageBuilder(object):
    def __init__(self) -> None:
        self._eco_background_check_package = EcoBackgroundCheckPackage()

    def account_id(self, account_id: str) -> "EcoBackgroundCheckPackageBuilder":
        self._eco_background_check_package.account_id = account_id
        return self

    def package_list(self, package_list: List[EcoBackgroundCheckPackageData]) -> "EcoBackgroundCheckPackageBuilder":
        self._eco_background_check_package.package_list = package_list
        return self

    def additional_item_list(self, additional_item_list: List[
        EcoBackgroundCheckPackageAdditionalItem]) -> "EcoBackgroundCheckPackageBuilder":
        self._eco_background_check_package.additional_item_list = additional_item_list
        return self

    def build(self) -> "EcoBackgroundCheckPackage":
        return self._eco_background_check_package
