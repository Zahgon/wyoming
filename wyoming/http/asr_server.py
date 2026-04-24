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
    parser = get_argument_parser()
    parser.add_argument("--model", help="Default model name for transcription")
    parser.add_argument("--language", help="Default language for transcription")
    parser.add_argument("--samples-per-chunk", type=int, default=1024)
    args = parser.parse_args()
    logging.basicConfig(level=logging.DEBUG if args.debug else logging.INFO)

    app = get_app("asr", CONF_PATH, args)

    @app.route("/api/speech-to-text", methods=["POST"])
    async def api_stt() -> Response:
        pass

    app.run(args.host, args.port)


if __name__ == "__main__":
    main()
