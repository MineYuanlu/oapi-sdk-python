# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .create_faq_request_body import CreateFaqRequestBody


class CreateFaqRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.request_body: Optional[CreateFaqRequestBody] = None

    @staticmethod
    def builder() -> "CreateFaqRequestBuilder":
        return CreateFaqRequestBuilder()


class CreateFaqRequestBuilder(object):

    def __init__(self) -> None:
        create_faq_request = CreateFaqRequest()
        create_faq_request.http_method = HttpMethod.POST
        create_faq_request.uri = "/open-apis/helpdesk/v1/faqs"
        create_faq_request.token_types = {AccessTokenType.USER}
        self._create_faq_request: CreateFaqRequest = create_faq_request

    def request_body(self, request_body: CreateFaqRequestBody) -> "CreateFaqRequestBuilder":
        self._create_faq_request.request_body = request_body
        self._create_faq_request.body = request_body
        return self

    def build(self) -> CreateFaqRequest:
        return self._create_faq_request
