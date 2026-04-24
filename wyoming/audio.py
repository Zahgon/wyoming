"""Audio input/output."""

import argparse
import io
import sys
import wave
from dataclasses import dataclass
from typing import Iterable, Optional, Union

try:
    # Use built-in audioop until it's removed in Python 3.13
    import audioop  # pylint: disable=deprecated-module
except ImportError:
    from . import pyaudioop as audioop  # type: ignore[no-redef]

from .event import Event, Eventable
from .util.dataclasses_json import DataClassJsonMixin

_CHUNK_TYPE = "audio-chunk"
_START_TYPE = "audio-start"
_STOP_TYPE = "audio-stop"


@dataclass
class AudioFormat(DataClassJsonMixin):
    """Base class for events with audio format information."""

    rate: int
    """Hertz"""

    width: int
    """Bytes"""

    channels: int
    """Mono = 1"""


@dataclass
class AudioChunk(AudioFormat, Eventable):
    """Chunk of raw PCM audio."""

    audio: bytes
    """Raw audio"""

    timestamp: Optional[int] = None
    """Milliseconds"""

    @staticmethod
    def is_type(event_type: str) -> bool:
        raise NotImplementedError

    def event(self) -> Event:
        raise NotImplementedError

    @staticmethod
    def from_event(event: Event) -> "AudioChunk":
        raise NotImplementedError

    @property
    def samples(self) -> int:
        pass

    @property
    def seconds(self) -> float:
        pass

    @property
    def milliseconds(self) -> int:
        pass


@dataclass
class AudioStart(AudioFormat, Eventable):
    """Audio stream has started."""

    timestamp: Optional[int] = None
    """Milliseconds"""

    @staticmethod
    def is_type(event_type: str) -> bool:
        raise NotImplementedError

    def event(self) -> Event:
        raise NotImplementedError

    @staticmethod
    def from_event(event: Event) -> "AudioStart":
        raise NotImplementedError


@dataclass
class AudioStop(Eventable):
    """Audio stream has stopped."""

    timestamp: Optional[int] = None
    """Milliseconds"""

    @staticmethod
    def is_type(event_type: str) -> bool:
        raise NotImplementedError

    def event(self) -> Event:
        raise NotImplementedError

    @staticmethod
    def from_event(event: Event) -> "AudioStop":
        raise NotImplementedError


@dataclass
class AudioChunkConverter:
    """Converts audio chunks using audioop/pyaudioop."""

    rate: Optional[int] = None
    width: Optional[int] = None
    channels: Optional[int] = None
    _ratecv_state = None

    def convert(self, chunk: AudioChunk) -> AudioChunk:
        """Converts sample rate, width, and channels as necessary."""
        raise NotImplementedError


def wav_to_chunks(
    wav_file: wave.Wave_read,
    samples_per_chunk: int,
    timestamp: int = 0,
    start_event: bool = False,
    stop_event: bool = False,
) -> Iterable[Union[AudioStart, AudioChunk, AudioStop]]:
    """Splits WAV file into AudioChunks."""
    raise NotImplementedError


# -----------------------------------------------------------------------------


def main() -> None:
    raise NotImplementedError


if __name__ == "__main__":
    main()
