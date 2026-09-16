# 03 — Switch Port Validation Procedure

[⬅ Back to README](../README.md)

Run on every newly cabled port before it's handed off for production traffic — this is the same check applied to every rack in the [capacity expansion project's](https://github.com/Suryatejagamidi11/data-center-capacity-expansion-plan) Row 5 and Row 6 build-out before cutover.

| Check | Command / method | Expected result |
| --- | --- | --- |
| Physical link | Visual + `show interface status` | Port shows `connected`, not `notconnect` or `disabled` |
| Speed/duplex | `show interface <port>` | Matches design (e.g., 1000/full); no "a-half" auto-negotiated duplex on a gigabit link |
| VLAN assignment | `show interface <port> switchport` | Access VLAN or trunk allowed-VLAN list matches the port's design intent |
| Port security (if configured) | `show port-security interface <port>` | Status not err-disabled, MAC count within configured max |
| Error counters | `show interface <port> counters errors` | Zero or near-zero CRC/input errors after a settle period |
| Cable certification | Fluke (or equivalent) cable certifier for copper; OTDR/light-source-power-meter for fiber | Passes category rating (Cat6A) or fiber loss budget |
| Label verification | Visual, both ends | Matches the `<Row>-<Rack>-<RU>-<Port>` format from the cabling standard |
| End-to-end test | `ping` from the connected device to its default gateway | Sustained ping, 0% loss over a 2-minute test |

Any check that fails stops the handoff — the port is not marked ready until every row above passes, and the failure plus fix is logged per [06-documentation-escalation.md](06-documentation-escalation.md).

See also: [08-validation-checklist.md](08-validation-checklist.md) for the field-ready, per-port checklist version of this procedure.
