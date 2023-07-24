# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .access_data import AccessData


class TemplateWorkplaceAccessData(object):
    _types = {
        "tpl_id": str,
        "access_data": AccessData,
    }

    def __init__(self, d=None):
        self.tpl_id: Optional[str] = None
        self.access_data: Optional[AccessData] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TemplateWorkplaceAccessDataBuilder":
        return TemplateWorkplaceAccessDataBuilder()


class TemplateWorkplaceAccessDataBuilder(object):
    def __init__(self) -> None:
        self._template_workplace_access_data = TemplateWorkplaceAccessData()

    def tpl_id(self, tpl_id: str) -> "TemplateWorkplaceAccessDataBuilder":
        self._template_workplace_access_data.tpl_id = tpl_id
        return self

    def access_data(self, access_data: AccessData) -> "TemplateWorkplaceAccessDataBuilder":
        self._template_workplace_access_data.access_data = access_data
        return self

    def build(self) -> "TemplateWorkplaceAccessData":
        return self._template_workplace_access_data
