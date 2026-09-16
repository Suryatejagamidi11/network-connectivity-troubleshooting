# 01 — Scope & Objectives

[⬅ Back to README](../README.md)

This project covers access-layer copper and fiber connectivity between end devices (servers, ToR switches) and the distribution layer — it does not cover routing protocol troubleshooting, firewall rules, or WAN circuits, which are separate disciplines.

## Objectives

| Objective | Target |
| --- | --- |
| Diagnose a reported connectivity issue to root cause | Under 20 minutes for access-layer issues, following the methodology |
| Validate every newly cabled switch port before go-live | 100% of new ports checked against the validation procedure |
| Reduce repeat tickets caused by unresolved root cause | No repeat ticket on the same port within 30 days |
| Standardize documentation so any technician can pick up a ticket | Every ticket logged with symptom, layer isolated, root cause, and fix |

## Equipment in Scope

- Cisco Catalyst-class access switches (commands in this project use Cisco IOS syntax as the reference platform; the same steps translate to other vendors' equivalents)
- Cat6A copper and OM4 fiber cabling
- The cable testers and port validation tools listed in [05-tools-commands-reference.md](05-tools-commands-reference.md)
