# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .equation import Equation
from .inline_block import InlineBlock
from .inline_file import InlineFile
from .mention_doc import MentionDoc
from .mention_user import MentionUser
from .reminder import Reminder
from .text_run import TextRun
from .undefined_element import UndefinedElement


class TextElement(object):
    _types = {
        "text_run": TextRun,
        "mention_user": MentionUser,
        "mention_doc": MentionDoc,
        "reminder": Reminder,
        "file": InlineFile,
        "undefined": UndefinedElement,
        "inline_block": InlineBlock,
        "equation": Equation,
    }

    def __init__(self, d=None):
        self.text_run: Optional[TextRun] = None
        self.mention_user: Optional[MentionUser] = None
        self.mention_doc: Optional[MentionDoc] = None
        self.reminder: Optional[Reminder] = None
        self.file: Optional[InlineFile] = None
        self.undefined: Optional[UndefinedElement] = None
        self.inline_block: Optional[InlineBlock] = None
        self.equation: Optional[Equation] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TextElementBuilder":
        return TextElementBuilder()


class TextElementBuilder(object):
    def __init__(self) -> None:
        self._text_element = TextElement()

    def text_run(self, text_run: TextRun) -> "TextElementBuilder":
        self._text_element.text_run = text_run
        return self

    def mention_user(self, mention_user: MentionUser) -> "TextElementBuilder":
        self._text_element.mention_user = mention_user
        return self

    def mention_doc(self, mention_doc: MentionDoc) -> "TextElementBuilder":
        self._text_element.mention_doc = mention_doc
        return self

    def reminder(self, reminder: Reminder) -> "TextElementBuilder":
        self._text_element.reminder = reminder
        return self

    def file(self, file: InlineFile) -> "TextElementBuilder":
        self._text_element.file = file
        return self

    def undefined(self, undefined: UndefinedElement) -> "TextElementBuilder":
        self._text_element.undefined = undefined
        return self

    def inline_block(self, inline_block: InlineBlock) -> "TextElementBuilder":
        self._text_element.inline_block = inline_block
        return self

    def equation(self, equation: Equation) -> "TextElementBuilder":
        self._text_element.equation = equation
        return self

    def build(self) -> "TextElement":
        return self._text_element
