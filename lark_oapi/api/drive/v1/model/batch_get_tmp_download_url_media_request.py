# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class BatchGetTmpDownloadUrlMediaRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.file_tokens: Optional[List[str]] = None
        self.extra: Optional[str] = None

    @staticmethod
    def builder() -> "BatchGetTmpDownloadUrlMediaRequestBuilder":
        return BatchGetTmpDownloadUrlMediaRequestBuilder()


class BatchGetTmpDownloadUrlMediaRequestBuilder(object):

    def __init__(self) -> None:
        batch_get_tmp_download_url_media_request = BatchGetTmpDownloadUrlMediaRequest()
        batch_get_tmp_download_url_media_request.http_method = HttpMethod.GET
        batch_get_tmp_download_url_media_request.uri = "/open-apis/drive/v1/medias/batch_get_tmp_download_url"
        batch_get_tmp_download_url_media_request.token_types = {AccessTokenType.USER, AccessTokenType.TENANT}
        self._batch_get_tmp_download_url_media_request: BatchGetTmpDownloadUrlMediaRequest = batch_get_tmp_download_url_media_request

    def file_tokens(self, file_tokens: List[str]) -> "BatchGetTmpDownloadUrlMediaRequestBuilder":
        self._batch_get_tmp_download_url_media_request.file_tokens = file_tokens
        self._batch_get_tmp_download_url_media_request.add_query("file_tokens", file_tokens)
        return self

    def extra(self, extra: str) -> "BatchGetTmpDownloadUrlMediaRequestBuilder":
        self._batch_get_tmp_download_url_media_request.extra = extra
        self._batch_get_tmp_download_url_media_request.add_query("extra", extra)
        return self

    def build(self) -> BatchGetTmpDownloadUrlMediaRequest:
        return self._batch_get_tmp_download_url_media_request
