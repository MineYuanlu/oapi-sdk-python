# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class GetMailgroupMemberResponseBody(object):
    _types = {
        "member_id": str,
        "email": str,
        "user_id": str,
        "department_id": str,
        "type": str,
    }

    def __init__(self, d=None):
        self.member_id: Optional[str] = None
        self.email: Optional[str] = None
        self.user_id: Optional[str] = None
        self.department_id: Optional[str] = None
        self.type: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetMailgroupMemberResponseBodyBuilder":
        return GetMailgroupMemberResponseBodyBuilder()


class GetMailgroupMemberResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._get_mailgroup_member_response_body = GetMailgroupMemberResponseBody()

    def member_id(self, member_id: str) -> "GetMailgroupMemberResponseBodyBuilder":
        self._get_mailgroup_member_response_body.member_id = member_id
        return self

    def email(self, email: str) -> "GetMailgroupMemberResponseBodyBuilder":
        self._get_mailgroup_member_response_body.email = email
        return self

    def user_id(self, user_id: str) -> "GetMailgroupMemberResponseBodyBuilder":
        self._get_mailgroup_member_response_body.user_id = user_id
        return self

    def department_id(self, department_id: str) -> "GetMailgroupMemberResponseBodyBuilder":
        self._get_mailgroup_member_response_body.department_id = department_id
        return self

    def type(self, type: str) -> "GetMailgroupMemberResponseBodyBuilder":
        self._get_mailgroup_member_response_body.type = type
        return self

    def build(self) -> "GetMailgroupMemberResponseBody":
        return self._get_mailgroup_member_response_body
