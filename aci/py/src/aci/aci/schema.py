"""ACI manifest schema definitions."""

MANIFEST_SCHEMA = {
    "agent_name": str,
    "version": str,
    "capabilities": list,
    "constraints": dict,
}
"""Required fields and their expected Python types for an ACI agent manifest."""
