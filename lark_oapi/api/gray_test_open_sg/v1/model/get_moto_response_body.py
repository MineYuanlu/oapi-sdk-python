# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .moto import Moto


class GetMotoResponseBody(object):
    _types = {
        "moto": Moto,
    }

    def __init__(self, d=None):
        self.moto: Optional[Moto] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetMotoResponseBodyBuilder":
        return GetMotoResponseBodyBuilder()


class GetMotoResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._get_moto_response_body = GetMotoResponseBody()

    def moto(self, moto: Moto) -> "GetMotoResponseBodyBuilder":
        self._get_moto_response_body.moto = moto
        return self

    def build(self) -> "GetMotoResponseBody":
        return self._get_moto_response_body
