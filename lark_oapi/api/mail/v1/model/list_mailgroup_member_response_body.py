# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .mailgroup_member import MailgroupMember


class ListMailgroupMemberResponseBody(object):
    _types = {
        "has_more": bool,
        "page_token": str,
        "items": List[MailgroupMember],
    }

    def __init__(self, d=None):
        self.has_more: Optional[bool] = None
        self.page_token: Optional[str] = None
        self.items: Optional[List[MailgroupMember]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListMailgroupMemberResponseBodyBuilder":
        return ListMailgroupMemberResponseBodyBuilder()


class ListMailgroupMemberResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._list_mailgroup_member_response_body = ListMailgroupMemberResponseBody()

    def has_more(self, has_more: bool) -> "ListMailgroupMemberResponseBodyBuilder":
        self._list_mailgroup_member_response_body.has_more = has_more
        return self

    def page_token(self, page_token: str) -> "ListMailgroupMemberResponseBodyBuilder":
        self._list_mailgroup_member_response_body.page_token = page_token
        return self

    def items(self, items: List[MailgroupMember]) -> "ListMailgroupMemberResponseBodyBuilder":
        self._list_mailgroup_member_response_body.items = items
        return self

    def build(self) -> "ListMailgroupMemberResponseBody":
        return self._list_mailgroup_member_response_body
