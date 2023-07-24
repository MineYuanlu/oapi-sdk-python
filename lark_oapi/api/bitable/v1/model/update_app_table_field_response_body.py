# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .app_table_field import AppTableField


class UpdateAppTableFieldResponseBody(object):
    _types = {
        "field": AppTableField,
    }

    def __init__(self, d=None):
        self.field: Optional[AppTableField] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UpdateAppTableFieldResponseBodyBuilder":
        return UpdateAppTableFieldResponseBodyBuilder()


class UpdateAppTableFieldResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._update_app_table_field_response_body = UpdateAppTableFieldResponseBody()

    def field(self, field: AppTableField) -> "UpdateAppTableFieldResponseBodyBuilder":
        self._update_app_table_field_response_body.field = field
        return self

    def build(self) -> "UpdateAppTableFieldResponseBody":
        return self._update_app_table_field_response_body
