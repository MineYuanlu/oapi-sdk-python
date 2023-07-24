# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .badge import Badge


class CreateBadgeRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.request_body: Optional[Badge] = None

    @staticmethod
    def builder() -> "CreateBadgeRequestBuilder":
        return CreateBadgeRequestBuilder()


class CreateBadgeRequestBuilder(object):

    def __init__(self) -> None:
        create_badge_request = CreateBadgeRequest()
        create_badge_request.http_method = HttpMethod.POST
        create_badge_request.uri = "/open-apis/admin/v1/badges"
        create_badge_request.token_types = {AccessTokenType.TENANT}
        self._create_badge_request: CreateBadgeRequest = create_badge_request

    def request_body(self, request_body: Badge) -> "CreateBadgeRequestBuilder":
        self._create_badge_request.request_body = request_body
        self._create_badge_request.body = request_body
        return self

    def build(self) -> CreateBadgeRequest:
        return self._create_badge_request
