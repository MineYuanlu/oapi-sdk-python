# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class Pin(object):
    _types = {
        "message_id": str,
        "chat_id": str,
        "operator_id": str,
        "operator_id_type": str,
        "create_time": str,
    }

    def __init__(self, d=None):
        self.message_id: Optional[str] = None
        self.chat_id: Optional[str] = None
        self.operator_id: Optional[str] = None
        self.operator_id_type: Optional[str] = None
        self.create_time: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "PinBuilder":
        return PinBuilder()


class PinBuilder(object):
    def __init__(self) -> None:
        self._pin = Pin()

    def message_id(self, message_id: str) -> "PinBuilder":
        self._pin.message_id = message_id
        return self

    def chat_id(self, chat_id: str) -> "PinBuilder":
        self._pin.chat_id = chat_id
        return self

    def operator_id(self, operator_id: str) -> "PinBuilder":
        self._pin.operator_id = operator_id
        return self

    def operator_id_type(self, operator_id_type: str) -> "PinBuilder":
        self._pin.operator_id_type = operator_id_type
        return self

    def create_time(self, create_time: str) -> "PinBuilder":
        self._pin.create_time = create_time
        return self

    def build(self) -> "Pin":
        return self._pin
