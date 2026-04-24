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
    parser = get_argument_parser()
    parser.add_argument("--voice", help="Default voice for synthesis")
    parser.add_argument("--speaker", help="Default voice speaker for synthesis")
    args = parser.parse_args()
    logging.basicConfig(level=logging.DEBUG if args.debug else logging.INFO)

    app = get_app("tts", CONF_PATH, args)

    @app.route("/api/text-to-speech", methods=["POST", "GET"])
    async def api_stt() -> Response:
        pass

    app.run(args.host, args.port)


if __name__ == "__main__":
    main()
