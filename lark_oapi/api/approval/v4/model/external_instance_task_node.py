# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .action_config import ActionConfig
from .external_instance_link import ExternalInstanceLink


class ExternalInstanceTaskNode(object):
    _types = {
        "task_id": str,
        "user_id": str,
        "open_id": str,
        "title": str,
        "links": ExternalInstanceLink,
        "status": str,
        "extra": str,
        "create_time": int,
        "end_time": int,
        "update_time": int,
        "action_context": str,
        "action_configs": List[ActionConfig],
        "display_method": str,
        "exclude_statistics": bool,
        "node_id": str,
        "node_name": str,
    }

    def __init__(self, d=None):
        self.task_id: Optional[str] = None
        self.user_id: Optional[str] = None
        self.open_id: Optional[str] = None
        self.title: Optional[str] = None
        self.links: Optional[ExternalInstanceLink] = None
        self.status: Optional[str] = None
        self.extra: Optional[str] = None
        self.create_time: Optional[int] = None
        self.end_time: Optional[int] = None
        self.update_time: Optional[int] = None
        self.action_context: Optional[str] = None
        self.action_configs: Optional[List[ActionConfig]] = None
        self.display_method: Optional[str] = None
        self.exclude_statistics: Optional[bool] = None
        self.node_id: Optional[str] = None
        self.node_name: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ExternalInstanceTaskNodeBuilder":
        return ExternalInstanceTaskNodeBuilder()


class ExternalInstanceTaskNodeBuilder(object):
    def __init__(self) -> None:
        self._external_instance_task_node = ExternalInstanceTaskNode()

    def task_id(self, task_id: str) -> "ExternalInstanceTaskNodeBuilder":
        self._external_instance_task_node.task_id = task_id
        return self

    def user_id(self, user_id: str) -> "ExternalInstanceTaskNodeBuilder":
        self._external_instance_task_node.user_id = user_id
        return self

    def open_id(self, open_id: str) -> "ExternalInstanceTaskNodeBuilder":
        self._external_instance_task_node.open_id = open_id
        return self

    def title(self, title: str) -> "ExternalInstanceTaskNodeBuilder":
        self._external_instance_task_node.title = title
        return self

    def links(self, links: ExternalInstanceLink) -> "ExternalInstanceTaskNodeBuilder":
        self._external_instance_task_node.links = links
        return self

    def status(self, status: str) -> "ExternalInstanceTaskNodeBuilder":
        self._external_instance_task_node.status = status
        return self

    def extra(self, extra: str) -> "ExternalInstanceTaskNodeBuilder":
        self._external_instance_task_node.extra = extra
        return self

    def create_time(self, create_time: int) -> "ExternalInstanceTaskNodeBuilder":
        self._external_instance_task_node.create_time = create_time
        return self

    def end_time(self, end_time: int) -> "ExternalInstanceTaskNodeBuilder":
        self._external_instance_task_node.end_time = end_time
        return self

    def update_time(self, update_time: int) -> "ExternalInstanceTaskNodeBuilder":
        self._external_instance_task_node.update_time = update_time
        return self

    def action_context(self, action_context: str) -> "ExternalInstanceTaskNodeBuilder":
        self._external_instance_task_node.action_context = action_context
        return self

    def action_configs(self, action_configs: List[ActionConfig]) -> "ExternalInstanceTaskNodeBuilder":
        self._external_instance_task_node.action_configs = action_configs
        return self

    def display_method(self, display_method: str) -> "ExternalInstanceTaskNodeBuilder":
        self._external_instance_task_node.display_method = display_method
        return self

    def exclude_statistics(self, exclude_statistics: bool) -> "ExternalInstanceTaskNodeBuilder":
        self._external_instance_task_node.exclude_statistics = exclude_statistics
        return self

    def node_id(self, node_id: str) -> "ExternalInstanceTaskNodeBuilder":
        self._external_instance_task_node.node_id = node_id
        return self

    def node_name(self, node_name: str) -> "ExternalInstanceTaskNodeBuilder":
        self._external_instance_task_node.node_name = node_name
        return self

    def build(self) -> "ExternalInstanceTaskNode":
        return self._external_instance_task_node
