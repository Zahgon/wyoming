"""HTTP server for automated speech recognition (ASR)."""

import io
import logging
import wave
from pathlib import Path

from flask import Response, jsonify, request

from wyoming.asr import Transcribe, Transcript
from wyoming.audio import wav_to_chunks
from wyoming.client import AsyncClient
from wyoming.error import Error

from .shared import get_app, get_argument_parser

_DIR = Path(__file__).parent
CONF_PATH = _DIR / "conf" / "asr.yaml"


def main():
    async def api_stt():
        raise NotImplementedError

    raise NotImplementedError


if __name__ == "__main__":
    main()
