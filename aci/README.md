# ACI — Agent Interaction Capabilities

**Version:** 0.9 (draft)

Agents publish a `/.well-known/aci/capabilities.json` endpoint describing what they can do. ACI is the discovery layer: a standard schema that answers "what capabilities does this agent expose?"

## Registry

- **PyPI:** `aci-spec`
- **Repo source:** [`narko4u/witnessos`](https://github.com/narko4u/witnessos) (ACI spec lives inside the WitnessOS repository)

## Core Concepts

- **Capability discovery** — agents advertise actions, connectors, evidence grades, and auth methods
- **Self-describing** — no prior agreement needed between agents
- **Discoverable** — standard well-known endpoint pattern

## Spec

The specification is in `spec/aci-spec.md`. Current coverage:

- Action types (evaluate, approve, deny, revoke)
- Connectors (gmail, stripe, robot)
- Evidence grades (E0–E4)
- Auth methods (HMAC, DPoP, Unix socket)
