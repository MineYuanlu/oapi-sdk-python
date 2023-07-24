# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class MaterialReviewResult(object):
    _types = {
        "file_token": str,
        "result": int,
    }

    def __init__(self, d=None):
        self.file_token: Optional[str] = None
        self.result: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "MaterialReviewResultBuilder":
        return MaterialReviewResultBuilder()


class MaterialReviewResultBuilder(object):
    def __init__(self) -> None:
        self._material_review_result = MaterialReviewResult()

    def file_token(self, file_token: str) -> "MaterialReviewResultBuilder":
        self._material_review_result.file_token = file_token
        return self

    def result(self, result: int) -> "MaterialReviewResultBuilder":
        self._material_review_result.result = result
        return self

    def build(self) -> "MaterialReviewResult":
        return self._material_review_result
