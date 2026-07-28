"""Agent Interaction Specification (ACI) — schema and validation tools."""

from aci.schema import MANIFEST_SCHEMA

VERSION = "0.1.0"


class SpecValidationError(Exception):
    """Raised when a manifest fails validation against the schema."""

    pass


class SpecValidator:
    """Validates ACI agent manifests against the MANIFEST_SCHEMA."""

    @staticmethod
    def validate_manifest(manifest: dict) -> dict:
        """Validate an agent manifest dict against the schema.

        Parameters
        ----------
        manifest : dict
            The agent manifest to validate.

        Returns
        -------
        dict
            The validated manifest (unchanged) on success.

        Raises
        ------
        SpecValidationError
            If the manifest is missing required fields or has invalid types.
        """
        if not isinstance(manifest, dict):
            raise SpecValidationError("Manifest must be a dict")

        for field, expected_type in MANIFEST_SCHEMA.items():
            if field not in manifest:
                raise SpecValidationError(f"Missing required field: '{field}'")
            value = manifest[field]
            if expected_type is list and not isinstance(value, list):
                raise SpecValidationError(
                    f"Field '{field}' must be a list, got {type(value).__name__}"
                )
            elif expected_type is dict and not isinstance(value, dict):
                raise SpecValidationError(
                    f"Field '{field}' must be a dict, got {type(value).__name__}"
                )
            elif expected_type is str and not isinstance(value, str):
                raise SpecValidationError(
                    f"Field '{field}' must be a string, got {type(value).__name__}"
                )

        return manifest


__all__ = ["VERSION", "SpecValidator", "SpecValidationError", "MANIFEST_SCHEMA"]
