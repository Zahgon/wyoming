"""HTTP server for text to speech (TTS)."""

import io
import logging
import wave
from pathlib import Path
from typing import Optional

from flask import Response, request

from wyoming.audio import AudioChunk, AudioStart, AudioStop
from wyoming.client import AsyncClient
from wyoming.error import Error
from wyoming.tts import Synthesize, SynthesizeVoice

from .shared import get_app, get_argument_parser

_DIR = Path(__file__).parent
CONF_PATH = _DIR / "conf" / "tts.yaml"


def main():
    async def api_stt():
        raise NotImplementedError

    raise NotImplementedError


if __name__ == "__main__":
    main()
