# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .notification import Notification


class CreateNotificationRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.request_body: Optional[Notification] = None

    @staticmethod
    def builder() -> "CreateNotificationRequestBuilder":
        return CreateNotificationRequestBuilder()


class CreateNotificationRequestBuilder(object):

    def __init__(self) -> None:
        create_notification_request = CreateNotificationRequest()
        create_notification_request.http_method = HttpMethod.POST
        create_notification_request.uri = "/open-apis/helpdesk/v1/notifications"
        create_notification_request.token_types = {AccessTokenType.USER}
        self._create_notification_request: CreateNotificationRequest = create_notification_request

    def user_id_type(self, user_id_type: str) -> "CreateNotificationRequestBuilder":
        self._create_notification_request.user_id_type = user_id_type
        self._create_notification_request.add_query("user_id_type", user_id_type)
        return self

    def request_body(self, request_body: Notification) -> "CreateNotificationRequestBuilder":
        self._create_notification_request.request_body = request_body
        self._create_notification_request.body = request_body
        return self

    def build(self) -> CreateNotificationRequest:
        return self._create_notification_request
