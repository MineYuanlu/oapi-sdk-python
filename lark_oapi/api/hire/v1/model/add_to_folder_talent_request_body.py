# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class AddToFolderTalentRequestBody(object):
    _types = {
        "talent_id_list": List[str],
        "folder_id": str,
    }

    def __init__(self, d=None):
        self.talent_id_list: Optional[List[str]] = None
        self.folder_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AddToFolderTalentRequestBodyBuilder":
        return AddToFolderTalentRequestBodyBuilder()


class AddToFolderTalentRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._add_to_folder_talent_request_body = AddToFolderTalentRequestBody()

    def talent_id_list(self, talent_id_list: List[str]) -> "AddToFolderTalentRequestBodyBuilder":
        self._add_to_folder_talent_request_body.talent_id_list = talent_id_list
        return self

    def folder_id(self, folder_id: str) -> "AddToFolderTalentRequestBodyBuilder":
        self._add_to_folder_talent_request_body.folder_id = folder_id
        return self

    def build(self) -> "AddToFolderTalentRequestBody":
        return self._add_to_folder_talent_request_body
