# Agent Interaction Specs — Open Standards Stack

**ACI** | **AIP** | **AJSON**

An open standards stack for autonomous agent interaction, governance, and evidence.

> 🌐 **Landing page:** [https://narko4u.github.io/agent-interaction-specs/](https://narko4u.github.io/agent-interaction-specs/)

## What's Here

- **ACI** — Agent Interaction Specification: agent manifest schema and validation library
  - `aci/py/` — Python package (`pip install aci-spec`)
  - Schema: `agent_name`, `version`, `capabilities`, `constraints`

- **AIP** — Agent Interaction Protocol: receipt chain and interaction record types
  - `aip/go/` — Go module (`go get github.com/narko4u/agent-interaction-specs/aip`)
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
import "github.com/narko4u/agent-interaction-specs/aip"

receipt := aip.AgentReceipt{
    AgentName:   "my-agent",
    ActionType:  "execute",
    Status:      "allowed",
    EvidenceE3:  "sha256:abc...",
}
```

---

## Acknowledgements

This repository packages the Agent Interaction Specifications - the Python `aci`
package and the Go `aip` package.

Neither has third-party runtime dependencies: `aci/py` uses the Python standard
library, and `aip/go` uses the Go standard library. There is therefore no
upstream code to attribute.

Both specifications are original work by Empire Labs Pty Ltd and have not been
reviewed, approved or certified by any standards body.

---

## License

MIT — Empire Labs Pty Ltd

[www.empirelabs.com.au](https://www.empirelabs.com.au)


---

<sub>Part of the [WitnessOS launch family](https://github.com/narko4u/witnessos): [eu-ai-act-compliance-grade](https://github.com/narko4u/eu-ai-act-compliance-grade) · [witnessos-verifier](https://github.com/narko4u/witnessos-verifier) · [agent-interaction-specs](https://github.com/narko4u/agent-interaction-specs) · [aci-spec](https://github.com/narko4u/aci-spec) · [aip-spec](https://github.com/narko4u/aip-spec) · [ajson](https://github.com/narko4u/ajson) — [Empire Labs Pty Ltd](https://www.empirelabs.com.au)</sub>