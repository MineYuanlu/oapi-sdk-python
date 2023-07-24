# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class MeetingInviteStatus(object):
    _types = {
        "id": str,
        "user_type": int,
        "status": int,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.user_type: Optional[int] = None
        self.status: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "MeetingInviteStatusBuilder":
        return MeetingInviteStatusBuilder()


class MeetingInviteStatusBuilder(object):
    def __init__(self) -> None:
        self._meeting_invite_status = MeetingInviteStatus()

    def id(self, id: str) -> "MeetingInviteStatusBuilder":
        self._meeting_invite_status.id = id
        return self

    def user_type(self, user_type: int) -> "MeetingInviteStatusBuilder":
        self._meeting_invite_status.user_type = user_type
        return self

    def status(self, status: int) -> "MeetingInviteStatusBuilder":
        self._meeting_invite_status.status = status
        return self

    def build(self) -> "MeetingInviteStatus":
        return self._meeting_invite_status
