# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .i18n import I18n


class CreateLeaveGrantingRecordRequestBody(object):
    _types = {
        "leave_type_id": str,
        "employment_id": str,
        "granting_quantity": str,
        "granting_unit": int,
        "effective_date": str,
        "reason": List[I18n],
        "external_id": str,
    }

    def __init__(self, d=None):
        self.leave_type_id: Optional[str] = None
        self.employment_id: Optional[str] = None
        self.granting_quantity: Optional[str] = None
        self.granting_unit: Optional[int] = None
        self.effective_date: Optional[str] = None
        self.reason: Optional[List[I18n]] = None
        self.external_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateLeaveGrantingRecordRequestBodyBuilder":
        return CreateLeaveGrantingRecordRequestBodyBuilder()


class CreateLeaveGrantingRecordRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._create_leave_granting_record_request_body = CreateLeaveGrantingRecordRequestBody()

    def leave_type_id(self, leave_type_id: str) -> "CreateLeaveGrantingRecordRequestBodyBuilder":
        self._create_leave_granting_record_request_body.leave_type_id = leave_type_id
        return self

    def employment_id(self, employment_id: str) -> "CreateLeaveGrantingRecordRequestBodyBuilder":
        self._create_leave_granting_record_request_body.employment_id = employment_id
        return self

    def granting_quantity(self, granting_quantity: str) -> "CreateLeaveGrantingRecordRequestBodyBuilder":
        self._create_leave_granting_record_request_body.granting_quantity = granting_quantity
        return self

    def granting_unit(self, granting_unit: int) -> "CreateLeaveGrantingRecordRequestBodyBuilder":
        self._create_leave_granting_record_request_body.granting_unit = granting_unit
        return self

    def effective_date(self, effective_date: str) -> "CreateLeaveGrantingRecordRequestBodyBuilder":
        self._create_leave_granting_record_request_body.effective_date = effective_date
        return self

    def reason(self, reason: List[I18n]) -> "CreateLeaveGrantingRecordRequestBodyBuilder":
        self._create_leave_granting_record_request_body.reason = reason
        return self

    def external_id(self, external_id: str) -> "CreateLeaveGrantingRecordRequestBodyBuilder":
        self._create_leave_granting_record_request_body.external_id = external_id
        return self

    def build(self) -> "CreateLeaveGrantingRecordRequestBody":
        return self._create_leave_granting_record_request_body
