# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class AppRoleBlockRole(object):
    _types = {
        "block_id": str,
        "block_type": str,
        "block_perm": int,
    }

    def __init__(self, d=None):
        self.block_id: Optional[str] = None
        self.block_type: Optional[str] = None
        self.block_perm: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AppRoleBlockRoleBuilder":
        return AppRoleBlockRoleBuilder()


class AppRoleBlockRoleBuilder(object):
    def __init__(self) -> None:
        self._app_role_block_role = AppRoleBlockRole()

    def block_id(self, block_id: str) -> "AppRoleBlockRoleBuilder":
        self._app_role_block_role.block_id = block_id
        return self

    def block_type(self, block_type: str) -> "AppRoleBlockRoleBuilder":
        self._app_role_block_role.block_type = block_type
        return self

    def block_perm(self, block_perm: int) -> "AppRoleBlockRoleBuilder":
        self._app_role_block_role.block_perm = block_perm
        return self

    def build(self) -> "AppRoleBlockRole":
        return self._app_role_block_role
