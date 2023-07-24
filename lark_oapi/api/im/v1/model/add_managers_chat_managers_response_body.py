# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class AddManagersChatManagersResponseBody(object):
    _types = {
        "chat_managers": List[str],
        "chat_bot_managers": List[str],
    }

    def __init__(self, d=None):
        self.chat_managers: Optional[List[str]] = None
        self.chat_bot_managers: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AddManagersChatManagersResponseBodyBuilder":
        return AddManagersChatManagersResponseBodyBuilder()


class AddManagersChatManagersResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._add_managers_chat_managers_response_body = AddManagersChatManagersResponseBody()

    def chat_managers(self, chat_managers: List[str]) -> "AddManagersChatManagersResponseBodyBuilder":
        self._add_managers_chat_managers_response_body.chat_managers = chat_managers
        return self

    def chat_bot_managers(self, chat_bot_managers: List[str]) -> "AddManagersChatManagersResponseBodyBuilder":
        self._add_managers_chat_managers_response_body.chat_bot_managers = chat_bot_managers
        return self

    def build(self) -> "AddManagersChatManagersResponseBody":
        return self._add_managers_chat_managers_response_body
