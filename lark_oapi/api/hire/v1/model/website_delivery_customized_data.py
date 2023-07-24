# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class WebsiteDeliveryCustomizedData(object):
    _types = {
        "object_id": str,
        "value": str,
    }

    def __init__(self, d=None):
        self.object_id: Optional[str] = None
        self.value: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "WebsiteDeliveryCustomizedDataBuilder":
        return WebsiteDeliveryCustomizedDataBuilder()


class WebsiteDeliveryCustomizedDataBuilder(object):
    def __init__(self) -> None:
        self._website_delivery_customized_data = WebsiteDeliveryCustomizedData()

    def object_id(self, object_id: str) -> "WebsiteDeliveryCustomizedDataBuilder":
        self._website_delivery_customized_data.object_id = object_id
        return self

    def value(self, value: str) -> "WebsiteDeliveryCustomizedDataBuilder":
        self._website_delivery_customized_data.value = value
        return self

    def build(self) -> "WebsiteDeliveryCustomizedData":
        return self._website_delivery_customized_data
