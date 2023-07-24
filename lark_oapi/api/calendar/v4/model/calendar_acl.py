# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .acl_scope import AclScope


class CalendarAcl(object):
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
    def builder() -> "CalendarAclBuilder":
        return CalendarAclBuilder()


class CalendarAclBuilder(object):
    def __init__(self) -> None:
        self._calendar_acl = CalendarAcl()

    def acl_id(self, acl_id: str) -> "CalendarAclBuilder":
        self._calendar_acl.acl_id = acl_id
        return self

    def role(self, role: str) -> "CalendarAclBuilder":
        self._calendar_acl.role = role
        return self

    def scope(self, scope: AclScope) -> "CalendarAclBuilder":
        self._calendar_acl.scope = scope
        return self

    def build(self) -> "CalendarAcl":
        return self._calendar_acl
