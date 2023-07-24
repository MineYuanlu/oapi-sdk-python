# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .create_calendar_event_response_body import CreateCalendarEventResponseBody


class CreateCalendarEventResponse(BaseResponse):
    _types = {
        "data": CreateCalendarEventResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[CreateCalendarEventResponseBody] = None
        init(self, d, self._types)
