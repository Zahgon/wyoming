"""Speech to text."""

from dataclasses import dataclass
from typing import Any, Dict, Optional

from .event import Event, Eventable

DOMAIN = "asr"
_TRANSCRIPT_TYPE = "transcript"
_TRANSCRIBE_TYPE = "transcribe"
_TRANSCRIPT_START_TYPE = "transcript-start"
_TRANSCRIPT_CHUNK_TYPE = "transcript-chunk"
_TRANSCRIPT_STOP_TYPE = "transcript-stop"


@dataclass
class Transcript(Eventable):
    """Transcription response from ASR system"""

    text: str
    """Text transcription of spoken audio"""

    context: Optional[Dict[str, Any]] = None
    """Context for next interaction."""

    language: Optional[str] = None
    """Language of the text."""

    @staticmethod
    def is_type(event_type: str) -> bool:
        raise NotImplementedError

    def event(self) -> Event:
        raise NotImplementedError

    @staticmethod
    def from_event(event: Event) -> "Transcript":
        raise NotImplementedError


@dataclass
class Transcribe(Eventable):
    """Transcription request to ASR system.

    Followed by AudioStart, AudioChunk+, AudioStop
    """

    name: Optional[str] = None
    """Name of ASR model to use"""

    language: Optional[str] = None
    """Language of spoken audio to follow"""

    context: Optional[Dict[str, Any]] = None
    """Context from previous interactions."""

    @staticmethod
    def is_type(event_type: str) -> bool:
        raise NotImplementedError

    def event(self) -> Event:
        raise NotImplementedError

    @staticmethod
    def from_event(event: Event) -> "Transcribe":
        raise NotImplementedError


@dataclass
class TranscriptStart(Eventable):
    """Streaming transcription response from ASR system"""

    context: Optional[Dict[str, Any]] = None
    """Context for next interaction."""

    language: Optional[str] = None
    """Language of the text."""

    @staticmethod
    def is_type(event_type: str) -> bool:
        raise NotImplementedError

    def event(self) -> Event:
        raise NotImplementedError

    @staticmethod
    def from_event(event: Event) -> "TranscriptStart":
        raise NotImplementedError


@dataclass
class TranscriptChunk(Eventable):
    """Chunk of streaming transcription response from ASR system"""

    text: str
    """Chunk of transcript text."""

    @staticmethod
    def is_type(event_type: str) -> bool:
        raise NotImplementedError

    def event(self) -> Event:
        raise NotImplementedError

    @staticmethod
    def from_event(event: Event) -> "TranscriptChunk":
        raise NotImplementedError


@dataclass
class TranscriptStop(Eventable):
    """End of streaming transcription response from ASR system"""

    @staticmethod
    def is_type(event_type: str) -> bool:
        raise NotImplementedError

    def event(self) -> Event:
        raise NotImplementedError

    @staticmethod
    def from_event(event: Event) -> "TranscriptStop":
        raise NotImplementedError
