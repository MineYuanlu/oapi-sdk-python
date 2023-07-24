# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .attendee_chat_member import AttendeeChatMember
from .calendar_attendee_resource_customization import CalendarAttendeeResourceCustomization


class CalendarEventAttendeeResp(object):
    _types = {
        "type": str,
        "attendee_id": str,
        "rsvp_status": str,
        "is_optional": bool,
        "is_organizer": bool,
        "is_external": bool,
        "display_name": str,
        "chat_members": List[AttendeeChatMember],
        "user_id": str,
        "chat_id": str,
        "room_id": str,
        "third_party_email": str,
        "operate_id": str,
        "resource_customization": List[CalendarAttendeeResourceCustomization],
    }

    def __init__(self, d=None):
        self.type: Optional[str] = None
        self.attendee_id: Optional[str] = None
        self.rsvp_status: Optional[str] = None
        self.is_optional: Optional[bool] = None
        self.is_organizer: Optional[bool] = None
        self.is_external: Optional[bool] = None
        self.display_name: Optional[str] = None
        self.chat_members: Optional[List[AttendeeChatMember]] = None
        self.user_id: Optional[str] = None
        self.chat_id: Optional[str] = None
        self.room_id: Optional[str] = None
        self.third_party_email: Optional[str] = None
        self.operate_id: Optional[str] = None
        self.resource_customization: Optional[List[CalendarAttendeeResourceCustomization]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CalendarEventAttendeeRespBuilder":
        return CalendarEventAttendeeRespBuilder()


class CalendarEventAttendeeRespBuilder(object):
    def __init__(self) -> None:
        self._calendar_event_attendee_resp = CalendarEventAttendeeResp()

    def type(self, type: str) -> "CalendarEventAttendeeRespBuilder":
        self._calendar_event_attendee_resp.type = type
        return self

    def attendee_id(self, attendee_id: str) -> "CalendarEventAttendeeRespBuilder":
        self._calendar_event_attendee_resp.attendee_id = attendee_id
        return self

    def rsvp_status(self, rsvp_status: str) -> "CalendarEventAttendeeRespBuilder":
        self._calendar_event_attendee_resp.rsvp_status = rsvp_status
        return self

    def is_optional(self, is_optional: bool) -> "CalendarEventAttendeeRespBuilder":
        self._calendar_event_attendee_resp.is_optional = is_optional
        return self

    def is_organizer(self, is_organizer: bool) -> "CalendarEventAttendeeRespBuilder":
        self._calendar_event_attendee_resp.is_organizer = is_organizer
        return self

    def is_external(self, is_external: bool) -> "CalendarEventAttendeeRespBuilder":
        self._calendar_event_attendee_resp.is_external = is_external
        return self

    def display_name(self, display_name: str) -> "CalendarEventAttendeeRespBuilder":
        self._calendar_event_attendee_resp.display_name = display_name
        return self

    def chat_members(self, chat_members: List[AttendeeChatMember]) -> "CalendarEventAttendeeRespBuilder":
        self._calendar_event_attendee_resp.chat_members = chat_members
        return self

    def user_id(self, user_id: str) -> "CalendarEventAttendeeRespBuilder":
        self._calendar_event_attendee_resp.user_id = user_id
        return self

    def chat_id(self, chat_id: str) -> "CalendarEventAttendeeRespBuilder":
        self._calendar_event_attendee_resp.chat_id = chat_id
        return self

    def room_id(self, room_id: str) -> "CalendarEventAttendeeRespBuilder":
        self._calendar_event_attendee_resp.room_id = room_id
        return self

    def third_party_email(self, third_party_email: str) -> "CalendarEventAttendeeRespBuilder":
        self._calendar_event_attendee_resp.third_party_email = third_party_email
        return self

    def operate_id(self, operate_id: str) -> "CalendarEventAttendeeRespBuilder":
        self._calendar_event_attendee_resp.operate_id = operate_id
        return self

    def resource_customization(self, resource_customization: List[
        CalendarAttendeeResourceCustomization]) -> "CalendarEventAttendeeRespBuilder":
        self._calendar_event_attendee_resp.resource_customization = resource_customization
        return self

    def build(self) -> "CalendarEventAttendeeResp":
        return self._calendar_event_attendee_resp
