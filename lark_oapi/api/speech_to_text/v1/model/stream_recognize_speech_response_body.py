# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class StreamRecognizeSpeechResponseBody(object):
    _types = {
        "stream_id": str,
        "sequence_id": int,
        "recognition_text": str,
    }

    def __init__(self, d=None):
        self.stream_id: Optional[str] = None
        self.sequence_id: Optional[int] = None
        self.recognition_text: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "StreamRecognizeSpeechResponseBodyBuilder":
        return StreamRecognizeSpeechResponseBodyBuilder()


class StreamRecognizeSpeechResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._stream_recognize_speech_response_body = StreamRecognizeSpeechResponseBody()

    def stream_id(self, stream_id: str) -> "StreamRecognizeSpeechResponseBodyBuilder":
        self._stream_recognize_speech_response_body.stream_id = stream_id
        return self

    def sequence_id(self, sequence_id: int) -> "StreamRecognizeSpeechResponseBodyBuilder":
        self._stream_recognize_speech_response_body.sequence_id = sequence_id
        return self

    def recognition_text(self, recognition_text: str) -> "StreamRecognizeSpeechResponseBodyBuilder":
        self._stream_recognize_speech_response_body.recognition_text = recognition_text
        return self

    def build(self) -> "StreamRecognizeSpeechResponseBody":
        return self._stream_recognize_speech_response_body
