# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class GetTicketCustomizedFieldRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.ticket_customized_field_id: Optional[str] = None

    @staticmethod
    def builder() -> "GetTicketCustomizedFieldRequestBuilder":
        return GetTicketCustomizedFieldRequestBuilder()


class GetTicketCustomizedFieldRequestBuilder(object):

    def __init__(self) -> None:
        get_ticket_customized_field_request = GetTicketCustomizedFieldRequest()
        get_ticket_customized_field_request.http_method = HttpMethod.GET
        get_ticket_customized_field_request.uri = "/open-apis/helpdesk/v1/ticket_customized_fields/:ticket_customized_field_id"
        get_ticket_customized_field_request.token_types = {AccessTokenType.TENANT}
        self._get_ticket_customized_field_request: GetTicketCustomizedFieldRequest = get_ticket_customized_field_request

    def ticket_customized_field_id(self, ticket_customized_field_id: str) -> "GetTicketCustomizedFieldRequestBuilder":
        self._get_ticket_customized_field_request.ticket_customized_field_id = ticket_customized_field_id
        self._get_ticket_customized_field_request.paths["ticket_customized_field_id"] = str(ticket_customized_field_id)
        return self

    def build(self) -> GetTicketCustomizedFieldRequest:
        return self._get_ticket_customized_field_request
