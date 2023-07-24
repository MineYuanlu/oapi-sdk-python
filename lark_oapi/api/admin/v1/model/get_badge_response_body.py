# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .badge import Badge


class GetBadgeResponseBody(object):
    _types = {
        "badge": Badge,
    }

    def __init__(self, d=None):
        self.badge: Optional[Badge] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetBadgeResponseBodyBuilder":
        return GetBadgeResponseBodyBuilder()


class GetBadgeResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._get_badge_response_body = GetBadgeResponseBody()

    def badge(self, badge: Badge) -> "GetBadgeResponseBodyBuilder":
        self._get_badge_response_body.badge = badge
        return self

    def build(self) -> "GetBadgeResponseBody":
        return self._get_badge_response_body
