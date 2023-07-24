# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .site_application_resume import SiteApplicationResume


class SiteApplication(object):
    _types = {
        "external_id": str,
        "job_post_id": str,
        "resume": SiteApplicationResume,
        "status": str,
    }

    def __init__(self, d=None):
        self.external_id: Optional[str] = None
        self.job_post_id: Optional[str] = None
        self.resume: Optional[SiteApplicationResume] = None
        self.status: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SiteApplicationBuilder":
        return SiteApplicationBuilder()


class SiteApplicationBuilder(object):
    def __init__(self) -> None:
        self._site_application = SiteApplication()

    def external_id(self, external_id: str) -> "SiteApplicationBuilder":
        self._site_application.external_id = external_id
        return self

    def job_post_id(self, job_post_id: str) -> "SiteApplicationBuilder":
        self._site_application.job_post_id = job_post_id
        return self

    def resume(self, resume: SiteApplicationResume) -> "SiteApplicationBuilder":
        self._site_application.resume = resume
        return self

    def status(self, status: str) -> "SiteApplicationBuilder":
        self._site_application.status = status
        return self

    def build(self) -> "SiteApplication":
        return self._site_application
