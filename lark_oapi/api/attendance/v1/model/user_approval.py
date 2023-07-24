# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .user_leave import UserLeave
from .user_out import UserOut
from .user_overtime_work import UserOvertimeWork
from .user_trip import UserTrip


class UserApproval(object):
    _types = {
        "user_id": str,
        "date": str,
        "outs": List[UserOut],
        "leaves": List[UserLeave],
        "overtime_works": List[UserOvertimeWork],
        "trips": List[UserTrip],
        "time_zone": str,
    }

    def __init__(self, d=None):
        self.user_id: Optional[str] = None
        self.date: Optional[str] = None
        self.outs: Optional[List[UserOut]] = None
        self.leaves: Optional[List[UserLeave]] = None
        self.overtime_works: Optional[List[UserOvertimeWork]] = None
        self.trips: Optional[List[UserTrip]] = None
        self.time_zone: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UserApprovalBuilder":
        return UserApprovalBuilder()


class UserApprovalBuilder(object):
    def __init__(self) -> None:
        self._user_approval = UserApproval()

    def user_id(self, user_id: str) -> "UserApprovalBuilder":
        self._user_approval.user_id = user_id
        return self

    def date(self, date: str) -> "UserApprovalBuilder":
        self._user_approval.date = date
        return self

    def outs(self, outs: List[UserOut]) -> "UserApprovalBuilder":
        self._user_approval.outs = outs
        return self

    def leaves(self, leaves: List[UserLeave]) -> "UserApprovalBuilder":
        self._user_approval.leaves = leaves
        return self

    def overtime_works(self, overtime_works: List[UserOvertimeWork]) -> "UserApprovalBuilder":
        self._user_approval.overtime_works = overtime_works
        return self

    def trips(self, trips: List[UserTrip]) -> "UserApprovalBuilder":
        self._user_approval.trips = trips
        return self

    def time_zone(self, time_zone: str) -> "UserApprovalBuilder":
        self._user_approval.time_zone = time_zone
        return self

    def build(self) -> "UserApproval":
        return self._user_approval
