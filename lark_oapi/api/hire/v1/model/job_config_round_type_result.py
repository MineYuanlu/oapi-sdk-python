# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .id_name_object import IdNameObject


class JobConfigRoundTypeResult(object):
    _types = {
        "assessment_round": IdNameObject,
        "assessment_template": IdNameObject,
    }

    def __init__(self, d=None):
        self.assessment_round: Optional[IdNameObject] = None
        self.assessment_template: Optional[IdNameObject] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "JobConfigRoundTypeResultBuilder":
        return JobConfigRoundTypeResultBuilder()


class JobConfigRoundTypeResultBuilder(object):
    def __init__(self) -> None:
        self._job_config_round_type_result = JobConfigRoundTypeResult()

    def assessment_round(self, assessment_round: IdNameObject) -> "JobConfigRoundTypeResultBuilder":
        self._job_config_round_type_result.assessment_round = assessment_round
        return self

    def assessment_template(self, assessment_template: IdNameObject) -> "JobConfigRoundTypeResultBuilder":
        self._job_config_round_type_result.assessment_template = assessment_template
        return self

    def build(self) -> "JobConfigRoundTypeResult":
        return self._job_config_round_type_result
