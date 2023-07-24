# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class StreamConfig(object):
    _types = {
        "stream_id": str,
        "sequence_id": int,
        "action": int,
        "format": str,
        "engine_type": str,
    }

    def __init__(self, d=None):
        self.stream_id: Optional[str] = None
        self.sequence_id: Optional[int] = None
        self.action: Optional[int] = None
        self.format: Optional[str] = None
        self.engine_type: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "StreamConfigBuilder":
        return StreamConfigBuilder()


class StreamConfigBuilder(object):
    def __init__(self) -> None:
        self._stream_config = StreamConfig()

    def stream_id(self, stream_id: str) -> "StreamConfigBuilder":
        self._stream_config.stream_id = stream_id
        return self

    def sequence_id(self, sequence_id: int) -> "StreamConfigBuilder":
        self._stream_config.sequence_id = sequence_id
        return self

    def action(self, action: int) -> "StreamConfigBuilder":
        self._stream_config.action = action
        return self

    def format(self, format: str) -> "StreamConfigBuilder":
        self._stream_config.format = format
        return self

    def engine_type(self, engine_type: str) -> "StreamConfigBuilder":
        self._stream_config.engine_type = engine_type
        return self

    def build(self) -> "StreamConfig":
        return self._stream_config
