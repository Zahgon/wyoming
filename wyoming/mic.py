"""Microphone input."""

import asyncio
import contextlib
import logging
import time
from asyncio.subprocess import Process
from typing import List, Optional

from .audio import AudioChunk
from .client import AsyncClient
from .event import Event

_LOGGER = logging.getLogger(__name__)

DOMAIN = "mic"


class MicProcessAsyncClient(AsyncClient, contextlib.AbstractAsyncContextManager):
    """Context manager for getting microphone audio from an external program."""

    def __init__(
        self,
        rate: int,
        width: int,
        channels: int,
        samples_per_chunk: int,
        program: str,
        program_args: List[str],
    ) -> None:
        raise NotImplementedError

    async def connect(self) -> None:
        pass

    async def disconnect(self) -> None:
        raise NotImplementedError

    async def __aenter__(self) -> "MicProcessAsyncClient":
        raise NotImplementedError

    async def __aexit__(self, exc_type, exc, tb):
        raise NotImplementedError

    async def read_event(self) -> Optional[Event]:
        raise NotImplementedError

    async def write_event(self, event: Event) -> None:
        """Client is read-only."""
