# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class GetUserFaceRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.is_cropped: Optional[bool] = None
        self.user_id_type: Optional[str] = None
        self.user_id: Optional[str] = None

    @staticmethod
    def builder() -> "GetUserFaceRequestBuilder":
        return GetUserFaceRequestBuilder()


class GetUserFaceRequestBuilder(object):

    def __init__(self) -> None:
        get_user_face_request = GetUserFaceRequest()
        get_user_face_request.http_method = HttpMethod.GET
        get_user_face_request.uri = "/open-apis/acs/v1/users/:user_id/face"
        get_user_face_request.token_types = {AccessTokenType.TENANT}
        self._get_user_face_request: GetUserFaceRequest = get_user_face_request

    def is_cropped(self, is_cropped: bool) -> "GetUserFaceRequestBuilder":
        self._get_user_face_request.is_cropped = is_cropped
        self._get_user_face_request.add_query("is_cropped", is_cropped)
        return self

    def user_id_type(self, user_id_type: str) -> "GetUserFaceRequestBuilder":
        self._get_user_face_request.user_id_type = user_id_type
        self._get_user_face_request.add_query("user_id_type", user_id_type)
        return self

    def user_id(self, user_id: str) -> "GetUserFaceRequestBuilder":
        self._get_user_face_request.user_id = user_id
        self._get_user_face_request.paths["user_id"] = str(user_id)
        return self

    def build(self) -> GetUserFaceRequest:
        return self._get_user_face_request
