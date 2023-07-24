# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .extend_field import ExtendField
from .multi_language import MultiLanguage
from .project_company_dept_mapping import ProjectCompanyDeptMapping


class Project(object):
    _types = {
        "project_uid": str,
        "code": str,
        "name": str,
        "type": str,
        "responsible_user_union_id": str,
        "start_day": str,
        "end_day": str,
        "parent_code": str,
        "level": int,
        "level_info": str,
        "status": int,
        "extend_info": List[ExtendField],
        "is_all_company": bool,
        "project_company_dept_mappings": List[ProjectCompanyDeptMapping],
        "multi_language_name": List[MultiLanguage],
    }

    def __init__(self, d=None):
        self.project_uid: Optional[str] = None
        self.code: Optional[str] = None
        self.name: Optional[str] = None
        self.type: Optional[str] = None
        self.responsible_user_union_id: Optional[str] = None
        self.start_day: Optional[str] = None
        self.end_day: Optional[str] = None
        self.parent_code: Optional[str] = None
        self.level: Optional[int] = None
        self.level_info: Optional[str] = None
        self.status: Optional[int] = None
        self.extend_info: Optional[List[ExtendField]] = None
        self.is_all_company: Optional[bool] = None
        self.project_company_dept_mappings: Optional[List[ProjectCompanyDeptMapping]] = None
        self.multi_language_name: Optional[List[MultiLanguage]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ProjectBuilder":
        return ProjectBuilder()


class ProjectBuilder(object):
    def __init__(self) -> None:
        self._project = Project()

    def project_uid(self, project_uid: str) -> "ProjectBuilder":
        self._project.project_uid = project_uid
        return self

    def code(self, code: str) -> "ProjectBuilder":
        self._project.code = code
        return self

    def name(self, name: str) -> "ProjectBuilder":
        self._project.name = name
        return self

    def type(self, type: str) -> "ProjectBuilder":
        self._project.type = type
        return self

    def responsible_user_union_id(self, responsible_user_union_id: str) -> "ProjectBuilder":
        self._project.responsible_user_union_id = responsible_user_union_id
        return self

    def start_day(self, start_day: str) -> "ProjectBuilder":
        self._project.start_day = start_day
        return self

    def end_day(self, end_day: str) -> "ProjectBuilder":
        self._project.end_day = end_day
        return self

    def parent_code(self, parent_code: str) -> "ProjectBuilder":
        self._project.parent_code = parent_code
        return self

    def level(self, level: int) -> "ProjectBuilder":
        self._project.level = level
        return self

    def level_info(self, level_info: str) -> "ProjectBuilder":
        self._project.level_info = level_info
        return self

    def status(self, status: int) -> "ProjectBuilder":
        self._project.status = status
        return self

    def extend_info(self, extend_info: List[ExtendField]) -> "ProjectBuilder":
        self._project.extend_info = extend_info
        return self

    def is_all_company(self, is_all_company: bool) -> "ProjectBuilder":
        self._project.is_all_company = is_all_company
        return self

    def project_company_dept_mappings(self, project_company_dept_mappings: List[
        ProjectCompanyDeptMapping]) -> "ProjectBuilder":
        self._project.project_company_dept_mappings = project_company_dept_mappings
        return self

    def multi_language_name(self, multi_language_name: List[MultiLanguage]) -> "ProjectBuilder":
        self._project.multi_language_name = multi_language_name
        return self

    def build(self) -> "Project":
        return self._project
