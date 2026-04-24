"""Audio output to speakers."""

import asyncio
import contextlib
import logging
from asyncio.subprocess import Process
from dataclasses import dataclass
from typing import List, Optional

from .audio import AudioChunk, AudioChunkConverter
from .client import AsyncClient
from .event import Event, Eventable

_LOGGER = logging.getLogger(__name__)

_PLAYED_TYPE = "played"


@dataclass
class Played(Eventable):
    """Audio has finished playing."""

    @staticmethod
    def is_type(event_type: str) -> bool:
        raise NotImplementedError

    def event(self) -> Event:
        raise NotImplementedError

    @staticmethod
    def from_event(event: Event) -> "Played":
        raise NotImplementedError


class SndProcessAsyncClient(AsyncClient, contextlib.AbstractAsyncContextManager):
    """Context manager for sending output audio to an external program."""

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

    async def __aenter__(self) -> "SndProcessAsyncClient":
        raise NotImplementedError

    async def __aexit__(self, exc_type, exc, tb):
        raise NotImplementedError

    async def read_event(self) -> Optional[Event]:
        """Client is write-only."""

    async def write_event(self, event: Event) -> None:
        raise NotImplementedError
