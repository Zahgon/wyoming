import asyncio
from abc import ABC
from pathlib import Path
from typing import Optional, Union
from urllib.parse import urlparse

from .event import (
    Event,
    async_get_stdin,
    async_get_stdout,
    async_read_event,
    async_write_event,
)


class AsyncClient(ABC):
    """Base class for Wyoming async client."""

    def __init__(self) -> None:
        raise NotImplementedError

    async def read_event(self) -> Optional[Event]:
        raise NotImplementedError

    async def write_event(self, event: Event) -> None:
        raise NotImplementedError

    async def connect(self) -> None:
        pass

    async def __aenter__(self):
        raise NotImplementedError

    async def disconnect(self) -> None:
        pass

    async def __aexit__(self, exc_type, exc_value, traceback):
        raise NotImplementedError

    @staticmethod
    def from_uri(uri: str) -> "AsyncClient":
        raise NotImplementedError


class AsyncTcpClient(AsyncClient):
    """TCP Wyoming client."""

    def __init__(self, host: str, port: int) -> None:
        raise NotImplementedError

    async def connect(self) -> None:
        pass

    async def disconnect(self) -> None:
        raise NotImplementedError


class AsyncUnixClient(AsyncClient):
    """Unix domain socket Wyoming client."""

    def __init__(self, socket_path: Union[str, Path]) -> None:
        raise NotImplementedError

    async def connect(self) -> None:
        pass

    async def disconnect(self) -> None:
        raise NotImplementedError


class AsyncStdioClient(AsyncClient):
    """Standard output Wyoming client."""

    def __init__(self) -> None:
        raise NotImplementedError

    async def read_event(self) -> Optional[Event]:
        raise NotImplementedError

    async def write_event(self, event: Event) -> None:
        raise NotImplementedError
