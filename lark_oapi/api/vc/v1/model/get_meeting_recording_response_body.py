# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .meeting_recording import MeetingRecording


class GetMeetingRecordingResponseBody(object):
    _types = {
        "recording": MeetingRecording,
    }

    def __init__(self, d=None):
        self.recording: Optional[MeetingRecording] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetMeetingRecordingResponseBodyBuilder":
        return GetMeetingRecordingResponseBodyBuilder()


class GetMeetingRecordingResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._get_meeting_recording_response_body = GetMeetingRecordingResponseBody()

    def recording(self, recording: MeetingRecording) -> "GetMeetingRecordingResponseBodyBuilder":
        self._get_meeting_recording_response_body.recording = recording
        return self

    def build(self) -> "GetMeetingRecordingResponseBody":
        return self._get_meeting_recording_response_body
