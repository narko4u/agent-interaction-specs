# ACI Spec

Agent Interaction Specification — schema and validation for ACI agent manifests.

## Usage

```python
from aci import SpecValidator, VERSION

validator = SpecValidator()
manifest = {
    "agent_name": "my-agent",
    "version": "1.0.0",
    "capabilities": ["tool_use", "memory"],
    "constraints": {"max_tokens": 4096},
}
validator.validate_manifest(manifest)  # returns manifest on success
```
