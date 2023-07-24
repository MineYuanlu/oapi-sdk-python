# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .trip_group_schedule import TripGroupSchedule
from .user import User


class TripGroup(object):
    _types = {
        "type": str,
        "instance_code": str,
        "start_user": User,
        "start_time": str,
        "end_time": str,
        "trip_interval": str,
        "trip_reason": str,
        "schedules": List[TripGroupSchedule],
        "trip_peers": List[User],
    }

    def __init__(self, d=None):
        self.type: Optional[str] = None
        self.instance_code: Optional[str] = None
        self.start_user: Optional[User] = None
        self.start_time: Optional[str] = None
        self.end_time: Optional[str] = None
        self.trip_interval: Optional[str] = None
        self.trip_reason: Optional[str] = None
        self.schedules: Optional[List[TripGroupSchedule]] = None
        self.trip_peers: Optional[List[User]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TripGroupBuilder":
        return TripGroupBuilder()


class TripGroupBuilder(object):
    def __init__(self) -> None:
        self._trip_group = TripGroup()

    def type(self, type: str) -> "TripGroupBuilder":
        self._trip_group.type = type
        return self

    def instance_code(self, instance_code: str) -> "TripGroupBuilder":
        self._trip_group.instance_code = instance_code
        return self

    def start_user(self, start_user: User) -> "TripGroupBuilder":
        self._trip_group.start_user = start_user
        return self

    def start_time(self, start_time: str) -> "TripGroupBuilder":
        self._trip_group.start_time = start_time
        return self

    def end_time(self, end_time: str) -> "TripGroupBuilder":
        self._trip_group.end_time = end_time
        return self

    def trip_interval(self, trip_interval: str) -> "TripGroupBuilder":
        self._trip_group.trip_interval = trip_interval
        return self

    def trip_reason(self, trip_reason: str) -> "TripGroupBuilder":
        self._trip_group.trip_reason = trip_reason
        return self

    def schedules(self, schedules: List[TripGroupSchedule]) -> "TripGroupBuilder":
        self._trip_group.schedules = schedules
        return self

    def trip_peers(self, trip_peers: List[User]) -> "TripGroupBuilder":
        self._trip_group.trip_peers = trip_peers
        return self

    def build(self) -> "TripGroup":
        return self._trip_group
