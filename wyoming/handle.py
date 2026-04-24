"""Intent recognition and handling."""

from dataclasses import dataclass
from typing import Any, Dict, Optional

from .event import Event, Eventable

DOMAIN = "handle"
_HANDLED_TYPE = "handled"
_NOT_HANDLED_TYPE = "not-handled"
_HANDLED_START_TYPE = "handled-start"
_HANDLED_CHUNK_TYPE = "handled-chunk"
_HANDLED_STOP_TYPE = "handled-stop"


@dataclass
class Handled(Eventable):
    """Result of successful intent handling."""

    text: Optional[str] = None
    """Human-readable response."""

    context: Optional[Dict[str, Any]] = None
    """Context for next interaction."""

    @staticmethod
    def is_type(event_type: str) -> bool:
        raise NotImplementedError

    def event(self) -> Event:
        raise NotImplementedError

    @staticmethod
    def from_event(event: Event) -> "Handled":
        raise NotImplementedError


@dataclass
class NotHandled(Eventable):
    """Result of intent handling failure."""

    text: Optional[str] = None
    """Human-readable response."""

    context: Optional[Dict[str, Any]] = None
    """Context for next interaction."""

    @staticmethod
    def is_type(event_type: str) -> bool:
        raise NotImplementedError

    def event(self) -> Event:
        raise NotImplementedError

    @staticmethod
    def from_event(event: Event) -> "NotHandled":
        raise NotImplementedError


@dataclass
class HandledStart(Eventable):
    """Start of streaming result of successful intent handling."""

    context: Optional[Dict[str, Any]] = None
    """Context for next interaction."""

    @staticmethod
    def is_type(event_type: str) -> bool:
        raise NotImplementedError

    def event(self) -> Event:
        raise NotImplementedError

    @staticmethod
    def from_event(event: Event) -> "HandledStart":
        raise NotImplementedError


@dataclass
class HandledChunk(Eventable):
    """Response chunk of streaming result of successful intent handling."""

    text: str
    """Chunk of response text."""

    @staticmethod
    def is_type(event_type: str) -> bool:
        raise NotImplementedError

    def event(self) -> Event:
        raise NotImplementedError

    @staticmethod
    def from_event(event: Event) -> "HandledChunk":
        raise NotImplementedError


@dataclass
class HandledStop(Eventable):
    """End of streaming sesult of successful intent handling."""

    @staticmethod
    def is_type(event_type: str) -> bool:
        raise NotImplementedError

    def event(self) -> Event:
        raise NotImplementedError

    @staticmethod
    def from_event(event: Event) -> "HandledStop":
        raise NotImplementedError
