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
    parser = get_argument_parser()
    parser.add_argument("--wake-word-name", action="append")
    parser.add_argument("--samples-per-chunk", type=int, default=1024)
    args = parser.parse_args()
    logging.basicConfig(level=logging.DEBUG if args.debug else logging.INFO)

    app = get_app("wake", CONF_PATH, args)

    @app.route("/api/detect-wake-word", methods=["POST", "GET"])
    async def api_wake() -> Response:
        pass

    app.run(args.host, args.port)


if __name__ == "__main__":
    main()
