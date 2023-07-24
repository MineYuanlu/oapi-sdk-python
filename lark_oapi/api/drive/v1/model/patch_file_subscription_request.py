# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .patch_file_subscription_request_body import PatchFileSubscriptionRequestBody


class PatchFileSubscriptionRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.file_token: Optional[str] = None
        self.subscription_id: Optional[str] = None
        self.request_body: Optional[PatchFileSubscriptionRequestBody] = None

    @staticmethod
    def builder() -> "PatchFileSubscriptionRequestBuilder":
        return PatchFileSubscriptionRequestBuilder()


class PatchFileSubscriptionRequestBuilder(object):

    def __init__(self) -> None:
        patch_file_subscription_request = PatchFileSubscriptionRequest()
        patch_file_subscription_request.http_method = HttpMethod.PATCH
        patch_file_subscription_request.uri = "/open-apis/drive/v1/files/:file_token/subscriptions/:subscription_id"
        patch_file_subscription_request.token_types = {AccessTokenType.USER}
        self._patch_file_subscription_request: PatchFileSubscriptionRequest = patch_file_subscription_request

    def file_token(self, file_token: str) -> "PatchFileSubscriptionRequestBuilder":
        self._patch_file_subscription_request.file_token = file_token
        self._patch_file_subscription_request.paths["file_token"] = str(file_token)
        return self

    def subscription_id(self, subscription_id: str) -> "PatchFileSubscriptionRequestBuilder":
        self._patch_file_subscription_request.subscription_id = subscription_id
        self._patch_file_subscription_request.paths["subscription_id"] = str(subscription_id)
        return self

    def request_body(self, request_body: PatchFileSubscriptionRequestBody) -> "PatchFileSubscriptionRequestBuilder":
        self._patch_file_subscription_request.request_body = request_body
        self._patch_file_subscription_request.body = request_body
        return self

    def build(self) -> PatchFileSubscriptionRequest:
        return self._patch_file_subscription_request
