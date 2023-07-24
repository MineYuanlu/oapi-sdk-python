# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class MeetingListExportRequestBody(object):
    _types = {
        "start_time": int,
        "end_time": int,
        "meeting_no": str,
        "user_id": str,
        "room_id": str,
    }

    def __init__(self, d=None):
        self.start_time: Optional[int] = None
        self.end_time: Optional[int] = None
        self.meeting_no: Optional[str] = None
        self.user_id: Optional[str] = None
        self.room_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "MeetingListExportRequestBodyBuilder":
        return MeetingListExportRequestBodyBuilder()


class MeetingListExportRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._meeting_list_export_request_body = MeetingListExportRequestBody()

    def start_time(self, start_time: int) -> "MeetingListExportRequestBodyBuilder":
        self._meeting_list_export_request_body.start_time = start_time
        return self

    def end_time(self, end_time: int) -> "MeetingListExportRequestBodyBuilder":
        self._meeting_list_export_request_body.end_time = end_time
        return self

    def meeting_no(self, meeting_no: str) -> "MeetingListExportRequestBodyBuilder":
        self._meeting_list_export_request_body.meeting_no = meeting_no
        return self

    def user_id(self, user_id: str) -> "MeetingListExportRequestBodyBuilder":
        self._meeting_list_export_request_body.user_id = user_id
        return self

    def room_id(self, room_id: str) -> "MeetingListExportRequestBodyBuilder":
        self._meeting_list_export_request_body.room_id = room_id
        return self

    def build(self) -> "MeetingListExportRequestBody":
        return self._meeting_list_export_request_body
