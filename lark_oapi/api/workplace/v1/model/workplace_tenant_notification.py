# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .rule import Rule


class WorkplaceTenantNotification(object):
    _types = {
        "notification_id": str,
        "content": str,
        "expire_time": int,
        "rule": Rule,
    }

    def __init__(self, d=None):
        self.notification_id: Optional[str] = None
        self.content: Optional[str] = None
        self.expire_time: Optional[int] = None
        self.rule: Optional[Rule] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "WorkplaceTenantNotificationBuilder":
        return WorkplaceTenantNotificationBuilder()


class WorkplaceTenantNotificationBuilder(object):
    def __init__(self) -> None:
        self._workplace_tenant_notification = WorkplaceTenantNotification()

    def notification_id(self, notification_id: str) -> "WorkplaceTenantNotificationBuilder":
        self._workplace_tenant_notification.notification_id = notification_id
        return self

    def content(self, content: str) -> "WorkplaceTenantNotificationBuilder":
        self._workplace_tenant_notification.content = content
        return self

    def expire_time(self, expire_time: int) -> "WorkplaceTenantNotificationBuilder":
        self._workplace_tenant_notification.expire_time = expire_time
        return self

    def rule(self, rule: Rule) -> "WorkplaceTenantNotificationBuilder":
        self._workplace_tenant_notification.rule = rule
        return self

    def build(self) -> "WorkplaceTenantNotification":
        return self._workplace_tenant_notification
