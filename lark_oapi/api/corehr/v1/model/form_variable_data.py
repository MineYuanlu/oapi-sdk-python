# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .form_field_variable import FormFieldVariable


class FormVariableData(object):
    _types = {
        "field_variable_values": List[FormFieldVariable],
    }

    def __init__(self, d=None):
        self.field_variable_values: Optional[List[FormFieldVariable]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "FormVariableDataBuilder":
        return FormVariableDataBuilder()


class FormVariableDataBuilder(object):
    def __init__(self) -> None:
        self._form_variable_data = FormVariableData()

    def field_variable_values(self, field_variable_values: List[FormFieldVariable]) -> "FormVariableDataBuilder":
        self._form_variable_data.field_variable_values = field_variable_values
        return self

    def build(self) -> "FormVariableData":
        return self._form_variable_data
