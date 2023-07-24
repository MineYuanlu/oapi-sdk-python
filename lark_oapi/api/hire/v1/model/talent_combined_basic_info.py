# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .talent_customized_data_object_value import TalentCustomizedDataObjectValue
from .talent_identification_info import TalentIdentificationInfo


class TalentCombinedBasicInfo(object):
    _types = {
        "name": str,
        "mobile": str,
        "mobile_country_code": str,
        "email": str,
        "identification_type": int,
        "identification_number": str,
        "identification": TalentIdentificationInfo,
        "start_work_time": str,
        "birthday": str,
        "gender": int,
        "nationality_id": str,
        "current_city_code": str,
        "hometown_city_code": str,
        "customized_data": List[TalentCustomizedDataObjectValue],
    }

    def __init__(self, d=None):
        self.name: Optional[str] = None
        self.mobile: Optional[str] = None
        self.mobile_country_code: Optional[str] = None
        self.email: Optional[str] = None
        self.identification_type: Optional[int] = None
        self.identification_number: Optional[str] = None
        self.identification: Optional[TalentIdentificationInfo] = None
        self.start_work_time: Optional[str] = None
        self.birthday: Optional[str] = None
        self.gender: Optional[int] = None
        self.nationality_id: Optional[str] = None
        self.current_city_code: Optional[str] = None
        self.hometown_city_code: Optional[str] = None
        self.customized_data: Optional[List[TalentCustomizedDataObjectValue]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TalentCombinedBasicInfoBuilder":
        return TalentCombinedBasicInfoBuilder()


class TalentCombinedBasicInfoBuilder(object):
    def __init__(self) -> None:
        self._talent_combined_basic_info = TalentCombinedBasicInfo()

    def name(self, name: str) -> "TalentCombinedBasicInfoBuilder":
        self._talent_combined_basic_info.name = name
        return self

    def mobile(self, mobile: str) -> "TalentCombinedBasicInfoBuilder":
        self._talent_combined_basic_info.mobile = mobile
        return self

    def mobile_country_code(self, mobile_country_code: str) -> "TalentCombinedBasicInfoBuilder":
        self._talent_combined_basic_info.mobile_country_code = mobile_country_code
        return self

    def email(self, email: str) -> "TalentCombinedBasicInfoBuilder":
        self._talent_combined_basic_info.email = email
        return self

    def identification_type(self, identification_type: int) -> "TalentCombinedBasicInfoBuilder":
        self._talent_combined_basic_info.identification_type = identification_type
        return self

    def identification_number(self, identification_number: str) -> "TalentCombinedBasicInfoBuilder":
        self._talent_combined_basic_info.identification_number = identification_number
        return self

    def identification(self, identification: TalentIdentificationInfo) -> "TalentCombinedBasicInfoBuilder":
        self._talent_combined_basic_info.identification = identification
        return self

    def start_work_time(self, start_work_time: str) -> "TalentCombinedBasicInfoBuilder":
        self._talent_combined_basic_info.start_work_time = start_work_time
        return self

    def birthday(self, birthday: str) -> "TalentCombinedBasicInfoBuilder":
        self._talent_combined_basic_info.birthday = birthday
        return self

    def gender(self, gender: int) -> "TalentCombinedBasicInfoBuilder":
        self._talent_combined_basic_info.gender = gender
        return self

    def nationality_id(self, nationality_id: str) -> "TalentCombinedBasicInfoBuilder":
        self._talent_combined_basic_info.nationality_id = nationality_id
        return self

    def current_city_code(self, current_city_code: str) -> "TalentCombinedBasicInfoBuilder":
        self._talent_combined_basic_info.current_city_code = current_city_code
        return self

    def hometown_city_code(self, hometown_city_code: str) -> "TalentCombinedBasicInfoBuilder":
        self._talent_combined_basic_info.hometown_city_code = hometown_city_code
        return self

    def customized_data(self,
                        customized_data: List[TalentCustomizedDataObjectValue]) -> "TalentCombinedBasicInfoBuilder":
        self._talent_combined_basic_info.customized_data = customized_data
        return self

    def build(self) -> "TalentCombinedBasicInfo":
        return self._talent_combined_basic_info
