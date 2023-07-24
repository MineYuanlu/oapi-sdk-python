# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .create_message_request_body import CreateMessageRequestBody


class CreateMessageRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.page_size: Optional[int] = None
        self.page_token: Optional[str] = None
        self.request_body: Optional[CreateMessageRequestBody] = None

    @staticmethod
    def builder() -> "CreateMessageRequestBuilder":
        return CreateMessageRequestBuilder()


class CreateMessageRequestBuilder(object):

    def __init__(self) -> None:
        create_message_request = CreateMessageRequest()
        create_message_request.http_method = HttpMethod.POST
        create_message_request.uri = "/open-apis/search/v2/message"
        create_message_request.token_types = {AccessTokenType.USER}
        self._create_message_request: CreateMessageRequest = create_message_request

    def user_id_type(self, user_id_type: str) -> "CreateMessageRequestBuilder":
        self._create_message_request.user_id_type = user_id_type
        self._create_message_request.add_query("user_id_type", user_id_type)
        return self

    def page_size(self, page_size: int) -> "CreateMessageRequestBuilder":
        self._create_message_request.page_size = page_size
        self._create_message_request.add_query("page_size", page_size)
        return self

    def page_token(self, page_token: str) -> "CreateMessageRequestBuilder":
        self._create_message_request.page_token = page_token
        self._create_message_request.add_query("page_token", page_token)
        return self

    def request_body(self, request_body: CreateMessageRequestBody) -> "CreateMessageRequestBuilder":
        self._create_message_request.request_body = request_body
        self._create_message_request.body = request_body
        return self

    def build(self) -> CreateMessageRequest:
        return self._create_message_request
