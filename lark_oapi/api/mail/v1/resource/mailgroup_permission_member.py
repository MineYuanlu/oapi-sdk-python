# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.batch_create_mailgroup_permission_member_request import BatchCreateMailgroupPermissionMemberRequest
from ..model.batch_create_mailgroup_permission_member_response import BatchCreateMailgroupPermissionMemberResponse
from ..model.batch_delete_mailgroup_permission_member_request import BatchDeleteMailgroupPermissionMemberRequest
from ..model.batch_delete_mailgroup_permission_member_response import BatchDeleteMailgroupPermissionMemberResponse
from ..model.create_mailgroup_permission_member_request import CreateMailgroupPermissionMemberRequest
from ..model.create_mailgroup_permission_member_response import CreateMailgroupPermissionMemberResponse
from ..model.delete_mailgroup_permission_member_request import DeleteMailgroupPermissionMemberRequest
from ..model.delete_mailgroup_permission_member_response import DeleteMailgroupPermissionMemberResponse
from ..model.get_mailgroup_permission_member_request import GetMailgroupPermissionMemberRequest
from ..model.get_mailgroup_permission_member_response import GetMailgroupPermissionMemberResponse
from ..model.list_mailgroup_permission_member_request import ListMailgroupPermissionMemberRequest
from ..model.list_mailgroup_permission_member_response import ListMailgroupPermissionMemberResponse


class MailgroupPermissionMember(object):
    def __init__(self, config: Config) -> None:
        self.config: Optional[Config] = config

    def batch_create(self, request: BatchCreateMailgroupPermissionMemberRequest,
                     option: Optional[RequestOption] = None) -> BatchCreateMailgroupPermissionMemberResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: BatchCreateMailgroupPermissionMemberResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                                BatchCreateMailgroupPermissionMemberResponse)
        response.raw = resp

        return response

    def batch_delete(self, request: BatchDeleteMailgroupPermissionMemberRequest,
                     option: Optional[RequestOption] = None) -> BatchDeleteMailgroupPermissionMemberResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: BatchDeleteMailgroupPermissionMemberResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                                BatchDeleteMailgroupPermissionMemberResponse)
        response.raw = resp

        return response

    def create(self, request: CreateMailgroupPermissionMemberRequest,
               option: Optional[RequestOption] = None) -> CreateMailgroupPermissionMemberResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: CreateMailgroupPermissionMemberResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                           CreateMailgroupPermissionMemberResponse)
        response.raw = resp

        return response

    def delete(self, request: DeleteMailgroupPermissionMemberRequest,
               option: Optional[RequestOption] = None) -> DeleteMailgroupPermissionMemberResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: DeleteMailgroupPermissionMemberResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                           DeleteMailgroupPermissionMemberResponse)
        response.raw = resp

        return response

    def get(self, request: GetMailgroupPermissionMemberRequest,
            option: Optional[RequestOption] = None) -> GetMailgroupPermissionMemberResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: GetMailgroupPermissionMemberResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                        GetMailgroupPermissionMemberResponse)
        response.raw = resp

        return response

    def list(self, request: ListMailgroupPermissionMemberRequest,
             option: Optional[RequestOption] = None) -> ListMailgroupPermissionMemberResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: ListMailgroupPermissionMemberResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                         ListMailgroupPermissionMemberResponse)
        response.raw = resp

        return response
