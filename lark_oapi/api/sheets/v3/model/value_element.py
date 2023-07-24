# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class ValueElement(object):
    _types = {
        "value": str,
    }

    def __init__(self, d=None):
        self.value: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ValueElementBuilder":
        return ValueElementBuilder()


class ValueElementBuilder(object):
    def __init__(self) -> None:
        self._value_element = ValueElement()

    def value(self, value: str) -> "ValueElementBuilder":
        self._value_element.value = value
        return self

    def build(self) -> "ValueElement":
        return self._value_element
