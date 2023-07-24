# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class View(object):
    _types = {
        "view_type": int,
    }

    def __init__(self, d=None):
        self.view_type: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ViewBuilder":
        return ViewBuilder()


class ViewBuilder(object):
    def __init__(self) -> None:
        self._view = View()

    def view_type(self, view_type: int) -> "ViewBuilder":
        self._view.view_type = view_type
        return self

    def build(self) -> "View":
        return self._view
