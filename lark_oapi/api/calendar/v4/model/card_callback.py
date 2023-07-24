# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .myai_card_status import MyaiCardStatus


class CardCallback(object):
    _types = {
        "message_id": int,
        "status": MyaiCardStatus,
        "callback_info": str,
    }

    def __init__(self, d=None):
        self.message_id: Optional[int] = None
        self.status: Optional[MyaiCardStatus] = None
        self.callback_info: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CardCallbackBuilder":
        return CardCallbackBuilder()


class CardCallbackBuilder(object):
    def __init__(self) -> None:
        self._card_callback = CardCallback()

    def message_id(self, message_id: int) -> "CardCallbackBuilder":
        self._card_callback.message_id = message_id
        return self

    def status(self, status: MyaiCardStatus) -> "CardCallbackBuilder":
        self._card_callback.status = status
        return self

    def callback_info(self, callback_info: str) -> "CardCallbackBuilder":
        self._card_callback.callback_info = callback_info
        return self

    def build(self) -> "CardCallback":
        return self._card_callback
