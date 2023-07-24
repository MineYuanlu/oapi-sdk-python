# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.create_user_mailbox_alias_request import CreateUserMailboxAliasRequest
from ..model.create_user_mailbox_alias_response import CreateUserMailboxAliasResponse
from ..model.delete_user_mailbox_alias_request import DeleteUserMailboxAliasRequest
from ..model.delete_user_mailbox_alias_response import DeleteUserMailboxAliasResponse
from ..model.list_user_mailbox_alias_request import ListUserMailboxAliasRequest
from ..model.list_user_mailbox_alias_response import ListUserMailboxAliasResponse


class UserMailboxAlias(object):
    def __init__(self, config: Config) -> None:
        self.config: Optional[Config] = config

    def create(self, request: CreateUserMailboxAliasRequest,
               option: Optional[RequestOption] = None) -> CreateUserMailboxAliasResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: CreateUserMailboxAliasResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                  CreateUserMailboxAliasResponse)
        response.raw = resp

        return response

    def delete(self, request: DeleteUserMailboxAliasRequest,
               option: Optional[RequestOption] = None) -> DeleteUserMailboxAliasResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: DeleteUserMailboxAliasResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                  DeleteUserMailboxAliasResponse)
        response.raw = resp

        return response

    def list(self, request: ListUserMailboxAliasRequest,
             option: Optional[RequestOption] = None) -> ListUserMailboxAliasResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: ListUserMailboxAliasResponse = JSON.unmarshal(str(resp.content, UTF_8), ListUserMailboxAliasResponse)
        response.raw = resp

        return response
