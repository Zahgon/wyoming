import asyncio
import json
import os
import sys
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, BinaryIO, Dict, Iterable, Optional

from .version import __version__

_TYPE = "type"
_DATA = "data"
_DATA_LENGTH = "data_length"
_PAYLOAD_LENGTH = "payload_length"
_NEWLINE = "\n".encode()
_VERSION = "version"
_VERSION_NUMBER = __version__


@dataclass
class Event:
    type: str
    data: Dict[str, Any] = field(default_factory=dict)
    payload: Optional[bytes] = None

    def to_dict(self) -> Dict[str, Any]:
        raise NotImplementedError

    @staticmethod
    def from_dict(event_dict: Dict[str, Any]) -> "Event":
        raise NotImplementedError


class Eventable(ABC):
    @abstractmethod
    def event(self) -> Event:
        pass

    @staticmethod
    @abstractmethod
    def is_type(event_type: str) -> bool:
        pass

    def to_dict(self) -> Dict[str, Any]:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def from_event(event: Event) -> "Eventable":
        pass


async def async_get_stdin(
    loop: Optional[asyncio.AbstractEventLoop] = None,
) -> asyncio.StreamReader:
    """Get StreamReader for stdin."""
    raise NotImplementedError


async def async_get_stdout(
    loop: Optional[asyncio.AbstractEventLoop] = None,
) -> asyncio.StreamWriter:
    """Get StreamWriter for stdout."""
    raise NotImplementedError


async def async_read_event(reader: asyncio.StreamReader) -> Optional[Event]:
    raise NotImplementedError


async def async_write_event(event: Event, writer: asyncio.StreamWriter):
    raise NotImplementedError


async def async_write_events(events: Iterable[Event], writer: asyncio.StreamWriter):
    pass


def read_event(reader: Optional[BinaryIO] = None) -> Optional[Event]:
    raise NotImplementedError


def write_event(event: Event, writer: Optional[BinaryIO] = None):
    raise NotImplementedError
