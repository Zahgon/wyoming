"""Text to speech."""

from dataclasses import dataclass
from typing import Any, Dict, Optional

from .event import Event, Eventable

DOMAIN = "tts"
_SYNTHESIZE_TYPE = "synthesize"

# streaming
_SYNTHESIZE_START_TYPE = "synthesize-start"
_SYNTHESIZE_CHUNK_TYPE = "synthesize-chunk"
_SYNTHESIZE_STOP_TYPE = "synthesize-stop"
_SYNTHESIZE_STOPPED_TYPE = "synthesize-stopped"


@dataclass
class SynthesizeVoice:
    """Information about the desired voice for synthesis."""

    name: Optional[str] = None
    """Voice name from tts info (overrides language)."""

    language: Optional[str] = None
    """Voice language from tts info."""

    speaker: Optional[str] = None
    """Voice speaker from tts info."""

    def to_dict(self) -> Dict[str, str]:
        raise NotImplementedError

    @staticmethod
    def from_dict(voice: Dict[str, Any]) -> "Optional[SynthesizeVoice]":
        raise NotImplementedError


@dataclass
class Synthesize(Eventable):
    """Request to synthesize audio from text."""

    text: str
    """Text to synthesize."""

    voice: Optional[SynthesizeVoice] = None
    """Voice to use during synthesis."""

    context: Optional[Dict[str, Any]] = None
    """Context for next interaction."""

    @staticmethod
    def is_type(event_type: str) -> bool:
        raise NotImplementedError

    def event(self) -> Event:
        raise NotImplementedError

    @staticmethod
    def from_event(event: Event) -> "Synthesize":
        raise NotImplementedError


@dataclass
class SynthesizeStart(Eventable):
    """Start of streaming request to synthesize audio from text."""

    voice: Optional[SynthesizeVoice] = None
    """Voice to use during synthesis."""

    context: Optional[Dict[str, Any]] = None
    """Context for next interaction."""

    @staticmethod
    def is_type(event_type: str) -> bool:
        raise NotImplementedError

    def event(self) -> Event:
        raise NotImplementedError

    @staticmethod
    def from_event(event: Event) -> "SynthesizeStart":
        raise NotImplementedError


@dataclass
class SynthesizeChunk(Eventable):
    """Text chunk from streaming request to synthesize audio from text."""

    text: str
    """Chunk of text to synthesize."""

    @staticmethod
    def is_type(event_type: str) -> bool:
        raise NotImplementedError

    def event(self) -> Event:
        raise NotImplementedError

    @staticmethod
    def from_event(event: Event) -> "SynthesizeChunk":
        raise NotImplementedError


@dataclass
class SynthesizeStop(Eventable):
    """End of streaming request to synthesize audio from text."""

    @staticmethod
    def is_type(event_type: str) -> bool:
        raise NotImplementedError

    def event(self) -> Event:
        raise NotImplementedError

    @staticmethod
    def from_event(event: Event) -> "SynthesizeStop":
        raise NotImplementedError


@dataclass
class SynthesizeStopped(Eventable):
    """End of streaming response to streaming request."""

    @staticmethod
    def is_type(event_type: str) -> bool:
        raise NotImplementedError

    def event(self) -> Event:
        raise NotImplementedError

    @staticmethod
    def from_event(event: Event) -> "SynthesizeStopped":
        raise NotImplementedError
