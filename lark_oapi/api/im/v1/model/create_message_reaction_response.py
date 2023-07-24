# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .create_message_reaction_response_body import CreateMessageReactionResponseBody


class CreateMessageReactionResponse(BaseResponse):
    _types = {
        "data": CreateMessageReactionResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[CreateMessageReactionResponseBody] = None
        init(self, d, self._types)
