# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .interview_assessment_dimension_args_score import InterviewAssessmentDimensionArgsScore


class InterviewAssessmentDimensionArgs(object):
    _types = {
        "score_list": List[InterviewAssessmentDimensionArgsScore],
    }

    def __init__(self, d=None):
        self.score_list: Optional[List[InterviewAssessmentDimensionArgsScore]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "InterviewAssessmentDimensionArgsBuilder":
        return InterviewAssessmentDimensionArgsBuilder()


class InterviewAssessmentDimensionArgsBuilder(object):
    def __init__(self) -> None:
        self._interview_assessment_dimension_args = InterviewAssessmentDimensionArgs()

    def score_list(self, score_list: List[
        InterviewAssessmentDimensionArgsScore]) -> "InterviewAssessmentDimensionArgsBuilder":
        self._interview_assessment_dimension_args.score_list = score_list
        return self

    def build(self) -> "InterviewAssessmentDimensionArgs":
        return self._interview_assessment_dimension_args
