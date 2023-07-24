# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .talent_customized_data_object_value import TalentCustomizedDataObjectValue


class TalentCombinedEducationInfo(object):
    _types = {
        "id": str,
        "degree": int,
        "school": str,
        "field_of_study": str,
        "start_time": str,
        "end_time": str,
        "education_type": int,
        "academic_ranking": int,
        "customized_data": List[TalentCustomizedDataObjectValue],
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.degree: Optional[int] = None
        self.school: Optional[str] = None
        self.field_of_study: Optional[str] = None
        self.start_time: Optional[str] = None
        self.end_time: Optional[str] = None
        self.education_type: Optional[int] = None
        self.academic_ranking: Optional[int] = None
        self.customized_data: Optional[List[TalentCustomizedDataObjectValue]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TalentCombinedEducationInfoBuilder":
        return TalentCombinedEducationInfoBuilder()


class TalentCombinedEducationInfoBuilder(object):
    def __init__(self) -> None:
        self._talent_combined_education_info = TalentCombinedEducationInfo()

    def id(self, id: str) -> "TalentCombinedEducationInfoBuilder":
        self._talent_combined_education_info.id = id
        return self

    def degree(self, degree: int) -> "TalentCombinedEducationInfoBuilder":
        self._talent_combined_education_info.degree = degree
        return self

    def school(self, school: str) -> "TalentCombinedEducationInfoBuilder":
        self._talent_combined_education_info.school = school
        return self

    def field_of_study(self, field_of_study: str) -> "TalentCombinedEducationInfoBuilder":
        self._talent_combined_education_info.field_of_study = field_of_study
        return self

    def start_time(self, start_time: str) -> "TalentCombinedEducationInfoBuilder":
        self._talent_combined_education_info.start_time = start_time
        return self

    def end_time(self, end_time: str) -> "TalentCombinedEducationInfoBuilder":
        self._talent_combined_education_info.end_time = end_time
        return self

    def education_type(self, education_type: int) -> "TalentCombinedEducationInfoBuilder":
        self._talent_combined_education_info.education_type = education_type
        return self

    def academic_ranking(self, academic_ranking: int) -> "TalentCombinedEducationInfoBuilder":
        self._talent_combined_education_info.academic_ranking = academic_ranking
        return self

    def customized_data(self,
                        customized_data: List[TalentCustomizedDataObjectValue]) -> "TalentCombinedEducationInfoBuilder":
        self._talent_combined_education_info.customized_data = customized_data
        return self

    def build(self) -> "TalentCombinedEducationInfo":
        return self._talent_combined_education_info
