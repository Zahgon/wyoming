"""Implement a tiny subset of dataclasses_json for config."""

from collections.abc import Mapping, Sequence
from dataclasses import asdict, fields, is_dataclass
from typing import Any, Dict, Type


class DataClassJsonMixin:
    """Adds from_dict to dataclass."""

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> Any:
        """Parse dataclasses recursively."""
        raise NotImplementedError

    def to_dict(self) -> Dict[str, Any]:
        """Alias for asdict."""
        raise NotImplementedError


def _decode(value: Any, target_type: Type) -> Any:
    """Decode value using (possibly generic) type."""
    raise NotImplementedError


def _is_optional(target_type: Type):
    """True if type is Optional"""
    raise NotImplementedError
