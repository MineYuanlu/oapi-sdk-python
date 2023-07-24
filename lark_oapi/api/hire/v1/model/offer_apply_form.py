# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .i18n import I18n


class OfferApplyForm(object):
    _types = {
        "id": str,
        "name": I18n,
        "create_time": str,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.name: Optional[I18n] = None
        self.create_time: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "OfferApplyFormBuilder":
        return OfferApplyFormBuilder()


class OfferApplyFormBuilder(object):
    def __init__(self) -> None:
        self._offer_apply_form = OfferApplyForm()

    def id(self, id: str) -> "OfferApplyFormBuilder":
        self._offer_apply_form.id = id
        return self

    def name(self, name: I18n) -> "OfferApplyFormBuilder":
        self._offer_apply_form.name = name
        return self

    def create_time(self, create_time: str) -> "OfferApplyFormBuilder":
        self._offer_apply_form.create_time = create_time
        return self

    def build(self) -> "OfferApplyForm":
        return self._offer_apply_form
