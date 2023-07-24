# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .approval_node_info import ApprovalNodeInfo
from .approval_viewer_info import ApprovalViewerInfo


class GetApprovalResponseBody(object):
    _types = {
        "approval_name": str,
        "status": str,
        "form": str,
        "node_list": List[ApprovalNodeInfo],
        "viewers": List[ApprovalViewerInfo],
        "approval_admin_ids": List[str],
        "form_widget_relation": str,
    }

    def __init__(self, d=None):
        self.approval_name: Optional[str] = None
        self.status: Optional[str] = None
        self.form: Optional[str] = None
        self.node_list: Optional[List[ApprovalNodeInfo]] = None
        self.viewers: Optional[List[ApprovalViewerInfo]] = None
        self.approval_admin_ids: Optional[List[str]] = None
        self.form_widget_relation: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetApprovalResponseBodyBuilder":
        return GetApprovalResponseBodyBuilder()


class GetApprovalResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._get_approval_response_body = GetApprovalResponseBody()

    def approval_name(self, approval_name: str) -> "GetApprovalResponseBodyBuilder":
        self._get_approval_response_body.approval_name = approval_name
        return self

    def status(self, status: str) -> "GetApprovalResponseBodyBuilder":
        self._get_approval_response_body.status = status
        return self

    def form(self, form: str) -> "GetApprovalResponseBodyBuilder":
        self._get_approval_response_body.form = form
        return self

    def node_list(self, node_list: List[ApprovalNodeInfo]) -> "GetApprovalResponseBodyBuilder":
        self._get_approval_response_body.node_list = node_list
        return self

    def viewers(self, viewers: List[ApprovalViewerInfo]) -> "GetApprovalResponseBodyBuilder":
        self._get_approval_response_body.viewers = viewers
        return self

    def approval_admin_ids(self, approval_admin_ids: List[str]) -> "GetApprovalResponseBodyBuilder":
        self._get_approval_response_body.approval_admin_ids = approval_admin_ids
        return self

    def form_widget_relation(self, form_widget_relation: str) -> "GetApprovalResponseBodyBuilder":
        self._get_approval_response_body.form_widget_relation = form_widget_relation
        return self

    def build(self) -> "GetApprovalResponseBody":
        return self._get_approval_response_body
