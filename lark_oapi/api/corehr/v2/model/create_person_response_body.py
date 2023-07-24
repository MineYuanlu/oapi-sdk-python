# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .person_info import PersonInfo


class CreatePersonResponseBody(object):
    _types = {
        "person": PersonInfo,
    }

    def __init__(self, d=None):
        self.person: Optional[PersonInfo] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreatePersonResponseBodyBuilder":
        return CreatePersonResponseBodyBuilder()


class CreatePersonResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._create_person_response_body = CreatePersonResponseBody()

    def person(self, person: PersonInfo) -> "CreatePersonResponseBodyBuilder":
        self._create_person_response_body.person = person
        return self

    def build(self) -> "CreatePersonResponseBody":
        return self._create_person_response_body
