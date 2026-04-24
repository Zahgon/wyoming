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
    raise NotImplementedError


def get_app(
    name: str, openapi_config_path: Union[str, Path], args: argparse.Namespace
) -> Flask:
    """Create Flask app with default endpoints."""

    def redirect_to_api():
        raise NotImplementedError

    async def api_info():
        raise NotImplementedError

    async def handle_error(err):
        raise NotImplementedError

    raise NotImplementedError
