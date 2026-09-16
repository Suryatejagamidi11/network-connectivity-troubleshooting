# 06 — Documentation & Escalation Standards

[⬅ Back to README](../README.md)

Every ticket is logged with five fields, filled in as the ticket is worked rather than reconstructed afterward: **symptom reported**, **layer isolated** (from the [methodology table](02-troubleshooting-methodology.md)), **root cause**, **fix applied**, and **verification step** used to confirm it's resolved.

## Escalation Path

![Escalation Path](../diagrams/escalation-path.png)

- **Level 1 (self-resolve):** physical layer and straightforward data-link issues — bad cable, duplex mismatch, wrong VLAN on an access port. Expected resolution inside the methodology's steps 1-5.
- **Level 2 (escalate):** issues that trace past the access switch — distribution/core routing, firewall rules, DHCP scope exhaustion — escalated once steps 1-6 confirm the access layer is clean, with the ticket log attached so the next technician isn't starting over.
- **Level 3 (change control):** anything requiring a config change outside a standard fix (new VLAN creation, trunk changes affecting other ports, spanning-tree topology changes) goes through change control rather than being pushed live during a live ticket.

The [validation checklist](08-validation-checklist.md) and the ticket log use the same field names, so a completed validation record doubles as the documentation for a new-port ticket — no separate paperwork for the same information.
