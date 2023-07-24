# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class DeleteChatMenuTreeRequestBody(object):
    _types = {
        "chat_menu_top_level_ids": List[int],
    }

    def __init__(self, d=None):
        self.chat_menu_top_level_ids: Optional[List[int]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DeleteChatMenuTreeRequestBodyBuilder":
        return DeleteChatMenuTreeRequestBodyBuilder()


class DeleteChatMenuTreeRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._delete_chat_menu_tree_request_body = DeleteChatMenuTreeRequestBody()

    def chat_menu_top_level_ids(self, chat_menu_top_level_ids: List[int]) -> "DeleteChatMenuTreeRequestBodyBuilder":
        self._delete_chat_menu_tree_request_body.chat_menu_top_level_ids = chat_menu_top_level_ids
        return self

    def build(self) -> "DeleteChatMenuTreeRequestBody":
        return self._delete_chat_menu_tree_request_body
