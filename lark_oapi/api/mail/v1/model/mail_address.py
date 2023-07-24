# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class MailAddress(object):
    _types = {
        "mail_address": str,
        "name": str,
    }

    def __init__(self, d=None):
        self.mail_address: Optional[str] = None
        self.name: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "MailAddressBuilder":
        return MailAddressBuilder()


class MailAddressBuilder(object):
    def __init__(self) -> None:
        self._mail_address = MailAddress()

    def mail_address(self, mail_address: str) -> "MailAddressBuilder":
        self._mail_address.mail_address = mail_address
        return self

    def name(self, name: str) -> "MailAddressBuilder":
        self._mail_address.name = name
        return self

    def build(self) -> "MailAddress":
        return self._mail_address
