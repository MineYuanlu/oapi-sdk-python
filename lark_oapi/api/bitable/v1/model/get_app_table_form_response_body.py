# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .app_table_form import AppTableForm


class GetAppTableFormResponseBody(object):
    _types = {
        "form": AppTableForm,
    }

    def __init__(self, d=None):
        self.form: Optional[AppTableForm] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetAppTableFormResponseBodyBuilder":
        return GetAppTableFormResponseBodyBuilder()


class GetAppTableFormResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._get_app_table_form_response_body = GetAppTableFormResponseBody()

    def form(self, form: AppTableForm) -> "GetAppTableFormResponseBodyBuilder":
        self._get_app_table_form_response_body.form = form
        return self

    def build(self) -> "GetAppTableFormResponseBody":
        return self._get_app_table_form_response_body
