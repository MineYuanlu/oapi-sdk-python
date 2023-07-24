# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class SiteResumeLanguageSkill(object):
    _types = {
        "language": str,
        "proficiency": str,
    }

    def __init__(self, d=None):
        self.language: Optional[str] = None
        self.proficiency: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SiteResumeLanguageSkillBuilder":
        return SiteResumeLanguageSkillBuilder()


class SiteResumeLanguageSkillBuilder(object):
    def __init__(self) -> None:
        self._site_resume_language_skill = SiteResumeLanguageSkill()

    def language(self, language: str) -> "SiteResumeLanguageSkillBuilder":
        self._site_resume_language_skill.language = language
        return self

    def proficiency(self, proficiency: str) -> "SiteResumeLanguageSkillBuilder":
        self._site_resume_language_skill.proficiency = proficiency
        return self

    def build(self) -> "SiteResumeLanguageSkill":
        return self._site_resume_language_skill
