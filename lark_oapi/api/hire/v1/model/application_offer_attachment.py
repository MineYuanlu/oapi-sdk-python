# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class ApplicationOfferAttachment(object):
    _types = {
        "attachment_id": str,
        "name": str,
    }

    def __init__(self, d=None):
        self.attachment_id: Optional[str] = None
        self.name: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ApplicationOfferAttachmentBuilder":
        return ApplicationOfferAttachmentBuilder()


class ApplicationOfferAttachmentBuilder(object):
    def __init__(self) -> None:
        self._application_offer_attachment = ApplicationOfferAttachment()

    def attachment_id(self, attachment_id: str) -> "ApplicationOfferAttachmentBuilder":
        self._application_offer_attachment.attachment_id = attachment_id
        return self

    def name(self, name: str) -> "ApplicationOfferAttachmentBuilder":
        self._application_offer_attachment.name = name
        return self

    def build(self) -> "ApplicationOfferAttachment":
        return self._application_offer_attachment
