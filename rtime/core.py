# AUTOGENERATED! DO NOT EDIT! File to edit: 00_core.ipynb (unless otherwise specified).

__all__ = ['UtcTime', 'LocalTime', 'PosixTime', 'MILLIS_IN_A_SECOND', 'MICROS_IN_A_MILLI', 'timestamp', 'to_utc',
           'to_local']

# Cell
import datetime
import time
from typing import cast, NewType

# Cell
UtcTime = NewType("UtcTime", datetime.datetime)
LocalTime = NewType("LocalTime", datetime.datetime)
PosixTime = NewType("PosixTime", int)
MILLIS_IN_A_SECOND = 1000
MICROS_IN_A_MILLI = 1000

# Internal Cell
def _seconds_to_posix(seconds: float) -> PosixTime:
    """Convert the seconds to a PosixTime."""
    return cast(PosixTime, int(MILLIS_IN_A_SECOND * seconds))

# Cell
def timestamp() -> PosixTime:
    """Return the current Posix time in milliseconds."""
    return _seconds_to_posix(seconds=time.time())

# Cell
def to_utc(timestamp: PosixTime) -> UtcTime:
    """Convert a timestamp to utc time."""
    seconds = timestamp / MILLIS_IN_A_SECOND
    dt = datetime.datetime.fromtimestamp(seconds, datetime.timezone.utc)
    return cast(UtcTime, dt)

# Cell
def to_local(timestamp: PosixTime) -> LocalTime:
    """Convert the timestamp to a time in the local timezone."""
    return cast(LocalTime, to_utc(timestamp=timestamp).astimezone())