# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .calendar import Calendar


class PatchCalendarRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.calendar_id: Optional[str] = None
        self.request_body: Optional[Calendar] = None

    @staticmethod
    def builder() -> "PatchCalendarRequestBuilder":
        return PatchCalendarRequestBuilder()


class PatchCalendarRequestBuilder(object):

    def __init__(self) -> None:
        patch_calendar_request = PatchCalendarRequest()
        patch_calendar_request.http_method = HttpMethod.PATCH
        patch_calendar_request.uri = "/open-apis/calendar/v4/calendars/:calendar_id"
        patch_calendar_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._patch_calendar_request: PatchCalendarRequest = patch_calendar_request

    def calendar_id(self, calendar_id: str) -> "PatchCalendarRequestBuilder":
        self._patch_calendar_request.calendar_id = calendar_id
        self._patch_calendar_request.paths["calendar_id"] = str(calendar_id)
        return self

    def request_body(self, request_body: Calendar) -> "PatchCalendarRequestBuilder":
        self._patch_calendar_request.request_body = request_body
        self._patch_calendar_request.body = request_body
        return self

    def build(self) -> PatchCalendarRequest:
        return self._patch_calendar_request
