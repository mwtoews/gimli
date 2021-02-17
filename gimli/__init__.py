import pkg_resources

from ._udunits2 import (
    Unit,
    UnitEncoding,
    UnitFormatting,
    UnitNameError,
    UnitStatus,
    UnitSystem,
)
from .errors import IncompatibleUnitsError

__version__ = pkg_resources.get_distribution("gimli").version
__all__ = [
    "IncompatibleUnitsError",
    "Unit",
    "UnitEncoding",
    "UnitFormatting",
    "UnitNameError",
    "UnitStatus",
    "UnitSystem",
]

del pkg_resources
