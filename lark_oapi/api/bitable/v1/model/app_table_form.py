# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class AppTableForm(object):
    _types = {
        "name": str,
        "description": str,
        "shared": bool,
        "shared_url": str,
        "shared_limit": str,
        "submit_limit_once": bool,
    }

    def __init__(self, d=None):
        self.name: Optional[str] = None
        self.description: Optional[str] = None
        self.shared: Optional[bool] = None
        self.shared_url: Optional[str] = None
        self.shared_limit: Optional[str] = None
        self.submit_limit_once: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AppTableFormBuilder":
        return AppTableFormBuilder()


class AppTableFormBuilder(object):
    def __init__(self) -> None:
        self._app_table_form = AppTableForm()

    def name(self, name: str) -> "AppTableFormBuilder":
        self._app_table_form.name = name
        return self

    def description(self, description: str) -> "AppTableFormBuilder":
        self._app_table_form.description = description
        return self

    def shared(self, shared: bool) -> "AppTableFormBuilder":
        self._app_table_form.shared = shared
        return self

    def shared_url(self, shared_url: str) -> "AppTableFormBuilder":
        self._app_table_form.shared_url = shared_url
        return self

    def shared_limit(self, shared_limit: str) -> "AppTableFormBuilder":
        self._app_table_form.shared_limit = shared_limit
        return self

    def submit_limit_once(self, submit_limit_once: bool) -> "AppTableFormBuilder":
        self._app_table_form.submit_limit_once = submit_limit_once
        return self

    def build(self) -> "AppTableForm":
        return self._app_table_form
