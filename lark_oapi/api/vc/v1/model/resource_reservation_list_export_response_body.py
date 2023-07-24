# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class ResourceReservationListExportResponseBody(object):
    _types = {
        "task_id": str,
    }

    def __init__(self, d=None):
        self.task_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ResourceReservationListExportResponseBodyBuilder":
        return ResourceReservationListExportResponseBodyBuilder()


class ResourceReservationListExportResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._resource_reservation_list_export_response_body = ResourceReservationListExportResponseBody()

    def task_id(self, task_id: str) -> "ResourceReservationListExportResponseBodyBuilder":
        self._resource_reservation_list_export_response_body.task_id = task_id
        return self

    def build(self) -> "ResourceReservationListExportResponseBody":
        return self._resource_reservation_list_export_response_body
