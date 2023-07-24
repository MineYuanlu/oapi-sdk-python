# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .update_ticket_request_body import UpdateTicketRequestBody


class UpdateTicketRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.ticket_id: Optional[str] = None
        self.request_body: Optional[UpdateTicketRequestBody] = None

    @staticmethod
    def builder() -> "UpdateTicketRequestBuilder":
        return UpdateTicketRequestBuilder()


class UpdateTicketRequestBuilder(object):

    def __init__(self) -> None:
        update_ticket_request = UpdateTicketRequest()
        update_ticket_request.http_method = HttpMethod.PUT
        update_ticket_request.uri = "/open-apis/helpdesk/v1/tickets/:ticket_id"
        update_ticket_request.token_types = {AccessTokenType.USER}
        self._update_ticket_request: UpdateTicketRequest = update_ticket_request

    def ticket_id(self, ticket_id: str) -> "UpdateTicketRequestBuilder":
        self._update_ticket_request.ticket_id = ticket_id
        self._update_ticket_request.paths["ticket_id"] = str(ticket_id)
        return self

    def request_body(self, request_body: UpdateTicketRequestBody) -> "UpdateTicketRequestBuilder":
        self._update_ticket_request.request_body = request_body
        self._update_ticket_request.body = request_body
        return self

    def build(self) -> UpdateTicketRequest:
        return self._update_ticket_request
