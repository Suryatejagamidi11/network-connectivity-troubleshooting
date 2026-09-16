# 08 — Sample Switch Port Validation Checklist

[⬅ Back to README](../README.md)

A field-ready version of the [validation procedure](03-switch-port-validation-procedure.md), filled in per port and attached to the ticket or handoff record.

- [ ] Port ID confirmed (matches `<Row>-<Rack>-<RU>-<Port>` label on both ends)
- [ ] Physical link light on, `show interface status` = connected
- [ ] Speed/duplex matches design, no auto-negotiation mismatch
- [ ] VLAN assignment correct (`show interface switchport`)
- [ ] Port security status clean, no violations (`show port-security interface`, if configured)
- [ ] Error counters at zero after settle period (`show interface counters errors`)
- [ ] Spanning-tree state = forwarding (`show spanning-tree interface`)
- [ ] Cable certified to category/loss-budget spec (copper: Cat6A certifier; fiber: OTDR/power meter)
- [ ] End-to-end ping test passes, 0% loss over 2 minutes
- [ ] Result logged: symptom (if applicable) / layer isolated / root cause / fix / verification

A port isn't marked ready-for-production until every box is checked — this is the same discipline applied to every rack going live in the capacity expansion project's Phase 2 and Phase 3 cutovers.
