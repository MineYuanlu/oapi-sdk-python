# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.delete_file_comment_reply_request import DeleteFileCommentReplyRequest
from ..model.delete_file_comment_reply_response import DeleteFileCommentReplyResponse
from ..model.list_file_comment_reply_request import ListFileCommentReplyRequest
from ..model.list_file_comment_reply_response import ListFileCommentReplyResponse
from ..model.update_file_comment_reply_request import UpdateFileCommentReplyRequest
from ..model.update_file_comment_reply_response import UpdateFileCommentReplyResponse


class FileCommentReply(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def delete(self, request: DeleteFileCommentReplyRequest,
               option: Optional[RequestOption] = None) -> DeleteFileCommentReplyResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: DeleteFileCommentReplyResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                  DeleteFileCommentReplyResponse)
        response.raw = resp

        return response

    def list(self, request: ListFileCommentReplyRequest,
             option: Optional[RequestOption] = None) -> ListFileCommentReplyResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: ListFileCommentReplyResponse = JSON.unmarshal(str(resp.content, UTF_8), ListFileCommentReplyResponse)
        response.raw = resp

        return response

    def update(self, request: UpdateFileCommentReplyRequest,
               option: Optional[RequestOption] = None) -> UpdateFileCommentReplyResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: UpdateFileCommentReplyResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                  UpdateFileCommentReplyResponse)
        response.raw = resp

        return response
