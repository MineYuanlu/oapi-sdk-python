# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .set_permission_meeting_recording_request_body import SetPermissionMeetingRecordingRequestBody


class SetPermissionMeetingRecordingRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.meeting_id: Optional[int] = None
        self.request_body: Optional[SetPermissionMeetingRecordingRequestBody] = None

    @staticmethod
    def builder() -> "SetPermissionMeetingRecordingRequestBuilder":
        return SetPermissionMeetingRecordingRequestBuilder()


class SetPermissionMeetingRecordingRequestBuilder(object):

    def __init__(self) -> None:
        set_permission_meeting_recording_request = SetPermissionMeetingRecordingRequest()
        set_permission_meeting_recording_request.http_method = HttpMethod.PATCH
        set_permission_meeting_recording_request.uri = "/open-apis/vc/v1/meetings/:meeting_id/recording/set_permission"
        set_permission_meeting_recording_request.token_types = {AccessTokenType.USER}
        self._set_permission_meeting_recording_request: SetPermissionMeetingRecordingRequest = set_permission_meeting_recording_request

    def user_id_type(self, user_id_type: str) -> "SetPermissionMeetingRecordingRequestBuilder":
        self._set_permission_meeting_recording_request.user_id_type = user_id_type
        self._set_permission_meeting_recording_request.add_query("user_id_type", user_id_type)
        return self

    def meeting_id(self, meeting_id: int) -> "SetPermissionMeetingRecordingRequestBuilder":
        self._set_permission_meeting_recording_request.meeting_id = meeting_id
        self._set_permission_meeting_recording_request.paths["meeting_id"] = str(meeting_id)
        return self

    def request_body(self,
                     request_body: SetPermissionMeetingRecordingRequestBody) -> "SetPermissionMeetingRecordingRequestBuilder":
        self._set_permission_meeting_recording_request.request_body = request_body
        self._set_permission_meeting_recording_request.body = request_body
        return self

    def build(self) -> SetPermissionMeetingRecordingRequest:
        return self._set_permission_meeting_recording_request
