"""HTTP server for wake word detection."""

import io
import logging
import wave
from pathlib import Path
from typing import Set

from flask import Response, jsonify, request

from wyoming.audio import wav_to_chunks
from wyoming.client import AsyncClient
from wyoming.error import Error
from wyoming.wake import Detect, Detection, NotDetected

from .shared import get_app, get_argument_parser

_DIR = Path(__file__).parent
CONF_PATH = _DIR / "conf" / "wake.yaml"


def main():
    async def api_wake():
        raise NotImplementedError

    raise NotImplementedError


if __name__ == "__main__":
    main()
