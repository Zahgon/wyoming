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
    async def api_stt():
        raise NotImplementedError

    raise NotImplementedError


if __name__ == "__main__":
    main()
