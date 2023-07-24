# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class Abbreviation(object):
    _types = {
        "id": str,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AbbreviationBuilder":
        return AbbreviationBuilder()


class AbbreviationBuilder(object):
    def __init__(self) -> None:
        self._abbreviation = Abbreviation()

    def id(self, id: str) -> "AbbreviationBuilder":
        self._abbreviation.id = id
        return self

    def build(self) -> "Abbreviation":
        return self._abbreviation
