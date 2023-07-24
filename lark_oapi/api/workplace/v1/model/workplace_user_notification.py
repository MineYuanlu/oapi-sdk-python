# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class WorkplaceUserNotification(object):
    _types = {
        "notification_id": str,
        "content": str,
        "expire_time": int,
    }

    def __init__(self, d=None):
        self.notification_id: Optional[str] = None
        self.content: Optional[str] = None
        self.expire_time: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "WorkplaceUserNotificationBuilder":
        return WorkplaceUserNotificationBuilder()


class WorkplaceUserNotificationBuilder(object):
    def __init__(self) -> None:
        self._workplace_user_notification = WorkplaceUserNotification()

    def notification_id(self, notification_id: str) -> "WorkplaceUserNotificationBuilder":
        self._workplace_user_notification.notification_id = notification_id
        return self

    def content(self, content: str) -> "WorkplaceUserNotificationBuilder":
        self._workplace_user_notification.content = content
        return self

    def expire_time(self, expire_time: int) -> "WorkplaceUserNotificationBuilder":
        self._workplace_user_notification.expire_time = expire_time
        return self

    def build(self) -> "WorkplaceUserNotification":
        return self._workplace_user_notification
