# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .batch_create_mailgroup_member_request_body import BatchCreateMailgroupMemberRequestBody


class BatchCreateMailgroupMemberRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.department_id_type: Optional[str] = None
        self.mailgroup_id: Optional[str] = None
        self.request_body: Optional[BatchCreateMailgroupMemberRequestBody] = None

    @staticmethod
    def builder() -> "BatchCreateMailgroupMemberRequestBuilder":
        return BatchCreateMailgroupMemberRequestBuilder()


class BatchCreateMailgroupMemberRequestBuilder(object):

    def __init__(self) -> None:
        batch_create_mailgroup_member_request = BatchCreateMailgroupMemberRequest()
        batch_create_mailgroup_member_request.http_method = HttpMethod.POST
        batch_create_mailgroup_member_request.uri = "/open-apis/mail/v1/mailgroups/:mailgroup_id/members/batch_create"
        batch_create_mailgroup_member_request.token_types = {AccessTokenType.TENANT}
        self._batch_create_mailgroup_member_request: BatchCreateMailgroupMemberRequest = batch_create_mailgroup_member_request

    def user_id_type(self, user_id_type: str) -> "BatchCreateMailgroupMemberRequestBuilder":
        self._batch_create_mailgroup_member_request.user_id_type = user_id_type
        self._batch_create_mailgroup_member_request.add_query("user_id_type", user_id_type)
        return self

    def department_id_type(self, department_id_type: str) -> "BatchCreateMailgroupMemberRequestBuilder":
        self._batch_create_mailgroup_member_request.department_id_type = department_id_type
        self._batch_create_mailgroup_member_request.add_query("department_id_type", department_id_type)
        return self

    def mailgroup_id(self, mailgroup_id: str) -> "BatchCreateMailgroupMemberRequestBuilder":
        self._batch_create_mailgroup_member_request.mailgroup_id = mailgroup_id
        self._batch_create_mailgroup_member_request.paths["mailgroup_id"] = str(mailgroup_id)
        return self

    def request_body(self,
                     request_body: BatchCreateMailgroupMemberRequestBody) -> "BatchCreateMailgroupMemberRequestBuilder":
        self._batch_create_mailgroup_member_request.request_body = request_body
        self._batch_create_mailgroup_member_request.body = request_body
        return self

    def build(self) -> BatchCreateMailgroupMemberRequest:
        return self._batch_create_mailgroup_member_request
