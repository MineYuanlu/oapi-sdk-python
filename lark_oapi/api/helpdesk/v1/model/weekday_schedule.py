# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class WeekdaySchedule(object):
    _types = {
        "start_time": str,
        "end_time": str,
        "weekday": int,
    }

    def __init__(self, d=None):
        self.start_time: Optional[str] = None
        self.end_time: Optional[str] = None
        self.weekday: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "WeekdayScheduleBuilder":
        return WeekdayScheduleBuilder()


class WeekdayScheduleBuilder(object):
    def __init__(self) -> None:
        self._weekday_schedule = WeekdaySchedule()

    def start_time(self, start_time: str) -> "WeekdayScheduleBuilder":
        self._weekday_schedule.start_time = start_time
        return self

    def end_time(self, end_time: str) -> "WeekdayScheduleBuilder":
        self._weekday_schedule.end_time = end_time
        return self

    def weekday(self, weekday: int) -> "WeekdayScheduleBuilder":
        self._weekday_schedule.weekday = weekday
        return self

    def build(self) -> "WeekdaySchedule":
        return self._weekday_schedule
