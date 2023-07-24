# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class OfferStatusOfferRequestBody(object):
    _types = {
        "offer_status": int,
        "expiration_date": str,
        "termination_reason_id_list": List[str],
        "termination_reason_note": str,
    }

    def __init__(self, d=None):
        self.offer_status: Optional[int] = None
        self.expiration_date: Optional[str] = None
        self.termination_reason_id_list: Optional[List[str]] = None
        self.termination_reason_note: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "OfferStatusOfferRequestBodyBuilder":
        return OfferStatusOfferRequestBodyBuilder()


class OfferStatusOfferRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._offer_status_offer_request_body = OfferStatusOfferRequestBody()

    def offer_status(self, offer_status: int) -> "OfferStatusOfferRequestBodyBuilder":
        self._offer_status_offer_request_body.offer_status = offer_status
        return self

    def expiration_date(self, expiration_date: str) -> "OfferStatusOfferRequestBodyBuilder":
        self._offer_status_offer_request_body.expiration_date = expiration_date
        return self

    def termination_reason_id_list(self, termination_reason_id_list: List[str]) -> "OfferStatusOfferRequestBodyBuilder":
        self._offer_status_offer_request_body.termination_reason_id_list = termination_reason_id_list
        return self

    def termination_reason_note(self, termination_reason_note: str) -> "OfferStatusOfferRequestBodyBuilder":
        self._offer_status_offer_request_body.termination_reason_note = termination_reason_note
        return self

    def build(self) -> "OfferStatusOfferRequestBody":
        return self._offer_status_offer_request_body
