# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .i18n import I18n


class TransferReason(object):
    _types = {
        "transfer_reason_unique_identifier": str,
        "name": List[I18n],
        "active": bool,
        "parent_transfer_reason_unique_identifier": str,
        "created_time": str,
        "updated_time": str,
    }

    def __init__(self, d=None):
        self.transfer_reason_unique_identifier: Optional[str] = None
        self.name: Optional[List[I18n]] = None
        self.active: Optional[bool] = None
        self.parent_transfer_reason_unique_identifier: Optional[str] = None
        self.created_time: Optional[str] = None
        self.updated_time: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TransferReasonBuilder":
        return TransferReasonBuilder()


class TransferReasonBuilder(object):
    def __init__(self) -> None:
        self._transfer_reason = TransferReason()

    def transfer_reason_unique_identifier(self, transfer_reason_unique_identifier: str) -> "TransferReasonBuilder":
        self._transfer_reason.transfer_reason_unique_identifier = transfer_reason_unique_identifier
        return self

    def name(self, name: List[I18n]) -> "TransferReasonBuilder":
        self._transfer_reason.name = name
        return self

    def active(self, active: bool) -> "TransferReasonBuilder":
        self._transfer_reason.active = active
        return self

    def parent_transfer_reason_unique_identifier(self,
                                                 parent_transfer_reason_unique_identifier: str) -> "TransferReasonBuilder":
        self._transfer_reason.parent_transfer_reason_unique_identifier = parent_transfer_reason_unique_identifier
        return self

    def created_time(self, created_time: str) -> "TransferReasonBuilder":
        self._transfer_reason.created_time = created_time
        return self

    def updated_time(self, updated_time: str) -> "TransferReasonBuilder":
        self._transfer_reason.updated_time = updated_time
        return self

    def build(self) -> "TransferReason":
        return self._transfer_reason
