# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .entity import Entity


class CreateEntityRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.request_body: Optional[Entity] = None

    @staticmethod
    def builder() -> "CreateEntityRequestBuilder":
        return CreateEntityRequestBuilder()


class CreateEntityRequestBuilder(object):

    def __init__(self) -> None:
        create_entity_request = CreateEntityRequest()
        create_entity_request.http_method = HttpMethod.POST
        create_entity_request.uri = "/open-apis/baike/v1/entities"
        create_entity_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._create_entity_request: CreateEntityRequest = create_entity_request

    def user_id_type(self, user_id_type: str) -> "CreateEntityRequestBuilder":
        self._create_entity_request.user_id_type = user_id_type
        self._create_entity_request.add_query("user_id_type", user_id_type)
        return self

    def request_body(self, request_body: Entity) -> "CreateEntityRequestBuilder":
        self._create_entity_request.request_body = request_body
        self._create_entity_request.body = request_body
        return self

    def build(self) -> CreateEntityRequest:
        return self._create_entity_request
