# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class ContactsRangeConfigurationApplicationRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.page_size: Optional[int] = None
        self.page_token: Optional[str] = None
        self.department_id_type: Optional[str] = None
        self.user_id_type: Optional[str] = None
        self.app_id: Optional[str] = None

    @staticmethod
    def builder() -> "ContactsRangeConfigurationApplicationRequestBuilder":
        return ContactsRangeConfigurationApplicationRequestBuilder()


class ContactsRangeConfigurationApplicationRequestBuilder(object):

    def __init__(self) -> None:
        contacts_range_configuration_application_request = ContactsRangeConfigurationApplicationRequest()
        contacts_range_configuration_application_request.http_method = HttpMethod.GET
        contacts_range_configuration_application_request.uri = "/open-apis/application/v6/applications/:app_id/contacts_range_configuration"
        contacts_range_configuration_application_request.token_types = {AccessTokenType.TENANT}
        self._contacts_range_configuration_application_request: ContactsRangeConfigurationApplicationRequest = contacts_range_configuration_application_request

    def page_size(self, page_size: int) -> "ContactsRangeConfigurationApplicationRequestBuilder":
        self._contacts_range_configuration_application_request.page_size = page_size
        self._contacts_range_configuration_application_request.add_query("page_size", page_size)
        return self

    def page_token(self, page_token: str) -> "ContactsRangeConfigurationApplicationRequestBuilder":
        self._contacts_range_configuration_application_request.page_token = page_token
        self._contacts_range_configuration_application_request.add_query("page_token", page_token)
        return self

    def department_id_type(self, department_id_type: str) -> "ContactsRangeConfigurationApplicationRequestBuilder":
        self._contacts_range_configuration_application_request.department_id_type = department_id_type
        self._contacts_range_configuration_application_request.add_query("department_id_type", department_id_type)
        return self

    def user_id_type(self, user_id_type: str) -> "ContactsRangeConfigurationApplicationRequestBuilder":
        self._contacts_range_configuration_application_request.user_id_type = user_id_type
        self._contacts_range_configuration_application_request.add_query("user_id_type", user_id_type)
        return self

    def app_id(self, app_id: str) -> "ContactsRangeConfigurationApplicationRequestBuilder":
        self._contacts_range_configuration_application_request.app_id = app_id
        self._contacts_range_configuration_application_request.paths["app_id"] = str(app_id)
        return self

    def build(self) -> ContactsRangeConfigurationApplicationRequest:
        return self._contacts_range_configuration_application_request
