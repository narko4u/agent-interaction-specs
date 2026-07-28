"""Agent Capability Interface (ACI) — open standard for agent capability discovery."""

__version__ = "1.0.0"
VERSION = __version__

from .schema import MANIFEST_SCHEMA, SpecValidator

__all__ = ["VERSION", "MANIFEST_SCHEMA", "SpecValidator"]
