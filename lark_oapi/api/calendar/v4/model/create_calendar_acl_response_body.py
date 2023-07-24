# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .acl_scope import AclScope


class CreateCalendarAclResponseBody(object):
    _types = {
        "acl_id": str,
        "role": str,
        "scope": AclScope,
    }

    def __init__(self, d=None):
        self.acl_id: Optional[str] = None
        self.role: Optional[str] = None
        self.scope: Optional[AclScope] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateCalendarAclResponseBodyBuilder":
        return CreateCalendarAclResponseBodyBuilder()


class CreateCalendarAclResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._create_calendar_acl_response_body = CreateCalendarAclResponseBody()

    def acl_id(self, acl_id: str) -> "CreateCalendarAclResponseBodyBuilder":
        self._create_calendar_acl_response_body.acl_id = acl_id
        return self

    def role(self, role: str) -> "CreateCalendarAclResponseBodyBuilder":
        self._create_calendar_acl_response_body.role = role
        return self

    def scope(self, scope: AclScope) -> "CreateCalendarAclResponseBodyBuilder":
        self._create_calendar_acl_response_body.scope = scope
        return self

    def build(self) -> "CreateCalendarAclResponseBody":
        return self._create_calendar_acl_response_body
