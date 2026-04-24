"""Error event."""

from dataclasses import dataclass
from typing import Any, Dict, Optional

from .event import Event, Eventable

_ERROR_TYPE = "error"


@dataclass
class Error(Eventable):
    """Error with text and an optional code."""

    text: str
    """Human-readable error message."""

    code: Optional[str] = None
    """Machine-readable error code."""

    @staticmethod
    def is_type(event_type: str) -> bool:
        raise NotImplementedError

    def event(self) -> Event:
        raise NotImplementedError

    @staticmethod
    def from_event(event: Event) -> "Error":
        raise NotImplementedError
