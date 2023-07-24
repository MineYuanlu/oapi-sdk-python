# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .application_app_contacts_range import ApplicationAppContactsRange


class ContactsRangeSuggestApplicationAppVersionResponseBody(object):
    _types = {
        "contacts_range": ApplicationAppContactsRange,
    }

    def __init__(self, d=None):
        self.contacts_range: Optional[ApplicationAppContactsRange] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ContactsRangeSuggestApplicationAppVersionResponseBodyBuilder":
        return ContactsRangeSuggestApplicationAppVersionResponseBodyBuilder()


class ContactsRangeSuggestApplicationAppVersionResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._contacts_range_suggest_application_app_version_response_body = ContactsRangeSuggestApplicationAppVersionResponseBody()

    def contacts_range(self,
                       contacts_range: ApplicationAppContactsRange) -> "ContactsRangeSuggestApplicationAppVersionResponseBodyBuilder":
        self._contacts_range_suggest_application_app_version_response_body.contacts_range = contacts_range
        return self

    def build(self) -> "ContactsRangeSuggestApplicationAppVersionResponseBody":
        return self._contacts_range_suggest_application_app_version_response_body
