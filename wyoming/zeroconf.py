"""Runs mDNS zeroconf service for Home Assistant discovery."""

import logging
import socket
import uuid
from typing import Optional

_LOGGER = logging.getLogger(__name__)

try:
    from zeroconf.asyncio import AsyncServiceInfo, AsyncZeroconf
except ImportError:
    _LOGGER.fatal("pip install zeroconf")
    raise

MDNS_TARGET_IP = "224.0.0.251"


class HomeAssistantZeroconf:
    """ZeroConf (mDNS) discovery for Home Assistant."""

    def __init__(
        self, port: int, name: Optional[str] = None, host: Optional[str] = None
    ) -> None:
        self.port = port
        self.name = name or _get_mac_address()

        if not host:
            test_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            test_sock.setblocking(False)
            test_sock.connect((MDNS_TARGET_IP, 1))
            host = test_sock.getsockname()[0]
            _LOGGER.debug("Detected IP: %s", host)

        assert host
        self.host = host
        self._aiozc = AsyncZeroconf()

    async def register_server(self) -> None:
        """Register ZeroConf server."""
        pass


def _get_mac_address() -> str:
    """Return MAC address formatted as hex with no colons."""
    pass
