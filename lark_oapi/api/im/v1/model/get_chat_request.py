# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class GetChatRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.chat_id: Optional[str] = None

    @staticmethod
    def builder() -> "GetChatRequestBuilder":
        return GetChatRequestBuilder()


class GetChatRequestBuilder(object):

    def __init__(self) -> None:
        get_chat_request = GetChatRequest()
        get_chat_request.http_method = HttpMethod.GET
        get_chat_request.uri = "/open-apis/im/v1/chats/:chat_id"
        get_chat_request.token_types = {AccessTokenType.USER, AccessTokenType.TENANT}
        self._get_chat_request: GetChatRequest = get_chat_request

    def user_id_type(self, user_id_type: str) -> "GetChatRequestBuilder":
        self._get_chat_request.user_id_type = user_id_type
        self._get_chat_request.add_query("user_id_type", user_id_type)
        return self

    def chat_id(self, chat_id: str) -> "GetChatRequestBuilder":
        self._get_chat_request.chat_id = chat_id
        self._get_chat_request.paths["chat_id"] = str(chat_id)
        return self

    def build(self) -> GetChatRequest:
        return self._get_chat_request
