# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.batch_create_mailgroup_member_request import BatchCreateMailgroupMemberRequest
from ..model.batch_create_mailgroup_member_response import BatchCreateMailgroupMemberResponse
from ..model.batch_delete_mailgroup_member_request import BatchDeleteMailgroupMemberRequest
from ..model.batch_delete_mailgroup_member_response import BatchDeleteMailgroupMemberResponse
from ..model.create_mailgroup_member_request import CreateMailgroupMemberRequest
from ..model.create_mailgroup_member_response import CreateMailgroupMemberResponse
from ..model.delete_mailgroup_member_request import DeleteMailgroupMemberRequest
from ..model.delete_mailgroup_member_response import DeleteMailgroupMemberResponse
from ..model.get_mailgroup_member_request import GetMailgroupMemberRequest
from ..model.get_mailgroup_member_response import GetMailgroupMemberResponse
from ..model.list_mailgroup_member_request import ListMailgroupMemberRequest
from ..model.list_mailgroup_member_response import ListMailgroupMemberResponse


class MailgroupMember(object):
    def __init__(self, config: Config) -> None:
        self.config: Optional[Config] = config

    def batch_create(self, request: BatchCreateMailgroupMemberRequest,
                     option: Optional[RequestOption] = None) -> BatchCreateMailgroupMemberResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: BatchCreateMailgroupMemberResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                      BatchCreateMailgroupMemberResponse)
        response.raw = resp

        return response

    def batch_delete(self, request: BatchDeleteMailgroupMemberRequest,
                     option: Optional[RequestOption] = None) -> BatchDeleteMailgroupMemberResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: BatchDeleteMailgroupMemberResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                      BatchDeleteMailgroupMemberResponse)
        response.raw = resp

        return response

    def create(self, request: CreateMailgroupMemberRequest,
               option: Optional[RequestOption] = None) -> CreateMailgroupMemberResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: CreateMailgroupMemberResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                 CreateMailgroupMemberResponse)
        response.raw = resp

        return response

    def delete(self, request: DeleteMailgroupMemberRequest,
               option: Optional[RequestOption] = None) -> DeleteMailgroupMemberResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: DeleteMailgroupMemberResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                 DeleteMailgroupMemberResponse)
        response.raw = resp

        return response

    def get(self, request: GetMailgroupMemberRequest,
            option: Optional[RequestOption] = None) -> GetMailgroupMemberResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: GetMailgroupMemberResponse = JSON.unmarshal(str(resp.content, UTF_8), GetMailgroupMemberResponse)
        response.raw = resp

        return response

    def list(self, request: ListMailgroupMemberRequest,
             option: Optional[RequestOption] = None) -> ListMailgroupMemberResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: ListMailgroupMemberResponse = JSON.unmarshal(str(resp.content, UTF_8), ListMailgroupMemberResponse)
        response.raw = resp

        return response
