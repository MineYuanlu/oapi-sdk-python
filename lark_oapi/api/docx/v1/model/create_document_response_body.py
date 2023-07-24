# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .document import Document


class CreateDocumentResponseBody(object):
    _types = {
        "document": Document,
    }

    def __init__(self, d=None):
        self.document: Optional[Document] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateDocumentResponseBodyBuilder":
        return CreateDocumentResponseBodyBuilder()


class CreateDocumentResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._create_document_response_body = CreateDocumentResponseBody()

    def document(self, document: Document) -> "CreateDocumentResponseBodyBuilder":
        self._create_document_response_body.document = document
        return self

    def build(self) -> "CreateDocumentResponseBody":
        return self._create_document_response_body
