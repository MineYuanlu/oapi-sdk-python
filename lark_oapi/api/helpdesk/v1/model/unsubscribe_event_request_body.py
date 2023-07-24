# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .event import Event


class UnsubscribeEventRequestBody(object):
    _types = {
        "events": List[Event],
    }

    def __init__(self, d=None):
        self.events: Optional[List[Event]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UnsubscribeEventRequestBodyBuilder":
        return UnsubscribeEventRequestBodyBuilder()


class UnsubscribeEventRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._unsubscribe_event_request_body = UnsubscribeEventRequestBody()

    def events(self, events: List[Event]) -> "UnsubscribeEventRequestBodyBuilder":
        self._unsubscribe_event_request_body.events = events
        return self

    def build(self) -> "UnsubscribeEventRequestBody":
        return self._unsubscribe_event_request_body
