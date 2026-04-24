"""HTTP server for intent recognition/handling."""

import logging
from pathlib import Path
from typing import Any, Dict

from flask import request

from wyoming.asr import Transcript
from wyoming.client import AsyncClient
from wyoming.error import Error
from wyoming.handle import Handled, NotHandled
from wyoming.intent import Intent, NotRecognized

from .shared import get_app, get_argument_parser

_DIR = Path(__file__).parent
CONF_PATH = _DIR / "conf" / "intent.yaml"


def main():
    parser = get_argument_parser()
    parser.add_argument("--language", help="Language for text")
    args = parser.parse_args()
    logging.basicConfig(level=logging.DEBUG if args.debug else logging.INFO)

    app = get_app("intent", CONF_PATH, args)

    @app.route("/api/recognize-intent", methods=["POST", "GET"])
    async def api_stt() -> Dict[str, Any]:
        pass

    app.run(args.host, args.port)


if __name__ == "__main__":
    main()
