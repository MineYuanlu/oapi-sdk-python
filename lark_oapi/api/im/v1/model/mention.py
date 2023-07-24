# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class Mention(object):
    _types = {
        "key": str,
        "id": str,
        "id_type": str,
        "name": str,
        "tenant_key": str,
    }

    def __init__(self, d=None):
        self.key: Optional[str] = None
        self.id: Optional[str] = None
        self.id_type: Optional[str] = None
        self.name: Optional[str] = None
        self.tenant_key: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "MentionBuilder":
        return MentionBuilder()


class MentionBuilder(object):
    def __init__(self) -> None:
        self._mention = Mention()

    def key(self, key: str) -> "MentionBuilder":
        self._mention.key = key
        return self

    def id(self, id: str) -> "MentionBuilder":
        self._mention.id = id
        return self

    def id_type(self, id_type: str) -> "MentionBuilder":
        self._mention.id_type = id_type
        return self

    def name(self, name: str) -> "MentionBuilder":
        self._mention.name = name
        return self

    def tenant_key(self, tenant_key: str) -> "MentionBuilder":
        self._mention.tenant_key = tenant_key
        return self

    def build(self) -> "Mention":
        return self._mention
