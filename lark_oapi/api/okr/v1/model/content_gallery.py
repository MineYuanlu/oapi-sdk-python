# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .content_image_item import ContentImageItem


class ContentGallery(object):
    _types = {
        "image_list": List[ContentImageItem],
    }

    def __init__(self, d=None):
        self.image_list: Optional[List[ContentImageItem]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ContentGalleryBuilder":
        return ContentGalleryBuilder()


class ContentGalleryBuilder(object):
    def __init__(self) -> None:
        self._content_gallery = ContentGallery()

    def image_list(self, image_list: List[ContentImageItem]) -> "ContentGalleryBuilder":
        self._content_gallery.image_list = image_list
        return self

    def build(self) -> "ContentGallery":
        return self._content_gallery
