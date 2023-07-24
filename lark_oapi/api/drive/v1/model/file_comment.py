# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .reply_list import ReplyList


class FileComment(object):
    _types = {
        "comment_id": str,
        "user_id": str,
        "create_time": int,
        "update_time": int,
        "is_solved": bool,
        "solved_time": int,
        "solver_user_id": str,
        "has_more": bool,
        "page_token": str,
        "is_whole": bool,
        "quote": str,
        "reply_list": ReplyList,
    }

    def __init__(self, d=None):
        self.comment_id: Optional[str] = None
        self.user_id: Optional[str] = None
        self.create_time: Optional[int] = None
        self.update_time: Optional[int] = None
        self.is_solved: Optional[bool] = None
        self.solved_time: Optional[int] = None
        self.solver_user_id: Optional[str] = None
        self.has_more: Optional[bool] = None
        self.page_token: Optional[str] = None
        self.is_whole: Optional[bool] = None
        self.quote: Optional[str] = None
        self.reply_list: Optional[ReplyList] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "FileCommentBuilder":
        return FileCommentBuilder()


class FileCommentBuilder(object):
    def __init__(self) -> None:
        self._file_comment = FileComment()

    def comment_id(self, comment_id: str) -> "FileCommentBuilder":
        self._file_comment.comment_id = comment_id
        return self

    def user_id(self, user_id: str) -> "FileCommentBuilder":
        self._file_comment.user_id = user_id
        return self

    def create_time(self, create_time: int) -> "FileCommentBuilder":
        self._file_comment.create_time = create_time
        return self

    def update_time(self, update_time: int) -> "FileCommentBuilder":
        self._file_comment.update_time = update_time
        return self

    def is_solved(self, is_solved: bool) -> "FileCommentBuilder":
        self._file_comment.is_solved = is_solved
        return self

    def solved_time(self, solved_time: int) -> "FileCommentBuilder":
        self._file_comment.solved_time = solved_time
        return self

    def solver_user_id(self, solver_user_id: str) -> "FileCommentBuilder":
        self._file_comment.solver_user_id = solver_user_id
        return self

    def has_more(self, has_more: bool) -> "FileCommentBuilder":
        self._file_comment.has_more = has_more
        return self

    def page_token(self, page_token: str) -> "FileCommentBuilder":
        self._file_comment.page_token = page_token
        return self

    def is_whole(self, is_whole: bool) -> "FileCommentBuilder":
        self._file_comment.is_whole = is_whole
        return self

    def quote(self, quote: str) -> "FileCommentBuilder":
        self._file_comment.quote = quote
        return self

    def reply_list(self, reply_list: ReplyList) -> "FileCommentBuilder":
        self._file_comment.reply_list = reply_list
        return self

    def build(self) -> "FileComment":
        return self._file_comment
