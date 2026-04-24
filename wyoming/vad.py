"""Voice activity detection."""

from dataclasses import dataclass
from typing import Optional

from .event import Event, Eventable

DOMAIN = "vad"
_STARTED_TYPE = "voice-started"
_STOPPED_TYPE = "voice-stopped"


@dataclass
class VoiceStarted(Eventable):
    """User has started speaking."""

    timestamp: Optional[int] = None
    """Milliseconds"""

    @staticmethod
    def is_type(event_type: str) -> bool:
        raise NotImplementedError

    def event(self) -> Event:
        raise NotImplementedError

    @staticmethod
    def from_event(event: Event) -> "VoiceStarted":
        raise NotImplementedError


@dataclass
class VoiceStopped(Eventable):
    """User has stopped speaking."""

    timestamp: Optional[int] = None
    """Milliseconds"""

    @staticmethod
    def is_type(event_type: str) -> bool:
        raise NotImplementedError

    def event(self) -> Event:
        raise NotImplementedError

    @staticmethod
    def from_event(event: Event) -> "VoiceStopped":
        raise NotImplementedError
