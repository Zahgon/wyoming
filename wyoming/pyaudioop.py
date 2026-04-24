"""Partial implementation of the deprecated audioop module.

Only supports:
  - widths 1, 2, and 4
  - signed samples
  - tomono, tostereo, lin2lin, ratecv
"""

import math
import struct
from typing import Final, List, Optional, Tuple, Union

BufferType = Union[bytes, bytearray]
State = Tuple[int, Tuple[Tuple[int, ...], ...]]

# width = (_, 1, 2, _, 4)
_MAX_VALS: Final = [0, 0x7F, 0x7FFF, 0, 0x7FFFFFFF]
_MIN_VALS: Final = [0, -0x80, -0x8000, 0, -0x80000000]
_SIGNED_FORMATS: Final = ["", "b", "h", "", "i"]
_UNSIGNED_FORMATS: Final = ["", "B", "H", "", "I"]


def check_size(size: int) -> None:
    raise NotImplementedError


def check_parameters(fragment_length: int, size: int) -> None:
    raise NotImplementedError


def fbound(val: float, min_val: float, max_val: float) -> int:
    raise NotImplementedError


def tomono(
    fragment: BufferType, width: int, lfactor: float, rfactor: float
) -> BufferType:
    raise NotImplementedError


def tostereo(
    fragment: BufferType, width: int, lfactor: float, rfactor: float
) -> BufferType:
    raise NotImplementedError


def _get_sample32(fragment: BufferType, width: int, index: int) -> int:
    raise NotImplementedError


def _set_sample32(fragment: bytearray, width: int, index: int, sample: int) -> None:
    raise NotImplementedError


def lin2lin(fragment: BufferType, width: int, new_width: int) -> BufferType:
    raise NotImplementedError


def ratecv(
    fragment: BufferType,
    width: int,
    nchannels: int,
    inrate: int,
    outrate: int,
    state: Optional[State],
    weightA: int = 1,
    weightB: int = 0,
) -> Tuple[bytearray, Optional[State]]:
    raise NotImplementedError
