# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .bottom_border_style import BottomBorderStyle
from .left_border_style import LeftBorderStyle
from .right_border_style import RightBorderStyle
from .top_border_style import TopBorderStyle


class BorderStyle(object):
    _types = {
        "top": TopBorderStyle,
        "left": LeftBorderStyle,
        "right": RightBorderStyle,
        "bottom": BottomBorderStyle,
    }

    def __init__(self, d=None):
        self.top: Optional[TopBorderStyle] = None
        self.left: Optional[LeftBorderStyle] = None
        self.right: Optional[RightBorderStyle] = None
        self.bottom: Optional[BottomBorderStyle] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BorderStyleBuilder":
        return BorderStyleBuilder()


class BorderStyleBuilder(object):
    def __init__(self) -> None:
        self._border_style = BorderStyle()

    def top(self, top: TopBorderStyle) -> "BorderStyleBuilder":
        self._border_style.top = top
        return self

    def left(self, left: LeftBorderStyle) -> "BorderStyleBuilder":
        self._border_style.left = left
        return self

    def right(self, right: RightBorderStyle) -> "BorderStyleBuilder":
        self._border_style.right = right
        return self

    def bottom(self, bottom: BottomBorderStyle) -> "BorderStyleBuilder":
        self._border_style.bottom = bottom
        return self

    def build(self) -> "BorderStyle":
        return self._border_style
