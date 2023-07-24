# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class Image(object):
    _types = {
        "image_token": str,
    }

    def __init__(self, d=None):
        self.image_token: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ImageBuilder":
        return ImageBuilder()


class ImageBuilder(object):
    def __init__(self) -> None:
        self._image = Image()

    def image_token(self, image_token: str) -> "ImageBuilder":
        self._image.image_token = image_token
        return self

    def build(self) -> "Image":
        return self._image
