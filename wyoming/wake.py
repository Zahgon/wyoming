"""Wake word detection"""

import asyncio
import contextlib
import logging
from asyncio.subprocess import Process
from dataclasses import dataclass
from typing import Any, Dict, List, Optional

from .audio import AudioChunk, AudioChunkConverter
from .client import AsyncClient
from .event import Event, Eventable

_LOGGER = logging.getLogger(__name__)

DOMAIN = "wake"
_DETECTION_TYPE = "detection"
_DETECT_TYPE = "detect"
_NOT_DETECTED_TYPE = "not-detected"


@dataclass
class Detection(Eventable):
    """Wake word was detected."""

    name: Optional[str] = None
    """Name of model."""

    timestamp: Optional[int] = None
    """Timestamp of audio chunk with detection"""

    speaker: Optional[str] = None
    """Name of speaker."""

    context: Optional[Dict[str, Any]] = None
    """Context for next interaction."""

    @staticmethod
    def is_type(event_type: str) -> bool:
        raise NotImplementedError

    def event(self) -> Event:
        raise NotImplementedError

    @staticmethod
    def from_event(event: Event) -> "Detection":
        raise NotImplementedError


@dataclass
class Detect(Eventable):
    """Wake word detection request.

    Followed by AudioStart, AudioChunk+, AudioStop
    """

    names: Optional[List[str]] = None
    """Names of models to detect (None = any)."""

    context: Optional[Dict[str, Any]] = None
    """Context for next interaction."""

    @staticmethod
    def is_type(event_type: str) -> bool:
        raise NotImplementedError

    def event(self) -> Event:
        raise NotImplementedError

    @staticmethod
    def from_event(event: Event) -> "Detect":
        raise NotImplementedError


@dataclass
class NotDetected(Eventable):
    """Audio stream ended before wake word was detected."""

    context: Optional[Dict[str, Any]] = None
    """Context for next interaction."""

    @staticmethod
    def is_type(event_type: str) -> bool:
        raise NotImplementedError

    def event(self) -> Event:
        raise NotImplementedError

    @staticmethod
    def from_event(event: Event) -> "NotDetected":
        raise NotImplementedError


class WakeProcessAsyncClient(AsyncClient, contextlib.AbstractAsyncContextManager):
    """Context manager for doing wake word detection with an external program."""

    def __init__(
        self,
        rate: int,
        width: int,
        channels: int,
        program: str,
        program_args: List[str],
    ) -> None:
        raise NotImplementedError

    async def connect(self) -> None:
        pass

    async def disconnect(self) -> None:
        raise NotImplementedError

    async def __aenter__(self) -> "WakeProcessAsyncClient":
        raise NotImplementedError

    async def __aexit__(self, exc_type, exc, tb):
        raise NotImplementedError

    async def read_event(self) -> Optional[Event]:
        raise NotImplementedError

    async def write_event(self, event: Event) -> None:
        raise NotImplementedError
