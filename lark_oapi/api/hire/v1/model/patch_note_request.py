# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .patch_note_request_body import PatchNoteRequestBody


class PatchNoteRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.note_id: Optional[str] = None
        self.request_body: Optional[PatchNoteRequestBody] = None

    @staticmethod
    def builder() -> "PatchNoteRequestBuilder":
        return PatchNoteRequestBuilder()


class PatchNoteRequestBuilder(object):

    def __init__(self) -> None:
        patch_note_request = PatchNoteRequest()
        patch_note_request.http_method = HttpMethod.PATCH
        patch_note_request.uri = "/open-apis/hire/v1/notes/:note_id"
        patch_note_request.token_types = {AccessTokenType.TENANT}
        self._patch_note_request: PatchNoteRequest = patch_note_request

    def user_id_type(self, user_id_type: str) -> "PatchNoteRequestBuilder":
        self._patch_note_request.user_id_type = user_id_type
        self._patch_note_request.add_query("user_id_type", user_id_type)
        return self

    def note_id(self, note_id: str) -> "PatchNoteRequestBuilder":
        self._patch_note_request.note_id = note_id
        self._patch_note_request.paths["note_id"] = str(note_id)
        return self

    def request_body(self, request_body: PatchNoteRequestBody) -> "PatchNoteRequestBuilder":
        self._patch_note_request.request_body = request_body
        self._patch_note_request.body = request_body
        return self

    def build(self) -> PatchNoteRequest:
        return self._patch_note_request
