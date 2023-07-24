# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class AppliTalentEducationInfo(object):
    _types = {
        "id": str,
        "degree": int,
        "school": str,
        "field_of_study": str,
        "start_time": str,
        "end_time": str,
        "education_type": int,
        "academic_ranking": int,
        "tag_list": List[int],
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
        self.tag_list: Optional[List[int]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AppliTalentEducationInfoBuilder":
        return AppliTalentEducationInfoBuilder()


class AppliTalentEducationInfoBuilder(object):
    def __init__(self) -> None:
        self._appli_talent_education_info = AppliTalentEducationInfo()

    def id(self, id: str) -> "AppliTalentEducationInfoBuilder":
        self._appli_talent_education_info.id = id
        return self

    def degree(self, degree: int) -> "AppliTalentEducationInfoBuilder":
        self._appli_talent_education_info.degree = degree
        return self

    def school(self, school: str) -> "AppliTalentEducationInfoBuilder":
        self._appli_talent_education_info.school = school
        return self

    def field_of_study(self, field_of_study: str) -> "AppliTalentEducationInfoBuilder":
        self._appli_talent_education_info.field_of_study = field_of_study
        return self

    def start_time(self, start_time: str) -> "AppliTalentEducationInfoBuilder":
        self._appli_talent_education_info.start_time = start_time
        return self

    def end_time(self, end_time: str) -> "AppliTalentEducationInfoBuilder":
        self._appli_talent_education_info.end_time = end_time
        return self

    def education_type(self, education_type: int) -> "AppliTalentEducationInfoBuilder":
        self._appli_talent_education_info.education_type = education_type
        return self

    def academic_ranking(self, academic_ranking: int) -> "AppliTalentEducationInfoBuilder":
        self._appli_talent_education_info.academic_ranking = academic_ranking
        return self

    def tag_list(self, tag_list: List[int]) -> "AppliTalentEducationInfoBuilder":
        self._appli_talent_education_info.tag_list = tag_list
        return self

    def build(self) -> "AppliTalentEducationInfo":
        return self._appli_talent_education_info
