# 05 — Tools & Commands Reference

[⬅ Back to README](../README.md)

## Switch CLI (Cisco IOS syntax; equivalents exist on other platforms)

| Command | Purpose |
| --- | --- |
| `show interface status` | Quick view of all ports: up/down, VLAN, speed/duplex |
| `show interface <port>` | Detailed stats for one port: errors, speed, duplex, load |
| `show interface <port> counters errors` | CRC, runts, giants, collisions on one port |
| `show interface <port> switchport` | VLAN mode, access/trunk VLAN assignment |
| `show vlan brief` | VLAN-to-port mapping across the switch |
| `show spanning-tree interface <port>` | STP role and state (forwarding/blocking/err-disabled) |
| `show port-security interface <port>` | Port security status, MAC count, violation mode |
| `show mac address-table interface <port>` | Which MAC(s) the switch sees on a port — useful for confirming the right device is even plugged in |

## Host-Side Tools

`ping`, `traceroute` / `tracert`, `arp -a`, `ipconfig` / `ifconfig` — used to confirm IP configuration before assuming the network is at fault.

## Hardware Tools

- Cable certifier (e.g., Fluke DSX series) for copper Cat6A certification
- OTDR or light-source/power-meter kit for fiber loss budget testing
- Basic tone/probe kit for tracing an unlabeled run back to its origin

## Field Rule

Host-side checks (`ipconfig`, `ping` to loopback) take 30 seconds and rule out half of "network is down" tickets that are actually a host misconfiguration — always run these before touching the switch.
