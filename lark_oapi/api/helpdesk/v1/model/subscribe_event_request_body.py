# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .event import Event


class SubscribeEventRequestBody(object):
    _types = {
        "events": List[Event],
    }

    def __init__(self, d=None):
        self.events: Optional[List[Event]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SubscribeEventRequestBodyBuilder":
        return SubscribeEventRequestBodyBuilder()


class SubscribeEventRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._subscribe_event_request_body = SubscribeEventRequestBody()

    def events(self, events: List[Event]) -> "SubscribeEventRequestBodyBuilder":
        self._subscribe_event_request_body.events = events
        return self

    def build(self) -> "SubscribeEventRequestBody":
        return self._subscribe_event_request_body
