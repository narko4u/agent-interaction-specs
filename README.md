# Agent Interaction Specs

**Open standards for autonomous AI agent communication and governance.**

A three-layer specification stack that lets agents discover, invoke, and document their capabilities — regardless of platform, provider, or jurisdiction.

```
┌───────────────────────────────────────────────────────┐
│                **AJSON Spec**                         │
│  Agent JSON — manifest & message format               │
│  "How agents describe themselves"                     │
│  `pip install ajson-spec`                             │
├───────────────────────────────────────────────────────┤
│                    **AIP**                             │
│  Agent Interaction Protocol — HTTP + event model      │
│  "How agents talk to each other"                      │
│  `go get github.com/empirelabs/aip`                  │
├───────────────────────────────────────────────────────┤
│                    **ACI**                             │
│  Agent Interaction Capabilities — discovery schema    │
│  "What agents can do"                                 │
│  `pip install aci-spec`                               │
└───────────────────────────────────────────────────────┘
```

---

## The Stack

| Layer | What It Does | Reference Implementation | Status |
|-------|-------------|------------------------|--------|
| **ACI** | Capability discovery — agents publish what they can do | Python (`aci-spec` on PyPI) | Active |
| **AIP** | Action protocol — agents invoke capabilities via structured HTTP | Go (`github.com/empirelabs/aip`) | Active |
| **AJSON Spec** | Manifest format — agent identity, boundaries, and state | Python (`ajson-spec` on PyPI) | [Active](https://github.com/narko4u/ajson) |

Each layer is independently usable. Together they form a complete stack for agent-to-agent interaction with built-in audit and governance hooks.

---

## Why This Exists

Current LLM agents are black boxes. They have no standard way to:

- **Declare capabilities** — "I can send emails, process refunds, and query databases"
- **Authenticate** — "I am agent X, operated by Y, authorised to do Z"
- **Enforce boundaries** — "This action requires human approval before execution"
- **Evidence generation** — "Here is the cryptographically signed chain of events for every action I took"

ACI, AIP, and AJSON solve this. They are the interoperability layer that turns autonomous agents from opaque scripts into auditable, governable systems.

---

## Repository Structure

```
agent-interaction-specs/
├── aci/
│   ├── spec/              # ACI specification documents
│   ├── py/                # Python reference implementation
│   └── tests/             # Conformance tests
├── aip/
│   ├── spec/              # AIP specification documents
│   ├── go/                # Go reference implementation
│   └── tests/             # Conformance tests
├── LICENSE
└── README.md
```

**AJSON Spec** lives in its own [standalone repository](https://github.com/narko4u/ajson) — it is a data format with no runtime dependencies, usable in any agent system. Install via `pip install ajson-spec`.

---

## Quick Start

```bash
# Clone the whole stack
git clone https://github.com/narko4u/agent-interaction-specs
cd agent-interaction-specs

# Python ACI reference implementation
pip install aci-spec

# Go AIP reference implementation
go get github.com/empirelabs/aip

# Python AJSON Spec reference implementation
pip install ajson-spec
```

---

## Governance & Compliance

These specifications are the open foundation for **WitnessOS** — the enterprise enforcement gateway that uses ACI, AIP, and AJSON to generate verifiable compliance evidence.

- Standards alignment: NSA MCP, EU AI Act, NIST CAISI, Singapore AI Verify
- Evidence grades: E0 (raw) → E4 (independently verifiable)
- Cryptographic chain: every action leaves a signed, hash-chained receipt

---

## Contributing

This is an early-stage open standard. Contributions are welcome — spec clarifications, new language implementations, conformance tests, and bug reports.

See the individual spec directories for contribution guidelines.

---

**Empire Labs Pty Ltd** · [empirelabs.com.au](https://www.empirelabs.com.au) · contact@empirelabs.com.au
