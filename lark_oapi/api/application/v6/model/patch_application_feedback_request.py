# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class PatchApplicationFeedbackRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.status: Optional[int] = None
        self.operator_id: Optional[str] = None
        self.app_id: Optional[str] = None
        self.feedback_id: Optional[int] = None

    @staticmethod
    def builder() -> "PatchApplicationFeedbackRequestBuilder":
        return PatchApplicationFeedbackRequestBuilder()


class PatchApplicationFeedbackRequestBuilder(object):

    def __init__(self) -> None:
        patch_application_feedback_request = PatchApplicationFeedbackRequest()
        patch_application_feedback_request.http_method = HttpMethod.PATCH
        patch_application_feedback_request.uri = "/open-apis/application/v6/applications/:app_id/feedbacks/:feedback_id"
        patch_application_feedback_request.token_types = {AccessTokenType.TENANT}
        self._patch_application_feedback_request: PatchApplicationFeedbackRequest = patch_application_feedback_request

    def user_id_type(self, user_id_type: str) -> "PatchApplicationFeedbackRequestBuilder":
        self._patch_application_feedback_request.user_id_type = user_id_type
        self._patch_application_feedback_request.add_query("user_id_type", user_id_type)
        return self

    def status(self, status: int) -> "PatchApplicationFeedbackRequestBuilder":
        self._patch_application_feedback_request.status = status
        self._patch_application_feedback_request.add_query("status", status)
        return self

    def operator_id(self, operator_id: str) -> "PatchApplicationFeedbackRequestBuilder":
        self._patch_application_feedback_request.operator_id = operator_id
        self._patch_application_feedback_request.add_query("operator_id", operator_id)
        return self

    def app_id(self, app_id: str) -> "PatchApplicationFeedbackRequestBuilder":
        self._patch_application_feedback_request.app_id = app_id
        self._patch_application_feedback_request.paths["app_id"] = str(app_id)
        return self

    def feedback_id(self, feedback_id: int) -> "PatchApplicationFeedbackRequestBuilder":
        self._patch_application_feedback_request.feedback_id = feedback_id
        self._patch_application_feedback_request.paths["feedback_id"] = str(feedback_id)
        return self

    def build(self) -> PatchApplicationFeedbackRequest:
        return self._patch_application_feedback_request
