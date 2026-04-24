"""Ping/pong messages."""

from dataclasses import dataclass
from typing import Optional

from .event import Event, Eventable

_PING_TYPE = "ping"
_PONG_TYPE = "pong"


@dataclass
class Ping(Eventable):
    """Request pong message."""

    text: Optional[str] = None
    """Text to copy to response."""

    @staticmethod
    def is_type(event_type: str) -> bool:
        raise NotImplementedError

    def event(self) -> Event:
        raise NotImplementedError

    @staticmethod
    def from_event(event: Event) -> "Ping":
        raise NotImplementedError


@dataclass
class Pong(Eventable):
    """Response to ping message."""

    text: Optional[str] = None
    """Text copied from request."""

    @staticmethod
    def is_type(event_type: str) -> bool:
        raise NotImplementedError

    def event(self) -> Event:
        raise NotImplementedError

    @staticmethod
    def from_event(event: Event) -> "Pong":
        raise NotImplementedError
