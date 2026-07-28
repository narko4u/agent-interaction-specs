# Agent Interaction Specs — Open Standards Stack

**ACI** | **AIP** | **AJSON**

An open standards stack for autonomous agent interaction, governance, and evidence.

## What's Here

- **ACI** — Agent Interaction Specification: agent manifest schema and validation library
  - `aci/py/` — Python package (`pip install aci-spec`)
  - Schema: `agent_name`, `version`, `capabilities`, `constraints`

- **AIP** — Agent Interaction Protocol: receipt chain and interaction record types
  - `aip/go/` — Go module (`go get github.com/empirelabs/aip`)
  - Types: `AgentReceipt`, `ActionRecord`, `ReceiptChain`, `Capability`

- **AJSON** — Agent JSON Notation: superset of JSON for agent manifests and interaction records

## Quick Start

```python
from aci import SpecValidator

v = SpecValidator()
manifest = v.validate_manifest({
    "agent_name": "my-agent",
    "version": "1.0.0",
    "capabilities": ["web", "code"],
    "constraints": {"max_tokens": 16000}
})
```

```go
import "github.com/empirelabs/aip"

receipt := aip.AgentReceipt{
    AgentName:   "my-agent",
    ActionType:  "execute",
    Status:      "allowed",
    EvidenceE3:  "sha256:abc...",
}
```

## License

MIT — Empire Labs Pty Ltd

[www.empirelabs.com.au](https://www.empirelabs.com.au)
