import asyncio
import sys
from abc import ABC, abstractmethod
from functools import partial
from pathlib import Path
from typing import Callable, Dict, Optional, Union
from urllib.parse import urlparse

from .event import Event, async_get_stdin, async_read_event, async_write_event


class AsyncEventHandler(ABC):
    """Base class for async Wyoming event handler."""

    def __init__(
        self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter
    ) -> None:
        raise NotImplementedError

    @abstractmethod
    async def handle_event(self, event: Event) -> bool:
        """Handle an event. Returning false will disconnect the client."""
        return True

    async def write_event(self, event: Event) -> None:
        """Send an event to the client."""
        raise NotImplementedError

    async def run(self) -> None:
        """Receive events until stopped or handle_event returns false."""
        raise NotImplementedError

    async def disconnect(self) -> None:
        """Called when client disconnects."""

    async def stop(self) -> None:
        """Try to stop the event handler."""
        pass


HandlerFactory = Callable[
    [asyncio.StreamReader, asyncio.StreamWriter], AsyncEventHandler
]


class AsyncServer(ABC):
    """Base class for async Wyoming server."""

    def __init__(self) -> None:
        raise NotImplementedError

    @abstractmethod
    async def run(self, handler_factory: HandlerFactory) -> None:
        """Start server and block while running."""

    @staticmethod
    def from_uri(uri: str) -> "AsyncServer":
        """Create server from URI."""
        raise NotImplementedError

    async def _handler_callback(
        self,
        handler_factory: HandlerFactory,
        reader: asyncio.StreamReader,
        writer: asyncio.StreamWriter,
    ):
        pass

    async def start(self, handler_factory: HandlerFactory) -> None:
        """Start server without blocking."""

    async def stop(self) -> None:
        """Try to stop all event handlers."""
        pass


class AsyncStdioServer(AsyncServer):
    """Wyoming server over stdin/stdout."""

    async def run(self, handler_factory: HandlerFactory) -> None:
        """Start server and block while running."""
        raise NotImplementedError


class AsyncTcpServer(AsyncServer):
    """Wyoming server over TCP."""

    def __init__(self, host: str, port: int) -> None:
        raise NotImplementedError

    async def run(self, handler_factory: HandlerFactory) -> None:
        raise NotImplementedError

    async def start(self, handler_factory: HandlerFactory) -> None:
        """Start server without blocking."""
        pass

    async def stop(self) -> None:
        """Try to stop all event handlers."""
        pass


class AsyncUnixServer(AsyncServer):
    """Wyoming server over a Unix domain socket."""

    def __init__(self, socket_path: Union[str, Path]) -> None:
        raise NotImplementedError

    async def run(self, handler_factory: HandlerFactory) -> None:
        """Start server and block while running."""
        # Need to unlink socket file if it exists
        raise NotImplementedError

    async def start(self, handler_factory: HandlerFactory) -> None:
        """Start server without blocking."""
        pass

    async def stop(self) -> None:
        """Try to stop all event handlers."""
        pass
