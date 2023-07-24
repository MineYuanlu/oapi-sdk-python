# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .cpst_band_width import CpstBandWidth
from .cpst_standard_type import CpstStandardType
from .reference_object import ReferenceObject


class CpstGradeStandardValue(object):
    _types = {
        "reference_object": ReferenceObject,
        "standard_type": CpstStandardType,
        "band_width": CpstBandWidth,
        "standard_value": str,
    }

    def __init__(self, d=None):
        self.reference_object: Optional[ReferenceObject] = None
        self.standard_type: Optional[CpstStandardType] = None
        self.band_width: Optional[CpstBandWidth] = None
        self.standard_value: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CpstGradeStandardValueBuilder":
        return CpstGradeStandardValueBuilder()


class CpstGradeStandardValueBuilder(object):
    def __init__(self) -> None:
        self._cpst_grade_standard_value = CpstGradeStandardValue()

    def reference_object(self, reference_object: ReferenceObject) -> "CpstGradeStandardValueBuilder":
        self._cpst_grade_standard_value.reference_object = reference_object
        return self

    def standard_type(self, standard_type: CpstStandardType) -> "CpstGradeStandardValueBuilder":
        self._cpst_grade_standard_value.standard_type = standard_type
        return self

    def band_width(self, band_width: CpstBandWidth) -> "CpstGradeStandardValueBuilder":
        self._cpst_grade_standard_value.band_width = band_width
        return self

    def standard_value(self, standard_value: str) -> "CpstGradeStandardValueBuilder":
        self._cpst_grade_standard_value.standard_value = standard_value
        return self

    def build(self) -> "CpstGradeStandardValue":
        return self._cpst_grade_standard_value
