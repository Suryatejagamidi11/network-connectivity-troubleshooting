# 02 — Troubleshooting Methodology

[⬅ Back to README](../README.md)

Every ticket is worked bottom-up through the OSI model rather than jumping straight to "restart the app" — each layer is confirmed good before moving to the next, so time isn't spent debugging Layer 3 routing when the real problem is a bad patch cable.

![Troubleshooting Methodology](../diagrams/troubleshooting-methodology.png)

| Step | Layer | Check | Pass criteria |
| --- | --- | --- | --- |
| 1 | Physical | Link light on NIC and switch port; cable seated; cable tester if link is down | Link light solid, no continuity faults |
| 2 | Physical | `show interface status` — port up/up, correct speed/duplex | Status = connected, no duplex mismatch |
| 3 | Data Link | `show interface counters errors` — CRC, collisions, runts | Error counters not climbing |
| 4 | Data Link | VLAN assignment matches design (`show vlan brief`, `show interface switchport`) | Port in intended VLAN, correct trunk/access mode |
| 5 | Data Link | Spanning-tree state (`show spanning-tree interface`) | Port in forwarding state, not blocking/err-disabled |
| 6 | Network | IP config, gateway reachability (`ping`, `arp -a`) | Host has correct IP, can reach default gateway |
| 7 | Network | End-to-end path (`traceroute`) if gateway is reachable but destination isn't | Path resolves without unexpected drops |

A ticket is not closed at "traffic passes now" — it's closed once the layer that actually failed is identified and logged (see [06-documentation-escalation.md](06-documentation-escalation.md)), since an unidentified root cause is how the same port generates a repeat ticket in two weeks.
