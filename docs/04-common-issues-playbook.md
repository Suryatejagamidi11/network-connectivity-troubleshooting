# 04 — Common Connectivity Issues & Resolution Playbook

[⬅ Back to README](../README.md)

| Symptom | Likely cause | Resolution |
| --- | --- | --- |
| Link light off, no connectivity | Bad cable, bad port, or NIC disabled | Swap cable to known-good; if still down, test cable with certifier; move to spare port to isolate switch vs. cable vs. NIC |
| Link up but intermittent drops, climbing CRC errors | Duplex mismatch or damaged cable | Force speed/duplex to match on both ends, or replace cable if certifier shows a fault |
| Device gets an IP but can't reach anything | Wrong VLAN assignment | Check `show interface switchport`; correct access VLAN to match design |
| Port suddenly shows err-disabled | Port security violation (MAC limit exceeded) or storm control trip | `show port-security interface`; clear violation and `shutdown` / `no shutdown` to recover **after** root cause is fixed, not before |
| Traffic loops, broadcast storm, ports flapping | Spanning-tree misconfiguration or accidental loop (both ends of a cable patched into the same switch) | Check `show spanning-tree interface` for blocking state; trace and remove the physical loop |
| Works at the desk, fails after a rack move | Cable run exceeds category/fiber loss budget after re-routing | Re-certify the run; a run that passed at 90m may fail after added slack or bends near limits |
| One VLAN works, another doesn't, same trunk port | Trunk's allowed-VLAN list doesn't include the new VLAN | `show interface trunk`; add the VLAN to the allowed list on both ends of the trunk |

This table is the first stop on a new ticket — most access-layer issues match one of these seven rows, and the [methodology](02-troubleshooting-methodology.md) is what confirms which one before applying a fix.
