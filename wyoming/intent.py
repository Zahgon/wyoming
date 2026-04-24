"""Intent recognition and handling."""

from dataclasses import asdict, dataclass, field
from typing import Any, Dict, List, Optional

from .event import Event, Eventable

DOMAIN = "intent"
_RECOGNIZE_TYPE = "recognize"
_INTENT_TYPE = "intent"
_NOT_RECOGNIZED_TYPE = "not-recognized"


@dataclass
class Entity:
    """Named entity with a value."""

    name: str
    value: Optional[Any] = None


@dataclass
class Recognize(Eventable):
    """Request to recognize an event from text."""

    text: str
    """Text with intent in natural language."""

    context: Optional[Dict[str, Any]] = None
    """Context from previous interactions."""

    @staticmethod
    def is_type(event_type: str) -> bool:
        raise NotImplementedError

    def event(self) -> Event:
        raise NotImplementedError

    @staticmethod
    def from_event(event: Event) -> "Recognize":
        raise NotImplementedError


@dataclass
class Intent(Eventable):
    """Result of successful intent recognition."""

    name: str
    """Name of intent."""

    entities: List[Entity] = field(default_factory=list)
    """Named entities with values."""

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
    def from_dict(data: Dict[str, Any]) -> "Intent":
        raise NotImplementedError

    @staticmethod
    def from_event(event: Event) -> "Intent":
        raise NotImplementedError

    def to_rhasspy(self) -> Dict[str, Any]:
        pass


@dataclass
class NotRecognized(Eventable):
    """Result of intent recognition failure."""

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
    def from_event(event: Event) -> "NotRecognized":
        raise NotImplementedError
