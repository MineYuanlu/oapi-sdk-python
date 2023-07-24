# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .bot import Bot
from .cloud_doc import CloudDoc
from .docs_block import DocsBlock
from .gadget import Gadget
from .message_action import MessageAction
from .navigate import Navigate
from .plus_menu import PlusMenu
from .web_app import WebApp
from .workplace_widget import WorkplaceWidget


class AppAbility(object):
    _types = {
        "gadget": Gadget,
        "web_app": WebApp,
        "bot": Bot,
        "workplace_widgets": List[WorkplaceWidget],
        "navigate": Navigate,
        "cloud_doc": CloudDoc,
        "docs_blocks": List[DocsBlock],
        "message_action": MessageAction,
        "plus_menu": PlusMenu,
    }

    def __init__(self, d=None):
        self.gadget: Optional[Gadget] = None
        self.web_app: Optional[WebApp] = None
        self.bot: Optional[Bot] = None
        self.workplace_widgets: Optional[List[WorkplaceWidget]] = None
        self.navigate: Optional[Navigate] = None
        self.cloud_doc: Optional[CloudDoc] = None
        self.docs_blocks: Optional[List[DocsBlock]] = None
        self.message_action: Optional[MessageAction] = None
        self.plus_menu: Optional[PlusMenu] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AppAbilityBuilder":
        return AppAbilityBuilder()


class AppAbilityBuilder(object):
    def __init__(self) -> None:
        self._app_ability = AppAbility()

    def gadget(self, gadget: Gadget) -> "AppAbilityBuilder":
        self._app_ability.gadget = gadget
        return self

    def web_app(self, web_app: WebApp) -> "AppAbilityBuilder":
        self._app_ability.web_app = web_app
        return self

    def bot(self, bot: Bot) -> "AppAbilityBuilder":
        self._app_ability.bot = bot
        return self

    def workplace_widgets(self, workplace_widgets: List[WorkplaceWidget]) -> "AppAbilityBuilder":
        self._app_ability.workplace_widgets = workplace_widgets
        return self

    def navigate(self, navigate: Navigate) -> "AppAbilityBuilder":
        self._app_ability.navigate = navigate
        return self

    def cloud_doc(self, cloud_doc: CloudDoc) -> "AppAbilityBuilder":
        self._app_ability.cloud_doc = cloud_doc
        return self

    def docs_blocks(self, docs_blocks: List[DocsBlock]) -> "AppAbilityBuilder":
        self._app_ability.docs_blocks = docs_blocks
        return self

    def message_action(self, message_action: MessageAction) -> "AppAbilityBuilder":
        self._app_ability.message_action = message_action
        return self

    def plus_menu(self, plus_menu: PlusMenu) -> "AppAbilityBuilder":
        self._app_ability.plus_menu = plus_menu
        return self

    def build(self) -> "AppAbility":
        return self._app_ability
