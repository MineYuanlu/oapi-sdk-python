# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class ChatMemberBot(object):
    _types = {
        "bot_id": str,
    }

    def __init__(self, d=None):
        self.bot_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ChatMemberBotBuilder":
        return ChatMemberBotBuilder()


class ChatMemberBotBuilder(object):
    def __init__(self) -> None:
        self._chat_member_bot = ChatMemberBot()

    def bot_id(self, bot_id: str) -> "ChatMemberBotBuilder":
        self._chat_member_bot.bot_id = bot_id
        return self

    def build(self) -> "ChatMemberBot":
        return self._chat_member_bot
