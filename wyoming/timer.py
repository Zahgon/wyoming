"""Support for voice timers."""

from dataclasses import dataclass
from typing import Optional

from .event import Event, Eventable

DOMAIN = "timer"
_STARTED_TYPE = "timer-started"
_UPDATED_TYPE = "timer-updated"
_CANCELLED_TYPE = "timer-cancelled"
_FINISHED_TYPE = "timer-finished"


@dataclass
class TimerStarted(Eventable):
    """New timer was started."""

    id: str
    """Unique id of timer."""

    total_seconds: int
    """Total number of seconds the timer will run for."""

    name: Optional[str] = None
    """Optional name provided by user."""

    start_hours: Optional[int] = None
    """Number of hours users requested the timer to run for."""

    start_minutes: Optional[int] = None
    """Number of minutes users requested the timer to run for."""

    start_seconds: Optional[int] = None
    """Number of minutes users requested the timer to run for."""

    @staticmethod
    def is_type(event_type: str) -> bool:
        raise NotImplementedError

    def event(self) -> Event:
        raise NotImplementedError

    @staticmethod
    def from_event(event: Event) -> "TimerStarted":
        raise NotImplementedError


@dataclass
class TimerUpdated(Eventable):
    """Existing timer was paused, resumed, or had time added or removed."""

    id: str
    """Unique id of timer."""

    is_active: bool
    """True if timer is running."""

    total_seconds: int
    """Number of seconds left on the timer."""

    @staticmethod
    def is_type(event_type: str) -> bool:
        raise NotImplementedError

    def event(self) -> Event:
        raise NotImplementedError

    @staticmethod
    def from_event(event: Event) -> "TimerUpdated":
        raise NotImplementedError


@dataclass
class TimerCancelled(Eventable):
    """Existing timer was cancelled."""

    id: str
    """Unique id of timer."""

    @staticmethod
    def is_type(event_type: str) -> bool:
        raise NotImplementedError

    def event(self) -> Event:
        raise NotImplementedError

    @staticmethod
    def from_event(event: Event) -> "TimerCancelled":
        raise NotImplementedError


@dataclass
class TimerFinished(Eventable):
    """Existing timer finished without being cancelled."""

    id: str
    """Unique id of timer."""

    @staticmethod
    def is_type(event_type: str) -> bool:
        raise NotImplementedError

    def event(self) -> Event:
        raise NotImplementedError

    @staticmethod
    def from_event(event: Event) -> "TimerFinished":
        raise NotImplementedError
