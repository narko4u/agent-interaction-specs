# AIP — Agent Interaction Protocol

**Version:** 0.9 (draft)

AIP is the action protocol layer. Once an agent discovers capabilities via ACI, it invokes them via AIP — structured HTTP requests with identity, authorisation, and audit hooks built in.

## Registry

- **Go Module:** `github.com/narko4u/agent-interaction-specs/aip`
- **Repo source:** [`narko4u/witnessos`](https://github.com/narko4u/witnessos) (AIP spec lives inside the WitnessOS repository)

## Core Concepts

- **Structured actions** — each action carries identity, intent, and payload
- **Exact-approval binding** — actions requiring human oversight are held pending until approved
- **Event model** — every action produces immutable, hash-chained events
- **Provider integration** — standard dispatch to Gmail, Stripe, and extensible connectors

## Spec

The specification is in `spec/aip-spec.md`. Current coverage:

- Request/response envelope
- Action lifecycle (requested → evaluated → approved/denied → dispatched → confirmed)
- Receipt format with cryptographic chain
- Error model
