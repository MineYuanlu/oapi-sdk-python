# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .delete_chat_menu_tree_request_body import DeleteChatMenuTreeRequestBody


class DeleteChatMenuTreeRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.chat_id: Optional[str] = None
        self.request_body: Optional[DeleteChatMenuTreeRequestBody] = None

    @staticmethod
    def builder() -> "DeleteChatMenuTreeRequestBuilder":
        return DeleteChatMenuTreeRequestBuilder()


class DeleteChatMenuTreeRequestBuilder(object):

    def __init__(self) -> None:
        delete_chat_menu_tree_request = DeleteChatMenuTreeRequest()
        delete_chat_menu_tree_request.http_method = HttpMethod.DELETE
        delete_chat_menu_tree_request.uri = "/open-apis/im/v1/chats/:chat_id/menu_tree"
        delete_chat_menu_tree_request.token_types = {AccessTokenType.TENANT}
        self._delete_chat_menu_tree_request: DeleteChatMenuTreeRequest = delete_chat_menu_tree_request

    def chat_id(self, chat_id: str) -> "DeleteChatMenuTreeRequestBuilder":
        self._delete_chat_menu_tree_request.chat_id = chat_id
        self._delete_chat_menu_tree_request.paths["chat_id"] = str(chat_id)
        return self

    def request_body(self, request_body: DeleteChatMenuTreeRequestBody) -> "DeleteChatMenuTreeRequestBuilder":
        self._delete_chat_menu_tree_request.request_body = request_body
        self._delete_chat_menu_tree_request.body = request_body
        return self

    def build(self) -> DeleteChatMenuTreeRequest:
        return self._delete_chat_menu_tree_request
