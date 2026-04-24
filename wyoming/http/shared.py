"""Shared code for HTTP servers."""

import argparse
from pathlib import Path
from typing import Union

from flask import Flask, jsonify, redirect, request
from swagger_ui import flask_api_doc  # pylint: disable=no-name-in-module

from wyoming.client import AsyncClient
from wyoming.info import Describe, Info


def get_argument_parser() -> argparse.ArgumentParser:
    """Create argument parser with shared arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", default="0.0.0.0")
    parser.add_argument("--port", type=int, default=5000)
    parser.add_argument("--uri", help="URI of Wyoming service")
    parser.add_argument(
        "--debug", action="store_true", help="Print DEBUG logs to console"
    )
    return parser


def get_app(
    name: str, openapi_config_path: Union[str, Path], args: argparse.Namespace
) -> Flask:
    """Create Flask app with default endpoints."""

    app = Flask(name)

    @app.route("/")
    def redirect_to_api():
        pass

    @app.route("/api/info", methods=["GET"])
    async def api_info():
        pass

    @app.errorhandler(Exception)
    async def handle_error(err):
        """Return error as text."""
        pass

    flask_api_doc(
        app, config_path=str(openapi_config_path), url_prefix="/api", title="API doc"
    )

    return app
