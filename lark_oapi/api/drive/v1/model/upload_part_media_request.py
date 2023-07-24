# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .upload_part_media_request_body import UploadPartMediaRequestBody


class UploadPartMediaRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.request_body: Optional[UploadPartMediaRequestBody] = None

    @staticmethod
    def builder() -> "UploadPartMediaRequestBuilder":
        return UploadPartMediaRequestBuilder()


class UploadPartMediaRequestBuilder(object):

    def __init__(self) -> None:
        upload_part_media_request = UploadPartMediaRequest()
        upload_part_media_request.http_method = HttpMethod.POST
        upload_part_media_request.uri = "/open-apis/drive/v1/medias/upload_part"
        upload_part_media_request.token_types = {AccessTokenType.USER, AccessTokenType.TENANT}
        self._upload_part_media_request: UploadPartMediaRequest = upload_part_media_request

    def request_body(self, request_body: UploadPartMediaRequestBody) -> "UploadPartMediaRequestBuilder":
        self._upload_part_media_request.request_body = request_body
        self._upload_part_media_request.body = request_body
        return self

    def build(self) -> UploadPartMediaRequest:
        return self._upload_part_media_request
