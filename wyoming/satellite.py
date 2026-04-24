"""Satellite events."""

from dataclasses import dataclass

from .event import Event, Eventable

_RUN_SATELLITE_TYPE = "run-satellite"
_PAUSE_SATELLITE_TYPE = "pause-satellite"
_STREAMING_STARTED_TYPE = "streaming-started"
_STREAMING_STOPPED_TYPE = "streaming-stopped"
_SATELLITE_CONNECTED_TYPE = "satellite-connected"
_SATELLITE_DISCONNECTED_TYPE = "satellite-disconnected"


@dataclass
class RunSatellite(Eventable):
    """Informs the satellite that the server is ready to run a pipeline."""

    @staticmethod
    def is_type(event_type: str) -> bool:
        raise NotImplementedError

    def event(self) -> Event:
        raise NotImplementedError

    @staticmethod
    def from_event(event: Event) -> "RunSatellite":
        raise NotImplementedError


@dataclass
class PauseSatellite(Eventable):
    """Informs the satellite that the server is not ready to run a pipeline."""

    @staticmethod
    def is_type(event_type: str) -> bool:
        raise NotImplementedError

    def event(self) -> Event:
        raise NotImplementedError

    @staticmethod
    def from_event(event: Event) -> "PauseSatellite":
        raise NotImplementedError


@dataclass
class StreamingStarted(Eventable):
    """Satellite has started streaming audio to server."""

    @staticmethod
    def is_type(event_type: str) -> bool:
        raise NotImplementedError

    def event(self) -> Event:
        raise NotImplementedError

    @staticmethod
    def from_event(event: Event) -> "StreamingStarted":
        raise NotImplementedError


@dataclass
class StreamingStopped(Eventable):
    """Satellite has stopped streaming audio to server."""

    @staticmethod
    def is_type(event_type: str) -> bool:
        raise NotImplementedError

    def event(self) -> Event:
        raise NotImplementedError

    @staticmethod
    def from_event(event: Event) -> "StreamingStopped":
        raise NotImplementedError


@dataclass
class SatelliteConnected(Eventable):
    """Satellite has connected to server."""

    @staticmethod
    def is_type(event_type: str) -> bool:
        raise NotImplementedError

    def event(self) -> Event:
        raise NotImplementedError

    @staticmethod
    def from_event(event: Event) -> "SatelliteConnected":
        raise NotImplementedError


@dataclass
class SatelliteDisconnected(Eventable):
    """Satellite has disconnected from server."""

    @staticmethod
    def is_type(event_type: str) -> bool:
        raise NotImplementedError

    def event(self) -> Event:
        raise NotImplementedError

    @staticmethod
    def from_event(event: Event) -> "SatelliteDisconnected":
        raise NotImplementedError
